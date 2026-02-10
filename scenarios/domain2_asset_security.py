"""
Domain 2: Asset Security scenarios.

Key CISSP concepts tested:
- Data Classification and Handling
- Asset Ownership and Responsibilities
- Data Lifecycle Management
- Retention Policies and Legal Holds
- Data Remanence and Secure Destruction
- Privacy Protection and Data Minimization

Each scenario supports dual themes:
- Fantasy: Medieval/magical Citadel setting
- Corporate: Modern office satire (Office Space style)
"""

DOMAIN_2_SCENARIOS = [
    # Scenario 1: Data Classification
    {
        "id": "d2_unmarked_chest",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE UNMARKED CHEST",
                "narrative": """
A dusty chest is discovered in a forgotten corner of the Citadel's storage
chambers. Inside lies a collection of scrolls, documents, and small artifacts.
None bear any classification markings - no seals, no labels, no indicators of
their sensitivity or value.

The young archivist who found them asks: "What should we do with these? Some
look ordinary, but others... these symbols seem important. Without markings,
how do we know how to handle them?"

The Storage Master suggests simply storing them with general inventory. "If
they were important, they would have been marked. Let's not create unnecessary
work."

The archivist looks to you for guidance. Unlabeled assets in a security-
conscious environment present a genuine dilemma.

How do you advise handling the unmarked materials?
                """,
                "choices": [
                    {"text": "Store with general inventory - if they were sensitive, they would have been marked"},
                    {"text": "Treat as highest classification until properly assessed and marked"},
                    {"text": "Destroy the materials - unclassified items represent a liability"},
                    {"text": "Leave them where they were found until someone claims them"}
                ],
                "success_text": """
You instruct the team carefully.

"When materials lack classification, we must assume the highest plausible
sensitivity until we can properly assess them. Here's why:"

"First, absence of marking often indicates failure to classify, not low
sensitivity. These items may pre-date our classification system, or their
labels may have been lost or removed."

"Second, the cost of over-protecting is temporary inconvenience. The cost
of under-protecting could be breach of genuinely sensitive information."

"We will secure these materials in the restricted archive. A qualified
assessor will examine each item, determine its proper classification, and
apply appropriate markings. Only after this process can items be moved to
less restrictive storage."

The archivist nods. "So the default for unknown items is 'handle with care'
until proven otherwise?"

"Exactly. When in doubt, protect. We can always reduce restrictions later,
but we cannot undo unauthorized exposure."

You have demonstrated proper ASSET CLASSIFICATION principles.
                """,
                "failure_texts": {
                    0: """
Assuming unmarked materials are low-sensitivity is dangerous. The absence of
markings often indicates failure to classify, not intentional low classification.
Sensitive materials may have lost their labels, or pre-date the classification
system. Treating unknown materials as low-sensitivity risks exposing genuinely
sensitive information to unauthorized access or improper handling.
                    """,
                    2: """
Destroying materials without assessment is reckless. The documents may contain
valuable information, historical records, or evidence of important events.
Destruction should only occur through proper disposal procedures AFTER items
have been assessed and determined to have no value. Hasty destruction could
destroy irreplaceable assets.
                    """,
                    3: """
Abandoning discovered materials creates ongoing risk. If they contain sensitive
information, they remain vulnerable in their unsecured location. If they're
valuable, they continue to deteriorate. Discovered assets must be processed
through proper channels - assessment, classification, and appropriate storage
or disposal.
                    """
                }
            },
            "corporate": {
                "title": "THE UNLABELED USB DRIVE",
                "narrative": """
Facilities found a box of USB drives in a supply closet during the office
renovation. No labels, no owner names, just a dozen random USB sticks
covered in dust.

"Someone probably forgot about these," the facilities manager says. "Should
we just toss them?"

The intern suggests plugging one into her laptop to see what's on it.
The IT guy shrugs - "If they were important, someone would have labeled them."

But you're thinking about all the possibilities: old backups with customer
data, someone's personal files, or even drives that were intentionally
hidden. USB drives found in a corporate environment are like mystery boxes
that could contain anything from nothing to nuclear launch codes.

What do you recommend?
                """,
                "choices": [
                    {"text": "Label them as 'General' and put them in the supply cabinet - they're just USB drives"},
                    {"text": "Secure them and treat as potentially sensitive until IT forensically examines them"},
                    {"text": "Destroy them immediately - unmanaged USB drives are a security liability"},
                    {"text": "Leave them in the closet until someone claims them"}
                ],
                "success_text": """
You stop everyone before anyone does something regrettable.

"Nobody plugs anything in. We treat these as potentially sensitive until
we know what's on them."

"Here's the deal: unmarked storage media could contain anything. Old
project files, customer PII, proprietary code, or someone's resume from
2015. We can't know without forensic examination, and we can't do that
forensic examination on production systems."

"Step one: bag and tag. Each drive gets a tracking number. Step two:
secure storage. These go in the locked evidence cabinet. Step three:
forensic review. IT Security examines them on an isolated system."

"Only after we know what's on them do we decide whether to destroy,
archive, or return them to someone."

The intern looks disappointed she didn't get to plug one in. "So the
default is 'assume important until proven otherwise'?"

"Exactly. We can always downgrade later. We can't un-leak data."

You've demonstrated DATA CLASSIFICATION principles.
                """,
                "failure_texts": {
                    0: """
You just labeled mystery USB drives as 'General' and made them available
to anyone. If one of those drives contains customer social security
numbers from a 2018 backup, you've just created a potential breach.

Unmarked doesn't mean unimportant. It means "unknown." And unknown should
be treated with caution, not casual disregard.
                    """,
                    2: """
You destroyed potential evidence without examination. What if those
drives contained records from a project that's now under litigation?
What if they had the only copy of documentation someone needs?

Destruction should happen AFTER assessment, not before. "They might be
bad" isn't justification for destroying "we don't know what."
                    """,
                    3: """
So the mystery USB drives stay in an unlocked supply closet... forever?
They're either important (in which case they're vulnerable) or they're
not (in which case they're taking up space and creating confusion).

Discovered assets need to be processed: examined, classified, and
handled appropriately. Ignoring them solves nothing.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 70,
        "hp_penalty": 20,
        "failure_text": """
Proper handling of unclassified materials:
- Assume highest plausible classification until properly assessed
- Secure in appropriate restricted storage pending review
- Conduct formal assessment by qualified personnel
- Apply proper classification markings based on content
- Document the discovery, assessment, and final classification

Never assume unmarked means unimportant.
        """,
        "domain_reference": "Domain 2: Asset Security - Data Classification, Handling Requirements, Labeling"
    },

    # Scenario 2: Asset Ownership
    {
        "id": "d2_departing_scribe",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE DEPARTING SCRIBE",
                "narrative": """
Senior Scribe Aldwin has announced his retirement after thirty years of
service. During his tenure, he accumulated vast knowledge about the Citadel's
operations, created numerous procedural documents, and maintained several
critical record systems.

"Who takes over Aldwin's responsibilities?" the Chief Administrator asks.
"His apprentice Marcus seems capable, but Marcus reports to the Operations
division, not Records."

The Keeper of Records suggests: "Let Marcus inherit everything - he knows
the systems best."

The Operations Chief counters: "Those records belong to Operations now that
Aldwin is leaving. We'll assign someone from our team."

Aldwin himself shrugs. "I always just did what needed doing. Never thought
much about who 'owned' what."

The lack of clarity threatens continuity. How do you advise resolving this?
                """,
                "choices": [
                    {"text": "Give everything to Marcus - practical knowledge trumps organizational charts"},
                    {"text": "Let Operations take over - the work serves their mission anyway"},
                    {"text": "Identify appropriate data owners for each category based on business accountability, then assign custodians"},
                    {"text": "Archive everything until the organization decides what to do with it"}
                ],
                "success_text": """
You guide the discussion toward proper asset ownership principles.

"First, we must distinguish between data OWNERS and data CUSTODIANS. The
owner is accountable for the data - they determine who can access it, how
it should be protected, and when it should be disposed. The custodian
maintains the data day-to-day but acts under the owner's authority."

"Aldwin created and maintained many things, but he wasn't necessarily the
OWNER of all that information. Let's categorize his work:"

"Operational procedures belong to whoever is accountable for those operations.
Financial records belong to Treasury. Personnel records belong to Human
Resources. Each owner then decides who will serve as custodian."

"Marcus may well be the best custodian for some systems - but that's different
from ownership. Owners must be identified based on business accountability,
not just technical familiarity."

The Chief Administrator nods. "So we need to inventory Aldwin's work, identify
the rightful owner for each category, and then let owners designate custodians."

"Exactly. This ensures no data becomes orphaned and accountability is clear."

You have demonstrated understanding of DATA OWNERSHIP AND CUSTODY.
                """,
                "failure_texts": {
                    0: """
While Marcus has practical knowledge, transferring ownership based solely on
familiarity ignores proper governance. Data ownership must align with business
accountability. The person who owns data is responsible for its protection,
accuracy, and appropriate use. Marcus may be a suitable custodian, but
ownership decisions should be based on organizational responsibility, not
just who happens to know the systems.
                    """,
                    1: """
Blanket transfer to a department ignores the nuance of different data types.
Aldwin likely worked with multiple categories of information - some operational,
some administrative, some cross-functional. Each category may have different
legitimate owners. Giving everything to one department may place sensitive
data with inappropriate owners who lack accountability for that information.
                    """,
                    3: """
Passive archiving creates orphan data - information without clear ownership,
accountability, or maintenance. Over time, archived data becomes stale,
potentially inaccurate, and increasingly difficult to properly classify.
Active decisions about ownership must be made during transitions, not deferred
indefinitely.
                    """
                }
            },
            "corporate": {
                "title": "THE KNOWLEDGE TRANSFER",
                "narrative": """
Bob from IT has finally given his two weeks notice after 15 years. Nobody's
really sure what Bob does exactly, but he seems to touch everything - the
legacy inventory system, various SharePoint sites, a bunch of Access databases,
and spreadsheets that somehow run half the company.

"So who owns all of Bob's stuff?" your manager asks in the emergency meeting.

HR says: "His direct reports should inherit his responsibilities."

The Operations Director objects: "Those systems serve our department. We
should take ownership."

IT argues: "It's all technical infrastructure. It belongs with us."

Bob himself shrugs from the back of the room. "I just built whatever people
asked for. Never really thought about who 'owns' it. Does anyone even have
documentation?"

The meeting devolves into turf wars while you realize nobody has a clear
answer. Bob's last day is in two weeks.

How do you advise handling this transition?
                """,
                "choices": [
                    {"text": "Give everything to Bob's team - they know the systems best"},
                    {"text": "Let Operations take over - they're the main users anyway"},
                    {"text": "Identify appropriate data owners for each system based on business accountability, then assign custodians"},
                    {"text": "Archive everything to a shared drive until leadership decides what to do"}
                ],
                "success_text": """
You interrupt the turf war with a framework that actually makes sense.

"Hold on. We're conflating two different things: data OWNERSHIP and data
CUSTODY. The owner is accountable for the data - they decide who accesses
it, how it's protected, and when it's deleted. The custodian maintains it
day-to-day but under the owner's authority."

"Bob maintained a lot of systems, but he wasn't the OWNER of all that data.
Let's categorize what he touched:"

"The inventory system? That's Operations' data - they're accountable for
inventory accuracy. The HR spreadsheets? HR owns that data. The financial
Access database? Finance owns it."

"Bob was the CUSTODIAN. Now we need to identify new custodians, but the
owners haven't changed. Each data owner should designate who maintains
their systems going forward."

Your manager nods slowly. "So we inventory Bob's stuff, figure out who
actually OWNS each piece, and they assign new custodians?"

"Exactly. Otherwise we get orphan data - stuff nobody's responsible for,
that slowly rots until it causes a compliance nightmare."

HR starts a list. "This is going to take more than two weeks..."

You've demonstrated DATA OWNERSHIP AND CUSTODY principles.
                """,
                "failure_texts": {
                    0: """
Just because Bob's team knows the systems doesn't mean they should own the
data. "Knowing how it works" and "being accountable for the data" are
different things.

Now you've got IT people responsible for HR data integrity. When auditors
ask "who's accountable for this personnel information?" the answer is...
some developer who happened to build the system?

Ownership should follow business accountability, not technical familiarity.
                    """,
                    1: """
Operations uses a lot of Bob's systems, but they don't use ALL of them.
What about the HR spreadsheets? The finance databases? The marketing reports?

You just gave one department ownership of data they shouldn't control. When
HR needs to update their own processes, they now have to ask Operations for
permission?

Different data serves different business functions. Each function should
own their own data.
                    """,
                    3: """
Ah yes, the corporate equivalent of shoving everything in a closet and
hoping the problem goes away.

That shared drive will become a data graveyard. Nobody maintains it, nobody
knows what's in it, but everyone's afraid to delete anything. In three years
someone will discover PII in there during an audit.

Data without clear ownership becomes liability. You need to make ownership
decisions now, not "later" (which means never).
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 65,
        "hp_penalty": 20,
        "failure_text": """
Data ownership principles:
- OWNER: Accountable for data - determines access, protection, disposal
- CUSTODIAN: Maintains data day-to-day under owner's authority

When staff transitions occur:
1. Inventory data and systems they managed
2. Categorize by business function
3. Identify appropriate owner based on business accountability
4. Owner designates new custodian(s)
5. Document ownership and custody assignments

Familiarity is not the same as ownership.
        """,
        "domain_reference": "Domain 2: Asset Security - Asset Ownership, Data Custodian, Roles and Responsibilities"
    },

    # Scenario 3: Data Remanence / Secure Destruction
    {
        "id": "d2_burned_ledger",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE BURNED LEDGER",
                "narrative": """
The Treasury has retired its old record-keeping system. The ancient ledgers
contain decades of financial transactions, some involving sensitive payments
to intelligence agents, covert operations funding, and confidential
negotiations with foreign powers.

"These ledgers must be destroyed," the Treasurer declares. "The information
is no longer needed for operations, and its exposure could compromise
ongoing activities and endanger lives."

The clerks present their options:

"We can burn them in the courtyard furnace - fire destroys all," suggests
the first clerk.

"I can scratch out the entries with acid and reuse the parchment," offers
the second.

"Simply place them in the locked disposal bin - the waste handlers will
deal with them," says the third.

The Treasurer turns to you. "Which method ensures these secrets truly die?"

How do you advise on destroying these highly sensitive records?
                """,
                "choices": [
                    {"text": "Burn in the furnace - fire is the most thorough destruction method"},
                    {"text": "Acid treatment - this allows parchment reuse and destroys the content"},
                    {"text": "Locked disposal bin - the waste handlers are vetted and trustworthy"},
                    {"text": "Archive in deep storage - complete destruction seems wasteful for historical records"}
                ],
                "success_text": """
You confirm the Treasurer's instincts about thorough destruction.

"For materials of this sensitivity, complete physical destruction through
burning is the most reliable method. Here's why the alternatives fail:"

"Acid treatment can leave traces - impressions, partial inks, or missed
pages. Forensic recovery techniques could potentially reconstruct information.
When lives and operations are at stake, 'potentially readable' is unacceptable."

"Transferring to waste handlers breaks our chain of custody. Even trusted
personnel face risks we cannot control. For the most sensitive materials,
destruction must occur under our direct supervision."

"However, burning alone isn't sufficient. We need a complete process:"

"First, inventory what's being destroyed and verify authorization. Second,
witness the destruction - multiple authorized personnel should observe.
Third, ensure complete destruction - verify nothing readable survives.
Fourth, document the destruction with witness signatures."

"The concept you're protecting against is called 'data remanence' - the
residual traces of information that survive insufficient destruction. For
critical secrets, we must ensure no remanence remains."

You have demonstrated understanding of DATA REMANENCE and secure destruction.
                """,
                "failure_texts": {
                    1: """
Chemical treatment may leave traces that can be recovered through forensic
techniques. Partially degraded inks, impressions in the parchment, or
incomplete treatment of all pages could allow reconstruction of sensitive
information. For the highest sensitivity data, complete physical destruction
is more reliable than chemical treatment.
                    """,
                    2: """
Transferring custody of sensitive materials to waste handlers introduces
unnecessary risk. The chain of custody breaks when materials leave direct
control. Even trusted handlers could be compromised, make errors, or face
their own disposal challenges. For highly sensitive materials, destruction
should occur under direct supervision of responsible parties.
                    """,
                    3: """
When destruction has been determined necessary due to risk, retention creates
ongoing liability. The decision to destroy was made because exposure risks
outweigh retention value. Keeping materials 'just in case' perpetuates that
risk indefinitely. Historical value must be weighed against operational
security during the retention decision, not used to reverse a destruction
decision.
                    """
                }
            },
            "corporate": {
                "title": "THE DECOMMISSIONED SERVERS",
                "narrative": """
IT is finally retiring the old file servers from the 2012 migration that
everyone forgot about. They've been sitting in a closet, unplugged but still
containing years of financial data, HR records, and what appears to be the
CEO's personal files from before he was CEO.

"These drives need to go," the IT Director announces. "We've got auditors
asking questions, and frankly, I'm scared of what's on them."

The junior admin suggests options:

"I can just delete everything and reformat. Quick and easy, then we sell
the hardware on eBay."

"We could use that disk wiping software - three passes should be enough.
Maybe we can reuse the drives in the test lab."

"Just put them in the e-waste bin. The recycling company handles disposal."

You've seen enough forensics presentations to know this matters. How do you
advise handling these drives containing highly sensitive data?
                """,
                "choices": [
                    {"text": "Physical destruction - degauss and shred the drives with a certified vendor"},
                    {"text": "Disk wiping software - DoD 5220.22-M standard should be sufficient"},
                    {"text": "E-waste recycling - the vendor is certified for secure disposal"},
                    {"text": "Keep them in storage - we might need that data for legal discovery someday"}
                ],
                "success_text": """
You save IT from a potentially career-ending mistake.

"For data this sensitive - financial records, HR data, executive files -
we need physical destruction. Here's why the other options fail:"

"Disk wiping? On modern drives with wear leveling and hidden sectors?
Forensic tools can recover data that 'passed' standard wiping procedures.
When you're talking C-suite personal files, 'probably wiped' isn't good
enough."

"E-waste vendor? We lose chain of custody the moment those drives leave
our building. I don't care how many certifications they have - we can't
verify destruction we don't witness."

"But destruction needs a process:"

"First, inventory the drives and verify authorization to destroy. Second,
use a certified destruction vendor who destroys ON-SITE while we watch.
Third, collect certificates of destruction for each drive serial number.
Fourth, keep destruction records for the audit trail."

"What we're preventing is called 'data remanence' - data that survives
deletion attempts. For sensitive data, assume it can be recovered unless
physically destroyed."

The IT Director exhales. "So no eBay side hustle then."

"Unless you want to be on the news. Use a shredder."

You've demonstrated DATA REMANENCE and secure destruction principles.
                """,
                "failure_texts": {
                    1: """
Disk wiping software is better than deletion, but for highly sensitive data?
Modern drives have wear leveling, bad sector remapping, and hidden areas that
wiping software can't always reach. Forensic recovery can sometimes retrieve
data that "passed" multiple wipe passes.

When you're dealing with executive personal files and HR records, "probably
destroyed" isn't good enough. Physical destruction eliminates the risk entirely.
                    """,
                    2: """
You just handed drives full of sensitive data to a third party and hoped for
the best. Sure, they're "certified" - but can you verify what actually happens
to those drives after they leave your building?

Chain of custody breaks the moment those drives leave your control. For the
most sensitive data, destruction should be witnessed. "Trust the vendor" isn't
a security control.
                    """,
                    3: """
So you're going to keep a ticking liability in a closet indefinitely because
you "might" need it?

Those drives are sitting there accumulating risk every day. They could be
stolen, accessed by curious employees, or subpoenaed in litigation you didn't
anticipate. If the decision was made to decommission, that means the data's
retention period is over.

"Might need it someday" isn't a retention policy. It's hoarding with legal
consequences.
                    """
                }
            }
        },
        "correct_index": 0,
        "xp_reward": 70,
        "hp_penalty": 25,
        "failure_text": """
Data remanence is residual data that survives after attempted deletion or
destruction. For highly sensitive materials:

Physical destruction methods:
- Burning (complete incineration)
- Shredding (cross-cut for highest sensitivity)
- Pulping/pulverizing
- Degaussing + physical destruction for magnetic media

Requirements for secure destruction:
1. Authorization verified before destruction
2. Chain of custody maintained until destruction
3. Witnessed destruction by authorized personnel
4. Verification that destruction is complete
5. Documentation of destruction process

Never trust intermediate handlers for the most sensitive materials.
        """,
        "domain_reference": "Domain 2: Asset Security - Data Remanence, Secure Destruction, Media Sanitization"
    },

    # Scenario 4: Retention Policies
    {
        "id": "d2_merchants_records",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE MERCHANT'S RECORDS",
                "narrative": """
The Archive Master reports a growing problem. The Citadel's storage vaults
are nearly full, and new records arrive daily. She presents a proposal to
the Council.

"We must purge old records to make room. I've identified thousands of
merchant transaction records over ten years old. Our policy says retain
for seven years, so these are past their required retention."

The Treasury representative objects: "Some of those transactions are still
being audited! The Royal Tax Assessors specifically requested records from
twelve years ago for their ongoing investigation."

The Legal Advisor adds: "And we have three active legal disputes involving
merchant transactions from eight to eleven years ago. Those records may
be needed as evidence."

The Archive Master sighs. "So our retention policy says seven years, but
various obligations say keep them longer. What actually governs here?"

How do you advise the Council?
                """,
                "choices": [
                    {"text": "Follow the seven-year policy strictly - policies exist for a reason"},
                    {"text": "Keep everything indefinitely - storage problems are easier to solve than legal problems"},
                    {"text": "Apply legal holds to affected records while disposing of records without active obligations"},
                    {"text": "Let each department decide what to keep from their own records"}
                ],
                "success_text": """
You help the Council understand retention complexity.

"The seven-year policy establishes our STANDARD retention period - what we
keep absent any special circumstances. But several factors can extend
retention beyond that standard:"

"Legal holds - when litigation is pending or reasonably anticipated, we must
preserve relevant records regardless of normal retention schedules. The
three active disputes create holds on those specific transaction records."

"Regulatory preservation - the Tax Assessors' audit creates an obligation
to preserve requested records until the audit concludes. Destroying them
could constitute obstruction."

"Business need - some records may have ongoing utility beyond minimum
retention requirements."

"The Archive Master should:"

"First, identify all records under legal hold or regulatory preservation -
these cannot be destroyed regardless of age. Second, verify remaining
records have no active business purpose or pending obligations. Third,
properly dispose of only those records truly past all retention requirements."

"We may also need to expand storage or move to more efficient formats. But
we cannot solve storage problems by destroying legally required records."

You have demonstrated understanding of RETENTION POLICIES AND LEGAL HOLDS.
                """,
                "failure_texts": {
                    0: """
Retention policies establish MINIMUM retention periods, not maximum. When
legal holds, ongoing litigation, or regulatory investigations exist, those
obligations override standard retention schedules. Destroying records under
legal hold could constitute obstruction of justice or spoliation of evidence,
resulting in severe penalties and adverse legal inferences.
                    """,
                    1: """
Indefinite retention creates its own risks: increased breach exposure,
higher storage costs, and potential privacy violations (some regulations
require disposal after purpose is fulfilled). The goal is not to keep
everything forever but to properly manage retention based on legitimate
needs. Records without business or legal purpose should eventually be
disposed of properly.
                    """,
                    3: """
Decentralized retention decisions lead to inconsistency and compliance gaps.
Individual departments may not be aware of all legal obligations, regulatory
requirements, or cross-functional needs for records. Retention management
requires central oversight with input from legal, compliance, and business
stakeholders to ensure all obligations are met.
                    """
                }
            },
            "corporate": {
                "title": "THE STORAGE QUOTA CRISIS",
                "narrative": """
The quarterly storage report lands on your desk with a big red warning:
"Enterprise archive at 94% capacity." The CFO is asking why storage costs
keep climbing when you're supposed to have a 7-year retention policy.

"I've identified 15 terabytes of customer transaction data older than seven
years," the Records Manager reports. "Per policy, we should be able to
delete it and free up space."

Legal immediately objects: "Hold on. We have ongoing litigation with three
customers involving transactions from 2015. Those records are under legal
hold."

Compliance adds: "The IRS is auditing our 2014-2016 tax filings. We can't
touch any records they might need until that closes."

The CFO is frustrated. "So our retention policy says seven years, but
apparently we can never delete anything? What's the point of having a
policy?"

The Records Manager looks at you. "What actually governs here? Policy or
all these exceptions?"

How do you advise?
                """,
                "choices": [
                    {"text": "Follow the seven-year policy strictly - policies exist for a reason"},
                    {"text": "Keep everything indefinitely - storage is cheap and legal problems are expensive"},
                    {"text": "Apply legal holds to affected records while disposing of records without active obligations"},
                    {"text": "Let each department decide what to keep from their own data"}
                ],
                "success_text": """
You help everyone understand retention isn't binary.

"The seven-year policy establishes our STANDARD retention period - the
default when nothing special is happening. But several factors can extend
retention beyond that:"

"Legal holds - when we're in litigation or reasonably expect to be, we must
preserve relevant records regardless of normal schedules. Those three
customer disputes? Legal hold. Touch nothing related to them."

"Regulatory preservation - the IRS audit creates an obligation to preserve
everything they might need. Destroying those records could be obstruction."

"But here's the key insight:"

"Not ALL 15 terabytes are under legal hold. Most of that data has no
litigation, no audit, no active business need. THOSE records can go."

"Here's the process: First, identify records under legal hold or regulatory
preservation - flag and protect those. Second, review remaining records
for any pending obligations. Third, dispose of everything that's truly past
all requirements."

"We're not keeping everything forever. We're not deleting everything blindly.
We're managing retention based on actual obligations."

The CFO nods. "So how much can we actually delete?"

"Let's find out. That's what proper records management looks like."

You've demonstrated RETENTION POLICIES AND LEGAL HOLDS.
                """,
                "failure_texts": {
                    0: """
You just instructed the team to delete records under active legal hold.
That's called "spoliation of evidence" and it's a really good way to lose
a lawsuit automatically.

When litigation is pending or reasonably anticipated, normal retention
schedules don't apply. Those records are frozen until the legal matter
concludes. "But our policy says..." doesn't protect you from sanctions
when a judge asks where the evidence went.

Retention policies establish minimums. Legal holds override everything.
                    """,
                    1: """
"Storage is cheap" is true until you have 500 terabytes of data you need
to search for e-discovery. Or until a breach exposes 20 years of customer
PII because you never deleted anything.

Infinite retention creates its own risks:
- More data to breach
- More data to search for legal requests
- Privacy regulations that REQUIRE deletion (GDPR, CCPA)
- Storage costs that compound annually

The goal isn't to keep everything. It's to keep what you need and properly
dispose of what you don't.
                    """,
                    3: """
So Marketing decides what marketing data to keep, Finance decides financial
records, and HR handles personnel files... independently?

What happens when Legal needs records for litigation that a department
already deleted? Or when Compliance needs data for an audit that nobody
thought to keep? Or when two departments have conflicting policies for the
same data?

Retention requires central coordination. Individual departments don't have
visibility into legal holds, regulatory requirements, or cross-functional
needs. Decentralized retention is how you fail audits.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 60,
        "hp_penalty": 20,
        "failure_text": """
Retention policy management:
- Standard retention periods establish minimums, not absolutes
- Legal holds override normal retention for litigation-relevant records
- Regulatory investigations create preservation obligations
- Disposition requires verification that no holds or needs exist

Key concepts:
- LEGAL HOLD: Preservation requirement for potential evidence
- SPOLIATION: Improper destruction of evidence (serious consequences)
- RETENTION SCHEDULE: Document specifying how long to keep record types

Never destroy records under legal hold.
        """,
        "domain_reference": "Domain 2: Asset Security - Retention Policies, Legal Holds, Records Management"
    },

    # Scenario 5: Privacy / Data Minimization
    {
        "id": "d2_census_scrolls",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE CENSUS SCROLLS",
                "narrative": """
The Royal Census Bureau requests access to Citadel records for the kingdom's
population survey. Their request includes:

"We need the following for all citizens who have interacted with the Citadel:
full names, birth dates, family relations, occupations, residences, income
records, health conditions, political affiliations, and religious practices."

The request is signed by the Census Director with proper authority seals.

The Keeper of Records hesitates. "We have most of this information, but...
the scope seems excessive. Do they really need health conditions and
religious practices for a population count?"

The Census representative explains: "Our research division wants to correlate
demographic factors. The more data, the better our analysis."

The Keeper looks to you. "They have legitimate authority to request records.
Must we provide everything they ask for?"

How do you advise the Keeper?
                """,
                "choices": [
                    {"text": "Provide everything requested - they have proper authority and seals"},
                    {"text": "Refuse entirely - sensitive data like religious practices should never be shared"},
                    {"text": "Provide only data necessary for the stated census purpose - negotiate scope based on data minimization"},
                    {"text": "Provide anonymized data - remove names but keep all other details"}
                ],
                "success_text": """
You advise a measured response that respects both authority and privacy.

"The Census Bureau has legitimate authority to collect population data, but
that authority doesn't extend to unlimited data collection. We must apply
the principle of DATA MINIMIZATION - sharing only what is necessary for the
stated purpose."

"For a population count and basic demographic survey, the Bureau needs:
names, birth dates, residences, and perhaps occupations. These directly
serve the census purpose."

"However, health conditions, religious practices, and political affiliations
are not necessary for counting population or basic demographics. These are
sensitive categories that require additional justification."

"Our response should be: 'We will gladly support the census with data
necessary for its stated purpose. Please clarify the specific need for
health and religious data, as these fall outside typical census scope.'"

"If they can demonstrate legitimate, proportionate need with appropriate
safeguards, we can discuss further. If it's simply 'nice to have for
research,' that doesn't justify the privacy intrusion."

The Keeper nods. "So authority to collect doesn't mean authority to collect
everything."

"Exactly. Purpose limitation and data minimization protect citizens even
from well-intentioned over-collection."

You have demonstrated understanding of DATA MINIMIZATION principles.
                """,
                "failure_texts": {
                    0: """
Authority to request data doesn't mean all data requested is appropriate.
The principle of data minimization requires providing only what is necessary
for the stated purpose. A population census doesn't require health conditions,
religious practices, or political affiliations. Providing excessive data
increases privacy risk for citizens and may violate their rights.
                    """,
                    1: """
Complete refusal isn't warranted for a legitimate census request. The Census
Bureau may have valid need for some demographic data. The issue isn't sharing
any data, but sharing MORE data than necessary. Proper response is to
negotiate scope down to necessary elements, not to refuse legitimate
government functions entirely.
                    """,
                    3: """
Anonymization alone may be insufficient. With enough data points (birth date,
occupation, residence, family relations), individuals can often be re-identified
even without names. True privacy protection requires both limiting data shared
AND ensuring remaining data doesn't allow re-identification. Data minimization
addresses the first concern; anonymization addresses the second, but both may
be needed.
                    """
                }
            },
            "corporate": {
                "title": "THE MARKETING DATA REQUEST",
                "narrative": """
Marketing sends over a data request for the "Customer 360 Initiative." They
want to build comprehensive customer profiles for "personalized experiences."

Their request includes: names, email addresses, phone numbers, purchase
history, browsing behavior, social media profiles, estimated income levels,
family composition, health insurance status, and political donation history.

"We want to really understand our customers," the Marketing VP explains.
"The more data points, the better our targeting. Our analytics vendor says
they can correlate all of this into actionable insights."

The Data Governance lead looks uncomfortable. "We have most of this data
across various systems, but... health insurance status? Political donations?
For a retail company?"

Marketing shrugs. "Our vendor can acquire that data and match it to our
customers. They just need the identifiers."

The request lands on your desk for approval. Marketing has legitimate
business purposes, and the CMO has signed off. Do you provide the data?

How do you advise?
                """,
                "choices": [
                    {"text": "Provide everything requested - Marketing has executive approval"},
                    {"text": "Refuse entirely - this feels like a privacy violation waiting to happen"},
                    {"text": "Provide only data necessary for the stated marketing purpose - negotiate scope based on data minimization"},
                    {"text": "Provide all data but anonymize customer names"}
                ],
                "success_text": """
You push back diplomatically but firmly.

"Marketing has legitimate business purposes, but that doesn't mean they
can collect unlimited data. We need to apply DATA MINIMIZATION - provide
only what's necessary for the stated purpose."

"For personalized marketing, they reasonably need: names, contact info,
purchase history, and maybe browsing behavior on our own sites. These
directly serve marketing purposes."

"But health insurance status? Political donations? These are sensitive
categories with no reasonable connection to retail marketing. If that data
leaked, we'd be explaining to regulators why we even had it."

"Our response: 'We'll support the initiative with data appropriate for
marketing purposes. Please justify the business need for health and political
data, including how you'll protect it and what regulations apply.'"

"'More data is better' isn't a valid justification. Neither is 'our vendor
can get it.' If we can't articulate why we NEED specific data, we shouldn't
collect it."

The Data Governance lead nods. "So executive approval doesn't override
privacy principles?"

"Approval doesn't make inappropriate data collection appropriate. It just
means someone signed without thinking it through."

You've demonstrated DATA MINIMIZATION principles.
                """,
                "failure_texts": {
                    0: """
Executive approval doesn't override privacy regulations or common sense.
You just greenlit collecting political donation history and health insurance
status for a retail marketing campaign.

When this inevitably leaks - or when a regulator asks why you're hoarding
sensitive data unrelated to your business - "Marketing wanted it" won't be
a valid defense. The CMO's signature doesn't protect you from CCPA, GDPR,
or FTC enforcement.

Data minimization means collecting only what's necessary. "We might use it
for targeting" isn't necessity.
                    """,
                    1: """
Complete refusal throws out legitimate needs with problematic ones. Marketing
DOES have valid reasons for some customer data - purchase history, contact
preferences, browsing behavior on your own site.

The issue isn't that Marketing wants data. It's that they want MORE data
than necessary. The right response is to negotiate scope, not slam the door.
You've just made Data Governance look like obstructionists rather than
partners.
                    """,
                    3: """
You anonymized names but kept... political donations and health insurance
status? Along with email addresses, phone numbers, and detailed purchase
history?

That's not anonymous. With that many data points, re-identification is
trivial. Anyone who knows "customer X bought Y products and has email
Z" can match them back. You've given Marketing the illusion of privacy
protection while providing none.

Data minimization means limiting WHAT you share, not just removing one
field and calling it anonymous.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 65,
        "hp_penalty": 20,
        "failure_text": """
Data minimization principles:
- Collect only data necessary for the stated purpose
- Purpose limitation - data collected for one purpose shouldn't be used for another
- Authority to collect doesn't equal authority to collect everything
- Sensitive categories (health, religion, politics) require additional justification

Privacy protection requires:
1. Question whether all requested data is truly necessary
2. Negotiate scope to minimum needed
3. Apply additional protections for sensitive categories
4. Document the purpose limitation for shared data
        """,
        "domain_reference": "Domain 2: Asset Security - Privacy, Data Minimization, Purpose Limitation"
    },

    # Scenario 6: Data Lifecycle Management
    {
        "id": "d2_inherited_archive",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE INHERITED ARCHIVE",
                "narrative": """
The Citadel has absorbed the archives of a smaller fortress that was
decommissioned. Hundreds of crates arrive containing records, artifacts,
and materials accumulated over decades under different management.

The Archive Master surveys the chaos. "We have no idea what's in here.
Different classification systems, unknown retention requirements, unclear
ownership. Some boxes haven't been opened in twenty years. Where do we
even begin?"

Various suggestions emerge:

"Just integrate it with our current archives by date," suggests one archivist.

"Store it separately and deal with it later," offers another.

"Sample a few boxes to get a sense of what's there," proposes a third.

The Archive Master seeks your guidance on handling this significant but
chaotic acquisition.

How do you advise approaching this inherited archive?
                """,
                "choices": [
                    {"text": "Integrate by date - it will eventually get reviewed as part of normal operations"},
                    {"text": "Conduct systematic lifecycle review - assess, classify, determine retention, then integrate or dispose appropriately"},
                    {"text": "Separate storage - keep it isolated until resources allow proper review"},
                    {"text": "Sample review - assess a random selection to estimate what's there"}
                ],
                "success_text": """
You outline a comprehensive approach to the archive challenge.

"This is a data lifecycle management challenge. Every item in that archive
is somewhere in its lifecycle, but we don't know where. We must assess
before we can properly manage."

"Here's the process:"

"First, SECURE the entire archive with appropriate access controls until
assessment is complete. Unknown materials get cautious treatment."

"Second, INVENTORY everything systematically. Document what exists before
deciding what to do with it."

"Third, CLASSIFY each item under our current system. Apply appropriate
markings based on content, not on what previous systems may have assigned."

"Fourth, DETERMINE RETENTION requirements. Some items may be past retention,
others under ongoing obligations. This requires research into the original
fortress's legal and regulatory context."

"Fifth, PROCESS appropriately: integrate properly classified materials into
our archives, dispose of materials past retention with no ongoing need,
and flag anything requiring special handling."

"This is resource-intensive, but there's no shortcut. You cannot properly
protect assets you haven't properly assessed."

The Archive Master sighs but agrees. "Better to do it right than to inherit
problems we don't understand."

You have demonstrated understanding of DATA LIFECYCLE MANAGEMENT.
                """,
                "failure_texts": {
                    0: """
Integration without assessment is dangerous. Materials of unknown classification
could end up in inappropriate locations. Sensitive documents might be stored
with general records. Toxic materials (literal or metaphorical) could
contaminate the main archive. Assessment must precede integration to ensure
proper handling.
                    """,
                    2: """
Indefinite deferral creates growing liability. The archive remains in limbo -
potentially containing sensitive materials in inadequate storage, subject to
deterioration, and without proper controls. 'Later' often becomes 'never.'
Resources must be allocated for proper processing, not just segregation.
                    """,
                    3: """
Sampling can provide initial insight but cannot replace comprehensive review
for security-critical materials. A sample might miss the most sensitive
documents, legal holds, or valuable assets. It's a reasonable first step
for planning, but the full archive must eventually be systematically
processed.
                    """
                }
            },
            "corporate": {
                "title": "THE ACQUISITION DATA DUMP",
                "narrative": """
Your company just acquired a smaller competitor. Along with the IP and
customer base comes... their data. All of it. Terabytes of files dumped
onto a NAS that someone wheeled into your data center.

"We have no idea what's in here," the Integration PM admits. "Different
file structures, no consistent naming conventions, unclear data owners.
Some of these folders haven't been accessed since 2016. Legal is asking
about retention, Security is asking about classification, and I'm asking
for a raise."

The team offers suggestions:

"Just merge it into our shared drives by department," suggests the admin.

"Put it in cold storage until someone needs something," offers IT.

"Let's sample some folders to see what we're dealing with," proposes an
analyst.

The CIO wants a plan by Friday. How do you advise handling this data
inheritance?
                """,
                "choices": [
                    {"text": "Merge by department - users will sort it out as they find things they need"},
                    {"text": "Conduct systematic data lifecycle review - inventory, classify, determine retention, then integrate or dispose appropriately"},
                    {"text": "Cold storage - park it until someone asks for something specific"},
                    {"text": "Sample assessment - review a random selection to estimate the scope"}
                ],
                "success_text": """
You lay out the only approach that won't create a compliance nightmare.

"This is a data lifecycle management problem. Every file in that dump is
somewhere in its lifecycle - we just don't know where. We have to assess
before we can manage."

"Here's the framework:"

"First, SECURE the whole thing. Unknown data gets treated as sensitive until
proven otherwise. Lock down access to the assessment team only."

"Second, INVENTORY systematically. Before we decide what to do, we document
what exists. File types, sizes, apparent owners, last access dates."

"Third, CLASSIFY under our standards. Their 'Confidential' might be our
'Internal.' Their 'Public' might contain PII. We can't inherit their
classification scheme."

"Fourth, DETERMINE RETENTION. Their contracts, their legal obligations,
their regulatory context. Some of this might be past retention. Some might
be under legal hold we don't know about."

"Fifth, PROCESS appropriately. Integrate what belongs with us, dispose of
what's past retention, and escalate anything weird."

"Yes, this is expensive. Yes, it takes time. But you know what's more
expensive? Discovering PII three years from now during a breach
investigation."

The PM sighs. "So no quick fixes."

"The quick fix is how you get fined. Ask me how I know."

You've demonstrated DATA LIFECYCLE MANAGEMENT.
                """,
                "failure_texts": {
                    0: """
You just merged unclassified, unassessed data into production systems.
What could go wrong?

How about: PII mixed into general shares, malware that survived the
migration, files under legal hold that someone deletes, confidential
data visible to wrong departments.

Integration without assessment is how you contaminate your clean systems
with someone else's mess. Their data governance problems are now yours,
except you don't even know what they are yet.
                    """,
                    2: """
Ah, the "shove it in a closet and forget about it" strategy. Classic.

That data is now sitting in cold storage, accumulating liability. What if
there's PII in there degrading without proper controls? What if there are
legal holds you're unknowingly violating? What if there's IP you're
obligated to protect?

"Nobody's asking for it" doesn't mean "nobody will ever ask." And when
they do - auditors, regulators, plaintiffs' attorneys - "we don't know
what's in there" isn't an answer.
                    """,
                    3: """
Sampling is a reasonable FIRST STEP for planning, but you're presenting
it as the solution. A 5% sample tells you roughly what you're dealing
with - great for budgeting the assessment project.

But what it doesn't tell you: where the legal holds are, which specific
files contain PII, what's past retention. You might sample nothing sensitive
while boxes of SSNs sit unexamined. Statistical inference doesn't work
for compliance; you need comprehensive review.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Data lifecycle management covers:
1. CREATION - how data is generated and initially classified
2. STORAGE - how data is maintained and protected
3. USE - how data is accessed and processed
4. SHARING - how data is transferred to others
5. ARCHIVAL - how data is preserved for long-term retention
6. DESTRUCTION - how data is properly disposed when no longer needed

When inheriting unknown archives:
- Secure before assessing
- Inventory completely
- Classify under current standards
- Determine retention obligations
- Process systematically

No shortcuts for asset assessment.
        """,
        "domain_reference": "Domain 2: Asset Security - Data Lifecycle, Asset Inventory, Classification"
    },

    # Scenario 7: Asset Inventory Management
    {
        "id": "d2_royal_inventory",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE ROYAL INVENTORY",
                "narrative": """
The annual asset review reveals disturbing discrepancies. Three enchanted
communication crystals are missing from the inventory. Additionally, the
Cipher Chamber contains two encryption devices that don't appear in any
records.

"How can we have both missing items AND unrecorded items?" the Steward
demands. "Our inventory is supposed to be complete and accurate!"

The Investigation reveals several issues: assets transferred between
departments without updating records, new items procured without proper
registration, old items disposed without documentation, and borrowed items
never returned.

"Our processes have failed," the Steward admits. "But fixing this after
the fact seems impossible. The problems have accumulated over years."

How do you advise addressing this asset inventory crisis?
                """,
                "choices": [
                    {"text": "Focus on finding the missing crystals - they're the immediate security concern"},
                    {"text": "Conduct complete physical inventory, reconcile with records, and implement proper asset management processes"},
                    {"text": "Start fresh - write off discrepancies and implement better processes going forward"},
                    {"text": "Implement stricter controls immediately - prevent future problems rather than investigating past ones"}
                ],
                "success_text": """
You outline a comprehensive remediation approach.

"This requires three parallel efforts: immediate response to the missing
crystals, baseline reconciliation of all assets, and process improvement
to prevent recurrence."

"For the crystals: Conduct focused investigation - last known location,
access logs, personnel with handling authority. These are security-sensitive
items requiring urgent attention."

"For the baseline: Complete physical inventory of all assets. Every room,
every container. Then reconcile against records. Items found but not recorded
get added. Items recorded but not found get investigated."

"For process improvement, we need:"
"- Mandatory registration before any asset enters service"
"- Transfer documentation for any movement between custody"
"- Periodic physical verification against records"
"- Clear accountability - every asset has an assigned custodian"
"- Documented disposal for items leaving service"

"The Cipher Chamber's unrecorded devices are almost as concerning as the
missing crystals. How did encryption equipment enter service without
registration? That's a control failure too."

"We cannot protect assets we don't know we have."

The Steward approves the comprehensive approach. "This will be painful, but
necessary."

You have demonstrated understanding of ASSET INVENTORY MANAGEMENT.
                """,
                "failure_texts": {
                    0: """
Finding specific missing items addresses only a symptom, not the underlying
disease. Even if the crystals are located, the systemic failures that caused
items to go missing will continue. Tomorrow's missing items might be more
critical. Root cause remediation must accompany specific item recovery.
                    """,
                    2: """
Writing off discrepancies means accepting that sensitive assets may be
unaccounted for indefinitely. The missing crystals could be in wrong hands,
lost, stolen, or simply misplaced. Security requires knowing what happened
to controlled items. Starting fresh without reconciliation leaves dangerous
uncertainties.
                    """,
                    3: """
New controls on a foundation of incorrect records will perpetuate problems.
You'll be controlling based on inaccurate information. Additionally, without
understanding how problems occurred, new controls may not address actual
failure modes. Assessment of current state must precede process improvement.
                    """
                }
            },
            "corporate": {
                "title": "THE IT ASSET AUDIT",
                "narrative": """
The annual IT asset audit just came back, and it's a disaster. Three
company laptops with full-disk encryption are missing. Meanwhile, the server
room contains two network switches that don't appear in any inventory
system.

"How do we have missing laptops AND mystery hardware?" the IT Director
asks, head in hands. "This is a compliance nightmare."

The investigation reveals a familiar story: laptops transferred between
employees without updating the asset database, hardware purchased on
departmental credit cards without going through IT procurement, old
equipment disposed of during office moves without documentation, and
"temporary" loaners that became permanent.

"Our CMDB is fiction," the asset manager admits. "And these problems go
back years. I don't even know where to start."

How do you advise addressing this asset management crisis?
                """,
                "choices": [
                    {"text": "Focus on finding the missing laptops - they're the immediate security concern"},
                    {"text": "Conduct complete physical inventory, reconcile with records, and implement proper asset management processes"},
                    {"text": "Start fresh - write off discrepancies and implement better tracking going forward"},
                    {"text": "Implement stricter procurement controls immediately - prevent future shadow IT"}
                ],
                "success_text": """
You lay out the remediation plan nobody wants but everybody needs.

"This requires three parallel efforts: immediate response to the missing
laptops, baseline reconciliation of all assets, and process improvement
to prevent recurrence."

"For the laptops: Security incident investigation. Last known users, last
network connections, BitLocker recovery key status. These contain company
data and need urgent attention."

"For the baseline: Complete physical inventory. Every closet, every desk,
every server rack. Then reconcile against the CMDB. Hardware found but not
recorded gets added with a 'discovered' flag. Records without matching
hardware get investigated."

"For process improvement:"
"- Mandatory registration before any asset enters service"
"- Asset tags that survive redeployment"
"- Transfer documentation for custody changes"
"- Annual physical verification"
"- Clear custodian assignment for every device"
"- Procurement controls that close the shadow IT loophole"

"Those mystery switches in the server room? Almost as concerning as the
missing laptops. Unknown hardware on your network is a security gap."

"You can't protect assets you don't know you have. You can't track assets
you've never recorded."

The IT Director sighs. "This is going to be a lot of work."

"Less work than explaining to auditors why you lost three laptops."

You've demonstrated ASSET INVENTORY MANAGEMENT.
                """,
                "failure_texts": {
                    0: """
Finding the missing laptops is urgent, yes. But you're treating the symptom,
not the disease.

Even if you find all three laptops, the broken processes that lost them
are still broken. Next quarter you'll lose different laptops. And the
mystery switches? Still mystery switches.

Security incident response is necessary but not sufficient. You need
process remediation alongside the investigation.
                    """,
                    2: """
"Let's just write it off and start fresh" sounds reasonable until you
realize what you're writing off.

Those three missing laptops? They contain company data. They might be in
someone's basement. They might be on eBay. They might be in a competitor's
hands. "We don't know where they are but we've updated our spreadsheet"
isn't a security posture.

You can't start fresh on asset management without accounting for existing
assets. Reconciliation must precede process improvement.
                    """,
                    3: """
Stricter procurement controls are great for preventing future problems.
They do nothing about your current mess.

You've got missing laptops that might be anywhere. You've got mystery
hardware on your network that nobody ordered. Your CMDB is fiction. New
policies don't fix any of that.

Before you can control assets going forward, you need to know what assets
you actually have. Assessment first, then controls.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 65,
        "hp_penalty": 20,
        "failure_text": """
Asset inventory management requires:
- Complete inventory - know everything you have
- Accurate records - records match physical reality
- Accountability - every asset has a responsible custodian
- Lifecycle tracking - registration, transfer, disposal documented
- Periodic verification - physical counts reconciled to records

When discrepancies are discovered:
1. Investigate security-sensitive items immediately
2. Conduct complete physical inventory
3. Reconcile against records
4. Investigate all discrepancies
5. Implement process improvements

You cannot protect what you don't know you have.
        """,
        "domain_reference": "Domain 2: Asset Security - Asset Inventory, Asset Tracking, Accountability"
    },

    # Scenario 8: Data in Transit
    {
        "id": "d2_traveling_diplomat",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE TRAVELING DIPLOMAT",
                "narrative": """
Ambassador Krynn must travel to a hostile kingdom for critical negotiations.
She needs to carry sensitive diplomatic documents - treaty proposals,
intelligence assessments, and negotiation boundaries.

"The journey takes me through territories where our enemies have spies,"
she explains. "My baggage may be searched, my camp may be observed, and
I cannot guarantee my quarters won't be infiltrated. How do I protect
these documents during transit?"

Her security advisor suggests several approaches:

"Commit the key points to memory and destroy the documents," offers one.

"Conceal them in hidden compartments," suggests another.

"Send them ahead via separate courier so you're not carrying them," proposes
a third.

"Use our strongest encryption on the documents," recommends a fourth.

The Ambassador seeks your counsel on protecting data in transit through
hostile territory.

How do you advise?
                """,
                "choices": [
                    {"text": "Memorize and destroy - what doesn't exist can't be captured"},
                    {"text": "Physical concealment - well-hidden documents are unlikely to be found"},
                    {"text": "Separate courier - the documents arrive independently of the Ambassador"},
                    {"text": "Strong encryption with physical protection - encrypted documents resistant to search or capture"}
                ],
                "success_text": """
You recommend a layered approach to protecting data in transit.

"Encryption transforms your documents from readable intelligence into
meaningless patterns without the proper key. Even if documents are captured,
their content remains protected."

"Here's a comprehensive approach:"

"First, encrypt all sensitive documents using our strongest ciphers. The
encryption key should be memorized - not written - and ideally split
between you and a trusted companion."

"Second, maintain physical security as an additional layer. Encrypted
documents in secure containers, under personal supervision. Encryption
protects confidentiality; physical control protects availability."

"Third, prepare for coercion scenarios. Consider whether carrying a
secondary set of plausible but less sensitive documents might satisfy
searchers without revealing the existence of encrypted materials."

"Fourth, establish secure key destruction procedures. If capture becomes
imminent, you can destroy the key while keeping the documents. Without the
key, the encrypted documents become permanently inaccessible."

"Encryption is your primary defense. Physical measures provide backup.
Memory alone is insufficient for detailed negotiations."

You have demonstrated understanding of DATA IN TRANSIT protection.
                """,
                "failure_texts": {
                    0: """
Human memory is unreliable for detailed treaty provisions, specific numbers,
and complex negotiation boundaries. Critical details could be forgotten or
misremembered, potentially undermining the entire diplomatic mission.
Additionally, under duress (torture, coercion), even memorized information
might be extracted. Complete elimination is rarely practical for detailed
negotiations.
                    """,
                    1: """
Relying solely on concealment is dangerous. Professional searches may find
hidden compartments. Discovery of concealed documents could be more damaging
than open possession - it suggests secret content worth hiding. Concealment
provides only security through obscurity, which fails when obscurity is
compromised.
                    """,
                    2: """
Transferring custody to a courier introduces additional risk. The courier
could be compromised, intercepted, or lose the documents. The Ambassador
loses control of timing and confirmation of receipt. If the courier fails,
the Ambassador arrives without necessary materials. This approach introduces
risks while not eliminating them.
                    """
                }
            },
            "corporate": {
                "title": "THE EXECUTIVE TRAVEL RISK",
                "narrative": """
The CEO is traveling to China for acquisition negotiations. She needs to
bring confidential deal documents - financial models, valuation analyses,
negotiation parameters, and competitive intelligence.

"I'll be going through airports with mandatory device inspections," she
explains. "My hotel room might be searched. The local network is definitely
monitored. How do I protect this information?"

IT Security proposes several options:

"Memorize the key numbers and don't bring any documents," suggests one.

"Use a hidden partition on your laptop that won't show up in casual
inspection," offers another.

"We'll send a separate courier with a briefcase of physical documents,"
proposes a third.

"Full device encryption with a travel-specific laptop that can be wiped
remotely," recommends the CISO.

How do you advise protecting data in transit through hostile territory?
                """,
                "choices": [
                    {"text": "Memorize key figures - if there's no data to capture, there's no risk"},
                    {"text": "Hidden partition - a casual border inspection won't find it"},
                    {"text": "Separate courier - documents arrive independently of the executive"},
                    {"text": "Strong encryption with travel laptop - data protected even if device is seized"}
                ],
                "success_text": """
You recommend the defense-in-depth approach.

"Full-device encryption means even if the laptop is seized and imaged, they
get encrypted noise without the key. Here's the comprehensive approach:"

"First, travel laptop only. No connection to corporate network, no email
history, no browser cache. Only the specific documents needed, fully
encrypted."

"Second, remote wipe capability. If the device is seized or compromised,
we can destroy the data remotely. Set up a check-in schedule - missed
check-in triggers automatic wipe."

"Third, key management. The decryption passphrase should be long and
memorized - not written anywhere. Consider split knowledge where a
colleague back home has part of the key for emergency access."

"Fourth, network hygiene. VPN for all connections. Assume the hotel WiFi
is hostile. No accessing sensitive systems from in-country."

"Fifth, plausible deniability files. Some visible, innocuous business
documents that look legitimate under inspection without revealing
sensitive data exists."

"Encryption is your primary defense. Everything else is backup. And yes,
this means she needs security training before travel."

The CEO nods. "So we assume everything gets searched and plan accordingly."

"Welcome to international data security."

You've demonstrated DATA IN TRANSIT protection.
                """,
                "failure_texts": {
                    0: """
You're asking the CEO to memorize a 47-page financial model with specific
valuation multiples, earnout structures, and deal terms? Good luck with that.

Human memory is unreliable for detailed business information. Miss one number
in negotiations and the deal structure changes. Forget a key term and you've
undermined your position.

Also, under pressure - whether legal threats or just stress - people
misremember details. You can't negotiate a billion-dollar deal from memory.
                    """,
                    1: """
"Security through obscurity" is not security. Hidden partitions get found
by forensic tools that border agents definitely have access to.

Worse: if they find a hidden partition, you've just demonstrated intent to
deceive. Now you have legal problems on top of security problems. In some
countries, refusing to decrypt on demand carries serious penalties.

Concealment fails when concealment is detected. Real protection is
encryption that protects data even when discovered.
                    """,
                    2: """
Now you've introduced a third party into your chain of custody. What's the
courier's security clearance? How are they traveling? What happens if
they're detained at customs?

The documents could be copied, lost, or delayed. The CEO arrives at
negotiations with nothing. And you've created a conspicuous separate
delivery of materials that screams "something important is here."

Don't transfer custody of sensitive materials when you don't have to.
                    """
                }
            }
        },
        "correct_index": 3,
        "xp_reward": 65,
        "hp_penalty": 20,
        "failure_text": """
Protecting data in transit requires:
- ENCRYPTION: Primary protection for confidentiality
- PHYSICAL SECURITY: Backup protection and availability
- KEY MANAGEMENT: Keys protected separately from encrypted data
- INTEGRITY VERIFICATION: Ability to detect tampering

Avoid:
- Memory alone (unreliable for detailed information)
- Concealment alone (fails when discovered)
- Custody transfer (introduces additional risk)

Layered defenses provide resilience when any single control fails.
        """,
        "domain_reference": "Domain 2: Asset Security - Data in Transit, Encryption, Transport Security"
    },

    # Scenario 9: Cloud Data Security
    {
        "id": "d2_cloud_vault",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE CLOUD VAULT",
                "narrative": """
The Citadel's leadership considers an innovative proposal: storing backup
archives with the Skykeep Consortium, who maintains magical vaults in the
clouds accessible from anywhere in the realm.

"Think of the benefits," argues the Innovation Advocate. "Our archives
would survive even if the Citadel itself fell. Access from any of our
outposts. No more maintaining our own vault infrastructure."

The Security Council raises concerns:

"Their vault masters would have access to our secrets," worries one member.

"How would we ensure our data isn't mixed with other clients'?" asks another.

"What happens if the Consortium fails or is compromised?" questions a third.

The Keeper of Secrets asks: "Can we benefit from their services while
maintaining appropriate security? Or is this fundamentally incompatible
with our requirements?"

How do you advise on this cloud storage proposal?
                """,
                "choices": [
                    {"text": "Reject cloud storage entirely - sensitive data must remain under direct physical control"},
                    {"text": "Encrypt data before upload, verify Consortium security practices, establish contractual protections, and maintain local backups"},
                    {"text": "Accept the proposal - the Consortium's reputation speaks for itself"},
                    {"text": "Use cloud storage only for non-sensitive data - keep important archives local"}
                ],
                "success_text": """
You advocate for managed cloud adoption with appropriate controls.

"Cloud storage can provide genuine benefits - resilience, accessibility,
reduced infrastructure burden. But we must manage the associated risks
rather than simply accepting them."

"Here's the approach:"

"First, ENCRYPT BEFORE UPLOADING. We control the encryption keys, not the
Consortium. Even their vault masters cannot read what they cannot decrypt.
This addresses the access concern."

"Second, VERIFY THEIR PRACTICES. We need due diligence on their security
controls, isolation between clients, incident response capabilities, and
regulatory compliance. Trust but verify."

"Third, ESTABLISH CONTRACTUAL PROTECTIONS. Data handling requirements,
breach notification obligations, audit rights, and termination provisions
that ensure data return or destruction."

"Fourth, MAINTAIN LOCAL BACKUPS for critical archives. The cloud provides
additional protection, not replacement for primary controls. If the
Consortium fails, we need our own copies."

"Finally, CLASSIFY what goes to cloud storage. Not everything needs the
same level of protection. Some archives may be appropriate for cloud
storage while others remain local only."

"With these controls, cloud storage becomes a managed risk rather than an
uncontrolled one."

You have demonstrated understanding of CLOUD DATA SECURITY.
                """,
                "failure_texts": {
                    0: """
Automatic rejection of external storage ignores its legitimate benefits and
the possibility of managing associated risks. Many organizations successfully
use cloud storage for sensitive data with appropriate controls. The question
isn't 'cloud or no cloud' but 'how do we secure cloud storage appropriately?'
Risk management, not risk avoidance, should guide the decision.
                    """,
                    2: """
Reputation doesn't guarantee security or appropriate controls for our specific
requirements. Different organizations have different risk tolerances and
requirements. What's adequate for other clients may be insufficient for our
most sensitive archives. Due diligence must verify specific capabilities and
controls before entrusting data to any provider.
                    """,
                    3: """
While tiering by sensitivity is reasonable, this approach foregoes the primary
benefit - disaster recovery for critical archives. If we only store unimportant
data externally, external storage provides limited value. The better approach
is to enable secure external storage of sensitive data through appropriate
controls.
                    """
                }
            },
            "corporate": {
                "title": "THE AWS MIGRATION DEBATE",
                "narrative": """
The CIO proposes migrating backup infrastructure to AWS. "Think of the
benefits," he argues. "Geo-redundancy, instant scalability, no more
maintaining our own disaster recovery site. Plus the CapEx to OpEx shift
makes the CFO happy."

Security has concerns:

"Amazon's employees could access our data," worries the CISO.

"How do we know our data isn't accidentally visible to other tenants?"
asks the compliance officer.

"What if AWS has an outage? Or gets subpoenaed? Or raises prices 10x?"
questions the risk manager.

The CIO is frustrated. "Everyone uses AWS. Are we saying we're smarter
than Netflix and Goldman Sachs about cloud security?"

The steering committee looks to you. Can cloud storage work for sensitive
corporate data, or is this fundamentally incompatible with your security
requirements?

How do you advise?
                """,
                "choices": [
                    {"text": "Reject cloud storage - our data is too sensitive for third-party infrastructure"},
                    {"text": "Encrypt data before upload, verify AWS security controls, establish contractual protections, and maintain on-prem backups"},
                    {"text": "Accept the proposal - AWS security is better than anything we could build"},
                    {"text": "Use cloud only for non-sensitive data - keep customer PII on-premises"}
                ],
                "success_text": """
You thread the needle between cloud enthusiasm and cloud paranoia.

"Cloud can work for us, but we need to manage the risk rather than just
accept it. Here's the framework:"

"First, ENCRYPT BEFORE UPLOADING. Customer-managed keys, not AWS-managed.
We control the encryption; they store the ciphertext. Even with full system
access, AWS sees noise without our keys."

"Second, DUE DILIGENCE. AWS has SOC 2 reports, compliance certifications,
and shared responsibility documentation. Read them. Understand what they
protect and what's still on us. 'Secure by default' doesn't mean 'secure
no matter what you do.'"

"Third, CONTRACTUAL PROTECTIONS. The Business Associate Agreement for HIPAA,
the Data Processing Agreement for GDPR, the standard SLA terms. Negotiate
breach notification timelines and audit rights where possible."

"Fourth, MAINTAIN ON-PREM BACKUPS. Cloud is additional protection, not
replacement. If AWS has a catastrophic failure - or more likely, if we
misconfigure something and delete our own data - we need recovery capability."

"Fifth, CLASSIFY. Not everything needs the same protection. Tier your data
and match cloud security controls to sensitivity."

The CIO nods. "So we're not saying no to cloud..."

"We're saying yes to cloud, correctly. The shared responsibility model
means AWS does their part, but we still have to do ours."

You've demonstrated CLOUD DATA SECURITY principles.
                """,
                "failure_texts": {
                    0: """
Blanket rejection of cloud storage ignores the reality that most
organizations - including competitors handling similar data - successfully
use cloud with appropriate controls.

The question isn't "cloud or not cloud" but "how do we secure cloud
appropriately?" Risk management means managing risk, not avoiding all risk.
Your on-premises data center isn't zero-risk either.

You just told the CIO "no" without offering a viable alternative.
                    """,
                    2: """
"AWS security is better than ours" might be true for physical data center
security, but that's not the whole picture.

AWS secures their infrastructure. They don't secure your configuration,
your access controls, your encryption key management, or your data
classification. That's the shared responsibility model.

Companies get breached on AWS all the time - not because AWS failed, but
because they misconfigured S3 buckets, left credentials in code, or
granted overly permissive IAM roles. AWS security doesn't protect against
customer mistakes.
                    """,
                    3: """
So your disaster recovery strategy only covers non-sensitive data?
What happens when your on-prem data center floods and you lose customer
PII? Where's the recovery?

The whole point of cloud backup is protecting your most critical data.
If you only store data you don't care about, you haven't solved the
disaster recovery problem - you've just added cloud costs.

The right answer is to enable secure cloud storage of sensitive data
through encryption and proper controls, not to exclude sensitive data
entirely.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 70,
        "hp_penalty": 20,
        "failure_text": """
Cloud data security requirements:
- ENCRYPTION: Encrypt before upload, control your own keys
- DUE DILIGENCE: Verify provider security practices and controls
- CONTRACTS: Data handling, breach notification, audit rights
- BACKUP STRATEGY: Cloud supplements, doesn't replace local copies
- DATA CLASSIFICATION: Match protection to sensitivity

Key questions for cloud providers:
- How is data isolated between clients?
- Who can access stored data?
- Where is data physically located?
- What happens at contract termination?

Cloud storage can be secure with appropriate controls.
        """,
        "domain_reference": "Domain 2: Asset Security - Cloud Security, Data Protection, Third-Party Management"
    },

    # Scenario 10: Media Sanitization
    {
        "id": "d2_abandoned_outpost",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE ABANDONED OUTPOST",
                "narrative": """
Strategic retreat from the Northern Outpost has been ordered. The garrison
has three days to evacuate before enemy forces arrive. The outpost contains
significant record-keeping materials: wax tablets, parchment files, and
several enchanted memory stones that stored sensitive communications.

The Quartermaster must decide how to handle these materials. Full evacuation
of all records is impossible - there's not enough transport capacity.

"What we cannot take, we must ensure the enemy cannot use," the Commander
orders.

The Quartermaster presents options: "We can burn the paper records easily
enough. The wax tablets can be melted. But the memory stones... they're
resilient. Simply smashing them doesn't guarantee the memories are truly
gone. And we have no mages with proper erasure spells available."

How do you advise handling media sanitization under these time constraints?
                """,
                "choices": [
                    {"text": "Prioritize evacuation of most sensitive items, destroy what can be destroyed, bury the memory stones"},
                    {"text": "Prioritize evacuation of most sensitive materials including memory stones; destroy remaining paper and wax thoroughly"},
                    {"text": "Destroy everything we cannot take - nothing should be left for the enemy"},
                    {"text": "Leave everything - records are just paper and stones, not worth risking lives for"}
                ],
                "success_text": """
You help prioritize the sanitization effort.

"With limited time and resources, we must be strategic. Not all materials
require the same treatment."

"HIGHEST PRIORITY for evacuation: Memory stones. These cannot be reliably
sanitized without specialized capabilities. If we can't destroy them
properly, we must evacuate them. Assign transport capacity accordingly."

"DESTROY THOROUGHLY: Paper records and wax tablets. Fire destroys paper
completely. Melted wax loses its inscriptions. Ensure complete destruction,
not partial burning that leaves readable fragments."

"VERIFY DESTRUCTION: Before evacuation is complete, verify that destroyed
materials are truly unrecoverable. Partial destruction may leave intelligence
value for the enemy."

"DOCUMENT what was destroyed and what was evacuated. Upon return to the
Citadel, leadership needs to know what the enemy might have captured if
anything was incomplete."

"Prioritization is key: Evacuate what we cannot reliably destroy. Destroy
what we cannot evacuate. Verify everything."

The Commander nods grimly. "Then we know our priorities. Memory stones
loaded first. Burn pits running continuously. Nothing usable left behind."

You have demonstrated understanding of MEDIA SANITIZATION under constraints.
                """,
                "failure_texts": {
                    0: """
Burying memory stones only delays discovery, not destruction. A determined
enemy will search the abandoned outpost thoroughly. Buried items will
eventually be found. For sanitization, items must be rendered unrecoverable,
not simply hidden. Burial is concealment, not destruction.
                    """,
                    2: """
With only three days and limited destruction capabilities, attempting to
destroy everything may result in incomplete destruction of critical items.
Resources should be focused on ensuring the most sensitive materials are
either evacuated or properly destroyed, rather than spreading effort across
all materials regardless of sensitivity.
                    """,
                    3: """
Intelligence value of abandoned records can be significant. Operational
information, names of agents, communication protocols, strategic plans -
all could aid the enemy. Proper sanitization is a military necessity, not
optional. The question is how to do it effectively with available resources,
not whether to do it at all.
                    """
                }
            },
            "corporate": {
                "title": "THE EMERGENCY OFFICE CLOSURE",
                "narrative": """
The regional office is being closed - immediately. A water main break has
made the building unsafe, and the landlord says you have 72 hours to vacate
before they start demolition prep. No extensions.

The office contains years of accumulated data: file cabinets, old laptops
in storage, backup tapes from the previous decade, and a server rack that
should have been decommissioned in 2019.

"We can't take everything," the facilities manager reports. "I've got two
moving trucks and whatever fits in people's cars. The rest gets abandoned
with the building."

IT speaks up: "The paper is easy - shred trucks are available. But those
old backup tapes? No degausser on site. The server drives? Standard wiping
takes longer than three days per drive, and we have twelve."

How do you advise handling this emergency sanitization?
                """,
                "choices": [
                    {"text": "Prioritize evacuation of most sensitive items, shred documents, bury the old tapes in the dumpster"},
                    {"text": "Prioritize evacuation of hard-to-sanitize media (tapes, drives); destroy documents thoroughly on-site"},
                    {"text": "Destroy everything - nothing leaves that could contain data"},
                    {"text": "Leave it all - the building is being demolished anyway"}
                ],
                "success_text": """
You help prioritize the emergency sanitization.

"Seventy-two hours isn't enough to do everything right. We need to be
strategic about what we can actually accomplish."

"HIGHEST PRIORITY for evacuation: Backup tapes and server drives. We can't
properly sanitize these without specialized equipment, so they leave with
us. Pack them in the trucks before anything else."

"DESTROY ON-SITE: Paper records. Get the shredding trucks rolling
immediately. Cross-cut shredding is sufficient for most documents. Burn
anything above Confidential if we can do it safely."

"VERIFY DESTRUCTION: Before we hand back the keys, walk the building.
Every drawer, every closet, every desk. If it stores data, it's either
gone or destroyed."

"DOCUMENT: What was evacuated, what was destroyed, what was inspected.
If something slips through, leadership needs to know what might have been
exposed."

"The old laptops in storage? Evacuate the drives, leave the shells. The
demolition company doesn't care about empty cases."

The facilities manager nods. "So tape drives and hard drives in the trucks,
shredding trucks running 24/7, and we personally verify every room."

"Exactly. If we can't destroy it properly, we take it with us. Period."

You've demonstrated MEDIA SANITIZATION under time constraints.
                """,
                "failure_texts": {
                    0: """
You just told IT to put backup tapes in a dumpster and "bury" them?

That's not sanitization. That's disposal. A demolition crew, a dumpster
diver, or literally anyone will find those tapes. And backup tapes are
notoriously durable - they'll survive being covered in construction debris.

If you can't destroy media properly, you must evacuate it. Concealment
is not destruction.
                    """,
                    2: """
You have 72 hours and twelve server drives that each need multi-pass
wiping. The math doesn't work.

"Destroy everything" sounds thorough but results in partial destruction
of everything, which is worse than complete destruction of some things.
A half-wiped drive is still recoverable.

Prioritization matters. Evacuate what you can't reliably destroy on-site.
Destroy what you can properly sanitize. Don't spread effort so thin that
nothing is actually secured.
                    """,
                    3: """
"The building is being demolished" doesn't mean your data is destroyed.

Demolition crews find stuff. They pull out recyclable metal, including
hard drives. They stack filing cabinets in salvage areas. Backup tapes
survive impacts that would destroy buildings.

Your data doesn't care about the landlord's schedule. Proper sanitization
is required regardless of what happens to the building afterward.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 65,
        "hp_penalty": 25,
        "failure_text": """
Media sanitization under time constraints requires:
- PRIORITIZATION: Focus on most sensitive materials first
- EVACUATION: Remove what cannot be reliably sanitized on-site
- APPROPRIATE METHODS: Match destruction method to media type
- VERIFICATION: Confirm destruction is complete
- DOCUMENTATION: Record what was destroyed vs. evacuated

Key principle: If you cannot reliably destroy sensitive media,
you must evacuate it. Partial destruction may be worse than none
if it creates false confidence.
        """,
        "domain_reference": "Domain 2: Asset Security - Media Sanitization, Emergency Procedures, Information Disposal"
    },

    # Scenario 11: Data Access Controls
    {
        "id": "d2_shared_scribes",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE SHARED SCRIBES",
                "narrative": """
The Citadel's Scribing Pool provides copying and documentation services to
multiple departments. Recently, concerns have emerged about scribes accessing
documents they shouldn't see.

"I sent a personal correspondence through the pool," complains Lord Ashford,
"and a scribe commented on its contents to a third party. The letter was
sealed!"

"And I found a scribe browsing inventory records unrelated to their current
task," adds the Supply Master.

The Scribing Pool supervisor defends the practice: "My scribes need broad
access to serve all departments efficiently. We can't constantly adjust
permissions based on individual tasks."

The Security Council asks you to evaluate the current access arrangements.
How do you advise addressing this situation?
                """,
                "choices": [
                    {"text": "Trust the scribes - they're vetted professionals who understand discretion"},
                    {"text": "Eliminate the Scribing Pool - each department should maintain its own scribes"},
                    {"text": "Implement need-to-know access - scribes access only documents required for their assigned tasks"},
                    {"text": "Log all scribe access and review for misuse - detection will deter improper access"}
                ],
                "success_text": """
You explain the principle of need-to-know access.

"The Scribing Pool can continue to serve all departments, but with
proper access controls. The principle is 'need-to-know' - personnel
access only information necessary for their specific assigned tasks."

"Implementation:"

"First, TASK-BASED ACCESS. When a scribe is assigned to copy Lord Ashford's
correspondence, they access that specific document. When finished, that
access ends. No browsing unrelated materials."

"Second, SEALED HANDLING. Personal correspondence and sensitive documents
should be handled without content access where possible. Copying sealed
letters doesn't require reading them."

"Third, ACCOUNTABILITY. Log what scribes access, review for patterns
outside normal duties. Not for punishment, but for detecting problems
and improving controls."

"Fourth, SUPERVISION. The pool supervisor ensures scribes receive only
appropriate assignments and maintains proper handling procedures."

"The supervisor's concern about efficiency is valid but manageable. Task-
based permissions can be administered efficiently with proper systems.
The efficiency cost is far less than the damage from confidentiality
breaches."

"Access should be a function of what you need to do, not who you are."

You have demonstrated understanding of DATA ACCESS CONTROLS.
                """,
                "failure_texts": {
                    0: """
Trust is not a substitute for access control. Even trusted personnel may
make mistakes, be curious beyond their need, or be compromised. The incidents
described demonstrate that current trust-based approaches have already failed.
Access controls protect both the organization and the individuals by removing
opportunities for improper access.
                    """,
                    1: """
Eliminating shared services to solve access problems is an overreaction that
creates inefficiency. The issue isn't shared services but inappropriate
access controls. Properly managed shared services can function securely.
The answer is better controls, not eliminated services.
                    """,
                    3: """
Logging and detection are important but insufficient alone. Detection occurs
AFTER improper access has happened. The confidential letter was already read,
the inventory already browsed. Prevention through appropriate access controls
should be the primary defense, with logging as a secondary control for
detection and investigation.
                    """
                }
            },
            "corporate": {
                "title": "THE ADMIN POOL PROBLEM",
                "narrative": """
The shared administrative assistant pool serves executives across the company.
Recently, there have been... incidents.

"I had Sarah draft a confidential email about the reorg," complains the VP
of Sales, "and somehow half the sales team knew about it before I even
sent it."

"And I found one of the admins browsing HR compensation files for the entire
department," adds the HR Director. "She said she was 'just curious' because
they're planning her department's admin appreciation gifts."

The Admin Pool manager pushes back: "My team needs broad system access to
support multiple executives. If they had to request permissions for every
task, they'd spend all day filling out access forms instead of working."

The CISO has asked you to evaluate the situation. How do you advise
addressing these access control problems?
                """,
                "choices": [
                    {"text": "Trust the admins - they're vetted employees who signed confidentiality agreements"},
                    {"text": "Eliminate the admin pool - each executive should have their own dedicated assistant"},
                    {"text": "Implement need-to-know access - admins access only data required for their assigned tasks"},
                    {"text": "Log all admin access and review for misuse - detection will deter improper access"}
                ],
                "success_text": """
You explain the principle of need-to-know access.

"The admin pool can continue supporting multiple executives, but with
proper access controls. The principle is 'need-to-know' - people access
only information necessary for their specific assigned tasks."

"Here's how it works:"

"First, TASK-BASED ACCESS. When Sarah is assigned to draft the reorg email,
she gets access to that document. When the task is done, access reverts.
No permanent broad access 'just in case.'"

"Second, ROLE SEPARATION. Admins working on HR tasks shouldn't have
access to Finance data at the same time. Segment access by current
assignment, not by 'admin pool member' status."

"Third, LOGGING AND MONITORING. Track what admins access and flag anomalies.
Not for punishment - for detecting problems before they become breaches.
'Browsing compensation files' should trigger an alert."

"Fourth, SUPERVISION. The pool manager is accountable for ensuring admins
receive only appropriate access and follow handling procedures."

"The manager's efficiency concern is valid but manageable. Modern access
management can handle dynamic permissions without excessive overhead. The
efficiency cost is far less than the cost of leaked reorg plans."

"Access should be based on what you're working on, not who you are."

You've demonstrated DATA ACCESS CONTROLS principles.
                """,
                "failure_texts": {
                    0: """
"They signed confidentiality agreements" is not an access control. The
confidentiality agreement didn't prevent Sarah from sharing the reorg
email. The NDA didn't stop the other admin from browsing HR files.

Trust is important but not sufficient. Even trusted, well-meaning employees
make mistakes, get curious, or face social pressure. Access controls
protect both the organization and the individuals by removing the
opportunity for improper access.

The incidents you just heard prove trust-only approaches have already
failed.
                    """,
                    1: """
So your solution to an access control problem is... spending 5x more on
dedicated admins for every executive?

The admin pool isn't the problem. The lack of proper access controls is
the problem. You can absolutely run shared services securely with
appropriate controls. Eliminating shared services because you can't
figure out permissions is admitting defeat.
                    """,
                    3: """
"We'll catch them after they do something wrong" isn't a security strategy.
It's damage control.

The reorg email was already leaked. The compensation files were already
browsed. Logging tells you what happened; it doesn't prevent it from
happening. By the time your SIEM alerts on anomalous access, the data
is already exposed.

Logging is important - as a secondary control. Prevention through proper
access restrictions is the primary defense. Detect what you can't prevent,
but try to prevent first.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 60,
        "hp_penalty": 20,
        "failure_text": """
Data access control principles:
- NEED-TO-KNOW: Access only information required for specific tasks
- LEAST PRIVILEGE: Minimum access necessary to perform duties
- TASK-BASED ASSIGNMENT: Permissions tied to assignments, not roles
- SEALED HANDLING: Process without viewing where possible
- LOGGING & MONITORING: Detect anomalous access patterns

Trust is not an access control. Even trusted personnel
should have only necessary access to reduce risk of error,
curiosity-driven access, or compromise.
        """,
        "domain_reference": "Domain 2: Asset Security - Access Controls, Need-to-Know, Least Privilege"
    },

    # Scenario 12: Data at Rest Protection
    {
        "id": "d2_encryption_debate",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE ENCRYPTION DEBATE",
                "narrative": """
The Treasury stores valuable financial records in the main vault - a
physically secure location with guards, locks, and limited access. The
Keeper of Coins argues against encrypting the records stored there.

"The vault is impenetrable," he insists. "Adding encryption to records
inside the most secure room in the Citadel is wasteful complexity. It
slows access, risks key loss, and provides no benefit when physical
security is already absolute."

The Security Advisor counters: "Physical security has failed before.
Guards can be bribed, locks can be picked, disasters can occur. What
happens if the vault's contents are exposed despite our physical measures?"

The Keeper scoffs. "You're suggesting we plan for failure. That's
defeatist thinking."

The Council asks your opinion on encrypting data that is already physically
secured.

How do you advise?
                """,
                "choices": [
                    {"text": "The Keeper is right - redundant security is wasteful when physical protection is strong"},
                    {"text": "Encrypt as a defense-in-depth measure - if physical security fails, encryption provides backup protection"},
                    {"text": "Encrypt only the most sensitive records - balance security benefit against operational cost"},
                    {"text": "Improve physical security instead - better locks and more guards address the actual weakness"}
                ],
                "success_text": """
You explain the principle of defense in depth.

"The Keeper's confidence in the vault is admirable but misplaced. Security
professionals don't plan for controls to fail because we're defeatist -
we plan for it because we're realistic."

"Consider the failure modes physical security doesn't address:"

"INSIDER THREAT - A trusted guard, bribed or coerced, grants unauthorized
access. The vault opens properly; the records are exposed."

"DISASTER - Fire, flood, or structural collapse exposes vault contents.
Physical integrity is lost; what protects confidentiality then?"

"SOPHISTICATED ATTACK - State actors or organized criminals with resources
we haven't anticipated find ways past our physical measures."

"Encryption provides a backup layer. Even if physical security fails,
encrypted records remain protected. The attacker gains ciphertext, not
intelligence."

"Yes, encryption has costs - key management, access overhead, recovery
complexity. But these are manageable costs for significant risk reduction."

"Defense in depth isn't planning for failure - it's planning for success
even when some controls fail. And some controls always eventually fail."

The Keeper reluctantly accepts the logic. "Very well. But key management
must be robust. I won't trade one vulnerability for another."

You have demonstrated understanding of DATA AT REST protection.
                """,
                "failure_texts": {
                    0: """
No physical security is 'absolute.' History shows that supposedly impenetrable
protections are eventually bypassed - through insider threat, sophisticated
attack, disaster, or unforeseen vulnerability. Defense in depth assumes that
any single control may fail and provides backup protection through additional
layers.
                    """,
                    2: """
While risk-based prioritization has merit, the argument here isn't about which
records to encrypt but whether to encrypt at all when physical security exists.
The principle of defense in depth applies regardless of sensitivity tier.
Classification may determine encryption strength, but the defense-in-depth
principle suggests encryption as a standard backup control.
                    """,
                    3: """
Improving physical security is valuable but doesn't address the fundamental
issue. Even perfect physical security (if such a thing existed) doesn't
protect against all failure modes - insider threat, coercion, disaster.
Different control types (physical, technical, administrative) address
different threats. Encryption addresses confidentiality; physical controls
address physical access. Both are needed.
                    """
                }
            },
            "corporate": {
                "title": "THE DATABASE ENCRYPTION DEBATE",
                "narrative": """
The DBA argues against encrypting the production database. "It's already
behind three layers of firewall, in a locked data center, on a network
segment that nobody can reach without VPN and MFA."

"Adding encryption-at-rest just slows down queries, complicates backups,
and introduces key management headaches. The data center is more secure
than most banks. Why add overhead when physical and network security is
already bulletproof?"

The Security Architect pushes back: "Physical security has limits. What
if a backup tape goes missing? What if a drive fails and goes to the
recycler with data still on it? What if someone with legit data center
access goes rogue?"

The DBA rolls his eyes. "You're being paranoid. You want us to plan for
every possible failure?"

The architecture review board looks to you for a tiebreaker. Should you
encrypt data that's already behind strong physical and network controls?
                """,
                "choices": [
                    {"text": "The DBA is right - encryption is redundant when physical and network security is strong"},
                    {"text": "Encrypt as defense-in-depth - if perimeter controls fail, encryption provides backup protection"},
                    {"text": "Encrypt only PII and payment data - balance security benefit against performance cost"},
                    {"text": "Improve physical security instead - better data center controls address the actual risk"}
                ],
                "success_text": """
You explain the principle of defense in depth.

"The DBA's confidence in perimeter security is understandable but
incomplete. Security professionals don't plan for control failure because
we're paranoid - we plan for it because we're realistic."

"Consider failure modes that physical and network security don't address:"

"INSIDER THREAT - A DBA, sysadmin, or data center tech with legitimate
access decides to exfiltrate data. All your perimeter controls see is
authorized access."

"MEDIA LIFECYCLE - Backup tapes get lost in transit. Failed drives get
recycled without proper sanitization. Decommissioned servers sit in
storage closets. Physical security protects running systems, not media
that leaves the building."

"BREACH ESCALATION - If someone does get through the perimeter, encryption
is the last line of defense. Without it, compromise of network access
equals compromise of all data."

"The performance overhead is manageable with modern hardware. Key management
is a solved problem. The complexity is far less than the cost of explaining
to regulators why unencrypted PII was on that missing backup tape."

"Defense in depth means assuming any single control can fail. Encryption
is the control that protects data when everything else has already failed."

The DBA sighs. "Fine. But I want hardware security modules for the keys."

"Now you're thinking like a security professional."

You've demonstrated DATA AT REST protection principles.
                """,
                "failure_texts": {
                    0: """
"The data center is secure" is what everyone says until backup tapes go
missing, or a contractor walks out with a drive, or an admin decides to
sell customer data on the dark web.

Physical and network security protect against external attack. They do
nothing against:
- Insiders with legitimate access
- Media that leaves the data center (backups, failed drives)
- Sophisticated attackers who get past the perimeter

No perimeter is "bulletproof." Defense in depth assumes any single control
can fail.
                    """,
                    2: """
"Only encrypt the sensitive stuff" sounds reasonable until you realize:
- Attackers don't care about your data classification
- The distinction between "PII" and "not PII" is often blurry
- Selective encryption creates configuration complexity and errors
- You might miss something

More importantly, the debate here isn't about WHICH data to encrypt - it's
about WHETHER to encrypt when physical security exists. The principle of
defense in depth says yes, regardless of data type.
                    """,
                    3: """
Better data center controls are great! And also: they don't address the
fundamental issue.

Physical security protects against physical intrusion. It doesn't protect
against:
- Authorized insiders going rogue
- Backup tapes lost in transit
- Drives recycled without sanitization
- Attackers who compromise the network layer

Different control types address different threats. Physical controls
address physical access. Encryption addresses confidentiality regardless
of how access was obtained. You need both.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 65,
        "hp_penalty": 20,
        "failure_text": """
Defense in depth for data at rest:
- Multiple control layers (physical + technical + administrative)
- Each layer provides backup if another fails
- No single control is 'absolute' or 'impenetrable'

Encryption for data at rest protects against:
- Insider threat (access doesn't equal reading)
- Physical security bypass
- Disaster exposure
- Device theft or loss

The cost of encryption is usually far less than
the cost of exposed data. Plan for control failures.
        """,
        "domain_reference": "Domain 2: Asset Security - Data at Rest, Encryption, Defense in Depth"
    },

    # Scenario 13: Data Sovereignty
    {
        "id": "d2_foreign_archive",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE FOREIGN ARCHIVE",
                "narrative": """
The Citadel maintains a small archive in a friendly foreign kingdom - a
backup location in case of catastrophe at home. Relations with that kingdom
have grown strained, and new laws there grant their crown authority to
inspect any archives within their borders.

"Our backup archive could be searched and copied by a foreign power," the
Foreign Affairs advisor warns. "Under their new laws, they have legal
authority within their borders."

"But it's OUR data," protests the Archive Master. "Surely ownership trumps
their local laws?"

"Location matters," the advisor replies. "Data within their borders is
subject to their jurisdiction, regardless of who owns it."

The Council debates whether to relocate the backup archive, accept the
risk, or find another solution.

How do you advise on this data sovereignty challenge?
                """,
                "choices": [
                    {"text": "Assert ownership rights - the data belongs to us regardless of location"},
                    {"text": "Accept the risk - the foreign kingdom is friendly and unlikely to actually inspect our archives"},
                    {"text": "Relocate the archive to jurisdiction we control, or encrypt so inspection yields nothing useful"},
                    {"text": "Negotiate a special agreement exempting our archive from their inspection laws"}
                ],
                "success_text": """
You address the data sovereignty concern directly.

"Data sovereignty means data is subject to the laws of where it resides.
Our ownership doesn't exempt our archive from their legal authority. We
have two reliable options:"

"RELOCATION: Move the archive to territory we control or to a jurisdiction
with stronger privacy protections. This removes the data from their legal
reach entirely. It may reduce some convenience benefits of the foreign
location but ensures sovereignty."

"ENCRYPTION: If relocation isn't feasible, encrypt the archive with keys
we control, stored outside their jurisdiction. They may have authority to
inspect, but inspection of properly encrypted data yields nothing useful.
This is a technical solution to a legal problem."

"Diplomatic agreements are worth pursuing but shouldn't be our only
protection. Political relationships change; technical controls remain
consistent."

"I recommend relocation as primary solution with encryption as standard
practice regardless. If relocation isn't immediately possible, encryption
buys time while we arrange the move."

The Council agrees. "We cannot control their laws, but we can control
where we put our data and how we protect it."

You have demonstrated understanding of DATA SOVEREIGNTY.
                """,
                "failure_texts": {
                    0: """
Legal jurisdiction typically follows physical location, not ownership.
Foreign governments can compel access to data within their borders regardless
of who owns it. Asserting ownership may be philosophically correct but
practically ineffective against sovereign authority. Physical location
determines whose laws apply.
                    """,
                    1: """
Relying on current friendly relations ignores political volatility. Today's
ally may be tomorrow's competitor or adversary. The laws enabling inspection
exist and could be invoked during any future diplomatic tension. Risk
acceptance based on current relations is shortsighted.
                    """,
                    3: """
Diplomatic agreements can provide some protection but are subject to change
with political winds. They may be revoked, reinterpreted, or overridden by
new laws. Technical and physical controls (relocation, encryption) provide
more reliable protection than diplomatic promises. Agreements should
supplement, not replace, concrete protections.
                    """
                }
            },
            "corporate": {
                "title": "THE EU DATA CENTER PROBLEM",
                "narrative": """
Your company operates a data center in Ireland for European customer data.
It's been convenient - GDPR compliance, EU data residency, good connectivity.
But new legislation just passed.

"The Irish government just enacted a law allowing access to data stored in
Ireland for national security purposes," Legal reports. "And the US
government is pressing its CLOUD Act rights on any data controlled by US
companies, regardless of where it's stored."

"Wait," the CISO says, "so BOTH governments can potentially demand access
to our European customer data?"

"It's OUR data," the CEO objects. "We own the servers, we own the building,
we control access. How can two governments claim jurisdiction?"

Legal sighs. "Data sovereignty doesn't work that way. Data is subject to
the laws where it resides AND to the laws of the company's home jurisdiction.
We're caught between two legal systems."

How do you advise addressing this data sovereignty challenge?
                """,
                "choices": [
                    {"text": "Assert that it's our data and resist any government demands"},
                    {"text": "Accept the risk - these laws are rarely enforced, and our customers won't know"},
                    {"text": "Relocate to a jurisdiction with stronger privacy laws, or implement customer-controlled encryption"},
                    {"text": "Negotiate agreements with both governments to limit data access requirements"}
                ],
                "success_text": """
You address the data sovereignty challenge directly.

"Data sovereignty means data is subject to the laws where it resides AND
the laws of controlling entities. We're in a dual-jurisdiction problem,
and ownership claims won't solve it. We have two options:"

"RELOCATION: Move European customer data to a jurisdiction with stronger
privacy protections - Switzerland, for example. This may complicate
operations but reduces legal exposure. Or: truly separate the EU entity
so it's not subject to US jurisdiction."

"ENCRYPTION: Implement customer-controlled encryption where we never have
access to the keys. If we can't decrypt the data, government demands become
technically moot. We hand over ciphertext; they get nothing useful."

"Both governments CAN legally compel access to data we control in their
jurisdictions. Our defense is to structure things so that either we're
outside their jurisdiction, or we technically can't comply because we
don't have the keys."

"Diplomatic agreements are nice to have but unreliable. GDPR adequacy
decisions get revoked. Privacy Shield got invalidated. Technical controls
are more durable than legal agreements."

The CEO nods. "So we can't argue our way out of this - we have to
architect our way out."

"Exactly. Data sovereignty is a technical problem as much as a legal one."

You've demonstrated DATA SOVEREIGNTY principles.
                """,
                "failure_texts": {
                    0: """
"It's our data and we'll resist demands" is a great way to get your
executives arrested and your company fined into oblivion.

Both governments have legal authority:
- Irish law applies to data physically in Ireland
- US law (CLOUD Act) applies to data controlled by US companies

Asserting ownership doesn't change jurisdiction. You can't argue your
way out of this - you need technical or structural solutions.
                    """,
                    1: """
"These laws are rarely enforced" is the security equivalent of "this
building code won't matter until there's a fire."

GDPR enforcement alone has generated billions in fines. The CLOUD Act
is actively used. And even if enforcement is rare, when it happens to
YOU, "rarely enforced" is no comfort.

Also: "our customers won't know" until they sue you for breach of contract
when their data gets disclosed. Risk acceptance requires informed
stakeholders - including customers.
                    """,
                    3: """
Negotiating with governments for special exemptions is... optimistic.

Governments don't typically carve out exceptions to national security
laws for individual companies. And even if they did, such agreements
are fragile - new administrations, new priorities, new interpretations.

Technical solutions (encryption, relocation) provide durable protection.
Diplomatic solutions provide temporary, revocable protection. Don't rely
on agreements when you can rely on architecture.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 70,
        "hp_penalty": 25,
        "failure_text": """
Data sovereignty principles:
- Data is subject to laws where it physically resides
- Ownership doesn't override local jurisdiction
- Political relationships change; plan for adverse scenarios
- Technical controls (encryption) can mitigate legal exposure
- Physical location determines legal authority

Strategies for data sovereignty:
1. Keep sensitive data in controlled jurisdictions
2. Encrypt data stored in other jurisdictions
3. Understand and comply with local laws
4. Don't rely solely on diplomatic relationships
        """,
        "domain_reference": "Domain 2: Asset Security - Data Sovereignty, Jurisdiction, International Data Protection"
    },

    # Scenario 14: Backup & Recovery
    {
        "id": "d2_backup_rotation",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE BACKUP ROTATION",
                "narrative": """
The Archive Master presents the Citadel's backup strategy for review.

"We create complete backups every moon at the full phase. The backup scrolls
are stored in the Eastern Tower - the same building as our primary archives
but in a different room. We keep three months of backups before recycling
the oldest."

She pauses. "We've done it this way for years. Is there anything wrong
with this approach?"

You note that the backup system has never been tested - they've never
actually needed to recover from a backup. The Archive Master admits that
no one has ever verified whether the backup scrolls are actually readable.

"But we follow the procedure faithfully," she says. "Surely that's
sufficient?"

What concerns do you raise about this backup strategy?
                """,
                "choices": [
                    {"text": "The strategy sounds adequate - monthly backups with three months of retention is reasonable"},
                    {"text": "Backups stored in the same building don't protect against building-level disasters; need offsite storage and regular testing"},
                    {"text": "Three months retention is too short - extend to one year minimum"},
                    {"text": "Monthly backups are too infrequent - should be daily to minimize data loss"}
                ],
                "success_text": """
You identify the critical gaps in the backup strategy.

"I see two major concerns that could make your entire backup effort worthless:"

"First, LOCATION. Storing backups in the same building as primary archives
provides no protection against building-level disasters - fire, flood,
structural collapse, enemy attack. If the Eastern Tower falls, you lose
both primary archives AND all backups. Offsite storage is essential."

"Second, TESTING. You've never verified that backups can actually be
restored. Backup scrolls could be damaged, incomplete, or use outdated
formats that are no longer readable. A backup you've never tested is an
assumption, not a safeguard."

"Additionally, consider:"

"Recovery Point Objective (RPO): How much data loss is acceptable? Monthly
backups mean potentially losing a full month of changes. Is that acceptable
for your archives?"

"Recovery Time Objective (RTO): How quickly must archives be restored
after a disaster? Do your current procedures support that timeline?"

"I recommend: establish offsite backup storage, implement regular test
restorations, and document recovery procedures so anyone can execute them
in an emergency."

The Archive Master looks concerned. "We've been doing this for years
thinking we were protected."

"You were partially protected. Let's make you fully protected."

You have demonstrated understanding of BACKUP AND RECOVERY principles.
                """,
                "failure_texts": {
                    0: """
The frequency and retention may be reasonable, but several critical issues
exist: same-building storage doesn't protect against building-level disasters,
untested backups may be unreadable, and no verification that backups actually
contain needed data. A backup that has never been tested is hope, not a plan.
                    """,
                    2: """
While retention period matters, it's not the most critical issue here. Even
a year of backups provides no protection if they're stored in the same
building that might be destroyed or if they've never been tested for
readability. Location and verification are more urgent concerns than
retention period.
                    """,
                    3: """
Backup frequency depends on how much data loss is acceptable (Recovery Point
Objective). Monthly may be appropriate for archival materials that don't
change daily. However, this criticism misses more fundamental issues: same-
building storage and lack of testing. Frequency optimization is secondary
to ensuring backups actually work and survive disasters.
                    """
                }
            },
            "corporate": {
                "title": "THE BACKUP AUDIT FINDINGS",
                "narrative": """
The external auditors have questions about your backup strategy.

"We back up to tape every night," the sysadmin explains. "The tapes are
stored in the server room closet. We rotate through a two-week set, so
we can go back 14 days. Been doing it this way since 2015."

The auditor raises an eyebrow. "When was the last time you tested a
restore?"

The sysadmin thinks. "We restored a file for accounting... maybe two years
ago? It worked fine."

"And where's your offsite copy?"

"The server room is in a different building than the offices. Different
building, different fire zone. That counts as offsite, right?"

The auditor makes a note. "It's on the same campus, connected to the same
infrastructure. What's your documented Recovery Time Objective?"

The sysadmin looks confused. "Our what?"

The auditors turn to you. What concerns do you raise about this backup
strategy?
                """,
                "choices": [
                    {"text": "The strategy sounds adequate - nightly backups with two weeks retention is reasonable"},
                    {"text": "Backups on the same campus don't protect against site disasters; need true offsite storage and regular testing"},
                    {"text": "Two weeks retention is too short - extend to 90 days minimum"},
                    {"text": "Nightly backups are too infrequent for transaction systems - should be hourly"}
                ],
                "success_text": """
You identify the critical gaps that the auditors are circling.

"I see two major concerns that could make your entire backup effort
worthless when you actually need it:"

"First, LOCATION. 'Different building on the same campus' is not offsite.
A campus-wide disaster - fire, flood, power event, ransomware that spreads
through the network - takes out both production AND backups. True offsite
means geographically separate, ideally in a different region."

"Second, TESTING. You haven't done a real restore test in two years. A
single file restore doesn't validate that you can actually recover your
systems. Those tapes might be degraded, the backup software might have
bugs, or the recovery procedures might be wrong. A backup you've never
tested is hope, not a plan."

"The auditors are going to ask about:"

"RPO (Recovery Point Objective): Nightly backups mean up to 24 hours of
data loss. Is that acceptable? For transaction systems, probably not."

"RTO (Recovery Time Objective): How quickly can you actually restore from
tape? Have you measured it? Can you meet business requirements?"

"I recommend: true offsite replication, regular test restores, and
documented recovery procedures with defined RPO/RTO metrics."

The sysadmin looks nervous. "So we've been running without a safety net."

"You've been running with a safety net that's never been tested. Big
difference when you actually fall."

You've demonstrated BACKUP AND RECOVERY principles.
                """,
                "failure_texts": {
                    0: """
The frequency and retention might be adequate, but you're missing the
critical issues:

1. "Different building on the same campus" is NOT offsite. A single
disaster - fire, flood, ransomware - can take out both production and
backups simultaneously.

2. No regular restore testing means you don't know if your backups work.
That two-year-old single-file restore doesn't validate full system recovery.

An untested backup in the same location is false security. You don't have
a backup strategy; you have a hope strategy.
                    """,
                    2: """
Retention period matters, but it's not the critical issue here.

Whether you keep backups for 2 weeks or 2 years, they're all sitting in
the same server room closet. A single disaster destroys all of them along
with your production systems.

And even with 90 days of retention, if you've never tested a restore,
you don't know if ANY of those tapes are usable. Location and testing
are more urgent problems than retention length.
                    """,
                    3: """
Backup frequency depends on your Recovery Point Objective - how much data
loss is acceptable. For some systems, hourly makes sense. For others,
nightly is fine.

But this criticism misses the fundamental problems: your "offsite" is
on the same campus, and you haven't tested a full restore in years.

Whether you back up hourly or nightly, if all copies are destroyed
together or none of them can be restored, frequency doesn't matter.
Fix location and testing first.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 65,
        "hp_penalty": 20,
        "failure_text": """
Backup strategy requirements:
- OFFSITE STORAGE: Backups survive disasters affecting primary location
- REGULAR TESTING: Verify backups are readable and complete
- RPO DEFINITION: How much data loss is acceptable?
- RTO DEFINITION: How quickly must recovery occur?
- DOCUMENTED PROCEDURES: Anyone can execute recovery

Common backup failures:
- Same-location storage (destroyed with primary)
- Never-tested backups (unreadable when needed)
- Incomplete backups (missing critical data)
- Obsolete formats (no longer usable)

An untested backup is hope, not a plan.
        """,
        "domain_reference": "Domain 2: Asset Security - Backup & Recovery, Disaster Recovery, RPO/RTO"
    },

    # Scenario 15: Labeling Requirements
    {
        "id": "d2_sensitive_markings",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE SENSITIVE MARKINGS",
                "narrative": """
The Classification Officer presents a dilemma. A senior advisor requested
that certain highly sensitive documents be "discretely classified" - marked
in a way that indicates their sensitivity to those who know how to read
the markings, but doesn't obviously scream "SECRET" to casual observers.

"He argues that obvious SECRET stamps actually draw attention to documents,"
the Officer explains. "Better to use subtle markings that authorized people
understand but that don't advertise the content's value."

The advisor's logic has appeal - obvious security markings do indicate
that something valuable is inside. But you sense something wrong with this
approach.

How do you advise the Classification Officer?
                """,
                "choices": [
                    {"text": "The advisor makes a good point - subtle markings reduce the 'advertising' effect of obvious stamps"},
                    {"text": "Labels must be clear and standard so everyone handling the material knows its sensitivity"},
                    {"text": "Use both - obvious stamps for internal handling, subtle marks for external transport"},
                    {"text": "Rely on physical protection instead of labeling - secure containers make labels unnecessary"}
                ],
                "success_text": """
You explain why clear labeling is essential.

"The advisor's concern about advertising value is understandable but
misguided. Classification labels serve a critical function that subtle
marking cannot fulfill."

"Consider who handles classified materials: couriers, clerks, archivists,
assistants, visiting officials - many of whom are not trained in subtle
coding schemes. They need to immediately recognize that a document
requires special handling."

"Clear, standard labeling ensures:"

"UNIVERSAL RECOGNITION - Anyone handling the document knows its sensitivity
regardless of their familiarity with internal coding systems."

"CONSISTENT HANDLING - Standard markings tie to standard procedures.
Everyone knows what SECRET means and how to handle it."

"ACCOUNTABILITY - Clear markings make mishandling obvious. Subtle markings
make violations easier to excuse or overlook."

"As for the 'advertising' concern - this is addressed through physical
protection of labeled documents, not by obscuring the labels themselves.
Sensitive documents should be in folders, containers, or restricted areas.
The label protects against improper handling; the container protects
against casual observation."

"Clear labeling protects documents. Subtle labeling protects nothing."

You have demonstrated understanding of LABELING REQUIREMENTS.
                """,
                "failure_texts": {
                    0: """
Subtle or hidden markings undermine the entire purpose of classification
labeling. Labels exist so that EVERYONE handling the material knows its
sensitivity and handling requirements - not just insiders who know the secret
codes. A courier, clerk, or new employee needs to immediately recognize
sensitive materials. Obscurity in labeling creates handling failures.
                    """,
                    2: """
Dual-marking systems create confusion and errors. Does this document have
obvious marking, subtle marking, or both? Which applies when? Complexity
in classification systems leads to handling mistakes. Consistent, clear,
standard marking is more reliable than sophisticated multi-layer schemes.
                    """,
                    3: """
Physical protection and labeling serve different purposes. Containers protect
during storage and transport; labels inform handlers at every point. A
document removed from its container still needs to show its classification.
Labeling is the persistent indicator; containers are temporary protection.
Both are needed.
                    """
                }
            },
            "corporate": {
                "title": "THE DISCRETE CLASSIFICATION REQUEST",
                "narrative": """
The VP of Strategy doesn't like how "CONFIDENTIAL" labels look on his
board presentations. He's requested that sensitive materials use a more
"discrete" marking system.

"Those big red CONFIDENTIAL stamps make documents look suspicious," he
argues. "When I'm traveling with board materials, I don't want everyone at
the airport thinking I'm carrying state secrets. Can't we use something
subtle, like a small colored dot that only insiders would recognize?"

The Information Security team is skeptical, but the VP has executive
support. "Other companies do this," he insists. "A little symbol that
authorized people understand, but that doesn't advertise the contents."

The classification manager asks your opinion. There is some logic to the
VP's concern - obvious labels do draw attention. But something about this
feels wrong.

How do you advise?
                """,
                "choices": [
                    {"text": "The VP makes a good point - subtle markings reduce the 'advertising' effect of obvious labels"},
                    {"text": "Labels must be clear and standard so everyone handling the material knows its sensitivity"},
                    {"text": "Use both - obvious labels for internal use, subtle marks for travel and external meetings"},
                    {"text": "Rely on physical protection instead - encrypted devices and locked bags make labels unnecessary"}
                ],
                "success_text": """
You explain why clear labeling is non-negotiable.

"The VP's concern about visibility is understandable, but his solution
undermines the entire purpose of classification marking."

"Consider who handles sensitive documents: admins printing them, mail
room sorting them, new employees not yet trained in secret dot systems,
conference center staff cleaning up after meetings. They all need to
immediately recognize that something requires special handling."

"Clear, standard labeling ensures:"

"UNIVERSAL RECOGNITION - The temp worker shredding documents knows what
CONFIDENTIAL means. They don't know what a blue dot means."

"CONSISTENT HANDLING - Everyone knows the procedures for CONFIDENTIAL.
'Subtle marking' creates confusion about what rules apply."

"ACCOUNTABILITY - When someone mishandles clearly labeled documents, it's
obviously wrong. 'I didn't know what the dot meant' is a valid excuse
when markings are deliberately obscure."

"As for airport concerns - that's what folders and laptop bags are for.
Physical containers protect documents from casual observation. Labels
protect documents from improper handling. Different problems, different
solutions."

"The VP can put his CONFIDENTIAL presentation in a plain folder. He can't
remove the classification."

You've demonstrated LABELING REQUIREMENTS principles.
                """,
                "failure_texts": {
                    0: """
You just approved a classification system that only works for insiders
who know the secret codes.

What happens when the new admin doesn't know that a blue dot means
confidential? What happens when facilities staff finds an unmarked
document? What happens when someone outside your secret-dot circle
needs to handle sensitive materials?

Labels exist so EVERYONE handling materials knows the sensitivity level.
"Subtle markings that authorized people understand" is security through
obscurity - and it fails the moment anyone outside the circle touches
the document.
                    """,
                    2: """
Now you have two parallel classification systems and nobody knows which
one applies when.

"This document has a red CONFIDENTIAL stamp but also a blue dot. Which
takes precedence?"
"We're traveling, so use the dot system. But wait, now we're meeting
with external parties who don't know the dot system..."

Complexity creates errors. The more complicated your marking scheme, the
more likely someone handles something wrong because they were confused.
One clear, consistent system beats two overlapping systems every time.
                    """,
                    3: """
"We don't need labels because everything is encrypted and locked" misses
the point entirely.

What happens when you decrypt the laptop to work on the presentation?
What happens when you print a copy for the meeting? What happens when
the locked bag gets opened at security?

Encryption protects data in transit and at rest. Physical containers
protect during transport. Labels protect documents at every point in
their lifecycle, including when they're being actively used. They solve
different problems.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 60,
        "hp_penalty": 20,
        "failure_text": """
Classification labeling requirements:
- CLEAR: Immediately recognizable to all handlers
- STANDARD: Consistent across the organization
- PROMINENT: Cannot be missed or overlooked
- PERSISTENT: Remains with the document throughout lifecycle

Labels serve handlers, not just owners. Everyone who touches
a classified document needs to know its sensitivity level
and handling requirements without special training in subtle
codes or hidden markings.

Physical protection (containers, folders) addresses visibility.
Labels address handling requirements.
        """,
        "domain_reference": "Domain 2: Asset Security - Classification Labeling, Marking Requirements, Handling"
    },

    # Scenario 16: Information Compartmentalization
    {
        "id": "d2_need_to_know",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE NEED TO KNOW",
                "narrative": """
Operation Shadowfall is the Citadel's most sensitive current initiative.
Information about it is strictly compartmentalized - only those directly
involved know anything about it.

The Chief of Operations, who oversees all Citadel activities, demands
full briefing. "I cannot effectively coordinate operations without
understanding all initiatives. My clearance is the highest in the
Citadel. I should know everything."

The Operation Shadowfall commander pushes back: "With respect, the Chief's
role doesn't require knowledge of our specific activities. Compartmental-
ization exists precisely to limit damage if any individual is compromised."

The Chief is offended. "Are you suggesting I might be compromised?"

"I'm suggesting that anyone might be, regardless of rank or loyalty."

The Council must resolve this dispute. The Chief has authority and clearance.
The commander has compartmentalization principles.

How do you advise the Council?
                """,
                "choices": [
                    {"text": "Brief the Chief - his rank and clearance entitle him to full knowledge of all operations"},
                    {"text": "Maintain compartmentalization - clearance without need-to-know doesn't justify access"},
                    {"text": "Provide a summary briefing - enough for coordination without full operational details"},
                    {"text": "Let the Chief decide - as senior leader, he can determine what he needs to know"}
                ],
                "success_text": """
You support the principle of compartmentalization.

"The Chief's clearance establishes that he MAY receive highly classified
information. It doesn't establish that he MUST receive all such information.
These are separate requirements."

"Compartmentalization exists because even highly cleared, thoroughly trusted
individuals represent risk. They might be:"

"COMPROMISED through blackmail, bribery, or coercion"
"CAPTURED during conflict or travel"
"CARELESS despite best intentions"
"CURIOUS about information outside their need"

"The more people who know a secret, the greater the risk of exposure. This
is mathematics, not distrust. Limiting knowledge to those who need it
reduces the attack surface and limits damage from any individual failure."

"If the Chief's coordination role genuinely requires Shadowfall knowledge,
that creates legitimate need-to-know. But coordination of other operations
doesn't automatically require knowledge of every operation."

"The proper process: Shadowfall command evaluates whether the Chief's role
requires specific knowledge. If yes, brief appropriately. If no, maintain
compartmentalization. The decision should be based on operational need,
not rank or clearance level."

You have demonstrated understanding of NEED-TO-KNOW principles.
                """,
                "failure_texts": {
                    0: """
Rank and clearance establish eligibility to receive information, not
entitlement to receive it. Need-to-know is a separate requirement. The Chief
may have clearance for this information, but if his role doesn't require it,
briefing him increases risk without operational benefit. Compartmentalization
specifically prevents 'everyone with clearance knows everything.'
                    """,
                    2: """
Partial briefings often satisfy neither security nor operational needs. The
Chief either needs the information or doesn't. If he needs it for coordination,
he needs enough to actually coordinate. If he doesn't need it for coordination,
why brief him at all? Partial disclosure creates misunderstanding without
enabling effective action.
                    """,
                    3: """
This undermines compartmentalization entirely. If people can decide for
themselves what they need to know, compartments become meaningless. The
decision about need-to-know should be based on operational requirements,
not individual desire for information. Those outside a compartment don't
decide to enter it.
                    """
                }
            },
            "corporate": {
                "title": "THE EXECUTIVE CURIOSITY",
                "narrative": """
The M&A team is working on a highly confidential acquisition - code name
"Project Phoenix." Only five people in the company know about it. The
deal would transform the company, but premature disclosure could tank the
stock price and alert competitors.

The CTO demands to be briefed. "I'm on the executive team. I have the
highest access level in the company. I should know about all strategic
initiatives. How can I plan technology strategy without knowing where
the company is going?"

The General Counsel pushes back: "With respect, your role doesn't require
knowledge of this specific transaction. Compartmentalization exists to
limit insider trading exposure and prevent leaks."

The CTO is offended. "You're treating me like a security risk. I've been
with this company for fifteen years!"

"Everyone is a potential security risk. That's not personal - it's math."

The CEO asks for your input. The CTO has the clearance and the rank. But
does he have the need-to-know?

How do you advise?
                """,
                "choices": [
                    {"text": "Brief the CTO - his executive role entitles him to knowledge of strategic initiatives"},
                    {"text": "Maintain compartmentalization - executive role without need-to-know doesn't justify access"},
                    {"text": "Provide a high-level summary - enough for planning without transaction details"},
                    {"text": "Let the CTO decide - as an executive, he can determine what he needs for his role"}
                ],
                "success_text": """
You support the principle of need-to-know.

"The CTO's executive status establishes that he MAY receive highly
confidential information. It doesn't establish that he MUST receive all
such information. These are separate requirements."

"Compartmentalization exists because even senior, trusted executives
represent risk:"

"INSIDER TRADING - The more people who know about an acquisition, the
greater the SEC scrutiny if anyone trades. Adding people to the compartment
increases legal exposure."

"INADVERTENT DISCLOSURE - People talk. Even careful executives mention
things to spouses, former colleagues, industry contacts. Every additional
person is an additional leak vector."

"SOCIAL ENGINEERING - Executives are high-value targets for competitive
intelligence. The CTO might be approached at a conference, and even
declining to comment on 'Project Phoenix' confirms something exists."

"If the CTO's technology planning genuinely requires Phoenix knowledge,
that creates legitimate need-to-know. But general 'I'm an executive'
doesn't satisfy need-to-know."

"The proper process: Does the CTO's specific role require this specific
information? If yes, brief appropriately and add him to the insider list.
If no, maintain compartmentalization."

The CEO nods. "So it's not about trust. It's about exposure."

"Exactly. Every person who knows is a risk vector. Add people when
necessary, not when requested."

You've demonstrated NEED-TO-KNOW principles.
                """,
                "failure_texts": {
                    0: """
"Executive role entitles him to know everything" is how insider trading
cases start.

The CTO doesn't need acquisition details for technology planning. What he
needs is: "There may be strategic changes coming. Build flexibility into
our architecture." He doesn't need target names, valuations, or timelines.

Every person added to the compartment increases SEC scrutiny, leak risk,
and social engineering exposure. Executive status establishes clearance
eligibility, not automatic entitlement. These are different things.
                    """,
                    2: """
"High-level summary" is a compromise that satisfies nobody and protects
nothing.

If the CTO needs to plan technology integration, he needs real details.
If he doesn't need details, why brief him at all? Now he knows something
exists (creating curiosity and leak risk) without knowing enough to
actually act on it.

Either there's a genuine need-to-know that justifies full briefing, or
there isn't and you maintain compartmentalization. Half-measures just
spread exposure without providing operational value.
                    """,
                    3: """
"Let people decide what they need to know" destroys compartmentalization
entirely.

If executives can self-authorize access to compartmented information,
compartments don't exist. Everyone will decide they "need" to know
everything interesting. The CTO's judgment about his own information
needs isn't the issue - it's whether his role actually requires this
specific information.

Need-to-know is determined by operational requirement, not by the requester's
desire for information.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 70,
        "hp_penalty": 25,
        "failure_text": """
Compartmentalization principles:
- CLEARANCE: Establishes eligibility to receive classified information
- NEED-TO-KNOW: Establishes requirement to receive specific information
- Both requirements must be met for access

Why compartmentalize:
- Limits damage from any single compromise
- Reduces attack surface (fewer targets to recruit/coerce)
- Mathematical risk reduction (fewer people = fewer exposure vectors)

Rank doesn't override need-to-know. Senior leaders
don't automatically need knowledge of every operation.
Access should be based on genuine operational requirement.
        """,
        "domain_reference": "Domain 2: Asset Security - Need-to-Know, Compartmentalization, Access Control"
    },

    # Scenario 17: Data Subject Rights
    {
        "id": "d2_data_request",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE DATA REQUEST",
                "narrative": """
A citizen named Marcus formally requests access to all information the
Citadel holds about him - a right granted under the new Privacy Charter.

The Records Keeper compiles the response and finds Marcus's file contains:
- Personal details he provided during a guild application
- Transaction records from the marketplace
- A confidential security assessment noting "suspected smuggling involvement"
- Notes from an ongoing investigation into his business associates

"The security assessment and investigation notes are problematic," the
Keeper observes. "If we reveal them, we compromise our intelligence
gathering. But the Privacy Charter says citizens can access their records."

How do you advise handling this data subject access request?
                """,
                "choices": [
                    {"text": "Provide everything - the Privacy Charter grants access rights that override other considerations"},
                    {"text": "Refuse the entire request citing security concerns"},
                    {"text": "Provide non-sensitive data; withhold investigation-related materials under legitimate exemptions"},
                    {"text": "Delay the response indefinitely while the investigation continues"}
                ],
                "success_text": """
You outline the appropriate approach to this access request.

"Privacy rights are important and should be honored - but they're not
absolute. The Privacy Charter includes exemptions that apply here."

"For Marcus's request:"

"PROVIDE: Personal details he submitted and transaction records. These
are his information, there's no sensitivity, and withholding would be
improper."

"WITHHOLD: Security assessment and investigation notes. These fall under
exemptions for ongoing investigations and intelligence methods. However,
we must:"

"DOCUMENT the exemption - record that certain materials were withheld
under specific Charter provisions, not arbitrarily."

"NOTIFY APPROPRIATELY - inform Marcus that some information is withheld
under lawful exemption, without revealing what the withheld information
contains or that an investigation exists."

"REVIEW PERIODICALLY - when the investigation concludes, reassess whether
exemptions still apply."

"The key is neither wholesale disclosure nor wholesale refusal. We provide
what we legitimately can, withhold what we legitimately must, and document
everything."

"Marcus receives a genuine response honoring his rights while protecting
legitimate security interests."

You have demonstrated understanding of DATA SUBJECT RIGHTS.
                """,
                "failure_texts": {
                    0: """
Privacy rights typically include exemptions for ongoing investigations,
national security, and third-party privacy. Revealing investigation details
could compromise current operations, endanger sources, or alert targets.
Privacy rights are important but not absolute - legitimate exemptions exist
and should be applied appropriately.
                    """,
                    1: """
Blanket refusal is inappropriate when the request includes data that can
legitimately be provided. The personal details and transaction records
have no security sensitivity. Refusing everything when only some data is
sensitive violates the citizen's legitimate rights and may invite legal
challenge.
                    """,
                    3: """
Indefinite delay is effectively denial without proper justification. Privacy
regulations typically require timely responses with documented reasons for
any denial or delay. Stalling without legal basis exposes the Citadel to
challenge and undermines legitimate privacy processes. If exemptions apply,
invoke them properly rather than simply delaying.
                    """
                }
            },
            "corporate": {
                "title": "THE DSAR DILEMMA",
                "narrative": """
You've received a Data Subject Access Request (DSAR) under GDPR. A customer
named Alex Chen wants all data your company holds about them.

The Privacy team compiles the response and finds Alex's file contains:
- Account information they provided during signup
- Purchase history and customer service transcripts
- An internal fraud alert flagging their account for "suspicious return patterns"
- Notes from an ongoing investigation by Loss Prevention

"The fraud alert and investigation notes are problematic," the Privacy
Officer observes. "If we reveal them, we tip off a potential fraudster
and compromise our investigation. But GDPR says individuals can access
their personal data."

Legal is nervous. "DSARs have strict timelines. We can't just ignore this."

Loss Prevention is nervous. "If they know we're watching, they'll change
behavior or destroy evidence."

How do you advise handling this data subject access request?
                """,
                "choices": [
                    {"text": "Provide everything - GDPR rights override internal investigations"},
                    {"text": "Refuse the entire request citing the ongoing investigation"},
                    {"text": "Provide non-investigation data; withhold fraud-related materials under legitimate exemptions"},
                    {"text": "Delay the response until the investigation concludes"}
                ],
                "success_text": """
You outline the proper DSAR response approach.

"GDPR rights are important and must be honored - but they're not absolute.
Article 23 allows exemptions for prevention and detection of criminal
offenses. This is one of those cases."

"For Alex's request:"

"PROVIDE: Account information, purchase history, customer service
transcripts. This is their data, there's no sensitivity, and withholding
would violate their rights."

"WITHHOLD: Fraud alert and investigation notes. These fall under exemptions
for crime prevention. However, we must:"

"DOCUMENT properly - record that materials were withheld under GDPR Article
23 exemptions, with legal review confirming the exemption applies."

"NOTIFY carefully - inform Alex that some information is withheld under
lawful exemption. We don't have to reveal what's withheld or why, but we
can't pretend the exemption doesn't exist."

"TIMELINE compliance - respond within the GDPR deadline (30 days), even
if the response is partial. Don't miss the deadline hoping the investigation
wraps up."

"REVIEW when investigation closes - if the case resolves, reassess whether
exemptions still apply and provide remaining data if appropriate."

"Alex gets a legitimate response honoring their privacy rights. We protect
the investigation without violating GDPR."

You've demonstrated DATA SUBJECT RIGHTS principles.
                """,
                "failure_texts": {
                    0: """
You just disclosed fraud investigation details to the subject of the
fraud investigation. Congratulations - you've tipped off a potential
fraudster.

GDPR isn't absolute. Article 23 explicitly allows exemptions for "the
prevention, investigation, detection or prosecution of criminal offences."
Fraud investigations qualify.

You can - and should - withhold investigation-related materials while
still providing the non-sensitive data they're entitled to.
                    """,
                    1: """
Blanket refusal violates GDPR when the request includes data that should
be provided.

The account information? Their data, no exemption. Purchase history?
Their data, no exemption. Customer service transcripts? Their data, no
exemption.

"There's an investigation" doesn't exempt ALL data - it exempts
investigation-RELATED data. Refusing everything invites a complaint to
the supervisory authority and demonstrates bad faith.
                    """,
                    3: """
GDPR has a 30-day response deadline (extendable to 90 days for complex
requests). "We'll respond when our investigation is done" isn't compliant.

Indefinite delay is effectively refusal without proper justification.
Regulators have specifically called out this tactic as non-compliant.

If exemptions apply, invoke them properly and respond on time. Explain
that some data is withheld under lawful exemption. Don't just stall and
hope they forget.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 65,
        "hp_penalty": 20,
        "failure_text": """
Data subject access rights include:
- Right to know what data is held about them
- Right to receive copy of their data
- But also: legitimate exemptions for security, investigations, third-party privacy

Proper handling:
1. Review all responsive data
2. Identify applicable exemptions
3. Provide what can be provided
4. Document exemptions properly
5. Notify data subject of withheld data and legal basis
6. Review exemptions periodically

Neither blanket disclosure nor blanket refusal is appropriate.
        """,
        "domain_reference": "Domain 2: Asset Security - Privacy Rights, Data Subject Access, Exemptions"
    },

    # Scenario 18: Data Migration Security
    {
        "id": "d2_merger_records",
        "domain": 2,
        "themes": {
            "fantasy": {
                "title": "THE MERGER RECORDS",
                "narrative": """
The Citadel is absorbing a smaller outpost through strategic merger. The
outpost's records must be migrated to Citadel systems. The project manager
presents a timeline for rapid integration.

"We'll copy everything over this weekend. The outpost systems will be
decommissioned by next moon. We need to move fast to realize the merger
benefits."

The Security Officer raises concerns: "Have we verified data integrity
after copying? Checked that classification levels are compatible? Ensured
nothing is lost in transfer? Confirmed the outpost systems are properly
sanitized after migration?"

The project manager waves dismissively. "We're copying files, not launching
ships. How complicated can it be?"

How do you advise on this data migration?
                """,
                "choices": [
                    {"text": "Support the rapid timeline - speed is important for merger success"},
                    {"text": "Require verification steps: integrity confirmation, classification mapping, source sanitization, with timeline adjusted accordingly"},
                    {"text": "Let IT handle it - data migration is a technical matter, not a security matter"},
                    {"text": "Keep copies on the outpost systems as backup - don't decommission until we're sure the migration worked"}
                ],
                "success_text": """
You insist on proper migration security.

"Data migration is not just copying files. It's transferring custody of
potentially sensitive information between systems. This requires security
rigor."

"The migration must include:"

"INTEGRITY VERIFICATION - After copying, verify that destination data
matches source data exactly. Checksums, record counts, sample verification.
Detect corruption or loss before decommissioning the source."

"CLASSIFICATION MAPPING - The outpost may use different classification
levels or labels. Map their classifications to ours so data receives
appropriate protection in the new environment."

"ACCESS CONTROL REVIEW - Who had access at the outpost? Who should have
access here? Don't blindly migrate permissions that may be inappropriate
in the new context."

"SOURCE SANITIZATION - When migration is verified complete, properly
sanitize the outpost systems. Don't leave sensitive data on decommissioned
equipment. This isn't optional - it's essential."

"DOCUMENTATION - Record what was migrated, verify its integrity, confirm
sanitization. Create audit trail for the entire process."

"The timeline adjusts to accommodate these requirements. Migration done
properly takes longer than 'just copying.' Migration done improperly
creates problems that take even longer to fix."

You have demonstrated understanding of DATA MIGRATION SECURITY.
                """,
                "failure_texts": {
                    0: """
Speed at the expense of security creates long-term problems. Rushed migrations
risk data loss, integrity failures, classification mismatches, and improper
source sanitization. Problems created during rapid migration may take far
longer to fix than a proper migration would have taken. Security requirements
don't disappear under time pressure.
                    """,
                    2: """
Data migration has significant security implications: potential data loss,
classification conflicts, exposed sensitive data on improperly sanitized
source systems, and chain of custody concerns. Security must be involved in
migration planning, not relegated to technical afterthought. IT and Security
must collaborate on proper migration.
                    """,
                    3: """
Maintaining data on decommissioned systems creates ongoing risk. Those systems
will receive less attention, security patches, and monitoring over time,
while still containing sensitive data. The proper approach is verified
migration followed by proper sanitization, not indefinite parallel storage.
                    """
                }
            },
            "corporate": {
                "title": "THE M&A DATA MIGRATION",
                "narrative": """
Your company just acquired a competitor. The integration PMO presents an
aggressive timeline for data migration.

"We need their customer database integrated by end of quarter to realize
the acquisition synergies. The plan is simple: dump their data into our
systems over the holiday weekend, then decommission their infrastructure."

The IT Security lead raises concerns: "Have we validated data integrity
after transfer? Mapped their data classification to ours? Verified that
permissions make sense in our environment? Planned for proper sanitization
of their old systems?"

The PMO lead is dismissive. "It's a database copy. We do this all the time.
The business is pushing hard on the timeline - we can't slow down for
theoretical security concerns."

The integration steering committee asks for your input. How do you advise
on this data migration?
                """,
                "choices": [
                    {"text": "Support the aggressive timeline - business value depends on quick integration"},
                    {"text": "Require verification steps: integrity validation, classification mapping, permission review, source sanitization, with timeline adjusted accordingly"},
                    {"text": "Let IT handle it - data migration is a technical matter, not a security matter"},
                    {"text": "Keep copies on their old systems as backup - don't decommission until we're sure the migration worked"}
                ],
                "success_text": """
You insist on proper migration security.

"Data migration isn't 'just a copy.' It's transferring custody of customer
PII, proprietary data, and potentially regulated information between systems.
This requires security rigor."

"The migration must include:"

"INTEGRITY VERIFICATION - After copying, validate that destination data
matches source exactly. Record counts, checksums, sample comparison. You
need to detect corruption before you decommission the source."

"CLASSIFICATION MAPPING - Their 'Confidential' might not match our
'Confidential.' Their column names might mask what's actually PII. Map
their schema and classifications to our standards."

"PERMISSION REVIEW - Their admin group shouldn't automatically become our
admin group. Review and adjust access controls for the new environment.
Migration shouldn't inherit inappropriate access."

"SOURCE SANITIZATION - When migration is verified complete, properly wipe
their old systems. Don't leave customer data on infrastructure you're
about to sell or scrap. This is a regulatory requirement, not optional."

"DOCUMENTATION - Complete audit trail. What was migrated, integrity
verification results, sanitization confirmation. You need this for
compliance and incident response."

"The timeline adjusts to accommodate these requirements. A fast bad
migration creates problems that take longer to fix than doing it right."

The PMO lead sighs. "So we're adding two weeks?"

"You're preventing six months of cleanup. Pick your timeline."

You've demonstrated DATA MIGRATION SECURITY principles.
                """,
                "failure_texts": {
                    0: """
"Business value depends on quick integration" is how you end up with:
- Corrupted customer records nobody notices for months
- PII in unprotected columns because classification wasn't mapped
- Former employees from the acquired company with admin access
- Customer data still sitting on servers you sold to a recycler

Rushed migrations create problems that take far longer to fix than a
proper migration would have taken. The business pressure doesn't eliminate
the security requirements - it just makes you pay for them later.
                    """,
                    2: """
"Let IT handle it" is how security gets relegated to cleanup duty.

Data migration has massive security implications:
- What data classifications apply to the migrated data?
- Who should have access in the new environment?
- What happens to the source systems after migration?
- How do you verify nothing was lost or corrupted?

IT can handle the technical migration. Security needs to be involved in
planning, verification, and sanitization. This isn't a technical matter -
it's a custody transfer of potentially sensitive data.
                    """,
                    3: """
"Keep copies as backup" sounds prudent but creates ongoing liability.

Those old systems will receive:
- Less attention (everyone's focused on the new environment)
- Fewer patches (why maintain infrastructure you're decommissioning?)
- Less monitoring (it's "backup," not production)

Meanwhile, they still contain customer PII, employee records, and
proprietary data. You've just created an unprotected data store that
will sit there accumulating risk.

The proper approach: verify migration completeness, THEN sanitize source
systems. Don't leave data in limbo.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 70,
        "hp_penalty": 25,
        "failure_text": """
Data migration security requirements:
- INTEGRITY: Verify data wasn't corrupted or lost in transfer
- CLASSIFICATION: Map source classifications to destination system
- ACCESS CONTROL: Review and adjust permissions for new environment
- SANITIZATION: Properly wipe source systems after verified migration
- DOCUMENTATION: Complete audit trail of migration process

Common migration failures:
- Data loss (corrupted or incomplete transfer)
- Classification mismatch (wrong protection levels)
- Orphan data (left on unsecured source systems)
- Permission inheritance (inappropriate access in new system)

Speed doesn't override security requirements.
        """,
        "domain_reference": "Domain 2: Asset Security - Data Migration, Integrity, Sanitization"
    }
]
