"""
Domain 1: Security and Risk Management scenarios.

Key CISSP concepts tested:
- Life Safety Priority
- Risk Management frameworks
- Business Continuity Planning
- Security Governance
- Ethics and Professional Conduct

Each scenario supports dual themes:
- Fantasy: Medieval/magical Citadel setting
- Corporate: Modern office satire (Office Space style)
"""

DOMAIN_1_SCENARIOS = [
    # Scenario 1: Life Safety Priority
    {
        "id": "d1_fire_scroll_room",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "FIRE IN THE SCROLL ROOM",
                "narrative": """
The acrid smell of smoke reaches your nostrils before the alarm bells begin their
frantic clanging. You round the corner to find the Great Scroll Room engulfed in
angry orange flames. The ancient archives - containing irreplaceable magical
codices and the kingdom's most sensitive decryption keys - are being consumed.

Through the smoke, you spot three scribes trapped behind a collapsed bookshelf,
their cries barely audible over the roar of the flames. The Master Archivist
shouts that the backup scrolls haven't been copied to the off-site vault in
three moons.

The heat is intense. You have moments to act. The fire brigade is still
minutes away.

What do you do?
                """,
                "choices": [
                    {"text": "Rush to save the scribes - their lives are irreplaceable"},
                    {"text": "Secure the encryption keys first - if compromised, the kingdom's communications are at risk"},
                    {"text": "Attempt to salvage the ancient codices - they contain centuries of accumulated knowledge"},
                    {"text": "Run to activate the magical suppression system to save everything at once"}
                ],
                "success_text": """
You charge through the smoke, the heat searing your lungs. With strength born
of purpose, you help lift the bookshelf and guide the three scribes to safety
just as the ceiling begins to groan.

Outside, catching your breath, the Master Archivist clasps your shoulder.
"The scrolls can be rewritten. The keys can be regenerated. But Elara, Marcus,
and young Pip - they cannot be replaced. You understood what truly matters."

The fire brigade arrives and contains the blaze. Though the Scroll Room
suffered losses, the most valuable assets - your fellow guardians - survive
to rebuild and protect another day.

You have demonstrated the first and most sacred principle: LIFE SAFETY
is always the highest priority.
                """,
                "failure_texts": {
                    1: """
While protecting cryptographic materials is crucial for information security,
you have placed data above human life. The CISSP Code of Ethics and fundamental
security principles establish that LIFE SAFETY is always the highest priority.
No data, no matter how sensitive or valuable, justifies risking human lives.
The scribes perished. Their knowledge and experience are truly irreplaceable.
                    """,
                    2: """
The ancient codices, while historically invaluable, are still just records.
They can potentially be reconstructed, researched anew, or may exist in
other forms. Human lives cannot be restored. By choosing artifacts over
people, you have violated the fundamental principle that safety of personnel
always takes precedence over property and information.
                    """,
                    3: """
While this seems like a clever solution, the suppression system takes time
to activate and may not reach the trapped scribes in time. In emergency
situations, you must prioritize immediate threats to life over technical
solutions that may or may not work. Direct action to save lives takes
precedence when lives are in immediate danger.
                    """
                }
            },
            "corporate": {
                "title": "FIRE IN THE SERVER ROOM",
                "narrative": """
The fire alarm pierces through the open-plan office. "THIS IS NOT A DRILL"
crackles over the PA system. You rush toward Building B's server room.

Through the glass wall, you see the nightmare scenario: smoke billowing from
a rack, sparks flying from a damaged PDU, and three contractors from the
overnight migration team trapped behind a collapsed server cabinet.

Your manager's voice echoes in your head from last week's all-hands: "Our
backup rotation is three days behind. If we lose those servers, Q4 is toast."

The contractors are banging on the glass. The fire suppression hasn't
triggered. Security is nowhere in sight.

What do you do?
                """,
                "choices": [
                    {"text": "Call 911 and help evacuate the contractors - people first"},
                    {"text": "Run to the tape safe to grab this week's backup tapes"},
                    {"text": "Try to gracefully shut down the production database"},
                    {"text": "Sprint to the electrical room to kill power to the floor"}
                ],
                "success_text": """
You're already dialing 911 as you grab the fire extinguisher from the wall.
"Building B, server room fire, three people trapped!" While the dispatcher
sends help, you smash the emergency release on the server room door.

Together, you and the contractors escape through the loading dock just as
the fire department arrives. One contractor has minor burns; all three will
be okay.

Your manager catches up to you outside, ashen-faced. "The backups? The
production DB?"

"Replaceable," you say. "Dave, Maria, and the new guy? Not so much."

He nods slowly. "HR is going to give you an award. And I'm going to fix
that backup rotation first thing Monday."

LIFE SAFETY always comes first. The CISSP Code of Ethics is clear:
protect society, the common good, and the infrastructure - and people
ARE the infrastructure that matters most.
                """,
                "failure_texts": {
                    1: """
You grabbed backup tapes while three people were trapped in a burning
server room. Sure, the tapes survived. Dave from the contractor team?
Second-degree burns. Maria? Smoke inhalation, two weeks in the hospital.

At the incident review, the CISO looked at you and said one thing:
"No backup tape is worth a human life. Ever."

LIFE SAFETY is the first priority in any emergency. Data can be restored.
People cannot.
                    """,
                    2: """
"Graceful shutdown"? Really? While people are trapped and smoke is filling
the room? By the time you initiated the shutdown sequence, the contractors
had to break through a window to escape.

Production was down for 72 hours anyway due to fire damage. Your "graceful
shutdown" saved nothing and delayed evacuation of personnel.

When lives are at risk, technical procedures take a back seat. ALWAYS.
                    """,
                    3: """
Cutting power seemed logical, right? Except: the server room door is
electronically locked, and cutting power trapped the contractors inside
even longer. The fire suppression system is also electronic - it never
triggered.

One contractor is in the ICU. Your "logical" decision nearly killed him.

In emergencies, your first priority is HUMAN LIFE, not systems. Call for
help, evacuate people, then worry about infrastructure.
                    """
                }
            }
        },
        "correct_index": 0,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
In information security, we protect many things: data, systems, secrets, and
operations. But above all else, we protect PEOPLE. The CISSP emphasizes that
life safety must always be the top priority in any security decision. No
amount of data, no matter how critical, is worth a human life.
        """,
        "domain_reference": "Domain 1: Security and Risk Management - Safety Priority, CISSP Code of Ethics"
    },

    # Scenario 2: Risk Assessment
    {
        "id": "d1_merchants_dilemma",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "THE MERCHANT'S DILEMMA",
                "narrative": """
The Grand Merchant approaches you with worry creasing his weathered face.
His caravans carry gold, spices, and most importantly, sealed diplomatic
pouches between the kingdoms.

"Three routes lie before us," he explains, spreading a map across the table.
"The Northern Pass is swift but plagued by bandits - we lose one in four
caravans. The Eastern Road is longer but safer - only one in twenty is lost.
The Southern Marshes... none who enter are ever seen again, though the
journey would be shortest."

He looks at you intently. "The Council demands I calculate our acceptable
level of loss. They speak of 'risk appetite' and 'residual risk.' I am but
a merchant. What framework should guide my decision?"

How do you advise the Merchant?
                """,
                "choices": [
                    {"text": "Always choose the safest route regardless of cost - security cannot have a price"},
                    {"text": "Calculate the expected loss for each route, compare against acceptable risk levels, then choose accordingly"},
                    {"text": "Take the Southern Marshes - the potential reward of the shortest route outweighs unknown risks"},
                    {"text": "Refuse all routes until the bandits are eliminated and the marshes are explored"}
                ],
                "success_text": """
The Merchant's eyes light up with understanding. "Ah! So I must weigh the
VALUE of what might be lost against the LIKELIHOOD of losing it!"

You nod. "Precisely. The Northern Pass loses 25% of caravans - if each
carries 100 gold in goods, you expect to lose 25 gold per journey on average.
The Eastern Road loses 5% - only 5 gold expected loss, even if the journey
takes longer."

"And the Southern Marshes?"

"Unknown threats with 100% historical loss rate represent unacceptable risk,
regardless of the time saved. We cannot make informed decisions about risks
we do not understand."

The Merchant bows gratefully. "You have given me a framework for all future
decisions. The Council shall hear of your wisdom."

You have demonstrated proper RISK ASSESSMENT methodology.
                """,
                "failure_texts": {
                    0: """
While admirable in sentiment, absolute security is neither achievable nor
practical. Risk management requires balancing security with business needs.
An organization that spends all resources on eliminating risk will have
nothing left to protect. The CISSP framework emphasizes that security must
enable business operations, not paralyze them with impossible standards.
                    """,
                    2: """
Choosing a path with unknown but potentially catastrophic consequences
violates fundamental risk management principles. 'None who enter are ever
seen again' represents an unquantified risk with potentially infinite loss.
Risk management requires understanding threats before accepting them.
Unknown risks must be investigated, not blindly accepted for convenience.
                    """,
                    3: """
While threat elimination is ideal, waiting for perfect security means
never conducting business. Risk management acknowledges that some risk
is inherent in all activities. The goal is not zero risk (which is
impossible) but rather managed, acceptable risk that allows operations
to continue while protecting critical assets proportionally.
                    """
                }
            },
            "corporate": {
                "title": "THE VENDOR SELECTION",
                "narrative": """
The VP of Operations corners you in the elevator. "I need your security
assessment on these cloud vendors by end of day. The board wants answers."

She hands you three proposals:

"CloudCheap Inc. - Half the price of everyone else. They're new, no SOC 2
report yet, but they promise their security is 'military grade.' Reviews
online are... mixed. Some customers report data losses."

"SecureCloud Pro - Industry standard pricing, SOC 2 Type II certified,
been around for a decade. Boring but reliable."

"MysteryCloud - Cheapest of all, no website, no documentation. Someone
on Reddit said they're amazing. CEO is 'definitely not in a country with
no extradition treaties.'"

The VP taps her watch. "Finance is pushing for the cheapest option. What's
your recommendation framework?"

How do you advise on this vendor risk assessment?
                """,
                "choices": [
                    {"text": "Always choose the most secure option regardless of cost - security is priceless"},
                    {"text": "Assess each vendor's risk profile against our risk tolerance, then make a cost-benefit decision"},
                    {"text": "Go with MysteryCloud - the cost savings outweigh the unknowns"},
                    {"text": "Reject all vendors until we can eliminate all possible risks"}
                ],
                "success_text": """
You pull out your risk assessment framework. "Here's how we approach this:

CloudCheap has a 25% customer complaint rate about data issues. With our
data volume, that's unacceptable risk.

SecureCloud Pro has a 2% incident rate over 10 years, all properly disclosed
and remediated. The higher cost buys us validated controls and accountability.

MysteryCloud... I can't even verify they're a real company. Unknown risks
with potentially catastrophic outcomes? That's a non-starter."

The VP nods. "So it's not about the cheapest option?"

"It's about the option that balances cost against acceptable risk. SecureCloud
isn't the cheapest, but their risk profile fits our tolerance. CloudCheap's
savings don't outweigh their incident rate. And MysteryCloud..."

"Is probably a guy in a basement."

"Probably."

You have demonstrated proper RISK ASSESSMENT methodology.
                """,
                "failure_texts": {
                    0: """
"Security is priceless" sounds great in a security awareness poster, but
it doesn't work in a budget meeting. The CISSP framework emphasizes that
security spending must be proportional to the risks and assets being
protected. Demanding the most expensive option without cost-benefit
analysis makes you look unreasonable and gets you cut out of decisions.

Risk management is about BALANCE, not absolutism.
                    """,
                    2: """
You just recommended a vendor you can't verify exists, with no documentation,
operating from an unknown location. This isn't "risk tolerance" - it's
willful negligence.

When risks are unknown but historical outcomes are catastrophic (or in this
case, unknowable), the answer is NOT to proceed. The cost savings mean
nothing if the company doesn't actually exist.

Due diligence before risk acceptance. Always.
                    """,
                    3: """
"Let's wait until all risks are eliminated" is another way of saying
"Let's never make a decision." Perfect security doesn't exist. Every
vendor has some risk. Every decision involves tradeoffs.

Your job isn't to eliminate all risk - it's to help the business make
INFORMED decisions about which risks are acceptable. Analysis paralysis
isn't security - it's just another way to fail.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 60,
        "hp_penalty": 20,
        "failure_text": """
Risk management is the foundation of security decision-making. It requires:
1. Identifying assets and their value
2. Identifying threats and vulnerabilities
3. Calculating likelihood and impact
4. Comparing against organizational risk appetite
5. Implementing appropriate controls

Neither absolute security nor blind risk-taking serves the organization.
        """,
        "domain_reference": "Domain 1: Security and Risk Management - Risk Assessment, Risk Appetite, Quantitative Risk Analysis"
    },

    # Scenario 3: Separation of Duties
    {
        "id": "d1_treasurers_request",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "THE TREASURER'S REQUEST",
                "narrative": """
The Royal Treasurer requests an audience. She is known throughout the realm
for her integrity and decades of loyal service. The kingdom's coffers have
never been more secure under her watchful eye.

"I come with a modest proposal," she says. "To increase efficiency, I suggest
that I be granted the authority to both AUTHORIZE payments and EXECUTE the
transfers. Currently, Lord Blackwood must approve each transaction I make,
causing delays of days for urgent matters."

She presents a scroll showing dozens of delayed payments - soldiers awaiting
wages, merchants awaiting settlements, diplomatic gifts held in limbo.

"Lord Blackwood is often traveling. Surely after twenty years of flawless
service, this additional authority is warranted?"

How do you respond?
                """,
                "choices": [
                    {"text": "Grant the request - her record speaks for itself, and efficiency matters"},
                    {"text": "Deny the request - separation of duties must be maintained regardless of individual trustworthiness"},
                    {"text": "Grant temporary authority only during Lord Blackwood's absences"},
                    {"text": "Suggest she train an apprentice who can act in Lord Blackwood's absence"}
                ],
                "success_text": """
The Treasurer's expression remains neutral, but you detect a slight nod of
respect. "You are wise to refuse, young guardian. I confess - this was a test."

She produces another scroll, this one bearing the King's seal. "His Majesty
asked me to evaluate the security awareness of new Citadel members. Many
before you have failed, swayed by my reputation or moved by the efficiency
argument."

She continues: "Separation of duties is not about distrust. It is about
protecting everyone - including ME - from suspicion, coercion, and error.
If I alone controlled the treasury, any discrepancy would point only to me.
With Lord Blackwood's oversight, we protect each other."

"The solution to delays," she adds, "is not to remove controls, but to
ensure backup approvers exist. I shall recommend Deputy Silverstone be
granted approval authority for when Lord Blackwood travels."

You have demonstrated understanding of SEPARATION OF DUTIES.
                """,
                "failure_texts": {
                    0: """
No matter how trustworthy an individual appears, concentrating authorization
and execution in one person creates unacceptable risk. Separation of duties
exists not because we distrust individuals, but because we recognize that:
1. People can be compromised, coerced, or corrupted
2. Errors go undetected without oversight
3. Insider threats often come from trusted positions
The Treasurer's perfect record actually makes her a higher-value target for
those who would corrupt or coerce her.
                    """,
                    2: """
This 'compromise' actually creates a predictable window of vulnerability.
Malicious actors would simply wait for Lord Blackwood's travels to act.
Temporary exceptions to security controls often become permanent, and
they signal that the controls are negotiable. Separation of duties must
be consistent to be effective.
                    """,
                    3: """
While training successors is valuable, this doesn't address the immediate
concern and subtly suggests the control itself is the problem. The correct
solution is to ensure proper backup APPROVERS exist, not to eliminate the
approval requirement. The Treasurer can have deputies; the approval process
should have designated alternates for Lord Blackwood.
                    """
                }
            },
            "corporate": {
                "title": "THE CFO'S REQUEST",
                "narrative": """
Janet Chen, CFO for 15 years and universally respected, stops by your desk.
Her reputation is impeccable - she's guided the company through three
recessions without a single audit finding.

"I need a favor," she says, closing your office door. "This dual-approval
process for wire transfers is killing us. I need to approve, then wait for
Tom in Treasury to approve, but Tom's always in meetings or on vacation."

She slides over documentation showing delayed payments - overdue vendor
invoices, payroll issues, an almost-missed acquisition deadline.

"I'm proposing we give me both roles - initiator AND approver - just for
transfers under $50,000. After 15 years, I think I've earned that trust.
The board's been complaining about efficiency."

How do you respond?
                """,
                "choices": [
                    {"text": "Approve it - her track record is spotless, and efficiency is important"},
                    {"text": "Deny the request - separation of duties must be maintained regardless of tenure"},
                    {"text": "Approve for 30 days while we find a better solution"},
                    {"text": "Suggest she delegate her initiator role to her assistant instead"}
                ],
                "success_text": """
Janet smiles. "Finally, someone who gets it."

You blink. "I... denied your request."

"Exactly. The last three security people said yes. The CISO wanted to see
who would stand firm on controls. You passed."

She pulls out a memo. "Look - I don't WANT that kind of access. If I could
approve my own transfers, and there was ever a discrepancy? I'd be suspect
number one. The control protects ME as much as the company."

"The real fix," she continues, "is backup approvers. Tom's out? Sarah can
approve. Sarah's out? Mike can approve. We maintain the control AND fix
the bottleneck."

"Separation of duties isn't about trust - it's about protection. From
external threats, from internal mistakes, and from suspicion. Smart
controls protect everyone, including the people being controlled."

You have demonstrated understanding of SEPARATION OF DUTIES.
                """,
                "failure_texts": {
                    0: """
Fifteen years of good behavior doesn't mean Year 16 will be the same. Fraud
statistics show that the typical embezzler has been with the company for
years and is often "the last person you'd suspect."

Separation of duties exists because:
1. Good people can be compromised (blackmail, gambling debts, sick family)
2. Mistakes happen even with good intentions
3. The control protects the individual from suspicion

Janet's perfect record makes her MORE valuable as a target, not less.
                    """,
                    2: """
"Temporary" exceptions have a way of becoming permanent. And they create
a predictable vulnerability window - anyone wanting to compromise Janet
just has to wait for "temporary access" periods.

More importantly, you've signaled that controls are negotiable if someone
complains enough. Next quarter, it'll be a 60-day exception. Then 90.
Then permanent.

Either the control matters or it doesn't. If it matters, maintain it.
                    """,
                    3: """
This misses the point entirely. The issue isn't WHO initiates - it's that
one person shouldn't do BOTH. Delegating initiation to Janet's assistant
just moves the problem, and now you have a more junior person initiating
large financial transactions.

The solution is backup approvers, not elimination of the approval step.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 65,
        "hp_penalty": 20,
        "failure_text": """
Separation of Duties is a critical control that prevents fraud and error by
ensuring no single person can complete a sensitive transaction alone. Key
principles include:
- Authorization, custody, and record-keeping should be separated
- Trust but verify - even trusted employees need oversight
- The control protects both the organization AND the individual
- Efficiency concerns should be addressed by adding backup personnel, not
  removing controls
        """,
        "domain_reference": "Domain 1: Security and Risk Management - Separation of Duties, Security Governance, Personnel Security"
    },

    # Scenario 4: Business Continuity
    {
        "id": "d1_siege_approaches",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "THE SIEGE APPROACHES",
                "narrative": """
Scouts report that the Obsidian Horde approaches from the east. You have
perhaps a fortnight before they reach the outer walls. The Citadel has
never fallen, but neither has it faced such numbers.

The Council convenes in emergency session. The High Chamberlain speaks:
"We must prepare for the possibility that the outer Citadel falls. Our
critical functions - the Treasury, the Cipher Chamber, the Royal Archives -
must continue even if we retreat to the Inner Keep."

She turns to you. "We need TWO plans: one to keep operations running during
the siege, and another to recover if the worst happens. The scribes are
confused about what we need. Explain the difference."

What do you tell them?
                """,
                "choices": [
                    {"text": "Focus only on defense - if we prevent the disaster, we won't need recovery plans"},
                    {"text": "Create one comprehensive plan that covers everything - separating them creates confusion"},
                    {"text": "BCP maintains operations during disruption; DRP restores systems after disaster - both are needed"},
                    {"text": "Prioritize DRP over BCP - recovery after the siege matters more than operations during it"}
                ],
                "success_text": """
The Council members nod as understanding dawns. You continue:

"The Business Continuity Plan addresses how we maintain critical operations
DURING the siege. Which functions are essential? The Treasury must still pay
soldiers. The Cipher Chamber must still decode enemy communications. We
identify these critical functions and ensure they can operate even from the
Inner Keep."

"The Disaster Recovery Plan addresses what happens IF the outer Citadel
falls. How do we restore the Treasury records from backup scrolls? How
quickly must the Cipher Chamber be operational again? We define Recovery
Time Objectives and Recovery Point Objectives for each system."

The High Chamberlain smiles grimly. "Then we need both plans, working in
concert. BCP keeps us fighting during the storm. DRP rebuilds after it passes."

You have demonstrated understanding of BCP and DRP principles.
                """,
                "failure_texts": {
                    0: """
Preventing disasters is important, but assuming prevention will always
succeed is dangerous overconfidence. Business Continuity Planning (BCP)
and Disaster Recovery Planning (DRP) exist precisely because we cannot
prevent all incidents. An organization without recovery plans faces
existential risk when (not if) a major incident occurs.
                    """,
                    1: """
While integration is valuable, BCP and DRP serve distinct purposes and
involve different teams, timeframes, and resources. BCP focuses on
maintaining operations DURING a disruption, while DRP focuses on
restoring systems AFTER a disaster. Conflating them leads to gaps
in coverage and unclear responsibilities during a crisis.
                    """,
                    3: """
Both plans are essential and neither should be prioritized over the other.
During a prolonged siege, BCP keeps critical functions running - soldiers
need to be paid, communications need to flow, records need to be maintained.
After the siege, DRP helps restore normal operations. Neglecting either
creates dangerous gaps in organizational resilience.
                    """
                }
            },
            "corporate": {
                "title": "THE RANSOMWARE TABLETOP",
                "narrative": """
The CISO gathers the leadership team for a tabletop exercise. "Scenario:
It's 2 AM Monday. Ransomware has encrypted 60% of our systems. The attackers
want $2 million in Bitcoin. What do we do?"

The executives look at each other nervously.

The CEO speaks first: "Let's focus on preventing this. Better firewalls,
more training. If we stop the attack, we don't need plans for after."

The CTO counters: "Let's just make one big plan. Having separate documents
for 'during' versus 'after' is confusing."

The CFO asks: "Which is more important - keeping things running during the
attack or recovering afterward?"

The CISO turns to you. "Help them understand what we actually need."

What's your recommendation?
                """,
                "choices": [
                    {"text": "Focus on prevention - if we stop the ransomware, we don't need recovery plans"},
                    {"text": "Create one comprehensive plan - separate BCP and DRP documents are redundant"},
                    {"text": "We need both: BCP to maintain operations during the incident, DRP to restore systems after"},
                    {"text": "Prioritize DRP - recovering from the attack is more important than operating during it"}
                ],
                "success_text": """
You grab the whiteboard marker. "Let me explain why we need both."

"BCP - Business Continuity - answers: 'How do we keep operating while 60%
of systems are down?' Can customer service take orders manually? Can we
process payroll by hand? What's our workaround for email?"

"DRP - Disaster Recovery - answers: 'How do we restore those encrypted
systems?' What's our backup strategy? How long until systems are back?
What's our order of restoration?"

The CEO nods. "So BCP keeps us alive during the crisis, DRP brings us
back to normal?"

"Exactly. And they have different metrics: BCP cares about Maximum Tolerable
Downtime - how long can a function be degraded? DRP cares about Recovery
Time Objective - how fast can we restore a system?"

The CFO adds: "And the $2 million question?"

"That's a separate decision tree. But we can't make it intelligently
without knowing our BCP capabilities and DRP timelines."

You have demonstrated understanding of BCP and DRP principles.
                """,
                "failure_texts": {
                    0: """
"Just prevent the attack" is not a plan - it's wishful thinking. Every
security framework acknowledges that prevention will eventually fail.
When (not if) it does, you need:
- Business Continuity to keep critical functions running
- Disaster Recovery to restore systems

The organizations that get destroyed by ransomware aren't the ones who got
attacked - they're the ones who thought it couldn't happen to them.
                    """,
                    1: """
BCP and DRP are related but different:

BCP: "How do we keep operating?" (during the incident)
- Identifies critical business functions
- Defines workarounds and manual procedures
- Focuses on the business, not just IT

DRP: "How do we restore systems?" (after the incident)
- Defines backup/restore procedures
- Sets RTO (how fast) and RPO (how much data loss)
- Focuses on technical recovery

Mixing them creates confusion during a crisis - exactly when you need clarity.
                    """,
                    3: """
This is like asking "Which is more important - the parachute or the reserve
parachute?" You need both.

During the ransomware attack, BCP keeps the business functioning - maybe
degraded, maybe manually, but functioning. Without BCP, every hour of
downtime is lost revenue, lost customers, lost trust.

After the attack, DRP restores systems. Without DRP, you're stuck in
manual mode forever.

You can't prioritize one over the other. You need both.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 70,
        "hp_penalty": 20,
        "failure_text": """
Business Continuity Planning (BCP) and Disaster Recovery Planning (DRP) are
complementary but distinct:

BCP: Focuses on maintaining critical business functions DURING a disruption
- Identifies critical business processes
- Establishes alternate procedures and workarounds
- Ensures essential operations continue

DRP: Focuses on restoring IT systems and data AFTER a disaster
- Defines Recovery Time Objectives (RTO) - how quickly systems must recover
- Defines Recovery Point Objectives (RPO) - how much data loss is acceptable
- Establishes technical recovery procedures

Both are essential components of organizational resilience.
        """,
        "domain_reference": "Domain 1: Security and Risk Management - Business Continuity Planning, Disaster Recovery Planning, RTO/RPO"
    },

    # Scenario 5: Ethics and Conflicts of Interest
    {
        "id": "d1_nobles_bribe",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "THE NOBLE'S BRIBE",
                "narrative": """
Lord Ashford corners you in a quiet corridor. His family is one of the
wealthiest in the realm, and his son recently failed the Citadel's entrance
examinations - caught attempting to copy another applicant's cipher work.

"A mere youthful indiscretion," Lord Ashford says smoothly, pressing a heavy
purse into your hands. "Surely such a small matter need not appear in the
official records. The boy has learned his lesson. And the Ashford family
has always been... generous... to those who show us kindness."

The purse contains enough gold to buy a small estate. Lord Ashford's
influence could advance your career significantly. The incident WAS minor -
the boy was caught before any real harm was done.

What do you do?
                """,
                "choices": [
                    {"text": "Accept the gold and remove the record - the incident was minor and no harm was done"},
                    {"text": "Refuse the bribe but agree to 'lose' the paperwork as a favor to a powerful family"},
                    {"text": "Refuse firmly and report the bribery attempt through proper channels"},
                    {"text": "Refuse the bribe but keep the incident private to avoid making a powerful enemy"}
                ],
                "success_text": """
You hand the purse back to Lord Ashford. "I cannot accept this, my lord.
And I must inform you that I am obligated to report this conversation to
the Ethics Council."

Lord Ashford's face flushes with anger, then settles into cold calculation.
"You've made a powerful enemy today, guardian."

"Perhaps," you reply. "But I remain a guardian. The moment I accepted your
gold, I would have become something else entirely."

Your report to the Ethics Council results in Lord Ashford being barred from
the Citadel grounds. His son, given a second chance to apply honestly next
year, eventually passes on his own merits and becomes a capable guardian -
one who later thanks you for not allowing his father to corrupt his path.

You have demonstrated the (ISC)² Code of Ethics: Protect society, act
honorably, provide diligent service, and advance the profession.
                """,
                "failure_texts": {
                    0: """
Accepting bribes to alter official records violates fundamental ethical
principles and the (ISC)² Code of Ethics. It doesn't matter that the
incident was 'minor' - the act of accepting payment to falsify records
is itself a serious breach. Moreover, if discovered, this would destroy
your credibility and career, and potentially implicate you in future
misconduct by Lord Ashford's son.
                    """,
                    1: """
This is still falsifying records, just without direct payment. The ethical
violation is the same whether or not gold changes hands. Additionally,
you've now created a debt to Lord Ashford that he may call upon later,
potentially for even more compromising requests. Integrity cannot be
selectively applied based on who benefits.
                    """,
                    3: """
While refusing the bribe is correct, failing to report the attempt enables
future corruption. Lord Ashford will likely try again with someone else,
and your silence makes you complicit in any future success he has. The
(ISC)² Code of Ethics requires not just personal integrity, but actively
protecting the profession and those it serves.
                    """
                }
            },
            "corporate": {
                "title": "THE BOARD MEMBER'S REQUEST",
                "narrative": """
Marcus Webb, board member and major shareholder, catches you after the
quarterly security briefing. His nephew was just fired for sharing his
login credentials with a contractor - a clear policy violation that led
to a minor data exposure.

"Between us," Marcus says quietly, handing you a thick envelope, "my nephew
made a mistake. Young people, you know how it is. I'm sure the investigation
report doesn't need to mention him by name. Just say 'a former employee.'"

The envelope contains $25,000 in cash. Marcus controls 15% of company stock.
His nephew DID make a relatively minor mistake - no customer data was exposed,
just some internal documents.

"The family appreciates discretion," Marcus adds. "And we have a long memory
for people who help us."

What do you do?
                """,
                "choices": [
                    {"text": "Take the money and anonymize the report - no one was really hurt"},
                    {"text": "Refuse the money but agree to modify the report as a professional courtesy"},
                    {"text": "Refuse firmly and report the bribery attempt to the Ethics Committee"},
                    {"text": "Refuse the bribe but agree to keep this conversation confidential"}
                ],
                "success_text": """
You push the envelope back across the table. "Mr. Webb, I'm not able to
accept this, and I'm obligated to report this conversation."

His face hardens. "You know who I am?"

"I do. And that's exactly why I have to report it. If a board member can
buy modifications to security reports, our entire program is worthless.
Every report becomes suspect."

You document the conversation and report to the Chief Ethics Officer. The
investigation is uncomfortable - Marcus tries to have you fired - but the
board ultimately removes him for attempted bribery.

Three months later, you're presenting the security report to the new board.
The chair stops you mid-slide: "Before you continue - I want everyone here
to know that this report is accurate because this person had the integrity
to refuse a bribe. That's the kind of security program we need."

You have demonstrated the (ISC)² Code of Ethics.
                """,
                "failure_texts": {
                    0: """
You just accepted a bribe from a board member. Congratulations, you're now:
1. Complicit in falsifying official records
2. Beholden to someone who knows you're corrupt
3. One discovery away from criminal charges and career destruction

The "minor incident" argument is irrelevant. The bribe is the incident now.
And Marcus will be back - with bigger requests, knowing you'll comply.

The (ISC)² Code of Ethics exists for exactly this reason.
                    """,
                    1: """
"No money changed hands" doesn't make this okay. You're still falsifying
a security report to protect someone from consequences of their actions.

Worse, you've now established yourself as someone who can be influenced.
Marcus didn't even have to pay! Next time, he'll ask for more. And you've
given him leverage - he knows you're willing to bend reports.

Integrity isn't about whether you profit from the compromise.
                    """,
                    3: """
Refusing the bribe is correct. Keeping it confidential is not.

By staying silent, you've:
1. Let Marcus think this approach might work on others
2. Failed to protect colleagues from similar approaches
3. Allowed someone who tried to corrupt security reports to remain on the board

The (ISC)² Code of Ethics requires protecting the profession. That means
reporting attempts to corrupt it, not just refusing them personally.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 70,
        "hp_penalty": 25,
        "failure_text": """
The (ISC)² Code of Ethics requires security professionals to:
1. Protect society, the common good, and the infrastructure
2. Act honorably, honestly, justly, responsibly, and legally
3. Provide diligent and competent service to principals
4. Advance and protect the profession

Accepting bribes, falsifying records, or remaining silent about corruption
attempts violates these fundamental principles. Ethics are not situational -
they must be applied consistently regardless of personal cost or benefit.
        """,
        "domain_reference": "Domain 1: Security and Risk Management - (ISC)² Code of Ethics, Professional Ethics, Conflicts of Interest"
    },

    # Scenario 6: Due Diligence vs Due Care
    {
        "id": "d1_new_supplier",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "THE NEW SUPPLIER",
                "narrative": """
The Quartermaster brings urgent news. Your current supplier of enchanted
parchment - used for all secure communications - has been destroyed by
dragon fire. A new supplier must be found immediately, or the Citadel's
secure messaging will cease within a fortnight.

Three suppliers have offered their services:

The first, Grimwald's Scrollworks, offers the lowest price and fastest
delivery. They are new to the market with no reputation to speak of.

The second, Thornberry & Sons, has supplied other citadels for decades.
Their prices are moderate, but they require a lengthy inspection of their
facilities before any contract.

The third, the Silverleaf Consortium, is the most expensive but offers
immediate delivery from existing stock.

The Quartermaster asks: "What considerations should guide our choice? The
Council speaks of 'due diligence' and 'due care' but I confuse the terms."

How do you explain the difference and advise the Quartermaster?
                """,
                "choices": [
                    {"text": "Choose Grimwald's - speed and cost matter most in a crisis, we can assess them later"},
                    {"text": "Due diligence is investigation BEFORE engagement; due care is ongoing responsible action AFTER - both matter"},
                    {"text": "Choose Silverleaf for immediate needs - their high price proves their quality"},
                    {"text": "Due diligence and due care are the same thing - just do your job carefully"}
                ],
                "success_text": """
The Quartermaster's confusion clears as you explain:

"Due diligence is what we do BEFORE choosing a supplier. We investigate their
security practices, verify their reputation, inspect their facilities, and
assess their risks. This is why Thornberry's inspection requirement is
actually a GOOD sign - they understand security-conscious customers."

"Due care is what we do AFTER we've made our choice. We monitor the supplier's
ongoing performance, verify each shipment, maintain proper handling of the
parchment, and respond appropriately to any concerns that arise."

You advise: "For the immediate crisis, purchase a small quantity from
Silverleaf to maintain operations. Meanwhile, conduct proper due diligence
on Thornberry & Sons for a long-term contract. Do not engage Grimwald's
until they've established a verifiable track record."

The Quartermaster nods. "So we need BOTH - investigation before, and
vigilance after. Neither alone is sufficient."

You have demonstrated understanding of Due Diligence and Due Care.
                """,
                "failure_texts": {
                    0: """
Choosing an unknown supplier without any vetting, especially for security-
critical materials, is a failure of due diligence. The enchanted parchment
is used for secure communications - if compromised, it could expose all of
the Citadel's secrets. Due diligence BEFORE engagement is essential,
regardless of urgency. The crisis doesn't eliminate the need for vetting.
                    """,
                    2: """
Price is not a reliable indicator of quality or security. While Silverleaf's
existing stock may solve the immediate crisis, committing to them long-term
without proper due diligence is still risky. High prices can mask poor
practices, and reputation alone doesn't guarantee current security. Due
diligence requires actual investigation, not assumptions based on cost.
                    """,
                    3: """
Due diligence and due care are related but distinct legal and professional
concepts. Due diligence refers to the investigation and assessment done
BEFORE making a decision or entering a relationship. Due care refers to
the ongoing responsibility to act reasonably and responsibly AFTER the
decision is made. Both are required, but at different stages.
                    """
                }
            },
            "corporate": {
                "title": "THE EMERGENCY VENDOR",
                "narrative": """
Your primary cloud security vendor just imploded - CEO arrested, data center
seized by the FBI, the works. You have 30 days before your current contract
terminates and you're left without a SIEM solution.

Three alternatives have emerged:

"FastCloud Security" - They can be operational in a week, they're cheap, and
they're VERY eager for your business. No SOC 2 report yet ("It's in progress"),
but the sales rep promises they're secure.

"SecureVendor Corp" - Industry leader, SOC 2 Type II certified, but they
require a 60-day security assessment period before any enterprise contract.
They won't budge.

"PremiumSec" - Most expensive option, immediate availability, excellent
reputation, but no one's actually reviewed their security practices in detail.

Your CISO asks: "Walk me through the due diligence versus due care framework
here. What should we actually do?"

How do you advise?
                """,
                "choices": [
                    {"text": "Go with FastCloud - we can assess them after we're operational, the urgency trumps process"},
                    {"text": "Due diligence is pre-contract investigation; due care is post-contract vigilance - we need a plan for both"},
                    {"text": "PremiumSec's high price and reputation mean they're probably fine - go with them"},
                    {"text": "Due diligence and due care are basically the same - just be careful throughout"}
                ],
                "success_text": """
You outline the framework:

"Due diligence is what we do BEFORE signing - assess their security controls,
review certifications, check references, understand their practices. It's the
'look before you leap' phase."

"Due care is what we do AFTER signing - ongoing monitoring, reviewing their
security updates, validating they're meeting commitments, responding to issues.
It's the 'trust but verify' phase."

"For our situation: FastCloud without due diligence is reckless - we'd be
trusting our security data to an unvetted vendor. PremiumSec's reputation
isn't due diligence - we need actual assessment."

"My recommendation: Short-term contract with PremiumSec to bridge the gap,
with immediate due diligence initiated. Parallel track SecureVendor's 60-day
assessment for long-term partnership. Document everything for auditors."

The CISO nods. "So we're not choosing between speed and security - we're
managing both with proper process at each stage."

You have demonstrated understanding of Due Diligence and Due Care.
                """,
                "failure_texts": {
                    0: """
"Assess them after we're operational" is how breaches happen. You'd be
sending your security logs - containing details of your entire infrastructure
- to an unvetted vendor. If FastCloud is compromised (or malicious), you've
just handed attackers a roadmap.

Due diligence must happen BEFORE you share sensitive data. The urgency
doesn't eliminate risk - it increases it. Rushing creates vulnerabilities.
                    """,
                    2: """
"Probably fine" isn't a security strategy. High prices can mask poor
practices. Good reputation can be based on marketing, not substance.
You're about to send your security telemetry to this company - that
requires actual investigation, not assumptions.

Reputation is a starting point for due diligence, not a replacement for it.
                    """,
                    3: """
Due diligence and due care are different things:

Due Diligence: "Did we properly investigate BEFORE engaging?"
- Happens pre-contract
- Assesses potential partners
- Identifies risks before commitment

Due Care: "Are we acting responsibly AFTER engaging?"
- Happens post-contract
- Monitors ongoing relationship
- Responds to issues as they arise

Conflating them creates gaps where neither is done properly.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 65,
        "hp_penalty": 20,
        "failure_text": """
Due Diligence and Due Care are complementary but distinct concepts:

DUE DILIGENCE: The investigation and assessment performed BEFORE making
a decision or entering a relationship
- Researching a vendor's security practices before contracting
- Assessing risks before implementing a new system
- Investigating an acquisition target before purchase

DUE CARE: The ongoing responsibility to act reasonably and responsibly
AFTER a decision has been made
- Maintaining proper security controls
- Responding appropriately to incidents
- Continuing to monitor and assess risks

Both are required to meet professional and legal standards of care.
        """,
        "domain_reference": "Domain 1: Security and Risk Management - Due Diligence, Due Care, Vendor Management, Third-Party Risk"
    },
]

# Add remaining scenarios (keeping them in legacy format for now, they'll be converted when corporate themes are written)
# These will fall back to fantasy theme automatically

DOMAIN_1_SCENARIOS.extend([
    # Scenario 7: Legal/Regulatory Conflicts
    {
        "id": "d1_competing_laws",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "THE COMPETING LAWS",
                "narrative": """
A messenger arrives bearing troubling news. The Citadel has been ordered to
comply with two conflicting decrees:

The Northern Kingdom demands that all citizen records be retained for seven
years for tax purposes. However, the Southern Alliance has enacted a new
privacy law requiring that personal data be deleted within one year unless
the citizen explicitly consents to longer retention.

Many citizens hold dual allegiance to both realms. The Citadel cannot comply
with both laws simultaneously for these individuals.

The Legal Advisor asks: "How do we navigate these conflicting requirements?"

What counsel do you provide?
                """,
                "choices": [
                    {"text": "Follow the stricter law - delete after one year to ensure maximum privacy protection"},
                    {"text": "Follow the local law where the Citadel is physically located"},
                    {"text": "Seek legal counsel, implement separate policies per jurisdiction, and document compliance decisions"},
                    {"text": "Refuse to accept data from dual-allegiance citizens until the laws are harmonized"}
                ],
                "success_text": """
The Legal Advisor nods approvingly. "You understand that legal conflicts
cannot be resolved by simple rules. We must:"

"First, engage legal counsel expert in both jurisdictions to analyze our
specific obligations. Second, implement separate data handling policies
based on which laws apply to each individual - Northern citizens follow
Northern retention, Southern citizens follow Southern privacy rules."

"For dual-allegiance citizens, we must determine primary jurisdiction
based on established legal principles, document our reasoning, and be
prepared to defend our decisions if challenged."

"Most importantly, we maintain detailed records of our compliance decisions
and the legal analysis supporting them. Regulators respect good-faith
efforts to comply with conflicting requirements."

You have demonstrated understanding of JURISDICTIONAL COMPLIANCE.
                """,
                "failure_texts": {
                    0: """
Simply following the stricter law ignores legitimate legal obligations to the
Northern Kingdom. This could result in legal penalties, inability to support
tax audits, and breach of the Citadel's duties to Northern authorities.
Legal conflicts require careful analysis, not automatic deference to the
strictest interpretation.
                    """,
                    1: """
Physical location alone doesn't determine which laws apply to data. Modern
privacy regulations often have extraterritorial reach - they apply based on
the data subjects' location, not where the data is processed. The Citadel
must consider which citizens are subject to which laws, not just its own
location.
                    """,
                    3: """
Refusing service to citizens caught between conflicting laws is neither
practical nor ethical. The Citadel has obligations to serve all citizens.
The solution is to manage the complexity through proper legal analysis and
jurisdictional policies, not to abandon those most affected by the conflict.
                    """
                }
            },
            "corporate": {
                "title": "THE GDPR VERSUS SOX SHOWDOWN",
                "narrative": """
The Legal department just dropped a bombshell in the compliance Slack channel.

Your company operates in both the EU and US. European customers are protected
by GDPR, which grants them the right to have their data deleted upon request.
But US financial regulations (SOX) require you to retain transaction records
for seven years for audit purposes.

A European customer who made significant purchases has submitted a formal
GDPR deletion request. But they're also flagged in a potential fraud
investigation, and those records are subject to a legal hold.

The EU compliance officer is threatening "massive fines." The US compliance
officer is warning about "obstruction of justice." Legal says "figure it out."

The CFO has scheduled an emergency meeting in 30 minutes.

What do you recommend?
                """,
                "choices": [
                    {"text": "Delete everything per GDPR - it's the stricter law and those fines are huge"},
                    {"text": "Keep everything per SOX - we're a US company, US law takes precedence"},
                    {"text": "Work with legal counsel to segment data: honor GDPR for general data, maintain legal holds where required"},
                    {"text": "Tell the customer we can't process their request until regulations are harmonized"}
                ],
                "success_text": """
You walk into the CFO's office with a plan.

"We don't have to choose between GDPR and SOX - we need to apply each
appropriately. Here's how:"

"First, we segment the customer's data by category. Marketing preferences,
browsing history, general account info? That gets deleted per GDPR."

"Transaction records required for SOX compliance and the legal hold?
Those stay, but we document WHY they stay - both regulations explicitly
allow retention for legal compliance and active investigations."

"We respond to the customer explaining which data was deleted and which
is retained under legal exceptions. We're transparent about the reasoning."

"Finally, we document everything for both regulators. When you show
good-faith effort to comply with conflicting requirements, regulators
typically respect that approach."

The CFO nods. "So we're not ignoring either law - we're applying each
where it's supposed to apply." Exactly.

You've demonstrated JURISDICTIONAL COMPLIANCE management.
                """,
                "failure_texts": {
                    0: """
You deleted everything, including records under legal hold for a fraud
investigation. Congratulations, you've just potentially committed
obstruction of justice, and the auditors are going to have questions
about those missing SOX records.

GDPR includes explicit exceptions for legal obligations. "Delete
everything" isn't compliance - it's panic.
                    """,
                    1: """
"We're a US company" doesn't exempt you from GDPR when you process EU
citizens' data. Those regulations have extraterritorial reach. The EU
regulator doesn't care where your headquarters is - they care where
your data subjects live.

Ignoring GDPR because of your location is a fast track to a 4% of
global revenue fine.
                    """,
                    3: """
"Come back when the laws agree" is not a compliance strategy. The
customer has legitimate rights NOW, and you have obligations NOW.

Parts of their request CAN be honored immediately. Refusing to act
on what you CAN do while explaining what you CAN'T do is proper
compliance. Refusing everything is just obstruction.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 65,
        "hp_penalty": 20,
        "failure_text": """
When laws conflict, organizations must:
1. Obtain qualified legal counsel for each jurisdiction
2. Analyze which laws apply to which data subjects
3. Implement jurisdiction-specific policies where possible
4. Document compliance decisions and supporting rationale
5. Maintain good-faith efforts to honor all legitimate obligations
6. Be prepared to defend decisions to regulators

Simple rules rarely resolve complex jurisdictional conflicts.
        """,
        "domain_reference": "Domain 1: Security and Risk Management - Legal & Regulatory Compliance, Jurisdictional Issues"
    },

    # Scenario 8: Import/Export Controls
    {
        "id": "d1_imported_goods",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "THE IMPORTED GOODS",
                "narrative": """
The Master of Trade approaches with a delicate matter. A merchant from the
Eastern Isles wishes to purchase the Citadel's renowned encryption crystals -
magical artifacts that can secure any communication against eavesdropping.

"The crystals would fetch a fortune," the Master explains. "The Eastern
merchant has gold aplenty and legitimate business needs. However, I've heard
whispers that the Eastern Isles are under... certain restrictions."

You investigate and discover that the Kingdom has placed export controls on
encryption technology to the Eastern Isles due to ongoing conflicts. The
crystals are classified as "dual-use" items - useful for both commerce and
military applications.

The merchant insists his intentions are purely commercial. The gold offered
would fund Citadel operations for months.

How do you advise the Master of Trade?
                """,
                "choices": [
                    {"text": "Approve the sale - the merchant's stated intentions are commercial, and we need the funds"},
                    {"text": "Deny the sale outright - export controls to the Eastern Isles prohibit this transaction"},
                    {"text": "Sell lower-grade crystals that aren't as powerful - they might not be controlled"},
                    {"text": "Have the merchant purchase through an intermediary in an unrestricted kingdom"}
                ],
                "success_text": """
The Master of Trade sighs but accepts your counsel. "The gold would have
been welcome, but I understand. We cannot risk the Citadel's standing."

You explain: "Export controls exist for national security reasons. The
encryption crystals are 'dual-use' - capable of both commercial and military
applications. When items are controlled, we must deny sales to restricted
destinations regardless of the buyer's stated intentions."

"Furthermore, attempting to circumvent controls through intermediaries,
modified products, or willful ignorance would compound our violation. The
penalties for export control breaches include loss of export privileges,
heavy fines, and even imprisonment for individuals involved."

"We must also report this inquiry, as authorities track attempts to
acquire controlled technology."

You have demonstrated understanding of EXPORT CONTROL compliance.
                """,
                "failure_texts": {
                    0: """
Export controls apply regardless of the buyer's stated intentions. The
classification of items as controlled is based on their CAPABILITY, not
their intended use. Trusting a buyer's assurances is not a defense against
export control violations. The Citadel could face severe penalties, loss
of export privileges, and damage to its reputation.
                    """,
                    2: """
'Might not be controlled' is not a compliance strategy. Each item must be
properly classified against control lists before export. Attempting to
circumvent controls by modifying products is itself a violation if the
intent is to evade restrictions. All encryption technology must be
properly evaluated against export control thresholds.
                    """,
                    3: """
This describes 'transshipment' - routing controlled goods through third
countries to evade restrictions. This is a serious export control violation.
The Citadel would be liable for knowingly participating in a scheme to
circumvent controls, potentially facing criminal penalties in addition to
civil ones.
                    """
                }
            },
            "corporate": {
                "title": "THE OVERSEAS DEAL",
                "narrative": """
Sales is practically vibrating with excitement. A huge order just came in
from a technology company based in a country that's been in the news lately
for... let's say "geopolitical tensions."

"They want our enterprise encryption suite," the Sales VP announces. "It's
a $2 million deal. They say it's for securing their banking infrastructure.
Totally legitimate commercial use."

You pull up BIS (Bureau of Industry and Security) guidelines on your laptop.
Your encryption software is classified as a dual-use item under EAR (Export
Administration Regulations). The destination country is on the restricted
entity list.

"But they said it's for banking!" the Sales VP protests. "And we REALLY
need to hit our quarterly numbers."

What do you recommend?
                """,
                "choices": [
                    {"text": "Approve the deal - they have a legitimate commercial purpose, and we need the revenue"},
                    {"text": "Deny the sale - export controls prohibit this regardless of stated intent"},
                    {"text": "Offer them our 'lite' version with weaker encryption - maybe that's not controlled"},
                    {"text": "Have them order through their subsidiary in a non-restricted country"}
                ],
                "success_text": """
You share your screen showing the EAR regulations.

"I know this hurts, but we cannot make this sale. Here's why:"

"First, the destination is on the restricted entity list. Our encryption
software is explicitly controlled under EAR. The buyer's stated intentions
don't matter - classification is based on CAPABILITY, not intended use."

"Second, and this is the part that should really concern everyone: export
control violations carry penalties up to $1 million per violation, denial
of export privileges, and criminal liability for individuals involved.
That $2M deal could cost us far more."

"Third, we need to report this inquiry to BIS. They track attempts to
acquire controlled technology from restricted entities."

The Sales VP is unhappy, but the General Counsel backs you up. "Better
to lose the sale than lose our export license."

You've demonstrated EXPORT CONTROL compliance.
                """,
                "failure_texts": {
                    0: """
"They said it's for banking" isn't a defense against export control
violations. Items are controlled based on CAPABILITY, not stated
intent. A buyer can say anything - that doesn't change the legal
restrictions.

Now you're facing potential criminal charges and your company may
lose its export privileges entirely. Was the commission worth it?
                    """,
                    2: """
"Maybe that's not controlled" is not a compliance strategy. Every
item must be properly classified BEFORE export. Deliberately weakening
a product to evade controls - while clearly intending to help a
restricted buyer - is itself a violation.

Export compliance requires certainty, not hopeful guessing.
                    """,
                    3: """
You just recommended transshipment - routing controlled goods through
a third country to evade restrictions. That's a serious federal crime.

The fact that it's their subsidiary doesn't matter. You knew the end
destination was restricted and you helped structure a workaround.
That's conspiracy to violate export controls.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 60,
        "hp_penalty": 20,
        "failure_text": """
Export controls regulate the transfer of controlled items across borders:
- Items are classified by capability, not intended use
- Buyer assurances don't override legal restrictions
- Circumvention attempts (intermediaries, modifications) are violations
- Penalties include fines, loss of privileges, and criminal charges
- Organizations must have export control compliance programs
- Suspicious inquiries should be reported to authorities
        """,
        "domain_reference": "Domain 1: Security and Risk Management - Export Controls, Regulatory Compliance, Dual-Use Technology"
    },

    # Scenario 9: Privacy Rights
    {
        "id": "d1_privacy_petition",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "THE PRIVACY PETITION",
                "narrative": """
A citizen named Aldric the Younger arrives at the Citadel with a formal
petition. He invokes the recently enacted "Right to Be Forgotten" - a new
privacy law granting citizens control over their personal information.

"I demand you erase all records of my name, my transactions, and my dealings
with the Citadel," Aldric declares. "The law grants me this right."

The Archivist checks the records and discovers Aldric's file contains:
- Personal details he provided during a guild application
- Transaction records from the marketplace
- A confidential security assessment noting "suspected smuggling involvement"
- Notes from an ongoing investigation into his business associates

Aldric insists the new privacy law overrides all other considerations.

How do you respond to Aldric's petition?
                """,
                "choices": [
                    {"text": "Grant the petition fully - the privacy law is clear about the right to erasure"},
                    {"text": "Deny the petition entirely - we need records for our operations"},
                    {"text": "Analyze each record type: erase commercial data, retain records with legal holds or regulatory requirements"},
                    {"text": "Tell Aldric to return after his dispute is settled and tax retention periods expire"}
                ],
                "success_text": """
You sit with Aldric and the Archivist to review his petition properly.

"Aldric, you have legitimate privacy rights under the new law, but these
rights have lawful exceptions. Let me explain what we can and cannot do."

"Your commercial records - purchases, memberships, general transactions -
these we CAN erase per your request. They serve no ongoing legal purpose."

"However, records related to your merchant dispute must be retained. Active
legal proceedings create a 'litigation hold' that supersedes erasure rights.
Destroying potential evidence could harm both parties and obstruct justice."

"Similarly, tax records must be kept for the period specified by financial
regulations. The privacy law explicitly exempts records required for legal
compliance."

Aldric accepts your explanation. "So my privacy rights are real, but not
unlimited. That is... fair, I suppose."

You have demonstrated understanding of PRIVACY RIGHTS AND EXCEPTIONS.
                """,
                "failure_texts": {
                    0: """
Privacy rights are rarely absolute. The 'right to be forgotten' typically
includes exceptions for legal obligations, ongoing disputes, and regulatory
requirements. Erasing records needed for tax compliance or active litigation
would violate other legal duties and could constitute destruction of evidence.
A blanket erasure ignores these critical exceptions.
                    """,
                    1: """
Organizational convenience is not grounds to deny legitimate privacy rights.
While some records must be retained, others can and should be erased when
requested. A blanket denial fails to properly analyze which records are
subject to the privacy right and which fall under legitimate exceptions.
                    """,
                    3: """
While the timing concern is valid for some records, this response fails to
address the records that CAN be erased now. The commercial transaction
history has no legal hold. Proper privacy compliance requires acting on
valid portions of a request even while explaining why other portions
cannot yet be fulfilled.
                    """
                }
            },
            "corporate": {
                "title": "THE DELETION REQUEST",
                "narrative": """
A DSAR (Data Subject Access Request) just landed in the privacy team's queue.
A former customer is invoking their GDPR Article 17 "right to erasure."

"I want ALL my data deleted. Everything. I know you have it, and I want it
GONE," the request reads. It's cc'd to a lawyer.

You pull up their record. This former customer has:
- Marketing preferences and email history (normal stuff)
- A support ticket history going back 3 years
- An open dispute over a $50,000 invoice that's headed to arbitration
- Records flagged for a pending SEC inquiry your legal team mentioned

The privacy officer looks nervous. "GDPR fines are 4% of global revenue.
Do we just... delete everything?"

What do you recommend?
                """,
                "choices": [
                    {"text": "Delete everything immediately - GDPR rights are absolute and those fines are scary"},
                    {"text": "Deny the request completely - we have legitimate business reasons for all this data"},
                    {"text": "Segment and analyze: delete marketing data, retain records under legal hold with documented exceptions"},
                    {"text": "Tell them to resubmit after the arbitration and SEC inquiry are resolved"}
                ],
                "success_text": """
You take a breath and walk through it methodically.

"GDPR Article 17 isn't absolute - it has explicit exceptions. Let's
categorize what we have:"

"Marketing preferences, email history, general support tickets older
than our retention policy? Delete those. That's a valid erasure request."

"The arbitration records? That's a legal hold. Article 17(3)(e) explicitly
exempts data needed for legal claims. We document that exception."

"The SEC inquiry? Same thing. We can't delete potential evidence in an
active investigation. We note the legal basis for retention."

"We respond to the customer professionally: 'We've deleted X, Y, Z.
Records A and B are retained under legal exceptions per Article 17(3).
Here's our documented reasoning.' Transparency builds trust."

The privacy officer relaxes. "So we're not ignoring GDPR - we're
applying it correctly, including its exceptions."

You've demonstrated PRIVACY RIGHTS AND EXCEPTIONS management.
                """,
                "failure_texts": {
                    0: """
You deleted records under legal hold for an SEC inquiry. That's not
GDPR compliance - that's obstruction of justice.

GDPR Article 17(3) explicitly lists exceptions for legal obligations
and legal claims. "Delete everything" isn't compliance - it's panic
that could land executives in federal prison.
                    """,
                    1: """
"We have business reasons" isn't a GDPR exception. The regulation
requires specific legal bases for retaining data against an erasure
request - legal obligations, legitimate interests that override the
subject's rights, etc.

Blanket denial without proper analysis is a fast track to regulatory
enforcement action.
                    """,
                    3: """
"Come back later" doesn't address the data you CAN delete now. Their
marketing preferences aren't under legal hold. Neither is most of
their support ticket history.

You're required to act on valid portions of a request while explaining
why other portions are retained. Refusing to do anything is itself
a GDPR violation.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 65,
        "hp_penalty": 20,
        "failure_text": """
Privacy rights typically include exceptions for:
- Legal obligations (tax records, regulatory requirements)
- Ongoing legal proceedings (litigation holds)
- Public interest (journalism, research, archiving)
- Legitimate business interests (where they outweigh privacy concerns)

Proper privacy compliance requires:
1. Analyzing each data category against applicable exceptions
2. Acting on valid erasure requests promptly
3. Documenting reasons for any denials
4. Informing the requestor of retained data and retention periods
        """,
        "domain_reference": "Domain 1: Security and Risk Management - Privacy Laws, Data Subject Rights, Legal Holds, Regulatory Retention"
    },

    # Scenario 10: Risk Transfer / Insurance
    {
        "id": "d1_insurance_claim",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "THE INSURANCE CLAIM",
                "narrative": """
A lightning strike damaged the Citadel's Eastern Tower, destroying several
valuable artifacts and interrupting operations for a week. The Citadel had
purchased insurance from the Merchant's Guild specifically for such events.

The Guild's assessor arrives and examines the damage. "The policy covers
the physical damage to the tower," she says, "but I see you're also claiming
for lost business during the restoration. And these 'intangible losses' for
damaged reputation?"

She reviews the policy carefully. "The standard policy covers property damage.
Extended coverage for business interruption was available but not purchased.
Reputational harm is generally uninsurable."

The Steward is frustrated. "We paid good gold for this insurance! Surely
they should cover our full losses?"

What do you explain to the Steward about risk transfer?
                """,
                "choices": [
                    {"text": "Insurance should cover everything - threaten legal action to force full payment"},
                    {"text": "Accept the property coverage, but understand that risk transfer has limitations - you can only transfer risks you've specifically contracted for"},
                    {"text": "Risk transfer is unreliable - we should have self-insured by keeping the premium gold in reserve"},
                    {"text": "File the full claim anyway - the insurer might pay to maintain good relations"}
                ],
                "success_text": """
You calm the Steward and explain the nature of risk transfer.

"Insurance is one form of risk transfer - we pay premiums to shift certain
risks to the insurer. But we can only transfer what we've specifically
contracted for. The policy we purchased covers property damage, and the
Guild will honor that coverage."

"Business interruption and reputational harm are real losses, but they
weren't included in our policy. For future planning, we should:"

"First, review our full risk exposure - property, business interruption,
liability, reputation. Second, for each risk, decide whether to accept,
mitigate, transfer, or avoid it. Third, when choosing to transfer via
insurance, ensure the policy actually covers the specific risks we intend
to transfer."

"Risk transfer is valuable, but it requires careful matching of policies
to actual risks. The uninsured losses we're experiencing now should inform
our coverage decisions going forward."

You have demonstrated understanding of RISK TRANSFER principles.
                """,
                "failure_texts": {
                    0: """
Insurance contracts are specific about what they cover. Threatening legal
action over losses explicitly excluded from a policy will fail and damage
the relationship with the insurer. The Steward's frustration is
understandable, but the coverage limitations were established before
the incident - they cannot be changed retroactively.
                    """,
                    2: """
Self-insurance is a valid strategy for small, frequent losses, but
catastrophic events like major storm damage typically exceed what most
organizations can absorb. The issue here isn't that risk transfer failed -
it's that the specific risks transferred didn't include all potential
losses. Both insurance and self-insurance have roles in a risk strategy.
                    """,
                    3: """
Filing claims for losses known to be excluded is potentially fraudulent
and will damage the relationship with the insurer. It may also increase
future premiums or lead to policy cancellation. Ethical conduct requires
claiming only what the policy legitimately covers.
                    """
                }
            },
            "corporate": {
                "title": "THE CYBER INSURANCE CLAIM",
                "narrative": """
Last month's ransomware attack is finally behind you. The servers are
restored, the forensics are complete, and now it's time to file the
insurance claim. You have a $5 million cyber insurance policy - surely
this is exactly what it's for.

The claims adjuster from CyberShield Insurance reviews the damages:
- $200,000 in forensics and incident response (covered)
- $150,000 in ransom payment (covered, with documentation)
- $800,000 in business interruption losses (hmm...)
- $2 million in reputational damage estimates (wait...)
- $500,000 in regulatory fines for the data breach (hold on...)

"I'm looking at your policy," she says. "You have standard cyber coverage.
Business interruption requires the 'Enhanced' tier - you have 'Basic.'
Regulatory fines are excluded under Section 14(b). And reputational
damage... that's not really insurable."

The CFO is livid. "We pay $80,000 a year for this policy!"

What do you explain?
                """,
                "choices": [
                    {"text": "Threaten to sue - we paid good money for this policy and they should pay out"},
                    {"text": "Accept what's covered, and review our policy for gaps we need to address at renewal"},
                    {"text": "Cyber insurance is worthless - we should self-insure and keep the premium money"},
                    {"text": "File the full claim anyway - adjusters always lowball, so shoot high"}
                ],
                "success_text": """
You take the CFO aside for a reality check.

"I know this is frustrating, but the policy is going to pay what it covers.
That's $350,000 for IR and ransom - which is real money. The rest? We
never bought coverage for it."

"Here's what we need to do going forward:"

"First, accept this payout and maintain a good relationship with CyberShield.
We may need them again."

"Second, at renewal, we review our actual risk exposure. Business
interruption is clearly a real risk - we need Enhanced coverage. We should
also look at first-party coverage limits."

"Third, for uninsurable risks like reputation, we need other strategies:
incident response plans, crisis communications prep, maybe a PR retainer."

"Insurance is one tool in risk management, not a magic wand. We can only
transfer risks we've specifically contracted for."

The CFO sighs. "So we got exactly what we paid for. Just not what we
needed." Exactly. Let's fix that at renewal.

You've demonstrated RISK TRANSFER understanding.
                """,
                "failure_texts": {
                    0: """
You're threatening to sue over policy exclusions that are clearly written
in your contract? Good luck with that. Insurance litigation is expensive,
and you'll lose because the policy says what it says.

Meanwhile, you've torpedoed your relationship with your insurer. Good luck
getting coverage renewal - or finding another carrier willing to take you.
                    """,
                    2: """
Self-insure against a $5 million loss? Unless your company has massive
cash reserves specifically earmarked for cyber incidents, that's not
realistic.

The problem wasn't that insurance failed - it's that you didn't buy the
right coverage. The solution is better insurance selection, not
abandoning risk transfer entirely.
                    """,
                    3: """
Filing claims for losses you know are excluded is insurance fraud. It's
also counterproductive - it wastes everyone's time and marks you as a
problem client.

Adjusters don't "lowball" - they apply the policy terms. Your job is to
understand what you bought and make sure it matches your needs.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 60,
        "hp_penalty": 20,
        "failure_text": """
Risk transfer through insurance:
- Only transfers specifically contracted risks
- Requires careful policy review to ensure coverage matches exposure
- Has limitations - some risks (like reputation) may be uninsurable
- Should be part of a broader risk treatment strategy

Risk treatment options include:
1. Accept - tolerate the risk as-is
2. Mitigate - implement controls to reduce likelihood or impact
3. Transfer - shift risk to another party (insurance, contracts)
4. Avoid - eliminate the risk by not engaging in the activity
        """,
        "domain_reference": "Domain 1: Security and Risk Management - Risk Transfer, Insurance, Risk Treatment Options"
    },

    # Scenario 11: Security Awareness Training
    {
        "id": "d1_mandatory_training",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "THE MANDATORY TRAINING",
                "narrative": """
The new Security Awareness program is ready to launch. The Training Master
presents three approaches for the Council's approval:

"Option one: A single comprehensive training session - four hours covering
all security topics. Efficient use of time, complete coverage in one day."

"Option two: Brief monthly reminders sent by messenger - short messages
about current threats. Minimal disruption to operations."

"Option three: A combination approach - initial training plus regular
refreshers, practical exercises, and different content for different roles.
More complex to administer."

The Council members debate. Some favor efficiency, others worry about
disruption to daily work. One elder notes that the last major security
incident occurred because a scribe didn't recognize a social engineering
attempt.

What training approach do you recommend?
                """,
                "choices": [
                    {"text": "Option one - comprehensive training ensures everyone receives complete information"},
                    {"text": "Option two - brief reminders minimize disruption while keeping security top-of-mind"},
                    {"text": "Option three - combined approach with role-based content maximizes retention and relevance"},
                    {"text": "Make training optional for experienced staff who already know security basics"}
                ],
                "success_text": """
The Council accepts your recommendation. You elaborate on the approach:

"Effective security awareness requires ongoing engagement, not one-time
events. The combined approach works because:"

"Initial training provides foundational knowledge - the WHY behind security
practices. Regular refreshers reinforce retention and address new threats.
Practical exercises - like simulated phishing attempts - test actual
behavior, not just knowledge. Role-based content ensures relevance - a
scribe needs different awareness than a guard."

"We should also measure effectiveness, not just completion. Track security
incidents before and after training. Test staff with realistic scenarios.
Adjust the program based on results."

"Remember, our goal isn't compliance checkboxes - it's actual behavior
change. The scribe who fell for social engineering didn't need more
information; they needed better training in recognizing and responding
to manipulation."

You have demonstrated understanding of SECURITY AWARENESS TRAINING.
                """,
                "failure_texts": {
                    0: """
Research consistently shows that single, lengthy training sessions lead to
poor retention. Humans forget most new information within days if it isn't
reinforced. A four-hour session might check a compliance box, but it won't
create lasting behavioral change - which is the actual goal of security
awareness training.
                    """,
                    1: """
Short reminders alone lack the depth needed to properly educate staff on
complex topics. Without foundational training, brief messages lack context.
Additionally, passive reminders don't build skills or change behavior -
they're easily ignored or forgotten.
                    """,
                    3: """
Security threats evolve constantly - 'experienced' staff may have outdated
knowledge. Additionally, making training optional signals that security
isn't truly important. Everyone, regardless of experience level, needs
regular refresher training. Social engineering attacks often target
overconfident individuals who believe they're too savvy to be fooled.
                    """
                }
            },
            "corporate": {
                "title": "THE MANDATORY TRAINING",
                "narrative": """
The annual security awareness training debate has arrived. The CISO presents
three proposals to the executive team:

"Option A: Four-hour annual compliance training. Everyone in a conference
room, PowerPoint marathon, check the box, done for the year."

"Option B: Monthly security tips via email. Quick reads, current threats,
minimal time investment."

"Option C: Blended approach - initial training, monthly micro-learning,
quarterly phishing simulations, role-specific modules. More complex to
manage, but more effective."

The CFO frowns. "Option A is cheapest. Option B is least disruptive.
Why would we choose C?"

Someone mentions that last quarter, an accountant wired $50,000 to scammers
because she didn't recognize a business email compromise attack.

What do you recommend?
                """,
                "choices": [
                    {"text": "Option A - comprehensive annual training ensures complete coverage and compliance"},
                    {"text": "Option B - monthly tips keep security top-of-mind without disrupting work"},
                    {"text": "Option C - the blended approach maximizes retention and tests actual behavior"},
                    {"text": "Make training optional for senior staff who've been here for years"}
                ],
                "success_text": """
You make the case for Option C.

"That $50,000 BEC loss? It happened because Sarah from accounting had the
knowledge but not the behavior. She sat through last year's training. She
probably even passed the quiz. But when the pressure was on and the email
looked real, she didn't stop to verify."

"Option A checks compliance boxes. Option B is easily ignored. Option C
actually changes behavior. Here's why it works:"

"Initial training builds the foundation. Monthly micro-learning reinforces
it before people forget. Phishing simulations test what people actually DO,
not what they know. Role-specific content means finance gets BEC training
while IT gets credential theft training."

"And we measure outcomes, not completion rates. Did phishing click rates
go down? Did incident reports go up? That tells us if the training works."

The CFO runs the numbers. "So Option C costs more upfront but prevents
losses like that $50K wire..." Exactly.

You've demonstrated SECURITY AWARENESS TRAINING principles.
                """,
                "failure_texts": {
                    0: """
The Ebbinghaus forgetting curve is brutal. Within a week of your four-hour
training marathon, people will have forgotten 80% of it. Within a month,
it's basically gone.

You've checked a compliance box. You haven't changed behavior. Sarah from
accounting will still click that BEC email.
                    """,
                    1: """
Monthly tips get filed in the same mental folder as "all-hands meeting
announcements" and "parking lot construction updates." People skim them,
maybe. Usually they just delete them.

Without foundational training, tips lack context. Without testing, you
have no idea if anyone's actually learning anything.
                    """,
                    3: """
"Senior staff know the basics" is how you get the CEO clicking phishing
links. Experienced people are often MORE vulnerable because they're
overconfident. They think they're too smart to be fooled.

Also, making training optional for anyone sends the message that security
is optional. It's not.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 60,
        "hp_penalty": 20,
        "failure_text": """
Effective security awareness programs:
- Use multiple modalities (training, reminders, exercises)
- Provide regular reinforcement, not just one-time events
- Tailor content to different roles and responsibilities
- Include practical exercises that test actual behavior
- Measure outcomes (incident reduction) not just completion
- Address the human element - psychology of manipulation
- Are mandatory for all staff regardless of experience

The goal is behavior change, not just information transfer.
        """,
        "domain_reference": "Domain 1: Security and Risk Management - Security Awareness Training, Human Factors, Behavior Change"
    },

    # Scenario 12: Audit Preparation
    {
        "id": "d1_audit_preparation",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "THE AUDIT PREPARATION",
                "narrative": """
Word arrives that the Kingdom's auditors will visit the Citadel in one moon's
time to assess compliance with royal security standards. The last audit was
three years ago and resulted in several findings that required remediation.

The Chief Steward calls an emergency meeting. "We have much to do. The
auditors will examine our policies, our practices, and our records. What
should be our priority in preparing?"

Several officers speak up:

The Records Keeper: "We should ensure all documentation is in order."

The Training Master: "Staff should be coached on what to say to auditors."

The Operations Chief: "We should focus on actually fixing our known
weaknesses, even if we can't document everything perfectly."

How do you advise the Chief Steward?
                """,
                "choices": [
                    {"text": "Focus on documentation - auditors primarily review records, so ensure paperwork is complete"},
                    {"text": "Coach staff on responses - consistent messaging prevents confusion during interviews"},
                    {"text": "Fix actual weaknesses while documenting accurately - genuine compliance over audit theater"},
                    {"text": "Request an audit delay - one moon isn't enough time to prepare properly"}
                ],
                "success_text": """
The Chief Steward nods as you explain your reasoning.

"Our goal should be genuine compliance, not audit theater. Auditors are
professionals trained to distinguish real practices from window dressing.
Here's our approach:"

"First, prioritize fixing actual weaknesses. Address the findings from
our last audit and any new issues we've identified. Real improvement
matters more than perfect documentation of poor practices."

"Second, document accurately. Our records should reflect what we actually
do - not what we wish we did or what we think auditors want to see.
Honest documentation of imperfect practices is better than false
documentation of perfect practices."

"Third, prepare staff to speak honestly. They should understand our
policies and be able to describe their actual daily practices. No scripts,
no coaching to give 'correct' answers - just honest engagement."

"If we fall short in some areas, we acknowledge it and present our
remediation plans. Auditors respect organizations that demonstrate
self-awareness and commitment to improvement."

You have demonstrated understanding of AUDIT PREPARATION and compliance.
                """,
                "failure_texts": {
                    0: """
While documentation matters, auditors don't just review paperwork. They
verify that documented practices are actually followed. Pristine
documentation that doesn't reflect reality creates worse audit findings
than incomplete documentation that accurately describes actual practices.
Auditors are trained to spot discrepancies.
                    """,
                    1: """
Coaching staff to give scripted responses is a form of deception that
auditors are trained to detect. When different staff give identical answers
to open-ended questions, it signals coaching rather than genuine practice.
This raises red flags and invites deeper scrutiny. Staff should be prepared
to honestly describe their actual practices.
                    """,
                    3: """
Organizations should always be audit-ready through continuous compliance.
Requesting delays signals that you know you're not compliant and need time
to create an appearance of compliance. This damages credibility and may
result in a more skeptical, thorough audit. The goal should be ongoing
compliance, not audit-specific preparation.
                    """
                }
            },
            "corporate": {
                "title": "THE SOC 2 AUDIT",
                "narrative": """
The calendar invite just landed: "SOC 2 Type II Audit - Fieldwork Begins
in 30 Days." Your company hasn't been audited in three years, and you
know there are gaps.

The emergency meeting convenes. Suggestions fly:

The Documentation Manager: "We need to get all our policies updated and
formatted. First impressions matter."

The IT Director: "Let's prepare a FAQ for staff so everyone knows what
to say when auditors ask questions."

The Security Engineer: "Forget the paperwork - we need to actually fix
the access control issues before they find them."

Someone suggests requesting a postponement to get properly ready.

What approach do you recommend?
                """,
                "choices": [
                    {"text": "Focus on documentation - auditors review policies first, so make them pristine"},
                    {"text": "Create staff talking points - consistent answers prevent contradictions"},
                    {"text": "Fix real issues while documenting accurately - genuine compliance beats audit theater"},
                    {"text": "Request a 60-day delay - we need more time to prepare properly"}
                ],
                "success_text": """
You stand up and address the room.

"Here's the reality: auditors are professionals. They've seen every flavor
of audit theater, and they're trained to spot it. Our best strategy is
genuine compliance."

"Priority one: Fix actual issues. Those access control gaps? Fix them.
Right now. A remediated finding is better than a finding that exists
because we were too busy polishing documentation."

"Priority two: Accurate documentation. Our policies should describe what
we actually do. If there's a gap between policy and practice, either
change the practice or update the policy - but make them match."

"Priority three: Prepare staff to be honest. No scripts. No canned
answers. Just 'here's what I do, here's why I do it.' Auditors respect
that. They get suspicious when five different people give identical
rehearsed answers."

"And no delay request. Asking to postpone screams 'we're not compliant
and need time to fake it.' Auditors will come in skeptical."

The room settles. Someone mutters, "So we just... tell the truth?"

Basically, yes.

You've demonstrated AUDIT PREPARATION best practices.
                """,
                "failure_texts": {
                    0: """
Auditors don't just read policies - they verify them. They'll ask staff
"show me how you do X" and compare it to what the policy says. Pristine
documentation that doesn't match reality is worse than honest documentation
of imperfect practices.

You've just set yourself up for a findings bonanza when practice doesn't
match policy.
                    """,
                    1: """
When five different employees give suspiciously similar answers to
open-ended questions, auditors notice. It's a red flag that screams
"coached responses."

This invites deeper scrutiny. The auditor will now go looking for what
you're trying to hide. You've made the audit harder, not easier.
                    """,
                    3: """
"We need more time" tells the auditor you know you're not compliant.
They'll come in assuming you're hiding problems and look extra hard
for them.

Also, continuous compliance means always being audit-ready. If you need
60 days to prepare, your compliance program has fundamental issues.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 65,
        "hp_penalty": 20,
        "failure_text": """
Proper audit preparation focuses on:
1. Genuine compliance - actually following policies and controls
2. Accurate documentation - records that reflect real practices
3. Honest engagement - staff who can describe actual procedures
4. Continuous readiness - not audit-specific cramming
5. Self-identification of issues - with remediation plans

Audit theater tactics that backfire:
- Scripted responses from staff
- Documentation that doesn't match practice
- Last-minute cosmetic fixes
- Delay requests that signal non-compliance
        """,
        "domain_reference": "Domain 1: Security and Risk Management - Compliance Auditing, Documentation, Continuous Compliance"
    },

    # Scenario 13: Risk Register Review
    {
        "id": "d1_quarterly_review",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "THE QUARTERLY REVIEW",
                "narrative": """
The Risk Council convenes for its quarterly review. The Risk Register -
a comprehensive scroll listing all identified risks and their treatments -
sits before the assembled officers.

"Since our last meeting," the Risk Keeper reports, "we've had no major
incidents. All controls are functioning as designed. I recommend we
affirm the current register without changes."

The younger Council members seem ready to agree and adjourn early. However,
you notice that the register was created two years ago. The kingdom has
changed significantly since then - new trade routes, new technologies,
shifting political alliances.

How do you advise the Council to proceed?
                """,
                "choices": [
                    {"text": "Accept the recommendation - no incidents means our risk management is working"},
                    {"text": "Request a complete reassessment - the entire register should be rebuilt from scratch"},
                    {"text": "Conduct a thorough review - evaluate existing risks, scan for new ones, and update treatments based on current conditions"},
                    {"text": "Focus only on adding new risks - the existing entries were already assessed and approved"}
                ],
                "success_text": """
You address the Council with measured urgency.

"Colleagues, the absence of incidents is encouraging, but it doesn't mean
our risks haven't changed. Our environment has evolved significantly in
two years, and our risk register must evolve with it."

"I propose a thorough review covering four areas:"

"First, existing risks - are they still relevant? Has likelihood or impact
changed? Are our treatments still effective?"

"Second, new risks - what threats have emerged from our new trade routes,
technologies, and political changes that weren't present two years ago?"

"Third, control effectiveness - even if risks are unchanged, have our
controls degraded? Are people still following procedures?"

"Fourth, treatment updates - do any risks require new or different responses
based on current conditions?"

The Council agrees to a proper review. Two days later, they discover several
new risks that had gone unidentified and three existing risks whose
treatments had become ineffective due to staff turnover.

You have demonstrated understanding of RISK MONITORING AND REVIEW.
                """,
                "failure_texts": {
                    0: """
The absence of incidents doesn't mean risks haven't changed. It could mean
we've been lucky, or that new risks haven't manifested yet. A two-year-old
risk register in a changing environment is almost certainly outdated. Risk
management requires active monitoring and updating, not just incident
response.
                    """,
                    1: """
While the register needs updating, a complete rebuild is excessive and
wasteful. Many identified risks and controls likely remain valid. The
proper approach is to review and update the existing register, not abandon
previous work. Risk management should be iterative, not periodic rebuilding.
                    """,
                    3: """
Existing risks must also be reassessed. Threat landscapes change, control
effectiveness degrades, and impact assessments shift with business changes.
A risk rated 'Low' two years ago might be 'High' today due to changed
circumstances. Both new and existing risks require regular evaluation.
                    """
                }
            },
            "corporate": {
                "title": "THE QUARTERLY GRC REVIEW",
                "narrative": """
It's Q4 risk review time. The GRC (Governance, Risk, and Compliance) team
has assembled in Conference Room B. The risk register spreadsheet glows
on the projector - all 847 rows of it.

"Good news everyone," the Risk Manager announces. "Zero incidents this
quarter. All KRIs green. I recommend we approve the register as-is and
break for lunch early."

The executives are already reaching for their phones. But you notice
something: the risk register was created two years ago, right before
the company pivoted to cloud-first. It still lists "mainframe failure"
as a top risk. The cloud infrastructure that now runs 80% of operations?
Two line items, both rated "Low."

Also, nobody's updated the "pandemic response" risk since 2020, despite
hybrid work becoming permanent.

What do you recommend?
                """,
                "choices": [
                    {"text": "Approve as-is - zero incidents means our risk management is working great"},
                    {"text": "Throw it out and start over - the entire register is clearly outdated"},
                    {"text": "Conduct a thorough review - evaluate existing risks, scan for new ones, update based on current business reality"},
                    {"text": "Just add the new cloud risks - everything else was already approved by leadership"}
                ],
                "success_text": """
You unmute yourself (it's a hybrid meeting, of course).

"Before we approve, I have concerns. This register is two years old, and
our business has fundamentally changed. Zero incidents doesn't mean zero
risk - it might mean we're tracking the wrong risks."

You share your screen and highlight some examples:

"Mainframe failure is listed as our #2 risk. We decommissioned the
mainframe 18 months ago. Meanwhile, our cloud infrastructure - which
runs 80% of production - has two line items rated 'Low.'"

"The hybrid work risks haven't been updated since the pandemic ended.
But hybrid is permanent now, and so are the associated risks."

"I recommend a structured review: validate existing risks against current
reality, scan for emerging threats, and update our treatments."

The CISO nods. "She's right. Let's schedule a proper review."

Two weeks later, the updated register identifies 12 new cloud-related
risks and deprecates 23 obsolete entries. The Risk Manager admits,
"I was just going through the motions. Thanks for pushing back."

You've demonstrated RISK MONITORING AND REVIEW.
                """,
                "failure_texts": {
                    0: """
Zero incidents means you haven't detected problems - it doesn't mean
problems don't exist. Your risk register still lists "mainframe failure"
as a top threat. You decommissioned the mainframe 18 months ago.

Meanwhile, actual risks - cloud misconfiguration, supply chain
compromise, remote work vulnerabilities - are barely documented.

"No news is good news" isn't a risk management strategy.
                    """,
                    1: """
Burn it down and start over? The existing register isn't worthless -
many risks are still valid. You just need to UPDATE it, not rebuild
from scratch.

Starting over means losing context, history, and institutional knowledge.
It also means 6 months of effort when 6 weeks of review would suffice.

Risk management is iterative, not periodic demolition and reconstruction.
                    """,
                    3: """
"Just add the new stuff" ignores the old stuff that's wrong. Your
register still lists the mainframe as a critical asset. The mainframe
is gone. The threat ratings for cloud infrastructure are laughably
outdated.

Adding new rows while leaving outdated rows in place creates a
risk register that's worse than useless - it actively misleads.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 60,
        "hp_penalty": 20,
        "failure_text": """
Risk monitoring and review requires:
- Regular reassessment of existing risks (at least annually)
- Environmental scanning for new and emerging risks
- Verification of control effectiveness
- Updates to risk treatments based on changed conditions
- Documentation of review findings and decisions

The risk register is a living document, not a static artifact.
'No incidents' doesn't mean 'no changes needed.'
        """,
        "domain_reference": "Domain 1: Security and Risk Management - Risk Monitoring, Risk Review, Risk Register Management"
    },

    # Scenario 14: Third-Party Risk
    {
        "id": "d1_new_partnership",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "THE NEW PARTNERSHIP",
                "narrative": """
The Merchant Council proposes an exciting opportunity: partnership with the
prestigious Ironhold Trading Company. Ironhold would handle all of the
Citadel's logistics - shipping, warehousing, and distribution - freeing
internal resources for core functions.

"Ironhold has an impeccable reputation," the Lead Merchant argues. "They
serve the three largest citadels in the realm. This partnership would
significantly improve our efficiency."

Before the agreement is signed, the Security Council must assess the
arrangement from a risk perspective. The Lead Merchant is impatient -
"Ironhold's reputation speaks for itself. Why delay this beneficial
partnership with bureaucratic assessments?"

How do you respond to the Security Council?
                """,
                "choices": [
                    {"text": "Approve based on reputation - Ironhold's track record with other citadels provides sufficient assurance"},
                    {"text": "Require a full security assessment of Ironhold before any partnership agreement"},
                    {"text": "Approve the partnership but include a termination clause in case problems arise"},
                    {"text": "Decline the partnership - third-party relationships always introduce unacceptable risk"}
                ],
                "success_text": """
You explain to the impatient Merchant why assessment is essential.

"Ironhold would have access to our logistics data, inventory information,
and potentially sensitive shipping details. They would become an extension
of our operations - and our attack surface. Their security posture directly
affects our security posture."

"A proper assessment should cover:"

"First, security practices - do their controls meet our requirements?
Second, compliance - are they certified to relevant standards?
Third, incident history - have they experienced breaches? How did they
respond? Fourth, subcontractors - do they outsource to others who would
also access our data?"

"We should also establish clear requirements in the contract: security
standards they must maintain, right to audit, breach notification
requirements, and liability provisions."

"Reputation is a starting point, not an endpoint. Trust, but verify."

The Merchant grudgingly agrees, and the subsequent assessment reveals
that Ironhold uses a subcontractor whose practices would not meet Citadel
standards - an issue that must be addressed before partnership.

You have demonstrated understanding of THIRD-PARTY RISK MANAGEMENT.
                """,
                "failure_texts": {
                    0: """
Reputation alone is not a substitute for proper due diligence. Other
citadels may have different risk tolerances or requirements. Ironhold's
practices, while suitable for them, may not meet our specific needs.
Additionally, past performance doesn't guarantee future security - even
reputable organizations can be compromised or have hidden weaknesses.
                    """,
                    2: """
A termination clause is necessary but not sufficient. By the time problems
'arise,' damage may already be done - data breached, operations disrupted,
reputation harmed. Prevention through upfront assessment is far more
valuable than the ability to exit after an incident. Both are needed.
                    """,
                    3: """
Third-party risk is manageable, not inherently unacceptable. Modern
organizations cannot avoid all external relationships. The goal is not
to eliminate third parties but to properly assess, monitor, and manage
the risks they introduce. Refusing all partnerships would severely limit
operational capability.
                    """
                }
            },
            "corporate": {
                "title": "THE VENDOR ONBOARDING",
                "narrative": """
The procurement team is excited. They've found a cloud provider that can
cut your infrastructure costs by 40%. CloudScale Solutions has an impressive
client list - three Fortune 500 companies use them.

"They're SOC 2 certified," the Procurement Director announces. "And their
references are stellar. We need to move fast - they're offering a 20%
discount if we sign by end of month."

But CloudScale would be hosting your customer database, processing payments,
and storing PII for 2 million users. They'd basically become an extension
of your infrastructure.

The CFO is pushing hard. "Their reputation is excellent. Why are we dragging
our feet with security bureaucracy?"

How do you advise the team?
                """,
                "choices": [
                    {"text": "Approve based on their reputation and SOC 2 certification - that's what SOC 2 is for"},
                    {"text": "Require a full vendor security assessment before signing any agreement"},
                    {"text": "Sign the deal but add a termination clause in case security issues emerge"},
                    {"text": "Reject the proposal - third-party cloud providers are inherently too risky"}
                ],
                "success_text": """
You stand your ground professionally.

"SOC 2 certification and references are a starting point, not an endpoint.
CloudScale will have access to 2 million customers' PII and payment data.
Their security posture directly affects our security posture."

"Before we sign, I need to assess:"

"First, their actual security controls - a SOC 2 report is a snapshot in
time, and the scope varies. What's actually in their report?"

"Second, their subprocessors - who do THEY outsource to? We need to know
the full supply chain."

"Third, incident history - have they had breaches? How did they respond?"

"Fourth, contractual protections - breach notification timelines, right
to audit, liability caps, data handling requirements."

"The 20% discount means nothing if they get breached and we're liable for
a GDPR fine that's 4% of global revenue."

The CFO pauses. "When you put it that way... let's do the assessment."

Two weeks later, your assessment reveals CloudScale uses a fourth-party
provider in a jurisdiction with no data protection laws. The deal
is restructured - or declined.

You've demonstrated THIRD-PARTY RISK MANAGEMENT.
                """,
                "failure_texts": {
                    0: """
SOC 2 certification isn't a security guarantee - it's a snapshot of
controls at a point in time, and the scope varies wildly. Some SOC 2
reports cover everything; others cover almost nothing useful.

You just signed a contract with a vendor who'll handle 2 million users'
PII based on a certificate you didn't even read. When they get breached,
your customers won't blame CloudScale - they'll blame you.
                    """,
                    2: """
"We can always terminate" is reactive thinking. By the time problems
emerge, their database has been exfiltrated. The termination clause
doesn't un-breach your customer data.

A termination clause is necessary but not sufficient. You need BOTH
upfront assessment AND exit provisions.
                    """,
                    3: """
"Cloud providers are too risky" in 2024? Good luck running a business
without any third-party services. Your competitors will eat your lunch
while you're maintaining your own data centers.

Third-party risk isn't inherently unacceptable - it's manageable with
proper assessment, contracts, and monitoring. Refusing all vendors
isn't security - it's paralysis.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 65,
        "hp_penalty": 20,
        "failure_text": """
Third-party risk management requires:
1. Due diligence - assess security practices before engagement
2. Contractual requirements - document security obligations
3. Right to audit - verify ongoing compliance
4. Subcontractor awareness - understand the full supply chain
5. Incident provisions - require breach notification
6. Monitoring - verify continued compliance throughout relationship

Reputation is not a substitute for proper assessment.
        """,
        "domain_reference": "Domain 1: Security and Risk Management - Third-Party Risk, Vendor Management, Supply Chain Security"
    },

    # Scenario 15: Security Policy Exception
    {
        "id": "d1_policy_exception",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "THE POLICY EXCEPTION",
                "narrative": """
Lord Commander Varys, one of the most respected military leaders in the
realm, requests an exception to the Citadel's password policy. The policy
requires complex passwords changed every 90 days, but the Lord Commander
argues his situation is unique.

"I command forces in the field, often under hostile conditions. I cannot
carry written passwords, and complex passwords are difficult to recall
under stress. I request permission to use a simpler, permanent password."

The Lord Commander's dedication is unquestionable. His forces protect the
kingdom's borders. He presents his case to the Security Council.

The younger officers seem inclined to grant the exception. "He's a war hero,"
one whispers. "Surely we can accommodate such a distinguished leader."

How do you advise the Council?
                """,
                "choices": [
                    {"text": "Grant the exception - the Lord Commander's circumstances are genuinely unique and his service exemplary"},
                    {"text": "Deny the exception but help find alternative authentication methods that address his legitimate constraints"},
                    {"text": "Deny the exception without discussion - policies exist for good reasons and must be enforced"},
                    {"text": "Grant a temporary exception while developing a better policy that addresses field conditions"}
                ],
                "success_text": """
You address the Lord Commander with respect for his service but firmness
on the principle.

"Lord Commander, your concerns are legitimate, and we honor your service.
However, granting a policy exception based on rank would undermine the
very security you fight to protect. Instead, let's solve the underlying
problem."

"For field conditions, we can offer alternatives: a token-based
authentication device that doesn't require memorizing passwords, or a
biometric seal that identifies you uniquely. These provide strong
authentication without the constraints of traditional passwords."

"We can also implement a tiered access system - limited access from field
locations with full access only from secured positions. This reduces risk
while maintaining operational capability."

The Lord Commander considers your proposal. "You're not simply saying 'no' -
you're helping me accomplish my mission securely. That I can respect."

You have demonstrated proper SECURITY POLICY EXCEPTION MANAGEMENT.
                """,
                "failure_texts": {
                    0: """
Granting exceptions based on status undermines the entire policy framework.
If the Lord Commander receives an exception, others will request the same
treatment. Soon the policy exists only for those without sufficient influence
to obtain exceptions. Security policies must apply equally regardless of
rank or reputation.
                    """,
                    2: """
While the conclusion (denial) is correct, the approach is wrong. Dismissing
legitimate operational concerns without attempting to address them breeds
resentment and drives people to work around security rather than with it.
The Lord Commander's constraints are real - they deserve consideration
even if the specific request must be denied.
                    """,
                    3: """
'Temporary' exceptions frequently become permanent. This approach signals
that the policy can be bypassed during the indefinite period of policy
development. It also leaves the Lord Commander's access vulnerable during
that time. The better approach is to solve the underlying problem now
rather than deferring it.
                    """
                }
            },
            "corporate": {
                "title": "THE EXECUTIVE EXCEPTION",
                "narrative": """
The CEO walks into your office - never a good sign.

"I need an exception to the password policy," she says. "I travel constantly,
use multiple devices, and can't remember 16-character passwords that change
every 90 days. I end up writing them on sticky notes, which I know isn't
great. I want to use a simpler password that I can actually remember."

Her schedule IS brutal. She's the most important person in the company.
And she's technically your boss's boss's boss.

The IT Director, who accompanied her, gives you a look that says "just
give her what she wants." The junior security analyst behind you looks
horrified.

What do you recommend?
                """,
                "choices": [
                    {"text": "Grant the exception - her circumstances are genuinely unique and she's the CEO"},
                    {"text": "Deny the exception but offer alternative authentication methods that address her legitimate concerns"},
                    {"text": "Deny the exception flatly - policies exist for good reasons and executives aren't above them"},
                    {"text": "Grant a temporary exception while IT develops a better solution for executives"}
                ],
                "success_text": """
You take a breath. This is the conversation that separates good security
people from great ones.

"I hear your frustration, and those are real constraints. But I can't
grant a policy exception - not because of bureaucracy, but because it
would undermine the policy for everyone else. If the CEO gets an
exception, every VP will want one too."

"However, let's actually solve your problem. How about:"

"First, a hardware security key. No passwords to remember - you just
tap it. Works on all your devices, travels easily."

"Second, a password manager with biometric unlock. One fingerprint and
you're in."

"Third, risk-based authentication. From your regular devices and
locations, fewer prompts. From new ones, we verify more carefully."

The CEO pauses. "So you're not just saying 'follow the rules' - you're
actually helping me."

"That's my job. Making security work for people, not against them."

She smiles. "Set me up with that security key thing."

You've demonstrated SECURITY POLICY EXCEPTION MANAGEMENT.
                """,
                "failure_texts": {
                    0: """
You just told everyone in the company that policies are optional for
important people. Within a week, every VP has submitted an exception
request. Within a month, your password policy only applies to people
without connections.

Attackers LOVE targeting executives - they have the highest privileges
and the most valuable access. You've just made your highest-value
targets your least-secured accounts.
                    """,
                    2: """
"No, follow the rules" is technically correct but practically useless.
You just made an enemy of your CEO, and she'll find ways around security
whether you help or not - sticky notes, shared passwords, bypasses.

Your job isn't to enforce rules blindly. It's to enable secure operations.
If you can't offer alternatives, you've failed even when you're right.
                    """,
                    3: """
"Temporary" exceptions become permanent exceptions. While IT "develops
a better solution" (which will take months because IT is always backed
up), the CEO is using a weak password.

Also, you've established the precedent that exceptions are available
while solutions are being developed. Every exception request will now
come with a "we'll fix it later" attached.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 65,
        "hp_penalty": 20,
        "failure_text": """
Security policy exception management:
- Policies should apply equally regardless of rank
- Exceptions undermine the entire policy framework
- Legitimate constraints deserve consideration and creative solutions
- Denial should be accompanied by alternatives when possible
- 'Temporary' exceptions tend to become permanent

The goal is to enable secure operations, not to blindly enforce rules.
Find ways to meet both security and operational requirements.
        """,
        "domain_reference": "Domain 1: Security and Risk Management - Security Policy, Exception Management, Authentication"
    },

    # Scenario 16: Whistleblower Handling
    {
        "id": "d1_whistleblower",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "THE WHISTLEBLOWER",
                "narrative": """
A junior scribe approaches you in confidence. She's trembling as she speaks.

"I've discovered something troubling. The Senior Archivist has been selling
copies of sensitive documents to outside parties. I've seen the gold change
hands. I wanted to report it, but... the Senior Archivist is well-connected.
His brother sits on the Council. I fear what might happen to me if I speak up."

She shows you a ledger she secretly copied - it appears to document the
transactions. The evidence seems credible, but you cannot verify it
immediately.

"What should I do?" she asks. "I want to do the right thing, but I'm afraid."

How do you counsel the junior scribe?
                """,
                "choices": [
                    {"text": "Tell her to confront the Senior Archivist directly - give him a chance to explain before escalating"},
                    {"text": "Advise her to report through proper channels, assure her of whistleblower protections, and offer to support her through the process"},
                    {"text": "Take the ledger and investigate yourself - you can verify the claims before involving others"},
                    {"text": "Suggest she forget what she saw - the risks of reporting outweigh the benefits"}
                ],
                "success_text": """
You speak calmly to reassure the frightened scribe.

"You've done the right thing by bringing this forward. The Citadel has
formal channels for reporting suspected misconduct, precisely because
situations like this can be intimidating."

"First, you should report to the Ethics Council through the confidential
reporting mechanism. This ensures your complaint is handled by people
independent of the Senior Archivist's connections."

"Second, the Citadel's whistleblower protections explicitly prohibit
retaliation against those who report suspected misconduct in good faith.
If anyone threatens or punishes you for reporting, that itself becomes
a serious violation."

"Third, I will personally ensure your report is received and acknowledged
through proper channels. You will not be alone in this process."

The scribe's fear doesn't disappear, but her resolve strengthens. "Thank you.
I was afraid I'd be told to stay quiet."

"Never," you reply. "Those who speak up protect us all."

You have demonstrated proper WHISTLEBLOWER HANDLING.
                """,
                "failure_texts": {
                    0: """
Direct confrontation with a suspected wrongdoer is dangerous, especially
when power imbalances exist. It gives the accused time to destroy evidence,
intimidate the witness, or construct alibis. It also puts the junior scribe
at personal risk. Suspected serious misconduct should go through proper
reporting channels, not personal confrontation.
                    """,
                    2: """
Personal investigation by an untrained party risks contaminating evidence,
alerting the suspect, and exceeding your authority. It also places you in
a difficult position - you become responsible for the investigation's
integrity. Proper channels exist for investigating misconduct. Your role
is to facilitate reporting, not conduct the investigation.
                    """,
                    3: """
Advising silence about suspected misconduct violates ethical obligations
and potentially legal duties. If the wrongdoing continues and causes harm,
both the witness and anyone who advised silence could bear responsibility.
Organizations need whistleblowers to identify problems. Discouraging
legitimate reports enables continued wrongdoing.
                    """
                }
            },
            "corporate": {
                "title": "THE ETHICS HOTLINE CALL",
                "narrative": """
A junior analyst from the Data Engineering team sends you a nervous Slack DM:
"Can we talk? Privately? It's important."

You meet in a quiet conference room. She's pale.

"I think my manager is selling customer data. I found exports to his personal
Google Drive - full PII, payment info, everything. I confronted him and he
said it was 'for a side project' and told me to forget about it."

"His uncle is the VP of Engineering. I'm scared to report this - I've only
been here six months. What if nobody believes me? What if I get fired?"

She shows you screenshots of the exports. They look legitimate. But you
can't verify the full chain of custody.

What do you advise?
                """,
                "choices": [
                    {"text": "Tell her to talk to her manager again - give him a chance to explain properly"},
                    {"text": "Advise her to use the anonymous ethics hotline, explain whistleblower protections, and offer support"},
                    {"text": "Take the screenshots and investigate yourself - you can verify the claims before escalating"},
                    {"text": "Suggest she let it go - rocking the boat this early in her career could backfire"}
                ],
                "success_text": """
You keep your voice calm and reassuring.

"You did the right thing by bringing this forward. This is exactly the
kind of situation our ethics program exists for."

"Here's what you should do: Use the anonymous ethics hotline. It's
designed for exactly this - reporting concerns when you're worried
about retaliation. The reports go to people outside the normal chain
of command."

"Second, our whistleblower policy explicitly protects employees who
report suspected misconduct in good faith. If anyone retaliates against
you - different assignments, bad reviews, termination - that itself
becomes a serious violation with real consequences."

"Third, I'll personally follow up to ensure your report is received
and handled properly. You're not alone in this."

She takes a breath. "I was afraid you'd tell me to keep my head down."

"Never. The people who speak up are the ones who protect this company
from itself."

You've demonstrated proper WHISTLEBLOWER HANDLING.
                """,
                "failure_texts": {
                    0: """
You just told her to confront the person who already warned her to
"forget about it." He's connected. She's junior. What do you think
happens next?

Best case: He deletes the evidence and she can't prove anything.
Worst case: He makes her life miserable until she quits. Either way,
the data theft continues.

Serious misconduct goes through proper channels, not confrontation.
                    """,
                    2: """
You're not an investigator. You're not authorized to conduct
investigations. And you've just inserted yourself into a potential
legal matter in a way that could compromise the entire case.

What if you access those systems and HE claims YOU were the one
exfiltrating data? You've just contaminated the evidence chain and
given a defense lawyer a field day.

Report through proper channels. Let qualified people investigate.
                    """,
                    3: """
"Keep your head down" is how companies get breached, sued, and shut
down. You just told a witness to suspected data theft to stay quiet.

If this gets worse - and it will - and it comes out that you knew and
advised silence? Your career is over. Possibly your freedom too, if
regulators get involved.

Whistleblowers protect organizations. Silencing them enables harm.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 70,
        "hp_penalty": 25,
        "failure_text": """
Proper whistleblower handling includes:
- Confidential reporting channels independent of potential wrongdoers
- Clear whistleblower protections against retaliation
- Good-faith reporting should be encouraged, not discouraged
- Support for reporters through the process
- Proper investigation by appropriate authorities

Discouraging reports enables wrongdoing.
Personal investigation risks contaminating evidence.
Confronting suspects can be dangerous and counterproductive.
        """,
        "domain_reference": "Domain 1: Security and Risk Management - Ethics, Whistleblower Protection, Reporting Mechanisms"
    },

    # Scenario 17: Security Budget Justification
    {
        "id": "d1_budget_meeting",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "THE BUDGET MEETING",
                "narrative": """
The annual budget review has arrived. The Treasury demands justification
for the Security Division's substantial allocation. Other divisions are
eager to claim any funds that might be freed up.

"Show me the return on this investment," the Lord Treasurer demands. "Every
gold piece spent on guards, wards, and training - what value does it provide?
The Kitchen accounts for every meal served. The Stables track every horse
maintained. What do YOU track?"

The challenge is familiar but difficult. Security spending often prevents
losses that might have occurred - but how do you demonstrate the value of
incidents that didn't happen?

How do you justify the security budget?
                """,
                "choices": [
                    {"text": "Point to the absence of major incidents - no breaches means security is working"},
                    {"text": "Present metrics on threats blocked, vulnerabilities remediated, compliance maintained, and comparison to industry loss data"},
                    {"text": "Warn about the catastrophic consequences of underfunding security - fear will justify the budget"},
                    {"text": "Accept whatever budget is offered - security should adapt to available resources"}
                ],
                "success_text": """
You present a comprehensive security metrics report.

"Lord Treasurer, let me show you what your investment has purchased:"

"First, threat metrics: Last year our perimeter defenses blocked 847
unauthorized access attempts. Our fraud detection identified 23 fraudulent
transaction attempts totaling an estimated 12,000 gold pieces."

"Second, vulnerability management: We identified and remediated 156
weaknesses in our defenses before they could be exploited. Based on
industry data, each unpatched critical vulnerability carries an average
exploitation cost of 500 gold pieces."

"Third, compliance: We maintained full compliance with Royal Standards,
avoiding potential fines of up to 10,000 gold pieces and reputational
damage from public disclosure of non-compliance."

"Fourth, industry comparison: Organizations of our size experience an
average of 3.2 significant incidents per year with average costs of
8,000 gold pieces each. Our investment has kept us well below this
benchmark."

The Lord Treasurer reviews the data. "This is... actually quite clear.
Very well - the allocation stands."

You have demonstrated SECURITY METRICS AND ROI justification.
                """,
                "failure_texts": {
                    0: """
'Nothing bad happened' is unconvincing to budget authorities. They cannot
distinguish between effective security and lucky circumstances. This
argument also makes security vulnerable when incidents DO occur - if
'no incidents' justifies the budget, does 'some incidents' mean the budget
was wasted? This reasoning creates a lose-lose situation.
                    """,
                    2: """
Fear-based arguments, while sometimes effective short-term, erode
credibility over time. If predicted catastrophes don't materialize,
security appears to be crying wolf. If they do materialize, the budget
failed to prevent them. Professional security justification uses data
and business analysis, not fear tactics.
                    """,
                    3: """
Passive acceptance fails to advocate for appropriate security investment.
If security is genuinely underfunded, accepting inadequate resources
without objection makes the Security Division complicit in the resulting
risks. While we must ultimately work within budgets, we have an obligation
to clearly communicate what risks those budgets leave unaddressed.
                    """
                }
            },
            "corporate": {
                "title": "THE BUDGET DEFENSE",
                "narrative": """
It's annual budget season. The CFO has summoned you to justify the
security team's $2.3 million budget request.

"Help me understand what I'm buying," she says, not unkindly. "Marketing
can show me leads generated. Sales shows me revenue closed. Engineering
ships features. What does Security produce?"

It's the eternal security dilemma: your success is measured in things
that didn't happen. How do you prove the value of prevented breaches?

The other department heads are watching. They'd love to absorb some of
your headcount if you can't make your case.

How do you justify your budget?
                """,
                "choices": [
                    {"text": "Point to zero major breaches this year - no news is good news"},
                    {"text": "Present metrics: threats blocked, vulns fixed, compliance maintained, plus industry breach cost comparisons"},
                    {"text": "Paint a picture of what happens if you're underfunded - fear is motivating"},
                    {"text": "Accept whatever budget is offered - security should work within constraints"}
                ],
                "success_text": """
You've prepared for this. You open your dashboard.

"Let me show you what your investment purchased this year."

"First, threat metrics: Our email security blocked 47,000 phishing attempts.
Our firewall blocked 2.3 million unauthorized connection attempts. Our
endpoint protection quarantined 847 malware instances."

"Second, vulnerability management: We identified and patched 1,247
vulnerabilities, including 89 critical ones. Industry data shows the
average cost of exploiting a critical vuln is $200,000."

"Third, compliance: We passed our SOC 2 audit with zero findings. A
failed audit would have cost us the Acme contract - that's $4M annually."

"Fourth, industry benchmarks: Companies our size average 3.2 breaches per
year with an average cost of $4.2M each. Our investment kept us at zero."

The CFO reviews the numbers. "So you're saying my $2.3M investment
prevented potential losses of... significantly more than $2.3M."

"That's exactly what I'm saying."

"Budget approved."

You've demonstrated SECURITY METRICS AND ROI justification.
                """,
                "failure_texts": {
                    0: """
"Nothing bad happened" isn't a metric - it's an absence of data. The
CFO can't distinguish between "security is working" and "we got lucky."

Also, what happens next year when you DO have an incident? Your entire
justification framework collapses. "We had no breaches last year" becomes
"we had one breach this year" - does that mean the budget failed?

You need metrics that work regardless of whether you have incidents.
                    """,
                    2: """
"Give me money or bad things will happen" is not a business case. It's
a threat. And it erodes your credibility every time the predicted
catastrophe doesn't materialize.

If the breach doesn't happen, you look like Chicken Little. If it does
happen, your budget didn't prevent it. Fear is a lose-lose justification
strategy.
                    """,
                    3: """
"Whatever you think is fair" just told the CFO that security isn't
important enough to fight for. She'll happily reallocate your headcount
to Marketing, who made a much better case for their needs.

If your budget is genuinely necessary, you have an obligation to
articulate why. Accepting inadequate resources makes you complicit
in the resulting risks.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 60,
        "hp_penalty": 20,
        "failure_text": """
Effective security budget justification includes:
1. Quantified metrics - threats blocked, vulnerabilities fixed
2. Cost avoidance - potential losses prevented
3. Compliance value - fines and reputation damage avoided
4. Industry benchmarks - comparison to peer organizations
5. Risk-based analysis - what risks does the budget address

Avoid:
- 'Nothing bad happened' (unconvincing)
- Fear-based arguments (erodes credibility)
- Passive acceptance (abdicates responsibility)

Security must speak the language of business value.
        """,
        "domain_reference": "Domain 1: Security and Risk Management - Security Metrics, ROI, Budget Justification, Risk Communication"
    },

    # Scenario 18: Personnel Security / Succession Planning
    {
        "id": "d1_succession_plan",
        "domain": 1,
        "themes": {
            "fantasy": {
                "title": "THE SUCCESSION PLAN",
                "narrative": """
The Master of Keys, keeper of the Citadel's most sensitive cryptographic
secrets, announces her retirement after forty years of service. She is the
only person who knows certain historical decryption methods, and she alone
can access the deepest vault.

"I've trained no successor," she admits. "The knowledge was too sensitive
to share widely. I always meant to document it, but the work was constant,
and now... well, here we are."

The Council is alarmed. Without the Master of Keys, certain archives become
permanently inaccessible, and historical continuity of cryptographic
practices will be lost.

How do you advise handling this personnel security failure?
                """,
                "choices": [
                    {"text": "Convince the Master of Keys to delay retirement until a successor is fully trained"},
                    {"text": "Immediately document all knowledge, establish succession requirements, and implement key person risk management"},
                    {"text": "Accept that some knowledge will be lost - this is an unavoidable consequence of tight security"},
                    {"text": "Promote the most senior remaining cryptographer to Master of Keys immediately"}
                ],
                "success_text": """
You take charge of addressing this critical personnel security gap.

"We face both an immediate transition and a systemic failure. Let's
address both."

"For the immediate situation: The Master of Keys must comprehensively
document all procedures, secrets, and access methods before departure.
This documentation will be secured with dual control - no single person
will have complete access. She will train at least two successors to
ensure no single point of failure."

"For systemic improvement: We must implement key person risk management
across the Citadel. Every critical role requires documented procedures,
cross-training, and succession planning. We need regular reviews to
identify emerging single points of failure before they become crises."

"Additionally, we should establish security requirements for role changes:
background verification for sensitive positions, proper handoff procedures,
and immediate access revocation upon departure."

The Council authorizes an intensive two-month transition period. The
Master of Keys remarks, "I wish someone had insisted on this years ago."

You have demonstrated understanding of PERSONNEL SECURITY management.
                """,
                "failure_texts": {
                    0: """
While buying time for transition is reasonable, this doesn't address the
systemic failure that allowed this situation to develop. Any delay is
temporary - the successor could later leave, become incapacitated, or
retire with the same result. The real problem is single points of failure
in knowledge and access. That must be addressed regardless of timeline.
                    """,
                    2: """
Knowledge loss is not an acceptable outcome of security - it's a security
failure. Proper security includes continuity of capability. If security
measures prevent legitimate succession and knowledge transfer, those
measures are poorly designed. Secure knowledge transfer is possible; it
simply requires planning and appropriate controls.
                    """,
                    3: """
Seniority alone doesn't qualify someone to assume critical responsibilities.
The new Master of Keys needs specific knowledge transfer, proper vetting,
and gradual assumption of duties. Immediate promotion without preparation
risks errors, security incidents, or simply an unqualified person in a
critical role. Succession must be managed, not improvised.
                    """
                }
            },
            "corporate": {
                "title": "THE BUS FACTOR",
                "narrative": """
Marcus, your senior DBA, just gave two weeks notice. He's taking a job
at a competitor for a 40% raise. Everyone wishes him well.

Then reality sets in.

Marcus is the only person who knows the production database passwords.
Marcus is the only one with access to the legacy encryption keys. Marcus
built the backup system and never documented it. Marcus is the "bus factor"
for basically your entire data infrastructure.

"I always meant to document everything," he says apologetically. "But
there was always something more urgent."

IT leadership is panicking. The CTO is asking how this happened.

What do you recommend?
                """,
                "choices": [
                    {"text": "Offer Marcus whatever it takes to stay - match the competitor's offer, add a bonus"},
                    {"text": "Immediately start knowledge capture: documentation, recorded walkthroughs, cross-training - and fix the systemic failure"},
                    {"text": "Accept that some knowledge will be lost - this is the reality of IT"},
                    {"text": "Promote the most senior remaining engineer to his role right away"}
                ],
                "success_text": """
You call an emergency meeting.

"We have an immediate problem and a systemic problem. Let's address both."

"Immediate: Marcus's last two weeks become intensive knowledge transfer.
Every system he touches gets documented. Every password gets recorded in
our vault. Every process gets video-recorded walkthroughs. He trains at
least two people on every critical function."

"Systemic: We need to identify every 'bus factor' role in the organization.
Every critical function needs documentation, cross-training, and succession
planning. No single person should ever be the only one who can do
anything important."

"We also need offboarding procedures: access revocation checklists, knowledge
handoff requirements, and exit interviews focused on capturing institutional
knowledge."

Marcus actually looks relieved. "Honestly, I've been stressed about being
the only one who knows this stuff. It's not fun knowing that if I get
hit by a bus, the company's in trouble."

The CTO nods grimly. "This is a wake-up call. Let's not need another one."

You've demonstrated PERSONNEL SECURITY and succession planning.
                """,
                "failure_texts": {
                    0: """
Counter-offers are a band-aid, not a solution. Even if Marcus stays,
what happens when he gets sick? Gets hit by a bus? Decides to leave
again in six months?

The fundamental problem isn't that Marcus is leaving - it's that critical
knowledge exists only in one person's head. That problem exists whether
Marcus stays or goes.
                    """,
                    2: """
"Sometimes knowledge is lost" is how companies suffer catastrophic failures.
What if Marcus had a heart attack instead of a resignation? Would you
accept "well, sometimes people die" as a risk management strategy?

Knowledge loss isn't inevitable - it's a failure of planning. Secure
knowledge transfer is possible with proper documentation, cross-training,
and succession planning. Accepting loss is giving up.
                    """,
                    3: """
"Most senior" doesn't mean "qualified to replace Marcus." The next person
on the org chart doesn't automatically know the production passwords or
the backup procedures.

Immediate promotion without knowledge transfer means you now have someone
with Marcus's title but none of Marcus's knowledge. You've solved nothing
and potentially created new problems.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 70,
        "hp_penalty": 25,
        "failure_text": """
Personnel security includes:
1. Succession planning - never single points of failure for critical roles
2. Knowledge documentation - procedures and secrets properly recorded
3. Cross-training - multiple people capable of critical functions
4. Role change procedures - proper handoffs and access management
5. Background verification - for sensitive position changes
6. Access revocation - immediate upon role termination

Key person risk is a common security vulnerability that
planning and process can prevent.
        """,
        "domain_reference": "Domain 1: Security and Risk Management - Personnel Security, Succession Planning, Key Person Risk"
    }
])
