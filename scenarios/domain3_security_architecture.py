"""
Domain 3: Security Architecture and Engineering scenarios.

Key CISSP concepts tested:
- Defense in Depth
- Security Models (Bell-LaPadula, Biba)
- Cryptography fundamentals
- PKI and Certificate Management
- Physical and Environmental Controls
- Cloud and Virtualization Security
- Zero Trust Architecture

Each scenario supports dual themes:
- Fantasy: Medieval/magical Citadel setting
- Corporate: Modern office satire (Office Space style)
"""

DOMAIN_3_SCENARIOS = [
    # Scenario 1: Defense in Depth
    {
        "id": "d3_single_wall",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE SINGLE WALL FALLACY",
                "narrative": """
The Kingdom of Valorheim boasts the mightiest wall ever constructed - forty feet
of enchanted stone, warded by seven archmages, and defended by the finest archers
in the realm. The King has poured the entire defense budget into this singular
barrier. No army has ever breached it.

A traveling war wizard visits your court and shakes his head grimly. "Your Majesty,
I have seen walls greater than this fall. What lies beyond the wall, should an
enemy pass it?"

The King gestures proudly. "Nothing can pass the wall! That is the point!"

The wizard turns to you, the newly appointed Security Advisor. "Tell your King
why this concerns me so."

What do you advise?
                """,
                "choices": [
                    {"text": "The wall vendor might abandon the enchantments - we need backup suppliers"},
                    {"text": "A single point of failure can be bypassed, leaving no additional protection behind it"},
                    {"text": "We should build three more identical walls behind this one"},
                    {"text": "Ancient regulations require exactly three defensive layers"}
                ],
                "success_text": """
The King's brow furrows as you explain. "Your Majesty, last winter the Obsidian
Horde bypassed the walls of Ironkeep entirely - they tunneled beneath. What defenses
existed inside? None. The city fell in a single night."

The wizard nods approvingly. "Your advisor speaks wisdom. Defense in depth means
MULTIPLE, DIFFERENT layers. The wall stops armies. But what stops the assassin who
scales it? The saboteur who tunnels? The traitor who opens the gate?"

You continue: "We need inner checkpoints, palace guards, trapped corridors, and
vault protections. Each layer should be DIFFERENT - diverse controls that address
different threats."

The King strokes his beard. "So my wall is not worthless?"

"It is your first layer, Majesty. But it should not be your only one."

You have demonstrated understanding of DEFENSE IN DEPTH.
                """,
                "failure_texts": {
                    0: """
While vendor stability matters for long-term maintenance, this misses the core
security principle. The issue isn't WHO maintains the wall - it's that the wall
is the ONLY defense. Defense in depth isn't about backup vendors; it's about
multiple, diverse security layers that protect even when one layer fails.
                    """,
                    2: """
Simply adding more of the same control doesn't provide true defense in depth.
Three more walls still all fail to the same threats: tunneling, flying, treachery.
Defense in depth requires DIVERSE, COMPLEMENTARY controls - walls, guards, traps,
vaults - each addressing different attack vectors and providing protection when
others fail.
                    """,
                    3: """
No ancient law mandates a specific number of defensive layers. Defense in depth
is a security principle, not a compliance checkbox. The goal is multiple,
complementary controls that provide continued protection when one fails - not
hitting an arbitrary number to satisfy auditors.
                    """
                }
            },
            "corporate": {
                "title": "THE FIREWALL FANTASY",
                "narrative": """
The IT Director beams with pride during the security review. "We've invested $2
million in the most advanced next-generation firewall on the market. AI-powered
threat detection, deep packet inspection, sandboxing - the works. Our perimeter
is IMPENETRABLE."

You notice something concerning: the network diagram shows the firewall as the
ONLY security control between the internet and the production databases.

A consultant from the audit firm leans over and whispers, "Ask about what happens
when - not if - something gets past their firewall."

The IT Director catches your expression. "Is there a problem? This firewall has
a 99.9% detection rate!"

What do you recommend?

                """,
                "choices": [
                    {"text": "The firewall vendor might go out of business - we need vendor diversity"},
                    {"text": "Single points of failure can be bypassed, leaving no additional protection"},
                    {"text": "We should buy three more identical firewalls in sequence"},
                    {"text": "Compliance requires exactly three security layers"}
                ],
                "success_text": """
You pull up the network diagram. "That 99.9% detection rate sounds impressive.
But with 10,000 attempts per day, that's 10 threats getting through. Every. Single.
Day. What's waiting on the other side?"

The IT Director blinks. "The... the production servers."

"Exactly. Defense in depth means layers. The firewall is your perimeter. But we
also need network segmentation, host-based firewalls, endpoint detection,
application-level controls, and database activity monitoring. DIFFERENT types
of controls at DIFFERENT layers."

The consultant nods. "The firewall stops 99.9% at the edge. The network segments
stop lateral movement. EDR catches what runs on hosts. Each layer catches what
the previous one missed."

The IT Director sighs. "So my expensive firewall..."

"Is still valuable. It's your first layer. But you need depth behind it."

You have demonstrated understanding of DEFENSE IN DEPTH.
                """,
                "failure_texts": {
                    0: """
Vendor stability is a valid concern for long-term operations, but it's not the
PRIMARY security issue here. The problem isn't who makes the firewall - it's
that it's the ONLY control. Defense in depth focuses on layered, diverse controls
that protect even when one layer fails or is bypassed.
                    """,
                    2: """
Buying three identical firewalls in sequence doesn't provide defense in depth.
They all fail to the same zero-day. They all miss the same evasion technique.
True layered security requires DIVERSE controls: firewalls, IDS, EDR, network
segmentation, application controls - each catching what others miss.
                    """,
                    3: """
No compliance framework mandates exactly three layers. The principle of defense
in depth is about effective security architecture, not hitting an arbitrary number.
The goal is multiple, complementary controls that provide continued protection
when individual controls fail.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Defense in depth is a fundamental security architecture principle that ensures
if one control fails or is bypassed, additional layers provide continued protection.
Key concepts:
- Multiple security controls at different layers
- Diverse control types (not just more of the same)
- Each layer addresses different threats or attack vectors
- No single point of failure should lead to complete compromise
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - Defense in Depth"
    },

    # Scenario 2: Bell-LaPadula Model
    {
        "id": "d3_scroll_classification",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE CLASSIFICATION CRISIS",
                "narrative": """
The Citadel's archives contain scrolls of varying sensitivity: PUBLIC proclamations,
CONFIDENTIAL trade agreements, SECRET military dispatches, and TOP SECRET royal
succession plans.

Young Scribe Aldric holds a SECRET clearance. He approaches you with a dilemma:

"I need to read a CONFIDENTIAL trade agreement to update my summary of merchant
routes - that's fine, I can read below my level. But I've also discovered a critical
insight that should be added to the TOP SECRET succession plans..."

He pauses. "Master Theron says I can WRITE to higher classifications but cannot
READ them. Is this true? It seems backward - shouldn't I be able to see what I'm
adding to?"

Which security model does Master Theron describe?
                """,
                "choices": [
                    {"text": "Biba Model - 'No read down, no write up' for integrity"},
                    {"text": "Bell-LaPadula Model - 'No read up, no write down' for confidentiality"},
                    {"text": "Clark-Wilson Model - Separation of duties enforcement"},
                    {"text": "Brewer-Nash Model - Chinese Wall for conflicts of interest"}
                ],
                "success_text": """
You nod at young Aldric. "Master Theron speaks of the Bell-LaPadula model, which
protects CONFIDENTIALITY - ensuring secrets flow only upward, never down."

You draw a diagram in the dust. "You hold SECRET clearance. Under Bell-LaPadula:
'No read up' means you cannot READ Top Secret - you might learn things above your
clearance. 'No write down' means you cannot WRITE to Confidential - you might
accidentally leak Secret information into a less protected document."

"So I CAN read Confidential scrolls - that's reading DOWN, which is permitted.
But writing my insight into Top Secret documents? That's writing UP, which is
also permitted - you can contribute to higher levels without compromising them."

Aldric's face lights up. "So the model prevents secrets from LEAKING DOWN, not
from being ADDED UP!"

"Exactly. Bell-LaPadula protects confidentiality by ensuring information only
flows toward higher classification, never lower."

You have demonstrated understanding of the BELL-LAPADULA MODEL.
                """,
                "failure_texts": {
                    0: """
The Biba model is actually the OPPOSITE - it protects INTEGRITY, not confidentiality.
Biba says 'No read down' (don't read less trusted sources that might corrupt your
work) and 'No write up' (don't corrupt higher-integrity data). The scenario
describes protecting secrets from leaking to lower classifications, which is
Bell-LaPadula's confidentiality focus.
                    """,
                    2: """
Clark-Wilson focuses on data integrity through well-formed transactions and
separation of duties. It doesn't address classification levels or information
flow between security levels. The scenario specifically involves reading/writing
between classification levels, which is Bell-LaPadula's domain.
                    """,
                    3: """
Brewer-Nash (Chinese Wall) prevents conflicts of interest - ensuring someone who
accesses data from one competitor cannot then access data from another. It's not
about classification levels or directional information flow. The scenario is
about military-style classification, which is Bell-LaPadula.
                    """
                }
            },
            "corporate": {
                "title": "THE DOCUMENT CLASSIFICATION DEBACLE",
                "narrative": """
The legal department has implemented a new document classification system:
PUBLIC, INTERNAL, CONFIDENTIAL, and RESTRICTED.

A junior analyst with CONFIDENTIAL clearance comes to you frustrated. "The system
is broken! I need to read an INTERNAL memo to update my analysis - and it won't
let me because it's 'below my level.' But it ALSO won't let me view RESTRICTED
board minutes that relate to my project."

Her manager chimes in: "Actually, the system is working correctly. You can read
down but not up. And when you write, you can only write to your level or higher
to prevent information leakage."

The analyst looks confused. "What model is this even based on? It seems designed
to make my job impossible!"

What security model is being implemented?
                """,
                "choices": [
                    {"text": "Biba Model - protecting data integrity"},
                    {"text": "Bell-LaPadula Model - protecting data confidentiality"},
                    {"text": "Clark-Wilson Model - enforcing separation of duties"},
                    {"text": "Brewer-Nash Model - preventing conflicts of interest"}
                ],
                "success_text": """
You open a whiteboard to explain. "This is the Bell-LaPadula model, designed to
protect CONFIDENTIALITY - keeping secrets from leaking to people without clearance."

"The rules are simple: 'No read up' means you can't access documents above your
clearance - so RESTRICTED is off-limits. 'No write down' means you can't write
to documents below your level - this prevents you from accidentally copying
confidential data into a less-protected document."

The analyst interrupts: "But I should be able to read INTERNAL memos - that's
BELOW my clearance!"

"Exactly - you CAN read down. If the system is blocking that, it's misconfigured.
Bell-LaPadula permits reading at or below your level. It only blocks reading ABOVE
your level."

The manager nods. "So the model assumes information should only flow UPWARD in
classification, never downward. Secrets go into the vault, not out of it."

"Precisely. Bell-LaPadula is all about preventing data leakage."

You have demonstrated understanding of the BELL-LAPADULA MODEL.
                """,
                "failure_texts": {
                    0: """
Biba model protects INTEGRITY, not confidentiality, with opposite rules: 'No read
down' (don't read untrusted sources) and 'No write up' (don't corrupt trusted data).
The scenario describes a system preventing reading above clearance and writing
below clearance - that's Bell-LaPadula's confidentiality model.
                    """,
                    2: """
Clark-Wilson focuses on integrity through well-formed transactions and separation
of duties. It's about ensuring data is only modified through controlled procedures
by authorized users. The scenario describes classification-based read/write
restrictions, which is the Bell-LaPadula model.
                    """,
                    3: """
Brewer-Nash (Chinese Wall) is about conflicts of interest - ensuring analysts who
access one client's data can't access a competitor's data. It has nothing to do
with hierarchical classification levels. The scenario describes a military-style
classification system, which is Bell-LaPadula.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 80,
        "hp_penalty": 30,
        "failure_text": """
Bell-LaPadula is a formal security model focused on CONFIDENTIALITY. Its core rules:
- Simple Security Property: 'No read up' - subjects cannot read objects at higher
  classification levels
- *-Property (Star Property): 'No write down' - subjects cannot write to objects
  at lower classification levels
This ensures information only flows UPWARD in classification, preventing leakage.
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - Security Models"
    },

    # Scenario 3: Symmetric vs Asymmetric Encryption
    {
        "id": "d3_key_distribution",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE HUNDRED KINGDOMS CIPHER",
                "narrative": """
The Grand Alliance of 100 kingdoms requires secure communication. Each kingdom
must exchange secret messages with the central Citadel using enchanted cipher
scrolls that require shared magical keys.

The Court Cryptographer presents his calculations: "If we use symmetric cipher
magic - where each kingdom shares a unique secret key with only the Citadel -
how many enchanted keys must we create and distribute?"

His apprentice, eager to show off, shouts: "I know this! If all 100 kingdoms need
to talk to EACH OTHER as well, we'd need 4,950 keys using the n(n-1)/2 formula!"

The Cryptographer sighs. "That's not what I asked. They only need to communicate
with the CITADEL, not with each other. It's a hub-and-spoke arrangement."

How many symmetric keys are needed for 100 kingdoms to each communicate securely
with the central Citadel?
                """,
                "choices": [
                    {"text": "100 keys - one unique shared key per kingdom-Citadel pair"},
                    {"text": "200 keys - two keys per kingdom for sending and receiving"},
                    {"text": "4,950 keys - using the n(n-1)/2 formula for all pairings"},
                    {"text": "10,000 keys - using the n-squared formula"}
                ],
                "success_text": """
The Cryptographer smiles as you give the correct answer. "Precisely! Hub-and-spoke
requires only ONE key per spoke."

He draws a diagram with the Citadel in the center and kingdoms around it. "Each
kingdom shares ONE unique symmetric key with us. Kingdom of the North has Key_North.
Kingdom of the East has Key_East. Each key encrypts messages in BOTH directions -
that's how symmetric encryption works."

The apprentice looks embarrassed. "So the 4,950 formula..."

"Only applies if EVERY kingdom needed to communicate directly with EVERY OTHER
kingdom - a full mesh. In that case, each pair needs a unique key, giving us
n(n-1)/2 combinations. But that's not our requirement."

The Cryptographer turns to you. "You understand the fundamental difference between
hub-and-spoke and full-mesh key distribution. This is why many organizations use
asymmetric encryption for key exchange - it scales better."

You have demonstrated understanding of SYMMETRIC KEY DISTRIBUTION.
                """,
                "failure_texts": {
                    1: """
Symmetric encryption uses the SAME key for both encryption and decryption - that's
what makes it 'symmetric.' You don't need separate keys for sending and receiving.
Each kingdom-Citadel pair shares ONE key that works in both directions.
                    """,
                    2: """
The n(n-1)/2 formula (giving 4,950 keys for 100 parties) applies only when ALL
parties need to communicate with ALL OTHER parties - a full mesh network. The
scenario specifies hub-and-spoke: each kingdom only talks to the Citadel, not to
other kingdoms. That requires only 100 keys - one per kingdom-Citadel relationship.
                    """,
                    3: """
The n-squared formula doesn't apply to symmetric key distribution in any standard
model. For hub-and-spoke with 100 kingdoms, you need exactly 100 keys - one shared
secret between each kingdom and the Citadel. Symmetric keys work in both directions.
                    """
                }
            },
            "corporate": {
                "title": "THE PARTNER ENCRYPTION PROBLEM",
                "narrative": """
The security team is planning encrypted file transfers with 100 external business
partners. Each partner needs to securely exchange files with your organization's
central file server.

The junior security analyst has been researching encryption and is confused:

"So if we use symmetric encryption - like AES - we need a shared secret with each
partner. That's 100 unique keys we need to manage securely. But I found this
formula online that says we need n(n-1)/2 keys, which would be 4,950!"

The senior analyst shakes her head. "That formula is for a different scenario.
Think about our actual architecture."

She turns to you. "Help our junior colleague understand. For point-to-point
symmetric encryption between our server and 100 individual partners, how many
keys do we actually need?"
                """,
                "choices": [
                    {"text": "100 keys - one unique key per partner relationship"},
                    {"text": "200 keys - we need separate encrypt and decrypt keys"},
                    {"text": "4,950 keys - using the n(n-1)/2 formula"},
                    {"text": "10,000 keys - using the n-squared formula"}
                ],
                "success_text": """
You sketch a hub-and-spoke diagram. "In our architecture, each partner only
communicates with OUR server. Partner A doesn't need to talk to Partner B. So:"

"Partner A and our server share Key_A. Partner B and our server share Key_B.
Each partner relationship needs exactly ONE symmetric key."

The junior analyst nods slowly. "So 100 partners means 100 keys..."

"Exactly. The n(n-1)/2 formula applies when EVERYONE needs to talk to EVERYONE -
like a peer-to-peer network where all 100 parties exchange files directly with
each other. That's a full mesh, requiring 4,950 unique key pairs."

The senior analyst adds: "This is actually why many organizations prefer asymmetric
encryption for these scenarios. With public key infrastructure, each party just
publishes a public key. No shared secrets to distribute securely."

"But for AES hub-and-spoke? One hundred partners, one hundred keys."

You have demonstrated understanding of SYMMETRIC KEY DISTRIBUTION.
                """,
                "failure_texts": {
                    1: """
Symmetric encryption uses the SAME key for encryption and decryption - that's the
definition of symmetric. AES with a 256-bit key uses that same key for both
operations. You don't need separate keys for each direction.
                    """,
                    2: """
The n(n-1)/2 formula calculates unique pairs when all parties need to communicate
with all other parties. With 100 partners: (100 x 99) / 2 = 4,950. But this applies
to FULL MESH networks, not hub-and-spoke. Our partners only talk to OUR server,
not to each other. That's 100 bilateral relationships = 100 keys.
                    """,
                    3: """
There's no standard symmetric key distribution model that uses n-squared. For
hub-and-spoke with 100 partners connecting to one central server, you need 100
unique shared keys - one per partner relationship. Each symmetric key is used
for both encryption and decryption.
                    """
                }
            }
        },
        "correct_index": 0,
        "xp_reward": 70,
        "hp_penalty": 25,
        "failure_text": """
Symmetric key distribution depends on the communication model:
- Hub-and-spoke: n keys (one per relationship with central node)
- Full mesh: n(n-1)/2 keys (every party needs unique key with every other party)

Symmetric encryption uses the same key for encryption and decryption, so each
bilateral relationship requires only ONE shared key that works in both directions.
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - Cryptography"
    },

    # Scenario 4: Hash Functions
    {
        "id": "d3_scroll_verification",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE TAMPERED TOME",
                "narrative": """
The Arcane Library receives a critical spellbook from a distant tower. Given the
dangerous journey through bandit-infested roads, the sending mage computed a
'magical fingerprint' of the book - a SHA-256 hash - and sent it by separate
magical courier.

When the book arrives, the librarian computes her own hash and compares it to
the one received. They match perfectly.

A young apprentice asks: "Master, what exactly does this matching hash prove?
Does it mean the book is truly from Master Eldwin? Does it mean no one can read
the spells during transit? Does it prove Master Eldwin cannot deny sending it?"

The librarian turns to you. "Explain to the apprentice what property the hash
verification provides."

What security property does hash verification prove?
                """,
                "choices": [
                    {"text": "Confidentiality - the spellbook contents were encrypted during transit"},
                    {"text": "Integrity - the spellbook was not modified during transit"},
                    {"text": "Authentication - the spellbook genuinely came from Master Eldwin"},
                    {"text": "Non-repudiation - Master Eldwin cannot deny sending the spellbook"}
                ],
                "success_text": """
You address the apprentice carefully. "The matching hash proves one thing and one
thing only: INTEGRITY. The spellbook you received is bit-for-bit identical to
what Master Eldwin sent. Not a single rune was changed."

The apprentice frowns. "But doesn't that mean it's really from him?"

"No. Consider: what if a bandit intercepted the book, replaced it with a cursed
forgery, computed a NEW hash for that forgery, and killed the courier carrying
the original hash? You'd receive a matching hash - but for the wrong book."

The librarian nods approvingly. "Hashes prove integrity, not authenticity. For
authentication and non-repudiation, Master Eldwin would need to SIGN the hash
with his private key - creating a digital signature that only he could produce."

"And confidentiality?" the apprentice asks.

"Hashes don't encrypt anything. The spellbook traveled in readable form. Anyone
who intercepted it could read every spell. Hashes verify integrity, nothing more."

You have demonstrated understanding of HASH FUNCTIONS AND INTEGRITY.
                """,
                "failure_texts": {
                    0: """
Hashes do not provide confidentiality. A hash is a one-way fingerprint, not
encryption. The spellbook contents travel in plaintext - anyone intercepting
it could read everything. The hash only verifies that what was received matches
what was sent, not that it was protected from viewing during transit.
                    """,
                    2: """
A hash alone does NOT prove authentication. An attacker could intercept the book,
replace it with a malicious version, and compute a new valid hash for their
version. The recipient would see a matching hash but receive forged content.
Authentication requires digital signatures (hash + private key), not just hashes.
                    """,
                    3: """
Non-repudiation requires something only the sender could produce - specifically,
a digital signature using their private key. Anyone can compute a hash of any
document. There's nothing in a hash that ties it to a specific sender. Without
cryptographic proof of origin, the sender can simply deny involvement.
                    """
                }
            },
            "corporate": {
                "title": "THE SOFTWARE UPDATE VERIFICATION",
                "narrative": """
The IT team is deploying a critical software update downloaded from the vendor's
website. Per security policy, they verify the SHA-256 hash published on the
vendor's HTTPS-secured download page.

The hash matches. The deployment engineer is about to approve installation when
a junior team member asks: "Wait, what does this hash actually prove? Does it
prove the software is really from the vendor? Does it mean no malware got added?"

The senior engineer pauses. "Good question. Let's be precise about what hash
verification tells us and what it doesn't."

What security property does the matching hash verification provide?
                """,
                "choices": [
                    {"text": "Confidentiality - the file was encrypted during download"},
                    {"text": "Integrity - the file was not modified during download"},
                    {"text": "Authentication - the file genuinely came from the vendor"},
                    {"text": "Non-repudiation - the vendor cannot deny publishing this file"}
                ],
                "success_text": """
You explain carefully: "The matching hash proves INTEGRITY. The file you downloaded
is exactly what was on the server when you downloaded it. No bits were corrupted
or modified in transit."

The junior team member asks: "But doesn't that prove it's really from the vendor?"

"Not quite. Consider: if an attacker compromised the vendor's website, they could
replace BOTH the software AND the hash. You'd download malware with a perfectly
matching hash. The hash proves the download wasn't modified - not that the source
is legitimate."

The senior engineer adds: "For authentication, we'd want the hash signed with the
vendor's code-signing certificate. That proves the vendor's private key was used -
something only they should possess."

"And confidentiality?"

"Hashes don't encrypt anything. You downloaded the file in the clear over HTTPS -
but that's the transport layer, not the hash. The hash is just a fingerprint."

You have demonstrated understanding of HASH FUNCTIONS AND INTEGRITY.
                """,
                "failure_texts": {
                    0: """
Hash functions don't provide confidentiality at all. A hash is a one-way fingerprint
of data, not encryption. In this case, HTTPS provides transport encryption, but
that's separate from the hash. The hash only verifies that what you downloaded
matches what was on the server - not that it was encrypted.
                    """,
                    2: """
A hash alone cannot prove authentication. If an attacker compromised the vendor's
website, they could post malicious software along with a valid hash of that
malware. You'd verify the hash and install compromised software. True authentication
requires digital signatures - the hash encrypted with the vendor's private key.
                    """,
                    3: """
Non-repudiation requires cryptographic proof that only the vendor could produce -
specifically, a digital signature using their private key. Anyone can compute a
hash of any file. The hash itself contains no proof of WHO created or published
the file. Only code signing provides non-repudiation.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Hash functions provide INTEGRITY verification - proving that data was not modified.

Hash functions do NOT provide:
- Confidentiality: Hashes don't encrypt; data travels in plaintext
- Authentication: Anyone can compute a hash; it doesn't prove origin
- Non-repudiation: No tie to a specific sender without digital signatures

For authentication and non-repudiation, you need DIGITAL SIGNATURES: the hash
encrypted with the sender's private key, which only they possess.
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - Cryptographic Hash Functions"
    },

    # Scenario 5: PKI Certificate Validation
    {
        "id": "d3_seal_of_trust",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE UNTRUSTED SEAL",
                "narrative": """
A messenger from the Duke's castle arrives with a wax-sealed scroll. The seal
bears the Duke's sigil, but your ward-scrying crystal flashes a warning:
"SEAL AUTHORITY NOT RECOGNIZED."

Investigation reveals that the Duke recently created his own official seal-making
apparatus - legitimate, but not recognized by the Kingdom's central Seal Authority.
All your ward crystals were enchanted to trust only seals verified by the Crown.

The castle's young squires have been trained to click "proceed anyway" whenever
the crystals flash warnings - "they flash all the time," they say dismissively.

How should you resolve this seal validation issue?
                """,
                "choices": [
                    {"text": "Train everyone to click 'proceed anyway' - the warnings are annoying"},
                    {"text": "Have the Duke purchase his seals from the Crown's Seal Authority"},
                    {"text": "Add the Duke's seal authority to your ward crystals' trusted list"},
                    {"text": "Disable seal validation entirely for messages from known castles"}
                ],
                "success_text": """
You immediately order: "No one clicks 'proceed anyway' without investigating.
That's how forgeries get accepted."

Then you contact the Citadel's crystal enchanters. "The Duke is an ally using
legitimate seals from his own authority. We need to add his seal authority - his
root certificate - to our ward crystals' trusted store."

Within hours, the enchantment is updated across all Citadel devices. The Duke's
seals now validate without warning, while true forgeries still trigger alerts.

The castle guard captain asks about the 'proceed anyway' habit. You shake your
head. "That trains people to ignore ALL warnings. When a real forgery arrives,
they'll click through just as easily. We validate properly, or we don't validate
at all - and if we don't validate, we shouldn't pretend we do."

You have demonstrated proper PKI CERTIFICATE TRUST MANAGEMENT.
                """,
                "failure_texts": {
                    0: """
Training users to ignore security warnings is catastrophically dangerous. They'll
click through legitimate threats just as easily as false positives. Every phishing
attack and forgery becomes easier to execute. The correct solution is to properly
configure trust relationships, not to bypass validation entirely.
                    """,
                    1: """
For INTERNAL resources like allied castles, using the Crown's (public CA) seals
is inappropriate. Public CAs shouldn't issue certificates for internal-only
resources. The Duke should maintain his own seal authority (internal CA), and
your crystals should be configured to trust it. This is proper PKI hierarchy.
                    """,
                    3: """
Disabling certificate validation removes ALL protection against forgery and
man-in-the-middle attacks. An enemy could forge the Duke's seal with impunity.
The solution is to properly configure trust, not abandon validation. Security
controls should be tuned, not bypassed.
                    """
                }
            },
            "corporate": {
                "title": "THE CERTIFICATE WARNING EPIDEMIC",
                "narrative": """
Help desk tickets are flooding in: "Browser shows certificate warning for the
HR Portal!" Investigation reveals the portal uses a certificate from your
organization's internal Certificate Authority - legitimate, but not in the
default browser trust store.

The IT director is annoyed. "Just tell everyone to click 'proceed anyway.'
It's an internal site, so it's safe."

The security team lead objects. "That's training users to ignore certificate
warnings everywhere. What happens when they get a phishing email with a link
to fake-hr-portal.company.evil.com?"

You're asked to recommend the proper solution.
                """,
                "choices": [
                    {"text": "Train users to click 'proceed anyway' for internal sites"},
                    {"text": "Purchase a public CA certificate for the internal HR portal"},
                    {"text": "Deploy the internal CA's root certificate to all managed devices"},
                    {"text": "Disable certificate validation for the corporate network"}
                ],
                "success_text": """
You explain the solution: "We deploy our internal CA's root certificate to all
managed devices through group policy. The browser will then trust our internal
CA, and certificates issued by it will validate without warnings."

The IT director asks about unmanaged devices.

"BYOD users either install our root certificate manually, or they use the
certificate warning as a reminder they're on an untrusted device accessing
internal resources. The warning becomes meaningful rather than noise."

The security lead nods approvingly. "And this preserves the integrity of
certificate warnings. When users DO see a warning, they'll know it matters -
because they don't see them constantly on legitimate sites."

You add: "Never train users to ignore security warnings. When they become
muscle memory, real attacks slip through. Configure trust properly."

You have demonstrated proper PKI CERTIFICATE TRUST MANAGEMENT.
                """,
                "failure_texts": {
                    0: """
Training users to click through certificate warnings is a security disaster
waiting to happen. When a real phishing site shows a warning, conditioned users
will click 'proceed' without thinking. This is how credential theft succeeds.
The solution is proper trust configuration, not normalized warning fatigue.
                    """,
                    1: """
Public CAs shouldn't issue certificates for internal-only resources. This exposes
internal infrastructure details in Certificate Transparency logs, may violate
CA policies, and adds unnecessary cost. Internal resources should use internal
CAs - you just need to distribute the root certificate to client devices.
                    """,
                    3: """
Disabling certificate validation removes protection against man-in-the-middle
attacks entirely. An attacker on the network could impersonate any internal
service with impunity. The solution is proper trust configuration - adding
your internal CA to the trust store - not abandoning validation.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 80,
        "hp_penalty": 30,
        "failure_text": """
PKI trust must be properly configured, not bypassed:

- Never train users to ignore certificate warnings - this enables phishing
- Internal resources should use internal CAs, not public CAs
- Deploy internal CA root certificates to managed devices through proper channels
- Certificate validation should never be disabled - configure trust instead

The goal is meaningful security warnings that users can actually respond to
correctly, not constant warnings that become background noise.
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - PKI and Certificate Management"
    },

    # Scenario 6: Digital Signatures
    {
        "id": "d3_treaty_signature",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE BINDING TREATY",
                "narrative": """
The peace treaty between the kingdoms must be signed in a way that proves the
King's agreement and prevents him from later denying he agreed to the terms.
The treaty will be copied and sent to dozens of kingdoms - all must be certain
the King actually approved.

The Royal Cryptographer presents options:

"We could encrypt the treaty with the King's public key - only he could decrypt
it. Or we could encrypt it with a symmetric key shared with the receiving kingdom.
Or we could compute a hash and send it alongside. Or..."

He pauses dramatically. "We could encrypt a hash of the treaty with the King's
PRIVATE key."

Which approach provides both authenticity and non-repudiation?
                """,
                "choices": [
                    {"text": "Encrypt the treaty with the King's public key"},
                    {"text": "Encrypt a hash of the treaty with the King's private key"},
                    {"text": "Encrypt the treaty with a symmetric key shared with recipients"},
                    {"text": "Compute a hash of the treaty and send it alongside"}
                ],
                "success_text": """
You confirm the Cryptographer's suggestion. "Only the King possesses his private
key. If we encrypt a hash of the treaty with that private key, anyone with his
public key can verify it - but only the King could have created it."

The Cryptographer nods. "This is a digital signature. The hash binds the signature
to this SPECIFIC treaty - change one word, and the hash changes, invalidating
the signature. And since only the King has the private key..."

"He cannot deny signing it," you conclude. "Non-repudiation."

The King's chancellor looks concerned. "What if the King's private seal is stolen?"

"Then we have a revocation crisis. But with proper key protection - which is why
we use the enchanted seal-ring that never leaves his finger - the signature
provides authentication AND non-repudiation. The treaty is bound to the King's
identity permanently."

You have demonstrated understanding of DIGITAL SIGNATURES.
                """,
                "failure_texts": {
                    0: """
Encrypting with the King's PUBLIC key provides confidentiality - only the King
could decrypt it. But it proves nothing about WHO encrypted it - anyone can use
the public key. It provides no authentication or non-repudiation. You want the
opposite: encrypt with the PRIVATE key so only the King could have done it.
                    """,
                    2: """
Symmetric encryption cannot provide non-repudiation because BOTH parties share
the key. Either party could have encrypted the document. The King could claim
the recipient forged it. Only asymmetric cryptography, where the King alone
holds his private key, provides non-repudiation.
                    """,
                    3: """
A hash alone proves integrity but nothing about WHO created the document.
Anyone can compute a hash. There's no proof that the King created or approved
the treaty. For authentication and non-repudiation, the hash must be SIGNED
with the King's private key - creating a digital signature.
                    """
                }
            },
            "corporate": {
                "title": "THE CONTRACT SIGNATURE REQUIREMENT",
                "narrative": """
A major contract requires a digital signature that proves the CEO signed it
and prevents the CEO from later denying the signature. The legal team needs
cryptographic non-repudiation.

The IT security team presents options:

"We could encrypt the contract with the CEO's public key for confidentiality.
We could use a shared symmetric key with the other party. We could compute a
hash to prove integrity. Or we could encrypt a hash of the contract using the
CEO's private key..."

The legal counsel interrupts: "I need to explain this in court if challenged.
Which option provides proof that our CEO specifically signed this document?"
                """,
                "choices": [
                    {"text": "Encrypt the contract with the CEO's public key"},
                    {"text": "Encrypt a hash of the contract with the CEO's private key"},
                    {"text": "Encrypt the contract with a symmetric key shared with the recipient"},
                    {"text": "Compute a hash of the contract and send it alongside"}
                ],
                "success_text": """
You explain to legal counsel: "A digital signature is created by hashing the
document and encrypting that hash with the CEO's private key. This provides:"

"Authentication: Anyone with the CEO's public key can decrypt and verify the
hash, confirming it was signed by someone holding the private key."

"Integrity: The hash is bound to the exact document contents. Any modification
invalidates the signature."

"Non-repudiation: Assuming proper key management, only the CEO has access to
the private key. She cannot claim someone else signed it."

The legal counsel nods. "So in court, we show: here's the signed hash, here's
the CEO's public key, the math checks out, and only she could have created it."

"Exactly. This is the cryptographic equivalent of a witnessed signature, but
mathematically verifiable."

You have demonstrated understanding of DIGITAL SIGNATURES.
                """,
                "failure_texts": {
                    0: """
Encrypting with the CEO's public key provides confidentiality (only she can
decrypt), but offers no proof SHE created the document. Anyone can encrypt
with a public key. For non-repudiation, you need the PRIVATE key - something
only the CEO possesses - to create proof of authorship.
                    """,
                    2: """
Symmetric encryption fundamentally cannot provide non-repudiation. If both
parties share the key, either could have created the encrypted document.
The CEO could claim the counterparty forged it using the shared key. Only
asymmetric cryptography with private keys provides non-repudiation.
                    """,
                    3: """
A hash alone proves the document wasn't modified, but anyone can compute a
hash of any document. There's no proof of who created the hash or approved
the document. For non-repudiation, the hash must be encrypted with the CEO's
private key - something only she possesses.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 80,
        "hp_penalty": 30,
        "failure_text": """
Digital signatures provide authentication, integrity, and non-repudiation:

1. Hash the document (binds signature to exact contents)
2. Encrypt the hash with the signer's PRIVATE key (only they can create it)
3. Anyone with the public key can verify (but cannot forge)

Key insight: PUBLIC key encryption = confidentiality (anyone can encrypt, only
key holder can decrypt). PRIVATE key encryption = authentication (only key
holder can create, anyone can verify).
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - Digital Signatures"
    },

    # Scenario 7: Physical Security Layers
    {
        "id": "d3_castle_design",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE ARCHITECT'S QUESTION",
                "narrative": """
The Master Architect is designing a new secure fortress for the realm's most
precious treasures. She presents her plans, showing concentric rings of security:

"Visitors first encounter the outer perimeter, then the fortress walls, then
the great hall, and finally the vault chamber. But I need to verify: what is
the correct order of physical security zones from OUTERMOST to INNERMOST?"

Her apprentice has scrambled the notes. The zones listed are:
- Vault chamber (individual secure cages)
- Main hall (general controlled area)
- Fortress entrance (building access point)
- Outer grounds (perimeter with walls and guards)

What is the correct order from outermost to innermost?
                """,
                "choices": [
                    {"text": "Vault chamber - Fortress entrance - Outer grounds - Main hall"},
                    {"text": "Outer grounds - Fortress entrance - Main hall - Vault chamber"},
                    {"text": "Fortress entrance - Outer grounds - Vault chamber - Main hall"},
                    {"text": "Main hall - Vault chamber - Fortress entrance - Outer grounds"}
                ],
                "success_text": """
You trace the proper progression on the architect's plans. "A visitor must pass
through each layer in sequence, from outside to inside:"

"First, the OUTER GROUNDS - the perimeter. Guards, walls, gates that control
who can even approach the fortress."

"Then, the FORTRESS ENTRANCE - the building itself. Additional verification
before entering the structure."

"Next, the MAIN HALL - the controlled interior space. General access areas
where authorized visitors may conduct business."

"Finally, the VAULT CHAMBER - the innermost sanctum. Individual secure cages
containing the most sensitive treasures, with the highest access controls."

The Architect nods. "Each layer requires successfully passing through all
previous layers. An intruder must defeat every defense in sequence."

You have demonstrated understanding of PHYSICAL SECURITY LAYERING.
                """,
                "failure_texts": {
                    0: """
This order is completely inverted - it lists innermost to outermost. Physical
security uses concentric rings from the perimeter inward: first you must pass
the outer perimeter, then building access, then restricted areas, then the
most secure inner sanctum. Each layer requires passing all previous layers.
                    """,
                    2: """
The fortress entrance cannot come before the outer grounds - you must pass
through the perimeter before reaching the building entrance. Physical security
zones are concentric: perimeter first, then building access, then interior
zones, then high-security areas.
                    """,
                    3: """
This order is reversed. The main hall (interior space) comes AFTER the
entrance, not before. And the vault is innermost, not second. Physical security
layers progress inward: perimeter, building access, general interior, secure
interior.
                    """
                }
            },
            "corporate": {
                "title": "THE DATA CENTER DESIGN REVIEW",
                "narrative": """
The facilities team presents their new data center security design for review.
They've planned concentric security zones, but want verification they have
the layers in the correct order from outermost to innermost:

The zones listed are:
- Server cages (individual locked enclosures for servers)
- Data hall (the main server room floor)
- Building entrance (lobby, reception, badge access)
- Parking lot (perimeter fence, gate, guards)

"We want to ensure someone must pass through each zone in sequence to reach
the servers. What's the correct order from the outside in?"
                """,
                "choices": [
                    {"text": "Server cages - Building entrance - Parking lot - Data hall"},
                    {"text": "Parking lot - Building entrance - Data hall - Server cages"},
                    {"text": "Building entrance - Parking lot - Server cages - Data hall"},
                    {"text": "Data hall - Server cages - Building entrance - Parking lot"}
                ],
                "success_text": """
You walk through the correct sequence. "Think about what a visitor - or an
attacker - must pass through to reach the servers:"

"PARKING LOT first - the outer perimeter. Fencing, gates, security cameras,
maybe a guard booth. This controls who can even approach the building."

"BUILDING ENTRANCE next - lobby, reception, badge readers, mantraps perhaps.
This is building access control - proving you're authorized to be in the
facility."

"DATA HALL follows - the server room floor itself. Biometric access, escorts
for visitors, environmental controls. A restricted zone within the building."

"SERVER CAGES innermost - individual locked enclosures. The specific rack
or cage containing the most sensitive equipment. Highest access restrictions."

The facilities manager nods. "So each layer adds security, and you must
defeat all previous layers to reach the next."

You have demonstrated understanding of PHYSICAL SECURITY LAYERING.
                """,
                "failure_texts": {
                    0: """
This order starts with the innermost layer and scrambles the rest. Server cages
are the INNERMOST protection, not the first. Physical security is concentric:
perimeter (parking lot) first, then building access, then restricted areas
(data hall), then high-security zones (server cages).
                    """,
                    2: """
You must pass through the parking lot (perimeter) BEFORE reaching the building
entrance. Physical security zones progress inward: perimeter first, then
building access, then interior zones. You can't enter a building you can't
approach.
                    """,
                    3: """
This order is completely reversed. Physical security layers from outermost to
innermost are: perimeter (parking lot), building access (entrance), restricted
area (data hall), high-security zone (server cages). Each layer requires
defeating all previous layers.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 70,
        "hp_penalty": 20,
        "failure_text": """
Physical security uses concentric layers from OUTERMOST to INNERMOST:

1. Perimeter (parking lot, fencing, gates) - controls approach
2. Building entrance (lobby, reception, badge access) - controls building access
3. Restricted areas (data hall, secure floors) - limits internal movement
4. High-security zones (server cages, vaults) - protects most sensitive assets

Each layer requires successfully passing through all previous layers. An
attacker must defeat every control in sequence to reach the target.
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - Physical Security"
    },

    # Scenario 8: Fire Suppression Systems
    {
        "id": "d3_scroll_room_fire",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE ARCHIVE FIRE DEBATE",
                "narrative": """
The new Archive of Infinite Scrolls is being designed, and a fierce debate has
erupted about fire suppression. The scrolls are irreplaceable, but scribes work
in the archive day and night.

The Builder's Guild proposes four options:

"Water pipes running throughout - proven effective against fires!"

"Enchanted gas that smothers flames - no water damage, safe for workers to
breathe and evacuate!"

"Alchemical powder deployed from the ceiling - instant fire suppression!"

"Heavy suffocating mist that displaces all air - fire cannot burn without air!"

The Head Librarian is adamant: "The scrolls cannot be damaged. But our scribes
must have time to evacuate safely!"

Which suppression system meets both requirements?
                """,
                "choices": [
                    {"text": "Water pipes throughout the archive"},
                    {"text": "Enchanted gas that smothers flames (clean agent)"},
                    {"text": "Alchemical powder from the ceiling (dry chemical)"},
                    {"text": "Heavy suffocating mist that displaces all air (CO2 flooding)"}
                ],
                "success_text": """
You recommend the enchanted gas system. "Clean agent suppression - like the
modern FM-200 or Novec 1230 - provides everything we need."

"It suppresses fire effectively through chemical interruption of the combustion
reaction, not by removing oxygen. This means scribes can breathe during
evacuation. The design concentration allows several minutes for safe egress."

"It leaves no residue - no water damage to scrolls, no corrosive powder coating
ancient parchment. After the fire is suppressed, the gas dissipates cleanly."

The Builder's Guild Master nods. "And the alternatives?"

"Water destroys the scrolls as surely as fire. Dry powder leaves corrosive
residue that damages delicate materials over time. CO2 flooding displaces
oxygen so completely that anyone trapped would suffocate - it's designed
for unoccupied spaces."

The Librarian sighs with relief. "Then clean agent it is."

You have demonstrated understanding of FIRE SUPPRESSION SYSTEMS for sensitive areas.
                """,
                "failure_texts": {
                    0: """
Water is absolutely inappropriate for archives containing valuable documents.
Water damage from sprinklers often destroys more than the fire itself. For
document storage, server rooms, and museums, clean agent suppression protects
assets without causing secondary damage.
                    """,
                    2: """
Dry chemical suppression leaves corrosive residue that damages sensitive
equipment and materials. The powder coats everything and requires extensive
cleanup. It's inappropriate for data centers, archives, or areas with delicate
electronics or documents.
                    """,
                    3: """
CO2 flooding displaces oxygen to suffocate fires - but it also suffocates
people. It's only appropriate for normally unoccupied spaces with proper
warning systems and evacuation procedures. For occupied spaces like an archive
with scribes, clean agent systems (FM-200, Novec) are the correct choice as
they allow safe evacuation.
                    """
                }
            },
            "corporate": {
                "title": "THE SERVER ROOM SUPPRESSION SELECTION",
                "narrative": """
The new server room needs fire suppression. The facilities manager presents
the options to the decision committee:

"Wet pipe sprinklers - standard building code, lowest cost, proven effective."

"Clean agent gas system - FM-200 or Novec 1230. More expensive, but no water."

"Dry chemical system - industrial grade, fast knockdown of fires."

"CO2 flooding system - removes oxygen so fire cannot burn."

The CTO speaks up: "Whatever we choose, remember that the night operations
team works in there 24/7. We can't choose something that kills our employees."

The CFO counters: "And we can't choose something that destroys $10 million
in servers during a false activation."

Which system meets both requirements?
                """,
                "choices": [
                    {"text": "Wet pipe sprinkler system"},
                    {"text": "Clean agent gas suppression (FM-200/Novec)"},
                    {"text": "Dry chemical extinguisher system"},
                    {"text": "CO2 flooding system"}
                ],
                "success_text": """
You recommend clean agent gas. "FM-200 or Novec 1230 provides exactly what
we need."

"First, it's safe for occupied spaces at design concentrations. The night
team will have time to evacuate, and the gas isn't an asphyxiant like CO2.
They can breathe while exiting."

"Second, it leaves no residue. No water damage to servers, no corrosive
powder coating circuit boards. After activation, the gas dissipates and
equipment can be powered back on after inspection."

The CFO asks about cost. "It's more expensive upfront, but consider: one
wet pipe activation destroys everything. One dry chemical activation
requires extensive cleaning and may still cause corrosion damage. CO2
requires the room to be completely evacuated before activation - risky
with 24/7 operations."

"Clean agent has the highest upfront cost but lowest risk of secondary
damage and highest personnel safety."

You have demonstrated understanding of FIRE SUPPRESSION SYSTEMS for data centers.
                """,
                "failure_texts": {
                    0: """
Water and electronics don't mix. A wet pipe sprinkler activation - or worse,
a false activation - would destroy the servers as effectively as fire. Server
rooms, data centers, and telecom facilities require clean agent suppression
that won't cause water damage.
                    """,
                    2: """
Dry chemical leaves corrosive residue that damages sensitive electronics.
The powder coats everything, gets into equipment, and requires extensive
cleanup. It can cause more long-term damage than a small fire. Clean agent
systems are specifically designed for electronics environments.
                    """,
                    3: """
CO2 systems remove oxygen to suppress fire - but this is lethal to personnel.
With 24/7 operations, you cannot use a system that kills anyone who doesn't
evacuate immediately. CO2 is for unmanned spaces only. Clean agent systems
(FM-200, Novec) are safe for occupied spaces while still protecting equipment.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Fire suppression for sensitive areas must balance asset protection and personnel safety:

- Wet pipe (water): Damages electronics and documents; inappropriate for server rooms
- Dry chemical: Leaves corrosive residue; damages sensitive equipment
- CO2 flooding: Displaces oxygen; lethal to personnel; for unoccupied spaces only
- Clean agent (FM-200, Novec): Safe for occupied spaces, no residue, no damage to equipment

For occupied spaces with sensitive equipment, clean agent suppression is the
standard solution.
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - Environmental Controls"
    },

    # Scenario 9: Hardware Security Modules
    {
        "id": "d3_key_vault",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE KEY KEEPER'S DILEMMA",
                "narrative": """
The Kingdom's payment system for merchant transactions requires protecting the
master encryption keys that secure all gold transfers. The Royal Auditors
have decreed: "The keys must NEVER exist in readable form outside of tamper-proof
magical protection."

The Treasurer presents options for storing the master keys:

"We could lock them in an enchanted database with powerful access wards."

"We could use a Cryptographic Keystone - a magical artifact that holds keys
internally and performs all encryption operations within itself, never
exposing the keys."

"We could inscribe them on protected scrolls locked in a warded vault."

"We could encrypt them with secondary magic and rotate them monthly."

Which approach satisfies the auditors' requirement?
                """,
                "choices": [
                    {"text": "Store keys in an enchanted database with access controls"},
                    {"text": "Use a Cryptographic Keystone (Hardware Security Module)"},
                    {"text": "Keep keys on protected scrolls in a physical vault"},
                    {"text": "Implement magical encryption with regular key rotation"}
                ],
                "success_text": """
You advise using the Cryptographic Keystone. "This is the only solution that
truly keeps keys protected at ALL times."

"A Hardware Security Module - our Keystone - generates keys internally. Stores
them internally. Performs all cryptographic operations internally. The keys
NEVER leave the tamper-resistant boundary, never exist in readable form
anywhere else."

The Treasurer looks puzzled. "But the encrypted database also protects them..."

"Until you need to USE them. When encrypting a transaction, the key must be
decrypted into memory to perform the operation. For that moment, the key
exists in plaintext in the server's memory - and could be extracted by an
attacker with memory access."

"The Keystone does the encryption INSIDE itself. You send it the data, it
encrypts with the internal key, returns the result. The key never leaves."

The auditors nod approvingly. "This meets our requirement."

You have demonstrated understanding of HARDWARE SECURITY MODULES.
                """,
                "failure_texts": {
                    0: """
An encrypted database protects keys at rest, but not in use. When you need to
encrypt a transaction, the key must be decrypted and loaded into memory -
creating a window where it exists in plaintext. An attacker with memory access
could extract it. HSMs keep keys protected even during operations.
                    """,
                    2: """
Physical vault storage protects keys when not in use, but to use a key you must
retrieve it, load it into memory, perform operations, then secure it again.
During that entire time, the key exists in readable form. HSMs perform operations
internally without ever exposing the key.
                    """,
                    3: """
Encryption-at-rest and key rotation are good practices, but don't solve the
fundamental problem: at some point, the key must be decrypted to be used. That
moment of plaintext exposure is what the auditors are concerned about. Only
HSMs perform operations without ever exposing keys in plaintext.
                    """
                }
            },
            "corporate": {
                "title": "THE PCI COMPLIANCE CHALLENGE",
                "narrative": """
The payment security audit is next week, and the auditors have flagged a critical
requirement: "Cryptographic keys used for PIN encryption must NEVER exist in
plaintext outside of tamper-resistant hardware. NEVER."

The IT team presents their options:

"We currently store keys in an encrypted database with strict access controls.
We could strengthen the encryption and add more logging."

"We could implement a Hardware Security Module that performs all cryptographic
operations internally without exposing keys."

"We could keep keys on encrypted USB drives in a physical safe, retrieved
only when needed."

"We could implement software-based key encryption with monthly rotation."

The CISO looks grim. "If we fail this requirement, we lose our ability to
process payments. Which option actually satisfies the auditors?"
                """,
                "choices": [
                    {"text": "Strengthen database encryption with better access controls"},
                    {"text": "Deploy a Hardware Security Module for all key operations"},
                    {"text": "Keep keys on encrypted USB drives in a physical safe"},
                    {"text": "Implement software encryption with monthly rotation"}
                ],
                "success_text": """
You recommend the HSM. "There's only one way to satisfy 'NEVER in plaintext
outside tamper-resistant hardware' - use tamper-resistant hardware."

"An HSM generates keys inside itself. They're stored inside. When we need to
encrypt a PIN, we send the PIN to the HSM, it encrypts using the internal
key, and returns the encrypted result. The key NEVER leaves the HSM boundary."

The IT lead asks: "What about the encrypted database approach?"

"When the application needs to encrypt something, it decrypts the key from
the database, loads it into memory, performs the operation, then erases it.
For that period - even if it's milliseconds - the key exists in plaintext
in memory. An attacker with memory access or a core dump could extract it."

"USB drives in a safe?"

"Same problem. You have to load the key into memory to use it."

"The HSM is the only solution where keys are NEVER exposed."

You have demonstrated understanding of HARDWARE SECURITY MODULES.
                """,
                "failure_texts": {
                    0: """
Database encryption protects keys at rest but not in use. When performing
cryptographic operations, the key must be decrypted into system memory. Even
briefly, it exists in plaintext and could be extracted through memory analysis.
PCI DSS requires keys NEVER exist in plaintext outside secure hardware - only
HSMs meet this requirement.
                    """,
                    2: """
Physical security for key storage doesn't address the operational problem.
When you retrieve the USB drive and load the key for use, it exists in plaintext
in memory. PCI DSS explicitly requires keys never exist in plaintext outside
tamper-resistant hardware - including during operations. Only HSMs perform
operations internally.
                    """,
                    3: """
Software encryption and rotation improve security but don't satisfy the
requirement. At some point, the key must be in plaintext memory to perform
operations. No amount of software security changes this fundamental issue.
Only hardware security modules keep keys permanently protected, even during
cryptographic operations.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 85,
        "hp_penalty": 30,
        "failure_text": """
Hardware Security Modules (HSMs) provide unique protection for cryptographic keys:

- Keys are generated INSIDE the HSM and never leave
- All cryptographic operations happen INSIDE the HSM
- Keys never exist in plaintext in system memory
- Tamper-resistant hardware provides physical protection

For compliance requirements like PCI DSS that mandate keys never exist in
plaintext outside secure hardware, HSMs are the only compliant solution.
Software encryption always exposes keys in memory during operations.
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - Hardware Security"
    },

    # Scenario 10: Buffer Overflow Prevention
    {
        "id": "d3_ancient_spell",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE CORRUPTED SPELLBOOK",
                "narrative": """
The ancient spell compiler - used for generations to create magical artifacts -
has a fatal flaw. Malicious input can overflow the rune buffer, allowing
attackers to inject their own spell commands into the compiler's execution.

Complete rewriting of the ancient compiler is impossible - generations of
spells depend on its exact quirks. The Archmage asks what protective
enchantments can be layered around it to mitigate the vulnerability.

"We have several options," the Security Enchanter explains:

"Scrying wards that detect unusual behavior - but cannot stop attacks in progress."

"Input purification at the castle gates - but many attack vectors bypass the gates."

"Memory randomization so attackers cannot predict where to inject, plus
execution barriers on memory regions containing data."

"Isolation wards around the compiler - limit damage but don't prevent the attack."

Which combination best mitigates the buffer overflow vulnerability?
                """,
                "choices": [
                    {"text": "Address Space Layout Randomization (ASLR) + Data Execution Prevention (DEP)"},
                    {"text": "Intrusion Detection System (IDS) + Web Application Firewall (WAF)"},
                    {"text": "Input validation at the network tier + Database encryption"},
                    {"text": "Network segmentation + Endpoint antivirus"}
                ],
                "success_text": """
You recommend the combination of memory randomization and execution barriers.
"ASLR and DEP work together to make buffer overflows much harder to exploit,
even when we can't fix the underlying vulnerability."

"ASLR - Address Space Layout Randomization - shuffles where code and data are
loaded in memory. An attacker crafting an overflow doesn't know where to point
their injected code. They might guess, but with randomization, they'll almost
certainly guess wrong."

"DEP - Data Execution Prevention - marks data memory regions as non-executable.
Even if an attacker successfully overflows the buffer and injects code, the
processor refuses to execute it. The data stack isn't for code."

The Security Enchanter nods. "Together, they don't patch the hole, but they
make it nearly impossible to exploit. The attacker can't find their target,
and can't execute their payload if they somehow do."

You have demonstrated understanding of BUFFER OVERFLOW MITIGATIONS.
                """,
                "failure_texts": {
                    0: """
IDS and WAF may detect some attack patterns, but they don't prevent exploitation
if an attack gets through. They're detective and preventive at the network layer,
but buffer overflows happen at the host layer. If an attacker bypasses the WAF
signature, the vulnerable application is still exploitable.
                    """,
                    2: """
Input validation at the web tier helps with web-based attacks but doesn't
protect against all buffer overflow vectors. And database encryption has
nothing to do with buffer overflows - it protects data at rest, not in-memory
code execution. These are unrelated to the vulnerability.
                    """,
                    3: """
Network segmentation limits lateral movement AFTER a compromise, and antivirus
may catch known malware, but neither prevents buffer overflow exploitation.
The attack happens before segmentation helps, and custom exploit code won't
match antivirus signatures. ASLR + DEP directly address the overflow mechanics.
                    """
                }
            },
            "corporate": {
                "title": "THE LEGACY APPLICATION CRISIS",
                "narrative": """
A critical legacy application has a known buffer overflow vulnerability, but
the vendor is defunct and source code was never provided. Rewriting is impossible
in the short term - the business cannot function without this application.

The security team needs to implement compensating controls while long-term
replacement is planned. The options:

"Deploy IDS and WAF to detect and block attack signatures."

"Implement ASLR and DEP through operating system settings."

"Add input validation at the application gateway and encrypt the database."

"Segment the network and deploy enhanced antivirus."

The CISO asks: "Which option most directly mitigates the buffer overflow risk?"
                """,
                "choices": [
                    {"text": "ASLR (Address Space Layout Randomization) + DEP (Data Execution Prevention)"},
                    {"text": "IDS (Intrusion Detection) + WAF (Web Application Firewall)"},
                    {"text": "Input validation + Database encryption"},
                    {"text": "Network segmentation + Endpoint antivirus"}
                ],
                "success_text": """
You explain the recommendation: "ASLR and DEP are the most direct mitigations
for buffer overflow vulnerabilities, even without application changes."

"ASLR randomizes where the application and libraries are loaded in memory.
Buffer overflow exploits need to know WHERE to redirect execution. With
randomization, they're shooting in the dark - most attempts will crash the
app harmlessly rather than executing malicious code."

"DEP marks memory regions as either executable OR writable, not both. Even if
an attacker successfully overwrites a return pointer, the injected shellcode
sits in a data region that won't execute. The processor refuses to run it."

The team lead asks about the other options.

"IDS/WAF might catch known attack patterns but miss variants. Input validation
helps but may have bypasses. Network segmentation limits damage AFTER compromise.
AV misses custom exploits. Only ASLR + DEP address the vulnerability mechanics
directly."

You have demonstrated understanding of BUFFER OVERFLOW MITIGATIONS.
                """,
                "failure_texts": {
                    0: """
IDS and WAF can detect known attack patterns, but they operate at the network
layer and can be bypassed. They don't prevent exploitation if an attacker
crafts an unrecognized payload. For buffer overflows, you need host-level
protections that make exploitation mechanically difficult: ASLR and DEP.
                    """,
                    2: """
Input validation may prevent some attack vectors but not all - buffer overflows
can occur through many input paths. And database encryption is completely
unrelated to buffer overflow protection - it protects data at rest, not
in-memory code execution. These don't address the core vulnerability.
                    """,
                    3: """
Network segmentation limits the blast radius AFTER an attacker gains code
execution - it doesn't prevent the initial exploit. Antivirus relies on
signatures that custom exploit code won't match. Neither directly addresses
the buffer overflow mechanics. ASLR + DEP make exploitation difficult at
the host level.
                    """
                }
            }
        },
        "correct_index": 0,
        "xp_reward": 90,
        "hp_penalty": 35,
        "failure_text": """
Buffer overflow mitigations at the OS level:

- ASLR (Address Space Layout Randomization): Randomizes memory addresses, making
  it difficult for attackers to predict where to redirect execution
- DEP (Data Execution Prevention): Marks memory as non-executable, preventing
  injected code from running even if written to memory

Together, these make exploitation significantly harder even when the underlying
vulnerability cannot be patched. Other controls (IDS, WAF, AV) may detect
attacks but don't prevent exploitation if bypassed.
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - Vulnerability Mitigation"
    },

    # Scenario 11: Cloud Shared Responsibility
    {
        "id": "d3_cloud_castle",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE FLOATING FORTRESS ACCORD",
                "narrative": """
The Kingdom has contracted with the Sky Mages to host their war planning
chambers in a Floating Fortress - a magical cloud platform. The accord
clearly divides responsibilities.

The Sky Mages provide: the physical fortress structure, the levitation
enchantments, the defensive wards around the platform, and the magical
conduits connecting fortress sections.

The Kingdom provides: their own scrying orbs, spell books, warding schemes
for their specific chambers, and decisions about what treasures to store there.

A dispute arises: the Kingdom's battle maps were corrupted by a miscast spell.
The Kingdom blames the Sky Mages. The Sky Mages say operating the scrying
orbs is the Kingdom's responsibility.

In this Infrastructure as a Service arrangement, who is responsible for
the "operating systems" of the scrying orbs?
                """,
                "choices": [
                    {"text": "The Sky Mages - they provide all magical infrastructure"},
                    {"text": "The Sky Mages - they maintain the levitation enchantments"},
                    {"text": "The Kingdom - they are responsible for their own systems and spells"},
                    {"text": "Shared equally - both parties maintain everything together"}
                ],
                "success_text": """
You clarify the shared responsibility model. "In an Infrastructure as a Service
arrangement - which this Floating Fortress represents - the provider handles
the infrastructure layer while the customer handles everything above it."

"The Sky Mages are responsible for: physical fortress security, levitation
magic, the platform's structural integrity, and the magical conduits - think
of these as physical security, hypervisor, and network infrastructure."

"The Kingdom is responsible for: the scrying orbs themselves, how they're
configured, what spells run on them, and their security settings. These are
analogous to operating systems, applications, and data."

The Sky Mage ambassador nods. "So when the Kingdom's miscast spell corrupted
their battle maps, that was their operating system - their responsibility."

"Exactly. In IaaS, customers are responsible for OS hardening and patching.
The provider only handles the infrastructure 'of' the cloud, not what the
customer runs 'in' the cloud."

You have demonstrated understanding of CLOUD SHARED RESPONSIBILITY.
                """,
                "failure_texts": {
                    0: """
In IaaS (Infrastructure as a Service), the provider does NOT handle customer
operating systems. They provide the infrastructure: physical security, network,
virtualization. The customer is responsible for everything they deploy ON that
infrastructure: OS, applications, configurations, and data.
                    """,
                    1: """
Levitation enchantments represent hypervisor/virtualization - that IS the
provider's responsibility. But operating system management is the customer's
responsibility in IaaS. The provider manages the PLATFORM; the customer manages
what runs ON the platform.
                    """,
                    3: """
Cloud shared responsibility is NOT shared equally - it's divided by layer.
In IaaS, the provider handles infrastructure (physical, network, virtualization)
and the customer handles everything above (OS, applications, data). Clear
boundaries prevent confusion and gaps in security coverage.
                    """
                }
            },
            "corporate": {
                "title": "THE CLOUD BLAME GAME",
                "narrative": """
The company's web application was compromised through an unpatched operating
system vulnerability on their IaaS cloud instances. Customer data was stolen.

The VP of IT storms into the post-incident meeting. "This is AWS's fault!
We're paying them for cloud services and they let our servers get hacked!"

The AWS representative calmly pulls up the shared responsibility model.
"In IaaS, we handle security OF the cloud - physical, network, and hypervisor.
You handle security IN the cloud - operating systems, applications, and data."

The VP isn't satisfied. "Then what are we paying you for?"

You're asked to clarify: In IaaS, which security control is the CUSTOMER's
responsibility?
                """,
                "choices": [
                    {"text": "Physical security of the data center"},
                    {"text": "Hypervisor patching and security"},
                    {"text": "Operating system hardening and patching"},
                    {"text": "Network infrastructure redundancy"}
                ],
                "success_text": """
You explain the shared responsibility model. "Let me walk through what
each party owns in IaaS."

"AWS handles security OF the cloud: physical data center security - locks,
guards, environmental controls. Network infrastructure - switches, routers,
DDoS protection. Virtualization layer - hypervisor patching and isolation."

"We handle security IN the cloud: operating system selection, hardening, and
patching. Application deployment and security. Data encryption and access
controls. Network configurations within our VPC."

The VP interjects: "So the unpatched OS..."

"Is entirely our responsibility. We chose to deploy that OS. We chose not to
patch it. AWS provides the compute instance; we're responsible for what runs
on it. This attack succeeded because WE didn't patch - not because AWS failed."

"In IaaS, 'you build it, you secure it' applies to everything above the
hypervisor layer."

You have demonstrated understanding of CLOUD SHARED RESPONSIBILITY.
                """,
                "failure_texts": {
                    0: """
Physical security of the data center is ALWAYS the cloud provider's
responsibility, regardless of the service model (IaaS, PaaS, or SaaS).
Customers cannot access or secure physical infrastructure they don't own.
This is fundamental to the shared responsibility model.
                    """,
                    1: """
Hypervisor security is the cloud provider's responsibility in IaaS. They manage
the virtualization layer that separates customer instances. If a hypervisor
vulnerability allowed cross-VM attacks, that would be AWS's failure. The
customer's responsibility starts at the operating system layer.
                    """,
                    3: """
Network infrastructure redundancy (physical switches, routers, connectivity)
is the provider's responsibility. They ensure the infrastructure OF the cloud
is reliable. Customers manage their network CONFIGURATIONS within that
infrastructure - security groups, NACLs, VPC design - but not the underlying
network hardware.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 80,
        "hp_penalty": 25,
        "failure_text": """
Cloud Shared Responsibility Model for IaaS:

Provider (security OF the cloud):
- Physical security
- Network infrastructure
- Hypervisor/virtualization

Customer (security IN the cloud):
- Operating systems
- Applications
- Data and encryption
- Access management
- Network configuration (security groups, NACLs)

In IaaS, everything from the OS layer up is the customer's responsibility.
The provider only handles infrastructure underneath.
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - Cloud Security"
    },

    # Scenario 12: Virtualization Security
    {
        "id": "d3_mirror_realms",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE MIRROR REALM BREACH",
                "narrative": """
The Citadel uses Mirror Realms - pocket dimensions created and managed by
a powerful Dimension Weaver - to isolate sensitive operations. Each realm
is supposed to be completely separate from others.

A terrifying report arrives: a demon summoned in one Mirror Realm somehow
reached through the dimensional barriers and read the memories of an archmage
working in an adjacent realm. The Weaver's isolation magic was supposed to
prevent any cross-realm interference.

The Dimension Weaver is horrified. "This should be impossible! Each realm
exists in its own isolated space, managed by my enchantments..."

What type of security breach has occurred?
                """,
                "choices": [
                    {"text": "Container escape - the demon broke out of a weaker container boundary"},
                    {"text": "VM escape / Hypervisor breakout - the demon bypassed realm isolation"},
                    {"text": "Side-channel attack - the demon observed indirect magical resonance"},
                    {"text": "Privilege escalation - the demon gained higher permissions within its realm"}
                ],
                "success_text": """
You identify the breach type. "This is a VM escape - what we'd call hypervisor
breakout. The demon broke through the fundamental isolation boundary between
realms."

The Dimension Weaver looks stricken. "My isolation enchantments..."

"Are analogous to a hypervisor - the magical layer that creates and separates
the realms. A VM escape occurs when code running inside a virtual machine
can break out to access the hypervisor or other VMs. The demon found a flaw
in your dimensional boundaries."

"But I maintain those boundaries so carefully!"

"Hypervisor vulnerabilities are rare but catastrophic. They invalidate the
entire isolation model that virtualization depends on. One compromised realm
can now reach ALL realms you manage - the Weaver itself, and every mirror
dimension it controls."

"We need to find and patch this dimensional flaw immediately."

You have demonstrated understanding of VIRTUALIZATION SECURITY BREACHES.
                """,
                "failure_texts": {
                    0: """
Container escape involves breaking out of container isolation - a different
and weaker boundary than VM isolation. Mirror Realms (full pocket dimensions)
are analogous to full virtual machines, not containers. The breach of realm
boundaries is VM escape, not container escape.
                    """,
                    2: """
Side-channel attacks extract information through indirect observation - timing,
power consumption, electromagnetic emissions. The demon directly accessed
another realm's memory, not indirect leakage. This is direct boundary
violation (VM escape), not side-channel analysis.
                    """,
                    3: """
Privilege escalation involves gaining higher permissions within the SAME system.
The demon didn't get root access in its own realm - it reached a completely
separate realm. Crossing isolation boundaries between VMs is hypervisor
breakout, not privilege escalation.
                    """
                }
            },
            "corporate": {
                "title": "THE VIRTUAL INFRASTRUCTURE NIGHTMARE",
                "narrative": """
A security researcher discloses a terrifying vulnerability: a process running
inside a virtual machine can read memory from OTHER virtual machines running
on the same hypervisor. The isolation boundary that keeps VMs separate has
been breached.

The CTO is in crisis mode. "If one customer VM can read another customer's
memory, our entire multi-tenant infrastructure is compromised. What type of
attack is this?"

The security team debates:

"Could be a container escape..."
"Maybe it's a side-channel attack..."
"I think it's privilege escalation..."
"No, this is hypervisor breakout..."

You're asked to clarify the attack type.
                """,
                "choices": [
                    {"text": "Container escape"},
                    {"text": "VM escape / Hypervisor breakout"},
                    {"text": "Side-channel attack"},
                    {"text": "Privilege escalation"}
                ],
                "success_text": """
You confirm the attack classification. "This is VM escape, also called
hypervisor breakout. The fundamental isolation boundary between virtual
machines has been compromised."

The CTO asks for clarification. "How is this different from the other attack
types?"

"Container escape breaks out of container isolation - but containers share
the host kernel. VMs have stronger isolation through the hypervisor."

"Side-channel attacks extract information indirectly - through timing, cache
behavior, power analysis. This is DIRECT memory access across VM boundaries."

"Privilege escalation gains higher permissions within a single system. This
crosses system boundaries entirely."

"VM escape is the worst-case scenario for virtualized infrastructure. The
hypervisor is the security boundary - if code inside a VM can reach outside
it, every VM on that host is compromised. The attacker can read memory from
any VM, potentially including the hypervisor itself."

You have demonstrated understanding of VIRTUALIZATION SECURITY BREACHES.
                """,
                "failure_texts": {
                    0: """
Container escape breaks container isolation, which is weaker than VM isolation.
Containers share the host kernel; VMs have separate kernels and are isolated
by a hypervisor. The vulnerability described breaches HYPERVISOR isolation
between full VMs, not container boundaries.
                    """,
                    2: """
Side-channel attacks extract secrets through indirect observation: timing
differences, cache behavior, power consumption. The vulnerability described
allows DIRECT memory reads across VM boundaries - that's not a side channel,
it's a direct breach of the isolation boundary.
                    """,
                    3: """
Privilege escalation gains higher privileges within a SINGLE system - like
gaining root access from a regular user. This vulnerability allows reading
memory from DIFFERENT VMs - it crosses system boundaries, not permission
levels. That's VM escape, not privilege escalation.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 85,
        "hp_penalty": 30,
        "failure_text": """
VM Escape (Hypervisor Breakout) occurs when code running in a virtual machine
can break through the hypervisor's isolation to:
- Access other VMs on the same host
- Access the hypervisor itself
- Read or modify memory across VM boundaries

This differs from:
- Container escape (weaker isolation, shared kernel)
- Side-channel attacks (indirect information leakage, not direct access)
- Privilege escalation (higher privileges within the SAME system, not across VMs)

VM escape is catastrophic because it invalidates the entire isolation model.
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - Virtualization Security"
    },

    # Scenario 13: Zero Trust Principles
    {
        "id": "d3_castle_within",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE TRUST ASSUMPTION",
                "narrative": """
The Citadel's inner halls have traditionally operated on simple principles:
once someone passes the outer gates and enters the castle, they're considered
trusted and can access most areas freely.

A visiting Security Sage from distant lands shakes his head. "This is the old
way. We now know that attackers often breach outer walls and then move freely
within. Your model assumes the walls will never fail."

He proposes a new philosophy: "Never trust, always verify. Even within your
walls, every access request must prove identity and authorization. Location
within the castle should grant nothing automatically."

A knight on patrol questions this approach: "But I'm walking through the
castle right now. Surely my presence here means I'm trusted?"

Under Zero Trust principles, what should happen when the knight tries to
access the armory?
                """,
                "choices": [
                    {"text": "Grant access - he's inside the castle, so he's trusted"},
                    {"text": "Verify identity, check authorization, confirm he's a knight before granting access"},
                    {"text": "Deny access until a commander approves the request"},
                    {"text": "Grant read-only access from within the castle, full access only from the barracks"}
                ],
                "success_text": """
You explain the Zero Trust approach. "The knight's physical presence in the
castle proves nothing. An attacker who scaled the walls looks the same
from the inside."

"Under Zero Trust: every access request requires verification. The armory
door checks the knight's identity - is this actually Sir Aldric? It checks
his authorization - is Sir Aldric permitted to access the armory? It might
even check his 'device health' - is he wearing the enchanted badge that
confirms he's on active duty?"

The knight looks skeptical. "That sounds exhausting."

"It's continuous verification. Your presence inside the network - or the
castle - grants you nothing automatically. 'Trust but verify' is replaced
with 'never trust, always verify.' Every access, every time."

The Sage nods approvingly. "This way, even if an attacker breaches your walls,
they cannot simply move freely. Every door asks the same questions."

You have demonstrated understanding of ZERO TRUST ARCHITECTURE.
                """,
                "failure_texts": {
                    0: """
"Inside the castle = trusted" is exactly the assumption Zero Trust eliminates.
This perimeter-based model fails when attackers breach the perimeter (which
they inevitably do). Zero Trust says location grants nothing - every access
must be verified regardless of where the request originates.
                    """,
                    2: """
Manager approval for every access might be part of some authorization schemes,
but it's not the core Zero Trust principle. Zero Trust focuses on continuous
VERIFICATION of identity and authorization, not adding human approval steps.
The system should verify automatically, not wait for commander sign-off.
                    """,
                    3: """
Zero Trust doesn't grant different trust levels based on location. "Read-only
from here, full access from there" is still a location-based trust model.
Zero Trust eliminates location as a trust factor entirely - verification
happens the same way regardless of where you are.
                    """
                }
            },
            "corporate": {
                "title": "THE ZERO TRUST IMPLEMENTATION",
                "narrative": """
The security team is implementing Zero Trust architecture. A marketing manager
is working from her desk in the corporate headquarters and tries to access
a sensitive customer database.

The legacy system would have granted access automatically - she's on the
corporate network, behind the firewall, connected to the trusted LAN.

Under the new Zero Trust model, what should the system do?
                """,
                "choices": [
                    {"text": "Grant access automatically - she's on the trusted corporate network"},
                    {"text": "Require authentication and verify device health before granting access"},
                    {"text": "Deny access until her manager approves the specific request"},
                    {"text": "Allow read-only access from corporate network, full access from VPN only"}
                ],
                "success_text": """
You explain the Zero Trust response. "Under Zero Trust, network location is
irrelevant. Being on the corporate network grants nothing."

"The system should verify her identity - is she actually logged in as herself?
Multi-factor authentication, not just network presence. It should check her
authorization - is this role permitted to access customer data? It should
verify device posture - is her laptop compliant, patched, not compromised?"

The IT director asks: "So what's the point of our network perimeter?"

"Defense in depth - but not the only layer. Attackers inside the network
used to move freely because everything trusted the perimeter. Now, every
resource verifies every request independently. An attacker who compromises
the network still can't access resources they're not authorized for."

"'Never trust, always verify' applies even - especially - on the corporate
network. That's where lateral movement happens after a breach."

You have demonstrated understanding of ZERO TRUST ARCHITECTURE.
                """,
                "failure_texts": {
                    0: """
"Trusted corporate network" is exactly what Zero Trust eliminates. This
perimeter-based model assumes network location equals trust. Zero Trust
says: network location grants nothing. Every access must be authenticated,
authorized, and validated regardless of where it originates.
                    """,
                    2: """
Manager approval for every access isn't Zero Trust - it's just adding human
bottlenecks. Zero Trust focuses on automated, continuous verification of
identity, authorization, and device health. The system should verify these
factors automatically, not wait for human approval.
                    """,
                    3: """
Granting different access based on network location (LAN vs VPN) is still
location-based trust. Zero Trust eliminates location as a trust factor
entirely. The same verification should happen whether you're in the office,
at home on VPN, or in a coffee shop. Location is irrelevant.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 80,
        "hp_penalty": 25,
        "failure_text": """
Zero Trust Architecture core principles:

1. Never trust, always verify - no implicit trust based on location
2. Assume breach - design as if attackers are already inside
3. Verify explicitly - authenticate and authorize every access request
4. Least privilege access - grant only what's needed for each request
5. Verify device health - ensure the connecting device meets security requirements

Network location (inside/outside corporate network) grants NOTHING in Zero Trust.
Every access is verified the same way regardless of origin.
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - Zero Trust Architecture"
    },

    # Scenario 14: Trusted Computing Base
    {
        "id": "d3_core_enchantment",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE CORE ENCHANTMENT",
                "narrative": """
The Grand Architect is designing the most secure magical vault ever conceived.
She explains her philosophy: "The Core Enchantment is the magical foundation
that everything else depends on. If the Core is flawed, nothing built upon
it can be trusted."

"Therefore," she continues, "I am making the Core as SMALL as possible. Every
enchantment I exclude is one less thing that can go wrong. The Core will
contain ONLY what is absolutely essential for security."

A young apprentice challenges her: "But wouldn't a larger, more powerful Core
be more secure? More enchantments means more protection!"

The Architect asks you to explain why she's correct about minimizing the Core.

What is the PRIMARY security reason for minimizing the Trusted Computing Base?
                """,
                "choices": [
                    {"text": "Smaller systems are faster and more efficient"},
                    {"text": "Fewer enchantments mean lower licensing costs"},
                    {"text": "A smaller TCB is easier to verify, audit, and secure"},
                    {"text": "Regulations require minimal magical footprints"}
                ],
                "success_text": """
You explain the principle to the apprentice. "The Trusted Computing Base is
everything we must trust to be correct for security to work. Every component
in the TCB is a potential source of vulnerabilities."

"Consider: if the Core contains 100 enchantments, we must verify ALL 100 are
correct. Each one could hide a flaw that undermines everything. But if the
Core contains only 10 essential enchantments? We only need to verify 10."

The apprentice persists: "But more enchantments..."

"Create more places for errors. More code means more bugs. More complexity
means more unexpected interactions. The Architect is wise: security comes
from SIMPLICITY, not complexity. A small TCB can be thoroughly examined,
mathematically verified, and carefully audited. A large TCB is too complex
to fully understand."

The Architect nods. "Complexity is the enemy of security. What we don't
include can't betray us."

You have demonstrated understanding of TRUSTED COMPUTING BASE.
                """,
                "failure_texts": {
                    0: """
While smaller systems may perform better, that's not the PRIMARY security
motivation. A minimal TCB is about reducing the amount of code that must be
trusted and verified. Security, not performance, drives TCB minimization.
                    """,
                    1: """
Cost reduction is a possible side benefit, but not the security reason for
minimizing TCB. The principle is about verification and trustworthiness -
smaller systems are easier to examine for flaws, not cheaper to license.
                    """,
                    3: """
No regulation mandates a specific TCB size. Minimizing the TCB is a security
design principle, not a compliance requirement. The goal is reducing
complexity to enable thorough verification - a security benefit, not a
regulatory checkbox.
                    """
                }
            },
            "corporate": {
                "title": "THE SECURITY ARCHITECTURE DEBATE",
                "narrative": """
The security architecture team is debating the design of a new high-security
system. The lead architect argues for minimizing the Trusted Computing Base.

"I want the TCB as small as possible. Every component we add to the security-
critical foundation is another potential vulnerability."

A junior architect pushes back: "But more security features mean more
protection! Let's include everything - full antivirus, endpoint detection,
behavioral analytics, threat intelligence, the works!"

The lead architect sighs. "You're missing the point. Why do we want a
MINIMAL TCB?"
                """,
                "choices": [
                    {"text": "Smaller systems have better performance"},
                    {"text": "Fewer components mean lower licensing costs"},
                    {"text": "A smaller TCB is easier to verify, audit, and secure"},
                    {"text": "Regulatory compliance requires minimal system footprint"}
                ],
                "success_text": """
You explain the principle. "The TCB includes ALL components that must be
trusted for security to work. Every line of code in the TCB could contain
a vulnerability that undermines the entire system."

"With a small TCB, we can actually VERIFY it works correctly. We can audit
every function. We can potentially even mathematically prove certain
properties. Security researchers can examine it thoroughly."

The junior architect asks: "But don't we want all those security features?"

"Defense in depth is valuable, but the TCB itself should be minimal. The
antivirus and EDR run ON TOP of the TCB - they're applications. The TCB is
the kernel, the security reference monitor, the components that MUST be
correct or nothing works."

"Think of it this way: we can't fully verify a million lines of code.
But we might be able to verify ten thousand. A smaller TCB means higher
confidence in the components we MUST trust."

You have demonstrated understanding of TRUSTED COMPUTING BASE.
                """,
                "failure_texts": {
                    0: """
Performance benefits from a smaller system are real but secondary. The PRIMARY
security motivation for minimizing TCB is verification - smaller systems can
be more thoroughly examined, audited, and proven correct. Security, not speed,
is the driver.
                    """,
                    1: """
Licensing costs are a business concern, not a security principle. The reason
to minimize TCB is that smaller systems are easier to verify and trust.
Every line of code in the TCB is a potential vulnerability - fewer lines means
fewer potential flaws.
                    """,
                    3: """
No specific regulation mandates TCB size. Minimizing the TCB is a security
design principle based on the idea that simplicity aids security. Smaller
systems can be verified; complex systems hide vulnerabilities. This is about
security engineering, not compliance.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 85,
        "hp_penalty": 30,
        "failure_text": """
Trusted Computing Base (TCB) minimization:

The TCB includes all hardware, firmware, and software critical to security
enforcement. Everything in the TCB MUST be correct for security to work.

Why minimize the TCB?
- Smaller = easier to verify and audit
- Fewer components = fewer potential vulnerabilities
- Less complexity = fewer unexpected interactions
- Can potentially achieve formal verification for very small TCBs

"Complexity is the enemy of security" - A minimal TCB can be thoroughly
examined; a large TCB cannot be fully understood.
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - Trusted Computing Base"
    },

    # Scenario 15: Common Criteria Evaluation
    {
        "id": "d3_artifact_certification",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE CERTIFIED ARTIFACT",
                "narrative": """
The Kingdom requires a magical barrier artifact certified by the Council of
Arcane Evaluation at their fourth level of assurance - EAL4 equivalent.

A merchant presents his barrier with the certification: "Evaluated Assurance
Level 4 - Methodically Designed, Tested, and Reviewed!"

The King's advisor is uncertain what this means. "Does this guarantee the
artifact has no flaws? That the Council's master wizards tried to break it?
That it was created by pure mathematical proof?"

You are asked to explain what EAL4 certification actually indicates.
                """,
                "choices": [
                    {"text": "The artifact has no known vulnerabilities or flaws"},
                    {"text": "The artifact was methodically designed, tested, and reviewed"},
                    {"text": "The artifact passed penetration testing by kingdom hackers"},
                    {"text": "All enchantment runes were formally verified mathematically"}
                ],
                "success_text": """
You clarify the certification meaning. "EAL4 means 'Methodically Designed,
Tested, and Reviewed.' It indicates the artifact was created following
rigorous development practices with thorough documentation and independent
testing."

The advisor asks: "So it's guaranteed secure?"

"No certification guarantees zero vulnerabilities. EAL4 means the development
PROCESS was sound. Design documentation exists. The artifact was tested
against its claimed security functions. Independent evaluators reviewed the
evidence. But 'no known flaws' would require infinite testing."

"What about mathematical proof?"

"That's EAL7 - the highest level. It requires formal methods and mathematical
verification. EAL4 is the highest level typically achieved by commercial
products without specialized techniques. It indicates HIGH confidence through
rigorous process, not absolute certainty through formal proof."

You have demonstrated understanding of COMMON CRITERIA EVALUATION.
                """,
                "failure_texts": {
                    0: """
No certification level guarantees zero vulnerabilities. EAL4 indicates the
product was developed using sound methodology and tested rigorously, but
vulnerabilities may still exist. The certification is about development
PROCESS quality, not a guarantee of perfection.
                    """,
                    2: """
EAL4 involves independent testing by evaluation labs, but not specifically
"penetration testing by government hackers." The evaluation confirms the
product meets its security claims through methodical testing and review.
Penetration testing may be part of the process but isn't the defining
characteristic of EAL4.
                    """,
                    3: """
Formal mathematical verification is EAL7, not EAL4. EAL4 is "Methodically
Designed, Tested, and Reviewed" - rigorous development practices and
independent testing. EAL7 requires semiformal design and formal methods,
which is rarely achieved by commercial products.
                    """
                }
            },
            "corporate": {
                "title": "THE COMMON CRITERIA REQUIREMENT",
                "narrative": """
The government contract requires all network security products to have Common
Criteria certification at Evaluation Assurance Level 4 (EAL4).

The procurement officer is reviewing a firewall that meets this requirement
but wants clarification: "What exactly does EAL4 tell us about this product?
Does it mean it's unhackable? That the NSA tested it? That it was built using
mathematical proofs?"

You're asked to explain what EAL4 certification actually means.
                """,
                "choices": [
                    {"text": "The firewall has no known vulnerabilities"},
                    {"text": "The product was methodically designed, tested, and reviewed"},
                    {"text": "The firewall passed penetration testing by government hackers"},
                    {"text": "All source code was formally verified mathematically"}
                ],
                "success_text": """
You explain EAL4. "Evaluation Assurance Level 4 means 'Methodically Designed,
Tested, and Reviewed.' This is the highest level commonly achieved by
commercial off-the-shelf products."

"What does that mean practically?"

"The vendor followed rigorous development practices. Design documentation
was created and reviewed. Independent evaluators examined the product and
verified it meets its claimed security functions. Testing was conducted
against the security target."

The procurement officer asks: "So no bugs?"

"Not guaranteed. EAL4 indicates confidence in the development PROCESS, not
perfection in the result. Vulnerabilities may still exist. The certification
means: if there are flaws, they're not due to sloppy development. The
methodology was sound."

"What would 'no vulnerabilities' require?"

"Infinite testing. Even EAL7 - which requires formal mathematical methods -
doesn't guarantee zero bugs. But EAL4 gives us high confidence that the
product was developed and tested professionally."

You have demonstrated understanding of COMMON CRITERIA EVALUATION.
                """,
                "failure_texts": {
                    0: """
No EAL level guarantees zero vulnerabilities. EAL4 certifies that the
development process was methodical and the product was independently tested,
but bugs can still exist. The certification is about process rigor, not
a warranty of perfection.
                    """,
                    2: """
EAL4 evaluation is performed by accredited commercial testing laboratories,
not specifically by government penetration testers. The evaluation confirms
the product meets its security claims through methodical testing and
documentation review, not through adversarial hacking.
                    """,
                    3: """
Formal mathematical verification is characteristic of EAL7, the highest
level. EAL4 is "Methodically Designed, Tested, and Reviewed" - it involves
rigorous development and independent evaluation but not formal proofs.
Very few products achieve EAL7 due to the extreme effort required.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 80,
        "hp_penalty": 30,
        "failure_text": """
Common Criteria Evaluation Assurance Levels:

EAL1: Functionally Tested
EAL2: Structurally Tested
EAL3: Methodically Tested and Checked
EAL4: Methodically Designed, Tested, and Reviewed (highest for most commercial products)
EAL5: Semiformally Designed and Tested
EAL6: Semiformally Verified Design and Tested
EAL7: Formally Verified Design and Tested (requires mathematical proofs)

Key understanding: Higher EALs indicate more rigorous development and evaluation
PROCESSES, not guarantees of zero vulnerabilities.
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - Security Evaluation Criteria"
    },

    # Scenario 16: Side-Channel Attacks
    {
        "id": "d3_timing_oracle",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE TIMING ORACLE",
                "narrative": """
The Citadel's master vault uses a magical lock that requires a spoken password.
When the wrong password is spoken, the lock glows red and refuses entry.

A clever thief has discovered something peculiar: when she speaks a password
that's ALMOST correct, the lock takes slightly longer to respond than when
the password is completely wrong. By measuring these tiny timing differences
across thousands of attempts, she's reconstructing the password one rune at a time.

The Master Locksmith is horrified. "She never broke the lock! She never used
force! She simply... observed how long it took to respond?"

What type of attack is the thief using?
                """,
                "choices": [
                    {"text": "Brute force attack - trying all possible passwords"},
                    {"text": "Timing side-channel attack - extracting secrets from response timing"},
                    {"text": "SQL injection attack - manipulating the lock's internal commands"},
                    {"text": "Man-in-the-middle attack - intercepting communications"}
                ],
                "success_text": """
You identify the technique. "This is a timing side-channel attack. The thief
isn't breaking the lock's encryption or guessing passwords randomly - she's
analyzing HOW LONG the lock takes to process different inputs."

The Locksmith is fascinated and horrified. "But why would the timing vary?"

"Consider how the lock checks passwords: it compares rune by rune. If the
first rune matches, it checks the second. If it doesn't, it rejects immediately.
A password with a correct first rune takes slightly longer to reject than
one that's wrong from the start."

"By measuring thousands of attempts, the thief can determine when the first
rune is correct (slightly longer response), then work on the second rune,
and so on. She extracts the password through timing information that was
never meant to be revealed."

"The defense is to make all comparisons take EXACTLY the same time, regardless
of where they fail - constant-time comparison."

You have demonstrated understanding of SIDE-CHANNEL ATTACKS.
                """,
                "failure_texts": {
                    0: """
Brute force attacks try all possible combinations until one works. This attack
is much more sophisticated - it uses timing information to narrow down the
password intelligently. Instead of trying billions of combinations, the thief
identifies correct characters one at a time through timing analysis.
                    """,
                    2: """
SQL injection manipulates database queries through malicious input. This attack
doesn't inject commands or manipulate the lock's logic at all - it simply
observes response times and draws conclusions from those observations. The
lock functions exactly as designed; its timing leaks information.
                    """,
                    3: """
Man-in-the-middle attacks intercept communications between two parties. This
attack doesn't intercept anything - the thief interacts directly with the
lock and measures its response times. No communication channel is being
intercepted; rather, the lock's own behavior reveals secrets.
                    """
                }
            },
            "corporate": {
                "title": "THE CRYPTOGRAPHIC TIMING LEAK",
                "narrative": """
Security researchers have published a paper: by measuring precisely how long
a server takes to respond to different inputs, they can reconstruct the
server's private encryption key. The attack works because certain cryptographic
operations take slightly different amounts of time depending on the key bits
being processed.

The CEO is baffled. "They didn't hack the server? They didn't steal the key
file? They just... measured response times?"

The CISO confirms: "They sent millions of requests, recorded the response
times down to the nanosecond, and performed statistical analysis. The key
was extracted entirely from timing variations."

What type of attack is this?
                """,
                "choices": [
                    {"text": "Brute force attack"},
                    {"text": "Timing side-channel attack"},
                    {"text": "SQL injection attack"},
                    {"text": "Man-in-the-middle attack"}
                ],
                "success_text": """
You explain the attack type. "This is a timing side-channel attack - one of
several types of side-channel attacks that extract secrets through indirect
observation rather than direct access."

"The cryptographic implementation leaks information through timing. Perhaps
a modular exponentiation takes longer when a key bit is 1 versus 0. Or a
comparison branches differently based on key material. These tiny timing
differences accumulate into statistically detectable patterns."

The CEO asks: "How do we prevent this?"

"Constant-time implementations. The cryptographic code must take exactly the
same time regardless of the key value. No early exits when comparisons fail.
No data-dependent branches. Every operation completes in the same number of
cycles regardless of the secret values involved."

"This is why security-critical code is written so carefully. Not just
functionally correct, but constant-time correct. Any timing variation is
a potential information leak."

You have demonstrated understanding of SIDE-CHANNEL ATTACKS.
                """,
                "failure_texts": {
                    0: """
Brute force attacks try all possible keys until finding the correct one.
This attack is far more efficient - it uses timing information to deduce
key bits directly. Instead of 2^256 guesses, the attacker might need only
millions of measurements to extract a 256-bit key.
                    """,
                    2: """
SQL injection attacks manipulate database queries through malicious input.
This attack doesn't inject anything - it simply observes how long the server
takes to respond to normal inputs. The server functions correctly; its timing
behavior unintentionally leaks cryptographic secrets.
                    """,
                    3: """
Man-in-the-middle attacks intercept and potentially modify communications
between parties. This attack works by directly interacting with the server
and measuring response times - no interception required. The attacker learns
secrets from the server's own observable behavior.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 85,
        "hp_penalty": 30,
        "failure_text": """
Side-channel attacks extract secrets through indirect observation of system
behavior, rather than direct attack on the cryptographic algorithm:

- Timing: Measure how long operations take
- Power analysis: Monitor power consumption patterns
- Electromagnetic: Detect EM emissions during operations
- Cache: Observe cache access patterns
- Acoustic: Listen to sounds during computation

Defense: Constant-time implementations that behave identically regardless
of secret values. No data-dependent branches, comparisons, or operations.
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - Side-Channel Attacks"
    },

    # Scenario 17: IoT Security Challenges
    {
        "id": "d3_enchanted_sensors",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE ENCHANTED SENSORS",
                "narrative": """
The castle is deploying hundreds of small enchanted sensors throughout the
grounds - motion detectors, temperature monitors, door sensors. They're
marvels of efficient enchantment, requiring only the tiniest spark of
magical power.

The Security Enchanter raises concerns: "These sensors are wonderfully
efficient, but their efficiency comes at a cost. They can only hold the
simplest enchantments - no room for complex protective wards, strong
authentication spells, or self-updating capabilities."

A nobleman scoffs. "They're just sensors! What could go wrong?"

The Enchanter turns to you. "Explain the GREATEST security challenge with
these constrained magical devices."
                """,
                "choices": [
                    {"text": "They have limited resources for security controls"},
                    {"text": "They are more expensive than traditional defenses"},
                    {"text": "They cannot connect to castle communication networks"},
                    {"text": "They require wired connections to power sources"}
                ],
                "success_text": """
You explain the fundamental challenge. "These sensors have CONSTRAINED RESOURCES.
Their small size and low power consumption mean limited space for security."

"Consider what they lack: Not enough magical capacity for strong encryption
spells - they might use weak or no encryption. No room for complex authentication -
they might use default or simple credentials. No ability to update their
enchantments - vulnerabilities discovered later cannot be patched."

The nobleman persists: "But they're inside our walls!"

"That's the danger. Once on your network, a compromised sensor becomes an
attack platform. Limited resources mean limited security means easy
compromise. And because they're 'just sensors,' they're often overlooked in
security monitoring."

The Enchanter adds: "We must compensate with network segmentation, monitoring,
and accepting that these devices cannot secure themselves. Their limitations
require us to secure the ENVIRONMENT around them."

You have demonstrated understanding of IOT SECURITY CHALLENGES.
                """,
                "failure_texts": {
                    0: """
IoT devices are typically LESS expensive than traditional computing, not more.
This low cost often contributes to the security problem - manufacturers cut
corners on security to meet price points. The challenge is limited resources
for security controls, not high cost.
                    """,
                    2: """
IoT devices DO connect to networks - that's often their primary purpose.
The challenge is that they connect with limited security capabilities.
Their network connectivity combined with weak security makes them attractive
targets and potential entry points for attackers.
                    """,
                    3: """
Most IoT devices use WIRELESS connectivity, not wired. This wireless nature
actually adds to security challenges - radio communications can be intercepted,
and wireless protocols may have their own vulnerabilities. The core challenge
is limited resources for security controls.
                    """
                }
            },
            "corporate": {
                "title": "THE IOT DEPLOYMENT DEBATE",
                "narrative": """
The facilities team wants to deploy hundreds of IoT sensors throughout the
manufacturing floor - temperature monitors, equipment sensors, access trackers.
The pitch emphasizes cost savings and operational efficiency.

The security team raises objections. The CISO asks you to explain the primary
security concern.

"These devices are simple, efficient, and cheap. We're getting thousands of
data points we never had before. What's the security team so worried about?"

What is the GREATEST security challenge specific to these IoT devices?
                """,
                "choices": [
                    {"text": "IoT devices have limited resources for security controls"},
                    {"text": "IoT devices are more expensive than traditional computers"},
                    {"text": "IoT sensors cannot connect to corporate networks"},
                    {"text": "IoT devices always require wired connections"}
                ],
                "success_text": """
You explain the core challenge. "IoT devices are constrained by design.
Limited CPU, limited memory, limited power. This efficiency comes at a cost:
limited security capabilities."

"Consider what these constraints mean:
- Weak or no encryption (processing overhead too high)
- Default or simple credentials (no interface for complex passwords)
- No patching capability (limited storage, no update mechanism)
- Minimal logging (no storage for security events)
- Long lifecycles (deployed for years, never updated)"

The facilities manager asks: "But they're on a separate network..."

"Network segmentation helps but doesn't eliminate the risk. These devices are
attack surfaces - entry points that attackers love because they're overlooked.
A compromised IoT device is a beachhead for lateral movement."

"We need to treat IoT as inherently insecure and compensate with network
controls, monitoring, and assuming they WILL be compromised."

You have demonstrated understanding of IOT SECURITY CHALLENGES.
                """,
                "failure_texts": {
                    0: """
IoT devices are typically CHEAP - that's part of the problem. Manufacturers
compete on price, often cutting security features to hit price points. The
challenge is that their low cost and limited resources mean inadequate
security controls.
                    """,
                    2: """
IoT devices absolutely connect to networks - network connectivity is often
their primary purpose. The security concern is that they connect with
INADEQUATE SECURITY. Their network presence plus weak security makes them
attractive targets for attackers seeking network access.
                    """,
                    3: """
Most IoT devices use wireless connectivity - WiFi, Zigbee, Z-Wave, cellular.
Wired connections are the exception. The wireless nature adds to security
challenges but isn't the primary concern. Limited resources for implementing
security controls is the fundamental IoT security challenge.
                    """
                }
            }
        },
        "correct_index": 0,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
IoT Security Challenges stem primarily from resource constraints:

Limited Resources Lead To:
- Weak or no encryption (CPU/power overhead)
- Default or simple credentials
- No patching capability
- Minimal security logging
- Long deployment lifecycles with no updates

IoT devices are:
- Cheap (cost-cutting affects security)
- Connected (network attack surface)
- Numerous (hard to manage at scale)
- Persistent (rarely replaced)

Compensating controls: Network segmentation, traffic monitoring, assume breach.
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - IoT Security"
    },

    # Scenario 18: Secure Design Principles (Fail Secure)
    {
        "id": "d3_door_failure",
        "domain": 3,
        "themes": {
            "fantasy": {
                "title": "THE POWER FAILURE PROTOCOL",
                "narrative": """
The castle's enchanted door system requires a design decision. When the magic
fails - and someday it will - what should the doors do?

The Knight Commander argues: "All doors should remain LOCKED! If magic fails,
we must assume an attack. Protect the treasury at all costs!"

The Fire Marshall counters: "All doors should UNLOCK! People must be able to
evacuate. Life safety comes first!"

The Master Architect proposes a middle ground: "Perhaps EXTERIOR doors for
evacuation should unlock for life safety, while INTERIOR secure areas like
the treasury remain locked to protect assets?"

The King asks for your recommendation on secure door design.
                """,
                "choices": [
                    {"text": "All doors unlock to allow evacuation (all fail-safe)"},
                    {"text": "All doors remain locked to protect assets (all fail-secure)"},
                    {"text": "Exterior doors unlock for egress; interior secure areas stay locked"},
                    {"text": "The system should switch to backup power indefinitely"}
                ],
                "success_text": """
You recommend the balanced approach. "Secure design must consider BOTH life
safety AND asset protection. The answer depends on the door's PURPOSE."

"EXTERIOR doors and emergency exits must FAIL-SAFE - unlock during power loss.
People trapped inside a burning building cannot be sacrificed for security.
Life safety always takes priority over asset protection."

"INTERIOR secure areas like the treasury should FAIL-SECURE - remain locked.
People are already evacuating through exterior doors. Keeping the vault locked
prevents opportunistic theft during the chaos of an emergency."

The Knight Commander nods. "So the principle isn't all-or-nothing?"

"Correct. 'Fail-safe' and 'fail-secure' are applied appropriately based on
what each control protects. Exterior = life safety = fail-safe. Interior
high-security = asset protection = fail-secure. The design balances both
requirements."

You have demonstrated understanding of FAIL-SAFE vs FAIL-SECURE design.
                """,
                "failure_texts": {
                    0: """
Unlocking ALL doors compromises security of sensitive areas unnecessarily.
While life safety is paramount for egress points, internal high-security
areas like the treasury don't need to unlock for evacuation - people exit
through exterior doors. Fail-safe for exterior, fail-secure for interior
secure areas is the appropriate balance.
                    """,
                    1: """
Locking ALL doors creates life safety hazards. People must be able to
evacuate during emergencies. If the power fails during a fire and all doors
lock, people die. Exterior doors and emergency exits MUST fail-safe (unlock)
for egress. Only interior high-security areas should fail-secure.
                    """,
                    3: """
Backup power is a good additional control but doesn't answer the design
question. Backup power eventually fails too. The design must handle COMPLETE
power loss - and that means defining fail-safe vs fail-secure behavior for
each door type. You can't rely on backup power forever.
                    """
                }
            },
            "corporate": {
                "title": "THE ACCESS CONTROL DESIGN DECISION",
                "narrative": """
The data center is installing a new access control system. A critical design
decision: what happens when the system loses power?

The Facilities Manager wants all doors to unlock: "Fire code requires egress!"

The CISO wants all doors to remain locked: "Security must be maintained!"

A senior architect proposes: "External doors to the building should unlock
for life safety. The secure door to the server room should remain locked."

The CTO asks for your security design recommendation.
                """,
                "choices": [
                    {"text": "All doors should unlock to allow evacuation"},
                    {"text": "All doors should remain locked to protect assets"},
                    {"text": "Exterior doors unlock for egress; interior secure areas remain locked"},
                    {"text": "The system should switch to backup power indefinitely"}
                ],
                "success_text": """
You explain the balanced design. "The principle is 'fail-safe' for life
safety, 'fail-secure' for asset protection. Apply each where appropriate."

"EXTERIOR doors and emergency exits must FAIL-SAFE. Fire code requires it,
and more importantly, human life requires it. You cannot trap people inside
a building during an emergency. These doors unlock when power fails."

"INTERIOR high-security areas like the server room should FAIL-SECURE. People
evacuate through exterior doors, so the server room staying locked doesn't
trap anyone - but it DOES prevent opportunistic access during the confusion
of an emergency."

The CISO asks: "So we get both life safety AND security?"

"Exactly. The design applies the right principle to each door based on its
purpose. Life safety doors unlock. Asset protection doors lock. This is
why access control design considers door PURPOSE, not just a global policy."

You have demonstrated understanding of FAIL-SAFE vs FAIL-SECURE design.
                """,
                "failure_texts": {
                    0: """
Unlocking all doors, including the server room, creates unnecessary security
risk. People evacuate through exterior doors - the server room doesn't need
to unlock for egress. Keeping it locked during emergencies prevents
opportunistic theft when attention is elsewhere. Apply fail-safe only where
life safety requires it.
                    """,
                    1: """
Locking all doors, including exterior exits, violates fire code and
endangers lives. If power fails during a fire, people die. Life safety
MUST take priority for egress points. Exterior doors and emergency exits
must fail-safe (unlock) while only interior high-security areas fail-secure.
                    """,
                    3: """
Backup power provides additional resilience but doesn't answer the design
question. All backup power eventually fails - batteries deplete, generators
run out of fuel. The system MUST define behavior for complete power loss.
Fail-safe exterior, fail-secure interior is the appropriate design.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 80,
        "hp_penalty": 25,
        "failure_text": """
Secure Design Principles - Fail-Safe vs Fail-Secure:

FAIL-SAFE: System fails to a safe state (usually OPEN)
- Applied to: Life safety systems, emergency exits, fire doors
- Rationale: Human life must never be endangered by security controls

FAIL-SECURE: System fails to a secure state (usually LOCKED)
- Applied to: Asset protection systems, vault doors, server rooms
- Rationale: Security is maintained even during system failures

Best Practice: Apply both principles appropriately:
- Exterior doors / emergency exits: FAIL-SAFE (life safety)
- Interior high-security areas: FAIL-SECURE (asset protection)
        """,
        "domain_reference": "Domain 3: Security Architecture and Engineering - Secure Design Principles"
    },
]
