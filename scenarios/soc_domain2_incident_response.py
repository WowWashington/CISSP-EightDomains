"""
Domain 2: Incident Response scenarios.

Key SOC concepts tested:
- NIST SP 800-61 IR lifecycle
- Incident classification (P1-P4)
- Evidence preservation and chain of custody
- Containment strategies
- Escalation decision making
- Post-incident activities
- Timeline reconstruction
- Recovery verification

Each scenario uses a single "standard" professional theme.
"""

SOC_DOMAIN_2_SCENARIOS = [
    # Scenario 1: Incident Classification
    {
        "id": "soc2_incident_classification",
        "domain": 2,
        "themes": {
            "standard": {
                "title": "SEVERITY ASSESSMENT",
                "narrative": """
At 10:45 AM, your EDR solution triggers a high-severity alert: "Ransomware behavior
detected." The affected system is WKSTN-HR-042, belonging to a Human Resources
coordinator. The alert shows:

- Process: vssadmin.exe deleting shadow copies
- File activity: Rapid file modifications with entropy changes in HR shared drives
- Network: Connections to Tor exit nodes detected
- User: Logged in as jsmith_hr (HR Coordinator, not admin)

The HR Director is calling, panicking about "everything being encrypted." Your
incident commander needs a severity classification to mobilize the appropriate
response.

Your organization uses P1-P4 classification:
- P1: Critical - Active threat, business-critical impact
- P2: High - Confirmed threat, significant impact
- P3: Medium - Potential threat, limited impact
- P4: Low - Suspicious activity, minimal impact

How do you classify this incident?
                """,
                "choices": [
                    {"text": "P4 (Low) - It's just one workstation, wait and see if it spreads"},
                    {"text": "P3 (Medium) - Ransomware is serious but it's contained to HR"},
                    {"text": "P1 (Critical) - Active ransomware with lateral movement indicators"},
                    {"text": "P2 (High) - Confirmed ransomware but need more analysis first"}
                ],
                "success_text": """
"P1 - CRITICAL INCIDENT," you report. "Active ransomware execution with indicators
of network propagation. We need immediate containment, executive notification, and
all hands."

Your incident commander acknowledges and initiates the P1 playbook:
- Network isolation of the HR subnet
- Emergency change advisory board bypass for defensive actions
- CISO notification and legal/PR standby
- All available responders mobilized

By classifying as P1 immediately, the response team contained the outbreak to 7
workstations instead of the 200+ that would have been affected with a delayed response.

The shadow copy deletion and Tor connections indicated an active, sophisticated attack.
This wasn't the time for "wait and see."

Post-incident review validates your call: "The analyst correctly identified multiple
high-fidelity indicators of active compromise and classified appropriately. The
rapid P1 response was directly responsible for limiting blast radius."

CLASSIFICATION PRINCIPLE: When multiple high-confidence indicators align, classify
high and mobilize fast. You can always downgrade. You can't un-encrypt files.
                """,
                "failure_texts": {
                    0: """
"Wait and see"? Shadow copies are being deleted. Files are encrypting. Tor connections
are active. This isn't suspicious activity - this is confirmed, ACTIVE ransomware.

By the time you "saw" more, the entire HR department was encrypted. Then Finance
(connected share). Then Legal (same subnet). The CEO's laptop followed.

LESSON: P4 is for "interesting anomaly, needs investigation." Not "ransomware
executing right now."
                    """,
                    1: """
"Contained to HR"? The HR shared drives are connected to the entire company. The
Tor connections suggest data exfiltration, not just encryption.

While you debated if this was "really P1," the ransomware spread through network
shares. The "contained" HR incident became a company-wide crisis.

LESSON: Ransomware rarely stays contained. Active encryption + network connectivity
= P1, every time.
                    """,
                    3: """
"Need more analysis first" - while ransomware is actively encrypting?

The evidence is overwhelming: vssadmin (shadow copy deletion), high entropy file
modifications (encryption), Tor connections (C2/exfiltration). What additional
analysis would change your response?

While you gathered "more data," the attackers gathered your data.

LESSON: In active incidents, containment precedes investigation. Classify, contain,
THEN analyze.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Incident classification factors:
1. ACTIVE vs. HISTORICAL - Is the threat executing now?
2. SCOPE - One system or organization-wide potential?
3. IMPACT - What data/systems are affected?
4. CONFIDENCE - How certain are we this is real?
        """,
        "domain_reference": "SOC Domain 2: Incident Response - NIST SP 800-61 Incident Classification"
    },

    # Scenario 2: Evidence Preservation
    {
        "id": "soc2_evidence_preservation",
        "domain": 2,
        "themes": {
            "standard": {
                "title": "THE COMPROMISED LAPTOP",
                "narrative": """
An executive's laptop has been confirmed as patient zero in a spear-phishing attack.
The attacker gained access via a malicious PDF attachment and established persistence.
Legal has informed you this incident may result in litigation, and law enforcement
may become involved.

The executive is impatient: "I have board presentations on that laptop. Can't you
just remove the malware and give it back? I need it by 3 PM."

Your forensic analyst has identified the malware but needs to preserve evidence.
The laptop is currently powered on with active network connection disabled.

What is the CORRECT approach for evidence handling?
                """,
                "choices": [
                    {"text": "Image the live system's memory first, then power down and image the drive"},
                    {"text": "Immediately power down the laptop to prevent further damage"},
                    {"text": "Remove the malware, document what you found, and return the laptop"},
                    {"text": "Let the executive copy their files to a USB drive first, then image"}
                ],
                "success_text": """
You explain to the executive: "I understand the urgency, but this device is now
evidence in a potential legal matter. We need to do this correctly."

Your forensic process:
1. Document the current state (photo of screen, running processes)
2. Capture volatile memory while system is live (RAM dump)
3. Power down cleanly using forensically sound methods
4. Create a bit-for-bit forensic image of the drive (write-blocked)
5. Generate hashes for chain of custody documentation
6. Work from the forensic copy, never the original

The executive gets a loaner laptop with files restored from backup. The evidence
is preserved for legal proceedings.

Six months later, the case goes to court. Opposing counsel challenges the evidence.
Your forensic analyst presents the chain of custody documentation: every step
logged, hashes verified, acquisition methods documented.

"The evidence is admissible," the judge rules.

EVIDENCE PRINCIPLE: In potential legal matters, proper acquisition beats speed.
Live memory is volatile and must be captured first. Original evidence is never modified.
                """,
                "failure_texts": {
                    0: """
Wait - you have the order correct, but "power down and image" loses critical volatile
evidence if you don't capture memory FIRST while the system is still running!

Memory must be captured LIVE. Once you power down:
- Active network connections showing C2 destinations - GONE
- Decrypted malware in memory - GONE
- Process execution history - GONE
- Encryption keys - GONE

LESSON: Order of volatility matters. Memory FIRST (most volatile), then disk (less
volatile). Power down only AFTER capturing RAM.
                    """,
                    1: """
Immediately powering down destroys volatile evidence! You lost:
- Memory contents (malware decrypted in RAM, encryption keys, active connections)
- Running process list
- Network connection state

The drive image was clean, but memory forensics would have revealed the attacker's
C2 infrastructure. That evidence is gone forever.

LESSON: Live systems have volatile evidence that disappears on power-off. Capture
memory FIRST, then safely power down, then image the drive.
                    """,
                    2: """
"Remove the malware and document it"? You just:
- Modified the original evidence (malware removal changes the system)
- Destroyed forensic integrity
- Made the evidence inadmissible in court
- Lost any ability to understand the full scope of compromise

When Legal asks "how do we prove this was the attack vector?" - you can't.

LESSON: Evidence systems are NEVER modified. Document, image, preserve. Clean a COPY
if needed, never the original.
                    """,
                    3: """
Letting the executive access the evidence system? You just:
- Modified file access timestamps (evidence tampering)
- Potentially copied malware to the USB drive
- Created chain of custody issues
- Made the executive a witness who needs to testify

Opposing counsel: "Your Honor, the plaintiff allowed the device owner to access the
evidence system before forensic acquisition."

Motion to exclude digital evidence: GRANTED.

LESSON: Evidence systems are not accessed by users until forensic acquisition is
complete and verified.
                    """
                }
            }
        },
        "correct_index": 0,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Digital forensics evidence handling:
1. ORDER OF VOLATILITY - Capture most volatile (memory) before least volatile (disk)
2. CHAIN OF CUSTODY - Document every action, every handler
3. FORENSIC IMAGING - Bit-for-bit copies with hash verification
4. ORIGINAL PRESERVATION - Work from copies, never modify originals
        """,
        "domain_reference": "SOC Domain 2: Incident Response - Digital Forensics and Evidence Handling"
    },

    # Scenario 3: Containment Decision
    {
        "id": "soc2_containment_decision",
        "domain": 2,
        "themes": {
            "standard": {
                "title": "THE RANSOMWARE DILEMMA",
                "narrative": """
Active ransomware is spreading through your network. You've confirmed 12 infected
systems so far, with encryption actively occurring. The infection is spreading
via SMB lateral movement.

Your options for containment:

A) Isolate only the known 12 infected systems
B) Isolate the entire affected subnet (150 systems, includes critical business apps)
C) Block all SMB traffic network-wide (will break file shares, printers, AD auth)
D) Wait for full scope assessment before containment (estimated: 45 minutes)

The CFO is on the phone demanding to know why the financial close process just
stopped working. The ransomware uses a 2-hour encryption timer before demanding
payment.

What containment action do you take?
                """,
                "choices": [
                    {"text": "Option A - Isolate only confirmed systems to minimize business disruption"},
                    {"text": "Option B - Isolate the entire subnet to stop spread"},
                    {"text": "Option C - Block SMB network-wide for maximum containment"},
                    {"text": "Option D - Complete the scope assessment first"}
                ],
                "success_text": """
"Option B - subnet isolation," you decide. "We're stopping the bleeding. CFO, I
understand the financial close is impacted. The alternative is encrypted financial
data and a ransom demand."

Your reasoning:
- Option A (12 systems only): Ransomware spreads faster than we can identify. By the
  time we confirm system #13, systems #14-20 are already encrypted.
- Option C (block SMB everywhere): Nuclear option breaks authentication and legitimate
  business. Reserve for catastrophic scenarios.
- Option D (wait 45 min): Ransomware doesn't wait. In 45 minutes, you won't have
  systems to assess.

Subnet isolation:
- Contains the threat to a known boundary
- Preserves evidence on isolated systems
- Allows business continuity on unaffected subnets
- Can be reversed once scope is determined

Post-incident: The ransomware had already reached 23 systems by the time you
contained. Without subnet isolation, it would have reached 200+ in the 45 minutes
needed for scope assessment.

CONTAINMENT PRINCIPLE: In active attacks, contain to a known boundary. Accept
business disruption to prevent catastrophic loss.
                """,
                "failure_texts": {
                    0: """
Isolating only confirmed systems is reactive whack-a-mole. Ransomware spreads via
automated processes - by the time you confirm system #13, systems #14-20 are
already encrypting.

While you isolated 12 systems, 35 more were compromised. You were always behind.

LESSON: Active threats require proactive containment. Isolate to a BOUNDARY, not
individual known-bad systems.
                    """,
                    2: """
Blocking SMB network-wide stops ransomware but also stops:
- Active Directory authentication (everyone gets locked out)
- File shares (business processes halt company-wide)
- Printers (okay, no one cares about printers)
- Legitimate administrative tools

This is the "burn down the house to kill the spider" approach. The ransomware was
on ONE subnet - you disrupted the ENTIRE company.

LESSON: Containment should be proportional. Subnet isolation contained the threat
without company-wide outage.
                    """,
                    3: """
"Wait for full scope assessment" - while ransomware actively encrypts files at
hundreds of files per minute?

In 45 minutes:
- The 12 known systems are fully encrypted
- The ransomware has spread to 200+ systems
- Your "scope assessment" now covers the entire network

You assessed the scope alright. The scope is "everything."

LESSON: In active attacks, containment precedes assessment. Stop the bleeding first.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Containment decision factors:
1. SPEED OF SPREAD - How fast is the threat propagating?
2. BOUNDARY OPTIONS - What natural boundaries exist?
3. BUSINESS IMPACT - What's the cost of containment vs. non-containment?
4. REVERSIBILITY - Can you undo the containment action?
        """,
        "domain_reference": "SOC Domain 2: Incident Response - Containment Strategies"
    },

    # Scenario 4: NIST IR Phase Identification
    {
        "id": "soc2_nist_phases",
        "domain": 2,
        "themes": {
            "standard": {
                "title": "THE IR TIMELINE",
                "narrative": """
You're documenting an incident for the post-incident report. The timeline shows:

08:00 - SIEM alert triggered for suspicious PowerShell activity
08:15 - Analyst triages alert and confirms malicious behavior
08:30 - Affected system isolated from network
09:00 - Malware identified and removed from isolated system
09:30 - System reimaged and restored from clean backup
10:00 - System returned to production with enhanced monitoring

According to NIST SP 800-61 Incident Response Lifecycle, which phase does the
activity at 09:00 (malware removal) belong to?
                """,
                "choices": [
                    {"text": "Detection and Analysis - we're still analyzing the malware"},
                    {"text": "Containment - removing the threat contains it"},
                    {"text": "Eradication - removing the malware eliminates the threat"},
                    {"text": "Recovery - we're preparing for system restoration"}
                ],
                "success_text": """
"Eradication," you correctly identify.

NIST SP 800-61 defines four phases:

1. PREPARATION (before incident)
   - Policies, procedures, tools, training

2. DETECTION AND ANALYSIS (08:00-08:15)
   - Alert triage, confirmation, scope assessment

3. CONTAINMENT, ERADICATION, AND RECOVERY (08:30-09:30)
   - Containment (08:30): Isolate to stop spread
   - Eradication (09:00): Remove malware/threat
   - Recovery (09:30): Restore systems to production

4. POST-INCIDENT ACTIVITY (after 10:00)
   - Lessons learned, documentation, process improvement

Malware removal is ERADICATION - eliminating the threat from the environment.
It's distinct from Containment (stopping spread) and Recovery (restoring operations).

Note: NIST groups Containment, Eradication, and Recovery as one phase because they
often overlap in practice. But understanding the distinct purposes helps ensure
you don't skip steps.

IR PHASES PRINCIPLE: Each phase has a distinct purpose. Containment stops spread.
Eradication removes the threat. Recovery restores operations. Don't confuse them.
                """,
                "failure_texts": {
                    0: """
Detection and Analysis ended at 08:15 when the analyst confirmed malicious behavior.
By 09:00, you've already contained the system - you're well past detection.

Analysis may continue in parallel, but the PRIMARY activity (malware removal) is
clearly Eradication.

LESSON: Detection and Analysis answers "what happened?" Eradication answers "how
do we remove it?"
                    """,
                    1: """
Containment occurred at 08:30 (system isolation). By 09:00, the system is already
isolated - containment is complete.

Removing the malware doesn't "contain" it - containment already happened. Removal
ERADICATES the threat from the environment.

LESSON: Containment = stopping spread. Eradication = removing the threat. They're
sequential, not simultaneous.
                    """,
                    3: """
Recovery occurs at 09:30 (reimage and restore). At 09:00, you're still removing
malware - the system isn't ready for recovery yet.

The sequence is: Contain (isolate) → Eradicate (remove) → Recover (restore).
Malware removal is Eradication, which precedes Recovery.

LESSON: Recovery means returning to production. You can't recover a system that
still has malware on it.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
NIST SP 800-61 IR Lifecycle:
1. Preparation - Before incidents (policies, tools, training)
2. Detection and Analysis - Identify and understand the incident
3. Containment, Eradication, Recovery - Stop, remove, restore
4. Post-Incident Activity - Lessons learned, improvements
        """,
        "domain_reference": "SOC Domain 2: Incident Response - NIST SP 800-61 Lifecycle Phases"
    },

    # Scenario 5: Escalation Decision
    {
        "id": "soc2_escalation",
        "domain": 2,
        "themes": {
            "standard": {
                "title": "THE ESCALATION CALL",
                "narrative": """
It's 2:30 AM on Saturday. You're the overnight analyst. An alert fires for a
production web server: "Web shell detected - /var/www/html/admin/shell.php"

Your investigation shows:
- File creation timestamp: 2:15 AM (15 minutes ago)
- File contains obfuscated PHP code matching known web shell signatures
- Apache access logs show shell.php accessed once from a VPN IP
- No other suspicious activity visible yet
- The web server hosts the company's customer portal (revenue-critical)

Your escalation options:
- Tier 2 Analyst (on-call, 15-min response SLA)
- Incident Manager (on-call, executive escalation authority)
- CISO (emergency-only contact)
- No escalation - continue investigation

Who do you escalate to?
                """,
                "choices": [
                    {"text": "No escalation - gather more evidence first"},
                    {"text": "Tier 2 Analyst - confirmed threat, need senior eyes"},
                    {"text": "Incident Manager - potential breach of customer data system"},
                    {"text": "CISO - revenue-critical system compromise"}
                ],
                "success_text": """
You escalate to the Incident Manager immediately.

"Incident Manager, this is overnight SOC. We have a confirmed web shell on the
customer portal server. Web shell created 15 minutes ago and already accessed.
This is an active breach of a customer-facing system."

The Incident Manager mobilizes:
- Wakes Tier 2 for technical support
- Initiates customer data exposure assessment
- Puts legal and PR on standby
- Authorizes emergency containment actions

Your reasoning:
- Web shell = confirmed compromise, not suspicious activity
- Customer portal = potential data breach notification trigger
- Already accessed = attacker is ACTIVE, not dormant
- 2:30 AM = deliberate off-hours attack for reduced detection

This isn't a Tier 2 investigation - this is an incident requiring management authority.
And it's not CISO-level (yet) - that's for confirmed data breach or executive decisions.

ESCALATION PRINCIPLE: Match escalation level to impact and authority needed. Web shell
on customer system with active access = Incident Manager, not just Tier 2.
                """,
                "failure_texts": {
                    0: """
"Gather more evidence" while an attacker has an active web shell on your customer
portal? What evidence do you need?

- File exists: confirmed
- Contains web shell code: confirmed
- Already accessed by attacker: confirmed
- Hosts customer data: confirmed

While you "gathered evidence," the attacker was gathering customer records.

LESSON: A confirmed web shell is an incident, not an investigation. Escalate
immediately.
                    """,
                    1: """
Tier 2 can help with technical analysis, but this situation requires more than
technical support:
- Customer data exposure assessment
- Potential breach notification decisions
- Authority to take emergency containment actions
- Business impact coordination

A Tier 2 analyst doesn't have authority to make those calls. You need management.

LESSON: Escalate based on authority needed, not just technical complexity. Customer
data systems require incident management involvement.
                    """,
                    3: """
CISO escalation is reserved for:
- Confirmed significant data breach
- Executive decision requirements
- Public-facing incident response
- Regulatory notification triggers

You have a web shell - you don't yet know if customer data was accessed. Incident
Manager can assess and escalate to CISO if warranted.

LESSON: Don't jump to the top. The escalation chain exists for a reason. Incident
Manager is the right level to assess and coordinate.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Escalation considerations:
1. SEVERITY - How serious is the confirmed threat?
2. AUTHORITY - What decisions need to be made?
3. IMPACT - What systems/data are affected?
4. TIMING - How active is the threat?
        """,
        "domain_reference": "SOC Domain 2: Incident Response - Escalation Procedures"
    },

    # Scenario 6: Post-Incident Review
    {
        "id": "soc2_post_incident",
        "domain": 2,
        "themes": {
            "standard": {
                "title": "LESSONS LEARNED",
                "narrative": """
The ransomware incident is over. Final impact:
- 23 systems encrypted
- 4 hours of business disruption
- $50,000 recovery costs
- No ransom paid, restored from backups

You're preparing the post-incident review. The Incident Commander asks what the
PRIMARY focus of the lessons learned session should be.

Your options:
A) Identify who made mistakes so they can be retrained
B) Document what happened for compliance and audit purposes
C) Identify process improvements to prevent/detect similar incidents faster
D) Calculate the full financial impact for insurance claims
                """,
                "choices": [
                    {"text": "Option A - Identify mistakes and individuals for retraining"},
                    {"text": "Option B - Document for compliance and audit"},
                    {"text": "Option C - Identify process improvements for future incidents"},
                    {"text": "Option D - Calculate financial impact for insurance"}
                ],
                "success_text": """
"Option C - process improvements," you recommend. "The goal is organizational
learning, not blame."

Your lessons learned agenda:
1. TIMELINE REVIEW: What happened, when, and how did we respond?
2. DETECTION GAPS: Why didn't we catch this sooner?
3. RESPONSE EFFECTIVENESS: What worked? What didn't?
4. PROCESS IMPROVEMENTS: What changes prevent recurrence?
5. ACTION ITEMS: Who owns each improvement, with deadlines?

Key findings from your review:
- Initial phishing email bypassed email security (action: tune email filters)
- Lateral movement wasn't detected for 45 minutes (action: improve SMB monitoring)
- Backup restoration took 2 hours (action: practice recovery procedures)

The Incident Commander approves: "This is exactly right. Blame kills honesty. If
people are afraid of punishment, they hide mistakes instead of reporting them.
We learn from incidents, we don't prosecute them."

POST-INCIDENT PRINCIPLE: The goal is ORGANIZATIONAL LEARNING, not individual blame.
Process improvements prevent future incidents. Blame prevents future reporting.
                """,
                "failure_texts": {
                    0: """
"Identify who made mistakes" creates a blame culture that destroys incident response.

When people fear punishment:
- They hide mistakes instead of reporting them
- They don't escalate early because "maybe it's nothing"
- They cover up errors instead of fixing root causes

The ransomware entered through a phishing email. Blaming the user who clicked is
pointless - users click. Your job is detecting and containing when they do.

LESSON: Blame culture kills security culture. Focus on process, not individuals.
                    """,
                    1: """
Compliance documentation is necessary but it's not the PRIMARY purpose of lessons
learned. Audit reports don't prevent future incidents - process improvements do.

The compliance team can document independently. The post-incident review is for
the response team to learn and improve.

LESSON: Documentation is an output, not the goal. The goal is learning.
                    """,
                    3: """
Financial impact calculation is important for insurance and budgeting, but it's
not the purpose of a lessons learned session.

Finance can calculate costs independently. The responders in the room need to
discuss what happened and how to do better, not spreadsheet math.

LESSON: Financial analysis belongs in a different meeting. Lessons learned is
about response improvement.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Post-incident review principles:
1. BLAMELESS CULTURE - Focus on processes, not individuals
2. LEARNING FOCUS - What can we improve?
3. ACTION-ORIENTED - Specific improvements with owners
4. TIMELY - Conduct while memories are fresh
        """,
        "domain_reference": "SOC Domain 2: Incident Response - Post-Incident Activity"
    },

    # Scenario 7: Timeline Reconstruction
    {
        "id": "soc2_timeline",
        "domain": 2,
        "themes": {
            "standard": {
                "title": "PIECING IT TOGETHER",
                "narrative": """
You're building an incident timeline from multiple log sources. You have:

Windows Security Event Log (from compromised system):
- "Process Create: powershell.exe" at 14:32:15 EST

SIEM Alert:
- "Suspicious PowerShell detected" at 14:32:18 EST

Network Firewall Log:
- "Outbound connection to 185.x.x.x:443" at 14:32:47 UTC

Your SIEM normalizes all timestamps to EST. The firewall is configured for UTC.

For accurate timeline reconstruction, what is the FIRST step you must take?
                """,
                "choices": [
                    {"text": "Sort all events by timestamp as-is"},
                    {"text": "Normalize all timestamps to a single timezone"},
                    {"text": "Ignore timestamp discrepancies - they're close enough"},
                    {"text": "Use only the SIEM timestamps since they're already normalized"}
                ],
                "success_text": """
"Normalize all timestamps to a single timezone," you correctly identify.

You convert the firewall log from UTC to EST:
- 14:32:47 UTC = 09:32:47 EST (assuming EST is UTC-5)

Now the timeline makes sense:
1. 09:32:47 EST - Firewall sees outbound connection (this is EARLIER than Windows!)
2. 14:32:15 EST - Windows logs PowerShell execution
3. 14:32:18 EST - SIEM alerts on PowerShell

Wait - the firewall event is 5 HOURS earlier? That means either:
- The firewall clock is wrong, OR
- The initial compromise was much earlier than the PowerShell detection

You check: the firewall was misconfigured and logging in UTC while labeled as "local
time." After correction, the TRUE timeline shows PowerShell preceded the C2 callback
by 32 seconds - which makes sense.

TIMELINE PRINCIPLE: Timestamp normalization is CRITICAL. Different systems use
different timezones, NTP sources, and formats. A single-timezone timeline is
essential for accurate reconstruction.
                """,
                "failure_texts": {
                    0: """
Sorting by timestamp as-is puts the firewall event at 14:32:47, AFTER the PowerShell
events. But the firewall is in UTC - that's actually 09:32:47 EST, FIVE HOURS EARLIER.

Your "timeline" shows PowerShell (14:32:15) → SIEM alert (14:32:18) → C2 callback
(14:32:47). But the C2 callback actually happened hours before the PowerShell you
detected.

Incorrect timelines lead to incorrect conclusions about attack sequence.

LESSON: Always normalize timestamps before analysis.
                    """,
                    2: """
"Close enough" in forensics isn't good enough. In this case, the timestamps are
FIVE HOURS apart due to timezone differences.

Ignoring timezone discrepancies:
- Produces an incorrect attack timeline
- Misrepresents the sequence of events
- Could identify the wrong initial access vector
- May be challenged in legal proceedings

LESSON: Precision matters. Normalize timestamps, don't assume.
                    """,
                    3: """
Using only SIEM timestamps loses critical forensic data:
- Firewall logs may show events the SIEM didn't parse
- Original source timestamps may be more accurate
- Some events may not have SIEM-normalized equivalents

The SIEM normalizes what it RECEIVES, but timezone errors at the SOURCE propagate
through. You need to verify source system configurations.

LESSON: SIEM normalization helps, but verify source timezone configurations for
complete accuracy.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Timeline reconstruction requirements:
1. NORMALIZE TIMEZONES - Convert all timestamps to a single reference
2. VERIFY NTP - Ensure source systems are time-synchronized
3. DOCUMENT ASSUMPTIONS - Note any clock skew or configuration issues
4. CROSS-REFERENCE - Use multiple sources to validate sequence
        """,
        "domain_reference": "SOC Domain 2: Incident Response - Timeline Reconstruction"
    },

    # Scenario 8: Recovery Verification
    {
        "id": "soc2_recovery_verification",
        "domain": 2,
        "themes": {
            "standard": {
                "title": "BACK TO PRODUCTION",
                "narrative": """
The ransomware incident is contained. The affected server (a file server) has been
reimaged and restored from backup. The system administrator says "It's ready to go
back into production."

Before authorizing the return to production, what verification steps are ESSENTIAL?

Your options:
A) Trust the admin's assessment - they reimaged it, it's clean
B) Run a quick antivirus scan and return to production
C) Verify the restored backup is clean and patch the vulnerability that was exploited
D) Keep the system isolated for 30 days of monitoring before production
                """,
                "choices": [
                    {"text": "Option A - Reimaged systems are clean by definition"},
                    {"text": "Option B - AV scan confirms no remaining malware"},
                    {"text": "Option C - Verify backup integrity and patch vulnerabilities"},
                    {"text": "Option D - Extended monitoring period before production"}
                ],
                "success_text": """
"Option C - verify backup and patch vulnerabilities," you recommend.

Your recovery verification checklist:
1. BACKUP VERIFICATION: Confirm the backup predates the compromise
   - Check backup timestamps vs. initial access timeline
   - Scan restored data for malware
   - Verify data integrity

2. VULNERABILITY REMEDIATION: Patch what let them in
   - The ransomware exploited an unpatched vulnerability
   - Restoring from backup restores the VULNERABLE configuration
   - Without patching, you'll be compromised again

3. ENHANCED MONITORING: Watch for signs of persistent access
   - Attackers may have left backdoors not in the restored backup
   - Monitor for suspicious activity for the first 48-72 hours

The admin realizes: "Oh, the backup was from last week - before we applied patches.
If I restored without patching, we'd be vulnerable to the exact same exploit."

You patch the system before it returns to production.

RECOVERY PRINCIPLE: Restoration without remediation equals re-compromise. Verify
backup integrity AND fix the vulnerability that enabled the initial access.
                """,
                "failure_texts": {
                    0: """
"Reimaged systems are clean" - but the backup might not be!

If the backup was taken AFTER initial compromise, you just restored:
- The malware
- The backdoors
- The persistence mechanisms

And even if the backup is clean, you restored the VULNERABLE configuration that
let attackers in the first time.

LESSON: Reimaging removes malware; verification ensures you don't restore it.
                    """,
                    1: """
AV scans are useful but insufficient:
- AV misses zero-days and sophisticated malware
- AV doesn't verify backup integrity
- AV doesn't patch vulnerabilities

You scanned for known malware and found nothing. The vulnerability that let
attackers in? Still unpatched. Re-compromise in 48 hours.

LESSON: AV is one tool, not the complete verification process.
                    """,
                    3: """
30 days of isolation is excessive and impacts business operations unnecessarily.
The file server is needed for daily work.

Enhanced monitoring is good, but 30 days of isolation means 30 days without a
critical business system. That's not proportional to the risk.

72 hours of enhanced monitoring with verified backup and patched vulnerabilities
is the right balance.

LESSON: Recovery verification should be thorough but proportional. Don't over-
isolate systems that are properly remediated.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Recovery verification steps:
1. BACKUP INTEGRITY - Verify backup predates compromise
2. MALWARE SCANNING - Check restored data for threats
3. VULNERABILITY REMEDIATION - Patch the initial access vector
4. ENHANCED MONITORING - Watch for residual threats post-recovery
        """,
        "domain_reference": "SOC Domain 2: Incident Response - Recovery and Verification"
    }
]
