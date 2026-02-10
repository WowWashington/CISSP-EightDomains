"""
Domain 5: Identity and Access Management scenarios.

Key CISSP concepts tested:
- Authentication Factors
- Multi-Factor Authentication
- Single Sign-On and Federation
- Access Control Models
- Privileged Access Management
- Account Lifecycle
- Identity Governance

Each scenario supports dual themes:
- Fantasy: Medieval/magical Citadel setting
- Corporate: Modern office satire (Office Space style)
"""

DOMAIN_5_SCENARIOS = [
    # Scenario 1: Authentication Factors
    {
        "id": "d5_two_keys_gate",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE TWO KEYS OF THE INNER SANCTUM",
                "narrative": """
The gates to the Inner Sanctum stand before you, guarded by ancient magic and
older tradition. The Gatekeeper, a wizened figure whose beard touches the floor,
regards you with knowing eyes.

"To enter," he intones, "one must present proof of identity. We require two
things: the Passphrase of your House - words known only to you - and the
Enchanted Sigil that each guardian carries upon their person."

He gestures to the great doors, inscribed with glowing runes. "Many have tried
with false words. Many have tried with stolen sigils. But the combination of
what you KNOW and what you CARRY has protected this sanctum for a thousand years."

A young apprentice nearby whispers, "Is this not excessive? Surely one proof
should suffice?"

The Gatekeeper turns to you. "Explain to this youngling: what type of
authentication guards our sanctum?"
                """,
                "choices": [
                    {"text": "Single-factor authentication - one strong proof is all that's needed"},
                    {"text": "Two-factor authentication - combining something you know with something you have"},
                    {"text": "Biometric authentication - the sigil reads your life force"},
                    {"text": "Risk-based authentication - the gate adapts to the threat level"}
                ],
                "success_text": """
You nod sagely at the apprentice. "The Gatekeeper speaks of two-factor
authentication. The passphrase is something you KNOW - it exists only in your
mind. The Enchanted Sigil is something you HAVE - a physical token you carry.
By requiring both, we ensure that neither a spy who overhears words nor a thief
who steals a sigil alone can breach our sanctum."

The Gatekeeper's eyes crinkle with approval. "Well spoken. A stolen passphrase
is useless without the sigil. A stolen sigil is useless without the passphrase.
This is the strength of combining different authentication factors."

The great doors swing open, acknowledging your wisdom.

TWO-FACTOR AUTHENTICATION (2FA) combines two different types of factors,
providing stronger security than any single factor alone.
                """,
                "failure_texts": {
                    0: """
The Gatekeeper shakes his head slowly. "Single factor? If a spy learns
your passphrase, they walk freely into our sanctum. If a thief steals
your sigil, the same. We require BOTH precisely because two factors are
stronger than one. This is the essence of multi-factor authentication."
                    """,
                    2: """
"Biometrics?" The Gatekeeper chuckles. "The sigil reads enchantment, not
life force. Biometrics would be something you ARE - a fingerprint, an
iris pattern, the unique pattern of your aura. The sigil is something
you HAVE - a physical token. Know the difference between factors."
                    """,
                    3: """
"Risk-based authentication adapts requirements based on context - location,
time, behavior patterns. Our gate does not change its requirements based
on perceived risk. It always demands the same two factors: something
KNOWN and something CARRIED. Consistency is our strength here."
                    """
                }
            },
            "corporate": {
                "title": "THE SECURITY TOKEN TRAINING",
                "narrative": """
You're sitting through the mandatory quarterly security training when Sharon
from HR pauses the video and turns to the room.

"Okay, before we continue, pop quiz!" She holds up her phone. "Our new
login system requires you to enter your password AND a code from your
authenticator app. Jenkins in Accounting keeps complaining this is
'overkill' and 'nobody has time for this.'"

She pulls up a slide showing the login screen with both fields. "For the
training record, I need someone to explain what type of authentication
this is. Don't all volunteer at once."

Your manager nudges you. "You're the security liaison. This is literally
your job."

The room waits expectantly. Even Jenkins stops checking his fantasy
football scores to glare at you.
                """,
                "choices": [
                    {"text": "Single-factor authentication - one strong password should be enough"},
                    {"text": "Two-factor authentication - something you know plus something you have"},
                    {"text": "Biometric authentication - the app reads your fingerprint"},
                    {"text": "Risk-based authentication - it adapts to threat levels"}
                ],
                "success_text": """
"This is two-factor authentication," you explain. "The password is
something you KNOW - it's in your head. The authenticator code is
something you HAVE - it requires possession of your phone. Two
different factor types."

You turn to Jenkins. "If someone shoulder-surfs your password at the
coffee shop, they still can't log in without your phone. If someone
steals your phone, they still need your password. That's the point."

Sharon beams. "Exactly! Thank you. Moving on - Jenkins, you can put
your phone away now."

Jenkins mutters something about "security theater" but you know the
truth: TWO-FACTOR AUTHENTICATION with two distinct factor types is
genuinely stronger than any single factor, no matter how complex.
                """,
                "failure_texts": {
                    0: """
Jenkins actually high-fives you before Sharon cuts in: "No, no. If we
only used a password, one phishing email and someone's in your account.
The whole point of the second factor is that compromising one isn't
enough. This is two-factor authentication, not single-factor."
                    """,
                    2: """
Sharon frowns. "The authenticator app doesn't read your fingerprint -
well, your phone might, but that's separate. The CODE from the app is
something you HAVE because you possess the phone. Biometrics would
be something you ARE, like a fingerprint scan. Different factor types."
                    """,
                    3: """
"Risk-based authentication would change requirements based on context,"
Sharon explains. "Like requiring extra verification for unusual locations.
Our system always requires both password AND code, regardless of risk.
It's two-factor authentication - two different factor types, every time."
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Two-factor authentication (2FA) requires two different types of authentication
factors: something you KNOW (password, PIN), something you HAVE (token, phone),
or something you ARE (biometric). Using two factors from the same category
(like two passwords) is NOT two-factor authentication. The strength comes
from requiring different types, so compromising one doesn't compromise both.
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Authentication Factors"
    },

    # Scenario 2: Single Sign-On Risks
    {
        "id": "d5_master_key_peril",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE MASTER KEY'S PERIL",
                "narrative": """
The Council of Realms has implemented a grand new system: the Master Key.
With one enchanted token, authenticated at the Central Gate, a guardian may
freely access the Treasury, the Armory, the Scroll Archives, and all
connected guildhalls throughout the realm.

"Such convenience!" the Trade Minister exclaims. "No more remembering dozens
of passphrases! One authentication and our people move freely!"

But the Security Council has called this emergency session. The Master of
Shadows speaks grimly: "We have intercepted intelligence. Enemy agents seek
to obtain a Master Key. The High Councilor wishes to know the PRIMARY
security concern this poses."

All eyes turn to you. The High Councilor taps her fingers impatiently.
"Speak plainly. What risk does this unified access create?"
                """,
                "choices": [
                    {"text": "The Master Key makes accessing the guildhalls slower"},
                    {"text": "Compromised credentials grant access to ALL connected locations"},
                    {"text": "Guardians must now remember more passphrases than before"},
                    {"text": "The Master Key doesn't work with allied kingdoms' gates"}
                ],
                "success_text": """
"The peril is clear," you address the Council. "If an enemy agent steals or
counterfeits a single Master Key, they gain access not to one guildhall, but
to ALL connected locations simultaneously. The Treasury, the Armory, the
Archives - all fall with one compromised credential."

The Master of Shadows nods approvingly. "Precisely. The convenience that
serves our guardians also serves our enemies - should they breach the
single point of authentication."

The High Councilor leans forward. "Then our Master Key system requires
the strongest possible protections. Multiple factors of authentication.
Constant vigilance over those tokens. The convenience is worth the risk
only if we defend that single point with our utmost effort."

SINGLE SIGN-ON creates a single point of compromise - protect it fiercely.
                """,
                "failure_texts": {
                    0: """
The Trade Minister snorts. "Slower? The Master Key is FASTER! One
authentication instead of many!" The High Councilor sighs. "We are
discussing security risks, not user experience. Think: what happens
if an enemy obtains a Master Key? They access EVERYTHING. That is
the primary concern with unified authentication."
                    """,
                    2: """
The High Councilor raises an eyebrow. "More passphrases? The entire
purpose of the Master Key is to REDUCE the number of credentials.
One authentication grants all access. The risk is that compromising
that ONE credential compromises EVERYTHING. Think it through."
                    """,
                    3: """
"Allied kingdoms use their own systems - that is federation, a
separate matter," the Master of Shadows interjects. "The PRIMARY
risk is internal: if an enemy steals a Master Key, they access
every connected location with that single stolen credential.
One breach, total access."
                    """
                }
            },
            "corporate": {
                "title": "THE SSO SECURITY REVIEW",
                "narrative": """
The IT Director stands before the executive team, presenting the quarterly
security review. You've been pulled in as the security subject matter expert.

"Our SSO implementation has been a huge success!" she announces. "Users log
in once and get access to email, Salesforce, the HR system, code repos,
financial systems - everything. Help desk tickets for password resets are
down 60%!"

The CISO clears his throat. "That's wonderful for productivity. But for
this review, I need the security team's assessment. What is the PRIMARY
security concern with our SSO implementation?"

The CFO checks his watch. The CEO is already on her phone. But the CISO
stares directly at you, waiting for the security perspective that justifies
his budget.

What do you tell them?
                """,
                "choices": [
                    {"text": "SSO makes applications slower to load"},
                    {"text": "Compromised credentials grant access to all connected applications"},
                    {"text": "SSO requires users to remember more passwords than before"},
                    {"text": "SSO doesn't work with our cloud applications"}
                ],
                "success_text": """
"The primary security concern," you explain, "is that SSO creates a single
point of compromise. If an attacker steals a user's SSO credentials - through
phishing, malware, or session hijacking - they don't just get access to email.
They get access to EVERY application connected to SSO."

You pull up a diagram. "With separate logins, stealing the HR system password
only compromises HR. With SSO, one stolen credential means email, financial
systems, code repos, HR - everything falls at once."

The CISO nods. "Which is why we require MFA for SSO authentication and
have invested in session monitoring. The convenience of SSO is worth the
risk only with strong compensating controls."

The CEO actually looks up from her phone. "So the security budget for
SSO protection is justified." "Absolutely," you confirm.
                """,
                "failure_texts": {
                    0: """
The IT Director looks confused. "Slower? SSO makes things faster - users
aren't constantly re-authenticating!" The CISO sighs. "The security
concern isn't performance. It's that one compromised credential grants
access to EVERYTHING. That's the risk we need to mitigate."
                    """,
                    2: """
The CFO actually laughs. "More passwords? The whole point of SSO is
ONE password for everything!" The CISO pinches the bridge of his nose.
"The concern is that when that ONE password is stolen, the attacker
gets access to ALL systems. Single point of failure, single point of
compromise."
                    """,
                    3: """
The IT Director waves dismissively. "All our cloud apps use SAML and
OIDC - they work fine with SSO." The CISO leans forward. "Focus on
the security concern: one compromised account means total access to
everything. That's what keeps me up at night."
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Single Sign-On (SSO) provides tremendous convenience but creates a critical
security concern: a SINGLE POINT OF COMPROMISE. If an attacker steals SSO
credentials or hijacks an SSO session, they gain access to ALL connected
applications, not just one. This requires compensating controls like strong
MFA, session monitoring, and robust credential protection.
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Single Sign-On Risks"
    },

    # Scenario 3: Federated Identity
    {
        "id": "d5_allied_kingdoms_treaty",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE TREATY OF TRUSTED REALMS",
                "narrative": """
The Ambassador from the Eastern Kingdom arrives with an urgent request.
"Our realms have long been allies," she begins. "Our scholars need access
to your Great Library. Your merchants need access to our trading halls.
Currently, each must obtain separate credentials in each realm - it is
cumbersome and insecure."

She unfurls a proposal scroll. "We propose a Treaty of Trusted Realms.
Your people authenticate with YOUR kingdom's credentials, and we accept
that authentication through magical trust tokens. Our people do the same
when visiting you. No sharing of actual secrets between our realms."

The Lord Chancellor strokes his beard. "You mean our Court Wizards vouch
for our people's identity, and your realm accepts our word through
these... trust tokens?"

"Precisely," the Ambassador nods. "What term do your security scholars
use for such an arrangement?"
                """,
                "choices": [
                    {"text": "Share a master password between both kingdoms"},
                    {"text": "Create duplicate accounts for users in both realms"},
                    {"text": "Implement federated identity using trust tokens (like SAML)"},
                    {"text": "Give the Eastern Kingdom access to our identity vaults"}
                ],
                "success_text": """
"This is federated identity," you explain. "Each realm maintains its own
identity system - its own Court Wizards who verify and vouch for their
people. When a scholar from our realm visits the Eastern Kingdom, our
Court Wizards issue a trust token - an assertion that says 'We have
verified this person's identity.'"

You continue, "The Eastern Kingdom's gates accept this token because of
the treaty - they TRUST our Court Wizards to do proper verification. The
actual credentials - our passphrases and secrets - never leave our realm.
Only the assertion of identity crosses the border."

The Ambassador smiles. "In your technical tongue, your realm is the
Identity Provider. Our trading halls are the Service Providers. The
trust tokens might be called SAML assertions or OIDC tokens. But the
principle is the same: trusted authentication without shared secrets."

FEDERATED IDENTITY allows cross-organization authentication through trust.
                """,
                "failure_texts": {
                    0: """
The Ambassador recoils. "Share a master password? Between kingdoms?
If that password were ever discovered, both realms would fall! No - the
very point of federation is that we NEVER share actual credentials.
Only assertions of verified identity cross between our realms."
                    """,
                    1: """
The Lord Chancellor shakes his head. "Duplicate accounts in both realms?
The administrative burden would be immense! When someone leaves service,
we would need to coordinate with the Eastern Kingdom to revoke their
access. Federation means we each manage only our own people."
                    """,
                    3: """
The Ambassador stands abruptly. "Access to your identity vaults? What
manner of madness is this? We ask for TRUST, not access to your secrets!
Federation means we trust each other's authentication - not that we
expose our internal systems to each other!"
                    """
                }
            },
            "corporate": {
                "title": "THE PARTNER PORTAL PROJECT",
                "narrative": """
The business development team has landed a major partnership, and now
they're in your office with "just a small technical requirement."

"So our employees need to access PartnerCo's supply chain portal," the
BD lead explains. "And their engineers need to access our API documentation
system. Currently, everyone's creating separate accounts with separate
passwords and it's a mess."

She continues, "PartnerCo's IT team mentioned something called 'federation'?
They said their people could use their PartnerCo credentials to access
our systems, and our people could use our corporate credentials to access
theirs. No sharing of actual passwords between companies."

Your manager nods. "Sounds reasonable. Can you explain how this would
actually work and what we'd need to implement?"

The BD lead waits expectantly. "I need to tell their IT team we know what
we're talking about."
                """,
                "choices": [
                    {"text": "Share a master password with PartnerCo's IT team"},
                    {"text": "Create duplicate user accounts in each other's systems"},
                    {"text": "Implement federated identity using SAML or OIDC"},
                    {"text": "Give PartnerCo access to our Active Directory"}
                ],
                "success_text": """
"Federated identity using SAML or OIDC is exactly right," you confirm.
"Here's how it works: we remain the Identity Provider for our employees.
When one of our people accesses PartnerCo's portal, they're redirected
to our login. They authenticate with us - with their normal corporate
credentials that never leave our control."

You sketch a quick diagram. "We then issue a signed assertion - a
cryptographic token - that says 'We've verified this is Jane from the
Security team.' PartnerCo's system trusts that assertion because of the
federation agreement. They never see Jane's actual password."

The BD lead nods. "So the same happens in reverse when their people
access our systems?" "Exactly. Their IT team authenticates their people,
issues tokens, and our systems trust those tokens. Identity stays
controlled by each organization. Only trusted assertions cross boundaries."

FEDERATED IDENTITY enables secure cross-organization access without
sharing credentials.
                """,
                "failure_texts": {
                    0: """
Your manager stares at you. "Share a password with another company?
That violates about six of our security policies. The whole point of
federation is that credentials NEVER leave their home organization.
We trust their authentication, not access their passwords."
                    """,
                    1: """
"Duplicate accounts?" The BD lead frowns. "So every time someone joins
or leaves either company, both IT teams need to coordinate? That's not
scalable. Federation means each company manages only their own identities.
We just trust each other's authentication."
                    """,
                    3: """
"Give them access to Active Directory?!" Your manager nearly spits out
his coffee. "That's our crown jewels! Federation means we trust their
authentication system, and they trust ours. Nobody gets access to each
other's directory services. Just trust assertions, nothing more."
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Federated Identity allows users to authenticate with their home organization
(the Identity Provider) and access partner services (Service Providers)
through trusted assertions/tokens like SAML or OIDC. Actual credentials
never leave the home organization - only cryptographically signed assertions
of identity are shared. This enables secure cross-organization access without
duplicating accounts or sharing passwords.
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Federated Identity"
    },

    # Scenario 4: Access Control Models (RBAC)
    {
        "id": "d5_guild_permissions",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE GUILD PERMISSIONS QUANDARY",
                "narrative": """
The Master of the Scribe's Guild approaches you with frustration evident
in every step. "A new scribe has joined our ranks! Young Elara, fresh
from the Academy. She should have the same access as every other scribe -
entry to the Copying Halls, the Ink Stores, the Lesser Archives."

He throws up his hands. "But every time we get a new scribe, the Master
of Keys must individually grant access to each location. It takes days!
Meanwhile, Elara sits idle. There must be a better way!"

The Lord Chamberlain, who oversees the castle's access systems, nods
thoughtfully. "We could define a 'Scribe' role with all appropriate
permissions. When someone is designated a Scribe, they automatically
inherit all those permissions. When they leave the guild or advance to
Senior Scribe, their role - and thus their access - changes accordingly."

He turns to you. "What do your security texts call this approach?"
                """,
                "choices": [
                    {"text": "Discretionary Access Control - the Guild Master grants access at his discretion"},
                    {"text": "Mandatory Access Control - access based on classification labels"},
                    {"text": "Role-Based Access Control - permissions assigned to roles, users assigned to roles"},
                    {"text": "Rule-Based Access Control - conditional rules based on time or location"}
                ],
                "success_text": """
"This is Role-Based Access Control - RBAC," you explain. "Instead of
granting individual permissions to each scribe, we define a 'Scribe'
role. The role includes: access to Copying Halls, access to Ink Stores,
access to Lesser Archives. Any other permissions scribes need."

You continue, "When Elara joins the guild, we simply assign her to the
Scribe role. She automatically inherits ALL permissions associated with
that role. When Marcus advances to Senior Scribe, we change his role -
his permissions change automatically."

The Master of Keys looks relieved. "So I define roles once, and then
merely assign people to roles? Instead of tracking hundreds of individual
permission grants?"

"Exactly. And when scribes should no longer access the Ink Stores, we
change the role definition - ALL scribes' access updates automatically."

RBAC simplifies access management through role assignments.
                """,
                "failure_texts": {
                    0: """
"That is what we do NOW," the Master of Keys sighs. "The Guild Master
requests access for each new member, and I grant it at my discretion,
location by location. DAC requires individual grants by resource owners.
The Chamberlain's proposal is different - assign roles, not individual
permissions."
                    """,
                    1: """
The Chamberlain shakes his head. "Mandatory Access Control uses security
classifications - Secret, Confidential, Restricted. The system compares
user clearance to document classification. We are not discussing labels
and classifications here, but job functions and roles."
                    """,
                    3: """
"Rule-based access uses conditions," the Chamberlain corrects. "A rule
might say 'scribes may access the Copying Halls only during daylight.'
That is different from grouping permissions by job function. We want to
assign access based on ROLE, not based on time or location conditions."
                    """
                }
            },
            "corporate": {
                "title": "THE NEW ACCOUNTANT PROBLEM",
                "narrative": """
It's Monday morning and Maria from HR is at your desk looking frazzled.

"New hire starts today in Accounting. Sarah Chen. She needs access to
the financial systems, the ERP, the expense platform, the budget
dashboards - basically everything the other accountants have."

She holds up a thick folder. "Currently, I have to submit seventeen
separate access request tickets. Each one goes to a different system
owner. Takes two weeks to get someone fully provisioned. It's insane."

Your manager walks over. "Didn't we implement that role-based system
last quarter? Where you define 'Accountant' as a role with all the
standard permissions, and just assign people to the role?"

Maria looks hopeful. "If that's working, I just need to request Sarah
be added to the Accountant role and she gets everything automatically?"

She turns to you. "What's this approach called again? I need to use
the right term in my email to IT."
                """,
                "choices": [
                    {"text": "Discretionary Access Control - system owners grant access individually"},
                    {"text": "Mandatory Access Control - access based on security clearance levels"},
                    {"text": "Role-Based Access Control - permissions tied to job roles"},
                    {"text": "Rule-Based Access Control - access rules based on conditions"}
                ],
                "success_text": """
"Role-Based Access Control - RBAC," you confirm. "Here's how it works:
IT defines an 'Accountant' role that includes all the permissions
accountants need. ERP access, financial system access, expense platform,
budget dashboards - all bundled into that role."

You pull up the access management portal. "When Sarah is designated as
an Accountant, she inherits all permissions from that role automatically.
No seventeen separate tickets. One role assignment."

Maria is already typing. "And when she transfers to Marketing next year,
we change her role and her access updates automatically?"

"Exactly. The beauty of RBAC is that permissions are managed through
roles, not individual grants. Change the role definition, everyone with
that role is updated. Change someone's role, their permissions change
to match."

Maria heads off happily. RBAC makes access management scalable.
                """,
                "failure_texts": {
                    0: """
Maria sighs. "That's what we're doing NOW. Each system owner grants
access at their discretion. Seventeen tickets, seventeen approvals,
two weeks of waiting. The whole point of roles is to bundle permissions
together so one assignment covers everything."
                    """,
                    1: """
Your manager shakes his head. "MAC is for classified environments -
Secret, Top Secret, that kind of thing. Access based on clearance
levels and data classification. We're talking about job functions
here, not security classifications. Think roles, not labels."
                    """,
                    3: """
"Rule-based would be things like 'access only during business hours'
or 'access only from the office network,'" your manager explains.
"We're talking about grouping permissions by job function - Accountant,
Developer, Manager. That's role-based, not rule-based."
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Role-Based Access Control (RBAC) assigns permissions to ROLES (like Accountant,
Developer, Manager), and users are assigned to roles. Users inherit all
permissions associated with their role(s). This simplifies access management
- instead of tracking individual permissions for each user, administrators
manage role definitions and role assignments. When users change jobs, their
role changes and permissions update automatically.
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Access Control Models (RBAC)"
    },

    # Scenario 5: Principle of Least Privilege
    {
        "id": "d5_emergency_access_request",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE ALCHEMIST'S REQUEST",
                "narrative": """
Aldric the Alchemist stands before the Council, his request causing
murmurs among the members. "I petition for permanent access to the
Forbidden Reagent Vault! Last moon, when the plague struck, I needed
components urgently. The delay in obtaining access cost lives!"

His voice rises with emotion. "Grant me standing access so I may respond
instantly when the next emergency arises!"

The Master of Security raises his hand. "The Forbidden Vault contains
substances that could devastate the kingdom if misused. How many times
in the past year have you actually needed emergency access?"

Aldric considers. "Twice. Perhaps thrice."

The Council turns to you. "What approach best balances the Alchemist's
legitimate need with the security of the realm? He speaks of emergencies,
yet permanent access seems... excessive."
                """,
                "choices": [
                    {"text": "Grant the permanent access as requested - emergencies require immediate response"},
                    {"text": "Deny all access to the Vault - the risk is too great for any alchemist"},
                    {"text": "Provide time-limited, just-in-time elevated access when emergencies arise"},
                    {"text": "Grant permanent read-only access to view the vault's contents"}
                ],
                "success_text": """
"The principle of least privilege guides us here," you explain. "Aldric
needs access rarely - perhaps thrice yearly. Granting permanent access
means 362 days of unnecessary risk each year."

You outline the solution: "Instead, we establish just-in-time access.
When an emergency arises, Aldric requests elevated access. A quick
approval from the Night Watch Captain or the Master of Healers - who
can verify the emergency - and access is granted immediately. The access
automatically expires after the emergency passes."

Aldric considers. "So I get what I need when I need it, but not when I
don't?" "Precisely. Minimum access, minimum time. If your credentials
were ever compromised on an ordinary day, the attacker gains nothing -
you have no standing access to compromise."

The Council nods approval. "Just-in-time access it is. The protection
of least privilege with the flexibility of emergency response."

LEAST PRIVILEGE means minimum access for minimum time.
                """,
                "failure_texts": {
                    0: """
The Master of Security shakes his head firmly. "Permanent access for
a once-per-season need? If Aldric's credentials are ever stolen or
coerced, the attacker has unlimited vault access. Least privilege
means providing access only when needed, for only as long as needed."
                    """,
                    1: """
The Master of Healers objects. "Deny all access? Then when the next
plague strikes, we watch people die while bureaucracy prevents our
alchemist from obtaining treatments? Least privilege does not mean
NO privilege - it means the MINIMUM necessary privilege, when necessary."
                    """,
                    3: """
"Read-only access to the Forbidden Vault?" Aldric looks confused.
"I need to TAKE the reagents, not merely observe them! And permanent
read access still provides intelligence to any who compromise my
credentials. The right answer is temporary full access when genuinely
needed, not permanent partial access."
                    """
                }
            },
            "corporate": {
                "title": "THE DEVELOPER'S REQUEST",
                "narrative": """
The senior developer sits across from you in the access review meeting,
making his case with practiced frustration.

"I need permanent admin access to production. Last month, there was a
critical bug at 2 AM. By the time I got emergency access approved, we'd
lost four hours of uptime. FOUR HOURS. Do you know what that cost us?"

He leans forward. "Just give me standing admin access. I've been here
eight years. I'm trustworthy. I promise I won't touch anything unless
there's an actual emergency."

Your manager pulls up the access logs. "How many times in the past year
have you actually needed emergency production access?"

The developer thinks. "Maybe three, four times?"

Your manager turns to you. "What's the security-appropriate way to handle
this request? The business need is real, but permanent admin access to
production..."
                """,
                "choices": [
                    {"text": "Grant permanent admin access - he's trustworthy and emergencies are real"},
                    {"text": "Deny all production access - developers shouldn't touch production"},
                    {"text": "Implement just-in-time access with time-limited approval workflow"},
                    {"text": "Grant permanent read-only admin access as a compromise"}
                ],
                "success_text": """
"Just-in-time access with a streamlined approval workflow," you recommend.
"Here's why: Dave needs emergency access maybe four times a year. If we
give him permanent admin access, we're accepting 361 days of unnecessary
risk for 4 days of genuine need."

You pull up the PAM system. "With just-in-time access, Dave requests
elevation when there's an actual emergency. An on-call approver - could
be the SRE lead or the security duty officer - approves it in minutes.
He gets full admin access, it's logged, and it automatically expires
after a set period."

Dave considers. "So if my credentials get phished tomorrow, the attacker
gets... nothing? Because I don't have standing access to production?"

"Exactly. And if someone compromises the PAM system, they still need to
justify and get approval for access. Layers of protection."

LEAST PRIVILEGE + JUST-IN-TIME ACCESS = security without impediment.
                """,
                "failure_texts": {
                    0: """
Your manager shakes his head. "Eight years of trust doesn't mean eight
years of need. What if Dave's laptop gets stolen? Or he clicks a
phishing link? Permanent admin access means the attacker gets permanent
admin access. Least privilege means minimum access for minimum time."
                    """,
                    1: """
"No production access at all?" Dave looks incredulous. "So when prod
is down at 2 AM, I just... watch? The SRE team is three people, and
sometimes I know the code better than they do." Least privilege isn't
zero privilege - it's the minimum needed, when it's needed.
                    """,
                    3: """
"Read-only admin?" Dave frowns. "That doesn't help when I need to
actually FIX things. And permanent read access still lets an attacker
see production data, configuration, secrets - plenty of damage possible.
The right answer is full access when genuinely needed, automatically
revoked when not."
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
The Principle of Least Privilege means granting MINIMUM access needed for
MINIMUM time needed. Just-in-time (JIT) access implements this by providing
elevated privileges only when required, with automatic revocation after the
need passes. This reduces the window of exposure if credentials are compromised
while still enabling legitimate emergency response.
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Least Privilege and Just-In-Time Access"
    },

    # Scenario 6: Privileged Access Management
    {
        "id": "d5_keymaster_audit",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE KEYMASTER'S DILEMMA",
                "narrative": """
The Royal Auditors have completed their inspection, and their findings
are grim. The Chief Auditor spreads parchments across the table.

"Your Keymasters - those who maintain the kingdom's most critical locks
and wards - each knows the master passphrases by heart. They use them
directly. There is no record of when or why they access the Royal
Vaults, the Dragon Treasury, or the Seal Archives."

She taps a damning report. "Last month, fifty gold bars vanished from
the Dragon Treasury. Every Keymaster had direct access. No one can
account for who entered when. There is no accountability."

The Lord Chamberlain is ashen. "We trust our Keymasters..."

"Trust is not accountability," the Auditor replies. "The Council demands
a solution that provides control over privileged access with full
tracking of who accessed what, when, and why."
                """,
                "choices": [
                    {"text": "Require Keymasters to change their passphrases monthly"},
                    {"text": "Implement a vault system with credential checkout, session recording, and automatic rotation"},
                    {"text": "Share one master passphrase among all Keymasters for simplicity"},
                    {"text": "Remove all Keymaster positions - no one should have such access"}
                ],
                "success_text": """
"The solution is a Privileged Access Management approach," you explain.
"The Keymasters will no longer know the master passphrases directly.
Instead, passphrases are stored in an enchanted vault - a secure
credential repository."

You outline the system: "When a Keymaster needs access, they request it
from the vault. The vault records the request - who, when, why. The
Keymaster is granted temporary use of the credential, and their entire
session is recorded by scrying mirrors. When done, the vault automatically
changes the passphrase."

The Chief Auditor nods. "So if gold vanishes again, you know exactly
which Keymaster accessed the Treasury, what they did, and when?"

"Precisely. Individual accountability through session recording.
Controlled access through the vault. And if a Keymaster leaves service,
they take no secrets with them - the vault holds the credentials, not
their memory."

PAM provides control, accountability, and credential protection.
                """,
                "failure_texts": {
                    0: """
The Chief Auditor sighs. "Monthly passphrase changes? The Keymasters
will still know the current passphrase. They can still access vaults
without accountability. Rotation without vaulting solves nothing.
We need to control access and record actions, not just change secrets."
                    """,
                    2: """
"One shared passphrase?" The Lord Chamberlain is aghast. "Then we have
even LESS accountability! Currently, at least each Keymaster has their
own credentials. A shared passphrase makes it impossible to distinguish
who accessed what. This is the opposite of our requirement."
                    """,
                    3: """
"Remove all Keymasters?" The Chief Auditor raises an eyebrow. "Then
who maintains the locks? Who responds when the Dragon Treasury needs
emergency access? Privileged access is necessary - the question is
controlling and auditing that access, not eliminating it entirely."
                    """
                }
            },
            "corporate": {
                "title": "THE ADMIN ACCOUNT AUDIT",
                "narrative": """
The external auditors have flagged a finding and your CISO is not happy.

"Our system administrators know the root passwords to every critical
server by heart," she reads from the audit report. "They access systems
directly using these credentials. There is no record of which admin
accessed which system, when, or what actions they performed."

She looks up. "Last quarter, someone made unauthorized configuration
changes to the financial database. Every sysadmin had access. We can't
determine who did it because there's no accountability for privileged
access."

The IT Director shifts uncomfortably. "We trust our admins..."

"Trust isn't an audit control," the CISO replies. "We need a solution
that provides accountability and control over privileged access. What
do you recommend?"
                """,
                "choices": [
                    {"text": "Require admins to change passwords monthly"},
                    {"text": "Implement a PAM solution with credential vaulting and session recording"},
                    {"text": "Share one admin account among all administrators for simplicity"},
                    {"text": "Remove all administrator accounts from the systems"}
                ],
                "success_text": """
"We need a Privileged Access Management solution," you explain. "Here's
how it works: admin credentials are stored in a secure vault. Admins
don't know the actual passwords - they request access through the PAM
system."

You outline the architecture: "When an admin needs root access, they
check out the credential from the vault. The PAM system logs who requested
access, to which system, with what justification, and when. The admin's
entire session is recorded. When they're done, the credential is checked
back in and automatically rotated."

The CISO nods. "So next time something unauthorized happens, we have a
complete record?"

"Video-like session recordings, command logs, who accessed what and when.
And when someone leaves the company, they take nothing with them - the
vault holds the credentials, and we can rotate them immediately."

PAM provides accountability and control over privileged access.
                """,
                "failure_texts": {
                    0: """
The CISO shakes her head. "Password rotation doesn't help if admins
still know and directly use the credentials. We need to control ACCESS
and record ACTIONS, not just change passwords monthly. The audit
finding is about accountability, not rotation frequency."
                    """,
                    2: """
"A shared admin account?" The CISO's eyes widen. "That ELIMINATES
accountability entirely! 'Someone' made changes becomes 'anyone could
have made changes.' This makes the audit finding worse, not better.
We need individual accountability, not anonymous shared access."
                    """,
                    3: """
"Remove all admin accounts?" The IT Director protests. "Then who patches
the servers? Who responds to incidents? Privileged access is necessary -
the question is how to control and audit it, not whether to have it at
all. Systems don't administer themselves."
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Privileged Access Management (PAM) solutions address accountability for
privileged users by: 1) Vaulting credentials so admins don't know actual
passwords, 2) Requiring checkout/check-in for credential use, 3) Recording
sessions for audit trails, 4) Automatically rotating credentials after use.
This provides control and accountability while enabling necessary administrative
functions.
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Privileged Access Management"
    },

    # Scenario 7: Account Lifecycle
    {
        "id": "d5_departing_guardian",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE GUARDIAN'S FAREWELL",
                "narrative": """
Sir Marcus has served the Citadel faithfully for twenty years, but age
and weariness have caught up with him. He has announced his retirement
from the Guardian Corps, effective at week's end.

The Master of Rosters approaches you with the delicate question. "Sir
Marcus still holds keys to the Armory, knowledge of patrol passwords,
and access runes to the Inner Sanctum. When should we revoke these
privileges?"

He presents several perspectives: "Some say immediately upon his
announcement - why risk his continued access during his notice period?
Others argue we should wait a fortnight after he departs, to ease the
transition. Sir Marcus himself suggests we simply leave his access active
'in case you need me to consult.'"

The Master looks troubled. "Sir Marcus is honorable, but principles must
guide our decision, not personal trust. When is the proper time to revoke
a departing guardian's access?"
                """,
                "choices": [
                    {"text": "Immediately when he announced his retirement"},
                    {"text": "On his last day, coordinated with his departure"},
                    {"text": "One fortnight after departure, to ensure smooth transition"},
                    {"text": "Only when Sir Marcus himself requests deactivation"}
                ],
                "success_text": """
"Access should be revoked on Sir Marcus's last day, coordinated with
his physical departure," you advise. "The principle is clear: active
employees need access to perform their duties. Former employees, no
matter how trusted, should not retain access to organizational resources."

You explain the reasoning: "Revoking immediately upon his announcement
would prevent Sir Marcus from completing his final duties and knowledge
transfer. But leaving access active after he departs creates risk - even
if Sir Marcus is honorable, his credentials could be compromised, or
circumstances could change."

The Master nods. "So on the evening of his last day, as he leaves the
Citadel for the final time, we revoke his access runes and change the
patrol passwords he knew?"

"Precisely. Dignity and security together. He completes his service
with full capability, and the moment he is no longer serving, his
access ends."

ACCOUNT LIFECYCLE: Access ends when employment ends.
                """,
                "failure_texts": {
                    0: """
"Immediately?" The Master frowns. "Sir Marcus has a week of service
remaining. He must complete knowledge transfer, final patrols, and
handover of his responsibilities. Revoking access now prevents him
from doing his job during his legitimate notice period."
                    """,
                    2: """
"A fortnight AFTER departure?" The Master looks alarmed. "For two weeks,
a former guardian - no longer bound by oath or oversight - retains
access to the Armory and Inner Sanctum? If his credentials were stolen,
we would not even know to suspect him. Access must end with employment."
                    """,
                    3: """
"When HE requests it?" The Master shakes his head firmly. "Users should
never control their own access termination. Sir Marcus might forget, or
decide he 'might need it someday.' Access is an organizational decision
based on organizational need, not personal preference."
                    """
                }
            },
            "corporate": {
                "title": "THE TWO WEEKS NOTICE",
                "narrative": """
Friday afternoon, and Jennifer from the Security Operations team just
dropped a resignation letter on her manager's desk. Two weeks notice.
She's heading to a competitor.

HR has pinged you for guidance. "Jennifer has access to the SIEM, the
vulnerability scanner, incident response procedures, and the threat
intelligence feeds. When do we revoke her access?"

They outline the options they're considering: "Legal says we COULD
revoke immediately and pay out the two weeks. Her manager says she
needs to complete knowledge transfer and shouldn't be treated like a
criminal. And Jennifer herself suggested we just 'leave things active
in case you have questions after I leave.'"

The HR rep looks at you. "What's the security-appropriate approach for
handling access when someone's leaving?"
                """,
                "choices": [
                    {"text": "Immediately upon receiving the resignation"},
                    {"text": "On her last day, coordinated with her departure"},
                    {"text": "One week after she leaves, to help with transition questions"},
                    {"text": "Only when Jennifer requests deactivation herself"}
                ],
                "success_text": """
"Access should be revoked on Jennifer's last day, coordinated with her
departure from the building," you explain. "The principle is simple:
employees need access to do their jobs. The day someone stops being an
employee, their access should stop too."

You address the concerns: "Revoking immediately might be appropriate if
she had access to extremely sensitive data or if there were concerns
about her conduct. But absent those factors, letting her work her notice
period is reasonable - she's still an employee doing her job."

The HR rep nods. "And after she leaves?"

"Zero access. Doesn't matter how trusted she was or how helpful she
wants to be. Former employees shouldn't have active credentials. If
she's truly needed for questions, she can be brought in as a consultant
with explicitly scoped access - but her permanent accounts end with
her employment."

ACCOUNT LIFECYCLE requires timely deprovisioning.
                """,
                "failure_texts": {
                    0: """
"Immediately?" Her manager objects. "She has two weeks of work to do -
documenting procedures, transitioning responsibilities, closing out
tickets. She's going to a competitor, yes, but she's still an employee
today. We need her to finish her job before we cut access."
                    """,
                    2: """
"A week AFTER she leaves?" The HR rep looks alarmed. "So a former
employee, now working for a competitor, still has access to our SIEM
and vulnerability data? That's a recipe for data breach. Access ends
when employment ends, period."
                    """,
                    3: """
"When SHE requests it?" You shake your head. "Users don't control
their own access termination. What if she forgets? What if she thinks
'just in case' is a valid reason? Access decisions are organizational
responsibilities, not personal choices."
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Account Lifecycle Management requires that access be terminated when
employment ends - ideally on the employee's last day, coordinated with
their physical departure. Premature revocation may prevent completion of
legitimate duties. Delayed revocation creates insider threat risk from
former employees who retain active credentials. Users should never control
their own access termination.
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Account Lifecycle"
    },

    # Scenario 8: Identity Proofing
    {
        "id": "d5_new_recruit_verification",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE STRANGER AT THE GATE",
                "narrative": """
A traveler in worn robes approaches the Citadel gates, claiming to be
Sir Aldric of Northmoor, newly assigned to the Guardian Corps. He
presents a letter of assignment bearing what appears to be the Royal Seal.

The Gate Captain pulls you aside. "Before I issue this man guardian
credentials - access runes, patrol schedules, armory keys - I need to
verify he is truly who he claims. A clever impostor with the right
letter could infiltrate our ranks."

He outlines the challenge: "This Sir Aldric claims noble blood and
military service. His letter looks genuine. But how do we KNOW he is
truly Sir Aldric of Northmoor and not an enemy agent with forged
documents?"

The traveler waits patiently. "I understand your caution," he says.
"In these dangerous times, you must verify before you trust."

What process is the Gate Captain describing?
                """,
                "choices": [
                    {"text": "Authentication - verifying the traveler's passphrase"},
                    {"text": "Authorization - determining what access Sir Aldric should have"},
                    {"text": "Identity proofing - verifying the person's identity before issuing credentials"},
                    {"text": "Access certification - reviewing Sir Aldric's existing access rights"}
                ],
                "success_text": """
"This is identity proofing," you explain. "Before we issue ANY credentials
to this traveler, we must verify that he truly is Sir Aldric of Northmoor.
This happens BEFORE authentication is even possible - we cannot authenticate
someone who has no credentials yet."

You outline the process: "Send a messenger to Northmoor to verify his
service record. Have our Court Wizard examine the Royal Seal for
authenticity. Compare his face to the sketch in the military rolls.
Only when we are confident this person IS Sir Aldric do we issue the
credentials that will later be used for authentication."

The Gate Captain nods. "So identity proofing establishes who someone is.
Authentication later verifies they are still that person, using the
credentials we issued based on that proofing?"

"Exactly. Identity proofing creates the foundation of trust. Without
proper proofing, you might issue legitimate credentials to an impostor."

IDENTITY PROOFING verifies identity BEFORE credentials are issued.
                """,
                "failure_texts": {
                    0: """
The Gate Captain shakes his head. "Authentication uses existing credentials
to verify identity. But this traveler has NO credentials yet - we haven't
issued them. First, we must verify he is who he claims. That verification
process, before any credential exists, is not authentication."
                    """,
                    1: """
"Authorization comes later," the Gate Captain explains. "Once we know
he IS Sir Aldric, we determine what a knight of his rank should access.
But first, we must verify his identity - that he is Sir Aldric at all.
Authorization determines what; identity verification determines who."
                    """,
                    3: """
"Access certification reviews EXISTING access rights," the Gate Captain
notes. "Do current guardians still need their current access? But this
traveler has no existing access to certify. We must first establish his
identity before we can give him anything to later certify."
                    """
                }
            },
            "corporate": {
                "title": "THE HIGH-SECURITY ONBOARDING",
                "narrative": """
The new Director of Security is scheduled to start next Monday, but
HR has flagged a concern. "This position has access to everything -
security systems, incident reports, vulnerability data, executive
protection details. Before we issue any credentials, how do we KNOW
this person is really Alexandra Chen, the candidate we hired?"

The HR manager outlines the situation. "She passed interviews, reference
checks, and a background check. But someone pointed out that sophisticated
adversaries have been known to substitute their own agent during the
onboarding process - especially for high-value security positions."

She continues, "Before we give this person an employee badge, domain
credentials, and access to our most sensitive systems... how do we
verify she is actually the Alexandra Chen who went through our hiring
process?"

You're asked to design the pre-credential verification process. What
is this process called?
                """,
                "choices": [
                    {"text": "Authentication - verifying her password works"},
                    {"text": "Authorization - determining her access levels"},
                    {"text": "Identity proofing - verifying the person's identity before issuing credentials"},
                    {"text": "Access certification - reviewing her existing access rights"}
                ],
                "success_text": """
"This is identity proofing," you explain. "Before we issue ANY credentials
to Alexandra - domain account, badge, security system access - we must
verify that the person standing in front of us is actually Alexandra
Chen, the individual we vetted and hired."

You outline appropriate proofing measures: "Government-issued photo ID
verification. Comparison with interview recordings. Confirmation of
unique identifiers from her background check. For this level of access,
we might even require in-person verification with the hiring manager
who interviewed her."

The HR manager nods. "So identity proofing is what we do BEFORE we issue
credentials?"

"Exactly. Authentication uses credentials to verify identity later. But
first, we must establish identity to ISSUE those credentials. Without
proper identity proofing, we might give legitimate credentials to an
impostor who would then 'authenticate' successfully every day."

IDENTITY PROOFING creates the foundation for all future authentication.
                """,
                "failure_texts": {
                    0: """
The HR manager frowns. "She doesn't have a password yet - we haven't
created her account. Authentication verifies identity using existing
credentials. We need to verify her identity BEFORE we create those
credentials. That's a different process."
                    """,
                    1: """
"Authorization is what she can access once we've verified who she is,"
you correct yourself. "But first we need to verify she IS who she claims.
Authorization determines permissions; this is about establishing identity
in the first place."
                    """,
                    3: """
"Access certification reviews EXISTING access," the HR manager notes.
"Like annual reviews of current employees' permissions. This person
has no existing access to certify. We're verifying her identity before
any access is granted at all."
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Identity Proofing is the process of verifying a person's identity BEFORE
credentials are issued. This might involve document verification, background
checks, biometric capture, or in-person verification. It establishes the
foundation for trust - without proper identity proofing, you might issue
valid credentials to an impostor. Authentication uses credentials later;
proofing happens before credentials exist.
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Identity Proofing"
    },

    # Scenario 9: Session Management
    {
        "id": "d5_abandoned_scrying_pool",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE UNATTENDED SCRYING POOL",
                "narrative": """
The Master Archivist has raised a concern about the kingdom's magical
scrying pools - enchanted basins that allow authorized users to access
sensitive records and communications across the realm.

"I observed something troubling," he reports. "The Treasury Scribe
authenticated to a scrying pool this morning, then was called away to
a meeting. She never properly closed her session. When I passed by an
hour later, the pool still showed her session - fully active, with
access to financial records - completely unattended."

He wrings his hands. "Anyone could have walked up and accessed those
records as if they were the Treasury Scribe! What security control
should govern how long an unattended session remains active?"

The question is important. Scrying pools throughout the kingdom face
the same risk.
                """,
                "choices": [
                    {"text": "Password complexity requirements - stronger passwords prevent this issue"},
                    {"text": "Session timeout / idle timeout - automatically end inactive sessions"},
                    {"text": "Multi-factor authentication - require additional factors"},
                    {"text": "Account lockout policy - lock out after failed attempts"}
                ],
                "success_text": """
"The control you need is session timeout, also called idle timeout,"
you explain. "After a period of inactivity - say, fifteen minutes with
no interaction - the scrying pool should automatically terminate the
session. The next person who approaches finds the pool sealed, requiring
fresh authentication."

The Master Archivist nods. "So even if someone forgets to close their
session, the pool closes itself after a period of neglect?"

"Exactly. Session timeouts reduce the window for unauthorized access
if someone walks away from an active session. The more sensitive the
access, the shorter the timeout should be. Treasury records might
timeout after ten minutes of inactivity. Public records might allow
thirty."

He makes notes. "And this complements multi-factor authentication - MFA
protects the initial login, but session timeout protects against
abandoned sessions."

SESSION TIMEOUT protects against the risk of unattended active sessions.
                """,
                "failure_texts": {
                    0: """
The Master Archivist shakes his head. "Password complexity protects
against guessing or cracking. But the Treasury Scribe used a proper
password - her session was legitimately authenticated. The problem is
that the session STAYED active after she left. Password strength
doesn't help when someone walks away without logging out."
                    """,
                    2: """
"Multi-factor authentication protects the initial login," the Archivist
notes. "The Treasury Scribe DID authenticate properly with multiple
factors. But then she walked away and left the session open. MFA
doesn't protect against abandoned sessions - it protects against
unauthorized initial access."
                    """,
                    3: """
"Account lockout prevents brute-force password attacks," the Archivist
explains. "Lock the account after five wrong guesses. But the Treasury
Scribe logged in correctly - there were no failed attempts. Lockout
doesn't address legitimate sessions that are left unattended."
                    """
                }
            },
            "corporate": {
                "title": "THE OPEN WORKSTATION",
                "narrative": """
The security team's weekly patrol report has identified a recurring
issue. "Multiple workstations left logged in and unattended," the
report notes. "Accounting, HR, even the CEO's office."

The IT Director reviews the findings. "I walked past Sarah's desk
yesterday. She'd been in a meeting for an hour. Her workstation was
still logged in with the HR database open on screen. Anyone could
have walked up and accessed employee records as 'Sarah.'"

She looks at you. "We've done the security awareness training. People
know they should lock their screens. But they forget, they get called
away suddenly, things happen. What technical control addresses this
problem?"

The CEO chimes in from across the table. "And don't tell me to require
login every five minutes. My people need to work, not re-authenticate
constantly."
                """,
                "choices": [
                    {"text": "Password complexity requirements - stronger passwords prevent this"},
                    {"text": "Session timeout / idle timeout - automatically lock after inactivity"},
                    {"text": "Multi-factor authentication - require additional factors to login"},
                    {"text": "Account lockout policy - lock accounts after failed login attempts"}
                ],
                "success_text": """
"Session timeout or idle timeout," you recommend. "Configure workstations
and applications to automatically lock or terminate sessions after a
period of inactivity. Fifteen minutes for general workstations, shorter
for sensitive systems."

The CEO frowns. "Fifteen minutes of inactivity, then they have to log
back in?"

"Yes, but that's the balance. If Sarah is genuinely working, she's
interacting with the system - no timeout. If she walks away, fifteen
minutes of idle time and the screen locks. If someone approaches her
desk while she's gone, they find a locked workstation, not an open
HR database."

The IT Director nods. "And sensitive applications like HR or Finance
could have even shorter timeouts?"

"Exactly. Session timeout is the technical control that catches human
forgetfulness. Awareness training says 'lock your screen.' Session
timeout says 'if you forget, the system locks itself.'"

SESSION TIMEOUT is a compensating control for human behavior.
                """,
                "failure_texts": {
                    0: """
The IT Director shakes her head. "Password complexity protects against
weak passwords being guessed. But Sarah's password is fine - she
logged in successfully. The problem is she walked away with the
session still active. Password strength doesn't help when the session
is legitimately open and unattended."
                    """,
                    2: """
"MFA is great for protecting the initial login," the IT Director agrees.
"But Sarah authenticated successfully, probably with MFA. Then she
left her session open. MFA doesn't protect against 'logged in and
walked away' - it protects against unauthorized initial authentication."
                    """,
                    3: """
"Account lockout is for failed login attempts," the IT Director
explains. "Too many wrong passwords, lock the account. But there
were no failed attempts here - Sarah logged in correctly, then left.
Lockout doesn't address legitimate sessions left unattended."
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Session Timeout (also called idle timeout) automatically terminates sessions
after a period of inactivity. This reduces the window for unauthorized access
if a user walks away from an authenticated session. Session timeout is a
compensating control for human forgetfulness - users SHOULD lock their screens,
but the system protects against situations where they forget.
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Session Management"
    },

    # Scenario 10: Access Recertification
    {
        "id": "d5_accumulating_keys",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE COLLECTION OF FORGOTTEN KEYS",
                "narrative": """
The Royal Auditors have discovered something disturbing. Sir Bartholomew,
now Captain of the Northern Watch, still holds keys and access runes
from every position he has held over his thirty-year career.

"He retains access to the Scribe's Archives from when he was a clerk,"
the auditor reads. "Access to the Smithy from his apprentice days.
Treasury access from his time as a quartermaster. Kitchen stores from
his first posting as a guard. Access he accumulated but never
relinquished as his duties changed."

The Lord Chamberlain looks pained. "Sir Bartholomew is loyal and would
never abuse these accesses. But the principle is concerning. How many
others hold keys they no longer need?"

The auditor looks at you. "What process should we implement to prevent
this accumulation of unnecessary access?"
                """,
                "choices": [
                    {"text": "More frequent password changes will address this"},
                    {"text": "Periodic access reviews and recertification by managers"},
                    {"text": "Stronger authentication requirements will prevent abuse"},
                    {"text": "Network segmentation will contain the risk"}
                ],
                "success_text": """
"You need periodic access reviews and recertification," you explain.
"Regularly - quarterly or annually - each person's manager must review
their access rights and certify that they are still appropriate for
their current role."

You outline the process: "Sir Bartholomew's current commander reviews
his access. 'Northern Watch access? Yes, he needs that. Treasury access?
No, he hasn't been quartermaster for fifteen years - revoke it.' The
commander certifies appropriate access and flags inappropriate access
for removal."

The Lord Chamberlain nods. "So access that creeps in over time gets
caught during these reviews?"

"Exactly. Access recertification prevents privilege accumulation. It
enforces least privilege over the long term, catching access that was
once appropriate but is no longer needed. Without regular recertification,
access only ever grows - it's rarely removed until a problem occurs."

ACCESS RECERTIFICATION prevents privilege accumulation over time.
                """,
                "failure_texts": {
                    0: """
The auditor frowns. "Password changes? Sir Bartholomew changes his
passwords regularly. That doesn't change the fact that he has ACCESS
he doesn't need. Password rotation is about credential freshness, not
about whether someone should have access in the first place."
                    """,
                    2: """
"Stronger authentication?" The auditor shakes his head. "Sir Bartholomew
authenticates properly. The problem is he has TOO MUCH authorized
access, not that his authentication is weak. We need to review what
access he SHOULD have, not make him authenticate more strongly."
                    """,
                    3: """
"Network segmentation controls network traffic," the auditor notes.
"It doesn't address the fundamental problem that Sir Bartholomew holds
access to locations his current role doesn't require. The access needs
to be reviewed and revoked, not just segmented."
                    """
                }
            },
            "corporate": {
                "title": "THE ACCESS ACCUMULATION PROBLEM",
                "narrative": """
The annual audit has uncovered an uncomfortable pattern. David from
Marketing has access to systems from every department he's touched in
his twelve years at the company.

"Finance systems from when he helped with the budget three years ago,"
the auditor reads. "Engineering repos from the product launch five years
ago. HR database from... honestly, no one remembers why he had that.
Customer database from his sales days. He has more access than most
executives."

David's manager looks surprised. "I had no idea he had all that access.
He only needs the Marketing tools for his current role."

The CISO turns to you. "This isn't just David - our audit found this
pattern across the organization. People accumulate access but it's
never removed as their roles change. What process should we implement?"
                """,
                "choices": [
                    {"text": "More frequent password changes will address this"},
                    {"text": "Periodic access reviews and recertification by managers"},
                    {"text": "Stronger multi-factor authentication will prevent abuse"},
                    {"text": "Network segmentation will contain the risk"}
                ],
                "success_text": """
"Access recertification," you recommend. "Quarterly or annually, every
manager reviews their team's access rights. For each system, they
certify: does this person still need this access for their current job?"

You outline the process: "David's Marketing manager reviews his access.
Marketing tools? Certified. Finance systems? 'He doesn't do budgets
anymore - remove.' Engineering repos? 'No need - remove.' The manager
certifies appropriate access and revokes the rest."

The CISO nods. "And if a manager certifies access they shouldn't?"

"That's a secondary review - sensitive systems might require additional
approval. And the audit trail shows who certified what, creating
accountability. The key is that access gets REVIEWED regularly instead
of accumulating forever."

David's manager shrugs. "Seems reasonable. I should know what my team
has access to."

ACCESS RECERTIFICATION maintains least privilege over time.
                """,
                "failure_texts": {
                    0: """
The CISO shakes her head. "David changes his password regularly. That
doesn't address the fact that he HAS access to twelve systems he
doesn't need. Password rotation is about credential security, not
about appropriate access levels."
                    """,
                    2: """
"MFA doesn't help here," the CISO notes. "David authenticates properly.
The problem is he has access to things he shouldn't - not that his
authentication is weak. We need to review and revoke inappropriate
access, not add more authentication factors."
                    """,
                    3: """
"Segmentation controls network paths," the CISO explains. "It doesn't
address application-level access. David can still access the HR
database if he's authorized, regardless of network segments. We need
to review whether that authorization is still appropriate."
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Access Recertification (also called access review) requires managers to
periodically review and confirm that their employees' access rights are
still appropriate for their current roles. This process catches privilege
accumulation - the tendency for access to grow over time as people take
on new responsibilities without losing old access. Recertification enforces
least privilege over the long term.
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Access Recertification"
    },

    # Scenario 11: Just-In-Time Access
    {
        "id": "d5_vault_access_protocol",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE VAULT KEEPER'S DILEMMA",
                "narrative": """
The Master Smith occasionally needs access to the Rare Metals Vault -
perhaps twice a month when unusual work requires mithril or starsilver.
He has requested permanent access to streamline his work.

"I am trusted with the kingdom's finest weapons," he argues. "Why must
I petition for vault access each time? Grant me standing access and
spare us all the bureaucracy."

The Vault Keeper considers the request. "The Rare Metals Vault contains
not just valuable materials but ones that could be catastrophic if
misused. Permanent access for someone who needs it twice monthly seems...
excessive."

She turns to you. "What approach balances the Master Smith's legitimate
needs with the security of materials that could threaten the kingdom?"
                """,
                "choices": [
                    {"text": "Grant permanent access - he's proven trustworthy"},
                    {"text": "Require personal accounts for each vault access"},
                    {"text": "Implement just-in-time access with time-limited approval"},
                    {"text": "Block all Smith access - too risky for anyone"}
                ],
                "success_text": """
"Just-in-time access," you recommend. "When the Master Smith needs
rare metals, he requests access. The Vault Keeper or an approver
verifies the legitimate need - perhaps cross-referencing the work order
for that enchanted blade. Access is granted immediately and automatically
expires after the specific task is complete."

The Master Smith frowns. "So I request each time?"

"Yes, but the approval can be swift for legitimate needs. The benefit is
this: if your credentials were ever stolen, or if circumstances changed
and you were compromised, the attacker would find you have no standing
vault access. They would have to request access themselves, triggering
review and likely rejection."

The Vault Keeper nods. "And we have a record of each access - who,
when, why - rather than unlimited access with no accountability?"

"Precisely. Just-in-time access implements least privilege while still
enabling necessary work."

JUST-IN-TIME ACCESS: access only when needed, for only as long as needed.
                """,
                "failure_texts": {
                    0: """
The Vault Keeper shakes her head. "Trust today doesn't guarantee trust
tomorrow. And if his credentials are compromised, the attacker inherits
that permanent access. Just-in-time means the window of risk is only
as long as the actual need - not permanent."
                    """,
                    1: """
"Personal accounts for each access?" The Master Smith looks confused.
"That is what he already has - a personal account. The question is
whether that account has STANDING access or TEMPORARY access. Personal
accounts don't address the duration of access."
                    """,
                    3: """
"Block all access?" The Vault Keeper looks alarmed. "Then how does he
work with rare metals? The kingdom's finest weapons require these
materials. We cannot block legitimate work - we must enable it securely.
Just-in-time access grants access when genuinely needed."
                    """
                }
            },
            "corporate": {
                "title": "THE PRODUCTION ACCESS DEBATE",
                "narrative": """
The architecture review is getting heated. The SRE team lead is pushing
back on a new access policy.

"My team needs production access for incident response," she argues.
"But this new policy says we can only have 'just-in-time' access -
request it when we need it, get approval, time-limited. What happens
at 3 AM when production is down and the approvers are asleep?"

The Security Architect responds. "The policy includes 'break glass'
emergency access with after-the-fact review. But for routine access,
yes - we want just-in-time rather than standing access."

The SRE lead crosses her arms. "My team is trustworthy. We've never
abused production access."

The CISO turns to you. "Explain why just-in-time access matters even
for trusted teams with legitimate needs."
                """,
                "choices": [
                    {"text": "Grant permanent production access to the SRE team"},
                    {"text": "Create shared accounts for production incident response"},
                    {"text": "Implement just-in-time access with streamlined workflow for incidents"},
                    {"text": "Block all SRE production access to eliminate risk"}
                ],
                "success_text": """
"Just-in-time access protects even trustworthy teams," you explain.
"Consider: if one of your team members gets phished and an attacker
captures their session, what do they get? With standing access - full
production access. With just-in-time - nothing, until they request
access and get approval."

You continue, "The approval workflow can be streamlined for genuine
incidents. On-call approvers. Rapid approval with post-incident review.
'Break glass' emergency access with mandatory after-action documentation.
The goal isn't to slow down incident response - it's to ensure that
access only exists when there's genuine need."

The SRE lead uncrosses her arms. "So the approval adds maybe sixty
seconds to incident response, but a credential compromise gives the
attacker... nothing?"

"Exactly. The attacker would have to request access, justify it, and
hope the approver doesn't notice something's wrong. Much harder than
simply using standing access that's always available."

JUST-IN-TIME ACCESS limits blast radius from credential compromise.
                """,
                "failure_texts": {
                    0: """
The CISO shakes his head. "If anyone on that team gets compromised,
the attacker has full production access immediately. Just-in-time means
a compromised credential has no standing access to exploit - the
attacker would have to request and justify access separately."
                    """,
                    1: """
"Shared accounts?" The Security Architect looks horrified. "Then we
lose all individual accountability. When something goes wrong in
production at 3 AM, we need to know WHO made what changes. Shared
accounts are the opposite of secure access management."
                    """,
                    3: """
"Block all access?" The SRE lead throws up her hands. "Then who
responds to production incidents? The whole point is enabling
necessary work securely, not preventing work entirely. Just-in-time
access enables work while limiting standing risk."
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Just-In-Time (JIT) Access grants temporary, time-limited elevated access
only when needed, with approval workflow and automatic expiration. This
implements least privilege by ensuring users don't have standing access
to sensitive systems - they request it when needed and it expires when done.
JIT access limits the blast radius from credential compromise since stolen
credentials have no standing access to exploit.
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Just-In-Time Access"
    },

    # Scenario 12: Service Accounts
    {
        "id": "d5_golem_credentials",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE GOLEM'S SECRET",
                "narrative": """
The enchanted golem that maintains the Grand Library has a problem. For
years, it has accessed the restricted stacks using a passphrase - a
secret word inscribed on a hidden scroll within its chest cavity.

"The passphrase has never been changed since the golem's creation,"
the Master Librarian reports. "The scroll is visible to anyone who
opens the golem's maintenance panel. And the passphrase is the same
one used by the Archival Golems in the Treasury - someone thought
sharing secrets would be simpler."

He looks worried. "If anyone discovered that passphrase, they could
access both the Library stacks AND the Treasury archives, pretending
to be a golem. What is the BEST way to secure our golem's access?"
                """,
                "choices": [
                    {"text": "Change the passphrase once per year"},
                    {"text": "Use magical identity binding - the golem is recognized by its essence, not a secret"},
                    {"text": "Encrypt the scroll inside the golem's chest"},
                    {"text": "Use a simpler passphrase for easier rotation"}
                ],
                "success_text": """
"The solution is magical identity binding," you explain. "Instead of
a passphrase that could be stolen or shared, the golem is recognized
by its unique magical essence - something inherent to this specific
golem that cannot be copied or transferred."

You outline the approach: "Think of it like binding the golem's identity
to its physical form. The restricted stacks recognize THIS golem, not
any entity that knows the right passphrase. No secret to steal. No
password to share between golems. No scroll to discover."

The Master Librarian nods. "So if someone opened the maintenance panel,
they would find... nothing useful?"

"Exactly. The golem's identity is tied to its existence, not to knowledge
of a secret. In the modern tongue, this is like managed identities or
certificate-based authentication for non-human entities. The identity
IS the golem, not something the golem KNOWS."

MANAGED IDENTITIES eliminate stored secrets for service accounts.
                """,
                "failure_texts": {
                    0: """
The Master Librarian shakes his head. "Annual passphrase changes still
leave the passphrase vulnerable to discovery. And if it's on a scroll
in the golem's chest, whoever finds it has access until the next
rotation - perhaps a year of unauthorized access."
                    """,
                    2: """
"Encrypting the scroll?" The Librarian looks skeptical. "Then how does
the golem read it? We would need another secret to decrypt the first
secret. We are adding complexity, not solving the problem. The fundamental
issue is having a stealable secret at all."
                    """,
                    3: """
"A simpler passphrase is WORSE security," the Librarian protests.
"Easier to guess, easier to remember by those who see it. The solution
is not to make the secret simpler - it's to eliminate the need for a
stealable secret entirely."
                    """
                }
            },
            "corporate": {
                "title": "THE SERVICE ACCOUNT SECRET",
                "narrative": """
The security assessment of your cloud environment has found a concerning
pattern. A critical application uses a service account to connect to
the database, and the password for that service account is stored in
a configuration file on the application server.

"The password has never been rotated," the assessor notes. "It's in
plaintext in config.ini. The same password is used by three different
applications - someone thought sharing would be easier. And it's the
only way the app can authenticate to the database."

The developer looks defensive. "It works. We've been doing it this
way for years."

The assessor turns to you. "What's the BEST way to secure this service
account access?"
                """,
                "choices": [
                    {"text": "Rotate the password once per year"},
                    {"text": "Use managed identities or certificate-based authentication"},
                    {"text": "Encrypt the configuration file"},
                    {"text": "Use a shorter password for easier rotation"}
                ],
                "success_text": """
"Managed identities or certificate-based authentication," you recommend.
"Eliminate the stored password entirely. In cloud environments, managed
identities tie the application's identity to its compute resource - the
VM or container IS the identity, there's no password to steal."

You explain further: "With managed identities, there's no secret in a
config file. No password to rotate. No credential to share between
applications. The identity is intrinsic to the compute resource. If
someone compromises the config file, they find... nothing useful."

The developer frowns. "How does the app authenticate then?"

"The cloud platform handles it automatically. The app requests a token
from the platform, which verifies the app is running on the authorized
compute resource, and issues a short-lived token. No long-lived secrets
anywhere in the application."

MANAGED IDENTITIES eliminate stored passwords for service accounts.
                """,
                "failure_texts": {
                    0: """
The assessor shakes her head. "Annual rotation still leaves the
password vulnerable to theft from the config file. And you'd have to
coordinate rotation across three applications that share this password.
The fundamental problem is having a stealable secret at all."
                    """,
                    2: """
"Encrypting the config file?" The assessor looks skeptical. "Then the
decryption key has to be stored somewhere accessible to the application.
You've just moved the secret, not eliminated it. And now you have key
management complexity on top of the original problem."
                    """,
                    3: """
"A shorter password is LESS secure," the assessor responds firmly.
"Easier to crack, easier to remember if observed. The solution is not
to make credentials weaker but to eliminate the need for long-lived
secrets entirely."
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Service accounts (non-human identities) should use managed identities or
certificate-based authentication rather than stored passwords. Managed
identities tie identity to the compute resource - there's no password to
steal, rotate, or share. The identity is intrinsic to the application's
infrastructure, eliminating the risk of credential theft or exposure.
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Service Accounts"
    },

    # Scenario 13: Biometric Authentication
    {
        "id": "d5_blood_seal_concerns",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE BLOOD SEAL DEBATE",
                "narrative": """
The Royal Council is considering a new security measure: Blood Seals.
Each guardian would register their unique blood signature with the
castle's wards. Entry to sensitive areas would require a drop of blood
from the registered guardian - impossible to forge, impossible to
transfer to another.

"Perfect security!" declares the Minister of Defense. "No passphrase
can be overheard, no sigil can be stolen. A guardian's blood is truly
their own."

But the Master Healer raises a troubling concern. "And what happens
when a guardian's blood signature is compromised? Perhaps through
magical means - a shapeshifter who can replicate it, or a dark ritual
that copies it. A passphrase can be changed. A sigil can be reissued.
But you cannot change a person's blood."

The Council turns to you. "What is the key concern with blood-based -
that is, biometric - authentication?"
                """,
                "choices": [
                    {"text": "Blood signatures are too easy to guess"},
                    {"text": "Biometrics cannot be changed if compromised"},
                    {"text": "Blood seal wards are too expensive to implement"},
                    {"text": "Blood signatures require guardians to remember complex patterns"}
                ],
                "success_text": """
"The Master Healer has identified the critical concern," you affirm.
"Unlike passphrases, which can be changed when compromised, or sigils,
which can be reissued, biometrics - blood signatures, fingerprints,
facial patterns - cannot be replaced if compromised."

You elaborate: "If a shapeshifter or dark magic duplicates a guardian's
blood signature, that guardian's biometric is compromised FOREVER. We
cannot issue them new blood. This makes protecting the stored biometric
data critically important - and argues for storing biometric templates
locally rather than in a central vault that could be raided."

The Minister of Defense looks troubled. "So biometrics are strong for
verification but carry permanent risk if the template is stolen?"

"Exactly. This doesn't mean we shouldn't use blood seals - but we must
protect the registered signatures with utmost care, and consider them
as ONE factor among multiple, not the only protection."

BIOMETRICS cannot be changed if compromised - protect templates carefully.
                """,
                "failure_texts": {
                    0: """
The Minister of Defense snorts. "Guess a blood signature? There are
millions of possible patterns. Blood signatures are not vulnerable to
guessing like simple passphrases. The concern is what happens if the
signature is COPIED, not guessed."
                    """,
                    2: """
"Cost is a practical concern," the Chancellor notes, "but not the
SECURITY concern the Master Healer raised. The question is about what
happens when biometrics are compromised - and the answer is they cannot
be reissued like a new passphrase."
                    """,
                    3: """
"Remember patterns?" The Master Healer looks confused. "The whole
advantage of biometrics is that guardians need remember nothing - their
identity IS the authentication. The concern is not memorization but
that biometrics are permanent. You cannot change your blood like you
change a passphrase."
                    """
                }
            },
            "corporate": {
                "title": "THE FINGERPRINT ROLLOUT",
                "narrative": """
The facilities team is excited about their new fingerprint scanners for
building access. "No more lost badges! No more shared PINs! Your finger
is always with you!"

But the security assessment has flagged a concern, and you're presenting
to the executive team.

"The fingerprint scanners are great for convenience," you begin. "But
there's a key security concern the team should understand before we
proceed with the rollout."

The CFO looks impatient. "We've already purchased the scanners. What's
the problem?"

You need to explain the unique risk of biometric authentication compared
to passwords or badges.
                """,
                "choices": [
                    {"text": "Fingerprints are too easy to guess"},
                    {"text": "Biometrics cannot be changed if compromised"},
                    {"text": "Fingerprint scanners are too expensive"},
                    {"text": "Fingerprints require users to remember complex patterns"}
                ],
                "success_text": """
"Biometrics cannot be changed if compromised," you explain. "If someone's
password is stolen, we issue them a new password. If their badge is
cloned, we issue a new badge. But if their fingerprint template is
stolen from the database?"

You let that sink in. "We cannot issue them new fingerprints. That
biometric is compromised permanently."

The CISO nods. "Which is why we store fingerprint templates locally on
the scanners, not in a central database that could be breached. And
why fingerprints should be combined with something else - a PIN, a badge
- rather than being the sole authentication factor."

The CFO looks concerned. "So the rollout is still okay?"

"Yes, but with proper protections. Encrypt the templates. Store locally.
Use as one factor of multi-factor authentication. Biometrics are
convenient and hard to share or forget - but we must protect them
accordingly because they can never be replaced."

BIOMETRIC templates require strong protection - they're irreplaceable.
                """,
                "failure_texts": {
                    0: """
The CISO shakes his head. "Fingerprints have billions of possible
patterns - they're not guessable like weak passwords. The concern is
what happens when the fingerprint TEMPLATE is stolen from our systems.
That's fundamentally different from password guessing."
                    """,
                    2: """
"We've already purchased them," the CFO notes. "Cost isn't the concern
here. The security question is: what makes biometrics different from
passwords in terms of compromise recovery? The answer is you can't
issue someone new fingerprints."
                    """,
                    3: """
The CFO looks confused. "Remember patterns? The whole point is that
people don't have to remember anything - their finger is the key.
The concern isn't about memorization but about what happens when
biometric data is compromised. It can't be changed like a password."
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Biometric authentication (fingerprints, face, iris, etc.) has a unique
risk: biometrics cannot be changed if compromised. Unlike passwords
(reissued) or tokens (replaced), biometric data is permanent. If fingerprint
templates are stolen, users cannot get new fingerprints. This makes
protecting biometric databases critical and argues for local storage,
encryption, and using biometrics as one factor of multi-factor authentication.
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Biometric Authentication"
    },

    # Scenario 14: Password Policies
    {
        "id": "d5_quarterly_passphrase_chaos",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE PARCHMENT PROBLEM",
                "narrative": """
The Master of Archives has discovered something troubling during his
rounds. Small parchments hidden under inkwells, tucked into book spines,
slipped beneath desk blotters - each containing the current passphrase
of a scribe or guardian.

"Our policy requires passphrase changes every moon cycle," he explains
to the Council. "We forbid reusing the last five passphrases. We require
eight runes minimum with symbols and numbers. And THIS is the result."

He gestures at a collection of confiscated parchments. "Sun4Moon!"
"Winter25!" "Spring26!" "The same patterns, incrementing. Written down
because no one can remember constantly changing complex passphrases."

The Council looks uncomfortable. "Surely more frequent changes would
improve security?"

The Master of Archives turns to you. "What change would BEST improve
both security and usability?"
                """,
                "choices": [
                    {"text": "Reduce minimum passphrase length to six runes"},
                    {"text": "Require weekly passphrase changes instead of monthly"},
                    {"text": "Require longer passphrases with less frequent changes"},
                    {"text": "Remove all passphrase requirements entirely"}
                ],
                "success_text": """
"Modern wisdom suggests longer passphrases with less frequent changes,"
you advise. "Instead of eight complex runes changed every moon, consider
twenty runes - a phrase! - changed only when compromised."

You explain: "A passphrase like 'TheNorthTowerGuardsTheDawn' is vastly
harder to crack than 'Sun4Moon!' - yet easier to remember. Because it's
memorable, scribes need not write it down. Because it changes rarely,
they don't develop predictable patterns."

The Master of Archives nods slowly. "So 'length over complexity, stability
over rotation'?"

"Exactly. Frequent rotation trains people to use predictable patterns
and write things down - the opposite of our goals. A truly strong
passphrase that lives only in memory is more secure than a weak one
that changes often and lives on parchment under the inkwell."

MODERN PASSWORD GUIDANCE: Longer passphrases, less frequent rotation.
                """,
                "failure_texts": {
                    0: """
The Master of Archives shakes his head. "Shorter passphrases are easier
to crack! Six runes versus eight makes attacks faster, not harder. The
problem is not length - it's the combination of complexity requirements
and frequent rotation that creates unusable policies."
                    """,
                    1: """
"MORE frequent changes?" The Master spreads his hands over the pile of
hidden parchments. "Weekly changes would make this worse! Scribes would
resort to even simpler patterns, even more written records. The problem
is that frequent rotation creates bad habits, not that rotation isn't
frequent enough."
                    """,
                    3: """
"No requirements at all?" The Master looks alarmed. "Then we would have
scribes using 'password' and 'hello' as their passphrases. Some structure
is necessary - the question is what structure promotes GOOD passphrases
without creating impossible burdens."
                    """
                }
            },
            "corporate": {
                "title": "THE STICKY NOTE AUDIT",
                "narrative": """
The annual security walkthrough has produced embarrassing results. The
auditors found sticky notes with passwords under keyboards, in desk
drawers, and taped to monitors throughout the office.

"Your password policy requires eight characters with uppercase, lowercase,
numbers, and symbols," the auditor notes. "Passwords must change every
90 days and cannot repeat the last twelve passwords."

She holds up a photo of a monitor with "Welcome2024!" written on a
sticky note. "The policy creates passwords too complex to remember and
changes too frequent to memorize. So users write them down."

The CISO looks at you. "Modern guidance has changed. What policy would
BEST improve both security and usability?"
                """,
                "choices": [
                    {"text": "Reduce minimum length to six characters"},
                    {"text": "Require monthly password changes instead of quarterly"},
                    {"text": "Require longer passphrases with less frequent changes"},
                    {"text": "Remove all password requirements entirely"}
                ],
                "success_text": """
"NIST 800-63B and modern security guidance recommend longer passphrases
with less frequent changes," you explain. "Instead of complex eight-
character passwords changed quarterly, consider sixteen-plus character
passphrases changed only when there's evidence of compromise."

You continue: "A passphrase like 'MyDogRexLovesToChaseSquirrels!' is
exponentially harder to crack than 'P@ssw0rd!' yet infinitely easier
to remember. No one writes it on a sticky note. And because it doesn't
change every quarter, users don't develop predictable patterns like
adding incrementing numbers."

The CISO nods. "So we get stronger authentication AND better usability?"

"Exactly. Frequent rotation with complexity requirements trains users
to work around the policy. Long, memorable passphrases with rare rotation
trains users to use genuinely strong credentials."

MODERN PASSWORD GUIDANCE favors length and stability over complexity and rotation.
                """,
                "failure_texts": {
                    0: """
The auditor shakes her head. "Shorter passwords are EASIER to crack.
Reducing from eight to six characters dramatically reduces the search
space. The problem isn't length - it's the combination of complexity
and frequent rotation that makes passwords unusable."
                    """,
                    1: """
"More frequent changes?" The auditor gestures at the sticky note photos.
"This IS the result of frequent changes. Users can't remember constantly
changing complex passwords, so they write them down or use predictable
patterns. Monthly changes would make this worse, not better."
                    """,
                    3: """
"No requirements at all?" The CISO frowns. "Then we'd have passwords
like '123456' and 'password.' Some guidance is necessary - the question
is what guidance creates usable security. Long passphrases with rare
rotation is the modern answer."
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Modern password guidance (including NIST 800-63B) recommends longer
passphrases with less frequent changes. Frequent rotation causes users
to choose weak, predictable passwords or write them down. Long passphrases
are more secure and more memorable than short complex passwords. Change
passwords when there's evidence of compromise, not on arbitrary schedules.
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Password Policies"
    },

    # Scenario 15: Directory Services
    {
        "id": "d5_registry_eavesdropping",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE REGISTRY OF SOULS",
                "narrative": """
The Kingdom's Registry of Souls maintains records of all guardians,
scribes, and officials - their identities, their roles, their access
permissions. When a guardian approaches a gate, the gate consults the
Registry to verify their standing.

The Master of Shadows has concerning news. "Our scryers have detected
enemy agents intercepting the messages between gates and the Registry.
The queries travel openly through the aether - who is asking, about
whom, and the Registry's response. This reveals our patrol patterns,
our personnel movements, our organizational structure."

The Keeper of the Registry looks worried. "We cannot stop using the
Registry - the entire kingdom depends on it for access decisions. But
these messages must be protected from eavesdroppers."

What should be implemented?
                """,
                "choices": [
                    {"text": "Disable the Registry entirely"},
                    {"text": "Enable encrypted communication with the Registry"},
                    {"text": "Use a different registry system"},
                    {"text": "Store all identities in plaintext scrolls at each gate"}
                ],
                "success_text": """
"We must enable encrypted communication - think of it as warded
channels - between the gates and the Registry," you explain. "The
queries and responses travel through magical conduits that only the
Registry and authorized gates can read. Eavesdroppers see only
unintelligible patterns."

The Master of Shadows nods. "Like speaking in a language only the
sender and recipient understand?"

"Exactly. In technical terms, this would be LDAPS - LDAP over TLS.
The Registry continues to function exactly as before, but all
communication is encrypted. Enemy agents intercepting the messages
would learn nothing - not who is being queried, not what permissions
they have, not who is making the requests."

The Keeper of the Registry looks relieved. "So we maintain our
Registry system but wrap it in protection?"

"Precisely. Encryption protects the confidentiality of directory
communications without disrupting directory functionality."

LDAPS encrypts directory service communications.
                """,
                "failure_texts": {
                    0: """
The Keeper of the Registry protests. "Disable the Registry? Then how
does any gate know who has access? The entire kingdom's access control
depends on the Registry! We cannot disable it - we must protect its
communications while maintaining its function."
                    """,
                    2: """
The Master of Shadows shakes his head. "A different registry system
would face the same problem if its communications travel openly. The
issue is not the registry itself but the protection of messages TO
and FROM the registry. We need encryption, not replacement."
                    """,
                    3: """
"Plaintext scrolls at each gate?" The Keeper looks horrified. "Then
every gate contains the entire roster of the kingdom's personnel and
permissions - any gate that falls exposes everything! And updates would
require courier travel to every gate. The Registry exists precisely
to avoid this chaos."
                    """
                }
            },
            "corporate": {
                "title": "THE LDAP FINDING",
                "narrative": """
The penetration test report has landed on your desk with a critical
finding highlighted in red.

"Active Directory LDAP queries are transmitted in cleartext," you read.
"A network-positioned attacker can observe authentication attempts,
user lookups, and group membership queries. Sensitive information about
organizational structure, user accounts, and access patterns is exposed."

The IT Director looks at the finding. "Everything uses AD - email,
file shares, applications. We can't just turn it off."

The network engineer offers a suggestion. "We could switch to a
different directory service?"

The CISO shakes her head. "That's a massive undertaking that doesn't
necessarily solve the problem. What's the appropriate fix?"
                """,
                "choices": [
                    {"text": "Disable LDAP and Active Directory"},
                    {"text": "Enable LDAPS (LDAP over TLS/SSL)"},
                    {"text": "Switch to a different directory service"},
                    {"text": "Store all passwords in plaintext to avoid encryption overhead"}
                ],
                "success_text": """
"Enable LDAPS - LDAP over SSL/TLS," you recommend. "This encrypts all
communication between clients and Active Directory. The queries still
work exactly the same way, but network observers see only encrypted
traffic instead of cleartext account information."

The IT Director nods. "So from the application perspective, nothing
changes?"

"Minimal changes. Applications need to use the LDAPS port and trust the
AD certificate. But the fundamental functionality is identical - we're
just wrapping it in transport encryption. The attacker who could
previously see 'User jsmith checking group membership for Domain Admins'
now sees encrypted traffic that reveals nothing."

The CISO looks satisfied. "So we maintain AD functionality while
protecting the wire traffic?"

"Exactly. LDAPS is the standard solution for securing directory
service communications."

LDAPS encrypts LDAP traffic, protecting directory queries from eavesdropping.
                """,
                "failure_texts": {
                    0: """
The IT Director stares. "Disable Active Directory? Every system in the
company authenticates against AD. Email, file shares, applications -
everything. We can't just turn it off. We need to SECURE it, not
eliminate it."
                    """,
                    2: """
The CISO shakes her head. "A different directory service would still
need to encrypt its communications. The problem isn't AD itself - it's
the lack of transport encryption. Switching directories is massive
effort that doesn't inherently solve the cleartext problem."
                    """,
                    3: """
The entire room falls silent. The CISO finally speaks: "Plaintext
passwords would be the worst possible approach. That's the opposite
of security. We need encryption of communications, not abandonment
of credential protection."
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Directory services like Active Directory use LDAP for queries. By default,
LDAP traffic is unencrypted - attackers can observe user lookups, group
memberships, and authentication attempts. LDAPS (LDAP over SSL/TLS) encrypts
this traffic, protecting directory information from network eavesdropping
while maintaining full directory functionality.
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Directory Services"
    },

    # Scenario 16: Attribute-Based Access Control
    {
        "id": "d5_complex_access_rules",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE SCHOLAR'S ACCESS PUZZLE",
                "narrative": """
The Grand Library faces a complex access challenge. Different scholars
need different access based on multiple factors - not just their role.

The Head Librarian presents the problem: "A scholar from the Mages'
Guild, researching classified magical texts, during daylight hours,
from within the Citadel walls - should have access. The same scholar,
at midnight, from outside the Citadel - should NOT have access to those
same texts."

She continues: "A scholar's access depends on their guild affiliation,
the classification of the document, the time of day, and their location.
Role-based access cannot capture this complexity - a 'Scholar' role is
too broad."

The Royal Architect asks: "What access control model allows decisions
based on multiple attributes - subject attributes, resource attributes,
environmental conditions - evaluated together?"
                """,
                "choices": [
                    {"text": "Role-Based Access Control - assign permissions to roles"},
                    {"text": "Discretionary Access Control - owners grant access"},
                    {"text": "Attribute-Based Access Control - evaluate multiple attributes for decisions"},
                    {"text": "Mandatory Access Control - labels and clearances"}
                ],
                "success_text": """
"This requires Attribute-Based Access Control - ABAC," you explain.
"ABAC evaluates multiple attributes to make access decisions: subject
attributes (guild affiliation, clearance level), resource attributes
(document classification, sensitivity), and environmental attributes
(time, location)."

You outline a policy: "A Mages' Guild scholar, clearance level Secret,
may access classified magical texts, during business hours, from within
the Citadel. Each element is an attribute; together they form the
access decision."

The Head Librarian nods. "So we can express complex policies that
traditional role-based access cannot capture?"

"Exactly. RBAC says 'Scholars can access the library.' ABAC says
'Mages' Guild scholars with Secret clearance can access classified
magical texts during daylight from trusted locations.' The granularity
is in the attributes, not the role."

ABAC provides fine-grained access control through attribute evaluation.
                """,
                "failure_texts": {
                    0: """
The Head Librarian shakes her head. "Role-based access assigns
permissions to roles like 'Scholar.' But a Scholar from the Mages'
Guild needs different access than a Scholar from the Healers' Guild,
and both depend on time and location. RBAC doesn't easily capture
all these conditions."
                    """,
                    1: """
"Discretionary access relies on resource owners granting permissions,"
the Royal Architect notes. "But our requirement is for POLICY-based
access decisions involving multiple factors. We need rules that consider
guild, classification, time, and location together - not owner discretion."
                    """,
                    3: """
"Mandatory Access Control uses fixed security labels - Secret, Top
Secret - compared to user clearance," the Architect explains. "It's
powerful but rigid. We need flexibility to incorporate time, location,
and multiple classifications, not just a label hierarchy."
                    """
                }
            },
            "corporate": {
                "title": "THE DYNAMIC ACCESS REQUIREMENT",
                "narrative": """
The new compliance mandate has created an access control nightmare.
The compliance officer explains the requirements.

"Access to financial data must consider: the user's department, the
data's classification level, the time of access, and the user's
location. An Accounting employee accessing Confidential-Finance data
during business hours from the office network is fine. The same access
at 2 AM from a coffee shop should be blocked."

She continues: "Same data, same user, different context, different
decision. Our current role-based system can't handle this. A 'Finance'
role is too blunt."

The IT architect scratches his head. "We need an access model that
evaluates multiple conditions together - user attributes, data
attributes, environmental factors. What model supports that?"
                """,
                "choices": [
                    {"text": "Role-Based Access Control - just add more roles"},
                    {"text": "Discretionary Access Control - let data owners decide"},
                    {"text": "Attribute-Based Access Control - evaluate multiple attributes dynamically"},
                    {"text": "Mandatory Access Control - clearance levels only"}
                ],
                "success_text": """
"Attribute-Based Access Control - ABAC," you recommend. "ABAC policies
evaluate attributes from multiple sources: subject attributes (department,
job level, training completed), resource attributes (data classification,
sensitivity, owner department), and environmental attributes (time, day,
network location, device type)."

You draft a sample policy: "IF user.department = 'Accounting' AND
resource.classification = 'Confidential-Finance' AND environment.time
BETWEEN 0800 AND 1800 AND environment.network = 'Corporate' THEN
PERMIT."

The compliance officer nods. "So we can express complex, context-aware
policies?"

"Exactly. ABAC provides the granularity you need. Role-based says 'who
can access what.' Attribute-based says 'who can access what, under what
conditions.' That context-awareness is what compliance requires."

ABAC enables fine-grained, context-aware access control.
                """,
                "failure_texts": {
                    0: """
The IT architect shakes his head. "More roles? We already have role
explosion. And roles don't capture time or location. We'd need roles
like 'Finance-Daytime-Office' and 'Finance-Daytime-Remote' - that's
not scalable. We need attribute evaluation, not more roles."
                    """,
                    1: """
"Data owner discretion doesn't help with time-based or location-based
decisions," the compliance officer notes. "We need automated policy
enforcement based on multiple factors, not case-by-case owner decisions.
DAC doesn't provide the dynamic context-aware controls we need."
                    """,
                    3: """
"Clearance levels alone aren't enough," the architect explains. "MAC
compares user clearance to data classification. But we also need to
consider time, location, and department affiliation. MAC's label
comparison is too narrow for these multi-factor requirements."
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Attribute-Based Access Control (ABAC) evaluates multiple attributes to make
access decisions: subject attributes (department, role, clearance), resource
attributes (classification, type, owner), and environmental attributes (time,
location, device). This enables fine-grained, context-aware policies like
"Finance users can access Confidential-Finance data during business hours
from corporate networks."
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Attribute-Based Access Control"
    },

    # Scenario 17: Identity Governance
    {
        "id": "d5_governance_chaos",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE LEDGER OF FORGOTTEN KEYS",
                "narrative": """
The Royal Auditors have completed their review, and their findings are
dire. The Grand Chamberlain reads the summary with growing dismay.

"Orphaned access: 247 guardians who left service still have active
access runes. Excessive permissions: Scribes with access to the Treasury,
Cooks with access to the Armory - permissions that make no sense. And
NO comprehensive view of who has access to what across all domains."

He slams the parchment down. "We do not know who has access. We cannot
review whether access is appropriate. We discover problems only when
something goes wrong. This is governance chaos."

The Master of Keys looks defensive. "Each domain manages its own access.
The Treasury manages Treasury access. The Armory manages Armory access.
There is no unified view."

What solution addresses these governance challenges?
                """,
                "choices": [
                    {"text": "Implement stronger passphrase policies"},
                    {"text": "Deploy an Identity Governance solution for unified visibility and lifecycle management"},
                    {"text": "Add more guard towers"},
                    {"text": "Require multi-factor authentication everywhere"}
                ],
                "success_text": """
"You need an Identity Governance solution," you explain. "Think of it
as a master ledger that aggregates access information from all domains,
provides unified visibility, automates access reviews, and manages the
identity lifecycle from appointment to departure."

You outline the capabilities: "Orphaned accounts? The governance system
tracks when guardians leave service and ensures access is revoked.
Excessive permissions? Automated reviews flag access that doesn't match
role expectations. No unified view? The system aggregates access from
Treasury, Armory, Archives - everywhere - into a single pane."

The Grand Chamberlain leans forward. "And policy violations are detected
automatically rather than discovered during audits?"

"Exactly. Continuous monitoring, automated access reviews, segregation
of duties enforcement, comprehensive audit trails. Governance addresses
the systemic issues, not just individual symptoms."

IDENTITY GOVERNANCE provides visibility, control, and lifecycle management.
                """,
                "failure_texts": {
                    0: """
The Grand Chamberlain sighs. "Stronger passphrases? That does not
address orphaned accounts or excessive permissions. People who have
left still have access - stronger passphrases just make their old
access harder to abuse, not impossible. We need governance, not
password policy."
                    """,
                    2: """
"More guard towers?" The Auditor looks bemused. "We are discussing
access governance, not physical security. Orphaned accounts, excessive
permissions, lack of visibility - these are identity management problems,
not problems solved by additional fortifications."
                    """,
                    3: """
"Multi-factor authentication strengthens login," the Auditor notes.
"But it doesn't address who SHOULD have access. Orphaned accounts with
MFA are still orphaned accounts. Excessive permissions with MFA are
still excessive permissions. We need governance over access rights, not
just stronger authentication."
                    """
                }
            },
            "corporate": {
                "title": "THE ACCESS CHAOS REPORT",
                "narrative": """
The external audit has produced findings that have the executive team
in crisis mode. The CISO reads the highlights.

"Orphaned accounts: 312 former employees still have active access.
Excessive permissions: Users with access to systems their roles don't
require. Segregation of duties violations: Users with conflicting
permissions. And no comprehensive view of who has access to what across
all systems."

She looks around the room. "Each system manages its own access. AD, AWS,
Salesforce, the ERP - no unified visibility, no coordinated lifecycle
management, no automated reviews."

The CEO taps the table. "What do we need to fix this? And don't tell
me 'more manual reviews' - we've tried that."

What solution addresses these governance challenges?
                """,
                "choices": [
                    {"text": "Implement stronger password policies"},
                    {"text": "Deploy an Identity Governance and Administration (IGA) solution"},
                    {"text": "Add more firewalls"},
                    {"text": "Require MFA for all applications"}
                ],
                "success_text": """
"You need an Identity Governance and Administration - IGA - solution,"
you recommend. "IGA provides unified visibility across all systems,
automated access reviews, policy enforcement, and identity lifecycle
management."

You outline the value: "Orphaned accounts? IGA integrates with HR to
automatically deprovision when employees leave. Excessive permissions?
Automated certification campaigns flag anomalies for manager review.
Segregation of duties? IGA enforces policies preventing conflicting
access. No visibility? Single dashboard showing who has access to what
across AD, AWS, Salesforce, and every connected system."

The CEO nods. "So instead of hoping each system owner manages their own
access correctly..."

"You have centralized governance with automated enforcement. IGA doesn't
replace system-level controls, but it provides the oversight layer that
catches what falls through the cracks."

IGA addresses identity governance holistically.
                """,
                "failure_texts": {
                    0: """
The CISO shakes her head. "Password policies don't address orphaned
accounts or excessive permissions. Former employees with strong passwords
still shouldn't have access. The problem is WHAT access people have,
not HOW they authenticate."
                    """,
                    2: """
"Firewalls?" The CEO looks confused. "We're talking about identity
governance, not network security. Firewalls don't prevent orphaned
accounts or excessive application permissions. Different problem
domain entirely."
                    """,
                    3: """
"MFA strengthens authentication," the CISO agrees. "But orphaned
accounts with MFA are still orphaned. Excessive permissions with MFA
are still excessive. We need governance over WHO should have access
to WHAT, not just stronger proof of identity at login."
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Identity Governance and Administration (IGA) solutions provide holistic
identity management: unified visibility across systems, automated access
reviews/certification, policy enforcement (SoD, least privilege), identity
lifecycle automation, and comprehensive audit trails. IGA addresses systemic
governance issues like orphaned accounts, privilege accumulation, and lack
of visibility.
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Identity Governance"
    },

    # Scenario 18: Credential Stuffing Defense
    {
        "id": "d5_stolen_keys_attack",
        "domain": 5,
        "themes": {
            "fantasy": {
                "title": "THE STOLEN KEYS FROM DISTANT LANDS",
                "narrative": """
The Master of Shadows brings alarming intelligence. "Enemy agents have
obtained a ledger of passphrases stolen from the Western Kingdoms. They
are trying these passphrases against our gates, hoping that some of our
guardians use the same phrases they used in the West."

The Gate Captain confirms the problem. "We have seen hundreds of attempts
today - passphrases that are valid elsewhere being tried here. Some
guardians DO use the same passphrase everywhere. When the attempt matches,
the attacker enters as that guardian."

The Lord Chamberlain looks grave. "Requiring longer passphrases will not
help if the exact passphrase was stolen from the Western Kingdoms. What
is our MOST effective defense?"
                """,
                "choices": [
                    {"text": "Require longer passphrases"},
                    {"text": "Implement multiple factors and detect repeated attempts from the same source"},
                    {"text": "Change the location of our gates"},
                    {"text": "Disable the ability to recover forgotten passphrases"}
                ],
                "success_text": """
"Our most effective defense combines multiple factors with detection,"
you explain. "If we require not just a passphrase but also a sigil
that each guardian carries - multi-factor authentication - then stolen
passphrases alone are insufficient. The enemy has the passphrase but
not the sigil."

You continue: "Additionally, we must detect and block these attacks.
If hundreds of attempts come from the same source, if attempts use
known-stolen passphrases, if the pattern of attempts suggests automated
attack - we block and alert. Rate limiting, known-breach checking,
behavioral detection."

The Master of Shadows nods. "So even if a guardian foolishly uses the
same passphrase everywhere, the attacker is stopped by the second factor
or detected by the patterns?"

"Exactly. Multi-factor defeats credential stuffing because stolen
credentials alone aren't enough. Detection and blocking adds defense
in depth."

MFA + DETECTION defeats credential stuffing attacks.
                """,
                "failure_texts": {
                    0: """
The Lord Chamberlain shakes his head. "Longer passphrases don't help
when the EXACT passphrase was stolen from elsewhere. If a guardian
uses 'TheDragonFliesSouth' in both kingdoms, and that exact passphrase
was stolen from the West, length provides no protection. The attack
uses the real stolen credential."
                    """,
                    2: """
The Gate Captain snorts. "Security through obscurity? The enemy will
find our gates eventually - they found them today. Moving gates doesn't
address the fundamental vulnerability that stolen credentials from
elsewhere can be tried here."
                    """,
                    3: """
The Master of Shadows looks confused. "Disabling passphrase recovery?
That affects guardians who forget their own passphrases, not attackers
using stolen passphrases. The recovery process is not the attack vector
here - the attack uses credentials stolen from other realms."
                    """
                }
            },
            "corporate": {
                "title": "THE CREDENTIAL STUFFING CAMPAIGN",
                "narrative": """
The SOC alert is blinking red. "We're seeing thousands of login attempts
from rotating IP addresses," the analyst reports. "The attempts are
using username/password combinations - real ones, stolen from breaches
at other companies. They're trying to see if our users reused passwords."

She pulls up the patterns. "When a combo works - because the user DID
reuse their password - the attacker is in. Full account access. We've
already had three confirmed compromises this morning."

The CISO arrives at the SOC. "Credential stuffing attack. What's our
most effective defense? These aren't weak passwords being guessed -
these are real passwords the users chose, stolen from elsewhere."
                """,
                "choices": [
                    {"text": "Require longer passwords"},
                    {"text": "Implement MFA and detect/block credential stuffing attempts"},
                    {"text": "Change the login page URL"},
                    {"text": "Disable the password recovery feature"}
                ],
                "success_text": """
"MFA combined with detection and blocking," you recommend immediately.
"First, multi-factor authentication means stolen passwords aren't enough.
The attacker has the password but not the authenticator app or hardware
token. They can't complete the login."

You continue outlining defenses: "Second, detection and blocking. Rate
limiting for login attempts. CAPTCHA after suspicious patterns. Checking
attempted passwords against known-breached credential databases. Blocking
IPs exhibiting stuffing patterns. These attackers are trying thousands
of credentials - they'll trigger detection."

The CISO nods. "So even if our users made the mistake of reusing
passwords, the additional factor and our detection capabilities protect
them?"

"Exactly. MFA defeats the attack because passwords alone aren't enough.
Detection catches and blocks the attack patterns. Defense in depth."

MFA + DETECTION is the solution for credential stuffing.
                """,
                "failure_texts": {
                    0: """
The analyst shakes her head. "Longer passwords don't help when the
EXACT password was stolen from a breach. If our user's password at
LinkedIn was 'MyD0gRex2024!' and they used it here too, length is
irrelevant - the attacker has the real credential."
                    """,
                    2: """
The CISO stares. "Change the login URL? That's security through
obscurity. The attackers will find it - they already found it today.
We need real defenses that work even when the attacker knows where
to attack."
                    """,
                    3: """
"Password recovery isn't the attack vector," the analyst notes. "These
attackers have stolen credentials from other breaches. They're not
trying to recover passwords - they're trying passwords they already
have. Disabling recovery would hurt our users, not the attackers."
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Credential stuffing attacks use passwords stolen from other breaches to
attempt login at your organization. Longer passwords don't help when the
EXACT password was stolen. Effective defense requires: 1) MFA - so stolen
passwords alone aren't enough, and 2) Detection/blocking - rate limiting,
CAPTCHA, known-breach credential checking, and blocking suspicious patterns.
Multi-factor authentication defeats credential stuffing by requiring
something beyond the stolen password.
        """,
        "domain_reference": "Domain 5: Identity and Access Management - Credential Stuffing Defense"
    },
]
