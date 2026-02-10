"""
Domain 7: Security Operations scenarios.

Key CISSP concepts tested:
- Incident Response Lifecycle
- Evidence Handling and Forensics
- SIEM and Log Management
- Threat Intelligence
- Patch and Change Management
- Business Continuity
- Disaster Recovery

Each scenario supports dual themes:
- Fantasy: Medieval/magical Citadel setting
- Corporate: Modern office satire (Office Space style)
"""

DOMAIN_7_SCENARIOS = [
    # Scenario 1: Incident Response Lifecycle
    {
        "id": "d7_incident_response_lifecycle",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE SIEGE HAS BEGUN",
                "narrative": """
The alarm bells shatter the midnight silence. Dark riders have been spotted
breaching the outer wall - scouts report at least a dozen infiltrators now
loose within the Citadel grounds. Your sentinel network has already identified
three towers showing signs of intrusion.

The Captain of the Guard rushes to your side. "We've detected them and
identified the affected areas. Our analysis is complete. What comes NEXT
in our response?"

The infiltrators are spreading. Every moment of indecision allows them to
embed deeper into your defenses. The response protocol scroll hangs on
the wall, its ancient wisdom guiding generations of guardians.

What is your next action?
                """,
                "choices": [
                    {"text": "Begin Preparation - gather supplies and train the guards"},
                    {"text": "Conduct Lessons Learned - document what happened for future reference"},
                    {"text": "Execute Containment, Eradication, and Recovery - stop the spread and remove the threat"},
                    {"text": "Continue Detection and Analysis - keep watching to see what else happens"}
                ],
                "success_text": """
You draw your blade and issue rapid orders. "Seal the affected towers! Deploy
the purification squads! No infiltrator escapes, and no clean area becomes
compromised!"

Your guards spring into action. The containment teams isolate the affected
towers while the eradication squads systematically clear each floor. By dawn,
the threat is eliminated and normal operations resume.

The Master Sentinel nods approvingly. "You understood the sacred sequence:
Preparation, then Detection and Analysis, then Containment and Recovery,
and finally Lessons Learned. You knew exactly where we stood and what came
next."

The incident response lifecycle flows like a river - each phase following
naturally from the last. Skipping ahead or falling behind invites disaster.
                """,
                "failure_texts": {
                    0: """
Preparation happens BEFORE incidents occur, not during them! While you
gathered supplies and held training sessions, the infiltrators embedded
themselves throughout the Citadel. By morning, they had compromised the
royal treasury.

The incident response lifecycle is: Preparation, Detection/Analysis,
Containment/Eradication/Recovery, and Post-Incident Review. You were in
Detection/Analysis - the NEXT phase was Containment.
                    """,
                    1: """
Lessons Learned is the FINAL phase of incident response, not the next step!
While you documented observations, the infiltrators spread unchecked through
the Citadel, eventually reaching the inner sanctum.

After Detection/Analysis comes Containment/Eradication/Recovery. Only AFTER
the incident is resolved do you conduct post-incident review.
                    """,
                    3: """
Detection and Analysis was already COMPLETE according to the scenario! You
identified affected systems and analyzed the threat. Continuing to analyze
while the threat spreads is paralysis by analysis.

The next phase after Detection/Analysis is Containment/Eradication/Recovery.
Act on the intelligence you've gathered - stop the spread!
                    """
                }
            },
            "corporate": {
                "title": "SOC ALERT: BREACH DETECTED",
                "narrative": """
Your phone buzzes at 2:47 AM. The SOC dashboard is lit up like a Christmas
tree. Multiple alerts indicate lateral movement across the network - someone
or something is hopping between servers in the finance department.

The night shift analyst briefs you quickly: "We detected anomalous activity
at 1:30 AM. We've identified twelve compromised hosts and analyzed the
attack pattern - looks like stolen credentials being used for lateral
movement. Analysis complete. What's our next move?"

The incident response plan sits in your shared drive, but there's no time
to re-read it now. You need to make a call.

What do you recommend?
                """,
                "choices": [
                    {"text": "Schedule tabletop exercise - we need more preparation before acting"},
                    {"text": "Set up the post-incident review meeting - let's document this"},
                    {"text": "Initiate containment - isolate affected hosts, block the credentials, begin remediation"},
                    {"text": "Keep monitoring - we need more data before we act"}
                ],
                "success_text": """
"Containment NOW," you order. "Isolate those twelve hosts, disable the
compromised credentials, and get EDR blocking that lateral movement pattern."

By 4 AM, the affected systems are isolated. By 6 AM, the eradication team
has cleared the malware. By noon, clean systems are being restored from
known-good backups.

At the post-incident review a week later, the CISO nods approvingly.
"Textbook response. Detection, Analysis, then straight into Containment
and Recovery. No dithering, no over-analysis. That's why we have the
incident response lifecycle - so we know exactly what comes next."

The coffee is cold, but the network is clean. That's a win.
                """,
                "failure_texts": {
                    0: """
"Schedule a tabletop?" The analyst stares at you. "We're IN an active
incident! Preparation happens BEFORE breaches, not during them!"

While you were planning theoretical exercises, the attackers exfiltrated
the quarterly financial data. The incident response lifecycle has distinct
phases - Preparation comes first, but you were already past Detection and
Analysis. Containment was the next step.
                    """,
                    1: """
"Post-incident review? The incident is still HAPPENING!" The analyst's
jaw drops as you open a calendar invite.

By the time you finished scheduling the PIR meeting, the attackers had
established persistent backdoors across the network. Lessons Learned is
the LAST phase - after Containment, Eradication, and Recovery.
                    """,
                    3: """
"More monitoring?" The analyst watches helplessly as the attack spreads.
"We already KNOW what's happening. We've done the analysis!"

By continuing to gather data on an understood threat, you allowed the
attackers to reach the crown jewels. Analysis paralysis is real. After
Detection and Analysis, you MUST move to Containment. You had enough
information - you needed to act.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
The Incident Response Lifecycle has four major phases: Preparation (before
incidents), Detection and Analysis (identifying and understanding the threat),
Containment/Eradication/Recovery (stopping and removing the threat), and
Post-Incident Review (learning from the incident). Understanding where you
are in this cycle determines your next action.
        """,
        "domain_reference": "Domain 7: Security Operations - Incident Response Lifecycle"
    },

    # Scenario 2: Evidence Handling / Chain of Custody
    {
        "id": "d7_chain_of_custody",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE STOLEN GRIMOIRE",
                "narrative": """
A priceless grimoire has vanished from the Arcane Vault, and suspicion falls
upon a junior scribe. The Magistrate demands evidence that will stand before
the Royal Court of Justice.

You discover a suspicious scroll hidden beneath the scribe's mattress. It
appears to contain copied passages from the missing grimoire. This could be
the evidence that proves guilt or innocence.

The Court Arbiter warns you: "Whatever evidence you present must be beyond
reproach. The defense will challenge how it was found, who touched it, and
whether it could have been planted or altered. The Royal Court requires
proof of evidence integrity."

What documentation is ESSENTIAL to ensure this evidence is admissible?
                """,
                "choices": [
                    {"text": "The scribe's performance evaluations from their supervisor"},
                    {"text": "Chain of custody documentation - who found it, who handled it, every transfer recorded"},
                    {"text": "The quarterly budget reports for the Arcane Vault"},
                    {"text": "The vendor contracts for scroll materials"}
                ],
                "success_text": """
You immediately produce a fresh evidence ledger. With careful precision, you
document: the exact time of discovery, the location, who found the scroll,
its condition, and who witnessed the finding.

As the scroll passes to the Court Examiner, you log the transfer - time,
reason, and both parties' marks. Every subsequent examination is recorded
with the same meticulous detail.

At trial, the defense attempts to claim the scroll was planted. The
Magistrate reviews your chain of custody documentation. "Every hand that
touched this evidence is accounted for. Every moment is documented. The
integrity of this evidence is beyond reproach."

The truth prevails because you preserved it properly.
                """,
                "failure_texts": {
                    0: """
"Performance evaluations?" The Magistrate is bewildered. "We're trying to
prove the evidence is genuine, not whether the scribe was good at their job!"

Without chain of custody documentation, the defense successfully argued
that the scroll could have been planted. The case was dismissed.

Chain of custody proves EVIDENCE integrity - who handled it, when, and
why. Without it, evidence is inadmissible.
                    """,
                    2: """
"Budget reports?" The Court Arbiter stares at you. "What do vault expenditures
have to do with whether this scroll was properly handled as evidence?"

The defense argued the scroll could have been tampered with since there was
no documentation of who touched it. The case collapsed.

Chain of custody documentation is essential for legal proceedings - it proves
evidence hasn't been altered or planted.
                    """,
                    3: """
"Vendor contracts for scroll materials?" The Magistrate sighs heavily.

Without any documentation of how the evidence was discovered and handled,
the defense easily created reasonable doubt. "Anyone could have placed this
scroll there," they argued. Case dismissed.

Chain of custody is ESSENTIAL for legal admissibility.
                    """
                }
            },
            "corporate": {
                "title": "THE HR INVESTIGATION",
                "narrative": """
HR and Legal have launched an investigation into a senior developer suspected
of stealing source code before leaving for a competitor. You've been asked to
assist with the forensic examination of their laptop.

While imaging the drive, you discover a folder containing what appears to be
proprietary code and customer data that was never authorized for local storage.

The company attorney pulls you aside. "This case is likely going to court.
If we can't prove this evidence is legitimate and untampered, their lawyers
will have it thrown out. What documentation do we NEED?"

What do you tell them is ESSENTIAL?
                """,
                "choices": [
                    {"text": "The developer's annual performance reviews"},
                    {"text": "Chain of custody documentation tracking everyone who handled the evidence"},
                    {"text": "The IT department's annual budget reports"},
                    {"text": "The company's vendor contracts with software suppliers"}
                ],
                "success_text": """
"Chain of custody," you respond immediately. You pull out your evidence
handling forms and begin documenting.

Every step is recorded: who discovered the laptop, when it was seized, who
transported it, when it reached the forensics lab, who performed the imaging,
what tools were used, who has accessed the image since.

Six months later, in court, opposing counsel challenges the evidence. Your
attorney presents the chain of custody documentation - every hand, every
moment, every action accounted for.

"The evidence stands," the judge rules. "Its integrity has been properly
documented throughout."

The case proceeds, and justice is served because you knew what mattered.
                """,
                "failure_texts": {
                    0: """
"Performance reviews?" The attorney's face falls. "We need to prove the
EVIDENCE is legitimate, not whether they were a good employee!"

Without chain of custody documentation, opposing counsel argued the data
could have been planted on the laptop. The judge agreed - evidence
excluded, case severely weakened.

Chain of custody is ESSENTIAL for legal admissibility.
                    """,
                    2: """
"Budget reports?" The attorney stares at you in disbelief. "How does IT's
budget prove this evidence wasn't tampered with?"

Without chain of custody, the defense successfully argued there was no way
to prove the evidence was genuine. Case dismissed.

Chain of custody documentation is the foundation of forensic evidence
admissibility.
                    """,
                    3: """
"Vendor contracts?" The attorney's hope visibly drains from their face.

At trial, opposing counsel challenged who had access to the laptop, whether
the data could have been planted, and whether proper procedures were followed.
Without chain of custody documentation, there was no defense.

Evidence excluded. Case collapsed. The company lost.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Chain of custody documentation is ESSENTIAL for legal proceedings. It records
everyone who handled evidence, when they handled it, why, and what they did
with it. This proves evidence integrity and prevents claims of tampering or
planting. Without proper chain of custody, even damning evidence may be
inadmissible in court.
        """,
        "domain_reference": "Domain 7: Security Operations - Chain of Custody"
    },

    # Scenario 3: Digital Forensics
    {
        "id": "d7_digital_forensics",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE CORRUPTED CRYSTAL",
                "narrative": """
A memory crystal recovered from a captured enemy spy contains what may be
critical intelligence about an impending attack. However, the crystal is
fragile - improper handling could corrupt or destroy its contents.

The Master of Secrets approaches you. "This crystal must be examined, but
its contents must remain pristine. Our enemies will claim we altered the
memories if we cannot prove the original remains untouched. The information
must hold up before the Allied Council."

You hold the crystal carefully. Its faint blue glow pulses with stored
memories. Whatever you do first will determine whether this evidence
remains viable.

What should be done FIRST to preserve evidence integrity?
                """,
                "choices": [
                    {"text": "View the memories directly in the original crystal to see what's there"},
                    {"text": "Create a perfect magical duplicate of the crystal, then examine only the copy"},
                    {"text": "Destroy any suspicious memories to prevent further damage"},
                    {"text": "Cleanse the crystal with purification magic and install examination runes"}
                ],
                "success_text": """
You carefully invoke the Duplication Ritual, creating an exact magical copy
of the crystal - every memory, every fragment, every whisper perfectly
preserved. The original is sealed in a warded vault, untouched.

All examination proceeds on the copy. When you discover plans for an attack
on the Western Fortress, you can present your findings with confidence.

Before the Allied Council, an enemy advocate demands: "How do we know these
memories weren't fabricated?"

You present the sealed original. "This has never been touched since capture.
Compare it to our copy - they are identical. Our findings come from the
duplicate, preserving the original as proof."

The evidence stands. The Western Fortress is warned in time.
                """,
                "failure_texts": {
                    0: """
The moment you accessed the crystal directly, the magical signatures changed.
Timestamps shifted, access marks appeared. The original evidence is now
contaminated.

At the Allied Council, the enemy advocate smirks. "The crystal shows it
was accessed by your people. How do we know you didn't add these memories?"

Without a pristine original, your evidence is challenged successfully.

ALWAYS create a forensic copy first - never examine the original directly.
                    """,
                    2: """
You destroyed potential evidence! Whatever "suspicious" memories you erased
might have contained crucial intelligence or proof of innocence.

The Allied Council is appalled. "You destroyed evidence before examination?
How can we trust anything you claim to have found?"

Deleting or altering evidence is the opposite of forensic preservation.
                    """,
                    3: """
"Cleansing" the crystal erased half its contents. "Installing examination
runes" overwrote memory addresses. The evidence is now useless and
contaminated.

Forensic examination must preserve original evidence in pristine state.
Creating a bit-for-bit copy first ensures the original can always verify
your findings.
                    """
                }
            },
            "corporate": {
                "title": "THE INSIDER'S LAPTOP",
                "narrative": """
The terminated employee's laptop sits on your forensics bench. Legal suspects
they stole trade secrets before leaving, and this drive may contain proof.
However, any misstep could make the evidence unusable in court.

Your manager hovers nervously. "The lawyers are breathing down my neck. They
need to know what's on that drive, but they also need it to hold up in court.
One wrong move and opposing counsel will tear us apart."

The laptop screen glows ominously. You know the first action you take will
be scrutinized heavily.

What should be done FIRST to preserve evidence integrity?
                """,
                "choices": [
                    {"text": "Boot up the laptop and browse through the files to see what's there"},
                    {"text": "Create a forensic image (bit-for-bit copy) of the drive"},
                    {"text": "Delete any files that look like malware to prevent further damage"},
                    {"text": "Format the drive and install forensics tools for analysis"}
                ],
                "success_text": """
"Don't touch that power button," you say, connecting a write-blocker to
the drive. Using your forensic imaging tool, you create a bit-for-bit copy
of the entire drive - every sector, every fragment, including deleted files
and slack space.

The original drive is sealed and secured. All analysis proceeds on the
forensic image. When you find the smoking gun - a folder of stolen designs
with timestamps from the week before termination - you can prove exactly
when and how you found it.

At trial, opposing counsel challenges your findings. You present the
sealed original and your forensic image. "Hash values match. The original
was never modified. Everything we found came from an exact copy."

The evidence stands. Justice is served.
                """,
                "failure_texts": {
                    0: """
The moment you booted the laptop, dozens of timestamps changed. The operating
system modified access times, temp files were created, and logs were updated.
The original evidence is now contaminated.

At trial, opposing counsel argues: "The drive was accessed after seizure.
How do we know what was original versus what was added or modified?"

NEVER examine original media directly. Create a forensic image first.
                    """,
                    2: """
You just destroyed evidence! Whatever you deleted - even if it was malware -
could have been crucial to the investigation. You've also shown tampering
with the evidence.

Legal is furious. "You DELETED files from evidence? Do you know what
'spoliation of evidence' means? We're going to be sanctioned!"

Never delete anything from evidence under any circumstances.
                    """,
                    3: """
"You FORMATTED THE DRIVE?!" Legal's screaming can be heard three floors up.

All evidence is destroyed. The case is not only lost - the company may face
sanctions for destruction of evidence. Your forensics career is effectively
over.

A forensic image preserves evidence. Formatting destroys it completely.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
The FIRST step in digital forensics is always to create a forensic image -
a bit-for-bit copy of the original evidence. All analysis is performed on
the copy, ensuring the original remains pristine. This preserves evidence
integrity and ensures findings can always be verified against an untouched
original.
        """,
        "domain_reference": "Domain 7: Security Operations - Digital Forensics"
    },

    # Scenario 4: SIEM Operations
    {
        "id": "d7_siem_operations",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE WATCHTOWER NETWORK",
                "narrative": """
The Kingdom maintains a dozen watchtowers along its borders, each reporting
sightings via messenger bird. The problem: each tower uses different codes,
reports at different intervals, and their messages often contradict each other.

The War Council is frustrated. "Yesterday, the Northern Tower reported dragon
sightings while the Eastern Tower saw bandits. Were they the same threat from
different angles? Different threats? We cannot tell! By the time we decode
and compare these messages, the threat has moved."

The Chief Scout sighs. "We need a way to gather all reports in one place,
translate them to a common language, and identify patterns across towers.
Right now, each tower's observations exist in isolation."

What solution addresses this problem?
                """,
                "choices": [
                    {"text": "Destroy older messages to reduce the volume of reports"},
                    {"text": "Establish a central intelligence room that correlates all tower reports"},
                    {"text": "Shut down the less important towers to reduce confusion"},
                    {"text": "Have all towers send their messages directly to the War Council without processing"}
                ],
                "success_text": """
You propose the creation of the Central Vigilance Chamber - a room where
trained analysts receive all watchtower reports, translate them to a common
format, and plot them on a master map.

Within weeks, the results are remarkable. When the Northern Tower reports
"large winged shadow moving south" and the Eastern Tower reports "increased
bandit activity" an hour later, analysts correlate: the "bandits" are
refugees fleeing the dragon.

"Magnificent!" the War Council exclaims. "Now we see the full picture, not
scattered fragments. We can identify attack patterns that individual towers
would never spot alone."

The Central Vigilance Chamber becomes the Kingdom's greatest defensive asset.
                """,
                "failure_texts": {
                    0: """
"Destroy messages?!" The Chief Scout is aghast. "Those records let us
identify patterns over time! We once caught a spy ring because their
movements created patterns across three moons of reports!"

Deleting security logs loses critical historical data and may violate
legal retention requirements. The solution is correlation, not deletion.
                    """,
                    2: """
"Close towers?" The War Council shakes their heads. "The 'less important'
Eastern Tower detected the assassination plot last spring! Attackers target
weaknesses - removing coverage creates blind spots they will exploit."

Reducing visibility makes problems worse, not better. The solution is
better correlation, not fewer data sources.
                    """,
                    3: """
The War Council is now drowning in unprocessed messages. The Chief Councilor
hasn't slept in three days trying to decode different tower formats.

"Raw data isn't intelligence!" he finally snaps. "We needed analysis and
correlation, not just a bigger pile of parchment!"

Data without correlation and analysis is just noise.
                    """
                }
            },
            "corporate": {
                "title": "THE LOG MANAGEMENT NIGHTMARE",
                "narrative": """
The security team is drowning. Firewall logs come in one format, Windows
event logs in another, cloud service logs in yet another. When an incident
occurs, analysts spend hours manually searching each system, trying to
piece together what happened.

The CISO convenes an emergency meeting. "Last week's breach investigation
took 72 hours because we couldn't correlate events across systems. The
attacker hit the VPN, then the web server, then the database - but we
couldn't see the pattern until we manually compared timestamps across
five different log sources."

The team lead throws up his hands. "Each system speaks a different language.
We can't identify attack patterns when we're looking at scattered puzzle
pieces."

What solution addresses this problem?
                """,
                "choices": [
                    {"text": "Delete older logs to reduce the volume we need to search"},
                    {"text": "Implement a SIEM for centralized log collection and correlation"},
                    {"text": "Disable logging on less critical systems to reduce complexity"},
                    {"text": "Email all logs to the security team for manual review"}
                ],
                "success_text": """
"We need a SIEM," you recommend. Within months, the Security Information
and Event Management platform is collecting logs from every source,
normalizing them to a common format, and correlating events automatically.

The transformation is dramatic. When the next suspicious login occurs at
3 AM, the SIEM automatically correlates: VPN connection from unusual
location, followed by privileged access to file server, followed by
large data transfer. The alert fires in seconds.

"We just went from 72 hours to 72 seconds for threat detection," the CISO
grins at the next board meeting. "The SIEM sees patterns no human analyst
could spot in real-time."

Your SOC is now truly operational.
                """,
                "failure_texts": {
                    0: """
"Delete logs?" The compliance officer nearly chokes. "We're required to
retain security logs for seven years! And those 'old' logs are how we
detected last year's persistent threat!"

Deleting logs destroys critical forensic evidence and violates retention
requirements. You need better analysis, not less data.
                    """,
                    2: """
"Disable logging?" The security analyst stares. "The 'less critical' HR
system is where the last three phishing attacks landed! Attackers love
systems without monitoring!"

Reducing visibility creates blind spots that attackers will exploit.
Security requires MORE visibility, not less.
                    """,
                    3: """
The security team's inbox now contains 50,000 emails per day. Nobody can
find anything. Critical alerts are buried in noise. The team lead quits.

Email cannot correlate, analyze, or prioritize events. You needed a SIEM -
a system designed for centralized log management and analysis.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
SIEM (Security Information and Event Management) systems collect logs from
multiple sources, normalize them to a common format, and correlate events
across systems. This enables detection of attack patterns that individual
log sources cannot reveal. Without SIEM, security teams drown in scattered
data that cannot be effectively analyzed.
        """,
        "domain_reference": "Domain 7: Security Operations - SIEM"
    },

    # Scenario 5: Threat Intelligence
    {
        "id": "d7_threat_intelligence",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE SPY NETWORK'S GIFT",
                "narrative": """
Your network of informants across the realms has proven invaluable. Last
moon, they warned of the Crimson Band's planned attack on merchant caravans.
The moon before, they identified poisoned grain shipments from a hostile
kingdom.

Now the Spymaster proposes an expansion: "We can obtain regular reports of
known threats - bandit hideouts, cursed artifacts in circulation, enemy
troop movements. This intelligence can be shared directly with our gate
guards, caravan masters, and tower sentinels."

The War Council debates. "Reactive defense means we're always one step behind.
By the time we know about a threat, it's already at our gates. But if we
had advance warning of known threats, we could block them before they arrive."

How should you implement proactive defense against known threats?
                """,
                "choices": [
                    {"text": "Wait for attacks to happen, then respond - reactive defense only"},
                    {"text": "Integrate threat intelligence with all defensive positions to proactively block known threats"},
                    {"text": "Sever all connections to other realms to eliminate external threats entirely"},
                    {"text": "Focus only on internal threats and ignore external intelligence"}
                ],
                "success_text": """
You establish the Threat Intelligence Network. Regular reports from informants
are translated into actionable warnings: "The Crimson Band's leader has a
distinctive scar - all gate guards now know his face. Poisoned grain bears
this maker's mark - all inspectors check for it."

The results are immediate. A known assassin is stopped at the gates before
entering. A shipment of cursed weapons is intercepted at the border. Enemy
scouts are identified by their unit's distinctive cloaks.

"We're no longer waiting for attacks," the War Council marvels. "We're
preventing them before they begin. Known threats are blocked automatically
because our defenses know what to look for."

Proactive defense through threat intelligence transforms your security posture.
                """,
                "failure_texts": {
                    0: """
"Reactive only?" The Spymaster is incredulous. "So we wait for the assassin
to strike, THEN try to catch them? We wait for the poison to kill people,
THEN investigate?"

Reactive defense means always being one step behind. By the time you respond,
the damage is done. Threat intelligence enables proactive blocking of
known threats before attacks succeed.
                    """,
                    2: """
"Sever all connections?" The merchants revolt. Trade collapses. The kingdom's
economy crumbles. Without external goods, people starve.

Meanwhile, internal threats flourish with no external intelligence to warn
of them. Isolation is not security - it's blindness with economic collapse.
                    """,
                    3: """
"Ignore external threats?" Six months later, an invasion force that your
abandoned spy network would have detected three weeks in advance appears
at your gates without warning.

External threats are significant and often more dangerous than internal
ones. Ignoring them is catastrophically negligent.
                    """
                }
            },
            "corporate": {
                "title": "THE THREAT FEED PROPOSAL",
                "narrative": """
The security vendor's pitch is compelling: "We aggregate threat data from
thousands of sources worldwide. Known malicious IPs, domains hosting malware,
file hashes of known threats - updated in real-time. We can integrate this
directly with your firewalls, proxies, and endpoint protection."

Your manager is skeptical. "Sounds expensive. Can't we just wait until
we detect threats ourselves?"

The CISO weighs in: "Last month's ransomware attack used infrastructure that
was flagged in threat feeds two weeks before it hit us. If our firewall had
that information, it would have blocked the initial callback automatically."

The team debates how to improve their defensive posture against known threats.
What should be implemented?
                """,
                "choices": [
                    {"text": "Stick with reactive incident response only"},
                    {"text": "Subscribe to threat intelligence feeds and integrate with security controls"},
                    {"text": "Disconnect from the internet entirely to eliminate external threats"},
                    {"text": "Ignore external threats and focus only on insider threats"}
                ],
                "success_text": """
The threat intelligence integration goes live on a Monday. By Friday, the
firewall has blocked 847 connections to known command-and-control servers.
The email gateway has quarantined 1,200 messages containing known malicious
attachments. EDR has prevented execution of 43 known malware samples.

"None of these would have been caught without the threat feeds," the SOC
lead reports. "We're blocking attacks before they even start."

Six months later, when a major ransomware campaign sweeps through your
industry, your organization is untouched. The malicious infrastructure
was flagged in your threat feeds before the campaign even launched.

Proactive defense wins.
                """,
                "failure_texts": {
                    0: """
"Reactive only?" The CISO sighs. "So we wait for ransomware to encrypt
our files, THEN respond? We wait for the breach, THEN investigate?"

Three months later, your organization is hit by the same ransomware
campaign that threat intelligence would have blocked. The cost of
recovery exceeds the threat feed subscription by 1000x.

Reactive defense is always one step behind.
                    """,
                    2: """
"Disconnect from the internet?" The CEO stares. "We're an e-commerce
company. Our entire business IS the internet."

This is not 1985. For most modern organizations, internet connectivity
is essential for operations. The solution is proactive defense, not
isolation.
                    """,
                    3: """
"Ignore external threats?" The next month, a nation-state APT compromises
your VPN appliance using a vulnerability that threat intelligence had
flagged two weeks earlier.

External threats are often more sophisticated and dangerous than insider
threats. Ignoring them is negligent.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Threat intelligence provides indicators of compromise (IPs, domains, file
hashes) for known threats. Integrating this intelligence with security
controls (firewalls, proxies, EDR) enables proactive blocking of known-bad
infrastructure before attacks succeed. Reactive-only defense means always
being one step behind attackers.
        """,
        "domain_reference": "Domain 7: Security Operations - Threat Intelligence"
    },

    # Scenario 6: Malware Analysis
    {
        "id": "d7_malware_analysis",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE CURSED ARTIFACT",
                "narrative": """
A strange amulet was discovered in a merchant's pack at the city gates. The
guards who touched it immediately felt compelled to open the vault doors.
Fortunately, senior guards restrained them before any harm was done.

The Court Wizard examines the amulet without touching it. "This bears
powerful mind-control enchantments. We must understand its full capabilities
to protect against similar artifacts. But actually testing it is dangerous -
its effects could spread."

The Master of Defense agrees. "We need to know what this thing does - what
triggers it, how far its influence reaches, what commands it implants. But
we cannot risk more guards falling under its spell."

How should this artifact be analyzed safely?
                """,
                "choices": [
                    {"text": "Have a guard touch it in the throne room to observe the effects"},
                    {"text": "Study it within an isolated magical containment circle where effects cannot escape"},
                    {"text": "Send it to the neighboring kingdom and ask if their guards are affected"},
                    {"text": "Destroy it immediately without learning anything about its capabilities"}
                ],
                "success_text": """
The Court Wizard constructs a Containment Circle of Isolation - a magical
barrier where no effect can escape. Within this controlled environment,
he carefully triggers the artifact and observes.

"Fascinating," he reports. "The compulsion only works within ten paces and
requires direct skin contact. It implants a single command that fades after
one hour. And..." he studies the runes, "these symbols identify the
creator - the Shadowmancer of the Eastern Wastes."

Armed with this intelligence, the Kingdom implements countermeasures: gloves
for all guards handling suspicious items, detection wards tuned to these
specific enchantments, and a warning sent to allied realms.

The threat is understood and mitigated because it was safely analyzed.
                """,
                "failure_texts": {
                    0: """
The guard touches the amulet in the crowded throne room. Within moments,
they're marching toward the treasury, and everyone within ten paces feels
the compulsion spreading. The King himself nearly hands over the crown
jewels before court wizards intervene.

You just infected your most secure location because you didn't use
isolation. Malware (or cursed artifacts) must be analyzed in contained
environments.
                    """,
                    2: """
You mailed a dangerous mind-control artifact to another kingdom? The courier
was compromised en route. Your allied realm now has three ministers under
hostile control.

Never expose others to threats you haven't analyzed. And never lose
containment of dangerous materials.
                    """,
                    3: """
The artifact is destroyed. You've learned nothing about how it works, who
made it, or how to detect similar items in the future.

Two weeks later, a dozen more amulets surface in various cities. Without
understanding the threat, you have no defense. Each one claims victims before
being discovered.

Destroying threats without analysis loses critical intelligence.
                    """
                }
            },
            "corporate": {
                "title": "THE SUSPICIOUS EXECUTABLE",
                "narrative": """
A user reports that they almost opened a suspicious email attachment before
thinking better of it. The file sits in their quarantine folder - an
executable with a generic name that's definitely not something IT deployed.

The SOC analyst examines the file's metadata. "This could be anything -
ransomware, a RAT, spyware. We need to understand what it does so we can
check if any other systems are affected and create detection rules."

Your manager is nervous. "What if analyzing it infects our systems? That
user's machine is connected to the corporate network."

The analyst nods. "We need to understand its behavior, but we can't risk
infection spreading. How do we safely analyze this?"

How should this suspicious executable be analyzed?
                """,
                "choices": [
                    {"text": "Run it on a production workstation and observe what happens"},
                    {"text": "Execute it in an isolated sandbox environment"},
                    {"text": "Email it to colleagues to see if their antivirus detects it"},
                    {"text": "Delete it immediately without any analysis"}
                ],
                "success_text": """
You fire up the malware analysis sandbox - an isolated virtual environment
that can't reach the production network or the internet. The executable is
detonated within this containment.

The sandbox captures everything: the file creates a hidden directory, drops
a secondary payload, attempts to contact a command-and-control server
(blocked by the isolated network), and begins encrypting files in the
documents folder.

"Ransomware," the analyst confirms. "And now we have the C2 domain to block,
the file hashes for detection rules, and the behavioral indicators for
threat hunting."

Within hours, network-wide scans confirm no other infections, and detection
rules are deployed across all endpoints. The threat is understood and
neutralized.
                """,
                "failure_texts": {
                    0: """
You run malware on a production workstation connected to the corporate
network. Congratulations - the ransomware is now spreading laterally.
Fourteen servers are encrypted before anyone can pull the plug.

NEVER run suspicious files on production systems. Sandboxes exist
specifically for this purpose.
                    """,
                    2: """
You emailed malware to your colleagues? Two of them opened it to "help with
testing." Their machines are now compromised. Also, your email system
is now flagged for distributing malware, and you're explaining yourself
to HR.

Never distribute potential malware - to anyone, ever.
                    """,
                    3: """
You deleted the only sample without analysis. A week later, five more
users report similar attachments. You still don't know what it does, what
it targets, or how to detect it.

Deleting without analysis loses critical threat intelligence. You can't
defend against what you don't understand.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Malware must be analyzed in isolated sandbox environments where it cannot
affect production systems or spread to other machines. Sandboxes capture
malware behavior (file changes, network connections, registry modifications)
without risking real infrastructure. This intelligence is essential for
creating detection rules and understanding the threat.
        """,
        "domain_reference": "Domain 7: Security Operations - Malware Analysis"
    },

    # Scenario 7: Patch Management
    {
        "id": "d7_patch_management",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE EMERGENCY WARD UPGRADE",
                "narrative": """
A messenger arrives in a lather: the Mages' Guild has discovered that a
common protection ward has a critical flaw. Dark mages are actively exploiting
it to breach fortresses across the land. The Kingdom of Whitestone fell
just yesterday.

The Court Wizard examines the ward correction scroll. "This must be applied
to all our defensive barriers. But our standard process requires two weeks
of testing in the practice chambers before deployment. The testing chambers
are currently occupied with the spring ward certification."

The War Council debates urgently. "Two weeks may be too long - enemies know
of this weakness and are exploiting it NOW. But applying untested corrections
could destabilize our other defenses."

What is the BEST approach to this critical vulnerability?
                """,
                "choices": [
                    {"text": "Strictly follow the two-week testing process regardless of the active threat"},
                    {"text": "Invoke emergency procedures for expedited testing and rapid deployment"},
                    {"text": "Ignore the ward correction since testing isn't complete"},
                    {"text": "Apply the correction everywhere immediately with no testing at all"}
                ],
                "success_text": """
You invoke the Emergency Ward Protocol. The Court Wizard convenes an emergency
session with senior mages. Within hours, accelerated testing validates the
correction on a representative sample of wards.

By nightfall, critical defensive positions receive the corrected wards.
By the following evening, all kingdom defenses are updated. The process
included testing - just accelerated, not abandoned.

Three days later, scouts report that enemies attempted the known exploit
against your gates. The corrected wards held firm. "The emergency protocol
saved us," the War Council agrees. "Speed with appropriate caution."

Critical vulnerabilities require emergency procedures - faster, but not
reckless.
                """,
                "failure_texts": {
                    0: """
You rigidly followed the two-week process. On day six, dark mages exploited
the vulnerability and breached the Eastern Gate. The castle fell before
testing was complete.

Emergency procedures exist precisely for situations like this. When
vulnerabilities are being actively exploited, standard timelines must
yield to appropriate urgency.
                    """,
                    2: """
"Ignore it?" The Court Wizard is aghast as enemy forces pour through the
now-exploited weakness in your wards. "Ignoring known, actively-exploited
vulnerabilities is not caution - it's negligence!"

The castle falls. Your "caution" killed everyone you were supposed to protect.
                    """,
                    3: """
You applied the correction everywhere with no testing. The ward correction
conflicted with the older enchantments on the North Tower, causing a
catastrophic magical feedback. The tower collapsed, taking the best mages
with it.

Emergency procedures still include testing - abbreviated, focused testing.
Zero testing risks catastrophic failures.
                    """
                }
            },
            "corporate": {
                "title": "THE CRITICAL ZERO-DAY",
                "narrative": """
The security news explodes: a critical zero-day in your VPN appliance is
being actively exploited in the wild. CISA has issued an emergency directive.
Your vendor has released an emergency patch.

The change manager pulls up the calendar. "Our standard change process
requires two weeks for testing and CAB approval. The next CAB meeting is
in five days."

The CISO's phone is already ringing - the CEO saw the news and is asking
if the company is protected. Meanwhile, your threat intel feed shows
exploitation attempts increasing hourly.

"Two weeks is our process," the change manager insists. "Process exists
for a reason."

What is the BEST approach?
                """,
                "choices": [
                    {"text": "Strictly follow the two-week testing process despite the active exploitation"},
                    {"text": "Use emergency change procedures for expedited approval and deployment"},
                    {"text": "Ignore the patch since our testing isn't complete"},
                    {"text": "Push the patch to production immediately with zero testing"}
                ],
                "success_text": """
"Invoke emergency change procedures," you declare. Within two hours, you've
assembled the emergency CAB - CISO, IT Director, and Change Manager. The
patch is tested on a non-production VPN concentrator.

Four hours later, testing confirms the patch works and doesn't break
critical functionality. The emergency CAB approves. By midnight, all VPN
appliances are patched.

The next morning, your SIEM shows 847 blocked exploitation attempts against
the now-patched vulnerability. "We dodged a bullet," the CISO tells the
board. "Emergency procedures exist for exactly this situation - faster
approval with appropriate controls, not bureaucratic paralysis."

The company is safe because you knew when and how to accelerate.
                """,
                "failure_texts": {
                    0: """
You waited for the two-week process. On day four, attackers exploited the
vulnerability and established persistence in your network. The breach cost
$4.7 million in remediation and regulatory fines.

"We have emergency change procedures for exactly this situation," the CISO
fumes. "Active exploitation means EMERGENCY. The two-week process is for
routine changes, not burning houses."
                    """,
                    2: """
"Ignore an actively-exploited critical vulnerability because testing isn't
complete?" The CISO stares in disbelief. "That's not caution - that's
negligence."

The breach occurs three days later. Your "process adherence" explanation
does not satisfy the regulators, the board, or the lawyers.
                    """,
                    3: """
You pushed the patch with zero testing. It conflicted with your custom
VPN configuration. All remote workers are now locked out. The sales team
can't access CRM. The executives can't get their email.

"Emergency procedures still include TESTING!" your manager shouts as the
help desk melts down. "Just FASTER testing!"

The patch is rolled back. The vulnerability remains. You've made everything
worse.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Organizations should have emergency change procedures for critical situations.
When vulnerabilities are being actively exploited, standard two-week processes
may be too slow. Emergency procedures allow expedited approval and accelerated
(but not eliminated) testing. Active exploitation warrants emergency response -
faster, but still controlled.
        """,
        "domain_reference": "Domain 7: Security Operations - Patch Management"
    },

    # Scenario 8: Change Management
    {
        "id": "d7_change_management",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE UNSANCTIONED WARD",
                "narrative": """
The Merchant Guild is furious. Their caravans were blocked at the city gates
for six hours yesterday - the gate wards inexplicably rejected their trade
tokens as counterfeit, despite being perfectly legitimate.

Investigation reveals that a junior enchanter, frustrated with the old ward's
slow verification process, modified the gate ward's detection thresholds
"just a little" to speed things up. He didn't tell anyone or test the
changes.

The Guild Master is demanding compensation. The Merchant Council is
threatening sanctions. The enchanter insists he was "just trying to help"
and that "the old settings were too slow anyway."

What type of control failure does this represent?
                """,
                "choices": [
                    {"text": "Incident response failure - the gates should have had a backup plan"},
                    {"text": "Change management failure - the modification was unapproved and untested"},
                    {"text": "Access control failure - the enchanter shouldn't have been able to touch the wards"},
                    {"text": "Encryption failure - the ward tokens should have been stronger"}
                ],
                "success_text": """
"This is a textbook change management failure," you explain to the Council.
"The enchanter made changes without approval, without review, without testing,
and without documentation. Change management exists precisely to prevent
this."

The Chief Enchanter nods grimly. "Every ward modification should go through
the Change Council. They verify the change is needed, review the plan, test
in the practice chambers, and approve deployment. None of that happened here."

New protocols are implemented: all ward modifications require Change Council
approval, testing in isolated chambers, and documentation of what was changed
and why. The junior enchanter receives additional training.

The incident becomes a teaching moment about why change management matters.
                """,
                "failure_texts": {
                    0: """
"Incident response?" The Chief Enchanter shakes his head. "The incident
HAPPENED because of the unauthorized change. Having a backup plan for
merchant verification doesn't prevent unauthorized modifications to wards."

The root cause was change management failure - unapproved changes. Incident
response handles problems after they occur; change management prevents them.
                    """,
                    2: """
"Access control?" The Change Council debates. "The enchanter was authorized
to work on wards - that's his job. The failure wasn't that he COULD make
changes, but that he made changes without approval or testing."

Access control determines WHO can make changes. Change management determines
WHETHER specific changes are appropriate. This was a change management failure.
                    """,
                    3: """
"Encryption failure?" The Court Wizard is confused. "The tokens weren't
counterfeited - they were REAL and were rejected because of unauthorized
threshold changes. Encryption is irrelevant here."

The problem was an unapproved, untested change. That's change management,
not cryptography.
                    """
                }
            },
            "corporate": {
                "title": "THE FRIDAY FIREWALL CHANGE",
                "narrative": """
The CEO's executive assistant is apoplectic. "The CEO hasn't been able to
access his trading app since last night! It's been blocked since about 5 PM
yesterday!"

Network investigation reveals that a firewall administrator, trying to block
a suspicious IP range before heading home for the weekend, added a rule that
inadvertently blocked the entire subnet used by the trading platform. No
change ticket. No peer review. No testing. Just a quick "fix" on his way out.

The CEO's losses from missed trades are potentially substantial. The firewall
admin insists he was "just trying to protect the network" and that "the
change process takes too long for urgent blocks."

What type of control failure does this represent?
                """,
                "choices": [
                    {"text": "Incident response failure - we should have caught the issue faster"},
                    {"text": "Change management failure - the modification was unapproved and untested"},
                    {"text": "Access control failure - the admin shouldn't have firewall access"},
                    {"text": "Encryption failure - the trading connection should have been encrypted"}
                ],
                "success_text": """
"Classic change management failure," you report to the incident review
committee. "The admin made a firewall change without a ticket, without peer
review, without testing, and without approval. Our change management process
exists precisely to catch mistakes like this."

The CISO nods. "Every firewall rule change should go through change management.
Someone else reviews the rule for unintended consequences. Testing verifies
no critical services are blocked. Documentation ensures we can track and
reverse changes."

The organization reinforces change management requirements and implements
mandatory peer review for all firewall modifications. The admin receives
additional training on proper procedures.

The incident becomes a case study in why change management matters.
                """,
                "failure_texts": {
                    0: """
"Incident response?" Your manager looks puzzled. "The incident OCCURRED
because of the unauthorized change. Faster detection doesn't prevent someone
from making unapproved modifications."

The root cause was change management failure. Incident response is reactive;
change management is preventive.
                    """,
                    2: """
"Access control failure?" The CISO considers. "No - the firewall admin is
supposed to have firewall access. That's their job. The failure was making
changes without the required approval and testing process."

Access control governs WHO can make changes. Change management governs
WHETHER specific changes are appropriate. Different controls, different
failures.
                    """,
                    3: """
"Encryption?" The network engineer is baffled. "The connection was encrypted.
It was BLOCKED, not intercepted. How would encryption prevent a firewall
rule from blocking traffic?"

The issue was an unapproved firewall change. That's change management, not
cryptography.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Change management requires all changes to be reviewed, approved, tested, and
documented before implementation. Unapproved changes bypass these controls
and can cause outages - as happened here. The process isn't bureaucracy for
its own sake; it prevents exactly this type of incident.
        """,
        "domain_reference": "Domain 7: Security Operations - Change Management"
    },

    # Scenario 9: Configuration Management
    {
        "id": "d7_configuration_management",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE INCONSISTENT WATCHTOWERS",
                "narrative": """
The Auditor General's report is damning. An inspection of the kingdom's
twenty watchtowers reveals complete chaos: six towers have unnecessary
observation mirrors that could leak information, four have outdated
defensive wards, three have conflicting communication crystals, and each
tower's configuration is completely different.

"How did this happen?" the War Council demands.

The Tower Commander shrugs helplessly. "Each tower master configures their
domain as they see fit. Gareth prefers extra mirrors for visibility. Eliza
relies on older, proven wards. Marcus uses experimental crystals."

The Auditor General slams the table. "This creates security gaps! Attackers
study the weakest configuration and exploit it. And when a tower master
retires, nobody knows how their tower is supposed to work!"

What should be implemented to address this?
                """,
                "choices": [
                    {"text": "Rebuild all towers from scratch with identical designs"},
                    {"text": "Implement configuration management with standardized baselines"},
                    {"text": "Document current configurations as-is and call them 'standard'"},
                    {"text": "Allow each tower master to continue configuring systems their preferred way"}
                ],
                "success_text": """
You propose the Standard Tower Configuration - a defined baseline specifying
exactly what wards, mirrors, and crystals each tower should have. Automation
ensorcellments are created to regularly verify compliance and report drift.

Within three months, all towers are aligned. Each has the same defensive
wards, appropriate observation mirrors, and compatible communication crystals.
When Tower Master Eliza retires, her successor can maintain the tower using
the documented standard.

"Magnificent," the Auditor General declares in the follow-up inspection.
"Consistent configurations mean consistent security. Drift is detected and
corrected automatically. This is proper configuration management."

The kingdom's defenses are now predictable, maintainable, and secure.
                """,
                "failure_texts": {
                    0: """
"Rebuild all towers?" The Treasury Minister chokes. "That would bankrupt
the kingdom! And without configuration management, they'd drift apart again
within a year anyway."

The expensive solution doesn't fix the underlying problem. You need defined
baselines and ongoing enforcement - configuration management.
                    """,
                    2: """
"Document the chaos and call it standard?" The Auditor General stares. "If
every tower is configured differently, which one IS the standard? You've just
given official sanction to chaos."

The inconsistency IS the problem. Documenting inconsistent configurations
doesn't create consistency.
                    """,
                    3: """
"Continue as-is?" One year later, an attacker identifies that Tower Fourteen
has outdated wards (Marcus's experimental approach), exploits the weakness,
and captures the tower. From there, they gain a foothold to attack others.

Individual preferences are the CAUSE of the problem. Configuration management
ensures consistency and security.
                    """
                }
            },
            "corporate": {
                "title": "THE SERVER AUDIT DISASTER",
                "narrative": """
The compliance auditors are not happy. Their review of your server estate
reveals chaos: some servers run unnecessary services, others have outdated
settings, configurations vary wildly between what should be identical
systems, and nobody can explain why Server 47 has its own unique firewall
rules.

"How did this happen?" the CISO demands.

The senior sysadmin shrugs. "Different admins configured different servers
at different times. Mike likes to enable experimental features. Sarah
prefers legacy configurations. Nobody ever established what 'correct'
looks like."

The auditor is blunt: "Inconsistent configurations create attack surfaces.
Attackers target the weakest server and pivot from there."

What should be implemented?
                """,
                "choices": [
                    {"text": "Rebuild all servers from scratch"},
                    {"text": "Implement configuration management with defined baselines"},
                    {"text": "Document current configurations as-is"},
                    {"text": "Allow each administrator to configure systems their preferred way"}
                ],
                "success_text": """
"We need configuration management," you recommend. Your team defines
standard baselines for each server type - what services run, what settings
are configured, what firewall rules apply. Automation tools enforce these
baselines and report drift.

Within three months, the transformation is complete. Every web server is
identical. Every database server matches the standard. When drift is
detected - someone enabling an unauthorized service - the automation
flags it immediately.

"This is what configuration management looks like," the auditors note in
their follow-up report. "Defined standards, automated enforcement, drift
detection. The inconsistency problem is solved."

Your environment is now consistent, auditable, and secure.
                """,
                "failure_texts": {
                    0: """
"Rebuild everything?" The IT Director laughs grimly. "That's a two-year
project with a $5 million budget. And without configuration management,
the servers would drift apart again within six months."

Rebuilding doesn't solve the problem - it just delays it. You need defined
baselines and ongoing enforcement.
                    """,
                    2: """
"Document the chaos?" The auditors shake their heads. "If every server is
different, which one is 'correct'? You've just created official documentation
of your inconsistency problem."

Documenting inconsistent configurations doesn't create consistency. You
need defined standards and enforcement.
                    """,
                    3: """
"Continue with individual preferences?" The following year's audit is worse.
Server 23, configured by an admin who left two years ago, is breached through
an obsolete service nobody knew was running. The attack spreads to twelve
other servers.

Individual preferences CAUSE the inconsistency. Configuration management
establishes and enforces standards.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Configuration management defines standard baselines and uses automation to
ensure consistency across systems. When configurations drift from the standard,
it's detected and corrected. Without configuration management, systems
become inconsistent, creating security gaps that attackers exploit.
        """,
        "domain_reference": "Domain 7: Security Operations - Configuration Management"
    },

    # Scenario 10: Business Continuity
    {
        "id": "d7_business_continuity",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE GREAT HALL COLLAPSE",
                "narrative": """
The earthquake struck without warning. The Great Hall - center of kingdom
operations - lies in ruins. The throne room is buried under rubble, the
treasury vault is inaccessible, and the communication crystal network
is severed.

The Master of Continuity unfolds the emergency scrolls. "We prepared for
this. Three contingency sites were established, each at different levels
of readiness. Which shall we activate?"

He spreads the options before you:

"The Cold Refuge in the Northern Mountains has space and basic structures
but would require days to set up governance operations. The Warm Sanctuary
in the Western Valley has some pre-positioned supplies and could be
operational in hours. The Hot Citadel in the Southern Fortress runs in
parallel with us - it has current records and can take over immediately
with no interruption."

What type of site allows IMMEDIATE failover with no data loss?
                """,
                "choices": [
                    {"text": "Cold Refuge - space and basic structures only"},
                    {"text": "Warm Sanctuary - some equipment, operational in hours"},
                    {"text": "Hot Citadel - fully synchronized, immediate takeover"},
                    {"text": "Mobile caravan - transportable but needs days to deploy"}
                ],
                "success_text": """
"Activate the Hot Citadel immediately!" you command.

Magical mirrors flash between the sites. Within moments, the Southern
Fortress assumes all kingdom operations. Because records were synchronized
in real-time, no decrees are lost, no treasury transactions are missing,
no communications are interrupted.

"Remarkable," the visiting ambassador observes. "I didn't even notice the
transition. Your governance continues uninterrupted."

The Master of Continuity nods. "Hot sites are expensive - we maintain a full
parallel operation at all times. But when disaster strikes, there is no
recovery time. We simply... continue."

Business continuity is about keeping critical operations running, no matter
what happens.
                """,
                "failure_texts": {
                    0: """
"The Cold Refuge?" By the time basic operations are established five days
later, three provinces have declared independence, the treasury records
are hopelessly confused, and the kingdom's enemies have exploited the
chaos.

Cold sites have space but nothing else. They're cheap but take days to
become operational. For immediate continuity, you need a hot site.
                    """,
                    1: """
"The Warm Sanctuary." Eight hours later, basic operations resume, but the
transition wasn't seamless. A full day of treasury records is missing.
Three important decrees were lost in the confusion.

Warm sites are faster than cold, but not immediate. For zero downtime and
zero data loss, you need a hot site with synchronous replication.
                    """,
                    3: """
"Mobile caravan?" The War Council stares. "That takes three days to deploy
and set up. We needed governance NOW!"

Mobile sites are portable but slow to become operational. For immediate
failover, you need a hot site that's already running.
                    """
                }
            },
            "corporate": {
                "title": "THE DATA CENTER DISASTER",
                "narrative": """
The call comes at 3 AM: the primary data center is offline. Fire suppression
activated after a transformer explosion, but the damage is extensive. Power
will not be restored for at least a week.

The BCP coordinator gathers the crisis team. "We have three recovery options
prepared. Which should we activate?"

She outlines the choices:

"Our cold site has rack space and power but no servers - we'd need to ship
and install equipment. Could take three to five days. The warm site has
hardware in place but needs current data restored from backup - four to
eight hours. The hot site runs in parallel with synchronous replication -
we can failover immediately with zero data loss."

The CEO is on the line: "Our trading platform cannot be down. Every minute
costs us $10,000. What type of site gives us IMMEDIATE failover with NO
data loss?"
                """,
                "choices": [
                    {"text": "Cold site - space and power, days to operational"},
                    {"text": "Warm site - hardware ready, hours to operational"},
                    {"text": "Hot site with synchronous replication - immediate failover, zero data loss"},
                    {"text": "Mobile site - transportable, days to deploy"}
                ],
                "success_text": """
"Activate the hot site," you direct. The team initiates failover.

Because of synchronous replication, every transaction that hit the primary
also hit the secondary in real-time. Within minutes, the trading platform
is running from the hot site. The morning's trading session opens on time.
Not a single transaction is lost.

"That's why we paid for a hot site," the CEO tells the board. "Zero downtime,
zero data loss. The investment pays for itself in a single incident like
this."

The hot site's continuous operation and real-time replication made the
difference between seamless continuity and catastrophic loss.
                """,
                "failure_texts": {
                    0: """
"Cold site?" The CEO's voice goes cold. "We'll be down for DAYS while you
ship and install equipment? Do you understand what that costs us?"

Five days later, when operations finally resume, the company has lost
millions in trading revenue, several major clients have left, and the
stock price has tanked. Cold sites are not for critical operations
requiring rapid recovery.
                    """,
                    1: """
"Warm site." Eight hours later, operations resume, but the last four hours
of transactions before the outage are missing - they weren't in the most
recent backup. Several million dollars in trades are lost or disputed.

Warm sites are faster than cold but not immediate. For zero data loss,
you need synchronous replication at a hot site.
                    """,
                    3: """
"Mobile site?" The CFO stares. "You want to TRUCK in equipment while our
trading platform is down? We'll be bankrupt before it's deployed!"

Mobile sites are for situations where fixed sites aren't available. For
immediate continuity of critical operations, you need a pre-established
hot site.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Business continuity sites have different levels of readiness: Cold sites have
space but no equipment (days to operational). Warm sites have equipment but
need data restored (hours). Hot sites run in parallel with synchronous
replication - immediate failover with zero data loss (RPO=0). The higher
the criticality, the hotter the site needed.
        """,
        "domain_reference": "Domain 7: Security Operations - Business Continuity"
    },

    # Scenario 11: Disaster Recovery (RTO/RPO)
    {
        "id": "d7_disaster_recovery",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE RECOVERY COVENANT",
                "narrative": """
The Grand Council is establishing recovery requirements for the kingdom's
critical operations. The Master of Records presents two key questions:

"First, the Royal Treasury processes gold transactions constantly. If the
Treasury Vault is destroyed, how long can we tolerate being unable to
process transactions before the kingdom's economy suffers irreparable harm?"

"Second, the Treasury ledgers are updated continuously. If we must restore
from backup records, how much lost transaction data can we tolerate before
merchants lose faith in our record-keeping?"

The Keeper of Numbers steps forward with scroll and quill. "We must define
these tolerances precisely. What do these two concepts represent?"
                """,
                "choices": [
                    {"text": "RTO: how often to test recovery procedures; RPO: how often to create backups"},
                    {"text": "RTO: maximum acceptable downtime; RPO: maximum acceptable data loss"},
                    {"text": "RTO: time to detect disasters; RPO: time to notify relevant parties"},
                    {"text": "RTO: budget for recovery operations; RPO: budget for backup systems"}
                ],
                "success_text": """
"RTO is our Recovery Time Objective," you explain. "It's the maximum time
we can tolerate the Treasury being non-operational. If we set RTO to four
hours, we MUST be able to restore Treasury operations within four hours of
any disaster."

"RPO is our Recovery Point Objective. It's the maximum data loss we can
tolerate, measured in time. If our RPO is one hour, we can lose at most
one hour of transaction records. This means we need backups at least every
hour."

The Keeper of Numbers nods approvingly. "So if RTO is four hours and RPO is
one hour, we need recovery capabilities that restore operations within
four hours, losing no more than one hour of data. These are our restoration
covenants."

The kingdom's recovery requirements are now clearly defined.
                """,
                "failure_texts": {
                    0: """
"Testing frequency and backup frequency?" The Master of Records frowns.
"No, those are operational practices. We're asking about recovery OBJECTIVES
- the acceptable limits of downtime and data loss."

RTO and RPO define what's acceptable, not how often you test or backup.
Testing and backup schedules should be designed to MEET your RTO/RPO.
                    """,
                    2: """
"Detection and notification times?" The Keeper of Numbers shakes his head.
"Those happen BEFORE recovery. We're asking about recovery OBJECTIVES - how
long until operations resume and how much data loss is acceptable."

Detection time and notification time are separate metrics. RTO/RPO focus
specifically on recovery outcomes.
                    """,
                    3: """
"Budget allocations?" The Treasury Minister chuckles. "While recovery does
cost money, RTO and RPO are TIME-based objectives, not budget metrics."

RTO is maximum acceptable downtime. RPO is maximum acceptable data loss
(measured in time). These are objectives that drive budgets, not budgets
themselves.
                    """
                }
            },
            "corporate": {
                "title": "THE DR PLANNING SESSION",
                "narrative": """
The disaster recovery planning committee is defining requirements for the
company's critical systems. The consultant poses two key questions:

"First, if your payment processing system goes down, how long can your
business tolerate that outage before losses become unacceptable? This drives
how fast you need to be able to recover."

"Second, your payment system processes transactions continuously. If you
have to restore from backup, how much transaction data can you afford to
lose? If you backup every four hours, you could lose up to four hours of
payments in a disaster."

The CTO asks for clarification: "What are these two concepts called, and
what do they mean precisely?"
                """,
                "choices": [
                    {"text": "RTO: how often to test recovery; RPO: how often to backup"},
                    {"text": "RTO: maximum acceptable downtime; RPO: maximum acceptable data loss"},
                    {"text": "RTO: time to detect disasters; RPO: time to notify staff"},
                    {"text": "RTO: budget for recovery; RPO: budget for backups"}
                ],
                "success_text": """
"RTO is Recovery Time Objective - the maximum time the system can be down
before business impact becomes unacceptable. If RTO is four hours, we must
be able to restore operations within four hours of any outage."

"RPO is Recovery Point Objective - the maximum data loss we can tolerate,
measured as a time period. If RPO is one hour, we can lose at most one hour
of transactions. This means we need backups or replication at least every
hour."

The consultant nods. "Exactly. So if your payment system RTO is four hours
and RPO is one hour, you need recovery solutions that can restore the
system within four hours while losing no more than one hour of data. Your
backup strategy, your recovery site, your replication - all must be designed
to meet these objectives."

The committee has clear targets to design against.
                """,
                "failure_texts": {
                    0: """
"Testing and backup frequency?" The consultant frowns. "No, those are
operational activities. RTO and RPO are OBJECTIVES - the acceptable limits
that those activities must be designed to meet."

RTO is about acceptable downtime. RPO is about acceptable data loss. Testing
and backup schedules are means to achieve those objectives.
                    """,
                    2: """
"Detection and notification?" The consultant shakes their head. "Those
happen during incident response, before recovery even begins. RTO and
RPO specifically measure recovery outcomes."

Detection time and notification time are different metrics entirely. RTO/RPO
focus on the recovery phase, not the detection phase.
                    """,
                    3: """
"Budget metrics?" The CFO laughs. "I wish RTO meant 'Recovery Treasure
Outlay,' but no. RTO and RPO are time-based objectives."

RTO is maximum acceptable downtime. RPO is maximum acceptable data loss
(in time). Budget is what you spend to achieve these objectives.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
RTO (Recovery Time Objective) is the maximum acceptable downtime - how long
systems can be unavailable before unacceptable business impact. RPO (Recovery
Point Objective) is the maximum acceptable data loss, measured as a time
period - losing up to 1 hour of data means RPO is 1 hour. These objectives
drive the design of backup and recovery solutions.
        """,
        "domain_reference": "Domain 7: Security Operations - Disaster Recovery"
    },

    # Scenario 12: Physical Security Operations
    {
        "id": "d7_physical_security",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE TAILGATING INTRUDER",
                "narrative": """
The morning guard briefing includes a concerning report. Yesterday, an
unauthorized person gained access to the Inner Sanctum by following closely
behind an authorized wizard as they passed through the warded doorway.

The Captain of the Guard is troubled. "The wards only check one person at
a time. When Master Aldrin opened the door, someone slipped through behind
him before it closed. Aldrin was distracted reading a scroll and didn't
notice."

The War Council demands solutions. "Posting 'no tailgating' signs has proven
ineffective - people ignore them or are too distracted. Adding more scrying
mirrors lets us SEE tailgaters but doesn't STOP them. We need something
that physically prevents this from happening."

What control BEST prevents tailgating?
                """,
                "choices": [
                    {"text": "Install additional scrying mirrors to observe entries"},
                    {"text": "Implement a mantrap - a double-door chamber that admits only one person at a time"},
                    {"text": "Post larger 'No Tailgating' warning signs"},
                    {"text": "Require stronger authentication passwords for door access"}
                ],
                "success_text": """
You propose the installation of a Chamber of Singular Passage - a mantrap.
The enchanted airlock consists of two doors that cannot both be open at
once, and a counting ward that only allows one person to pass per
authentication.

When Master Aldrin approaches now, he enters the first door, which seals
behind him. Only after the counting ward confirms exactly one person is
present does the inner door open. If someone tries to tailgate, the chamber
refuses to release - instead, an alarm sounds.

"Foolproof," the Captain of the Guard approves. "You cannot tailgate through
a mantrap no matter how distracted the authorized person is. The system
physically prevents more than one person per authentication."

The Inner Sanctum is now truly secure against tailgating.
                """,
                "failure_texts": {
                    0: """
"More scrying mirrors?" The Captain sighs. "Mirrors let us WATCH someone
tailgate, but they don't STOP them. The intruder still gets in - we just
have better footage of it happening."

Detective controls identify problems. Preventive controls stop them.
Tailgating requires a preventive physical control.
                    """,
                    2: """
"Bigger signs?" The War Council is unimpressed. "The wizard was reading a
scroll and didn't notice someone behind him. How would a bigger sign help?
And determined intruders ignore signs anyway."

Signs are awareness measures. They don't physically prevent tailgating.
                    """,
                    3: """
"Stronger passwords?" The Court Wizard frowns. "The authentication worked
correctly - Master Aldrin WAS authorized. The problem was someone slipping
through with him, not breaking the authentication."

Stronger authentication doesn't prevent tailgating. The authorized person
passed authentication; the issue is the unauthorized person following them.
                    """
                }
            },
            "corporate": {
                "title": "THE BADGE-SWIPE PROBLEM",
                "narrative": """
Physical security reviews the access logs and security footage. Yesterday,
an unauthorized individual accessed the secure development floor by walking
closely behind an authorized employee. The employee was on their phone and
didn't notice the person behind them.

The Security Director is frustrated. "This is the third tailgating incident
this month. We've posted signs, sent awareness emails, and reminded people
to be vigilant. But employees are distracted, polite, or just don't notice."

The CISO wants a permanent solution. "Awareness is clearly not enough.
People hold doors, don't pay attention, or feel rude challenging tailgaters.
We need something that physically prevents this, regardless of human behavior."

What control BEST prevents tailgating?
                """,
                "choices": [
                    {"text": "Install additional security cameras at entry points"},
                    {"text": "Implement a mantrap/airlock entry system"},
                    {"text": "Post 'No Tailgating' signs at all entrances"},
                    {"text": "Require longer, more complex badge PINs"}
                ],
                "success_text": """
"We need a mantrap," you recommend. The security team installs an airlock
system at the secure floor entrance: two sets of doors with a small chamber
between them.

When an employee badges in, the outer door opens and they enter the chamber.
The outer door must fully close before the inner door will open. Weight
sensors and occupancy detection ensure only one person passes per badge
swipe. If two people are detected in the chamber, neither door opens and
security is alerted.

"Problem solved," the Security Director reports after a month. "Zero
tailgating incidents. The mantrap doesn't care if someone is polite,
distracted, or on their phone. It physically prevents multiple people
from passing on a single authentication."

Tailgating is eliminated through physical controls, not awareness.
                """,
                "failure_texts": {
                    0: """
"More cameras?" The CISO shakes their head. "We already have footage of
the tailgating. Cameras are detective controls - they record incidents but
don't prevent them. The unauthorized person still got in."

Prevention requires physical controls. Cameras only provide evidence after
the fact.
                    """,
                    2: """
"More signs?" The Security Director gestures at the existing signs. "We
already have signs. People ignore them, are too polite to confront
tailgaters, or are simply distracted. Signs don't physically stop anyone."

Awareness measures have limited effectiveness. Physical prevention is needed.
                    """,
                    3: """
"Stronger PINs?" The access control vendor is confused. "The authentication
wasn't bypassed - the employee properly authenticated. The problem is
someone following them through the door before it closes."

Authentication strength is irrelevant to tailgating. The authorized person
passed authentication; the issue is the unauthorized person following them.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Mantraps (also called airlocks or interlocks) are enclosed entry systems where
only one door can be open at a time, ensuring only one person passes per
authentication. This PHYSICALLY prevents tailgating - the system won't allow
a second person through regardless of human behavior or awareness.
        """,
        "domain_reference": "Domain 7: Security Operations - Physical Security"
    },

    # Scenario 13: Personnel Security
    {
        "id": "d7_personnel_security",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE TROUBLED TREASURER",
                "narrative": """
The Royal Spymaster presents a concerning report about the Deputy Treasurer.
"Lord Blackwood controls access to significant gold reserves. Recently, my
sources report he has accumulated substantial gambling debts. He's been
seen working late into the night, alone in the Treasury. He appears anxious
and has declined his annual leave for three years."

The Master of Coin is troubled. "Blackwood has served faithfully for fifteen
years. But financial pressure combined with access to gold, working alone
without oversight, and never taking time off... these are warning signs."

The Council debates. "We cannot dismiss someone based on personal financial
troubles - that would be unjust. But we must address the risk without
rushing to harsh judgment."

What security principle addresses this risk appropriately?
                """,
                "choices": [
                    {"text": "Require mandatory vacation periods where others must perform his duties"},
                    {"text": "Immediately terminate Lord Blackwood based on the gambling debts"},
                    {"text": "Remove all his access permanently without investigation"},
                    {"text": "Ignore personal financial issues as irrelevant to security"}
                ],
                "success_text": """
"Mandatory vacation," you advise. "All personnel with sensitive access should
be required to take continuous leave periods during which their colleagues
must handle their responsibilities."

The policy is implemented. When Lord Blackwood takes his required two-week
leave, the substitute treasurer discovers discrepancies in the records -
small amounts that Blackwood had been 'borrowing' with intent to repay.

The early detection allows for quiet remediation. Blackwood admits his
mistakes, makes restitution, and receives counseling rather than prosecution.
The treasury controls are strengthened.

"Mandatory vacation is a detective control for insider threats," the
Spymaster explains. "It forces others to perform the duties, revealing
fraud or unauthorized activities that a single person could hide indefinitely."
                """,
                "failure_texts": {
                    0: """
"Immediate termination?" The Council is disturbed. "Based on personal
financial circumstances, without evidence of wrongdoing? That is unjust
and potentially illegal. Many people have debts without becoming thieves."

Termination based solely on personal circumstances is inappropriate.
Mandatory vacation is a fair control that applies to everyone and reveals
problems without presuming guilt.
                    """,
                    2: """
"Remove all access permanently?" Lord Blackwood's lawyers would have a
field day. "You've destroyed his career based on gossip about gambling
debts, without any evidence of actual wrongdoing."

This is excessive and unjust. Mandatory vacation is a reasonable control
that treats everyone fairly while revealing potential issues.
                    """,
                    3: """
"Ignore personal issues?" One year later, a full audit reveals Lord
Blackwood has embezzled 50,000 gold pieces to cover his gambling losses.
The kingdom is devastated - financially and reputationally.

Personal financial stress combined with access to assets is a known
insider threat indicator. Mandatory vacation would have revealed the
problem much earlier.
                    """
                }
            },
            "corporate": {
                "title": "THE AFTER-HOURS EMPLOYEE",
                "narrative": """
HR flags a concerning pattern about a senior financial analyst. The employee
has access to wire transfer systems and has been exhibiting warning signs:
visible financial stress (car repossessed, foreclosure notice), working
unusual late hours alone, and hasn't taken vacation in three years despite
multiple reminders.

The security team debates. "These are classic insider threat indicators -
financial pressure plus access plus opportunity. But we can't fire someone
just because they're having money problems. That would be discrimination."

The CISO agrees. "We need a control that addresses the risk fairly, without
punishing someone for personal circumstances. Something that applies to
everyone in sensitive positions."

What security principle appropriately addresses this risk?
                """,
                "choices": [
                    {"text": "Implement mandatory vacations for all employees in sensitive positions"},
                    {"text": "Immediately terminate the employee based on the financial stress"},
                    {"text": "Remove all access permanently without any investigation"},
                    {"text": "Ignore personal financial issues as not security-relevant"}
                ],
                "success_text": """
"Mandatory vacation policy," you recommend. "All employees with access to
sensitive systems must take at least one week of continuous vacation per
year, during which their colleagues handle their responsibilities."

The policy is implemented company-wide. When the financial analyst finally
takes mandated leave, the backup discovers subtle wire transfers to an
outside account - small amounts the analyst had been diverting.

The early detection limits the damage. The employee is dealt with through
appropriate channels, and internal controls are strengthened to require
dual authorization for wire transfers.

"Mandatory vacation is an elegant control," the CISO explains to the board.
"It forces regular rotation of duties, naturally revealing any hidden
activities. It's fair because it applies to everyone, and it's effective
because fraudsters can't hide forever when others must do their job."
                """,
                "failure_texts": {
                    0: """
"Immediate termination?" HR is alarmed. "You want to fire someone because
they're having financial problems? That's potentially illegal discrimination.
Many people face financial hardship without becoming criminals."

Termination without evidence is unjust. Mandatory vacation is a fair,
policy-based control that reveals problems without presuming guilt.
                    """,
                    2: """
"Remove all access with no investigation?" The employee's lawyer calls
the next day. "You've destroyed my client's career based on rumors about
their personal finances. We'll see you in court."

This response is both excessive and legally risky. Mandatory vacation
achieves security goals while treating people fairly.
                    """,
                    3: """
"Ignore it?" Two years later, a forensic audit reveals the employee
diverted $340,000 in small wire transfers over time. The financial pressure
was real; so was the theft.

Personal financial stress combined with system access is a well-documented
insider threat indicator. Ignoring it is negligent.
                    """
                }
            }
        },
        "correct_index": 0,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Mandatory vacation is a personnel security control that requires employees to
take continuous time off while others perform their duties. This can reveal
fraud or unauthorized activities that a single person could hide. Combined
with job rotation, it's an effective detective control for insider threats
that applies fairly to everyone without presuming guilt.
        """,
        "domain_reference": "Domain 7: Security Operations - Personnel Security"
    },

    # Scenario 14: Media Sanitization
    {
        "id": "d7_media_sanitization",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE DECOMMISSIONED MEMORY CRYSTALS",
                "narrative": """
The Treasury is upgrading its record-keeping system. Hundreds of memory
crystals containing decades of financial records - merchant transactions,
noble accounts, tax records - are being replaced. The old crystals must
be disposed of.

The Master of Secrets raises a concern: "These crystals contain sensitive
data. Merchant trading patterns, noble financial positions, tax payment
histories - in the wrong hands, this information could be used for
blackmail, market manipulation, or espionage."

The Treasury Clerk proposes: "We'll simply mark them as 'erased' and sell
them to the Mages' Academy for reuse. Memory crystals are expensive."

The Court Wizard shakes his head. "A skilled mage could recover those
'erased' memories easily. Marking them erased doesn't remove the data -
it just hides it."

What sanitization method ensures data cannot be recovered before resale?
                """,
                "choices": [
                    {"text": "Mark the crystals as 'erased' - that should be sufficient"},
                    {"text": "Remove all visible contents and empty the recycle vessel"},
                    {"text": "Apply the Shattering Ritual or degaussing enchantment to destroy data completely"},
                    {"text": "Remove the crystal labels so nobody knows what was on them"}
                ],
                "success_text": """
"Complete destruction is required," you decree. For crystals being reused
or sold, the Degaussing Enchantment completely scrambles the magical
patterns storing data - making recovery impossible even for master mages.

For crystals containing the most sensitive data, the Shattering Ritual
physically destroys them into powder that can never be reassembled.

The Court Wizard verifies each sanitized crystal. "I cannot recover a
single memory from these. The degaussing was complete. And the shattered
ones..." he gestures at a pile of crystal dust, "...are beyond any
recovery spell."

The sensitive records are truly gone, and the Treasury's secrets die with
the old storage system.
                """,
                "failure_texts": {
                    0: """
"Mark them erased?" The Court Wizard sighs. "Watch this." He takes a
'erased' crystal and performs a recovery spell. Transaction records,
noble accounts, and tax information flow forth in vivid detail.

"'Erasing' just marks space as available for reuse. The DATA remains
until overwritten. Any skilled mage can recover it."
                    """,
                    1: """
"Empty the recycle vessel?" The Court Wizard demonstrates: the 'emptied'
crystal still contains recoverable data. "Removing visible contents doesn't
touch the actual memory patterns. Those remain until properly sanitized."

Standard deletion leaves data fully recoverable.
                    """,
                    3: """
"Remove the labels?" The Court Wizard is incredulous. "The label says
nothing about the contents. Anyone with recovery skills can read what's
actually ON the crystal regardless of what's written ON it."

Labels are metadata. Data sanitization requires destroying the actual
data, not the labels.
                    """
                }
            },
            "corporate": {
                "title": "THE HARD DRIVE DONATION",
                "narrative": """
The company is refreshing its workstation fleet. 500 old hard drives, many
containing sensitive customer data, payment information, and internal
documents, need to be disposed of.

The sustainability committee proposes: "We should donate these to the
local school's computer lab. They could really use the storage."

IT security raises a concern: "These drives contain PII, financial data,
and confidential business information. We can't just hand them over."

The sustainability lead responds: "We'll do a quick format on each drive.
That erases everything, right?"

The security analyst shakes their head. "Quick format just clears the
file table. The actual data remains on the platters and is easily recovered
with free tools."

What sanitization method ensures data cannot be recovered before donation?
                """,
                "choices": [
                    {"text": "Quick format of the drives - that clears everything"},
                    {"text": "Delete all files and empty the recycle bin"},
                    {"text": "Degaussing or physical destruction of the drives"},
                    {"text": "Remove the drive labels so nobody knows what company they came from"}
                ],
                "success_text": """
"We have two options for proper sanitization," you explain. "For drives
being donated, we use degaussing - a powerful magnetic field that scrambles
all data on the platters beyond recovery. For drives containing the most
sensitive data, physical destruction - industrial shredding into small
fragments."

The process is implemented. Each drive is either degaussed with verification
that no data is recoverable, or physically shredded by a certified vendor
who provides certificates of destruction.

"The school gets properly sanitized drives they can safely use," you report.
"And our sensitive data is truly, irreversibly gone. This meets DoD and
NIST standards for media sanitization."

Data protection extends through the entire asset lifecycle, including
disposal.
                """,
                "failure_texts": {
                    0: """
"Quick format?" Three months later, the local news runs a story: 'School
Computer Finds Thousands of Customer Records on Donated Drives.' A
student's parent, who works in IT, recovered the data with free tools.

Quick format only clears the file system table. The actual data remains
on disk and is trivially recoverable.
                    """,
                    1: """
"Delete and empty recycle bin?" The compliance officer sighs and demonstrates:
using a free recovery tool, he retrieves thousands of 'deleted' files
from a test drive.

File deletion doesn't remove data from the physical disk. It marks space
as available for reuse. Recovery is trivial.
                    """,
                    3: """
"Remove labels?" The security auditor stares. "How does removing a sticker
protect the data stored on the magnetic platters? Anyone with a SATA cable
can read everything on that drive."

Labels are cosmetic. Data sanitization requires destroying the actual data,
not the labels.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Proper media sanitization for sensitive data requires degaussing (for magnetic
media) or physical destruction (shredding). Quick format and file deletion
only clear file tables - the actual data remains on disk and is easily
recovered. Before disposal, reuse, or donation of storage media, data must
be made unrecoverable through approved sanitization methods.
        """,
        "domain_reference": "Domain 7: Security Operations - Media Sanitization"
    },

    # Scenario 15: Investigations / E-Discovery
    {
        "id": "d7_ediscovery",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE IMPENDING TRIBUNAL",
                "narrative": """
A messenger from the Royal Court of Justice arrives with dire news. A
merchant guild is bringing a trade dispute before the Tribunal, claiming
your kingdom's trade ministry engaged in unlawful practices. The Tribunal
requires preservation of all correspondence, transaction records, and
internal communications related to the matter.

The Master of Records approaches you urgently. "Our standard practice
destroys routine correspondence after one year. The oldest relevant
documents are approaching that date. What do we do?"

The Court Advisor warns: "Destroying documents after we've been notified
of the Tribunal's requirements would be viewed as spoliation - destruction
of evidence. The penalties for that are severe - the Tribunal may assume
the destroyed documents would have proven our guilt."

What is your IMMEDIATE obligation?
                """,
                "choices": [
                    {"text": "Destroy the correspondence to protect sensitive information"},
                    {"text": "Issue a preservation order halting all destruction of relevant documents"},
                    {"text": "Continue normal retention practices - the Tribunal hasn't formally started yet"},
                    {"text": "Let the legal advisors handle it - records management isn't their concern"}
                ],
                "success_text": """
"Issue a preservation order immediately!" you command. Royal messengers
race throughout the kingdom with sealed scrolls: all document destruction
is halted for anything potentially related to the trade ministry matter.

The Master of Records implements the hold: "All correspondence involving
trade agreements, merchant communications, and ministry decisions is now
preserved regardless of age. Our normal destruction schedule is suspended
for these documents until the Tribunal concludes."

When the Tribunal convenes months later, your advocate presents a complete
record. The opposing guild attempts to claim you destroyed evidence, but
your preservation order - with its timestamp and scope - proves otherwise.

"Proper preservation demonstrates good faith," the Tribunal notes. "This
kingdom has complied with all obligations."
                """,
                "failure_texts": {
                    0: """
"Destroy the documents?" The Court Advisor turns pale. "After receiving
notice of the Tribunal's interest? That is spoliation of evidence!"

At the Tribunal, the opposing guild presents evidence of your post-notice
destruction. The judges draw an adverse inference: destroyed documents
are presumed to have supported the opposition's claims. Your kingdom
suffers severe penalties.

Never destroy evidence after receiving legal hold notice.
                    """,
                    2: """
"Continue normal practices?" Two months later, at the Tribunal, the
opposing advocate demands documents that no longer exist - destroyed under
'normal retention.'

"You were notified of this matter," the judge frowns. "Yet you allowed
document destruction to continue? That is spoliation." Severe sanctions
follow.

Legal hold requirements begin when you're notified, not when proceedings
formally begin.
                    """,
                    3: """
"Not our concern?" Unfortunately, the legal advisors don't control the
records. By the time they realize documents are being destroyed, critical
evidence is gone.

At the Tribunal: "The kingdom claims its records department wasn't
properly instructed. That is not a defense - it's an admission of
internal failure." Sanctions for spoliation are imposed.

IT/Records controls the data and must implement preservation.
                    """
                }
            },
            "corporate": {
                "title": "THE LITIGATION HOLD",
                "narrative": """
The General Counsel bursts into the IT director's office. "We just received
notice that a former employee is suing the company for wrongful termination.
The plaintiff's attorney has demanded preservation of all emails, documents,
and communications related to this employee's tenure and termination."

The IT director checks the retention policies. "Our standard policy deletes
emails older than 90 days. Some of the relevant communications are
approaching that threshold."

The General Counsel is emphatic: "If we delete any of that data now, after
receiving this notice, it's spoliation. Courts can sanction us, draw
adverse inferences, or even enter default judgment against us. We could
lose the case without it ever being decided on merits."

What is IT's IMMEDIATE obligation?
                """,
                "choices": [
                    {"text": "Delete the emails to protect employee privacy"},
                    {"text": "Issue a legal hold to preserve all relevant data"},
                    {"text": "Continue normal retention policies - the lawsuit hasn't been filed yet"},
                    {"text": "Let Legal handle it - IT doesn't deal with lawsuits"}
                ],
                "success_text": """
"We'll implement a legal hold immediately," you confirm. Within hours,
the email system is configured to preserve all communications involving
the former employee, the HR department, the employee's manager, and
anyone involved in the termination decision.

A company-wide notification is sent to relevant custodians: "Do not delete
any documents, emails, or files related to [employee name] or their
termination. Automatic deletion is suspended for these records."

When discovery proceeds, the company can produce a complete record. The
opposing attorney's attempt to claim spoliation fails - the legal hold
documentation shows immediate action to preserve all relevant data.

"Proper e-discovery preservation," your attorney notes, "prevented what
could have been catastrophic sanctions."
                """,
                "failure_texts": {
                    0: """
"Delete the emails?" The General Counsel nearly faints. "After we received
a preservation demand? That's textbook spoliation!"

During discovery, the opposing attorney subpoenas email server logs showing
large-scale deletions after the notice date. The judge imposes sanctions
and an adverse inference instruction: the jury is told to assume deleted
emails would have supported the plaintiff.

The case, which might have been winnable, is effectively lost.
                    """,
                    2: """
"Continue normal retention?" Three months into litigation, the plaintiff's
attorney demands emails that were auto-deleted under 'normal policies'
after you received the preservation notice.

"Your Honor, the defendant continued deleting emails AFTER receiving our
preservation demand." The judge is not impressed. Sanctions for spoliation
are substantial.

Legal hold obligations begin when you reasonably anticipate litigation.
                    """,
                    3: """
"Not IT's problem?" Legal doesn't control the email server. By the time
they realize data is being deleted, critical communications are gone.

In court: "The defendant claims their IT and Legal departments failed to
coordinate. That internal failure doesn't excuse spoliation." The sanctions
are severe.

IT controls the data - they must implement the preservation.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
A legal hold (litigation hold) suspends normal data destruction when litigation
is reasonably anticipated. Once you receive notice of potential legal action,
continuing to delete relevant data is spoliation - destruction of evidence -
which can result in severe sanctions, adverse inferences, or losing the case
entirely. IT must implement the hold because IT controls the data.
        """,
        "domain_reference": "Domain 7: Security Operations - E-Discovery"
    },

    # Scenario 16: Security Monitoring
    {
        "id": "d7_security_monitoring",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE OVERWHELMED WATCHERS",
                "narrative": """
The Sentinel Tower receives reports from across the kingdom - suspicious
travelers, unusual magical signatures, potential threats. But the Chief
Sentinel is drowning.

"We receive ten thousand reports daily," he explains wearily. "We can
only investigate perhaps one hundred. Most reports are false alarms or
minor issues, but buried in there somewhere are real threats. Last week,
we missed a genuine assassination plot because the report was lost in the
noise."

The Captain of the Guard examines the situation. "Some reports are clearly
more important than others. A suspicious person in the marketplace is
less urgent than a known assassin spotted near the castle. And many of
these reports - like 'stranger wearing a hood' - are too broad to be useful."

What should be done to make the alert volume manageable?
                """,
                "choices": [
                    {"text": "Ignore all alerts since there are too many to handle"},
                    {"text": "Tune alert thresholds and implement prioritization - focus on high-severity threats first"},
                    {"text": "Investigate alerts randomly - fairness is important"},
                    {"text": "Disable the sentinel network to eliminate the alert flood"}
                ],
                "success_text": """
You implement a two-part solution. First, alert tuning: 'stranger in hood'
is too vague and generates too many false positives - the threshold is
raised to require additional suspicious indicators. Second, prioritization:
threats near critical areas or involving known adversaries are flagged
as high priority and investigated first.

Within a month, the transformation is remarkable. Alert volume has dropped
to 3,000 daily (tuning eliminated the false positives), and sentinels
investigate the highest-priority threats first. The assassination plot
from last week? Similar reports are now immediately escalated.

"We're no longer drowning," the Chief Sentinel reports. "We focus on what
matters, and the false alarms no longer bury real threats."

Effective monitoring requires tuning and prioritization, not just more
alerts.
                """,
                "failure_texts": {
                    0: """
"Ignore all alerts?" The next week, a real threat is missed because it
was among the 'ignored' alerts. The kingdom suffers an attack that could
have been prevented.

The solution isn't to ignore everything - it's to filter and prioritize
so important alerts get attention.
                    """,
                    2: """
"Random investigation?" By chance, the sentinels spend days investigating
'suspicious cat behavior' while the genuine assassination plot goes
uninvestigated. The king narrowly survives.

Random investigation doesn't prioritize critical threats. High-severity
alerts must be investigated first.
                    """,
                    3: """
"Disable the sentinel network?" The kingdom goes blind. Without any
monitoring, threats arrive without warning. The first indication of the
invasion is when enemy troops appear at the gates.

Some monitoring is essential. The solution is better monitoring, not
no monitoring.
                    """
                }
            },
            "corporate": {
                "title": "THE SOC ALERT NIGHTMARE",
                "narrative": """
The SOC team lead presents the problem at the security committee meeting.
"We're getting 10,000 alerts per day. We can investigate maybe 100. Our
analysts are burned out, real threats are getting missed, and morale is
in the toilet."

The CISO examines the alert dashboard. "I see thousands of 'failed login
attempt' alerts - most are probably users mistyping passwords. And these
'suspicious outbound connection' alerts - half of them are just marketing
analytics platforms. Meanwhile, the alert for lateral movement yesterday
was buried so deep that nobody saw it until the damage was done."

The team lead nods. "We're drowning in noise. The important stuff is
getting lost. But we can't just ignore alerts - what if we miss something?"

What should be done?
                """,
                "choices": [
                    {"text": "Ignore all alerts since there are too many to process"},
                    {"text": "Tune alert thresholds and implement prioritization"},
                    {"text": "Investigate alerts randomly to ensure fairness"},
                    {"text": "Disable monitoring entirely to eliminate the alert flood"}
                ],
                "success_text": """
"Two things," you recommend. "Alert tuning and prioritization."

Over the next month, the team refines alert rules: single failed logins
no longer alert (threshold raised to 5 failures in 10 minutes); known-good
analytics platforms are whitelisted; and overly broad signatures are made
more specific.

Simultaneously, remaining alerts are prioritized: lateral movement,
privilege escalation, and data exfiltration patterns are flagged critical
and investigated first. Low-priority alerts (normal user behavior that's
slightly unusual) are batched for weekly review.

"Alert volume is down to 2,000 per day," the team lead reports after a
month. "And analysts actually look at the critical queue first. We haven't
missed a single high-priority threat."

The SOC is functioning effectively again.
                """,
                "failure_texts": {
                    0: """
"Ignore all alerts?" Two weeks later, ransomware encrypts the entire
domain. The alerts were there - lateral movement, suspicious SMB traffic,
unusual service account activity - but they were being 'ignored.'

The solution isn't to ignore everything; it's to make alerts actionable
through tuning and prioritization.
                    """,
                    2: """
"Random investigation?" The analysts spend a week investigating false
positives selected at random while a genuine APT quietly exfiltrates
customer data. The critical alerts were there - just not randomly selected.

Random investigation doesn't prioritize threats by severity. Critical
alerts must be investigated first.
                    """,
                    3: """
"Disable monitoring?" The CISO stares. "You want to fly completely blind?
Do you know what happens to organizations with no security monitoring?"

Six months later, the breach investigation reveals attackers were in the
network for four months. With no monitoring, there was nothing to detect
them.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Effective security monitoring requires alert tuning (reducing false positives
by adjusting thresholds and rules) and prioritization (ensuring high-severity
threats are investigated first). Without these, SOC teams drown in noise
and miss genuine threats. The goal is actionable alerts, not more alerts.
        """,
        "domain_reference": "Domain 7: Security Operations - Security Monitoring"
    },

    # Scenario 17: Problem Management
    {
        "id": "d7_problem_management",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE RECURRING BREACH",
                "narrative": """
The War Council reviews the incident log with growing frustration. "This
is the THIRD time in two moons that infiltrators have entered through the
Eastern Sewers. Each time, we catch them, expel them, and repair the damage.
And each time, they return using the same route."

The Captain of the Guard is defensive. "We've handled each incident perfectly.
Detection was rapid, response was effective, the intruders were expelled,
and operations resumed quickly."

The Grand Strategist shakes his head. "You've treated the symptoms three
times, but the disease remains. Why do infiltrators keep choosing the
Eastern Sewers? What is it about that route that makes it attractive? And
how do we fix the underlying vulnerability so this stops happening?"

What process should address the ROOT CAUSE to prevent recurrence?
                """,
                "choices": [
                    {"text": "Incident management - handle each occurrence as it happens"},
                    {"text": "Problem management - identify and fix the root cause"},
                    {"text": "Change management - approve changes to the sewer"},
                    {"text": "Release management - deploy updates to defenses"}
                ],
                "success_text": """
"We need problem management," you explain. "Incident management addresses
individual events. Problem management asks WHY incidents recur and
implements permanent fixes."

A problem investigation is launched. The team discovers that the Eastern
Sewer's detection wards have a blind spot where two coverage areas don't
overlap. Infiltrators have learned to exploit this gap.

The root cause identified, a permanent fix is designed: overlapping ward
coverage with no gaps. Once implemented, infiltration attempts through
the Eastern Sewer drop to zero.

"Problem management prevents recurrence," the Grand Strategist approves.
"We're no longer repeatedly treating the same wound. We've healed it
permanently."
                """,
                "failure_texts": {
                    0: """
"Keep handling each occurrence?" The fourth infiltration occurs the next
week. Then the fifth. Then the sixth.

"We're very good at handling these incidents," the Captain notes proudly.
"But shouldn't we, perhaps, stop them from happening?"

Incident management handles events. Problem management prevents recurrence.
                    """,
                    2: """
"Change management?" The Change Council asks: "Change what, exactly? We
need to know what's broken before we can approve a fix."

Change management approves changes. Problem management identifies what
changes are needed by analyzing root causes.
                    """,
                    3: """
"Release management?" The deployment team asks: "Deploy what? We don't
have a solution to deploy - we don't even know what the problem is."

Release management deploys solutions. Problem management identifies what
solutions are needed through root cause analysis.
                    """
                }
            },
            "corporate": {
                "title": "THE RECURRING PHISHING PROBLEM",
                "narrative": """
The security team lead reviews the quarterly metrics with frustration.
"This is the THIRD major phishing incident in two months. Each time, users
click malicious links, credentials get stolen, and we reset passwords and
clean up the mess. And each time, it happens again."

The SOC manager is proud of the response. "Our incident response is
excellent. Average time from detection to containment is under two hours.
We have playbooks, we have tools, we have trained staff."

The CISO interrupts: "You're very good at mopping the floor. But you
haven't turned off the faucet. Why do users keep clicking these links?
What is it about our defenses that lets these phishing emails through?
And how do we stop this from happening again?"

What process should address the ROOT CAUSE?
                """,
                "choices": [
                    {"text": "Incident management - handle each phishing event as it occurs"},
                    {"text": "Problem management - identify and fix the root cause of recurring incidents"},
                    {"text": "Change management - approve changes to email systems"},
                    {"text": "Release management - deploy patches to email servers"}
                ],
                "success_text": """
"We need problem management," you recommend. "Incident management handles
individual events. Problem management investigates why they keep recurring."

The problem investigation reveals multiple root causes: email filtering
isn't catching lookalike domains, security awareness training hasn't been
updated in two years, and there's no mechanism for users to report
suspicious emails.

Permanent fixes are implemented: enhanced email filtering with lookalike
domain blocking, refreshed security awareness training with phishing
simulations, and a simple 'Report Phishing' button in the email client.

Three months later, phishing incidents have dropped 90%. "Problem management
turned off the faucet," the CISO notes. "We're not just mopping anymore."
                """,
                "failure_texts": {
                    0: """
"Keep handling each incident?" The fourth phishing campaign succeeds the
next month. Then the fifth. Then the sixth.

"Our incident response metrics are excellent," the SOC manager notes.
"But shouldn't we, you know, stop having so many incidents?"

Incident management responds to events. Problem management prevents them.
                    """,
                    2: """
"Change management?" The CAB asks: "What change are you proposing? We
approve changes - we don't identify what changes are needed."

Change management is the approval process. Problem management identifies
what needs to change through root cause analysis.
                    """,
                    3: """
"Release management?" The deployment team asks: "Deploy what? We need a
solution before we can deploy it."

Release management handles deployment. Problem management identifies
what solutions are needed by analyzing root causes.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Problem management focuses on identifying root causes of recurring incidents
and implementing permanent fixes. Incident management handles individual
occurrences but doesn't prevent recurrence. When the same incident type
keeps happening, problem management investigates why and implements systemic
solutions.
        """,
        "domain_reference": "Domain 7: Security Operations - Problem Management"
    },

    # Scenario 18: Resource Protection (Deprovisioning)
    {
        "id": "d7_deprovisioning",
        "domain": 7,
        "themes": {
            "fantasy": {
                "title": "THE DEPARTED GUARDIAN",
                "narrative": """
Two weeks ago, Sir Aldric left the Citadel Guard under bitter circumstances
after a dispute with the Captain. Today, a sentry reports something alarming:
Sir Aldric was seen entering the barracks at midnight using his old access
crystal, which still functions.

The Captain of the Guard is furious. "He was terminated fourteen days ago!
Why does his crystal still work? Why wasn't his access to the barracks
revoked?"

Investigation reveals a troubling pattern: the provisioning office creates
access crystals for new guardians promptly, but there's no corresponding
process for deactivating them when guardians depart. Sir Aldric's crystal
was simply... never disabled.

What operational process failure does this indicate?
                """,
                "choices": [
                    {"text": "Background check process failure - we shouldn't have hired him"},
                    {"text": "Account provisioning and deprovisioning failure - access wasn't revoked upon departure"},
                    {"text": "Training program failure - he should have known to return his crystal"},
                    {"text": "Encryption key management failure - the crystals should use stronger magic"}
                ],
                "success_text": """
"This is a deprovisioning failure," you explain. "We have good processes
for granting access - provisioning. But we have no corresponding process
for revoking access when someone leaves - deprovisioning."

You implement an immediate fix: all access must be revoked on or before
a guardian's final day. A checklist ensures all access points are covered:
gate crystals, barracks entry, armory access, training ground permissions,
communication crystals, and any special authorizations.

A weekly audit compares the active guardian roster to active access
permissions, flagging any discrepancies immediately.

"Deprovisioning is now part of our standard offboarding," the Captain
reports. "No former guardian will have active access after departure."
                """,
                "failure_texts": {
                    0: """
"Background check failure?" The Provost shakes his head. "Sir Aldric's
background check was thorough. The problem isn't that we hired him - it's
that his access wasn't revoked when he left."

Background checks are pre-employment. Deprovisioning is at termination.
Different processes, different failures.
                    """,
                    2: """
"Training failure?" The Training Master is confused. "Train him to do what?
Voluntarily surrender his functioning access crystal? That's not realistic.
The SYSTEM should have disabled it automatically."

Relying on departed personnel to self-revoke access is not a control.
Deprovisioning must be a managed, systematic process.
                    """,
                    3: """
"Encryption key management?" The Court Wizard sighs. "The crystal's magic
is perfectly strong. The problem is that his AUTHORIZATION was never
revoked. Stronger encryption doesn't fix that."

The crystal worked correctly - it authenticated a valid credential. The
problem was that the credential should no longer have been valid.
                    """
                }
            },
            "corporate": {
                "title": "THE GHOST BADGE",
                "narrative": """
Security calls with an alarming report: an access card that should have
been deactivated two weeks ago was just used to enter the building at
11:47 PM. Badge records show it belongs to a terminated employee - one
who left under acrimonious circumstances after a heated dispute with
management.

HR confirms: the employee was terminated fourteen days ago. But their
badge? Still active in the access control system. Their Active Directory
account? Still enabled. Their VPN credentials? Still valid.

The CISO is furious. "This person left two weeks ago! Why do they still
have access to ANYTHING?"

Investigation reveals there's no formal deprovisioning process. Provisioning
new employees is well-documented, but there's no checklist or process for
removing access when they leave.

What operational process failure does this indicate?
                """,
                "choices": [
                    {"text": "Background check process failure - we shouldn't have hired them"},
                    {"text": "Account/access provisioning and deprovisioning failure"},
                    {"text": "Training program failure - they should have returned their badge"},
                    {"text": "Encryption key management failure - badges should use stronger encryption"}
                ],
                "success_text": """
"This is a deprovisioning failure," you explain. "We're good at giving
people access when they join - that's provisioning. But we have no matching
process for taking it away when they leave - that's deprovisioning."

You work with HR and IT to create a comprehensive offboarding checklist:
badge deactivation, AD account disable, VPN revocation, email access
removal, application access removal, and physical key collection - all
completed on or before the employee's last day.

An automated report now compares HR's employee roster to active access
accounts daily, flagging any orphaned access immediately.

"No terminated employee will have lingering access," you report. "The
process gap is closed."
                """,
                "failure_texts": {
                    0: """
"Background check failure?" HR is confused. "Their background check was
fine when we hired them. The problem isn't the hiring decision - it's
that their access wasn't removed when they left."

Background checks happen at hiring. Deprovisioning happens at termination.
Completely different processes.
                    """,
                    2: """
"Training failure?" The security team stares. "You think we should train
terminated employees to please remember to return their badges and disable
their own accounts? That's not how access management works."

Deprovisioning must be a managed, systematic process. Relying on departed
employees to self-revoke access is not a control.
                    """,
                    3: """
"Encryption on badges?" The badge vendor rep sighs. "The badge encryption
is fine. It authenticated correctly - the problem is that it SHOULD no
longer have been valid. That's not an encryption issue."

The authentication worked. The AUTHORIZATION should have been revoked.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Deprovisioning is the process of revoking all access - logical and physical -
when an employee leaves the organization. It should occur on or before the
employee's last day and must be comprehensive: badge access, system accounts,
VPN, applications, and any special permissions. Failure to deprovision
leaves organizations vulnerable to former employee access.
        """,
        "domain_reference": "Domain 7: Security Operations - Resource Protection"
    },
]
