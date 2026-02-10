"""
Domain educational introductions for The Citadel of the Eight Domains.

Each domain introduction provides theme-specific content:
- Fantasy theme: Medieval/magical narrative style
- Corporate theme: Modern office satire style

Both themes teach the same CISSP concepts with different narrative framing.
"""

DOMAIN_INTRODUCTIONS = {
    1: {
        # Fantasy theme (default)
        "title": "DOMAIN I: SECURITY AND RISK MANAGEMENT",
        "narrator": "THE KEEPER OF GOVERNANCE",
        "introduction": """
The Hall of Security and Risk Management is the foundation upon which all
other domains rest. Here, the ancient principles of governance, risk, and
compliance converge. You will learn to see security not as a technical
puzzle alone, but as a balance between protecting assets and enabling the
realm to function.

This domain teaches you to think like a leader: How do we decide what to
protect? How much risk is acceptable? What policies guide our guardians?
You will encounter questions of ethics, business continuity, and the laws
that bind us all. Master these principles, and you will have the foundation
to understand every domain that follows.

Above all else, remember the cardinal rule that governs every decision in
this Citadel: LIFE SAFETY IS ALWAYS THE HIGHEST PRIORITY. No asset, no data,
no secret is worth more than a human life. This principle will guide you
through every trial ahead, and it is the first lesson every guardian must
learn.
        """,
        # Corporate theme
        "corporate": {
            "narrator": "THE CISO (via all-hands meeting)",
            "introduction": """
Welcome to Level 1: Security Governance and Risk Management. This is where
we figure out what we're protecting, why we're protecting it, and how much
money we can convince the CFO to spend on it.

Think of this as the "business side" of security. You'll learn about risk
assessments (how bad could this really get?), business continuity (what
happens when the data center floods?), and compliance (keeping auditors
happy so they'll leave us alone).

Here's the one rule that overrides everything else: LIFE SAFETY FIRST.
If the server room is on fire and someone's trapped inside, you save the
person, not the backup tapes. No data is worth a human life. Ever. This
isn't just ethics - it's literally the first thing they'll ask about on
the CISSP exam. And in real life, it's the difference between being a
security professional and being a monster.

Now, let's talk about managing risk without losing our minds...
            """
        }
    },
    2: {
        # Fantasy theme (default)
        "title": "DOMAIN II: ASSET SECURITY",
        "narrator": "THE GUARDIAN OF TREASURES",
        "introduction": """
The Vault of Asset Security holds the second great truth of our profession:
you cannot protect what you do not know. Before any defense can be mounted,
we must first understand what we guard - its value, its nature, and who
bears responsibility for its safety.

In this domain, you will learn the arts of classification and ownership.
Not all treasures are equal; some require iron vaults while others need
only wooden chests. You must distinguish between the DATA OWNER - who
determines how information should be protected - and the DATA CUSTODIAN -
who maintains it day-to-day. These roles are distinct and essential.

You will discover how assets flow through their lifecycle: from creation
through storage, use, and sharing, to eventual archival or destruction.
Pay special attention to the concept of DATA REMANENCE - the ghost of
information that lingers even after we believe it destroyed. Many a secret
has been betrayed by careless disposal. The wise guardian ensures that
when data must die, it dies completely, leaving no trace for enemies to
recover.
        """,
        # Corporate theme
        "corporate": {
            "narrator": "THE DATA GOVERNANCE TEAM LEAD",
            "introduction": """
Welcome to Level 2: Asset Security. Or as I like to call it, "Where is all
our stuff, and who's supposed to be watching it?"

Here's the uncomfortable truth: most organizations have no idea what data
they actually have, where it lives, or who's responsible for it. Sound
familiar? Yeah, that's why we have this department.

You'll learn about classification (is this 'Confidential' or just 'Internal
Use Only'?), data ownership (hint: the person who created it isn't always
the owner), and the data lifecycle (from creation to that beautiful moment
when you finally get to delete it legally).

Pay attention to DATA REMANENCE - that's the fun phenomenon where deleted
data isn't really deleted. That hard drive you threw in the dumpster?
Someone's probably reading it right now. Sleep well tonight!

Let's learn how to actually secure the things that matter...
            """
        }
    },
    3: {
        # Fantasy theme (default)
        "title": "DOMAIN III: SECURITY ARCHITECTURE AND ENGINEERING",
        "narrator": "THE MASTER ARCHITECT",
        "introduction": """
Welcome to the Engineering Halls, where the very foundations of our defenses
are designed and built. Here you will learn that security is not merely
bolted on after construction - it must be woven into the fabric of every
wall, every ward, every magical circuit from the very beginning.

The great architects of old understood DEFENSE IN DEPTH - that no single
barrier, however mighty, should be trusted alone. Layer upon layer of
protection, each independent, each capable of standing when others fall.
Study the security models that govern our realm: Bell-LaPadula guards our
secrets from prying eyes, while Biba ensures the integrity of our records.

You will master the arcane arts of cryptography - the ancient mathematics
that transforms readable text into indecipherable ciphers. Learn the
difference between symmetric keys (shared secrets) and asymmetric pairs
(public and private). Understand that even the strongest encryption fails
if its keys are poorly managed.

Above all, remember: a castle built on sand will crumble, no matter how
thick its walls. Security must be architected into the foundation.
        """,
        "corporate": {
            "narrator": "THE ENTERPRISE ARCHITECT",
            "introduction": """
Welcome to Level 3: Security Architecture and Engineering. This is where
we actually BUILD the security controls everyone else just talks about.

Ever wonder why that "quick fix" from five years ago is now a critical
vulnerability? Because someone skipped the architecture review. Security
needs to be designed in from the start, not duct-taped on during the
penetration test.

You'll learn about DEFENSE IN DEPTH (because your firewall WILL fail
someday), security models (Bell-LaPadula for confidentiality, Biba for
integrity - yes, there will be a test), and cryptography (the thing
everyone uses but nobody understands).

Key lesson: symmetric encryption uses one key, asymmetric uses two. If
you remember nothing else, remember that. Also remember that the guy who
says "we'll add security later" is the reason we have incident response
teams.

Let's learn how to build things that don't fall apart at the first sign
of an attacker...
            """
        }
    },
    4: {
        # Fantasy theme (default)
        "title": "DOMAIN IV: COMMUNICATION AND NETWORK SECURITY",
        "narrator": "THE WARDEN OF PATHWAYS",
        "introduction": """
The realm is connected by countless magical pathways - ley lines that carry
messages, enchanted courier routes, and mystical portals that span vast
distances. This domain teaches you to secure these vital connections, for
an enemy who controls the pathways controls the flow of all information.

You will study the great OSI model - seven layers of communication, each
with its own vulnerabilities and protections. From the physical crystals
that carry our signals to the application spells that interpret them, every
layer must be guarded.

Learn the art of network segmentation - dividing your realm into protected
zones so that a breach in one area cannot spread to others. Master the
deployment of firewalls, those magical barriers that examine every message
and block the suspicious. Understand VPNs - encrypted tunnels through
hostile territory that protect travelers from eavesdroppers.

Be ever vigilant against the dark arts: man-in-the-middle attacks where
enemies insert themselves into conversations, denial-of-service floods
that overwhelm our defenses, and the countless ways attackers exploit
poorly secured connections. The network is the battlefield.
        """,
        "corporate": {
            "narrator": "THE NETWORK SECURITY MANAGER",
            "introduction": """
Welcome to Level 4: Communication and Network Security. This is where we
learn why "just plug it into the network" is a phrase that makes security
people twitch.

Remember the OSI model from your networking class? Good, because you'll
need it. Seven layers, each one a new opportunity for someone to break
something. From physical cables to application protocols, every layer has
its own special flavor of vulnerability.

You'll learn about VLANs (keeping departments from accidentally seeing
each other's traffic), firewalls (the first line of defense that everyone
thinks is the ONLY line of defense), and VPNs (so road warriors can work
from coffee shops without exposing everything).

The fun stuff is the attacks: man-in-the-middle (reading your traffic),
DDoS (drowning you in garbage packets), and DNS poisoning (redirecting
users to evil sites). These aren't theoretical - they happen every day.

Let's learn how to keep the network from becoming your biggest liability...
            """
        }
    },
    5: {
        # Fantasy theme (default)
        "title": "DOMAIN V: IDENTITY AND ACCESS MANAGEMENT",
        "narrator": "THE GATEKEEPER",
        "introduction": """
Who goes there? This ancient challenge echoes through the Citadel's gates,
for the art of Identity and Access Management is the art of knowing who
seeks entry and what they should be permitted to do once inside.

You will master the three pillars of authentication: something you KNOW
(a password or secret phrase), something you HAVE (a token or enchanted
amulet), and something you ARE (the unique patterns of your very essence).
Wise defenders combine these factors, for a single pillar may be knocked
down, but three standing together rarely fall.

Learn the principle of LEAST PRIVILEGE - that every soul should receive
only the access necessary for their duties, no more. A scribe needs access
to the library, not the treasury. A guard needs the armory, not the royal
chambers. Excessive privilege is excessive risk.

Study the lifecycle of identity: from the moment a new apprentice is
granted their first access, through their career of changing roles and
responsibilities, to the critical moment when they depart and all access
must be revoked. Many a castle has fallen to a "departed" member whose
keys were never collected.
        """,
        "corporate": {
            "narrator": "THE IAM TEAM LEAD",
            "introduction": """
Welcome to Level 5: Identity and Access Management. Or as I call it,
"Who are you, and why do you think you can access that?"

This is the domain where we answer three eternal questions: Authentication
(are you who you claim to be?), Authorization (are you allowed to do what
you're trying to do?), and Accounting (what did you actually do?). The
holy trinity of IAM.

You'll learn about MFA (because passwords alone are basically useless),
SSO (one login to rule them all), and the ever-popular access reviews
(quarterly reminders that Bob from accounting still has admin rights
three years after he transferred to marketing).

Key concept: LEAST PRIVILEGE. Everyone gets the minimum access needed to
do their job. That intern doesn't need domain admin. Neither does the CEO,
honestly. The more access you have, the more damage you can accidentally
cause.

And remember: the most dangerous time for access is when someone leaves.
If you don't revoke access immediately, congratulations, you've created
an insider threat. Let's learn how to not do that...
            """
        }
    },
    6: {
        # Fantasy theme (default)
        "title": "DOMAIN VI: SECURITY ASSESSMENT AND TESTING",
        "narrator": "THE GRAND INQUISITOR",
        "introduction": """
Trust, but verify. This ancient wisdom guides the Sixth Domain, where we
learn the arts of testing our own defenses before our enemies do. For
what good are walls never inspected? What use are wards never tested?

You will learn the difference between vulnerability assessments - the
careful cataloging of potential weaknesses - and penetration testing -
the simulated attacks that prove whether those weaknesses can truly be
exploited. Both have their place; neither is sufficient alone.

Study the three approaches to testing: black box (knowing nothing, as an
outside attacker would), white box (knowing everything, as an insider
might), and gray box (the realistic middle ground). Each reveals different
truths about your defenses.

Master the art of the security audit - the formal examination of controls
and compliance. Learn to read logs and analyze patterns, for the history
of what has happened reveals what might happen again. And practice the
tabletop exercise - the gathering of minds to walk through crisis scenarios
before they become reality.

The kingdom that tests itself finds its weaknesses. The kingdom that does
not... has its weaknesses found for it.
        """,
        "corporate": {
            "narrator": "THE SECURITY TESTING MANAGER",
            "introduction": """
Welcome to Level 6: Security Assessment and Testing. This is where we
find out how bad things really are, before the bad guys do.

There's a crucial difference between a vulnerability assessment (here's
a list of things that MIGHT be exploitable) and a penetration test (here's
proof that we just exploited them). One gives you a to-do list. The other
gives you a heart attack and a to-do list.

You'll learn about black-box testing (attacker knows nothing), white-box
testing (tester knows everything), and gray-box (realistic middle ground).
You'll also learn why the auditors want all those logs, and what happens
when you don't have them (spoiler: you fail the audit).

Key tools: vulnerability scanners (automated weakness detection), SAST
and DAST (finding bugs in code before and after deployment), and the
humble log review (where we discover that the breach actually happened
three months ago).

Remember: if you don't test your security, someone else will. And they
won't send you a nice report afterward. Let's learn how to find problems
before they find us...
            """
        }
    },
    7: {
        # Fantasy theme (default)
        "title": "DOMAIN VII: SECURITY OPERATIONS",
        "narrator": "THE COMMANDER OF THE WATCH",
        "introduction": """
The walls are built. The guards are trained. The wards are set. But security
is not a destination - it is an endless journey. Welcome to Security
Operations, where the daily work of protection never ceases.

You will learn the sacred art of incident response - what to do when the
unthinkable happens. Preparation, identification, containment, eradication,
recovery, and lessons learned. Every incident follows this path; every
defender must know it by heart.

Master the handling of evidence, for in the aftermath of an attack, the
truth lives in the artifacts left behind. Chain of custody must be
preserved, or justice cannot be served. Learn forensic techniques that
reveal what happened, when, and by whom.

Study the watchtowers of our profession: SIEM systems that gather and
correlate signals from every corner of the realm, threat intelligence
that warns of coming storms, and the continuous monitoring that never
sleeps. Patch management, change control, configuration management - the
unglamorous work that prevents most incidents before they begin.

In Security Operations, vigilance is life. Complacency is death.
        """,
        "corporate": {
            "narrator": "THE SOC MANAGER",
            "introduction": """
Welcome to Level 7: Security Operations. This is where the rubber meets
the road, where theory becomes "it's 3 AM and something is very wrong."

The SOC (Security Operations Center) never sleeps. Neither will you, if
you work here long enough. You'll learn about SIEM platforms (drowning
in logs so you don't have to), incident response (what to do when things
go sideways), and threat intelligence (knowing what the bad guys are up
to before they get here).

The incident response lifecycle is your new bible: Preparation, Detection,
Containment, Eradication, Recovery, Lessons Learned. Memorize it. Live it.
You'll walk through it at 2 AM more often than you'd like.

Key skills: Evidence handling (don't contaminate the crime scene), patch
management (update before you're exploited), and change management (so
the new "improvement" doesn't break everything). Also, documentation -
because "we fixed it but don't remember how" is not a valid incident report.

Remember: the SIEM alert at 3 AM is always real. Until it isn't. But treat
every one like it is, because the one you ignore will be the actual breach.
Let's learn how to survive the operational trenches...
            """
        }
    },
    8: {
        # Fantasy theme (default)
        "title": "DOMAIN VIII: SOFTWARE DEVELOPMENT SECURITY",
        "narrator": "THE MASTER ARTIFICER",
        "introduction": """
Every magical artifact begins as raw potential. In the hands of a careless
artificer, that potential becomes a cursed object that betrays its user.
In the hands of a master, it becomes a trustworthy tool. Welcome to Software
Development Security, where we learn to create without creating vulnerabilities.

You will learn that security must be woven into the development lifecycle
from the very first incantation. Requirements, design, implementation,
testing, deployment - at every stage, security must be present. The
grimoire written without security in mind becomes a gateway for attackers.

Study the common vulnerabilities that plague magical constructs: buffer
overflows that allow possession, injection attacks that turn the artifact
against its user, cross-site scripting that spreads corruption. Learn the
OWASP Top Ten - the most common mistakes artificers make - and how to
prevent each one.

Master the arts of code review and security testing. Learn to use automated
tools that scan for weakness, but never trust them completely - the human
eye catches what machines miss. Understand secure deployment, so that even
a well-crafted artifact is not undone by careless installation.

In this domain, we create. And with creation comes responsibility.
        """,
        "corporate": {
            "narrator": "THE APPSEC LEAD",
            "introduction": """
Welcome to Level 8: Software Development Security. This is where we try
to convince developers that security is their problem too. (It's going
about as well as you'd expect.)

Here's the hard truth: most vulnerabilities are born in development, not
discovered by attackers. That SQL injection? A developer didn't validate
input. That XSS? A developer didn't encode output. That hardcoded password?
I don't even want to talk about it.

You'll learn about the SDLC (Security Development Lifecycle - yes, we
added "Security" to the acronym, no, it didn't magically fix everything).
The goal is to bake security into every phase: requirements, design, coding,
testing, and deployment. "We'll add security later" is how breaches happen.

Key topics: OWASP Top Ten (the greatest hits of web vulnerabilities),
secure coding practices (input validation, output encoding, the basics
everyone skips), and code review (where we find out what the automated
tools missed).

Oh, and DevSecOps. It's like DevOps, but with security people awkwardly
inserted into the pipeline. It works better than you'd think, once
everyone stops being territorial.

Let's learn how to build software that doesn't immediately get popped...
            """
        }
    }
}
