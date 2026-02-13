"""
Domain 4: Network Security Monitoring scenarios.

Key SOC concepts tested:
- C2 beaconing detection
- DNS exfiltration
- IDS/IPS alert analysis
- Traffic baseline deviation
- Lateral movement indicators
- Encrypted traffic metadata analysis
- Network anomaly detection
- Protocol analysis

Each scenario uses a single "standard" professional theme.
"""

SOC_DOMAIN_4_SCENARIOS = [
    # Scenario 1: C2 Beaconing Detection
    {
        "id": "soc4_c2_beaconing",
        "domain": 4,
        "themes": {
            "standard": {
                "title": "THE SUSPICIOUS HEARTBEAT",
                "narrative": """
During routine threat hunting, you notice an unusual pattern in your Zeek
connection logs. Workstation WKSTN-MKTG-017 has been making HTTPS connections
to an external IP with the following characteristics:

- Destination: 185.234.XX.XX (registered to a small hosting provider)
- Connections: Exactly every 60 seconds for the past 72 hours
- Session duration: 0.3-0.5 seconds each
- Bytes transferred: Consistently 247-312 bytes each direction
- SNI: "api.cloudmetrics.io" (legitimate-looking domain)
- Certificate: Valid certificate from Let's Encrypt

The user is a marketing coordinator with no known relationship with cloud
metrics providers. The workstation appears to function normally.

What is the MOST likely explanation for this traffic pattern?
                """,
                "choices": [
                    {"text": "Normal application telemetry - many apps phone home regularly"},
                    {"text": "C2 beaconing - the interval regularity indicates malware"},
                    {"text": "DNS over HTTPS (DoH) - the user configured privacy DNS"},
                    {"text": "Windows Update checks - Microsoft services check regularly"}
                ],
                "success_text": """
"C2 beaconing," you report. "The regularity is too precise for legitimate software."

Your analysis:
1. TIMING: Exactly 60-second intervals for 72+ hours. Human-initiated traffic varies;
   automated malware doesn't.
2. SIZE: Consistent byte counts suggest structured C2 protocol, not varied activity.
3. DESTINATION: Small hosting provider isn't typical for enterprise telemetry.
4. CONTEXT: Marketing coordinator with no cloud metrics relationship.

Your EDR team investigates and finds a fileless implant living in memory, using
legitimate Windows processes for network communication. The C2 server was using
domain fronting to appear as legitimate traffic.

The threat hunt discovered what the SIEM missed: a low-and-slow implant that had
been quietly beaconing for three days.

BEACONING INDICATORS: Perfect intervals (jitter <5%), consistent session sizes,
unusual geographic destinations, and no business justification.
                """,
                "failure_texts": {
                    0: """
Application telemetry does phone home, but with JITTER - randomized intervals to
avoid thundering herds and handle retries. "Exactly every 60 seconds for 72 hours"
is machine precision.

Legitimate telemetry also varies in payload size. Consistent byte counts suggest
a structured C2 protocol.

LESSON: Look for precision. Legitimate software has variance. Malware often doesn't.
                    """,
                    2: """
DNS over HTTPS doesn't create persistent connections every 60 seconds. DoH resolves
DNS queries on-demand based on browsing activity, not fixed intervals.

Also, DoH goes to known resolvers (Cloudflare, Google, Quad9), not obscure hosting
providers.

LESSON: Understand legitimate protocols. DoH patterns don't match this traffic.
                    """,
                    3: """
Windows Update doesn't check every 60 seconds - that would be absurdly aggressive.
WU checks are scheduled (typically daily) or user-initiated.

They also don't beacon with perfect intervals to foreign IPs with consistent
byte counts.

LESSON: Know your baseline. Windows Update has well-documented patterns - this isn't it.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
C2 beaconing indicators:
- Perfect timing intervals (low jitter)
- Consistent payload sizes
- Long duration patterns (days/weeks)
- Unusual destinations
- No business justification

Legitimate traffic has variance; malware often has precision.
        """,
        "domain_reference": "SOC Domain 4: Network Security - C2 Beaconing Detection"
    },

    # Scenario 2: DNS Exfiltration
    {
        "id": "soc4_dns_exfil",
        "domain": 4,
        "themes": {
            "standard": {
                "title": "THE SUSPICIOUS QUERIES",
                "narrative": """
Your DNS monitoring solution flags unusual activity. Workstation WKSTN-FIN-023
(financial analyst) is generating thousands of DNS queries to subdomains of
"update-service.net":

Sample queries (last 5 minutes):
- dXNlcm5hbWU6amRvZTtw.update-service.net
- YXNzd29yZDpQQHNzd29y.update-service.net
- ZDE7ZGF0YWJhc2U6ZmluYW5.update-service.net
- Y2lhbDtkYXRhOnEzX3Jldm.update-service.net

Characteristics:
- 500+ unique subdomain queries in 5 minutes
- Subdomain prefixes are 20-30 characters of seemingly random text
- All queries receive NXDOMAIN responses
- No legitimate business relationship with update-service.net

What type of attack are you MOST likely observing?
                """,
                "choices": [
                    {"text": "DNS tunneling for C2 communication"},
                    {"text": "DNS cache poisoning attack"},
                    {"text": "Domain Generation Algorithm (DGA) malware"},
                    {"text": "DNS exfiltration of encoded data"}
                ],
                "success_text": """
"DNS exfiltration," you identify. "Those subdomain prefixes are Base64-encoded
data being smuggled out through DNS queries."

You decode the samples:
- "dXNlcm5hbWU6amRvZTtw" decodes to "username:jdoe;p"
- "YXNzd29yZDpQQHNzd29y" decodes to "assword:P@sswor"
- "ZDE7ZGF0YWJhc2U6ZmluYW4" decodes to "d1;database:finan"

"They're exfiltrating credentials through DNS queries. The attacker's nameserver
for update-service.net logs every query - they don't need responses."

You escalate immediately. Network blocks go in place, the workstation is isolated,
and forensics begins. The attacker was using DNS because it's often allowed
outbound even from restricted networks.

EXFILTRATION INDICATOR: High volume of queries with Base64-like subdomain strings.
Data is encoded in the query itself - the attacker's DNS server captures it.
                """,
                "failure_texts": {
                    0: """
DNS tunneling requires RESPONSES to carry data back to the malware. These queries
are getting NXDOMAIN responses - there's no bidirectional data channel.

This is one-way: data encoded in queries, no meaningful responses. That's
exfiltration, not C2 tunneling.

LESSON: DNS tunneling uses queries AND responses. DNS exfiltration only needs queries.
                    """,
                    1: """
DNS cache poisoning injects false records into DNS caches. It doesn't generate
thousands of queries with encoded strings.

The workstation is SENDING these queries, not receiving poisoned responses.
Completely different attack pattern.

LESSON: Cache poisoning is about malicious RESPONSES. This is about suspicious
QUERIES.
                    """,
                    2: """
DGA malware generates random-LOOKING domains to contact C2 servers. But DGA tries
different BASE domains, and expects RESOLUTION.

These queries all go to subdomains of ONE domain (update-service.net), and the
attacker doesn't care about responses.

LESSON: DGA tries many random domains seeking resolution. Exfiltration encodes
data in subdomains of a known domain.
                    """
                }
            }
        },
        "correct_index": 3,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
DNS exfiltration:
1. Malware encodes data as subdomain: "ZGF0YQ==.attacker.com"
2. Query goes to attacker's authoritative nameserver
3. Nameserver logs the query (capturing the data)
4. Response doesn't matter - data already captured

Indicators: Base64 subdomains, high query volume, NXDOMAIN responses.
        """,
        "domain_reference": "SOC Domain 4: Network Security - DNS Exfiltration Detection"
    },

    # Scenario 3: IDS/IPS Alert Analysis
    {
        "id": "soc4_ids_analysis",
        "domain": 4,
        "themes": {
            "standard": {
                "title": "THE INTRUSION ALERT",
                "narrative": """
Your network IDS triggers a high-severity alert:

ALERT: ET EXPLOIT Possible Apache Struts OGNL Injection (CVE-2017-5638)
Source: 203.0.113.50 (External)
Destination: 10.1.50.25:8080 (DMZ web server)
Rule: alert http any any -> $HOME_NET 8080 (msg:"ET EXPLOIT..."; content:"%{";
      content:"getRuntime"; within:200;)

The alert triggered on a single packet. Your web application team says the server
runs Apache Struts. The source IP is from a cloud provider often used by
researchers and attackers alike.

What should your NEXT step be?
                """,
                "choices": [
                    {"text": "Block the source IP immediately at the perimeter firewall"},
                    {"text": "Verify if the web server is vulnerable to CVE-2017-5638"},
                    {"text": "Close as false positive - IDS signatures have high false positive rates"},
                    {"text": "Wait for additional alerts before investigating"}
                ],
                "success_text": """
"Verify vulnerability status," you correctly prioritize.

Your investigation:
1. CHECK APPLICATION: Is Apache Struts installed? What version?
2. VERIFY VULNERABILITY: Is CVE-2017-5638 patched?
3. REVIEW LOGS: Did the attack succeed? Check web server logs for execution.
4. THEN BLOCK: If vulnerable/exploited, then block and contain.

You find:
- Struts version: 2.3.31 (VULNERABLE to CVE-2017-5638)
- Web server logs: POST request with OGNL payload, followed by unusual process
  execution (cmd.exe spawned by Tomcat)
- The attack SUCCEEDED

Now you escalate: isolate the web server, block the IP, initiate incident response.

If you had just blocked the IP without investigating, you'd have:
- Missed that the server was already compromised
- Let the attacker continue through their existing access
- False sense of security

IDS ANALYSIS PRINCIPLE: Alerts tell you to INVESTIGATE, not what ACTION to take.
Verify the vulnerability and check for compromise before reactive blocking.
                """,
                "failure_texts": {
                    0: """
Blocking the IP addresses the scanner, not the vulnerability. If the attack already
succeeded, the attacker is INSIDE - blocking the scanner doesn't help.

Also, blocking IPs is trivial to bypass. The attacker uses a different IP and tries
again. Meanwhile, you don't know if you're already compromised.

LESSON: IP blocking is a symptom treatment, not a solution. Investigate first.
                    """,
                    2: """
"False positive" is a dangerous assumption for a specific CVE-based exploit alert
targeting a server that RUNS STRUTS.

If the signature matched on legitimate traffic, investigate WHY. If the signature
is for CVE-2017-5638 and you run Struts, this is HIGH PRIORITY.

LESSON: Don't dismiss high-fidelity alerts on vulnerable systems as false positives.
Investigate.
                    """,
                    3: """
"Wait for additional alerts" while an attacker potentially has code execution on
your web server?

This isn't a low-confidence behavior alert - this is a SPECIFIC EXPLOIT SIGNATURE
targeting a KNOWN VULNERABILITY on a POTENTIALLY VULNERABLE SYSTEM.

LESSON: High-fidelity exploit alerts require immediate investigation, not patience.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
IDS alert triage:
1. UNDERSTAND the alert - What vulnerability? What attack?
2. VERIFY the target - Is it vulnerable?
3. CHECK for success - Did the attack work?
4. RESPOND appropriately - Contain if compromised, patch if vulnerable

Alerts inform investigation, not immediate action.
        """,
        "domain_reference": "SOC Domain 4: Network Security - IDS/IPS Alert Analysis"
    },

    # Scenario 4: Traffic Baseline Deviation
    {
        "id": "soc4_baseline_deviation",
        "domain": 4,
        "themes": {
            "standard": {
                "title": "THE AFTER-HOURS SPIKE",
                "narrative": """
Your network monitoring shows unusual traffic at 3:00 AM:

Server: FILESRV-01 (Internal file server)
Normal baseline (business hours): 50-200 MB/hour outbound
Current traffic: 15 GB/hour outbound to 185.X.X.X
Protocol: HTTPS (port 443)
Destination: Cloud storage provider IP range

The server hosts financial documents and HR records. No scheduled backups run
at this time. No users should be accessing files at 3 AM.

What is your assessment?
                """,
                "choices": [
                    {"text": "Scheduled backup to cloud - check with IT for new backup jobs"},
                    {"text": "Normal file sync activity - cloud storage often syncs overnight"},
                    {"text": "Potential data exfiltration - the deviation is too extreme to ignore"},
                    {"text": "Network monitoring error - 15 GB/hour seems impossibly high"}
                ],
                "success_text": """
"Potential data exfiltration," you report. "This is a 75x deviation from baseline
to an unexpected destination during off-hours."

Your analysis:
- VOLUME: 15 GB/hour vs 50-200 MB baseline = 75-300x normal
- TIMING: 3 AM when no users are active
- DESTINATION: External cloud storage, not corporate backup infrastructure
- CONTENT: Server holds financial and HR data (high value targets)

You escalate and investigate:
1. Check for unauthorized access on the file server
2. Review what accounts are active
3. Examine which files are being accessed
4. Preserve network packet captures

Investigation reveals: An attacker gained access through a compromised service
account and is staging data to cloud storage for later retrieval.

If you had dismissed this as "probably backup," 15 GB of sensitive data would
have been exfiltrated.

BASELINE PRINCIPLE: Significant deviations from established baselines during
unusual times warrant investigation. "75x normal" is never normal.
                """,
                "failure_texts": {
                    0: """
"Check with IT" delays response. If this IS exfiltration, you're giving the
attacker time to complete.

Investigate WHILE checking with IT. Don't wait for confirmation that "there's
no backup job" while data flows out.

Also - backup jobs go to BACKUP INFRASTRUCTURE, not random cloud storage IPs.

LESSON: Investigate suspicious activity immediately. Verify in parallel, don't
wait.
                    """,
                    1: """
File sync happens during BUSINESS HOURS when users save files, not at 3 AM when
no one is working. And sync doesn't suddenly spike to 75x normal volume.

"Normal overnight sync" would show up in your BASELINE. This is a massive deviation
from baseline behavior.

LESSON: Baseline exists for a reason. 75x deviation during off-hours is not
"normal sync."
                    """,
                    3: """
15 GB/hour is completely achievable on modern networks. A gigabit connection can
move 450 GB/hour. Your file server certainly has the bandwidth.

Dismissing the alert as "impossible" means missing the exfiltration in progress.

LESSON: Trust your monitoring data. Investigate anomalies rather than dismissing
them as errors.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Baseline deviation analysis:
1. MAGNITUDE - How far from normal?
2. TIMING - Expected or unusual hours?
3. DESTINATION - Known infrastructure or unexpected?
4. CONTEXT - What data is on that system?

Significant deviations warrant investigation, not explanations.
        """,
        "domain_reference": "SOC Domain 4: Network Security - Traffic Baseline Deviation"
    },

    # Scenario 5: Lateral Movement Detection
    {
        "id": "soc4_lateral_movement",
        "domain": 4,
        "themes": {
            "standard": {
                "title": "THE INTERNAL SCAN",
                "narrative": """
Your network monitoring detects unusual internal traffic from a workstation:

Source: WKSTN-DEV-042 (Developer workstation)
Activity (last 30 minutes):
- 847 SMB connection attempts to various internal IPs
- 312 successful connections
- 535 "Access Denied" failures
- Connections span multiple subnets (HR, Finance, Executive, Server)

The developer normally only connects to development servers and their team's
file share. This activity is completely outside their normal pattern.

What does this traffic pattern indicate?
                """,
                "choices": [
                    {"text": "Developer running an authorized network scan for a security project"},
                    {"text": "Misconfigured software trying to find network resources"},
                    {"text": "Lateral movement - compromised workstation probing the network"},
                    {"text": "Active Directory group policy pushing updates to systems"}
                ],
                "success_text": """
"Lateral movement," you assess. "This is a compromised workstation scanning the
internal network for accessible shares."

Your analysis:
- 847 SMB attempts in 30 minutes = aggressive network enumeration
- Mix of successes and "Access Denied" = credential checking
- Multiple subnets = not searching for a specific resource
- Outside normal pattern = not legitimate developer activity

You investigate WKSTN-DEV-042:
- Recent suspicious PowerShell activity
- Credential harvesting tools in memory
- Attacker trying to find writable shares with the developer's credentials

The attacker compromised the developer's workstation and is now moving laterally,
testing which systems the developer's credentials can access.

You isolate the workstation and begin incident response.

LATERAL MOVEMENT PRINCIPLE: Internal systems scanning across multiple subnets
with mixed access results indicates an attacker probing the network with
compromised credentials.
                """,
                "failure_texts": {
                    0: """
"Authorized network scan" from a developer workstation? Without coordination with
security? Spanning HR, Finance, and Executive subnets?

Authorized security scans come from dedicated scanning infrastructure, during
approved windows, with proper coordination. Not from random developer workstations.

LESSON: Unauthorized scanning is unauthorized, regardless of who the system
belongs to.
                    """,
                    1: """
"Misconfigured software" doesn't scan 847 unique IPs across HR, Finance, and
Executive subnets looking for SMB shares.

Software misconfigurations cause repetitive connections to specific targets, not
broad network enumeration across business units.

LESSON: Lateral movement looks like lateral movement. Don't rationalize it.
                    """,
                    3: """
Group Policy doesn't make workstations scan other workstations via SMB. GPO is
pushed FROM domain controllers TO clients, not peer-to-peer.

Also, GPO doesn't result in "Access Denied" failures across multiple subnets.
That's credential testing, not policy application.

LESSON: Understand how Windows infrastructure actually works. This isn't GPO.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Lateral movement indicators:
- Internal systems scanning multiple subnets
- Mix of successful and denied access attempts
- Activity outside normal baseline
- Credential testing patterns

Internal reconnaissance is a key attacker phase after initial compromise.
        """,
        "domain_reference": "SOC Domain 4: Network Security - Lateral Movement Detection"
    },

    # Scenario 6: Encrypted Traffic Metadata
    {
        "id": "soc4_encrypted_metadata",
        "domain": 4,
        "themes": {
            "standard": {
                "title": "THE ENCRYPTED MYSTERY",
                "narrative": """
You can't inspect encrypted traffic content, but your network metadata shows:

Workstation: WKSTN-EXEC-001 (CEO's laptop)
Destination: 185.X.X.X:443 (Unknown external IP)
Connection pattern: Every 5 minutes, exactly
Session length: 0.2 seconds each
Bytes: 150 bytes out, 150 bytes in (consistent)
JA3 fingerprint: Matches known Cobalt Strike Beacon
Certificate: Self-signed, issued today

The CEO is traveling and connecting via hotel WiFi. The traffic is HTTPS
(encrypted) so you can't see the content.

Based on metadata alone, what is your assessment?
                """,
                "choices": [
                    {"text": "Normal HTTPS traffic - can't determine intent without content"},
                    {"text": "VPN connection - the CEO is connecting to corporate resources"},
                    {"text": "Probable C2 implant - metadata strongly indicates Cobalt Strike"},
                    {"text": "Banking website - the CEO is checking accounts while traveling"}
                ],
                "success_text": """
"Probable C2 implant," you assess. "The metadata screams Cobalt Strike Beacon."

Your metadata analysis:
- JA3 FINGERPRINT: Matches known Cobalt Strike client. JA3 fingerprints the TLS
  handshake, visible even in encrypted traffic.
- TIMING: Exactly 5-minute intervals (beacon sleep timer)
- SIZE: Consistent payload sizes (structured C2 protocol)
- CERTIFICATE: Self-signed, issued TODAY (not legitimate infrastructure)
- DESTINATION: Unknown IP, not corporate infrastructure

You can't see the CONTENT, but the METADATA tells the story:
- Legitimate websites have ESTABLISHED certificates
- Legitimate traffic has VARIABLE timing
- Legitimate connections have VARIABLE payload sizes
- JA3 fingerprinting IDENTIFIES the client software

You alert the executive protection team and begin remote containment procedures.

METADATA PRINCIPLE: Encryption hides content, not behavior. JA3 fingerprints,
timing patterns, and certificate metadata reveal threat indicators even in
encrypted traffic.
                """,
                "failure_texts": {
                    0: """
You CAN determine intent from metadata - you just demonstrated it by reading
the evidence.

JA3 fingerprint matching Cobalt Strike, self-signed cert issued today, perfect
interval timing, consistent payload sizes. This isn't "normal HTTPS."

LESSON: Metadata analysis is powerful. Don't give up just because content is
encrypted.
                    """,
                    1: """
Corporate VPN has:
- Known endpoint IPs
- Established certificates from corporate CA
- Variable session lengths based on activity
- Recognizable JA3 fingerprints from standard VPN clients

This has: Unknown IP, self-signed cert, Cobalt Strike JA3 fingerprint. Not VPN.

LESSON: Know what your corporate infrastructure looks like. This doesn't match.
                    """,
                    3: """
Banking websites have:
- Well-known certificate authorities (not self-signed)
- Certificates issued months/years ago (not today)
- Variable session lengths based on user activity
- Browser JA3 fingerprints (not Cobalt Strike)

No bank issues self-signed certificates that expire tomorrow.

LESSON: Legitimate websites have legitimate certificates. Self-signed = suspicious.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Encrypted traffic metadata analysis:
- JA3 FINGERPRINTS: Identify client software from TLS handshake
- TIMING PATTERNS: Regular intervals indicate automation
- PAYLOAD SIZES: Consistent sizes suggest structured protocols
- CERTIFICATE DATA: Self-signed, validity period, issuer

Encryption hides content; behavior remains visible.
        """,
        "domain_reference": "SOC Domain 4: Network Security - Encrypted Traffic Metadata Analysis"
    },

    # Scenario 7: Port Scan Recognition
    {
        "id": "soc4_port_scan",
        "domain": 4,
        "themes": {
            "standard": {
                "title": "THE SCANNING PATTERN",
                "narrative": """
Your firewall logs show external traffic to your DMZ:

Source: 45.X.X.X (External IP from a known scanning service)
Destination: Your public IP range
Time span: 15 minutes
Activity:
- 65,535 SYN packets to one server, ports 1-65535
- Each port receives exactly 1 SYN packet
- 147 SYN-ACK responses (open ports)
- Remaining 65,388 RST responses (closed ports)

This scan completed at 2:47 AM. A similar scan from a different IP occurred
3 days ago.

What type of scan is this, and what should you do?
                """,
                "choices": [
                    {"text": "Full port scan - block the IP and ignore (background noise)"},
                    {"text": "Stealth scan (SYN scan) - investigate which ports responded open"},
                    {"text": "DDoS attack - implement rate limiting immediately"},
                    {"text": "Legitimate vulnerability assessment - check if this is authorized"}
                ],
                "success_text": """
"SYN scan - let's review what the attacker learned," you recommend.

Your analysis:
- SCAN TYPE: SYN scan (TCP half-open). Sends SYN, receives SYN-ACK or RST, never
  completes handshake. Classic reconnaissance technique.
- SCOPE: Full port range (1-65535). Attacker wants complete picture.
- TIMING: 2:47 AM, off-hours to avoid detection.
- PATTERN: Similar scan 3 days ago = repeated reconnaissance.

Your response:
1. IDENTIFY OPEN PORTS: What 147 ports responded? Are they all expected?
2. CHECK SERVICES: Are vulnerable services exposed?
3. CORRELATE: Did anything happen after the scan 3 days ago?
4. REVIEW DMZ: Should these ports be open?

You find:
- Port 8080 open: Forgotten test server, running vulnerable Tomcat
- Port 9200 open: Elasticsearch with no authentication
- Port 27017 open: MongoDB with default config

The scan revealed exposure you didn't know existed.

SCAN RESPONSE PRINCIPLE: Port scans aren't just noise - they tell you what
attackers see. Use their reconnaissance to improve your defenses.
                """,
                "failure_texts": {
                    0: """
"Block and ignore" means you:
- Don't know what the attacker learned
- Miss that you have 147 open ports (expected or not?)
- Ignore the reconnaissance phase of a potential attack
- May have services exposed that shouldn't be

The NEXT step after reconnaissance is exploitation. Don't wait for it.

LESSON: Scans tell you what attackers see. Review your exposure.
                    """,
                    2: """
65,535 packets over 15 minutes is ~73 packets/second. That's not a DDoS - that's
a measured, methodical scan designed to enumerate services.

DDoS would be millions of packets attempting to overwhelm resources. This is
reconnaissance, not denial of service.

LESSON: Know the difference between scanning (reconnaissance) and flooding (DoS).
                    """,
                    3: """
Authorized vulnerability scans are scheduled, documented, and come from known
scanning infrastructure. Not random IPs at 2:47 AM.

If your security team was scanning, you'd know. This is external reconnaissance.

LESSON: Legitimate security testing is coordinated. Unknown scans are hostile.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Port scan analysis:
1. IDENTIFY scan type (SYN, connect, UDP, etc.)
2. REVIEW what responded (open ports)
3. VERIFY services are expected and secured
4. CORRELATE with subsequent activity

Reconnaissance precedes exploitation. Use their scan to audit your exposure.
        """,
        "domain_reference": "SOC Domain 4: Network Security - Port Scan Recognition"
    },

    # Scenario 8: Protocol Anomaly
    {
        "id": "soc4_protocol_anomaly",
        "domain": 4,
        "themes": {
            "standard": {
                "title": "THE STRANGE PROTOCOL",
                "narrative": """
Your network monitoring detects unusual traffic from an internal server:

Source: DATABASE-PROD-01 (Production Oracle database)
Destination: 104.X.X.X:53 (External IP)
Protocol: DNS (UDP port 53)
Behavior: Large DNS responses (5000+ bytes) every 30 seconds
Query type: TXT records to random-looking subdomains of "legit-service.net"

Normal DNS characteristics:
- Queries go to internal DNS servers, not external IPs directly
- Response sizes are typically 100-500 bytes
- TXT records are rarely used in enterprise environments

What is the MOST likely explanation?
                """,
                "choices": [
                    {"text": "DNS misconfiguration - the server is using wrong DNS servers"},
                    {"text": "DNS tunneling - data is being smuggled through DNS protocol"},
                    {"text": "SPF/DKIM verification - email security uses TXT records"},
                    {"text": "CDN health checks - content delivery often uses DNS TXT"}
                ],
                "success_text": """
"DNS tunneling," you assess. "This database server has no business making direct
external DNS queries, especially for TXT records with 5KB responses."

Your analysis:
- DIRECT EXTERNAL DNS: Normal hosts use internal DNS servers. Direct external
  queries bypass your DNS security controls.
- TXT RECORDS: Used for DNS tunneling because they support longer data payloads.
- RESPONSE SIZE: 5KB responses contain encoded data being sent TO the server
  (reverse tunnel for C2 commands).
- 30-SECOND INTERVAL: Automated beaconing pattern.

DNS tunneling uses DNS as a covert channel:
- Queries can send data OUT (encoded in subdomain names)
- Responses can send data IN (encoded in TXT or other records)
- Looks like "normal" DNS to simple monitoring

A production database with DNS tunneling = major compromise. You escalate immediately.

PROTOCOL ANOMALY PRINCIPLE: Legitimate protocols can be abused for covert channels.
Large TXT responses, unusual record types, and direct external queries are red flags.
                """,
                "failure_texts": {
                    0: """
"Misconfiguration" doesn't explain:
- Why it's querying TXT records
- Why responses are 5KB
- Why it's happening every 30 seconds
- Why it's contacting random-looking subdomains

Misconfigurations cause connectivity failures, not structured covert communication.

LESSON: Structured, regular, unusual traffic is not misconfiguration.
                    """,
                    2: """
SPF/DKIM verification happens in email servers, not database servers. A production
Oracle database has no business doing email authentication.

Also, SPF/DKIM queries go to the SENDER'S domain, not random "legit-service.net"
domains with encoded subdomain names.

LESSON: Understand which systems perform which functions. Databases don't do email.
                    """,
                    3: """
CDN health checks are initiated BY CDN infrastructure, not by database servers
making outbound queries. And they don't use 5KB TXT responses.

Database servers don't participate in CDN operations. They serve queries from
applications, not content delivery networks.

LESSON: Know your architecture. Databases don't do CDN health checks.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Protocol anomaly indicators:
- Unusual record types (TXT for data channels)
- Abnormal payload sizes (DNS responses > 1KB)
- Direct external queries (bypassing internal DNS)
- Unexpected sources (database servers making DNS queries)

Legitimate protocols can hide covert channels.
        """,
        "domain_reference": "SOC Domain 4: Network Security - Protocol Anomaly Detection"
    }
]
