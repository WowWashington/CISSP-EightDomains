"""
Domain 6: Security Assessment and Testing scenarios.

Key CISSP concepts tested:
- Vulnerability Assessment vs Penetration Testing
- Security Audits
- Code Review and Analysis
- Security Metrics
- Red Team / Blue Team
- Compliance Testing
- Continuous Security Testing

Each scenario supports dual themes:
- Fantasy: Medieval/magical Citadel setting
- Corporate: Modern office satire (Office Space style)
"""

DOMAIN_6_SCENARIOS = [
    # Scenario 1: Vulnerability Assessment vs Penetration Testing
    {
        "id": "d6_castle_survey",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE CITADEL'S WEAKNESS SURVEY",
                "narrative": """
The Citadel Council has grown concerned about the fortress's defenses. Years of
peace have led to complacency, and whispers speak of forgotten vulnerabilities
in the outer walls and magical wards.

The High Commander approaches you with a delicate matter. "We must understand
our weaknesses," she says, "but the realm is at peace. I cannot have siege
engines battering our walls or war mages testing our barriers with actual
combat spells. The disruption would panic the citizenry and potentially
damage what we seek to protect."

She needs a comprehensive inventory of all defensive weaknesses - crumbling
stonework, degraded enchantments, gaps in patrol routes - but with minimal
risk of actual damage.

"How would you survey our defenses without actually attacking them?"
                """,
                "choices": [
                    {"text": "Conduct a full siege simulation with battering rams and war magic"},
                    {"text": "Survey and catalog all defensive weaknesses without testing them destructively"},
                    {"text": "Hire enemy infiltrators to test our defenses with real attacks"},
                    {"text": "Send spies to test the guards' susceptibility to bribery and deception"}
                ],
                "success_text": """
You organize teams of engineers, ward-inspectors, and veteran guards to
methodically survey every inch of the Citadel's defenses. They probe stones
for weakness, trace magical wards for degradation, and map patrol patterns
for gaps - all without swinging a single weapon or casting an offensive spell.

The resulting report is sobering but invaluable: forty-seven points of
potential failure, prioritized by severity and ease of exploitation. The
Council can now allocate resources for repairs based on actual risk.

"This is precisely what we needed," the High Commander nods approvingly.
"A complete picture of our vulnerabilities without the chaos of actual
assault. Now we can strengthen what matters most."

A VULNERABILITY ASSESSMENT identifies weaknesses through examination and
scanning without exploitation. When management needs comprehensive
visibility with minimal disruption, assessment is the right choice.
                """,
                "failure_texts": {
                    0: """
The siege simulation went exactly as feared. While your battering rams
identified three structural weaknesses in the eastern wall, they also
created two new ones. Three guards were injured. A section of the ward
matrix collapsed entirely when your war mages tested it.

Penetration testing with exploitation provides deeper validation but
carries higher risk of disruption. When management explicitly wants
minimal risk, a vulnerability assessment (scanning without exploitation)
is the appropriate choice.
                    """,
                    2: """
Hiring actual enemy infiltrators seemed clever until one of them decided
to actually defect - but to the other side. He took detailed maps of your
defenses back to his true masters. Red team exercises have their place,
but they carry inherent risks and weren't what management requested.

When the goal is understanding weaknesses with minimal disruption, a
vulnerability assessment provides comprehensive scanning without the
risks of actual exploitation attempts.
                    """,
                    3: """
Your social engineering test revealed that several guards could indeed
be bribed - but now those guards know they were tested and are either
resentful or fired. Meanwhile, you still don't know about the crumbling
section of the eastern wall or the failing ward crystals.

Social engineering tests evaluate people, not infrastructure. A
vulnerability assessment of the defenses themselves was what the
High Commander actually requested.
                    """
                }
            },
            "corporate": {
                "title": "THE SECURITY WEAKNESS REVIEW",
                "narrative": """
The quarterly board meeting left the CISO looking pale. "The board wants
to understand our security weaknesses," she explains during the emergency
team huddle. "But they're terrified of business disruption. Last year's
pen test took down the trading floor for two hours and nobody has
forgotten it."

She pulls up the email from the CEO: "Need comprehensive view of
vulnerabilities. ABSOLUTELY NO SYSTEM DISRUPTION. Quarterly numbers
depend on 100% uptime this month."

The security team looks at you. Someone has to figure out how to give
the board what they want without breaking anything.

"We need to map our weaknesses," the CISO continues, "but if we crash
production again, heads will roll. What approach do we take?"
                """,
                "choices": [
                    {"text": "Run a full penetration test with exploitation against production"},
                    {"text": "Conduct vulnerability scanning without exploitation attempts"},
                    {"text": "Bring in a red team for adversarial attack simulation"},
                    {"text": "Launch a social engineering campaign against the sales team"}
                ],
                "success_text": """
You schedule authenticated vulnerability scans during low-traffic windows,
carefully tuned to avoid aggressive probing that might destabilize services.
The scans identify missing patches, misconfigurations, and exposed services
without actually exploiting any of them.

The resulting report identifies 847 vulnerabilities across the environment,
categorized by severity and mapped to business-critical systems. The board
gets their comprehensive view. Production stays up. The CISO keeps her job.

"This is exactly what we needed," she says, reviewing the executive summary.
"Clear visibility into our risk posture without the drama. Schedule these
quarterly."

VULNERABILITY ASSESSMENT through scanning provides comprehensive weakness
identification with minimal disruption. Penetration testing validates
exploitability but carries higher risk - save it for when stakeholders
accept that risk.
                """,
                "failure_texts": {
                    0: """
The penetration test was thorough. It was also catastrophic. Your testers
found an exploitable vulnerability in the payment gateway - by exploiting
it. The payment system crashed for four hours during peak trading.

The board got their answer about vulnerabilities: you have them. They also
got a firsthand demonstration of why they didn't want active exploitation.
The CISO was asked to "pursue other opportunities."

When management explicitly requests minimal disruption, vulnerability
assessment (scanning without exploitation) is the appropriate approach.
                    """,
                    2: """
Red team exercises are excellent for testing detection and response, but
they're adversarial by nature. Your red team successfully exfiltrated
"sensitive data" (it was a test) but also triggered three real security
incidents, caused a P1 outage during their lateral movement, and gave the
SOC team collective PTSD.

The board wanted a quiet survey, not a war. Vulnerability assessment
would have provided the comprehensive view they requested without the
operational chaos.
                    """,
                    3: """
Your social engineering campaign revealed that 40% of sales staff would
click a phishing link. It also resulted in three HR complaints, one
lawsuit threat, and a very angry VP of Sales demanding to know why
you're "attacking my people."

More importantly, you still don't know anything about the technical
vulnerabilities in your infrastructure. Social engineering tests people;
the board asked about system weaknesses.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Vulnerability assessment and penetration testing serve different purposes.
Assessment identifies weaknesses through scanning and examination without
exploitation. Penetration testing actively exploits vulnerabilities to
prove impact. When minimal disruption is required, vulnerability assessment
provides comprehensive visibility with lower risk.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - Vulnerability Assessment"
    },

    # Scenario 2: Penetration Test Types (Black/White/Gray Box)
    {
        "id": "d6_siege_knowledge",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE SIEGE MASTER'S KNOWLEDGE",
                "narrative": """
The Citadel has hired the legendary Siege Master Valdris to test the fortress
defenses. Before he begins, the War Council must decide how much information
to provide him.

"This decision shapes the entire exercise," the High Commander explains.
"We could give him nothing - let him approach as a true enemy would, learning
our defenses only through reconnaissance. We could give him everything -
blueprints, ward specifications, guard schedules, patrol routes - so he can
find the deepest flaws. Or something in between."

The Council has chosen to provide Valdris with complete architectural plans
of the fortress, the magical specifications of every ward, access to the
guard rotation schedules, and even the emergency response procedures.

A young knight looks confused. "If we tell him everything, how is that a
real test?"

What type of siege test has the Council commissioned?
                """,
                "choices": [
                    {"text": "A black box test - the attacker knows nothing"},
                    {"text": "A white box test - the attacker has full knowledge"},
                    {"text": "A gray box test - the attacker has partial knowledge"},
                    {"text": "A blind test - no information is provided"}
                ],
                "success_text": """
"This is WHITE BOX testing," you explain to the knight. "By giving Siege
Master Valdris complete information, we enable him to find the deepest,
most subtle vulnerabilities. He won't waste time discovering what we
already know - he can focus on finding what we DON'T know."

The High Commander nods approvingly. "Exactly. A black box test simulates
the average enemy. But Valdris, with full knowledge, simulates the most
dangerous threat: an enemy with inside information. If he cannot breach
us, no one can."

The siege test proceeds with remarkable efficiency. Valdris identifies
seventeen vulnerabilities that external reconnaissance would never have
revealed, including a critical flaw in the ward matrix that only appears
under specific conditions documented in the specifications.

WHITE BOX (clear box) testing provides complete information to testers,
enabling thorough examination that time-limited black box testing might miss.
                """,
                "failure_texts": {
                    0: """
Black box testing provides NO information to the testers. They must
discover everything through reconnaissance, just as an external attacker
would. But the Council explicitly gave Valdris complete architectural
plans, ward specifications, and guard schedules.

With full information provided, this is WHITE BOX testing. Black box
would mean Valdris arrives knowing nothing about the Citadel's defenses.
                    """,
                    2: """
Gray box testing provides PARTIAL information - perhaps some network
diagrams but not source code, or user-level access but not admin
credentials. But the Council provided EVERYTHING: complete plans,
full specifications, all schedules.

This level of disclosure makes it WHITE BOX testing. Gray box would
involve withholding some significant information.
                    """,
                    3: """
"Blind testing" is similar to black box - no information provided to
testers. But the Council explicitly gave Valdris complete documentation
and access to all defensive specifications.

With full information disclosure, this is WHITE BOX (clear box) testing.
Blind/black box testing would mean starting with zero knowledge.
                    """
                }
            },
            "corporate": {
                "title": "THE PENETRATION TEST BRIEF",
                "narrative": """
Initech has contracted an external penetration testing firm for their annual
security assessment. The kickoff meeting gets interesting when the lead
tester asks about scope and knowledge.

"What information are you providing us?" asks the tester, pen ready.

The IT Director slides a stack of documents across the table. "Everything.
Network diagrams for all segments. System documentation. Source code for
our custom applications. Admin credentials for test accounts. Architecture
documents. Our security policies and procedures."

The tester's eyebrows rise. "That's... comprehensive."

"We want thorough results," the IT Director responds. "No point in paying
you to spend three weeks discovering what's in these documents."

A junior security analyst whispers to you, "Isn't giving them everything
kind of cheating? What kind of test is this?"

What type of penetration test has Initech commissioned?
                """,
                "choices": [
                    {"text": "Black box test - simulating an external attacker"},
                    {"text": "White box test - full knowledge and documentation provided"},
                    {"text": "Gray box test - partial information provided"},
                    {"text": "Blind test - testers have no advance information"}
                ],
                "success_text": """
"This is a WHITE BOX penetration test," you explain quietly. "Also called
clear box or crystal box testing. We're giving them full access to
documentation, source code, and architecture."

The junior analyst still looks skeptical. You continue: "Think about it.
A black box test means they spend days on reconnaissance, finding things
we already know. With white box, they skip straight to finding what we
DON'T know. It's more thorough, not less."

The test proves your point. With source code access, the testers find
three critical vulnerabilities in custom code that no amount of black
box probing would have uncovered. The architecture review identifies
design flaws that only manifest under specific conditions.

"Best ROI we've gotten from a pen test," the IT Director says at the
readout. "Turns out giving them the blueprints helps them find the
real problems."

WHITE BOX testing enables thorough examination of known systems,
finding deeper issues that time-limited black box testing often misses.
                """,
                "failure_texts": {
                    0: """
Black box testing simulates an external attacker with NO prior knowledge.
Testers must discover everything through reconnaissance and enumeration.
But Initech explicitly provided network diagrams, source code, credentials,
and complete documentation.

With full information provided, this is WHITE BOX testing. Black box
would mean the testers start with zero knowledge of Initech's environment.
                    """,
                    2: """
Gray box testing provides PARTIAL knowledge - perhaps user-level access
but not admin credentials, or network diagrams but not source code.
But Initech provided EVERYTHING: complete diagrams, full source code,
admin credentials, and all documentation.

This level of disclosure defines WHITE BOX testing. Gray box implies
significant information was withheld.
                    """,
                    3: """
Blind testing means testers receive no advance information about the
target. This is similar to black box testing. But Initech's IT Director
explicitly provided complete documentation, source code, and credentials.

With full knowledge provided, this is WHITE BOX testing. Blind/black
box testing would begin with zero information about the environment.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Penetration test types are defined by the knowledge provided to testers:
- Black box: No information (simulates external attacker)
- White box: Full information (documentation, source code, credentials)
- Gray box: Partial information (some access/knowledge)

When testers receive complete documentation and access, it's white box testing.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - Penetration Testing Types"
    },

    # Scenario 3: Vulnerability Scanning
    {
        "id": "d6_ward_scan",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE WARD INSPECTOR'S DILEMMA",
                "narrative": """
The Citadel's Ward Inspector bursts into your office, looking distressed.
Her magical detection crystals have completed their monthly scan of the
fortress's protective enchantments, and the results are troubling.

"Five hundred critical ward failures!" she exclaims, spreading the
parchment across your desk. "If this is true, the entire Citadel is
essentially unprotected!"

You examine the report more closely. The scan flagged wards as "failed"
based on energy signature patterns. But as you review specific entries,
something seems off. Ward 247 in the Eastern Tower is flagged as failed,
but you inspected it personally last week - it was functioning perfectly.
You check three more "critical failures" and find the same issue.

"I manually verified some of these," you tell the Inspector. "They're
working fine. I think your detection crystals are misfiring."

"But there ARE real failures in here!" she protests. "What do we do with
these results?"

What is the appropriate response to this vulnerability scan report?
                """,
                "choices": [
                    {"text": "Report all 500 critical findings as genuine ward failures"},
                    {"text": "Discard the entire scan since the crystals are clearly unreliable"},
                    {"text": "Validate findings manually and tune the detection crystals to reduce false positives"},
                    {"text": "Only address the failures that seem most dangerous based on location"}
                ],
                "success_text": """
"We need to do both things," you tell the Inspector. "First, manually
validate a sample of these findings to separate the real failures from
the false alarms. Then, we tune your detection crystals to reduce the
noise."

The validation effort reveals that 400 of the 500 findings were false
positives - wards functioning normally but triggering detection due to
crystal calibration issues. But critically, 100 findings were REAL ward
failures that needed immediate attention.

By tuning the detection crystals with the validation data, future scans
become far more accurate. The Ward Inspector can now trust her results.

"Thank you," she says, recalibrating her equipment. "I was so
overwhelmed by the volume that I didn't know where to start. Validation
and tuning - I should have known."

VULNERABILITY SCAN VALIDATION is essential. False positives waste effort;
false negatives create risk. Validate findings and tune scanners for
improved accuracy over time.
                """,
                "failure_texts": {
                    0: """
Reporting all 500 findings as genuine sends remediation teams chasing
400 non-existent problems. The real 100 failures get lost in the noise.
Resources are wasted. Credibility is destroyed when teams discover
they're "fixing" working systems.

Vulnerability scan results REQUIRE validation. Reporting unvalidated
findings undermines the entire program and wastes organizational resources.
                    """,
                    1: """
Discarding the entire scan throws out 100 REAL ward failures along with
the 400 false positives. The baby goes out with the bathwater. Those
100 genuine vulnerabilities remain unaddressed.

False positives don't invalidate an entire scan. The proper response
is validation to identify real issues and tuning to improve future
scan accuracy.
                    """,
                    3: """
"Seems most dangerous" is subjective judgment, not evidence-based
analysis. Location might matter, but you can't know which failures are
real without validation. You might address false positives while
ignoring real critical failures in "unimportant" locations.

Validation provides factual basis for prioritization. Proper tuning
then improves future scan accuracy.
                    """
                }
            },
            "corporate": {
                "title": "THE VULNERABILITY SCAN DISASTER",
                "narrative": """
Friday afternoon. Your vulnerability management tool just completed its
quarterly scan of the production environment. The dashboard lights up
like a Christmas tree of doom: 500 CRITICAL vulnerabilities detected.

You start drilling into the results. The first critical finding claims
your main web server is running an ancient version of Apache with a
known remote code execution vulnerability. But you personally patched
that server last week. You check - it's running the latest version.

Curious, you validate a few more "critical" findings. Same story.
The scanner is detecting vulnerabilities that don't actually exist on
these systems - version detection gone wrong, perhaps.

But not ALL the findings are false. Some of these criticals are real.
The scanner has identified genuine issues mixed in with the noise.

Your manager leans over your shoulder. "500 criticals? We're going
to have to work the weekend. Unless... what's the deal with these
results?"

What do you recommend?
                """,
                "choices": [
                    {"text": "Report all 500 as genuine critical vulnerabilities to management"},
                    {"text": "Ignore the entire scan since it is clearly unreliable"},
                    {"text": "Validate the findings and tune the scanner to reduce false positives"},
                    {"text": "Only fix the vulnerabilities that seem most dangerous"}
                ],
                "success_text": """
"Hold off on the weekend war room," you tell your manager. "These
results need validation first. I've already found significant false
positives."

You spend Friday evening validating a representative sample. The
results are telling: 400 false positives (version detection failures,
configuration differences the scanner didn't understand) and 100
genuine critical vulnerabilities that absolutely need remediation.

Monday morning, you present the validated findings with a plan:
immediate patching for the 100 real criticals, and scanner tuning
(credential configuration, updated plugins, exception rules) to
reduce false positives in future scans.

"This is how vulnerability management should work," your manager
nods. "Validated findings we can trust, not raw scanner output that
buries us in noise. Good work."

VALIDATE vulnerability scan results. FALSE POSITIVES waste resources
and destroy credibility. TUNE scanners based on validation data to
improve accuracy over time.
                """,
                "failure_texts": {
                    0: """
You reported 500 critical vulnerabilities. Remediation teams scrambled.
Weekend overtime was authorized. By Tuesday, teams had verified that
400 of your "criticals" were false positives. Real criticals got lost
in the rush. Your credibility with the infrastructure team is shot.

"Next time," your manager says coldly, "validate before you report."

Vulnerability scan results REQUIRE validation before reporting.
Unvalidated findings waste resources and destroy program credibility.
                    """,
                    1: """
You threw away a scan that contained 100 REAL critical vulnerabilities
because it also had false positives. Those 100 genuine issues remain
unpatched. Three weeks later, one of them gets exploited.

"Why wasn't this in the scan?" the CISO demands during the incident
review.

"It was," you admit. "I discarded the whole scan because of false
positives."

False positives don't invalidate a scan. Validate findings and tune
the scanner - don't throw out the baby with the bathwater.
                    """,
                    3: """
"Seem most dangerous" based on what? Gut feeling? Without validation,
you don't know which findings are real. You might patch false positives
while ignoring genuine criticals because they "seemed" less urgent.

The scan contained 100 real criticals and 400 false positives. Random
prioritization without validation is security theater, not risk
management. Validate first to establish facts.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Vulnerability scan results require validation. False positives are common
due to version detection limitations, configuration differences, or
scanner limitations. Proper validation confirms actual vulnerabilities.
Scanner tuning (credentials, updated plugins, exclusions) improves
future accuracy. Neither blind acceptance nor complete rejection is
appropriate.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - Vulnerability Scanning"
    },

    # Scenario 4: Security Audit Types
    {
        "id": "d6_independent_audit",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE INDEPENDENT INSPECTION",
                "narrative": """
The Merchant Guild Confederation has issued new requirements for all
trading houses that handle inter-kingdom gold transfers. Among the
regulations is a mandate for annual security inspections.

The key requirement reads: "All trading houses shall undergo annual
security inspection by parties with no vested interest in the findings."

Your trading house has received this mandate. The Guild Master gathers
the leadership to discuss compliance.

"We have options," he explains. "Our own security wardens could inspect
our vaults. The vault managers could assess their own protections.
Fellow trading houses could review each other. Or we could bring in
the independent Inspection Guild from across the sea."

The Chief Treasurer frowns. "Independent inspectors are expensive. Can't
our own security wardens do this? They know our systems better than any
outsider."

What type of inspection satisfies the "no vested interest" requirement?
                """,
                "choices": [
                    {"text": "Internal inspection by your own security wardens"},
                    {"text": "Self-assessment by the vault managers themselves"},
                    {"text": "Independent third-party inspection by the Inspection Guild"},
                    {"text": "Peer review by another trading house in the Confederation"}
                ],
                "success_text": """
"The regulation requires 'no vested interest in the findings,'" you
explain. "That means inspectors who don't benefit from favorable
results. Our wardens work for us. Vault managers assess their own work.
Fellow trading houses compete with us - they might benefit from our
failure."

You continue: "Only the independent Inspection Guild from across the
sea meets the requirement. They have no stake in our success or failure.
Their reputation depends on honest assessment, not on pleasing us."

The Guild Master nods slowly. "Expensive, but necessary. The regulation
is clear - we need true independence."

The Inspection Guild's assessment is thorough and objective. Their
recommendations improve security without the bias that internal
reviews often carry.

THIRD-PARTY AUDITS provide organizational independence. When regulations
require "no vested interest," this means external auditors who don't
benefit from favorable findings.
                """,
                "failure_texts": {
                    0: """
Your internal security wardens work for the trading house. Their
performance reviews, pay, and job security depend on favorable results.
If they find major failures, it reflects poorly on their own work.
This is the definition of "vested interest."

"No vested interest" requires auditors who are organizationally
independent - third parties with no stake in the outcome.
                    """,
                    1: """
Vault managers assessing their own vaults is the most vested interest
possible. They designed the protections, implemented them, and would
be blamed for failures. Self-assessment is valuable for improvement
but cannot satisfy independence requirements.

Third-party auditors with no organizational relationship are required
when regulations mandate "no vested interest."
                    """,
                    3: """
Peer review by competing trading houses seems independent, but creates
a different conflict. Competitors might benefit from undermining your
reputation, or might go easy hoping for reciprocal treatment. Either
way, they have vested interests.

True independence requires parties with NO organizational, competitive,
or reciprocal relationships that could influence findings.
                    """
                }
            },
            "corporate": {
                "title": "THE AUDIT REQUIREMENT",
                "narrative": """
Initech's compliance team has been reviewing new regulatory requirements.
The latest mandate from the Financial Services Authority is clear:
"Annual security audits must be performed by parties with no vested
interest in the findings."

The CFO gathers the leadership team to discuss options and costs.

"We have our internal audit department," she begins. "They're qualified
and already on payroll. We also have the security team who could do a
self-assessment. Our sister company across the street offered to
review us if we review them. Or we could pay Big Four prices for an
external firm."

The CEO winces at the budget numbers. "Those external auditors want
$200,000. Internal audit is free. Can't we just use our own people?"

What type of audit satisfies the "no vested interest" regulatory
requirement?
                """,
                "choices": [
                    {"text": "Internal audit by the company's audit department"},
                    {"text": "Self-assessment by the security team"},
                    {"text": "Independent third-party audit by an external firm"},
                    {"text": "Peer review by the sister company"}
                ],
                "success_text": """
"The regulation specifically requires 'no vested interest,'" you
explain. "That's a legal term that means organizational independence.
Our internal audit reports to our board. The security team would be
assessing their own work. The sister company has business relationships
with us."

The CFO looks pained but understanding. "So only external auditors
qualify."

"Correct. External audit firms stake their reputation and licensing
on independence. They have no financial or career stake in our
results. That's what the regulation demands."

The external audit is expensive but produces defensible results.
When regulators ask, Initech can demonstrate true independence.
The $200,000 is cheaper than regulatory fines for non-compliance.

THIRD-PARTY AUDITS satisfy independence requirements. External
auditors have no organizational stake in results and stake their
professional reputation on objectivity.
                """,
                "failure_texts": {
                    0: """
Internal audit, while independent of operations, still works for
the company. Their paychecks come from Initech. Their career
advancement depends on Initech. If they find catastrophic failures,
it reflects on their employer - they have vested interest.

"No vested interest" in regulatory terms means organizational
independence. Only external third-party auditors qualify.
                    """,
                    1: """
Self-assessment is literally the most vested interest possible. The
security team assessing their own security program is like grading
your own test. They designed it, implemented it, and would be blamed
for failures.

Regulatory independence requirements specifically exist because
self-assessment, while valuable internally, cannot be trusted for
compliance purposes.
                    """,
                    3: """
The sister company has business relationships with Initech. Shared
resources, intercompany transactions, common ownership - all create
vested interests. They might go easy expecting reciprocal treatment,
or might be too harsh for competitive reasons.

"No vested interest" means NO organizational, financial, or
reciprocal relationships that could bias findings.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
"No vested interest" requires organizational independence. Internal
auditors work for the organization. Self-assessors evaluate their own
work. Peer reviewers may have competitive or reciprocal relationships.
Only independent third-party auditors - external firms with no stake
in the outcome - satisfy strict independence requirements.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - Security Audits"
    },

    # Scenario 5: Log Review
    {
        "id": "d6_night_watch_log",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE NIGHT WATCH ANOMALY",
                "narrative": """
As the Citadel's log analyst, you begin your morning review of the night
watch records. The Watch Commander's magical ledger automatically records
every gate passage, every guard challenge, and every authentication at
the treasury and armory.

One entry immediately catches your eye. Guard Captain Aldric's sigil was
used to authenticate access to the treasury vault, the armory, and the
records chamber - all within a single hour between 3 AM and 4 AM. The
ledger shows 2,847 failed authentication attempts before each successful
entry.

This is concerning for several reasons. Aldric works the day shift. He
has never worked the night watch in his twenty years of service. And
the volume of failed attempts suggests something other than a forgotten
passphrase.

The Watch Commander asks for your assessment of these log entries.
What do these patterns most likely indicate?
                """,
                "choices": [
                    {"text": "Normal automated guard patrol system activity"},
                    {"text": "Captain Aldric forgot his authentication phrases and kept trying"},
                    {"text": "Possible credential compromise or brute force attack"},
                    {"text": "A malfunction in the magical ledger recording system"}
                ],
                "success_text": """
"This pattern indicates credential compromise or brute force attack,"
you report. "Consider the evidence: thousands of failed attempts
before success suggests either credential stuffing - trying stolen
credentials - or brute force password guessing. The 3 AM timing, when
Aldric never works, suggests an attacker operating when they assumed
no one would notice."

The Watch Commander immediately suspends Aldric's access and summons
him for questioning. Investigation reveals that Aldric's sigil token
was stolen during a visit to the Night Market district. An infiltrator
had been using magical tools to guess authentication codes.

Thanks to the log analysis, the breach is contained before significant
damage occurs. New authentication protocols are implemented.

LOG ANALYSIS identifies security incidents through pattern recognition.
Mass failed attempts followed by success, off-hours activity, and
unusual access patterns are strong indicators of credential compromise
or active attack.
                """,
                "failure_texts": {
                    0: """
Automated patrol systems use SERVICE sigils, not personal guard
credentials. They also don't fail authentication thousands of times
before succeeding. Legitimate automation doesn't generate this
pattern of errors.

Mass failed attempts from a single account, at unusual hours, across
multiple sensitive locations indicates attack activity, not normal
operations.
                    """,
                    1: """
If Aldric forgot his passphrase, he would fail a few times and then
seek help resetting it. 2,847 failed attempts across THREE different
secure locations in one hour? That's not forgetfulness - that's an
automated attack tool systematically guessing credentials.

This pattern strongly indicates brute force attack or credential
stuffing. Immediate investigation is required.
                    """,
                    3: """
Ledger malfunctions don't generate failed authentication events. A
malfunction might lose entries, corrupt records, or show impossible
timestamps - not create thousands of false failed attempts followed
by successful access to real locations.

These log entries describe real authentication attempts. The pattern
indicates attack activity, not equipment failure.
                    """
                }
            },
            "corporate": {
                "title": "THE 3 AM LOG ANOMALY",
                "narrative": """
Monday morning. You're the first one in the SOC, coffee in hand,
starting the daily log review. The SIEM dashboard shows something
that immediately grabs your attention.

The account "jsmith" - belonging to Jennifer Smith in Accounting -
generated 3,412 failed login attempts across the domain controller,
file servers, and email gateway between 3 AM and 4 AM Sunday morning.
After the failures, successful authentications occurred.

You check Jennifer's schedule. She's strictly 9-to-5. No record of
working weekends, ever. No VPN connection from her home. The login
attempts came from an IP address in Eastern Europe.

Your manager walks in. "Anything interesting from the weekend logs?"

What does this pattern most likely indicate?
                """,
                "choices": [
                    {"text": "Normal automated system activity using her account"},
                    {"text": "Jennifer forgot her password and kept trying until it worked"},
                    {"text": "Possible credential compromise or brute force attack"},
                    {"text": "A logging system malfunction generating false events"}
                ],
                "success_text": """
"We have a potential credential compromise," you report, already
pulling up additional details. "3,400 failed attempts isn't password
forgetfulness - that's an automated attack. The 3 AM timing when no
one's watching, the Eastern European IP, the fact that Jennifer
never works weekends - this is either credential stuffing or brute
force."

Your manager goes pale. "Lock the account. Now."

The investigation confirms your analysis. Jennifer's credentials
were found in a breach dump from another site where she reused her
password. Attackers were attempting to use them across Initech's
infrastructure.

Thanks to rapid detection, the attackers gained no access beyond
initial authentication. Jennifer's password is reset, and a
company-wide password reset and MFA rollout is expedited.

LOG ANALYSIS catches attacks. Mass failed logins from unusual
sources at unusual times are classic indicators of credential
compromise or brute force attacks.
                """,
                "failure_texts": {
                    0: """
Automated systems use SERVICE ACCOUNTS, not user credentials.
They also don't fail thousands of times before succeeding. No
legitimate automation pattern looks like this.

User account + mass failures + unusual hours + foreign IP = attack,
not normal operations. This requires immediate investigation.
                    """,
                    1: """
Forgetting a password causes a few failed attempts, then a password
reset request. 3,412 failed attempts from an IP in Eastern Europe
at 3 AM on a Sunday? That's an automated attack tool, not a confused
employee.

This pattern indicates credential stuffing (trying stolen credentials)
or brute force attack. Jennifer's credentials have been compromised.
                    """,
                    3: """
Logging systems don't generate fake failed authentication events.
A malfunction might drop logs, corrupt timestamps, or create
impossible entries - not fabricate thousands of sequential failed
login attempts that match a known attack pattern.

These are real authentication attempts from a real IP address.
The pattern indicates active attack against Jennifer's credentials.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Log analysis reveals security incidents through pattern recognition.
Mass failed authentication attempts followed by success indicates
brute force attack or credential stuffing. Off-hours activity from
unusual sources raises additional suspicion. Legitimate automation
uses service accounts and doesn't fail repeatedly. Legitimate users
don't generate thousands of failed attempts.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - Log Analysis"
    },

    # Scenario 6: Static Code Analysis
    {
        "id": "d6_spell_scroll_review",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE SPELL SCROLL INSPECTION",
                "narrative": """
The Citadel's Arcane Development Guild has created a new batch of spell
scrolls - complex enchantments that will power the fortress's automated
defenses. Before these scrolls can be deployed to the ward towers, they
must be reviewed for safety.

The Guild Master approaches you with the scrolls. "My enchanters have
worked hard on these, but I'm concerned. One of our previous batches
contained a critical flaw that only manifested when the wards were
activated during a thunderstorm. We nearly lost the entire eastern tower."

"We need to find these kinds of problems BEFORE the scrolls are deployed,"
he continues. "But we can't just activate every scroll to test it - some
of these enchantments would level the practice grounds. Is there a way
to examine the spell patterns themselves, without actually casting the
spells?"

What approach should be used to find vulnerabilities in the spell scrolls
before they are deployed and activated?
                """,
                "choices": [
                    {"text": "Cast each spell in the practice grounds to see what happens"},
                    {"text": "Analyze the spell patterns and rune sequences without casting them"},
                    {"text": "Deploy them to production and monitor for problems"},
                    {"text": "Test how long the spells take to cast under heavy load"}
                ],
                "success_text": """
"We can examine the spell patterns directly," you explain. "A trained
ward analyst can trace the rune sequences, identify dangerous pattern
combinations, and find logical flaws - all without actually casting
a single spell."

You arrange for the Citadel's senior ward analysts to review the
scrolls. Using pattern-recognition techniques, they trace energy
flows, check for forbidden rune combinations, and verify that fail-safe
sequences are properly integrated.

"Found it," one analyst announces, pointing to a scroll. "This
amplification loop has no termination condition. If cast, it would
draw power until the caster collapsed. Good catch BEFORE deployment."

The flaw is corrected in the source patterns. The scrolls are
rewritten safely.

STATIC CODE ANALYSIS examines code without executing it. By analyzing
patterns, logic, and structure, vulnerabilities can be found early -
before the dangerous consequences of execution.
                """,
                "failure_texts": {
                    0: """
Casting spells to find problems is DYNAMIC testing - testing through
execution. The Guild Master specifically asked about finding problems
WITHOUT activating the spells, because some of them could "level the
practice grounds."

STATIC ANALYSIS examines the spell patterns (code) without execution.
This finds vulnerabilities early, before the consequences manifest.
                    """,
                    2: """
"Deploy and monitor" is the most dangerous approach possible. You'd
put potentially flawed enchantments into production and wait for
failures. Given that the last flaw "nearly lost the entire eastern
tower," this approach risks catastrophic damage.

Testing should occur BEFORE deployment. Static analysis examines
code without execution, finding problems when they're cheap to fix.
                    """,
                    3: """
Testing casting time under load is PERFORMANCE testing, not security
testing. It measures how long spells take, not whether they have
dangerous flaws in their logic.

The Guild Master needs to find security vulnerabilities in the spell
patterns - logical flaws, dangerous combinations, missing safeguards.
Static analysis examines the patterns directly, without execution.
                    """
                }
            },
            "corporate": {
                "title": "THE PRE-DEPLOYMENT CODE REVIEW",
                "narrative": """
The development team has just finished a sprint on a critical new
payment processing module. Before it can go to production, the security
team needs to review it for vulnerabilities.

The lead developer is anxious. "We're already behind schedule. The
product manager is asking for deployment by Friday."

The security architect reviews the timeline. "Traditional pen testing
takes weeks. But we need to find security issues - SQL injection,
hardcoded credentials, buffer overflows - before this code touches
production."

"Is there a way to scan the code itself?" the developer asks. "Without
deploying it anywhere, without running it? We have the source right
here. Can we analyze it directly?"

What type of security testing examines source code without executing
the application?
                """,
                "choices": [
                    {"text": "Dynamic Application Security Testing (DAST)"},
                    {"text": "Static Application Security Testing (SAST)"},
                    {"text": "Penetration testing"},
                    {"text": "Stress testing"}
                ],
                "success_text": """
"Static Application Security Testing - SAST," you confirm. "It
analyzes source code directly, without running the application.
We can scan for SQL injection patterns, hardcoded secrets,
unsafe function calls, and buffer overflow conditions just by
examining the code."

You integrate a SAST tool into the CI/CD pipeline. Within an hour,
it identifies three instances of SQL string concatenation vulnerable
to injection, one hardcoded API key in a configuration file, and
several uses of deprecated cryptographic functions.

"Found and fixed before anyone outside this room knew about them,"
the developer says, making the corrections. "This should be part
of every sprint."

SAST finds vulnerabilities early, when they're cheap to fix. By
analyzing code without execution, it integrates into development
pipelines for continuous security feedback.
                """,
                "failure_texts": {
                    0: """
Dynamic Application Security Testing (DAST) tests RUNNING applications
by sending requests and analyzing responses. It requires the
application to be deployed and executed. The developer specifically
asked about analyzing code WITHOUT running it.

SAST (Static testing) analyzes source code without execution.
DAST (Dynamic testing) requires a running application.
                    """,
                    2: """
Penetration testing targets deployed, running systems. It tests
real applications in real environments through actual attack
simulation. This requires deployment, which defeats the purpose
of finding issues BEFORE deployment.

SAST analyzes source code without deployment, finding vulnerabilities
while they're still in development and cheap to fix.
                    """,
                    3: """
Stress testing evaluates performance under load - how many
transactions per second, what happens under peak traffic, etc.
It measures capacity and stability, not security vulnerabilities.

The team needs to find SQL injection, hardcoded credentials, and
other security flaws. SAST analyzes source code for these patterns
without requiring execution.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Static Application Security Testing (SAST) analyzes source code without
executing it. It finds vulnerabilities like SQL injection, buffer
overflows, and hardcoded credentials by examining code patterns. This
enables early detection during development, before deployment. Dynamic
testing (DAST) requires execution; penetration testing requires
deployment.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - Static Analysis"
    },

    # Scenario 7: Dynamic Testing (DAST)
    {
        "id": "d6_portal_testing",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE PORTAL'S ACTIVE DEFENSES",
                "narrative": """
The Citadel's new teleportation portal is nearly ready for deployment.
The Arcane Guild has reviewed the spell patterns (static analysis)
and found no obvious flaws in the enchantment design. But the Portal
Master isn't satisfied.

"The spell patterns look correct," she admits, "but portals are
complex. Problems emerge during actual operation. The authentication
sequence might have flaws that only manifest when someone actually
attempts passage. Session binding might break under specific conditions.
Configuration errors might leave backdoors that analysis can't detect."

She gestures at the shimmering gateway. "I need to test this portal
while it's RUNNING. Send actual magical requests through it. See how
it responds to malformed transport sequences. Check if the authentication
can be bypassed during active operation."

What testing approach examines the portal's security while it's actively
operating?
                """,
                "choices": [
                    {"text": "Review the portal's enchantment diagrams again more carefully"},
                    {"text": "Test the running portal by sending requests and analyzing responses"},
                    {"text": "Have scholars study the portal's design documentation"},
                    {"text": "Analyze the portal's original architectural blueprints"}
                ],
                "success_text": """
"We need DYNAMIC testing," you explain. "We send actual transport
requests through the active portal - properly formed, malformed,
malicious - and observe how it responds. We test authentication
bypass, session manipulation, and configuration weaknesses in the
running system."

A team of ward testers is assembled. They attempt to transport
without proper credentials. They send malformed destination sequences.
They probe for configuration weaknesses. All against the RUNNING
portal.

"Found it!" a tester calls out. "If you send a partial authentication
followed immediately by a valid request, the session binding fails.
You could potentially hijack another traveler's destination."

The flaw exists only during runtime - static analysis would never
have found it. The dynamic testing caught it before deployment.

DYNAMIC APPLICATION SECURITY TESTING (DAST) tests running systems
by sending requests and analyzing responses. It finds runtime
vulnerabilities that static analysis misses.
                """,
                "failure_texts": {
                    0: """
Reviewing the enchantment diagrams is STATIC analysis - examining
the code/design without execution. The Portal Master specifically
noted that static analysis was already completed and wanted to test
the portal "while it's RUNNING."

Dynamic testing examines active systems through interaction, finding
runtime vulnerabilities that static analysis cannot detect.
                    """,
                    2: """
Studying documentation is design review, not security testing. It
examines plans and intentions, not actual implementation and behavior.
Documents might say one thing while the running system does another.

The Portal Master needs to test the OPERATIONAL portal - how it
actually responds to requests. That requires dynamic testing against
the running system.
                    """,
                    3: """
Architectural blueprints describe intended design, not actual
implementation. They might specify perfect authentication, but
the running portal might have misconfigured it. Static analysis
of plans doesn't reveal runtime behavior.

Dynamic testing sends actual requests to the running system,
discovering how it actually behaves rather than how it was
designed to behave.
                    """
                }
            },
            "corporate": {
                "title": "THE RUNNING APPLICATION TEST",
                "narrative": """
The new web application has passed code review and static analysis.
The security team signed off on the source code examination. But the
application security architect wants one more round of testing.

"SAST found the coding issues," she explains, "but some vulnerabilities
only manifest at runtime. Authentication bypass that depends on session
state. Configuration errors that leave debug endpoints exposed.
Race conditions that only appear under real traffic patterns."

She pulls up the staging environment on her screen. "The application
is deployed and running. I need to test it AS a running application -
send it requests, probe its authentication, check its session
management, find configuration errors."

"But we already reviewed the code," the project manager protests.

"Code review tells us what the developers WROTE. I need to know
what the running application actually DOES."

What type of testing examines security in a running web application?
                """,
                "choices": [
                    {"text": "Review the application source code again"},
                    {"text": "Perform dynamic application security testing (DAST)"},
                    {"text": "Conduct a code review meeting"},
                    {"text": "Analyze the application design documents"}
                ],
                "success_text": """
"Dynamic Application Security Testing - DAST," you confirm. "We
test the running application by actually interacting with it.
Send HTTP requests, probe authentication endpoints, test session
management, look for exposed configuration."

The DAST tool crawls the running application, finds all endpoints,
and begins probing. Within hours, it identifies issues that code
review missed:

- An authentication bypass when session cookies are manipulated
- A debug endpoint accidentally exposed in the staging config
- Session fixation vulnerability in the login flow

"None of these were visible in the code," the architect notes.
"They emerged from configuration, deployment, and runtime behavior.
This is why we test running applications."

DAST tests running applications through interaction, finding
runtime vulnerabilities that static analysis cannot detect.
                """,
                "failure_texts": {
                    0: """
The scenario explicitly states that source code review (SAST) was
already completed. The architect is asking for something different:
testing the RUNNING application to find vulnerabilities that only
manifest during execution.

DAST tests running applications. SAST examines code without
execution. The architect already has static results.
                    """,
                    2: """
A code review meeting examines source code - that's static analysis.
The scenario notes that static analysis is complete. The architect
wants to test what the running application "actually DOES."

Dynamic testing interacts with the deployed, running application
to find runtime vulnerabilities invisible in code.
                    """,
                    3: """
Design documents describe intended behavior, not actual behavior.
The running application might deviate from design in ways that
create vulnerabilities. Documents don't catch configuration
errors, runtime issues, or deployment problems.

DAST tests the actual running application through interaction,
discovering what it actually does rather than what it was
designed to do.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Dynamic Application Security Testing (DAST) tests running applications
by sending requests and analyzing responses. It finds runtime
vulnerabilities like authentication bypasses, session management
flaws, and configuration errors that static analysis cannot detect.
DAST requires a deployed, running application; SAST analyzes code
without execution.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - DAST"
    },

    # Scenario 8: Compliance Testing
    {
        "id": "d6_guild_certification",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE MERCHANT GUILD CERTIFICATION",
                "narrative": """
The Citadel serves as a central hub for gold transfers between the
Five Kingdoms. The Inter-Kingdom Merchant Confederation has established
strict standards for any fortress that handles such transfers - the
Gold Transfer Security Standards (GTSS).

The annual certification deadline approaches. Your trading house must
demonstrate adherence to GTSS requirements: specific vault construction
standards, guard rotation protocols, magical ward specifications, and
record-keeping procedures.

A young apprentice suggests various testing approaches. "Should we
scan for vulnerabilities? Test our performance under heavy load? Check
if our vaults are easy to use?"

The Chief Treasurer sighs. "Those are all fine activities, but they
won't satisfy the Confederation. We need to prove we meet GTSS
specifically. Every requirement. Every control. Documented and verified."

What type of assessment demonstrates adherence to GTSS requirements?
                """,
                "choices": [
                    {"text": "General vulnerability scanning of the vaults"},
                    {"text": "GTSS compliance assessment/audit"},
                    {"text": "Performance load testing during peak transfer hours"},
                    {"text": "Usability assessment of vault access procedures"}
                ],
                "success_text": """
"We need a GTSS COMPLIANCE ASSESSMENT," you explain to the apprentice.
"It's specifically designed to verify adherence to the Confederation's
requirements. Each GTSS control is evaluated: do we meet it or not?
Is there evidence? Is it documented?"

You engage certified GTSS assessors who methodically work through
every requirement. Vault construction: verified against specifications.
Guard protocols: observed and documented. Ward standards: measured
and certified. Records: audited for completeness.

The assessment produces a detailed report mapping your controls to
GTSS requirements, with evidence of compliance for each. The
Confederation accepts your certification.

"General security testing is valuable," the assessor notes, "but
compliance assessment specifically verifies adherence to a particular
standard's requirements. That's what regulators need."

COMPLIANCE ASSESSMENTS verify adherence to specific regulatory or
standard requirements, mapping controls to specifications.
                """,
                "failure_texts": {
                    0: """
General vulnerability scanning identifies weaknesses but doesn't map
to specific GTSS requirements. You might have excellent scan results
while still failing multiple GTSS controls. The Confederation doesn't
accept "our vulnerability scan was clean" as proof of compliance.

Compliance assessment specifically evaluates each GTSS requirement
and documents adherence.
                    """,
                    2: """
Performance load testing measures capacity and speed - how many
transfers per hour, response time under peak load. Valuable
operationally, but completely irrelevant to GTSS compliance.

GTSS specifies vault construction, guard protocols, and security
controls - not performance metrics. Compliance assessment verifies
adherence to the standard's actual requirements.
                    """,
                    3: """
Usability assessment evaluates how easy systems are to use. While
user experience matters operationally, GTSS doesn't care if your
vaults are easy to access - it cares if they're SECURE according
to specific standards.

Compliance assessment verifies that each required security control
is implemented according to the standard's specifications.
                    """
                }
            },
            "corporate": {
                "title": "THE PCI DSS DEADLINE",
                "narrative": """
Initech processes credit card payments. As a Level 2 merchant, they
must maintain PCI DSS compliance and produce an annual Self-Assessment
Questionnaire with supporting evidence.

The compliance deadline is in three weeks. The Compliance Manager is
organizing the assessment effort.

"We've done vulnerability scans," she reviews her checklist. "We've
tested our disaster recovery. We've done a nice usability study on
the checkout flow. But the QSA is going to ask about PCI DSS
requirements specifically. Do we encrypt cardholder data? Do we
have proper access controls? Are our network segments correctly
isolated?"

A junior analyst suggests just sending the vulnerability scan results.
"Those prove we're secure, right?"

The Compliance Manager shakes her head. "We need to demonstrate we
meet PCI DSS requirements specifically. That's not the same thing."

What type of assessment demonstrates PCI DSS compliance?
                """,
                "choices": [
                    {"text": "General vulnerability scan results"},
                    {"text": "PCI DSS compliance assessment/audit"},
                    {"text": "Performance load testing results"},
                    {"text": "Usability assessment of the checkout flow"}
                ],
                "success_text": """
"We need a PCI DSS COMPLIANCE ASSESSMENT," you explain. "It specifically
evaluates adherence to PCI DSS requirements. Each control from the
standard is checked: do we meet it, and where's the evidence?"

The assessment methodically works through PCI DSS requirements:

- Requirement 3: Is cardholder data encrypted at rest? Evidence?
- Requirement 7: Are access controls properly implemented? Proof?
- Requirement 11: Is vulnerability scanning performed quarterly? Logs?

Each requirement is evaluated, documented, and evidenced. The result
is a compliance report that the QSA can validate, showing exactly
how Initech meets each PCI DSS control.

"Vulnerability scans are ONE requirement," the Compliance Manager
notes. "PCI DSS has hundreds. Compliance assessment covers them all."

COMPLIANCE ASSESSMENT specifically verifies adherence to regulatory
or standard requirements with documented evidence for each control.
                """,
                "failure_texts": {
                    0: """
Vulnerability scanning is ONE component of PCI DSS (Requirement 11).
But PCI DSS has hundreds of requirements covering encryption, access
control, logging, policies, and more. A clean vulnerability scan
doesn't prove you meet encryption standards, access controls, or
data retention policies.

Compliance assessment evaluates ALL requirements from the standard,
not just one component.
                    """,
                    2: """
Performance load testing measures system capacity and speed. PCI DSS
doesn't care if your checkout can handle 10,000 transactions per
second - it cares whether you're protecting cardholder data according
to specific security requirements.

Compliance assessment verifies security controls, not performance
characteristics.
                    """,
                    3: """
Usability assessment evaluates user experience. PCI DSS requirements
focus on security, not convenience. A checkout flow that's easy to
use but transmits unencrypted cardholder data fails compliance.

Compliance assessment specifically evaluates security controls
against PCI DSS requirements, not user experience metrics.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Compliance assessments specifically evaluate adherence to regulatory or
standard requirements. They map organizational controls to specific
requirements and document evidence of compliance. General vulnerability
scanning, performance testing, and usability assessments serve other
purposes but don't demonstrate compliance with specific standards.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - Compliance Testing"
    },

    # Scenario 9: Security Metrics
    {
        "id": "d6_metrics_council",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE DEFENSE COUNCIL REPORT",
                "narrative": """
The Citadel's Defense Council has summoned you for a quarterly review.
They want to understand how effectively the fortress is managing its
defensive weaknesses - the crumbling walls, the fading wards, the
gaps in patrol coverage.

"We've invested significantly in remediation," the High Commander
states. "Stone masons, ward enchanters, additional guards. I need
to know: is it working? Are we actually fixing problems faster?"

The Chief Quartermaster suggests various metrics. "We could report
how many weaknesses we've discovered across all time. Or count our
new stoneworking tools. Or simply report how many guards we've hired."

But these don't seem to answer the Commander's question about
remediation EFFECTIVENESS.

Which metric BEST indicates how effectively you're addressing
defensive weaknesses?
                """,
                "choices": [
                    {"text": "Total number of weaknesses ever discovered in Citadel history"},
                    {"text": "Mean time to remediate critical defensive weaknesses"},
                    {"text": "Number of security tools and equipment purchased"},
                    {"text": "Size of the guard and maintenance force"}
                ],
                "success_text": """
"Mean time to remediate critical weaknesses," you report. "When we
identify a serious problem - a crumbling section of wall, a failing
ward crystal - how long does it take to fix it? This directly measures
remediation effectiveness."

You present the data: "Three moons ago, critical weaknesses took an
average of 45 days to address. After our investments, we're now at
22 days. Our remediation SPEED has doubled, meaning critical risks
are exposed for less time."

The High Commander nods with satisfaction. "Now THAT tells me
something useful. Not how many tools we bought, not how many guards
we hired - but whether we're actually fixing problems faster."

MEAN TIME TO REMEDIATE (MTTR) for critical vulnerabilities directly
measures remediation effectiveness. Lower MTTR means faster risk
reduction. This is an outcome metric, not an input metric.
                """,
                "failure_texts": {
                    0: """
Total discoveries across all time is historical volume, not current
performance. "We've found 10,000 weaknesses ever" says nothing about
whether you're fixing them. You could be finding problems and never
addressing them.

MTTR measures how quickly you address problems - that's remediation
effectiveness.
                    """,
                    2: """
Tool count is an INPUT metric - resources consumed. Having more
tools doesn't mean you're using them effectively. You could own
every stoneworking implement in the kingdom and still have
crumbling walls if you're not deploying them well.

MTTR is an OUTCOME metric - it measures results, not resources.
                    """,
                    3: """
Staff size is another INPUT metric. More guards and masons doesn't
automatically mean faster remediation. They could be poorly managed,
working on low-priority issues, or simply not deployed effectively.

The question is about effectiveness: are we FIXING problems faster?
MTTR answers that question directly.
                    """
                }
            },
            "corporate": {
                "title": "THE VULNERABILITY MANAGEMENT REVIEW",
                "narrative": """
The quarterly security review with the CISO. She wants to understand
how effective the vulnerability management program is.

"We've added headcount. We've bought new scanning tools. We've
increased our patch management budget by 40%," she lists. "But I
need EVIDENCE that we're actually performing better. Give me a
metric that shows our remediation effectiveness."

The security team offers suggestions:
- "We've found 50,000 vulnerabilities this year!"
- "We purchased three new scanning platforms!"
- "We hired four more vulnerability analysts!"

The CISO frowns. "Those tell me what we've spent and found. They
don't tell me if we're actually fixing things faster. What metric
shows our remediation PERFORMANCE?"
                """,
                "choices": [
                    {"text": "Total number of vulnerabilities ever discovered"},
                    {"text": "Mean time to remediate critical vulnerabilities"},
                    {"text": "Number of security tools purchased"},
                    {"text": "Size of the security team"}
                ],
                "success_text": """
"Mean time to remediate critical vulnerabilities," you respond.
"When we identify a critical CVE, how many days until it's patched?
That directly measures remediation effectiveness."

You pull up the dashboard. "Q1: average 34 days for critical
remediation. Q3: average 19 days. We've nearly cut our exposure
window in half. Critical vulnerabilities are fixed 44% faster
than six months ago."

The CISO nods. "Now THAT'S a meaningful metric. Not input metrics
like headcount and tool purchases - an outcome metric that shows
whether our investments are producing results. Keep tracking this."

MTTR (Mean Time to Remediate) for critical vulnerabilities is
the key effectiveness metric for vulnerability management. It
measures outcomes, not inputs, showing whether you're actually
reducing risk faster.
                """,
                "failure_texts": {
                    0: """
"Total vulnerabilities discovered" is a volume metric with no
context. Finding 50,000 vulnerabilities means nothing if you're
not fixing them. You could be discovering more while your backlog
grows infinitely.

MTTR measures how quickly you REMEDIATE - that's the effectiveness
the CISO asked about.
                    """,
                    2: """
Tool count is an INPUT metric. Buying three scanners doesn't
prove you're using them effectively. You could have the best
tools in the industry and still have a 200-day remediation
cycle if processes are broken.

MTTR is an OUTCOME metric showing actual remediation performance.
                    """,
                    3: """
Team size is an INPUT metric - resources consumed. Four new
analysts doesn't automatically mean faster remediation. They
could be onboarding, working on low-priority items, or stuck
in process bottlenecks.

The CISO asked about EFFECTIVENESS. MTTR shows whether problems
are actually being fixed faster, regardless of team size.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Mean Time to Remediate (MTTR) for critical vulnerabilities measures how
quickly dangerous issues are fixed - directly indicating remediation
effectiveness. This is an OUTCOME metric showing actual performance.
Input metrics like tool count, team size, or total discoveries don't
indicate whether you're actually reducing risk. Lower MTTR = faster
risk reduction.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - Security Metrics"
    },

    # Scenario 10: Red Team vs Blue Team
    {
        "id": "d6_war_games",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE CITADEL WAR GAMES",
                "narrative": """
The Citadel's annual defense review has arrived. The War Council wants
to test not just the fortress walls and wards, but also the defenders
themselves. Can the guard force detect intrusions? Can they respond
effectively? Do their communication procedures work under pressure?

The Master of Defense presents his proposal: "I suggest we form two
teams. The CRIMSON team will attempt to infiltrate the Citadel and
reach the treasury, using whatever tactics they can devise. The
AZURE team - our regular guard force - will try to detect, respond,
and stop them."

A skeptical council member objects. "We already run automated ward
scans. Why do we need humans pretending to attack?"

The Master of Defense smiles. "Scans test our magical barriers. This
tests our PEOPLE - whether they can actually detect and respond to
a thinking adversary."

What type of exercise tests both technical defenses AND defender
capabilities?
                """,
                "choices": [
                    {"text": "Automated vulnerability scanning"},
                    {"text": "Red team vs blue team exercise"},
                    {"text": "Policy documentation review"},
                    {"text": "Control self-assessment questionnaire"}
                ],
                "success_text": """
"RED TEAM versus BLUE TEAM exercise," you confirm. "The red team
simulates adversaries, attempting to achieve objectives. The blue
team - the defenders - tries to detect, respond, and stop them.
It tests both technical controls AND human response capabilities."

The exercise begins at dawn. The Crimson team (red) attempts
infiltration through multiple vectors - the water gate, the old
servant passage, even social engineering of a new guard. The Azure
team (blue) monitors wards, patrols, and responds to alerts.

After three days, the results are illuminating. The red team found
two physical access points that bypassed magical wards. But more
importantly, the blue team's response revealed communication gaps -
warnings from the eastern tower took too long to reach central
command.

"Automated scans would never have found these human factors," the
Master of Defense concludes. "Red vs blue tests the whole system."
                """,
                "failure_texts": {
                    0: """
Automated vulnerability scanning tests TECHNICAL controls - wards,
barriers, detection crystals. It doesn't test whether the guards
can actually detect and respond to a thinking attacker. Scanners
don't probe human procedures, communication, or response capability.

Red team vs blue team exercises test the complete defensive system:
technology AND people.
                    """,
                    2: """
Policy review examines documentation - what procedures SAY should
happen. It doesn't test whether people can actually EXECUTE those
procedures under pressure from a determined adversary.

Red vs blue exercises prove whether defenders can actually detect,
respond, and stop attacks - not just whether they have policies.
                    """,
                    3: """
Self-assessment questionnaires ask people to evaluate their own
capabilities. "Can you detect intrusions?" "Yes." But can you
really? Self-assessment doesn't involve active testing against
a determined adversary.

Red vs blue exercises PROVE detection and response capability
through actual adversarial simulation.
                    """
                }
            },
            "corporate": {
                "title": "THE SECURITY WAR GAMES",
                "narrative": """
The CISO presents a proposal to the executive team for the annual
security exercise.

"I want to test our complete security posture," she explains.
"Not just our firewalls and endpoint protection - I want to know
if our SOC can actually detect a sophisticated attacker. Can our
incident response team actually contain a breach? Do our runbooks
work under pressure?"

She outlines her plan: "We'll engage an external team to simulate
real adversaries - let's call them the red team. They'll try to
achieve specific objectives: exfiltrate customer data, establish
persistence, whatever. Our internal security team - the blue team -
will try to detect and stop them, using only our normal tools and
procedures."

The CEO raises an eyebrow. "We already have vulnerability scans
and automated alerts."

"Those test our technology," the CISO responds. "This tests our
PEOPLE."

What type of exercise tests both defenses AND defender capabilities?
                """,
                "choices": [
                    {"text": "Automated vulnerability scanning"},
                    {"text": "Red team vs blue team exercise"},
                    {"text": "Policy review"},
                    {"text": "Control self-assessment"}
                ],
                "success_text": """
"RED TEAM versus BLUE TEAM exercise," you confirm. "The red team
(attackers) attempts to achieve objectives. The blue team
(defenders) tries to detect, respond, and stop them. It tests
the complete security program: technology, people, and process."

The exercise runs for two weeks. The red team attempts phishing,
exploits unpatched systems, and tries lateral movement. The blue
team monitors their SIEM, responds to alerts, and tries to
contain the simulated attack.

Results are illuminating:
- Red team achieved persistence on 3 systems before detection
- Blue team detection time averaged 6 hours (not great)
- Incident response runbook had 4 critical gaps
- Communication between SOC and management broke down

"Automated scans wouldn't have found any of this," the CISO notes.
"We learned more about our actual security posture in two weeks
than in a year of compliance audits."
                """,
                "failure_texts": {
                    0: """
Vulnerability scanning tests technical controls - can it find
missing patches, misconfigurations, exposed ports? It doesn't
test whether the SOC can detect an actual attacker, or whether
incident response procedures work under pressure.

Red vs blue exercises test the complete system: technology,
process, AND people working together against adversaries.
                    """,
                    2: """
Policy review examines what procedures are documented. It doesn't
test whether people can execute those procedures when a real
attack is happening. Documentation might be perfect while
execution completely fails.

Red vs blue exercises PROVE execution capability through actual
adversarial simulation.
                    """,
                    3: """
Self-assessment asks teams to evaluate their own capabilities.
"We're great at detection!" "We can contain any breach!" But
self-perception doesn't equal reality. Organizations routinely
overestimate their detection and response capabilities.

Red vs blue exercises provide evidence of actual capability
against a thinking adversary.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Red team vs blue team exercises test both technical controls AND human
detection/response capabilities. The red team (attackers) attempts to
achieve objectives while the blue team (defenders) tries to detect,
respond, and stop them. Automated scanning tests technology but not
people. Policy review checks documentation but not execution.
Self-assessment collects opinions but not evidence.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - Red Team / Blue Team"
    },

    # Scenario 11: Bug Bounty Programs
    {
        "id": "d6_bounty_hunters",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE FLAW FINDER'S REWARD",
                "narrative": """
The Citadel's defenses have been tested by internal teams and hired
siege masters. But the Master of Defense wants something more.

"Our own people are skilled," she acknowledges, "but they think like
us. They know our patterns. I want fresh eyes - MANY fresh eyes - from
across all the kingdoms. Rogues, trap-breakers, ward-crackers - anyone
who can find flaws we've missed."

She proposes an unusual program. "We announce a challenge to all the
kingdoms: find a flaw in the Citadel's defenses and prove it. In
return, we pay a bounty - gold for genuine discoveries. No punishment
for honest attempts. Continuous testing from the most diverse pool
of talent possible."

The Chief Treasurer frowns. "We're already paying siege masters for
annual assessments. Why pay outsiders for the same thing?"

What program provides continuous testing from diverse external
researchers, paying only for valid findings?
                """,
                "choices": [
                    {"text": "Annual penetration test contract with a siege master"},
                    {"text": "Bug bounty program open to researchers across the kingdoms"},
                    {"text": "Internal security audit by the guard force"},
                    {"text": "Compliance certification by the Merchant Guild"}
                ],
                "success_text": """
"A BUG BOUNTY PROGRAM," you explain. "We invite external researchers -
the rogues and trap-breakers the Master mentions - to find flaws.
We pay bounties only when they find valid vulnerabilities. Continuous
testing from diverse perspectives with pay-for-results economics."

The program launches. Within the first moon, twelve researchers from
six kingdoms have submitted findings. Two critical flaws that your
internal teams never found. Seven moderate issues. Three false alarms
that cost nothing because bounties require validation.

"Annual siege master contracts give us one perspective for a fixed
fee," the Master of Defense notes. "The bounty program gives us
dozens of perspectives, and we only pay for results. The mathematics
favor us."

BUG BOUNTY PROGRAMS enable continuous security testing from diverse
external researchers worldwide, paying only for valid findings.
                """,
                "failure_texts": {
                    0: """
Annual penetration test contracts provide periodic testing - once
a year, fixed fee, one team's perspective. The Master of Defense
specifically wanted CONTINUOUS testing from MANY researchers, not
periodic testing from one team.

Bug bounty programs run continuously and attract diverse researchers
with pay-for-results economics.
                    """,
                    2: """
Internal security audits use INTERNAL staff, not external researchers.
Internal teams think like insiders - they know the patterns and may
have blind spots. The Master of Defense specifically wanted "fresh
eyes from across all the kingdoms."

Bug bounty programs attract diverse external perspectives that
internal teams cannot provide.
                    """,
                    3: """
Compliance certifications are point-in-time assessments against
specific standards, not continuous security testing. They verify
you meet requirements; they don't find new vulnerabilities.

Bug bounty programs provide ongoing vulnerability discovery from
diverse researchers, not compliance verification.
                    """
                }
            },
            "corporate": {
                "title": "THE CROWDSOURCED SECURITY PROGRAM",
                "narrative": """
The security team is reviewing options for expanding their testing
coverage. The CISO presents a challenge.

"Our annual pen test gives us one firm's perspective for two weeks a
year. I want continuous testing. I want HUNDREDS of researchers with
different skill sets, different perspectives, different techniques.
And I want to pay only when they find something real."

The budget analyst perks up at that last part. "Pay only for results?
That's better than paying for time regardless of findings."

"Exactly," the CISO continues. "There are researchers all over the
world who specialize in finding flaws. Web app experts, mobile
specialists, crypto researchers. I want access to all of them,
continuously, with economics that make sense."

What program enables continuous testing from diverse global
researchers with pay-for-results economics?
                """,
                "choices": [
                    {"text": "Annual penetration test contract"},
                    {"text": "Bug bounty program"},
                    {"text": "Internal security audit"},
                    {"text": "Compliance certification"}
                ],
                "success_text": """
"A BUG BOUNTY PROGRAM," you confirm. "We define scope, set reward
tiers based on severity, and invite external researchers to find
vulnerabilities. They report findings through a coordinated
disclosure process. We validate and pay bounties for confirmed
issues."

Within three months of launch:
- 340 researchers have tested the applications
- 23 valid vulnerabilities discovered (including 2 criticals)
- Total payout: $47,000 (far less than annual pen test cost)
- One researcher found an authentication bypass the pen testers missed

"The math is compelling," the CFO notes in the quarterly review.
"We're getting continuous coverage from hundreds of researchers
for less than we paid for annual point-in-time testing."

BUG BOUNTY PROGRAMS provide continuous, crowdsourced security testing
with pay-for-results economics and diverse global perspectives.
                """,
                "failure_texts": {
                    0: """
Annual pen test contracts provide periodic testing from one firm.
The CISO specifically wanted CONTINUOUS testing from HUNDREDS of
researchers with DIVERSE perspectives. Annual contracts are the
opposite: periodic, single-source, homogeneous.

Bug bounty programs attract diverse researchers for continuous
testing with pay-for-results economics.
                    """,
                    2: """
Internal security audits use internal staff. The CISO specifically
wanted "researchers all over the world" with different specialties.
Internal teams can't provide the diversity or continuous external
perspective of a global researcher community.

Bug bounty programs tap into worldwide security researcher talent
that internal teams cannot replicate.
                    """,
                    3: """
Compliance certifications verify adherence to standards at a point
in time. They don't provide continuous vulnerability discovery.
The CISO wanted ongoing testing that finds new issues, not periodic
compliance verification.

Bug bounty programs enable continuous security testing with diverse
global participation.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Bug bounty programs invite external security researchers worldwide to
find vulnerabilities, paying rewards ("bounties") only for valid
findings. This provides continuous testing from diverse perspectives
with pay-for-results economics. Annual contracts are periodic and
single-source. Internal audits lack external perspective. Compliance
certifications are point-in-time verification, not ongoing testing.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - Bug Bounty Programs"
    },

    # Scenario 12: Tabletop Exercises
    {
        "id": "d6_crisis_council",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE CRISIS COUNCIL DRILL",
                "narrative": """
The Citadel's incident response team hasn't faced a major crisis in
years. The Master of Defense is concerned that when the next dragon
attack or dark wizard siege occurs, the response team won't know
their roles.

"I want to test our response procedures," she explains. "But I can't
summon an actual dragon or invite a dark wizard. I need a way to
practice WITHOUT affecting our actual defenses."

She gathers the key responders around a table. "Imagine this scenario:
a shape-shifting infiltrator has replaced the treasury guard captain.
Treasury funds are being siphoned. Walk me through your response."

No one leaves the room. No guards are dispatched. No wards are
activated. But for the next two hours, the team discusses, debates,
and walks through every step of their response plan.

What type of exercise practices incident response without affecting
production systems?
                """,
                "choices": [
                    {"text": "Full-scale disaster recovery test with actual failover"},
                    {"text": "Tabletop exercise / discussion-based walkthrough"},
                    {"text": "Production penetration test"},
                    {"text": "Automated backup restoration test"}
                ],
                "success_text": """
"This is a TABLETOP EXERCISE," you explain. "Discussion-based practice
where participants talk through their responses to hypothetical
scenarios. No systems are touched. No guards are deployed. We're
testing whether our people know the procedures and can work together."

The exercise reveals valuable insights:

- The communications officer didn't know who authorizes external
  disclosure to the other kingdoms
- The treasury guard captain's backup authority wasn't clearly defined
- Two responders thought they had the same responsibility

All discovered through discussion, not production impact.

"If we'd found these gaps during an actual crisis, lives could have
been lost," the Master of Defense notes. "Tabletop exercises are
safe practice for dangerous situations."

TABLETOP EXERCISES are discussion-based walkthroughs that test
response procedures without affecting operational systems.
                """,
                "failure_texts": {
                    0: """
Full-scale disaster recovery tests involve actual system failover -
real systems going down, real recovery procedures executing. This
affects production and carries risk. The Master of Defense specifically
wanted to practice WITHOUT affecting defenses.

Tabletop exercises are discussion-only, no system impact.
                    """,
                    2: """
Penetration testing targets real systems with real attacks (even if
controlled). This affects production systems and could cause disruption.
The scenario explicitly asks for practice that doesn't affect actual
defenses.

Tabletop exercises are purely discussion-based - no systems touched.
                    """,
                    3: """
Backup restoration tests actual recovery processes - real data being
restored, real systems being rebuilt. This is operational testing,
not incident response practice.

Tabletop exercises test response PROCEDURES and team coordination
through facilitated discussion, not technical recovery processes.
                    """
                }
            },
            "corporate": {
                "title": "THE RANSOMWARE DRILL",
                "narrative": """
The incident response team at Initech has documented procedures for
handling ransomware attacks. But they've never actually responded to
one. The CISO wants to test their preparedness without, obviously,
actually infecting the network with ransomware.

"I want to gather the team," she explains. "Present them with a
scenario: ransomware has encrypted our file servers, attackers are
demanding Bitcoin, the FBI is calling for an interview, and the
press has wind of it. Walk through what we'd do. Who calls who?
What decisions need to be made? Where are our runbooks?"

She looks around the conference room. "We'll stay right here. No
systems touched. Just talk through the response."

What type of exercise allows incident response practice without
affecting production systems?
                """,
                "choices": [
                    {"text": "Full-scale disaster recovery test"},
                    {"text": "Tabletop exercise / walkthrough"},
                    {"text": "Production penetration test"},
                    {"text": "Automated backup restoration"}
                ],
                "success_text": """
"TABLETOP EXERCISE," you confirm. "Discussion-based scenario practice.
We present a hypothetical situation and walk through our response,
identifying gaps in procedures, unclear roles, and coordination
issues - all without touching a single production system."

The exercise runs for three hours. Key findings:

- The CFO wasn't sure when to engage cyber insurance
- Legal didn't know the ransomware payment disclosure requirements
- IT and Security disagreed on who has authority to isolate systems
- The communication plan didn't include after-hours contact methods

"Better to find these gaps in a conference room than during an
actual ransomware attack," the CISO notes. "Schedule these
quarterly."

TABLETOP EXERCISES test response procedures through facilitated
discussion, identifying gaps safely before real incidents occur.
                """,
                "failure_texts": {
                    0: """
Full-scale DR tests involve actual failover of systems - real
servers going down, real recovery processes executing. This affects
production and carries risk of extended outage.

The CISO specifically wanted discussion-based practice without
touching systems. Tabletop exercises provide exactly that.
                    """,
                    2: """
Penetration testing attacks real production systems. Even authorized
pen tests can cause service disruption. The CISO explicitly wanted
to stay in the conference room with no systems touched.

Tabletop exercises are discussion-only - the scenario is hypothetical,
the learning is real, the systems are untouched.
                    """,
                    3: """
Backup restoration tests actual recovery technology - pulling backups,
restoring data, validating integrity. This is operational testing of
backup systems, not incident response practice.

Tabletop exercises test people and procedures through discussion,
not technology through execution.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Tabletop exercises are discussion-based walkthroughs where participants
talk through their responses to hypothetical scenarios. No actual systems
are affected, making them safe for practicing incident response. They
reveal gaps in procedures, role confusion, and coordination issues
without operational risk. Full-scale tests affect real systems;
penetration tests attack real targets.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - Tabletop Exercises"
    },

    # Scenario 13: Disaster Recovery Testing
    {
        "id": "d6_recovery_validation",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE RECOVERY PROMISE",
                "narrative": """
The Citadel's disaster recovery plan contains a bold claim: "In the
event of catastrophic tower collapse, critical ward systems can be
restored within four hours."

The High Commander is reviewing the plan with growing skepticism.
"This document was written three years ago. Have we ever actually
TESTED whether we can restore wards in four hours?"

The Ward Master looks uncomfortable. "Well, no. But we have the
backup ward crystals stored in the vault. And the restoration
procedures are documented..."

"Documentation says we CAN do it. I need to KNOW we can do it."
The Commander's voice is firm. "Before we tell the kingdom they're
protected by four-hour recovery, I want proof."

What type of test BEST validates that the four-hour recovery time
objective is actually achievable?
                """,
                "choices": [
                    {"text": "Review the disaster recovery documentation more carefully"},
                    {"text": "Conduct a full-scale recovery test with actual failover"},
                    {"text": "Ask the Ward Master if he thinks four hours is achievable"},
                    {"text": "Compare the four-hour target to other citadels' benchmarks"}
                ],
                "success_text": """
"We need a FULL-SCALE RECOVERY TEST," you advise. "Actually trigger
a failover scenario. Restore the ward systems from backup crystals.
Time the entire process. Prove that four hours is achievable - or
learn what the real number is."

The test is scheduled for a low-activity period. The ward tower is
isolated. Recovery begins from stored crystals following documented
procedures.

Result: Recovery took six hours and forty minutes. The documentation
was wrong. Several critical steps weren't even documented. One backup
crystal was corrupted and hadn't been validated in two years.

"Better to know NOW than during an actual disaster," the Commander
acknowledges. "Update the recovery time to eight hours to include
margin, and fix those procedures. And schedule these tests annually."

FULL-SCALE DR TESTS validate whether stated recovery objectives are
achievable. Documentation review and opinions don't prove capability.
                """,
                "failure_texts": {
                    0: """
The disaster recovery documentation CLAIMS four-hour recovery. But
claims aren't proof. The document might be outdated, inaccurate, or
based on assumptions that no longer hold. Only actual testing proves
whether the documented RTO is achievable.

Review shows what's written. Full-scale testing proves what's real.
                    """,
                    2: """
The Ward Master's opinion isn't evidence of capability. People
routinely overestimate recovery capability because they've never
actually tested it. "I think we can do it" doesn't equal "we've
proven we can do it."

Full-scale testing reveals the gap between belief and reality.
                    """,
                    3: """
What other citadels can achieve tells you nothing about YOUR
capability. Different infrastructure, different procedures, different
staff. Benchmarks are comparisons, not validation.

Only testing YOUR actual recovery process proves YOUR actual
capability.
                    """
                }
            },
            "corporate": {
                "title": "THE RTO VALIDATION",
                "narrative": """
Initech's disaster recovery plan promises a 4-hour Recovery Time
Objective (RTO) for critical systems. This RTO is reported to the
board, included in customer contracts, and cited in regulatory
filings.

The new IT Director notices a problem: "When was this RTO last
validated?"

Silence. The DR plan has existed for five years. The RTO has
never been tested.

"We're promising customers and regulators that we can recover in
four hours," the Director continues. "We have no evidence this is
true. We've never actually performed a full recovery test."

The Operations Manager is defensive. "We have the backups. We have
the procedures documented. We've done tabletop exercises."

"Those prove we have a PLAN. They don't prove the plan WORKS."

What test BEST validates that the 4-hour RTO is achievable?
                """,
                "choices": [
                    {"text": "Review the DR documentation for completeness"},
                    {"text": "Conduct a full-scale DR test with actual failover"},
                    {"text": "Ask the operations team if they think 4 hours is realistic"},
                    {"text": "Compare Initech's RTO to industry benchmarks"}
                ],
                "success_text": """
"FULL-SCALE DR TEST with actual failover," you recommend. "Declare
a simulated disaster. Fail over to the recovery site. Restore from
backups. Time every step. Prove we can meet RTO - or learn what
our real capability is."

The test is scheduled for a maintenance window. The primary
datacenter is isolated. Recovery begins.

Result: 7 hours, 23 minutes to full service restoration. The 4-hour
RTO was fiction.

Post-mortem findings:
- Two critical systems weren't in the backup scope
- Network configuration restore procedures were outdated
- Staff had never actually practiced the failover steps

"This is embarrassing," the IT Director admits, "but infinitely
better than discovering during a real disaster that we can't meet
our promises. Update the RTO to 8 hours and fix these gaps."

FULL-SCALE DR TESTING validates actual recovery capability against
stated objectives.
                """,
                "failure_texts": {
                    0: """
Documentation review verifies that a plan exists and is complete.
It doesn't verify that the plan WORKS. Procedures might be outdated.
Backup scope might be wrong. Actual execution might take twice as
long as documented.

Only full-scale testing reveals real-world recovery capability.
                    """,
                    2: """
Staff opinions aren't evidence. Operations teams routinely believe
they can recover faster than they actually can because they've never
tested it. Optimism isn't validation.

Full-scale testing provides actual evidence of recovery capability.
                    """,
                    3: """
Industry benchmarks show what other companies achieve, not what
Initech can achieve. Different infrastructure, different complexity,
different procedures. Comparison is not validation.

Testing YOUR actual recovery process proves YOUR actual RTO.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Only actual failover testing validates whether stated RTOs are achievable.
Documentation review shows what's planned but not what's possible.
Staff opinions express belief but not proof. Industry benchmarks compare
but don't validate. Full-scale DR tests reveal the gap between stated
objectives and real-world capability, identifying issues before actual
disasters occur.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - DR Testing"
    },

    # Scenario 14: Control Testing
    {
        "id": "d6_ward_validation",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE WARD VERIFICATION",
                "narrative": """
The Citadel's ward-keepers have installed a new protective enchantment.
This ward is designed to block portal travel from unauthorized locations
- specifically, from coordinates known to be dark wizard strongholds.

The Ward Master presents his report to the Security Council. "The ward
is configured and active. Here's the configuration scroll showing all
blocked coordinates."

A council member asks the obvious question: "How do we know it's
actually WORKING? Configuration scrolls show intent. I want proof
that if someone tries to portal from a blocked location, they actually
get blocked."

The Ward Master considers his options for validating that the new
control is functioning as designed.

How should this control be validated?
                """,
                "choices": [
                    {"text": "Review the ward configuration scrolls in detail"},
                    {"text": "Attempt test portals from blocked locations and verify they fail"},
                    {"text": "Ask the ward-keeper if the ward is working properly"},
                    {"text": "Check whether any unauthorized portals have occurred recently"}
                ],
                "success_text": """
"We need to ACTIVELY TEST the control," you advise. "Travel to a
location we know is blocked. Attempt to portal to the Citadel.
Verify that the portal fails. That's the only way to prove the
ward actually works as designed."

The Ward Master arranges a controlled test. A trusted mage travels
(by mundane means) to coordinates on the blocklist. She attempts
to open a portal to the Citadel.

The portal fails. The rejection is logged in the ward's detection
crystal. The control is confirmed working.

"Configuration shows INTENT," you explain. "Testing shows REALITY.
The ward is configured correctly AND functioning correctly. Without
this test, we'd only know one of those things."

CONTROL TESTING validates that security controls actually function
as intended. Attempting blocked actions and verifying failure
proves operational effectiveness.
                """,
                "failure_texts": {
                    0: """
Configuration review shows INTENT - what the ward is SUPPOSED to
do. It doesn't prove the ward is actually blocking portals. The
configuration might be correct while the ward itself malfunctions.

Active testing - attempting blocked actions and verifying they
fail - proves operational effectiveness.
                    """,
                    2: """
The ward-keeper's opinion isn't evidence. He might believe the ward
works because he configured it correctly, but belief isn't proof.
The ward could be misconfigured, malfunctioning, or bypassed in
ways he doesn't realize.

Actual testing provides evidence of control effectiveness.
                    """,
                    3: """
Absence of incidents doesn't prove the control works. Maybe no one
has tried to portal from blocked locations. Maybe attempts are
succeeding but not being detected. Maybe the control is working
for other reasons.

Active testing provides direct evidence that the specific control
functions as designed.
                    """
                }
            },
            "corporate": {
                "title": "THE FIREWALL RULE VALIDATION",
                "narrative": """
The security team has implemented a new firewall rule: block all
outbound connections to known malicious IP addresses. A threat
intelligence feed provides the blocklist, updated daily.

The Security Manager presents the implementation to the CISO.
"The rule is configured and active. Here's the firewall policy
showing the blocklist integration."

The CISO looks at the policy printout. "Configuration looks
correct. But how do we KNOW it's working? Configuration shows
what we intended. I want proof that malicious IPs are actually
being blocked."

The Security Manager considers options for validating this
control.

How should this firewall control be validated?
                """,
                "choices": [
                    {"text": "Review the firewall configuration files"},
                    {"text": "Attempt connections to known-bad IPs and verify they are blocked"},
                    {"text": "Ask the firewall administrator if it is working"},
                    {"text": "Check if any malware infections have occurred since deployment"}
                ],
                "success_text": """
"We need to ACTIVELY TEST the control," you recommend. "Attempt
connections to IPs on the blocklist from inside the network.
Verify they're blocked. Check the firewall logs for deny entries.
That proves the control works as designed."

You set up a test workstation. You attempt connections to several
IPs from the threat intelligence blocklist. Each connection times
out. The firewall logs show explicit deny entries for each attempt.

"Configuration tells us what we INTENDED. Testing tells us what
actually HAPPENS," you report to the CISO. "The control is verified
working. We should schedule periodic re-validation as part of
control monitoring."

CONTROL TESTING validates that security controls actually function
as intended by actively testing them and verifying expected behavior.
                """,
                "failure_texts": {
                    0: """
Configuration review shows INTENT - what the firewall SHOULD do.
But configuration errors, rule order problems, or integration
failures could mean the rule doesn't actually block anything.

Active testing - attempting blocked connections and verifying
failure - proves the control is operationally effective.
                    """,
                    2: """
The firewall admin's opinion isn't evidence. They might believe
the rule works because they configured it correctly, but that
doesn't account for implementation errors, rule conflicts, or
unexpected behavior.

Actual testing provides proof of control effectiveness.
                    """,
                    3: """
Absence of malware doesn't prove the firewall rule works. Maybe
no malware tried to connect to blocklist IPs. Maybe other controls
(endpoint protection, IDS) are doing the blocking. Maybe infections
occurred but weren't detected.

Active testing proves this SPECIFIC control functions as designed.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Effective control testing requires actively testing the control.
Attempting blocked actions and verifying they fail demonstrates
operational effectiveness. Configuration review shows intent but not
reality. Administrator opinions aren't evidence. Absence of incidents
doesn't prove the control works - other factors might be responsible.
Active positive testing proves controls function as designed.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - Control Validation"
    },

    # Scenario 15: Breach Attack Simulation
    {
        "id": "d6_continuous_siege",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE ENDLESS SIEGE DRILL",
                "narrative": """
The Citadel's defenses are tested annually by siege masters. But the
Master of Defense has grown concerned about the gaps between tests.

"Once a year, we hire siege masters for two weeks. They find problems.
We fix them. But then what?" She gestures at the ward towers. "Eleven
months go by. New enchantments are deployed. Guard rotations change.
Magic is updated. By the time the next siege test arrives, we've
drifted back into unknown territory."

She presents a new proposal: "I want to acquire a system - a permanent
automated siege simulation. Something that continuously tests our
wards and walls using the same techniques real attackers would use.
Every day. Every hour. Without needing to hire siege masters each time."

What solution provides continuous, automated attack simulation to
validate security controls?
                """,
                "choices": [
                    {"text": "Monthly vulnerability scans of the ward crystals"},
                    {"text": "Breach and Attack Simulation platform"},
                    {"text": "Annual penetration test by siege masters"},
                    {"text": "Install more protective ward crystals"}
                ],
                "success_text": """
"You're describing a BREACH AND ATTACK SIMULATION platform," you
explain. "Automated systems that continuously simulate real attack
techniques - portal intrusion, ward bypasses, credential attacks -
to validate whether your defensive controls actually detect and
prevent them."

The platform is deployed. It runs attack simulations hourly:
- Attempts known ward bypass techniques
- Tests detection enchantments with simulated dark magic signatures
- Validates blocking controls against intrusion patterns

Each test produces results: did the defenses detect it? Block it?
Alert on it? Continuous validation without continuous siege
master fees.

"This is exactly what I needed," the Master of Defense nods.
"Point-in-time tests have value. But continuous validation ensures
our defenses never silently drift into failure."

BREACH AND ATTACK SIMULATION (BAS) platforms provide continuous,
automated testing of security controls against real attack techniques.
                """,
                "failure_texts": {
                    0: """
Vulnerability scans identify known weaknesses - missing patches,
misconfigurations. They don't simulate actual attack techniques
to validate whether controls detect and prevent them.

BAS platforms actively simulate attacks (like MITRE ATT&CK
techniques) to test whether controls work as expected.
                    """,
                    2: """
Annual penetration tests are exactly what the Master of Defense
identified as insufficient. Point-in-time testing with eleven-month
gaps. She specifically asked for CONTINUOUS, AUTOMATED testing.

BAS platforms run continuously without manual testing effort.
                    """,
                    3: """
More ward crystals are a CONTROL - something being tested, not a
testing platform. Adding defenses doesn't validate that existing
defenses work. You'd still need to test whether the new crystals
actually function correctly.

BAS platforms TEST controls; they don't add new ones.
                    """
                }
            },
            "corporate": {
                "title": "THE CONTINUOUS VALIDATION PLATFORM",
                "narrative": """
The CISO reviews the security testing calendar with frustration.

"We do an annual pen test - two weeks, then they're gone. We have
quarterly vulnerability scans. But between tests, how do I know
our controls still work? Did that firewall change break our
detection? Is the new EDR actually blocking attack techniques?
Did something drift?"

She pulls up a vendor presentation. "There are platforms now that
continuously simulate attack techniques against our environment.
The MITRE ATT&CK framework - automated. Constantly testing whether
our SIEM detects lateral movement. Whether our endpoint protection
blocks known malware techniques. 24/7 validation, not annual
snapshots."

"Isn't that what pen testers do?" asks the CFO.

"Pen testers are human experts doing point-in-time testing. This
is automated continuous validation."

What type of platform provides continuous, automated attack
simulation across the kill chain?
                """,
                "choices": [
                    {"text": "Monthly vulnerability scans"},
                    {"text": "Breach and Attack Simulation (BAS) platform"},
                    {"text": "Annual penetration test"},
                    {"text": "Antivirus software"}
                ],
                "success_text": """
"BREACH AND ATTACK SIMULATION," you confirm. "BAS platforms
continuously and automatically simulate attack techniques -
aligned with frameworks like MITRE ATT&CK. They test whether
your controls detect and prevent each technique."

The platform runs simulations across the kill chain:
- Initial access: phishing simulations, exploit attempts
- Execution: malicious script techniques
- Persistence: registry modifications, scheduled tasks
- Lateral movement: pass-the-hash, remote execution
- Exfiltration: data staging, C2 communication

For each technique, results show: did the control detect it?
Block it? Alert on it? Continuous validation of the entire
security stack.

"Now I have evidence," the CISO says, reviewing the dashboard.
"Not 'we tested once last year' - evidence that our controls
work TODAY."

BAS platforms provide continuous, automated security control
validation against real-world attack techniques.
                """,
                "failure_texts": {
                    0: """
Vulnerability scans find known weaknesses - CVEs, misconfigurations.
They don't simulate attack techniques or test whether controls
detect and prevent actual threats.

BAS platforms actively simulate attacks to validate detection
and prevention capabilities.
                    """,
                    2: """
Annual pen tests are point-in-time. The CISO specifically
identified the problem with "annual snapshots" versus continuous
validation. Pen tests use human experts periodically; BAS provides
automated continuous testing.

BAS platforms fill the eleven-month gap between annual tests.
                    """,
                    3: """
Antivirus is a CONTROL - something being tested, not a testing
platform. BAS platforms test whether your antivirus (and SIEM,
and firewall, and EDR) actually works against attack techniques.

You need something that tests controls, not another control.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Breach and Attack Simulation (BAS) platforms continuously and
automatically simulate attack techniques (often mapped to MITRE ATT&CK)
to test whether security controls detect and prevent them. This provides
ongoing validation without manual testing effort. Vulnerability scans
find weaknesses but don't simulate attacks. Annual pen tests are
point-in-time. Antivirus is a control being tested, not a testing tool.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - Breach Attack Simulation"
    },

    # Scenario 16: Software Composition Analysis
    {
        "id": "d6_component_review",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE BORROWED ENCHANTMENTS",
                "narrative": """
The Citadel's Arcane Development Guild has adopted a modern approach
to spell crafting. Rather than writing every enchantment from scratch,
they incorporate pre-written magical components from the Open Spell
Repository - shared enchantments created by mages across all kingdoms.

The Arch-Mage reviews the latest defensive ward. "This protection
spell uses forty-seven external magical components. Binding hexes,
energy channelers, focus crystals - all borrowed from the Repository."

A young mage asks, "Is that secure? We're using spells written by
mages we've never met."

The Arch-Mage nods thoughtfully. "An excellent question. Some of
these components may contain known flaws that have been discovered
since we adopted them. We need a way to identify which of our
borrowed components have known vulnerabilities."

What type of analysis identifies known vulnerabilities in third-party
magical components?
                """,
                "choices": [
                    {"text": "Static analysis of the ward's original rune patterns"},
                    {"text": "Component composition analysis of borrowed enchantments"},
                    {"text": "Interactive testing of the ward while active"},
                    {"text": "Protective barrier around the ward to block attacks"}
                ],
                "success_text": """
"SOFTWARE COMPOSITION ANALYSIS," you explain (using the closest
analogy). "A technique that examines all borrowed components and
cross-references them against known vulnerability databases. If
a component we're using has been found to have a flaw, we're
alerted immediately."

The composition analysis tool scans the ward's dependencies:
- Binding Hex v2.3: VULNERABLE - energy leak allows bypass
- Focus Crystal v4.1: Safe
- Energy Channeler v1.8: VULNERABLE - buffer overflow in charging
- ...and 44 more components analyzed

"Three of our borrowed components have known flaws," the report
concludes. "These were discovered after you incorporated them.
Updates are available."

"Without this analysis, we'd have deployed vulnerable wards," the
Arch-Mage acknowledges. "Composition analysis identifies inherited
risk."

SOFTWARE COMPOSITION ANALYSIS (SCA) identifies known vulnerabilities
in third-party components, libraries, and dependencies.
                """,
                "failure_texts": {
                    0: """
Static analysis examines YOUR code - the original rune patterns
written by your mages. It doesn't analyze the third-party components
you've incorporated. Those borrowed enchantments need composition
analysis to check for known vulnerabilities.

SCA specifically examines external dependencies, not original code.
                    """,
                    2: """
Interactive testing (IAST) examines running applications through
instrumentation. It might find issues during execution, but it's
not designed to identify known vulnerabilities in specific third-party
components by version.

Composition analysis specifically cross-references component versions
against vulnerability databases.
                    """,
                    3: """
A protective barrier (Web Application Firewall analogy) blocks
attacks at runtime. It doesn't identify that you're using vulnerable
components - it might block some attacks while leaving the underlying
vulnerability unaddressed.

Composition analysis identifies vulnerable components so they can
be updated or replaced.
                    """
                }
            },
            "corporate": {
                "title": "THE OPEN SOURCE RISK",
                "narrative": """
The development team at Initech builds applications using dozens of
open-source libraries. Package managers make it easy - npm install,
pip install, mvn dependency - and suddenly your application has
hundreds of components written by developers you've never met.

The security architect raises a concern during sprint planning.
"Our payment application imports 247 npm packages. How many of those
have known vulnerabilities? Log4j taught us that one vulnerable
dependency can compromise everything."

The lead developer looks thoughtful. "Our SAST tool checks our code.
But you're right - it doesn't check the code we imported."

"We need something that specifically analyzes our dependencies,"
the architect continues. "Cross-references every package version
against CVE databases. Alerts us when libraries we're using have
known flaws."

What type of tool identifies known vulnerabilities in third-party
open-source components?
                """,
                "choices": [
                    {"text": "Static Application Security Testing (SAST)"},
                    {"text": "Software Composition Analysis (SCA)"},
                    {"text": "Interactive Application Security Testing (IAST)"},
                    {"text": "Web Application Firewall (WAF)"}
                ],
                "success_text": """
"SOFTWARE COMPOSITION ANALYSIS - SCA," you confirm. "It analyzes
your dependency manifest - package.json, requirements.txt, pom.xml -
and cross-references every component version against vulnerability
databases like the National Vulnerability Database."

The SCA tool scans the payment application:
- lodash@4.17.15: CRITICAL - CVE-2020-28500, prototype pollution
- log4j@2.14.1: CRITICAL - CVE-2021-44228, remote code execution
- jackson-databind@2.9.8: HIGH - multiple deserialization flaws
- ...and 244 more packages analyzed

"Three packages with critical CVEs that we're actively using,"
the architect reports. "Update paths are available. Without SCA,
we'd have shipped with known vulnerabilities."

SOFTWARE COMPOSITION ANALYSIS identifies known vulnerabilities
in third-party dependencies, enabling proactive remediation.
                """,
                "failure_texts": {
                    0: """
SAST analyzes YOUR source code - the code your developers wrote.
It looks for coding patterns that indicate vulnerabilities. But
it doesn't analyze third-party libraries you've imported.

SCA specifically examines external dependencies and their known
vulnerability status.
                    """,
                    2: """
IAST instruments running applications to identify vulnerabilities
during testing. While it might catch some issues, it's not designed
to systematically identify all known CVEs in your dependency tree.

SCA cross-references every component version against vulnerability
databases.
                    """,
                    3: """
WAF blocks attacks against running applications. It doesn't identify
that you're using vulnerable libraries - it might mitigate some
attacks while the underlying vulnerable code remains. WAF is a
control, not an analysis tool.

SCA identifies vulnerable components so they can be updated before
deployment.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Software Composition Analysis (SCA) tools analyze third-party dependencies
(libraries, packages, components) to identify known vulnerabilities. They
cross-reference component versions against CVE databases, alerting when
your project uses vulnerable versions. SAST analyzes your code, not
dependencies. IAST tests running applications. WAF blocks attacks but
doesn't identify vulnerable components.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - Software Composition Analysis"
    },

    # Scenario 17: Continuous Security Testing
    {
        "id": "d6_pipeline_testing",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE ENCHANTMENT FORGE REVIEW",
                "narrative": """
The Citadel's Arcane Development Guild has a problem. Security reviews
of new enchantments happen only before major deployments - typically
once per season. But the guild produces new enchantments weekly.

"By the time the seasonal review happens," the Guild Master explains,
"we've deployed dozens of enchantments. When reviewers find flaws,
we have to recall enchantments that are already protecting the walls.
Expensive. Disruptive. Embarrassing."

A young enchanter suggests a solution: "What if security review
happened AS WE CRAFT? Every time we add a new rune sequence to the
spell forge, automated analysis runs immediately. We find problems
when the enchantment is still on the workbench, not after it's
embedded in the walls."

"Integrating security testing into our enchantment creation process
itself..." the Guild Master muses. "Not a separate activity, but part
of how we work."

What approach integrates security testing into the development process
for immediate feedback?
                """,
                "choices": [
                    {"text": "More frequent seasonal security audits"},
                    {"text": "Integrate security testing into the enchantment forge process"},
                    {"text": "Hire more security reviewers for larger seasonal reviews"},
                    {"text": "Delay all deployments until security approves"}
                ],
                "success_text": """
"INTEGRATE SECURITY TESTING INTO THE DEVELOPMENT PIPELINE," you
advise. "Every time enchanters commit new rune sequences, automated
security analysis runs immediately. Static analysis checks the
patterns. Composition analysis verifies borrowed components. Results
appear before the enchantment leaves the forge."

The integration is implemented. Now:
- New rune patterns trigger immediate static analysis
- Borrowed components are checked against vulnerability databases
- Enchanters see security feedback within minutes of crafting
- Flaws are fixed while the enchantment is still in development

"The seasonal review still happens," the Guild Master notes, "but
now it finds almost nothing because issues are caught during creation.
Shift left - find problems when they're cheap to fix."

CONTINUOUS SECURITY TESTING integrates SAST, DAST, and SCA into
development pipelines for immediate feedback on every change.
                """,
                "failure_texts": {
                    0: """
More frequent audits are still PERIODIC. Quarterly instead of
seasonal still means enchantments deploy weeks before review.
The fundamental problem - finding issues after deployment -
remains.

Pipeline integration provides IMMEDIATE feedback on every change,
not periodic batch reviews.
                    """,
                    2: """
More reviewers for larger seasonal reviews doesn't address timing.
It might find more issues, but still only during the seasonal review.
Enchantments still deploy before review. Recalls still happen.

The issue is WHEN testing occurs, not review capacity. Pipeline
integration shifts testing to development time.
                    """,
                    3: """
Delaying all deployments creates a bottleneck. Every enchantment
waits for approval. Security becomes a barrier, not an enabler.
The guild's velocity plummets while security reviews the backlog.

Pipeline integration provides immediate automated feedback without
slowing delivery - security enables rather than blocks.
                    """
                }
            },
            "corporate": {
                "title": "THE CI/CD SECURITY GAP",
                "narrative": """
Initech's development teams deploy to production multiple times daily
through their CI/CD pipeline. Code goes from commit to production in
hours. But security testing? That happens quarterly.

"By the time the quarterly security review occurs," the Security
Architect explains, "hundreds of changes have deployed. When we find
vulnerabilities, they've been in production for weeks. Remediation is
expensive because the developers have moved on to new features."

The Development Lead sees the problem. "What if security testing was
part of the pipeline itself? Every commit triggers security scans.
Every build includes vulnerability checking. Developers get feedback
immediately, not three months later."

"That's a significant change to how we work," the CISO notes. "But
it would catch issues when they're cheapest to fix."

What approach integrates security testing into the CI/CD pipeline
for immediate developer feedback?
                """,
                "choices": [
                    {"text": "More frequent quarterly audits"},
                    {"text": "Integrate SAST/DAST into CI/CD pipeline"},
                    {"text": "Hire more security auditors"},
                    {"text": "Delay releases until security approves"}
                ],
                "success_text": """
"INTEGRATE SECURITY TESTING INTO CI/CD," you recommend. "SAST runs
on every commit. DAST runs against deployment environments. SCA
checks dependencies on every build. Developers get security feedback
within minutes of pushing code."

The integration is implemented:
- Pre-commit hooks run quick SAST checks
- Build pipeline includes full SAST and SCA analysis
- Staging deployments trigger DAST scans
- Security findings appear in developer workflows immediately

"Last quarter, we found 47 vulnerabilities," the Security Architect
reports. "Since pipeline integration, we catch equivalent issues
immediately. Developers fix them before they leave their IDE. Our
quarterly review now finds almost nothing because issues are caught
at creation."

CONTINUOUS SECURITY TESTING integrates SAST, DAST, and SCA into
CI/CD pipelines, providing immediate feedback and shifting security left.
                """,
                "failure_texts": {
                    0: """
Quarterly audits are still PERIODIC. Even monthly would mean code
deploys weeks before review. The problem is timing, not frequency
of batch reviews.

Pipeline integration provides feedback on EVERY commit, not
periodic batch reviews after deployment.
                    """,
                    2: """
More auditors increases review capacity but doesn't change timing.
Quarterly reviews with more people still happen quarterly. Code
still deploys before review. Remediation is still expensive.

The issue is WHEN testing occurs. Pipeline integration shifts
testing to development time.
                    """,
                    3: """
Delaying releases creates a security gate that blocks everything.
Development velocity crashes. Security becomes the team everyone
hates. Features are held hostage waiting for review.

Pipeline integration provides automated, immediate feedback without
creating bottlenecks - security enables velocity rather than
blocking it.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Integrating security testing (SAST, DAST, SCA) into CI/CD pipelines provides
continuous, automated security feedback. Developers find issues immediately
when code is committed, enabling faster remediation. More frequent audits
are still periodic. More auditors don't change timing. Blocking releases
creates bottlenecks. Pipeline integration shifts security left for early
detection without slowing delivery.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - Continuous Security Testing"
    },

    # Scenario 18: Reporting and Remediation Tracking
    {
        "id": "d6_remediation_status",
        "domain": 6,
        "themes": {
            "fantasy": {
                "title": "THE SIEGE MASTER'S FOLLOW-UP",
                "narrative": """
Three moons ago, the Citadel hired Siege Master Valdris to test the
fortress defenses. His assessment identified fifty weaknesses - twenty
critical, fifteen moderate, fifteen minor. The High Commander approved
remediation plans for all findings.

Now the War Council has convened. The High Commander needs to report
to the kingdom's rulers on security posture.

"Three moons have passed," she states. "I need to know: what is the
CURRENT status of those fifty findings? How many are fixed? How many
are still being worked? How many remain untouched?"

The Master of Records considers the options. He could present Valdris's
original report. He could commission a new siege test. He could simply
assure the Council that all is well.

What should be provided to show the current remediation status?
                """,
                "choices": [
                    {"text": "The original siege master report from three moons ago"},
                    {"text": "A remediation status report showing fixed, in progress, and open findings"},
                    {"text": "Commission a new siege test to find current vulnerabilities"},
                    {"text": "Verbal assurance that the defense team is working on everything"}
                ],
                "success_text": """
"A REMEDIATION STATUS REPORT," you advise. "It tracks the current state
of each finding from Valdris's assessment. For every weakness identified:
is it fixed? Is remediation in progress? Is it still open? Risk-accepted
with compensating controls?"

The Master of Records produces the tracking report:
- 50 total findings
- 32 remediated and verified (64%)
- 11 in active remediation (22%)
- 5 risk-accepted with documentation (10%)
- 2 still open, awaiting resources (4%)

"This tells me exactly what I need," the High Commander nods. "Not
what Valdris found three moons ago - we know that. Not a new assessment
that ignores prior findings. The current status of KNOWN issues.
This is accountability."

REMEDIATION STATUS REPORTS track the current state of identified
findings, providing visibility and accountability for vulnerability
management.
                """,
                "failure_texts": {
                    0: """
The original report shows what Valdris found three moons ago. It
doesn't show what's been fixed, what's in progress, or what's still
open. The Council already has this report - they need CURRENT status.

Remediation tracking shows the present state of known findings,
not historical discoveries.
                    """,
                    2: """
A new siege test would find NEW vulnerabilities, not report on
the status of KNOWN issues. Valdris found fifty problems. The
Council needs to know if those fifty are addressed - not discover
fifty new ones.

New assessments and remediation tracking serve different purposes.
Both are needed, but the question is about tracking known issues.
                    """,
                    3: """
Verbal assurance provides no documentation, no verification, and
no accountability. "We're working on it" doesn't tell the Council
WHICH findings are fixed, WHICH are in progress, or whether
critical issues remain open.

Formal remediation tracking provides evidence and accountability.
                    """
                }
            },
            "corporate": {
                "title": "THE PEN TEST FOLLOW-UP",
                "narrative": """
Three months ago, Initech's annual penetration test identified 50
vulnerabilities - 20 critical, 15 high, 15 medium. The findings
were assigned to various teams for remediation. Now the board wants
a security update.

"The board meeting is Tuesday," the CISO says. "They want to know:
what happened to those 50 findings? They remember the scary presentation
three months ago. Now they want to know if we're still scary."

The security manager considers options:
- Present the original pen test report (they already saw it)
- Commission a new pen test (won't be done by Tuesday)
- Give verbal assurance that everything is fine (they'll want proof)
- Produce a tracking report showing current status of each finding

What should be provided to show current remediation status?
                """,
                "choices": [
                    {"text": "The original penetration test report"},
                    {"text": "Remediation status report showing fixed, in progress, and open findings"},
                    {"text": "A new penetration test"},
                    {"text": "Verbal assurance that everything is being addressed"}
                ],
                "success_text": """
"REMEDIATION STATUS REPORT," you recommend. "It tracks every
finding from the pen test. Current status: remediated, in progress,
risk-accepted, or still open. Evidence of closure for fixed items.
Target dates for open items. The board gets accountability, not
promises."

You produce the tracking report:
- 50 total findings from March pen test
- 37 remediated and verified (74%)
- 8 in active remediation, ETA next month (16%)
- 3 risk-accepted with compensating controls (6%)
- 2 blocked, waiting on vendor patches (4%)

"This is exactly what they need," the CISO nods. "Not the old
report - they saw that. Not a new test - that finds new issues.
The current status of KNOWN issues. Progress. Accountability.
Evidence."

REMEDIATION STATUS REPORTS provide visibility into vulnerability
management program effectiveness and demonstrate accountability.
                """,
                "failure_texts": {
                    0: """
The original pen test report is three months old. The board already
saw it. They want to know what's happened SINCE then. How many
findings are fixed? How many remain? What's the current risk posture?

The original report shows discovery. Remediation tracking shows
progress.
                    """,
                    2: """
A new pen test finds NEW vulnerabilities. It doesn't tell the board
whether the 50 KNOWN issues were addressed. They want to know about
the specific findings that concerned them three months ago.

New assessments and remediation tracking are both needed but serve
different purposes.
                    """,
                    3: """
Boards want evidence, not assurance. "We're working on everything"
doesn't tell them WHICH criticals are fixed, how long others will
take, or whether material risks remain. They'll ask for specifics.

Remediation tracking provides documented, verifiable status with
evidence of closure.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Remediation status reports track the current state of identified findings:
fixed, in progress, risk-accepted, or open. This provides accountability
and visibility into vulnerability management effectiveness. Original
reports are historical and don't show progress. New tests find new issues
but don't track known ones. Verbal assurance lacks documentation and
evidence.
        """,
        "domain_reference": "Domain 6: Security Assessment and Testing - Remediation Tracking"
    },
]
