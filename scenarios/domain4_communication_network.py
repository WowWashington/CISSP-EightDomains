"""
Domain 4: Communication and Network Security scenarios.

Key CISSP concepts tested:
- OSI Model and TCP/IP
- Network Segmentation
- Firewalls and VPNs
- Wireless Security
- Network Attacks and Defenses
- IDS/IPS Systems
- Secure Protocols

Each scenario supports dual themes:
- Fantasy: Medieval/magical Citadel setting
- Corporate: Modern office satire (Office Space style)
"""

DOMAIN_4_SCENARIOS = [
    # Scenario 1: OSI Model Layers
    {
        "id": "d4_osi_layers",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE CRYSTAL MESSENGER'S DILEMMA",
                "narrative": """
The Arcane Communications Tower crackles with frustrated energy. A crystal
messenger sprite reports that enchanted scrolls are reaching their destinations,
but the words upon them are scrambled into nonsense.

"Most peculiar," mutters the Tower Keeper. "I can trace the magical pathways
perfectly - the scroll reaches the correct tower. The magical seals verify
the scroll is intact. Yet the message translation spell fails completely."

You examine the communication channels. The physical crystal links glow
strong and steady. The magical routing sigils correctly direct each scroll.
The transport enchantments confirm delivery and receipt.

"It seems the lower layers of our magical network function perfectly," you
observe. "The crystals connect, the routes work, the deliveries confirm..."

The Keeper nods grimly. "Yet the Name-to-Tower translation spell - converting
friendly names like 'Archmage Theron' to actual tower coordinates - fails
entirely. At which layer of our communication magic does the problem lie?"

What layer of the magical network is failing?
                """,
                "choices": [
                    {"text": "The Crystal Layer - the physical connections must be subtly damaged"},
                    {"text": "The Routing Layer - the magical pathways are misdirecting scrolls"},
                    {"text": "The Transport Layer - delivery confirmations are being forged"},
                    {"text": "The Application Layer - the name translation spell operates at the highest level"}
                ],
                "success_text": """
"Of course!" The Tower Keeper's eyes widen with understanding. "The
Name-to-Tower translation is an application-level service, like our
DNS - Domain Name Sorcery!"

You nod approvingly. "The physical crystals work, the routing functions,
the transport confirms delivery. All lower layers are operational. It is
only the highest layer - where names become addresses - that fails."

The Keeper immediately dispatches a repair sprite to the Name Translation
Sanctuary. Within the hour, scrolls flow freely once more.

"You have taught me to troubleshoot systematically," the Keeper says
gratefully. "When lower layers function, look to the highest layers for
the fault."

You have demonstrated understanding of the OSI MODEL LAYERS.
                """,
                "failure_texts": {
                    0: """
Physical layer issues would prevent all communication entirely - not even
basic connectivity would work. Since the scrolls physically reach their
destinations (proven by IP-equivalent crystal tracing), the physical
layer is functioning perfectly. DNS/name resolution operates at Layer 7,
the Application layer.
                    """,
                    1: """
The routing layer (Network layer) handles addressing and path selection.
Since scrolls reach the correct destination tower when addressed by
coordinates (like an IP address), routing works correctly. The problem
is translating friendly names to addresses - a Layer 7 function.
                    """,
                    2: """
The Transport layer handles reliable delivery and session management.
Since delivery confirmations work properly, this layer is functional.
DNS name resolution - converting hostnames to IP addresses - is an
Application layer (Layer 7) service.
                    """
                }
            },
            "corporate": {
                "title": "THE HELPDESK MYSTERY",
                "narrative": """
The helpdesk phone hasn't stopped ringing all morning. Every caller has
the same complaint: they can't reach the company's internal wiki.

You start troubleshooting methodically. "Can you ping 10.0.50.25?"

"Yes, that works fine."

"Okay, now try ping wiki.internal.corp"

"Hmm... 'could not resolve hostname.' What does that mean?"

You run some tests yourself. The network cables are fine. The switches
show green lights. Traceroute to the wiki server's IP address works
perfectly. The server itself responds to direct IP connections.

But anything requiring a hostname lookup fails completely. Someone
mumbles something about the new IT guy "cleaning up" the server room
yesterday and accidentally unplugging something he thought was unused.

Your manager appears, looking stressed. "The CTO is asking which OSI
layer is affected. She needs it for the incident report. Yesterday."

At which OSI layer is this problem occurring?
                """,
                "choices": [
                    {"text": "Layer 1 - Physical: probably a loose cable somewhere"},
                    {"text": "Layer 3 - Network: the IP routing must be broken"},
                    {"text": "Layer 4 - Transport: TCP connections are failing"},
                    {"text": "Layer 7 - Application: DNS resolution is an application-layer service"}
                ],
                "success_text": """
You pull up the incident report template. "It's Layer 7 - Application
layer. DNS resolution is an application-layer protocol."

"But wait," your manager protests, "DNS seems so fundamental..."

"It is fundamental, but it's still an application service. Here's the
proof: Layer 1-3 are working because we can ping by IP address. Layer 4
is working because TCP connections succeed. The only thing broken is
the DNS lookup, which translates hostnames to IP addresses at Layer 7."

The new IT guy sheepishly admits he unplugged the DNS server thinking
it was "some old forgotten box." The server is plugged back in, and
within minutes, the helpdesk phones go quiet.

"Put 'DNS server temporarily offline - Application Layer' in the report,"
you tell your manager. "And maybe put labels on the critical servers."

You have demonstrated understanding of the OSI MODEL LAYERS.
                """,
                "failure_texts": {
                    0: """
If the Physical layer were damaged, ping by IP address would also fail.
Since IP connectivity works perfectly, all physical connections are
functional. DNS operates at Layer 7 (Application), not Layer 1.
                    """,
                    1: """
The Network layer handles IP addressing and routing. Since ping to the
server's IP address works, routing is functioning correctly. DNS
translates hostnames to IP addresses and operates at Layer 7, not
Layer 3.
                    """,
                    2: """
The Transport layer (TCP/UDP) handles connection establishment and
reliability. Since TCP connections to IP addresses work, Layer 4 is
fine. DNS is an application-layer protocol that uses UDP (port 53)
but is itself a Layer 7 service.
                    """
                }
            }
        },
        "correct_index": 3,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
The OSI model has 7 layers. DNS resolution operates at Layer 7 (Application).
When troubleshooting, if lower layers work (ping by IP succeeds), the
problem is at a higher layer. DNS translates human-friendly names to
IP addresses - an application-layer service.
        """,
        "domain_reference": "Domain 4: Communication and Network Security - OSI Model"
    },

    # Scenario 2: Network Segmentation
    {
        "id": "d4_network_segmentation",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE PLAGUE OF CORRUPTED SCROLLS",
                "narrative": """
Disaster has struck the Citadel's archive network. A cursed scroll, opened
by a careless apprentice in the Accounting Scriptorium, has spread its
corruption throughout the entire network. Ancient texts in the Research
Sanctum - irreplaceable magical formulas - now writhe with the same
dark enchantment.

The Grand Archivist is beside himself. "How could corruption spread from
mere ledger-keepers to our most sacred research chambers? They have nothing
in common!"

You investigate and find the terrible truth: all Scriptoriums share the
same magical messaging network with no barriers between them. A corruption
in one chamber flows freely to all others.

"This must never happen again," the Archivist declares. "What protection
would BEST prevent such lateral spreading of magical corruption in the
future?"

How do you advise the Grand Archivist?
                """,
                "choices": [
                    {"text": "Install more powerful cleansing wards on all scrolls throughout the network"},
                    {"text": "Divide the network into separate segments with warded barriers between each"},
                    {"text": "Require stronger authentication passwords for all scribes"},
                    {"text": "Encrypt all scroll messages so corruption cannot read them"}
                ],
                "success_text": """
"We must segment the network," you explain, conjuring an illusion of the
new architecture. "The Accounting Scriptorium becomes its own isolated
realm. Research another. Each segment protected by warded barriers that
control exactly what messages may pass between them."

The Archivist studies the design. "So if corruption strikes Accounting..."

"It remains contained. The barriers - like magical firewalls - block any
unauthorized spread. Research receives only pre-approved message types
from Accounting, nothing more."

"But won't this slow our work?"

"Slightly. But the alternative is losing everything when one apprentice
opens the wrong scroll. Defense in depth requires accepting some friction
for much greater protection."

The segmentation project begins immediately. Future incidents remain
isolated to their origin chambers.

You have demonstrated proper NETWORK SEGMENTATION principles.
                """,
                "failure_texts": {
                    0: """
Cleansing wards (antivirus) may detect known corruptions, but they cannot
stop determined dark magic from spreading once it has a foothold. They
also cannot prevent zero-day curses. Segmentation physically prevents
lateral movement - even if corruption evades detection, it cannot cross
warded barriers to other segments.
                    """,
                    2: """
Stronger passwords protect against unauthorized access, but this corruption
spread through the legitimate network connections between chambers. Once
malware is inside a system, authentication doesn't prevent it from moving
to connected systems. Segmentation limits what systems CAN connect.
                    """,
                    3: """
Encryption protects message confidentiality but doesn't prevent malware
spread. Corrupted data can be encrypted just as easily as clean data.
The corruption doesn't need to read messages - it just uses the network
paths to spread. Segmentation blocks those paths entirely.
                    """
                }
            },
            "corporate": {
                "title": "THE RANSOMWARE RETROSPECTIVE",
                "narrative": """
The incident response team sits in grim silence. Last week's ransomware
attack started when someone in Accounting opened a malicious email
attachment. Within four hours, it had encrypted the R&D servers, the
HR database, the CEO's laptop, and half of production.

The CISO rubs her temples. "I don't understand. These departments have
nothing to do with each other. How did malware from Karen's desktop in
Accounting end up encrypting prototype designs in R&D?"

You pull up the network diagram. It's a flat network - one giant subnet
with no internal barriers. Any device can reach any other device. The
malware simply walked from system to system through open network paths.

"Well," the CISO says, "we're rebuilding from backups anyway. What
single control would BEST prevent this lateral movement in our new
network design?"

What do you recommend?
                """,
                "choices": [
                    {"text": "Deploy better antivirus on all endpoints - catch malware before it spreads"},
                    {"text": "Implement network segmentation with firewall rules between departments"},
                    {"text": "Require 20-character passwords for all users"},
                    {"text": "Encrypt all internal network traffic with VPN"}
                ],
                "success_text": """
You sketch out the new design on the whiteboard. "We segment. Accounting
gets its own VLAN. R&D gets another. HR, Production, Management - each
in isolated network segments with firewalls controlling traffic between
them."

"Won't that be complicated?" someone asks.

"Yes. But here's the thing: even if Karen clicks another phishing email
next year - and she will - the malware gets trapped in the Accounting
segment. The firewall blocks it from reaching R&D because there's no
legitimate reason for Karen's desktop to connect to R&D servers."

The CISO nods slowly. "So we limit the blast radius."

"Exactly. Antivirus might miss the malware. Passwords don't stop it once
it's running. But segmentation physically prevents it from reaching what
it can't legitimately access."

The network redesign project gets immediate budget approval.

You have demonstrated proper NETWORK SEGMENTATION principles.
                """,
                "failure_texts": {
                    0: """
Antivirus is important but imperfect - it missed this malware the first
time. Zero-day threats evade signature detection. Segmentation provides
defense in depth: even if AV fails, the malware can't traverse firewalled
boundaries between segments. Don't rely on a single control.
                    """,
                    2: """
Strong passwords prevent unauthorized login, but the ransomware didn't
need passwords - it spread through network vulnerabilities and open
connections between systems. Once malware is executing, password strength
is irrelevant. Segmentation blocks the network paths malware uses.
                    """,
                    3: """
VPN encrypts traffic, but encryption doesn't block malicious traffic -
it just makes it confidential. Encrypted malware communication is still
malware communication. Segmentation controls WHICH systems can talk to
which, not just whether the conversation is encrypted.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Network segmentation divides networks into isolated zones with controlled
access between them. It limits lateral movement - even if one segment is
compromised, firewalls prevent attackers from reaching other segments.
This is fundamental defense in depth for network security.
        """,
        "domain_reference": "Domain 4: Communication and Network Security - Network Segmentation"
    },

    # Scenario 3: Stateful Firewall
    {
        "id": "d4_stateful_firewall",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE PHANTOM REPLY SCROLLS",
                "narrative": """
The Border Sentinel reports a disturbing pattern. Strange scrolls are
appearing at the Citadel gates, claiming to be replies to messages the
Citadel never sent. They bear all the correct magical seals and routing
marks of legitimate responses.

"Our scouts never sent inquiries to these foreign towers," the Sentinel
Commander explains. "Yet these 'reply' scrolls arrive constantly, each
claiming to answer questions we never asked. Some contain hidden curses
that activate upon reading."

You examine the gates' defenses. The current barrier enchantment examines
each scroll individually, checking only its current form and destination.
It has no memory of past communications.

"The attackers exploit this ignorance," you realize. "They send forged
replies to conversations that never existed. Our stateless barrier cannot
know the difference."

The Commander grips his sword hilt. "What manner of defense would
recognize these phantom replies for the deceptions they are?"

What type of firewall defense do you recommend?
                """,
                "choices": [
                    {"text": "A simple packet-checking barrier that examines each scroll independently"},
                    {"text": "A connection-tracking barrier that remembers all outgoing messages and validates replies"},
                    {"text": "A web-specific barrier designed for HTTP messages only"},
                    {"text": "A session-layer gateway that validates scroll formatting"}
                ],
                "success_text": """
"You need a stateful barrier," you explain. "One that maintains a ledger
of all legitimate conversations - every message sent outward, awaiting
its proper reply."

You demonstrate the concept with an illusion. "When a scout sends an
inquiry, the barrier records: 'Message to Tower Valdris, expecting reply.'
When a scroll arrives claiming to be that reply, the barrier checks its
ledger. If no matching outgoing message exists..."

"The reply is a phantom! A forgery!" The Commander's eyes light up.

"Precisely. Stateless barriers are blind to conversation context. They
see each scroll in isolation. Stateful barriers understand that replies
must match requests. No request means no legitimate reply can exist."

The enchantment is upgraded within the week. The phantom reply attacks
cease entirely - the attackers cannot forge what the barrier validates.

You have demonstrated understanding of STATEFUL INSPECTION FIREWALLS.
                """,
                "failure_texts": {
                    0: """
A stateless packet-checking barrier is exactly the problem! It examines
each packet/scroll independently without remembering previous traffic.
It cannot detect that a "reply" has no corresponding "request." You need
stateful inspection that tracks connection state.
                    """,
                    2: """
Web Application Firewalls (WAFs) specialize in HTTP/HTTPS traffic and
application-layer attacks like SQL injection. They don't address the
fundamental issue of forged TCP connection responses. Stateful inspection
tracks all connection types, not just web traffic.
                    """,
                    3: """
Session-layer gateways work at OSI Layer 5 and handle session establishment.
While they have some awareness of connections, stateful inspection firewalls
specifically maintain connection state tables to track TCP/UDP conversations
and validate that responses match legitimate outbound requests.
                    """
                }
            },
            "corporate": {
                "title": "THE UNSOLICITED RESPONSES",
                "narrative": """
The security monitoring console keeps flagging suspicious traffic. Packets
are arriving from external addresses, all formatted as TCP response packets
with the ACK flag set - as if responding to connections your network
initiated. But your logs show no corresponding outbound connections.

"It's a classic TCP session hijacking attempt," you explain to the junior
analyst. "Attackers send packets that look like they're part of existing
conversations. If our firewall is stateless, it might let them through."

The analyst frowns. "But these packets have proper headers, correct ports,
valid checksums..."

"All of which a stateless firewall would accept. It only examines each
packet individually. It doesn't know whether there's actually a
conversation happening."

Your manager walks over. "The board is asking what type of firewall
we need to prevent these attacks. They want it in writing."

What type of firewall should you recommend?
                """,
                "choices": [
                    {"text": "Packet filtering firewall - it can examine packet headers"},
                    {"text": "Stateful inspection firewall - it tracks connection state"},
                    {"text": "Web application firewall - it understands HTTP"},
                    {"text": "Circuit-level gateway - it validates session establishment"}
                ],
                "success_text": """
You type up the recommendation: "We need a stateful inspection firewall."

"Here's why," you explain to your manager. "Stateful firewalls maintain
a connection state table. When our network initiates a connection to
google.com, the firewall notes: 'Connection from 10.0.1.15:52344 to
142.250.80.46:443 - expecting responses.'

"When packets arrive claiming to be responses, the stateful firewall
checks its table. If there's a matching outbound connection, the reply
is legitimate. If not - if we never made that request - the packet is
dropped as unauthorized."

"And packet filters can't do this?"

"Packet filters examine each packet in isolation. They might see a
properly-formatted response packet and say 'looks fine, come on in.'
They have no memory, no context. Stateful firewalls remember."

The recommendation is approved and the attack traffic stops getting
through entirely.

You have demonstrated understanding of STATEFUL INSPECTION FIREWALLS.
                """,
                "failure_texts": {
                    0: """
Packet filtering firewalls (stateless) are exactly what the attackers
are exploiting. They examine individual packets without connection context.
They cannot determine that a "response" has no legitimate "request."
Stateful inspection maintains connection tables to track this.
                    """,
                    2: """
WAFs protect web applications from HTTP-layer attacks like XSS, SQL
injection, and similar. They don't address TCP-level session manipulation.
The attack described operates at the network/transport layer, requiring
stateful connection tracking, not application inspection.
                    """,
                    3: """
Circuit-level gateways work at the session layer and can validate that
handshakes complete properly. However, stateful inspection firewalls
provide more comprehensive connection tracking, maintaining full state
tables for all TCP/UDP conversations and validating that responses
match recorded requests.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Stateful firewalls maintain connection state tables, tracking all active
sessions. They can detect packets claiming to be part of connections that
were never established. Stateless packet filters examine each packet
independently and cannot detect this type of attack.
        """,
        "domain_reference": "Domain 4: Communication and Network Security - Firewall Technologies"
    },

    # Scenario 4: VPN Technologies
    {
        "id": "d4_vpn_technologies",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE WANDERING SCHOLARS",
                "narrative": """
The Citadel's traveling scholars face a dilemma. They journey to distant
lands, staying in foreign inns and markets, yet must consult the Citadel's
protected archives remotely. The public message crystals in these places
are notoriously untrustworthy - any eavesdropper can intercept the magic.

"We cannot install special enchanted crystals in every inn across the
realm," the Head Scholar sighs. "Our people carry only basic communication
orbs - the kind any merchant uses."

"Yet they must access restricted archives through these untrusted
channels?" you ask.

"Precisely. The foreign inns often block unusual magical protocols -
they only permit the most basic message-scrying. Our scholars need
something that works everywhere, using only the tools they already
carry."

The Head Scholar spreads her hands. "What approach would allow our
scholars secure access to the archives from any location, using only
standard equipment that won't be blocked by suspicious innkeepers?"

What VPN approach do you recommend?
                """,
                "choices": [
                    {"text": "IPSec tunnel magic - powerful but requires special crystals"},
                    {"text": "SSL/TLS browser-based access - works through any standard scrying orb"},
                    {"text": "PPTP enchantment - old magic that most barriers recognize and block"},
                    {"text": "L2TP without encryption - fast but offers no protection from eavesdroppers"}
                ],
                "success_text": """
"SSL/TLS scrying is your answer," you declare. "It works through any
standard communication orb - no special equipment needed. The magic
travels on the same channels that merchants use for trade, so suspicious
innkeepers have no reason to block it."

"But is it secure enough for archive access?"

"Absolutely. SSL/TLS creates an encrypted tunnel that protects all
communication. The foreign inn sees only ordinary-looking traffic.
Inside that tunnel, your scholars access archives as if they were
within the Citadel itself."

"And our people need no special training?"

"If they can use a standard scrying orb for basic message-reading, they
can use SSL/TLS access. The complexity is hidden behind simplicity."

The Head Scholar smiles with relief. "Finally, a solution that works in
the real world, not just in theoretical enchantment manuals."

You have demonstrated understanding of VPN TECHNOLOGIES.
                """,
                "failure_texts": {
                    0: """
IPSec provides excellent security but typically requires dedicated client
software and uses protocols (ESP, AH) that are often blocked by firewalls.
Hotel and cafe networks frequently block non-standard protocols. SSL/TLS
VPNs use HTTPS (port 443), which is almost never blocked.
                    """,
                    2: """
PPTP is an obsolete protocol with known security vulnerabilities. Many
networks block it entirely. Modern security requirements demand current
protocols. SSL/TLS VPNs are widely supported and use standard HTTPS
channels that aren't blocked.
                    """,
                    3: """
L2TP without encryption provides NO confidentiality - all traffic would
be visible to anyone on the untrusted network. This defeats the entire
purpose of VPN access from hostile environments. SSL/TLS VPNs provide
both the accessibility and the encryption required.
                    """
                }
            },
            "corporate": {
                "title": "THE REMOTE WORK REALITY",
                "narrative": """
The pandemic changed everything. Now half your employees work from home,
coffee shops, hotel business centers, or wherever they happen to be.
They all need access to internal resources - file shares, internal apps,
development environments.

The old IPSec VPN worked fine when everyone was at home, but complaints
flood in from traveling employees. "The hotel wifi blocks it." "The
coffee shop firewall kills my connection." "I had to use my phone's
hotspot because nothing else worked."

The CTO calls an emergency meeting. "We need VPN access that works from
anywhere - hotels, airports, conference centers, wherever. Our people
can't always install special client software - sometimes they're on
borrowed laptops or public kiosks. What's our solution?"

What VPN approach do you recommend?
                """,
                "choices": [
                    {"text": "Stick with IPSec tunnel mode - tell users to work around firewall blocks"},
                    {"text": "Deploy SSL/TLS VPN with browser-based access"},
                    {"text": "Use PPTP - it's simpler and faster to deploy"},
                    {"text": "Implement L2TP without encryption for maximum compatibility"}
                ],
                "success_text": """
"SSL/TLS VPN with browser access," you recommend. "Here's why it solves
all our problems:

"First, it works through web browsers - no client software installation
required. Users on borrowed laptops can still connect.

"Second, it uses HTTPS on port 443. That's the same port as every
secure website. No hotel or coffee shop blocks port 443 because it
would break the entire internet for their customers.

"Third, it provides full encryption. Unlike some of the... alternatives...
we've considered."

The CTO nods. "What about our power users who need full tunnel access?"

"The browser provides access to specific resources. For power users,
we offer the full SSL VPN client - it's still more compatible than
IPSec because it tunnels through HTTPS."

Within a month, the helpdesk tickets about VPN connectivity drop by 90%.

You have demonstrated understanding of VPN TECHNOLOGIES.
                """,
                "failure_texts": {
                    0: """
"Work around firewall blocks" is not a scalable solution. Users can't
control hotel or conference center firewalls. IPSec uses protocols
(ESP, AH) and ports that are frequently blocked. SSL/TLS VPNs use
standard HTTPS traffic that networks cannot block without breaking
all secure web browsing.
                    """,
                    2: """
PPTP is a legacy protocol with well-documented security vulnerabilities.
It's been deprecated by Microsoft and is blocked by many enterprise
networks. Using PPTP would be a step backward in security and wouldn't
solve the compatibility issues. SSL/TLS is the modern standard.
                    """,
                    3: """
L2TP without encryption means all traffic is visible to anyone on the
network - exactly what a VPN is supposed to prevent. Users connecting
from hostile networks (coffee shops, hotels) would have zero protection.
This is worse than no VPN because it provides false confidence.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
SSL/TLS VPNs work through standard web browsers using HTTPS (port 443),
which is almost never blocked by firewalls. They don't require special
client software for basic access. This makes them ideal for users
connecting from diverse, uncontrolled network environments.
        """,
        "domain_reference": "Domain 4: Communication and Network Security - VPN Technologies"
    },

    # Scenario 5: Wireless Security (Evil Twin)
    {
        "id": "d4_wireless_evil_twin",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE PHANTOM BEACON",
                "narrative": """
Guards rush to the Citadel with alarming news. Apprentices returning from
the Eastern Market report that their communication crystals automatically
linked to what they believed was the Citadel's message network - but
something was wrong. The signal came from a wagon in the market square,
not the Citadel's towers.

"They said it looked exactly like our network beacon," a guard explains.
"Same name, same appearance. Their crystals connected without asking.
Then all their messages - passwords, secrets, everything - flowed through
this impostor's wagon."

You examine one of the affected crystals. It's configured to automatically
connect to any beacon broadcasting the Citadel's network name. There's
no verification that the beacon is genuine.

"The villain created a perfect duplicate of our signal," you realize.
"Crystals cannot tell the fake from the real thing by name alone."

The Guard Captain demands answers. "What manner of attack is this? I
must report to the Council."

What type of attack was this?
                """,
                "choices": [
                    {"text": "Crystal signature forgery - the attacker cloned device identities"},
                    {"text": "Evil twin attack - a rogue beacon mimicking the legitimate network"},
                    {"text": "Bluetooth hijacking - the attacker intercepted short-range signals"},
                    {"text": "Setup code attack - the attacker cracked the network's protection"}
                ],
                "success_text": """
"This is an evil twin attack," you explain to the Council. "The attacker
created a rogue access point - a fake beacon - broadcasting the same
network name as our legitimate signal. Because our network name isn't
secret and crystals auto-connect to familiar names..."

"The crystals had no way to know which beacon was real," the Archmage
finishes grimly.

"Precisely. The evil twin often has a stronger signal - being physically
closer in the market - so crystals prefer it over our distant towers.
All traffic then routes through the attacker, who can capture credentials,
modify messages, or inject malicious content."

"What defenses exist?"

"Users must verify they're connected to legitimate networks before
transmitting sensitive data. Certificate-based authentication helps
crystals recognize genuine beacons. And we should warn everyone about
the dangers of auto-connecting to familiar network names."

You have demonstrated understanding of WIRELESS SECURITY attacks.
                """,
                "failure_texts": {
                    0: """
MAC spoofing changes a device's hardware address to impersonate another
device. While related to network attacks, the scenario specifically
describes a fake access point mimicking a legitimate network name -
that's an evil twin attack, not MAC spoofing.
                    """,
                    2: """
Bluetooth hijacking targets Bluetooth connections, which operate
differently from WiFi networks. This attack involved WiFi - devices
connecting to a fake access point with a matching network name. That's
specifically an evil twin (rogue access point) attack.
                    """,
                    3: """
WPS PIN attacks target the WiFi Protected Setup feature to crack a
network's password. This attack didn't crack the legitimate network -
it created a completely separate fake network with the same name. The
evil twin captures traffic from deceived users.
                    """
                }
            },
            "corporate": {
                "title": "THE PARKING LOT PROBLEM",
                "narrative": """
Three employees from the Legal department report something strange.
Yesterday morning, while sitting in the parking lot before work, their
laptops connected to "CorpWiFi-5G" - the company's wireless network.
They answered some emails, logged into a few internal systems...

Then they walked inside and discovered they were still 50 feet from
the building. The network name was right, but they'd been connected
to... something else. Something in a white van parked near the entrance.

The security team reviews the laptop logs. All three devices auto-
connected to a network broadcasting your company's exact SSID. But the
access point wasn't yours. It was a portable hotspot in that van,
which drove away an hour later.

Legal is furious. The CISO needs answers for the board.

What type of attack was this?
                """,
                "choices": [
                    {"text": "MAC spoofing attack - the attacker cloned legitimate device addresses"},
                    {"text": "Evil twin / Rogue access point attack"},
                    {"text": "Bluetooth hijacking attack"},
                    {"text": "WPS PIN attack to crack the network password"}
                ],
                "success_text": """
"This was an evil twin attack," you explain to the CISO. "Also called
a rogue access point. The attacker set up their own WiFi hotspot and
named it 'CorpWiFi-5G' - identical to our legitimate network."

"But how did the laptops connect to it?"

"Because they're configured to auto-connect to known networks by name.
When they saw 'CorpWiFi-5G,' they connected automatically - no user
interaction needed. The evil twin had a stronger signal in the parking
lot than our actual network inside the building."

"So everything they did..."

"Went through the attacker's device. Login credentials, email content,
internal system access - all potentially captured."

The CISO sighs. "What do we do?"

"Disable auto-connect on managed devices. Implement 802.1X authentication
so devices verify the network is genuine. Train users to verify connections
before entering credentials. And sweep for rogue access points regularly."

You have demonstrated understanding of WIRELESS SECURITY attacks.
                """,
                "failure_texts": {
                    0: """
MAC spoofing involves changing a device's MAC address to bypass access
controls or impersonate another device. This attack created a completely
fake access point with a matching SSID - that's an evil twin attack,
which tricks devices into connecting to a malicious network.
                    """,
                    2: """
Bluetooth hijacking attacks Bluetooth connections, not WiFi networks.
This attack targeted WiFi - the laptops connected to a fake WiFi
access point broadcasting the company's SSID. That's specifically
an evil twin (rogue access point) attack.
                    """,
                    3: """
WPS attacks attempt to crack the legitimate network's password by
exploiting weaknesses in WiFi Protected Setup. This attacker didn't
crack your network - they created their own fake network with an
identical name. Evil twin attacks capture traffic from deceived
users, not crack passwords.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
An evil twin attack creates a fake access point with the same SSID as
a legitimate network. Devices configured to auto-connect will join the
malicious AP, allowing attackers to intercept traffic, steal credentials,
or launch further attacks. Defense includes 802.1X authentication and
disabling auto-connect features.
        """,
        "domain_reference": "Domain 4: Communication and Network Security - Wireless Security"
    },

    # Scenario 6: DNS Security
    {
        "id": "d4_dns_security",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE MISDIRECTED PILGRIMS",
                "narrative": """
Pilgrims seeking the Sacred Treasury have been arriving at a dark temple
instead. They asked their guide-crystals for directions to "Sacred Treasury"
and followed faithfully - yet ended up at an impostor site designed to
steal their offerings and secrets.

The Name Keepers investigate and discover corruption in the Direction
Oracle - the magical system that translates destination names into actual
locations. Someone has poisoned its knowledge, replacing the true path
to the Sacred Treasury with directions to the dark temple.

"When pilgrims ask for 'Sacred Treasury,' the Oracle gives them the wrong
location," a Name Keeper explains. "The dark temple is a perfect replica
- visitors don't realize they're in the wrong place until it's too late."

"Can we simply correct the Oracle's records?"

"We've tried. But the poisoner keeps re-corrupting them. We need a way
to verify that direction answers are authentic and haven't been tampered
with."

What security measure would BEST prevent this attack?
                """,
                "choices": [
                    {"text": "Install protective wards at the Sacred Treasury entrance"},
                    {"text": "Implement signed directions that prove authenticity through cryptographic seals"},
                    {"text": "Add guardians to inspect travelers before entering destinations"},
                    {"text": "Filter which pilgrims can access the naming service"}
                ],
                "success_text": """
"We need cryptographically signed directions," you declare. "When the
Oracle provides a path, it must bear an unforgeable seal proving the
answer is authentic and unchanged."

"How would this work?"

"The legitimate Name Keepers hold secret signing keys. Every direction
they issue is sealed with their unique signature. Pilgrims' guide-crystals
verify the seal before following directions. Unsigned or incorrectly
signed directions are rejected."

"But the dark temple operators could create their own seals..."

"Not ones that match the legitimate signers. Without the secret keys,
any forgery is detectable. This is called DNSSEC in the mortal realm -
DNS Security Extensions. It cryptographically protects the integrity
of name resolution."

"Even if the Oracle is poisoned, the false directions won't have valid
signatures!" The Name Keeper's face lights up with understanding.

You have demonstrated understanding of DNS SECURITY.
                """,
                "failure_texts": {
                    0: """
SSL certificates on the destination server authenticate the server
itself, but that doesn't help if pilgrims are directed to the wrong
location in the first place. They'd arrive at the dark temple, which
could have its own certificates. DNSSEC prevents the misdirection
before it happens.
                    """,
                    2: """
Web Application Firewalls protect web applications from attacks like
SQL injection. They don't address DNS poisoning, which happens before
users ever reach the web server. The problem is in the name resolution
system, requiring DNS-level protection like DNSSEC.
                    """,
                    3: """
MAC filtering controls which devices can access a network based on
hardware addresses. It has nothing to do with DNS resolution or
preventing cache poisoning attacks. DNSSEC cryptographically validates
DNS responses to prevent exactly this type of attack.
                    """
                }
            },
            "corporate": {
                "title": "THE BANKING REDIRECT",
                "narrative": """
Users are calling in a panic. They typed "bankofamerica.com" in their
browsers, hit enter, and landed on a site that looked exactly like
Bank of America - but wasn't. Login credentials entered on this fake
site went straight to attackers.

Your team investigates and finds the horrifying truth: someone has
poisoned your DNS server's cache. When users request the IP address
for the bank's website, your DNS server returns an attacker-controlled
IP instead of the legitimate one.

"But they typed the correct URL!" your manager protests.

"The URL doesn't matter if DNS gives them the wrong IP address. They
get redirected before they know anything's wrong."

"The bank's website has SSL certificates..."

"Which only proves they reached the server the DNS sent them to. If
DNS is compromised, they never reach the real bank in the first place."

What security measure would BEST prevent this attack?
                """,
                "choices": [
                    {"text": "Require all banking sites to have SSL certificates"},
                    {"text": "Implement DNSSEC to cryptographically validate DNS responses"},
                    {"text": "Deploy a web application firewall"},
                    {"text": "Enable MAC address filtering on the network"}
                ],
                "success_text": """
"We need DNSSEC," you explain. "DNS Security Extensions add cryptographic
signatures to DNS responses. When our DNS server asks for bankofamerica.com,
the response comes signed with keys that only the legitimate DNS
infrastructure controls."

"And if someone poisons our cache?"

"The poisoned entries won't have valid signatures. Our DNS resolver
rejects unsigned or incorrectly signed responses. The attackers can't
forge the cryptographic signatures without the private keys."

"Why isn't everyone using this already?"

"Deployment is still ongoing. But for our corporate DNS, we can enable
DNSSEC validation today. Any poisoned responses get rejected because
they can't produce valid signatures."

The DNS infrastructure is upgraded within a week. The next cache
poisoning attempt fails immediately - the forged responses have no
valid DNSSEC signatures.

You have demonstrated understanding of DNS SECURITY.
                """,
                "failure_texts": {
                    0: """
SSL certificates authenticate the web server, but they don't prevent
DNS redirection. If DNS sends users to 192.168.1.evil instead of the
real server, they never reach the legitimate SSL-protected server.
The attackers can even have their own SSL certificate for the fake
site. DNSSEC prevents the redirection at the DNS level.
                    """,
                    2: """
Web Application Firewalls protect web applications from HTTP-layer
attacks. They don't operate at the DNS level and cannot prevent DNS
cache poisoning. The attack happens before any HTTP traffic occurs -
it's in the name resolution phase. DNSSEC is the appropriate defense.
                    """,
                    3: """
MAC filtering controls which devices can access the network based on
hardware addresses. It has no relationship to DNS security and cannot
prevent cache poisoning attacks. DNSSEC cryptographically validates
DNS responses to prevent exactly this type of manipulation.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
DNSSEC (DNS Security Extensions) cryptographically signs DNS records,
allowing clients to verify that responses are authentic and haven't
been tampered with. This prevents DNS spoofing and cache poisoning
attacks that redirect users to malicious sites.
        """,
        "domain_reference": "Domain 4: Communication and Network Security - DNS Security"
    },

    # Scenario 7: Email Security (SPF/DKIM/DMARC)
    {
        "id": "d4_email_security",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE FORGED ROYAL DECREES",
                "narrative": """
The Kingdom is in chaos. Official decrees bearing the Royal Seal have been
arriving at provincial lords, demanding tribute payments to a mysterious
new treasury. The decrees look perfect - correct formatting, proper seals,
authentic-looking signatures.

But the King issued no such decrees. Someone is forging royal communications,
and the forgeries are indistinguishable from genuine messages.

"The lords receive these false decrees through the standard message network,"
the Chancellor explains. "The messages claim to originate from the Royal
Palace, but they come from impostors. Our current message system cannot
verify that a message truly comes from where it claims."

"We need layers of verification," you respond. "First, we declare which
message towers are authorized to send royal decrees. Second, we cryptographically
sign each genuine message. Third, we tell receiving lords to reject any
message that fails either check."

The Chancellor nods gravely. "What would you call such a system?"

What combination of controls prevents domain spoofing?
                """,
                "choices": [
                    {"text": "Spam filters and message scanning for malicious content"},
                    {"text": "SPF to authorize senders, DKIM to sign messages, and DMARC to enforce policy"},
                    {"text": "Encrypted message transmission to protect content confidentiality"},
                    {"text": "Individual message encryption with magical seals for each recipient"}
                ],
                "success_text": """
"Three controls working together," you explain, sketching the design.

"First: Sender Policy Framework - a public declaration listing which
message towers are authorized to send royal decrees. Any message claiming
royal origin but coming from an unlisted tower is suspicious.

"Second: DomainKeys Identified Mail - each genuine message bears a
cryptographic signature that only the Royal Scribes can create. Receivers
verify the signature to confirm the message is authentic and unchanged.

"Third: Domain-based Message Authentication - a policy telling receivers
what to do when messages fail SPF or DKIM checks. We declare: 'Reject
any message claiming to be from us that fails authentication.'"

"So receivers know to ignore the forgeries?"

"Precisely. SPF verifies the sending tower. DKIM verifies the message
integrity. DMARC enforces the policy. Together, they make domain spoofing
detectable and rejectable."

You have demonstrated understanding of EMAIL SECURITY controls.
                """,
                "failure_texts": {
                    0: """
Spam filters may catch some phishing attempts but cannot specifically
verify that messages truly originate from claimed domains. They don't
prevent domain spoofing - an attacker can craft convincing messages
that pass spam filters. SPF+DKIM+DMARC specifically authenticate
message origin.
                    """,
                    2: """
TLS encrypts email in transit, protecting confidentiality between
mail servers. It doesn't verify that the sender domain is legitimate -
encrypted forgeries are still forgeries. SPF+DKIM+DMARC authenticate
the sender domain, which is a different concern than encryption.
                    """,
                    3: """
S/MIME encrypts and signs individual messages between specific users,
providing end-to-end protection. But it doesn't prevent domain-level
spoofing where attackers claim to send from your organization.
SPF+DKIM+DMARC work at the domain level to prevent anyone from
impersonating your organization.
                    """
                }
            },
            "corporate": {
                "title": "THE INTERNAL PHISHING WAVE",
                "narrative": """
The executive assistant bursts into your office. "The CEO is NOT
requesting emergency wire transfers! These emails are NOT from him!"

Over the past week, dozens of employees received urgent emails appearing
to come from executives - requesting wire transfers, gift cards, password
resets. The "From" addresses showed legitimate company domains. Some
employees fell for it.

"How is this possible?" your manager demands. "They're sending email
as OUR domain!"

You examine the message headers. The emails originated from external
servers but claimed to be from @yourcompany.com. Your mail servers
accepted them because there's no mechanism verifying that messages
actually come from authorized sources.

"We're being domain-spoofed," you explain. "Anyone on the internet can
claim to send email from our domain, and recipients have no way to
verify it's genuine."

What combination of controls would BEST prevent this?
                """,
                "choices": [
                    {"text": "Upgrade spam filters and add better antivirus scanning"},
                    {"text": "Implement SPF, DKIM, and DMARC for domain authentication"},
                    {"text": "Enable TLS encryption for all email transmission"},
                    {"text": "Deploy S/MIME encryption for all employee emails"}
                ],
                "success_text": """
You pull up the implementation plan. "We need three layers of email
authentication:

"SPF - we publish a DNS record listing every server authorized to send
email for our domain. Receiving mail servers can check if incoming mail
actually came from an authorized server.

"DKIM - we cryptographically sign all outgoing messages. Receivers can
verify the signature to confirm messages are genuine and unmodified.

"DMARC - we publish a policy telling receivers what to do with messages
that fail SPF or DKIM. We say 'reject anything that fails authentication.'
We also get reports about spoofing attempts."

"And this stops the spoofing?"

"Receiving servers that check DMARC will reject spoofed emails claiming
to be from us. The attackers can't forge valid DKIM signatures without
our private keys. They can't send from authorized servers without
compromising them."

Implementation takes a month. The spoofing attacks drop to near zero.

You have demonstrated understanding of EMAIL SECURITY controls.
                """,
                "failure_texts": {
                    0: """
Spam filters help but cannot specifically prevent domain spoofing.
Attackers can craft convincing emails that pass content filters.
SPF+DKIM+DMARC provide cryptographic verification of sender domains,
which is fundamentally different from content scanning.
                    """,
                    2: """
TLS encrypts email in transit, protecting against eavesdropping. It
doesn't verify that the sender domain is legitimate. An attacker's
spoofed email can travel over TLS just as easily as legitimate email.
SPF+DKIM+DMARC authenticate sender domains, addressing the spoofing
problem directly.
                    """,
                    3: """
S/MIME provides end-to-end encryption and signing for individual users,
but it doesn't prevent domain-level spoofing. Attackers sending email
as "ceo@yourcompany.com" don't have the CEO's S/MIME certificate, but
most recipients don't check for that. SPF+DKIM+DMARC work at the
infrastructure level to reject spoofed messages before delivery.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
SPF validates which servers can send email for your domain. DKIM
cryptographically signs emails proving origin. DMARC provides policy
enforcement and reporting. Together, they allow receiving servers to
reject spoofed emails claiming to be from your domain.
        """,
        "domain_reference": "Domain 4: Communication and Network Security - Email Security"
    },

    # Scenario 8: Man-in-the-Middle / ARP Spoofing
    {
        "id": "d4_arp_spoofing",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE INVISIBLE INTERCEPTOR",
                "narrative": """
Messages between the Citadel's towers are being intercepted and modified,
yet no one can find the spy. Scouts report that enchanted parchments reach
their destinations unchanged... or so they appear. But critical orders are
arriving corrupted, approvals are being forged, and secrets are leaking.

An apprentice wizard finally notices the pattern. "The messages pass through
someone else before reaching the gate tower! When I trace the magical
pathway, I see our local address crystal being answered by... something
else. Something claiming to BE the gate tower."

You investigate the local address resolution system. When a tower asks
"What is the crystal signature for the Gate Tower?", an impostor answers
first: "It's MY signature. Send everything to ME." The impostor receives
all messages, reads or modifies them, then forwards them to the real gate.

"The villain corrupts our local address tables," you realize. "Every tower
thinks the impostor IS the gate tower. What attack is this?"

What type of attack is being described?
                """,
                "choices": [
                    {"text": "Name oracle poisoning - corrupting the direction-giving system"},
                    {"text": "Address resolution deception - redirecting traffic through a false node"},
                    {"text": "Flood attack - overwhelming the towers with too many messages"},
                    {"text": "Message fragmentation - exploiting how large messages are split"}
                ],
                "success_text": """
"This is ARP spoofing - Address Resolution Protocol poisoning," you explain.
"In the mundane realm, ARP translates IP addresses to physical MAC addresses.
Here, it translates tower names to crystal signatures."

"The attacker sends false address claims - 'I am the Gate Tower' - and
our crystals believe them. All traffic meant for the Gate Tower flows to
the impostor instead. They're now 'in the middle' of every conversation."

"How did we not notice?"

"Because the impostor forwards everything after reading it. Messages still
arrive, just... slightly delayed. The interception is invisible unless you
trace the actual pathway."

"The defense?"

"Static address tables for critical towers. Dynamic ARP inspection that
validates claims against known-good values. Port security to limit which
devices can make address claims. And encryption of message contents so
interception reveals nothing useful."

You have demonstrated understanding of NETWORK ATTACKS - specifically ARP spoofing.
                """,
                "failure_texts": {
                    0: """
DNS poisoning attacks the name-to-IP translation (Layer 7). This attack
operates at Layer 2, corrupting the IP-to-MAC address resolution tables.
ARP spoofing poisons local network address tables, allowing an attacker
to intercept traffic on the same network segment.
                    """,
                    2: """
SYN flood is a denial-of-service attack that overwhelms servers with
connection requests. This attack doesn't deny service - traffic still
flows, just through an interceptor. ARP spoofing enables man-in-the-middle
attacks, not denial of service.
                    """,
                    3: """
IP fragmentation attacks exploit how large packets are split and
reassembled. This attack manipulates address resolution to redirect
traffic. ARP spoofing poisons address tables, causing traffic to route
through an attacker-controlled system.
                    """
                }
            },
            "corporate": {
                "title": "THE COFFEE SHOP COMPROMISE",
                "narrative": """
Your security awareness training just got very real. You're at a coffee
shop, laptop open, working on email. A colleague texts you: "Did you
just send me credentials to the development server? That's weird..."

You check your sent folder. Nothing there. But your network traffic is
being captured - someone on this coffee shop network is intercepting
everything you send and receive.

Later, analyzing the attack from a secure location, you understand what
happened. An attacker on the same network sent fake responses to your
laptop's address resolution requests. When your laptop asked "What's the
MAC address for the gateway router?", the attacker answered: "It's MY
MAC address."

All your traffic - meant for the internet - routed through the attacker's
laptop first. They captured credentials, session tokens, everything
unencrypted.

What attack did you fall victim to?
                """,
                "choices": [
                    {"text": "DNS poisoning attack"},
                    {"text": "ARP spoofing/poisoning attack"},
                    {"text": "SYN flood denial of service attack"},
                    {"text": "IP fragmentation attack"}
                ],
                "success_text": """
"ARP spoofing," you confirm, writing up the incident report. "The attacker
exploited how local networks resolve IP addresses to physical MAC addresses."

You sketch the attack flow:
"1. My laptop needs to send traffic to the gateway (192.168.1.1)
2. It broadcasts: 'Who has 192.168.1.1?'
3. The attacker responds: 'That's me! Send traffic to my MAC.'
4. My laptop's ARP cache now maps the gateway IP to the attacker's MAC
5. All my internet traffic goes to the attacker first
6. Attacker forwards it after logging everything"

"Why didn't you notice?"

"Because traffic still worked. The attacker forwarded everything - just
captured a copy first. Classic man-in-the-middle positioning through
ARP cache poisoning."

"Lessons learned?"

"Never trust public WiFi for sensitive work. Use VPN. Use HTTPS exclusively.
Assume the network is hostile. ARP spoofing is trivially easy on shared
networks."

You have demonstrated understanding of NETWORK ATTACKS.
                """,
                "failure_texts": {
                    0: """
DNS poisoning corrupts name-to-IP resolution at the DNS level. This attack
operated at Layer 2, poisoning ARP tables that map IP addresses to MAC
addresses. Different attack vectors - DNS is application layer, ARP is
data link layer.
                    """,
                    2: """
SYN flood is a denial-of-service attack that prevents new connections.
This attack didn't prevent anything - it intercepted traffic. ARP spoofing
enables man-in-the-middle attacks where the attacker captures and forwards
traffic transparently.
                    """,
                    3: """
IP fragmentation attacks exploit packet reassembly vulnerabilities. This
attack manipulated Layer 2 address resolution to redirect traffic through
an attacker system. ARP spoofing poisons local address tables, enabling
traffic interception.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
ARP spoofing (or ARP poisoning) involves sending fake ARP replies to
associate the attacker's MAC address with legitimate IP addresses (like
the gateway). This redirects traffic through the attacker's machine,
enabling man-in-the-middle interception.
        """,
        "domain_reference": "Domain 4: Communication and Network Security - Network Attacks"
    },

    # Scenario 9: IDS vs IPS
    {
        "id": "d4_ids_vs_ips",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE OBSERVING GARGOYLE",
                "narrative": """
The Citadel was breached last night. A dark wizard slipped through the
outer wards, traversed the inner corridors, and stole three ancient relics
before escaping. The Citadel's enchanted gargoyle guardian saw everything.

"You saw the intruder?" the Archmage demands of the stone creature.

"Oh yes, Master. I observed his every move. I noted his dark aura, his
malicious intent, his strange shadow-walking magic. I created detailed
records of his entire intrusion." The gargoyle gestures at a stack of
parchments. "My reports were quite thorough."

"But you didn't STOP him?!"

"That... is not my function. I detect and alert. I do not intervene.
You should have received my warning scrolls?"

The Archmage's face turns crimson. "AFTER the theft! Hours later!"

"Yes, I report at the end of each night. Is that not sufficient?"

What is the fundamental problem with this security control?

                """,
                "choices": [
                    {"text": "It's an IPS that failed to detect the intrusion - replace with a better IPS"},
                    {"text": "It's an IDS that only detects; they need an IPS that actively blocks threats"},
                    {"text": "It's a WAF that only handles web attacks - they need network protection"},
                    {"text": "It's a firewall that needs better detection rules added to it"}
                ],
                "success_text": """
"Your gargoyle is an IDS - an Intrusion Detection System," you explain
to the frustrated Archmage. "It observes, analyzes, records, and alerts.
But it does not intervene. It cannot block attacks in progress."

"Then it's useless!"

"Not useless - but insufficient alone. Detection without prevention allows
attackers to succeed while you receive alerts. What you need is an IPS -
an Intrusion Prevention System."

"What's the difference?"

"An IPS sits directly in the path of traffic. When it detects malicious
activity, it blocks it immediately. The dark wizard would have been stopped
at the first ward, not observed committing the theft and reported later."

"Then why have IDS at all?"

"IDS watches traffic copies without delaying them - useful for analysis
without impacting performance. But for stopping attacks in real-time, you
need IPS positioned inline."

You have demonstrated understanding of IDS versus IPS.
                """,
                "failure_texts": {
                    0: """
The gargoyle detected the intrusion just fine - it created detailed records
of everything. The problem isn't detection capability but the lack of
prevention capability. IDS detects and alerts; IPS detects AND blocks.
This was an IDS functioning as designed, but design was insufficient.
                    """,
                    2: """
WAFs (Web Application Firewalls) specifically protect web applications
from HTTP attacks. This scenario describes general intrusion detection,
not web-specific protection. The issue is IDS vs IPS - detection-only
versus active prevention of detected threats.
                    """,
                    3: """
Firewalls block traffic based on rules about ports, protocols, and addresses.
IDS/IPS analyze traffic content and behavior for malicious patterns.
The gargoyle was detecting malicious activity (intrusion detection) but
not blocking it. It needs to be replaced with or supplemented by an IPS.
                    """
                }
            },
            "corporate": {
                "title": "THE SECURITY SYSTEM THAT WATCHED",
                "narrative": """
The post-incident review is brutal. Last week, attackers exfiltrated the
entire customer database. The attack took six hours. The security team
found out the next morning when they reviewed overnight alerts.

"How did we not stop this?!" the CISO demands.

The security analyst pulls up the logs. "We have 147 alerts from the
attack. The security system detected every phase: initial access, lateral
movement, privilege escalation, data staging, exfiltration. Complete
visibility into the entire attack chain."

"So you WATCHED them steal our data?!"

"The system detected and alerted. That's what it does. It doesn't block
traffic - it copies traffic, analyzes it, and generates alerts. The
alerts went to the queue... which we review each morning."

The CISO's eye twitches. "So we have a system that watches crimes happen
and sends us a report afterward?"

What is the fundamental issue here?
                """,
                "choices": [
                    {"text": "It was an IPS that failed - upgrade to a better IPS"},
                    {"text": "It was an IDS - they need an IPS for active blocking"},
                    {"text": "It was a WAF - they need network-level protection"},
                    {"text": "It was a firewall - they need better rules"}
                ],
                "success_text": """
"You have an IDS - Intrusion Detection System," you explain. "It detected
everything perfectly. The problem is, IDS only monitors and alerts. It
does not block."

"The vendor said it was 'advanced threat detection'!"

"And it detected threats. Admirably. It just can't stop them. For that,
you need an IPS - Intrusion Prevention System. An IPS sits inline - all
traffic passes through it. When it detects malicious activity, it blocks
it immediately."

"Why would anyone want IDS instead of IPS?"

"IDS analyzes copies of traffic, so it can't accidentally block legitimate
activity. Some organizations fear false positives disrupting operations.
But as you've learned, detection without prevention means watching attacks
happen while generating excellent documentation of your compromise."

"So we need IPS?"

"You need IPS for active threats. You can keep IDS for additional visibility.
But something must be able to actually stop attacks, not just observe them."

You have demonstrated understanding of IDS versus IPS.
                """,
                "failure_texts": {
                    0: """
The system detected everything - 147 accurate alerts across the entire
attack chain. Detection worked perfectly. The problem is that IDS only
detects; it doesn't block. If it were an IPS, it would have stopped the
attack at the first detected phase instead of just alerting.
                    """,
                    2: """
WAFs protect web applications from HTTP-layer attacks. This scenario
describes a data exfiltration across the network, detected but not blocked.
The distinction is between IDS (detection only) and IPS (detection plus
prevention). They need IPS to actually block detected attacks.
                    """,
                    3: """
Firewalls filter traffic based on predetermined rules about addresses,
ports, and protocols. IDS/IPS analyze traffic behavior and content for
malicious patterns. This was definitely an IDS - it detected the attack.
The missing capability is prevention, which requires an IPS.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
An Intrusion Detection System (IDS) monitors and alerts but doesn't block
traffic. An Intrusion Prevention System (IPS) sits inline and can actively
block detected threats. If detection occurred but blocking didn't, an IDS
was in use when an IPS was needed.
        """,
        "domain_reference": "Domain 4: Communication and Network Security - IDS/IPS"
    },

    # Scenario 10: Network Access Control (802.1X)
    {
        "id": "d4_network_access_control",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE MERCHANT'S UNKNOWN CRYSTAL",
                "narrative": """
A traveling merchant arrives at the Citadel gates, producing a communication
crystal and requesting access to the trading network. The guards are unsure -
the crystal looks legitimate, but they have no way to verify its origin or
ensure it meets Citadel security standards.

"We cannot simply allow unknown crystals onto our network," the Captain
of the Guard argues. "What if it carries corruption? What if it's been
compromised? We don't even know if it has proper protective enchantments."

The merchant protests. "I am a legitimate trader! I have documents!"

"Documents can be forged. Your crystal may be genuine, or it may be a
vessel for dark magic. We need a way to verify both your identity AND
your crystal's security before granting network access."

What technology enables the Citadel to verify device identity and
security posture before granting network access?
                """,
                "choices": [
                    {"text": "Message inspection to detect rogue DHCP enchantments"},
                    {"text": "Crystal duplication for monitoring network traffic"},
                    {"text": "Portal authentication with security verification before network access"},
                    {"text": "Maintaining a list of approved crystal signatures for matching"}
                ],
                "success_text": """
"We implement port-based access control with health verification," you
explain. "In the mortal realm, this is called 802.1X with NAC - Network
Access Control."

"How does it work?"

"When the merchant's crystal connects to a network access point, it cannot
communicate until it authenticates. First, we verify the merchant's identity
through a central authentication authority. Second, we inspect the crystal
itself - does it have current protective enchantments? Is it free of
corruption? Does it meet our security requirements?"

"And if it fails?"

"It's quarantined. The crystal can only access remediation services - a
healing ward to cure infections, an update fountain to refresh protections.
Only after passing all checks does it gain network access."

"So no unknown, unhealthy crystals on our network?"

"Precisely. Every device must prove both identity and health before
gaining access. This prevents compromised or non-compliant devices from
accessing protected resources."

You have demonstrated understanding of NETWORK ACCESS CONTROL.
                """,
                "failure_texts": {
                    0: """
DHCP snooping prevents rogue DHCP servers from assigning addresses on
the network. It doesn't authenticate devices or verify their security
posture. 802.1X with NAC provides both device authentication and health
verification before granting network access.
                    """,
                    1: """
Port mirroring copies traffic to a monitoring device for analysis. It
doesn't control network access or verify device compliance. 802.1X with
NAC actually blocks network access until both identity and security
posture are verified.
                    """,
                    3: """
MAC address tables are used for basic switching decisions and can be
filtered for basic access control. However, MAC addresses can be spoofed,
and MAC filtering doesn't verify device health or identity through
authentication. 802.1X with NAC provides true identity verification and
posture assessment.
                    """
                }
            },
            "corporate": {
                "title": "THE CONTRACTOR'S LAPTOP",
                "narrative": """
The network just got interesting. A contractor showed up, plugged their
personal laptop into an open network jack in the conference room, and
connected directly to the corporate network. No authentication. No
verification. Full access.

Your manager discovered this when the contractor's malware-infected laptop
started scanning internal servers.

"How is this possible?" the IT director demands. "Anyone can just plug in
and get network access?"

"Currently, yes. Our network ports are open. If something connects and
requests an IP address, DHCP gives it one, and it's on the network."

"That's insane. A visitor could plug in a compromised device and have
access to everything!"

"That's exactly what happened."

What technology should be implemented to verify device identity and
security posture before granting network access?
                """,
                "choices": [
                    {"text": "DHCP snooping to prevent rogue DHCP servers"},
                    {"text": "Port mirroring to monitor all traffic"},
                    {"text": "802.1X with NAC for authentication and posture checking"},
                    {"text": "Maintain a MAC address whitelist"}
                ],
                "success_text": """
"We need 802.1X with NAC," you explain, pulling up a diagram. "Here's
how it works:

"When a device plugs into a network port, it can't communicate with
anything except an authentication server. The port is 'closed' until
the device proves itself.

"First, 802.1X verifies the device's identity - through certificates,
credentials, or domain membership.

"Second, NAC checks the device's security posture - is antivirus running
and current? Is the OS patched? Does it meet our security baseline?

"If either check fails, the device goes to a quarantine VLAN where it
can only access remediation resources."

"What about legitimate contractors?"

"They authenticate with guest credentials and get limited network access
only. Their device posture is still verified before any access is granted."

"So no more 'plug in and you're on the network'?"

"Every device must prove identity and health. No exceptions."

You have demonstrated understanding of NETWORK ACCESS CONTROL.
                """,
                "failure_texts": {
                    0: """
DHCP snooping prevents rogue DHCP servers from operating on the network -
it doesn't control which devices can connect or verify their security
status. 802.1X with NAC provides port-based authentication and health
checking before granting network access.
                    """,
                    1: """
Port mirroring copies traffic for monitoring and analysis. It doesn't
prevent unauthorized devices from connecting or verify device compliance.
802.1X with NAC actually blocks network access until authentication and
posture verification succeed.
                    """,
                    3: """
MAC address whitelists provide very limited access control. MAC addresses
are easily spoofed, and this approach doesn't verify device health or
use strong authentication. 802.1X provides certificate or credential-
based authentication, and NAC verifies device security posture.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
802.1X provides port-based network access control, requiring authentication
before granting network access. Combined with NAC (Network Access Control),
it can also verify device health/posture (patches, antivirus, compliance)
before allowing connection.
        """,
        "domain_reference": "Domain 4: Communication and Network Security - Network Access Control"
    },

    # Scenario 11: Secure Protocols (SFTP)
    {
        "id": "d4_secure_protocols",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE SCROLL COURIER'S CONCERN",
                "narrative": """
The Master Scribe summons you with an urgent request. "We must establish
secure scroll transfer to the Northern Archives. The route crosses disputed
territory - every message we send could be intercepted by enemy scouts."

"What are the requirements?" you ask.

"First, the scroll contents must be protected from prying eyes - complete
secrecy of what we send. Second, we must verify we're actually reaching
the Northern Archives and not some impostor tower. Third, the common
message couriers along the route support only standard protocols - we
cannot require special magical equipment at every waystation."

You consider the options. Standard scroll couriers transmit everything
in clear text - anyone who intercepts them reads everything. The Northern
Archives have their own authentication seals that could verify their
identity if the protocol supports it.

"Which transfer enchantment meets both requirements - confidentiality
AND server verification - using standard magical infrastructure?"
                """,
                "choices": [
                    {"text": "Standard open courier - fastest and simplest"},
                    {"text": "Lightweight courier with no authentication - quick but not secure"},
                    {"text": "Encrypted tunneled courier with server seal verification"},
                    {"text": "Voice message relay - spoken words cannot be captured"}
                ],
                "success_text": """
"You need SFTP - Secure File Transfer Protocol," you explain. "In magical
terms, an encrypted tunnel with server verification."

"How does it differ from standard couriers?"

"Standard file transfer - FTP - sends everything in clear text, including
your authentication words. Anyone who intercepts the courier reads
everything. SFTP runs over an encrypted channel - SSH. The contents are
protected from eavesdroppers."

"And the verification requirement?"

"SSH verifies the server's identity through cryptographic seals - host
keys. When you first connect to the Northern Archives, you verify their
seal. Future connections confirm that seal hasn't changed. If an impostor
tries to intercept your connection, the seal mismatch alerts you."

"So confidentiality and server authentication in one protocol?"

"Precisely. SFTP provides both encryption for data in transit and server
authentication through SSH. It's the secure way to transfer files across
untrusted networks."

You have demonstrated understanding of SECURE PROTOCOLS.
                """,
                "failure_texts": {
                    0: """
FTP - File Transfer Protocol - transmits everything in cleartext,
including usernames and passwords. Anyone intercepting the traffic reads
everything. It provides no encryption and no server authentication. Never
use FTP for sensitive file transfers across untrusted networks.
                    """,
                    1: """
TFTP - Trivial File Transfer Protocol - has no authentication and no
encryption whatsoever. It was designed for simple, trusted environments
like network boot sequences. Using TFTP across hostile territory would
expose everything to any interceptor.
                    """,
                    3: """
Telnet transmits everything in cleartext, just like FTP. Using Telnet
for file transfer would expose all content and credentials. Even if you
encoded files as text, interception would reveal everything. SSH/SFTP
provides actual encryption and server authentication.
                    """
                }
            },
            "corporate": {
                "title": "THE DEVELOPER'S DILEMMA",
                "narrative": """
The development team needs to transfer build artifacts to a remote server.
The server is located in a cloud provider's network - traffic crosses the
public internet.

"Just FTP it," someone suggests. The security team's collective groan
is audible three floors away.

"We have requirements," you explain patiently. "First, encryption - the
build artifacts contain proprietary code. They must be protected in transit.
Second, server authentication - we must verify we're actually connecting
to our server, not some man-in-the-middle. Third, it should use standard
protocols - no weird custom solutions."

The developer looks confused. "What's wrong with FTP?"

"FTP sends everything in cleartext. Credentials, file contents, everything.
Anyone between here and the server can read it all. And it doesn't verify
you're talking to the right server."

Which protocol is MOST appropriate for secure file transfer?
                """,
                "choices": [
                    {"text": "FTP - File Transfer Protocol"},
                    {"text": "TFTP - Trivial File Transfer Protocol"},
                    {"text": "SFTP - SSH File Transfer Protocol"},
                    {"text": "Telnet with file transfer commands"}
                ],
                "success_text": """
"SFTP - SSH File Transfer Protocol," you explain. "It solves both problems.

"First, SFTP runs over SSH, which encrypts everything. The file contents,
the commands, even the authentication - all encrypted. Someone intercepting
traffic sees only encrypted noise.

"Second, SSH verifies the server's identity through host key checking.
The first time you connect, you verify the server's fingerprint. If
someone tries a man-in-the-middle attack, the key mismatch triggers a
warning.

"Third, every Unix/Linux server supports SSH and SFTP natively. Windows
servers can run OpenSSH. It's standard, secure, and mature."

"What about FTPS?"

"FTPS adds TLS encryption to FTP. It works, but SFTP is generally simpler
to implement and firewall - single port, single connection, encrypted
everything."

The developer nods and updates the deployment scripts to use SFTP.

You have demonstrated understanding of SECURE PROTOCOLS.
                """,
                "failure_texts": {
                    0: """
FTP transmits data and credentials in cleartext - zero encryption. Anyone
on the network path can capture usernames, passwords, and file contents.
For sensitive transfers across untrusted networks, FTP is completely
unacceptable. SFTP provides the required encryption.
                    """,
                    1: """
TFTP - Trivial FTP - has no authentication and no encryption. It was
designed for simple trusted environments, not internet file transfers.
Using TFTP across the public internet would be catastrophically insecure.
SFTP is the secure alternative.
                    """,
                    3: """
Telnet transmits everything in cleartext, including file contents.
It's considered deprecated for any security-sensitive purpose. SSH
replaced Telnet specifically because of these security weaknesses.
SFTP runs over SSH, providing both encryption and server authentication.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
SFTP runs over SSH, providing encryption for data in transit and server
authentication through SSH host keys. FTP and TFTP transmit data in
cleartext with no encryption. Always use SFTP or equivalent secure
protocols for file transfers across untrusted networks.
        """,
        "domain_reference": "Domain 4: Communication and Network Security - Secure Protocols"
    },

    # Scenario 12: DDoS Mitigation
    {
        "id": "d4_ddos_mitigation",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE SIEGE OF A THOUSAND MESSENGERS",
                "narrative": """
The Citadel is under attack, but not by swords or siege engines. A thousand
messenger birds arrive each minute, each carrying a trivial request that
must be processed. The Message Hall is overwhelmed - scribes cannot sort
the flood of meaningless queries from legitimate communications.

"The road to our gates is choked with these false messengers," the Warden
reports grimly. "Even if we could identify and reject them at the Message
Hall, they've already consumed our capacity to receive anything. The
pathway itself is saturated."

You examine the situation. The Citadel's receiving capacity is 100
messages per minute. Enemies are sending 10,000 per minute from locations
across the realm. Even with perfect filtering, 9,900 malicious messages
must still travel the road to reach your filters.

"The attack volume exceeds our entire capacity to receive," you realize.
"Filtering at our gates is useless - the pathway is flooded before
messages reach us."

What is the MOST effective mitigation approach?
                """,
                "choices": [
                    {"text": "Add more filtering scribes at the Message Hall to reject bad messages faster"},
                    {"text": "Double the size of our receiving pathway to handle more traffic"},
                    {"text": "Engage cloud scrubbing towers that absorb the flood before it reaches us"},
                    {"text": "Tell our Message Hall to process requests more slowly to reduce load"}
                ],
                "success_text": """
"You need a cloud-based DDoS mitigation service," you explain, conjuring
an illustration. "Think of it as a network of allied kingdoms with
massive message-handling capacity, positioned between you and the attackers."

"How would that help?"

"The attack traffic never reaches your gates. The cloud service has
receiving capacity thousands of times greater than yours, distributed
across the realm. They absorb the flood of malicious messages at their
locations, filter out the attacks, and forward only legitimate traffic
to you."

"But can't the attackers just... send more?"

"The cloud services are specifically designed for this battle. They
have more capacity than any attacker can generate. Your 100-message
capacity becomes irrelevant because you only receive the 10 legitimate
messages per minute that survive the filtering."

"Fighting at our gates was hopeless because the road was already flooded.
Fighting in the cloud means the flood never reaches our road."

You have demonstrated understanding of DDOS MITIGATION.
                """,
                "failure_texts": {
                    0: """
If traffic volume exceeds your connection capacity, malicious packets
are dropped BEFORE reaching your firewall. Adding more filtering capacity
at your location doesn't help because the flood has already consumed your
bandwidth. Cloud-based mitigation absorbs attacks before they reach your
infrastructure.
                    """,
                    1: """
Attackers can typically scale faster than you can buy bandwidth. This
becomes an economic war you cannot win - they generate traffic cheaply
from botnets while you pay for expensive bandwidth upgrades. Cloud DDoS
mitigation services have economy of scale that individual organizations
cannot match.
                    """,
                    3: """
Rate limiting on your web server helps with application-layer attacks
but cannot stop volumetric attacks that saturate your connection before
traffic reaches the server. If the pipe is flooded, what happens at
the end of the pipe is irrelevant. Cloud mitigation stops the flood
before it reaches your pipe.
                    """
                }
            },
            "corporate": {
                "title": "THE BANDWIDTH APOCALYPSE",
                "narrative": """
Your company's website is dead. Not crashed - dead. The entire internet
connection is saturated with incoming traffic. Packet loss is at 90%.
Legitimate customers can't reach you because the pipe is completely
flooded with garbage traffic.

"Can't we just block the attacking IPs?" the CEO demands during the
emergency call.

"We're trying. But there are millions of source IPs - it's a distributed
attack. And even if we could identify and block them all, the traffic
still hits our internet connection before reaching our firewall. The
pipe is full. Nothing else fits."

"Add more bandwidth?"

"We have 1 Gbps. The attack is 50 Gbps. Even if we upgraded to 10 Gbps
by tomorrow, they'd just increase to 60 Gbps. We can't win this race."

The CFO looks pale. "Every minute of downtime is costing us..."

What is the MOST effective mitigation approach?
                """,
                "choices": [
                    {"text": "Increase local firewall rule capacity to block malicious IPs"},
                    {"text": "Upgrade to a faster internet connection"},
                    {"text": "Engage a cloud-based DDoS mitigation service"},
                    {"text": "Enable rate limiting on the web servers"}
                ],
                "success_text": """
"We need cloud-based DDoS mitigation," you explain. "Here's why nothing
else works:

"Local firewall rules can't help because traffic is dropped before it
reaches our firewall - the ISP link is saturated.

"Buying more bandwidth is a losing game - attackers rent botnets for
pennies while we pay for premium bandwidth.

"Rate limiting happens after traffic reaches our servers - which it
can't when the connection is flooded.

"Cloud DDoS services have massive globally distributed capacity. We
route our DNS to them. Attack traffic hits their scrubbing centers
instead of our pipe. They filter out the garbage and forward only
legitimate traffic. Our 1 Gbps connection suddenly only carries the
few Mbps of real user traffic."

Within an hour of engaging the cloud service, the website is back.
The attack continues for days, absorbed harmlessly by the mitigation
provider.

You have demonstrated understanding of DDOS MITIGATION.
                """,
                "failure_texts": {
                    0: """
When traffic volume exceeds your connection capacity, packets are dropped
at the ISP level before reaching your firewall. Adding more firewall
rules is irrelevant - the traffic never gets there to be filtered. Cloud
mitigation absorbs the attack before it reaches your network.
                    """,
                    1: """
Attackers can scale faster than you can buy bandwidth. Botnet capacity
is effectively unlimited and cheap. Enterprise bandwidth is expensive
and slow to provision. This is an economic battle you cannot win. Cloud
DDoS services have economy of scale that makes them viable where direct
bandwidth competition is not.
                    """,
                    3: """
Rate limiting only helps if traffic reaches your servers. When the
internet connection is saturated, requests never reach the servers at
all. The congestion happens before your infrastructure. Cloud mitigation
intercepts traffic before it reaches your connection, where your rate
limiting could theoretically apply.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Cloud-based DDoS mitigation services have massive capacity distributed
globally. They absorb attack traffic at their edge locations before it
reaches your network, handling volumes that would overwhelm any single-
location defense.
        """,
        "domain_reference": "Domain 4: Communication and Network Security - DDoS Mitigation"
    },

    # Scenario 13: Load Balancing Security
    {
        "id": "d4_load_balancing",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE ENCHANTED GATEWAY'S DILEMMA",
                "narrative": """
The Citadel's main gateway has been enhanced with an enchanted distributor
that spreads incoming visitors across seven identical reception halls.
This prevents any single hall from being overwhelmed. But a new requirement
has arrived.

"The Council demands that we inspect all incoming messages for dark magic
before allowing entry," the Gateway Keeper explains. "We must also apply
protection wards to block malicious enchantments."

"That requires reading the content of sealed scrolls," you observe.

"Precisely the problem. Our scrolls travel in magical encrypted seals -
SSL enchantments - that hide their contents. The distributor cannot
inspect what it cannot read, nor can it apply protection wards to
encrypted traffic."

"Could you simply ignore the encryption?"

"Absolutely not! That would leave all messages vulnerable to eavesdroppers
between the sender and our gates."

How should SSL/TLS be configured to enable inspection and protection
at the load balancer?
                """,
                "choices": [
                    {"text": "SSL passthrough - keep everything encrypted end-to-end without inspection"},
                    {"text": "SSL offloading/termination - decrypt at the gateway for inspection"},
                    {"text": "Disable SSL entirely for better performance"},
                    {"text": "Use different SSL certificates for each hall"}
                ],
                "success_text": """
"You need SSL offloading - also called SSL termination," you explain.
"The encrypted seals are opened at the gateway, allowing full inspection."

"But then the messages are exposed!"

"Only between the gateway and the reception halls - inside your own
protected domain. The gateway can re-encrypt traffic for the internal
journey if required. But the key is: at the gateway, you can read
the content."

"And the protection wards?"

"Once traffic is decrypted, you can apply any inspection you need -
web application firewall rules, content scanning, dark magic detection.
You can make intelligent routing decisions based on content. You have
full visibility."

"What about performance?"

"The gateway handles all encryption work, offloading it from the seven
halls. They receive already-decrypted traffic and focus on their primary
function. Overall efficiency often improves."

You have demonstrated understanding of LOAD BALANCING SECURITY.
                """,
                "failure_texts": {
                    0: """
SSL passthrough maintains end-to-end encryption but completely prevents
the load balancer from inspecting traffic. It cannot see content, cannot
apply WAF rules, cannot make content-based routing decisions. If you need
inspection and protection at the load balancer, you need SSL termination.
                    """,
                    2: """
Disabling SSL entirely removes all encryption protection. Messages would
be readable by anyone on the network between sender and gateway. This is
completely unacceptable for sensitive applications. SSL termination
provides inspection capability while maintaining encryption to the gateway.
                    """,
                    3: """
Different certificates per backend server doesn't address the inspection
requirement at the load balancer. The load balancer still can't read
encrypted traffic passing through it. SSL termination decrypts at the
load balancer, enabling inspection before forwarding to backend servers.
                    """
                }
            },
            "corporate": {
                "title": "THE WAF CONFIGURATION PROBLEM",
                "narrative": """
The security team has a problem. They've deployed a web application
firewall to protect against SQL injection, XSS, and other attacks. The
WAF is integrated with the load balancer. There's just one problem.

"It's not catching anything," the security analyst reports. "We tested
it with known attack patterns. Nothing. The WAF sees... nothing useful."

You examine the configuration. All traffic between users and the load
balancer is HTTPS - encrypted. The load balancer is configured for SSL
passthrough, forwarding encrypted traffic directly to the backend servers.

"There's your problem," you explain. "The load balancer can't inspect
what it can't see. The traffic is encrypted. Your WAF is looking at
encrypted ciphertext, not the actual HTTP requests."

"But we need HTTPS for security!"

"You need HTTPS between users and your infrastructure. You don't
necessarily need it to pass through the load balancer uninspected."

How should SSL/TLS be configured to enable WAF functionality?
                """,
                "choices": [
                    {"text": "SSL passthrough - maintains encryption but prevents inspection"},
                    {"text": "SSL offloading/termination - decrypt at load balancer for inspection"},
                    {"text": "Disable SSL entirely for better visibility"},
                    {"text": "Use different SSL certificates for each backend server"}
                ],
                "success_text": """
"We need SSL termination at the load balancer," you explain, sketching
the new architecture.

"Users connect via HTTPS to the load balancer. The load balancer terminates
SSL - it decrypts the traffic using its certificate. Now the load balancer
sees actual HTTP requests, not encrypted blobs."

"And the WAF?"

"The WAF can now inspect every request. It sees the actual URLs, headers,
parameters, POST bodies - everything it needs to detect attacks. SQL
injection attempts are caught. XSS payloads are blocked."

"But what about the traffic to the backend servers?"

"You have two options: send it unencrypted over your trusted internal
network, or re-encrypt it - SSL re-encryption. Either way, the inspection
happens at the load balancer where you have full visibility."

The configuration is updated. Within a week, the WAF has blocked
hundreds of attack attempts that were previously invisible.

You have demonstrated understanding of LOAD BALANCING SECURITY.
                """,
                "failure_texts": {
                    0: """
SSL passthrough is exactly the problem! It maintains end-to-end encryption
but prevents any inspection at the load balancer. The WAF sees encrypted
traffic and cannot analyze HTTP content. SSL termination is required to
decrypt traffic for inspection.
                    """,
                    2: """
Disabling SSL entirely would expose all traffic to eavesdroppers on the
network. User credentials, session tokens, personal data - all visible to
anyone who can intercept traffic. SSL termination provides inspection
capability at the load balancer while maintaining encryption from users.
                    """,
                    3: """
Different certificates per backend server doesn't help with inspection
at the load balancer. The traffic is still encrypted as it passes through.
SSL termination decrypts at the load balancer, enabling WAF inspection
before forwarding to backend servers.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
SSL offloading (termination) decrypts traffic at the load balancer,
allowing it to inspect content, apply WAF rules, and make intelligent
routing decisions. Traffic can be re-encrypted to backend servers if
needed. Passthrough maintains encryption but prevents inspection.
        """,
        "domain_reference": "Domain 4: Communication and Network Security - Load Balancing"
    },

    # Scenario 14: CDN Security
    {
        "id": "d4_cdn_security",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE DISTRIBUTED WATCHTOWERS",
                "narrative": """
The Citadel's public message boards are famous throughout the realm.
Visitors from every kingdom access them constantly. But recently, a
coordinated attack targeted the boards directly, flooding the Citadel
with requests until the service collapsed.

"We've been attacked three times this month," the Public Affairs Minister
sighs. "Our message boards serve the entire realm, but we have only one
tower. When enemies learn its location, they strike directly."

"You need Content Distribution Towers," you suggest. "Copies of your
message boards, positioned throughout the realm. Visitors access the
nearest tower, not your central Citadel."

"How does that help with attacks?"

"Beyond improved performance, there are security benefits. First, the
distributed towers can absorb attack traffic across many locations
instead of one. Second..."

What is a key security benefit CDNs provide beyond performance?
                """,
                "choices": [
                    {"text": "CDNs automatically encrypt all origin databases"},
                    {"text": "CDN edge nodes absorb attack traffic and hide the origin server location"},
                    {"text": "CDNs eliminate the need for SSL certificates"},
                    {"text": "CDNs provide automatic vulnerability scanning of your code"}
                ],
                "success_text": """
"The security benefit is twofold," you explain. "First, CDN edge nodes
absorb attack traffic. A DDoS attack targeting your message boards hits
the distributed edge locations instead of your central tower. Those edge
locations have massive capacity specifically designed to handle traffic
floods."

"And the second benefit?"

"Origin hiding. Your actual Citadel tower address becomes secret. Public
visitors connect to CDN edge locations. The edge locations connect to
your origin, but attackers cannot directly target what they cannot find.
Properly configured, your true location is invisible to the outside world."

"So even if attackers bypass the edge..."

"They don't know WHERE to attack. Direct origin attacks become extremely
difficult when the origin address is hidden behind the CDN layer. Combined
with the distributed attack absorption, you become a much harder target."

"The realm's visitors get faster access AND we're better protected."

You have demonstrated understanding of CDN SECURITY.
                """,
                "failure_texts": {
                    0: """
CDNs cache and deliver content - they don't interact with databases at
all. Database encryption is a separate concern handled by the database
and application layers. CDN security benefits relate to traffic handling
and origin protection, not backend data security.
                    """,
                    2: """
CDNs don't eliminate the need for SSL certificates - they often provide
them! Many CDN services offer SSL certificates for edge locations. But
this is about providing SSL, not eliminating it. The security benefit
is about attack absorption and origin hiding.
                    """,
                    3: """
CDNs deliver content to end users efficiently - they don't scan your
code for vulnerabilities. Code scanning is performed by SAST (Static
Application Security Testing) and DAST (Dynamic Application Security
Testing) tools. CDN security relates to traffic handling and origin
protection.
                    """
                }
            },
            "corporate": {
                "title": "THE HIDDEN ORIGIN",
                "narrative": """
Your company's public website has been attacked repeatedly. Each time,
attackers discover your origin server IP address and launch targeted
DDoS attacks against it directly. The attacks bypass cloud-based
protections because they hit the origin directly.

"How do they keep finding our server?" the frustrated CTO asks.

"DNS history, email headers, configuration leaks, failed requests that
reveal origin... there are many ways," you explain. "Every time we
change IPs, they find the new one within days."

The security architect proposes a solution: "What if they couldn't find
the origin at all? What if every public request went through an
intermediary that hid our actual server location?"

"That's exactly what a properly configured CDN does," you realize.

From a security perspective, what is a key benefit the CDN provides?
                """,
                "choices": [
                    {"text": "CDNs automatically encrypt all backend databases"},
                    {"text": "CDN edge nodes absorb attack traffic and hide origin server IPs"},
                    {"text": "CDNs eliminate the need for SSL certificates"},
                    {"text": "CDNs provide automatic code vulnerability scanning"}
                ],
                "success_text": """
"There are two security benefits," you explain in the architecture review.

"First, origin hiding. When properly configured, the CDN becomes the only
public face of our infrastructure. Users connect to CDN edge locations.
The edges connect to our origin over private networks. Our origin IP is
never exposed publicly. Attackers can't directly target what they can't
find."

"What if they somehow discover the origin?"

"That's the second benefit - attack absorption. CDN edge locations are
designed to handle massive traffic volumes. Even if attackers target the
edges with DDoS attacks, the distributed infrastructure absorbs it across
many locations globally. The capacity is designed for exactly this threat."

"And our origin server?"

"Only receives legitimate traffic forwarded by the CDN. The flood never
reaches us because it's absorbed at the edge. Combined with origin hiding,
this creates a formidable defensive position."

The website hasn't suffered a successful DDoS attack since deployment.

You have demonstrated understanding of CDN SECURITY.
                """,
                "failure_texts": {
                    0: """
CDNs cache and deliver content - they don't touch databases. Database
encryption is a completely separate concern handled at the database
layer. CDN security is about traffic handling and hiding your origin
infrastructure, not backend data protection.
                    """,
                    2: """
CDNs don't eliminate SSL - they often provide it. Many CDNs offer
managed SSL certificates for their edge locations. But SSL provision
is about encryption, not the core security benefit of CDNs. The key
benefits are DDoS absorption and origin hiding.
                    """,
                    3: """
CDNs optimize content delivery - they don't analyze your code. Code
vulnerability scanning requires SAST/DAST tools that analyze source
code or running applications. CDN security relates to traffic handling
and protecting infrastructure location.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
CDNs distribute traffic across many edge locations globally. During DDoS
attacks, this distributed infrastructure absorbs malicious traffic.
Additionally, properly configured CDNs hide origin server IP addresses,
making direct attacks on your infrastructure much harder.
        """,
        "domain_reference": "Domain 4: Communication and Network Security - CDN Security"
    },

    # Scenario 15: SD-WAN Security
    {
        "id": "d4_sdwan_security",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE NEW ROAD NETWORK",
                "narrative": """
The Citadel is modernizing its communication routes to branch towers.
For decades, the kingdom maintained expensive private roads - MPLS
enchanted pathways - connecting each tower. Secure, reliable, but
enormously costly.

"We're switching to the common road network," the Logistics Minister
announces. "Cheaper, more flexible, and we can add new towers quickly
without building new private roads."

"The common roads are public," you warn. "Anyone can travel them. Our
messages will pass alongside merchant caravans, traveling performers,
and... those with less noble intentions."

"SD-WAN enchantments will manage the routing intelligently," the Minister
explains. "But I need you to identify the MOST critical security
consideration for this transition."

What security consideration is MOST critical when using internet-based
SD-WAN connections?
                """,
                "choices": [
                    {"text": "SD-WAN eliminates all need for tower firewalls"},
                    {"text": "All SD-WAN traffic must be encrypted since it traverses public roads"},
                    {"text": "SD-WAN automatically provides protection against curses and hexes"},
                    {"text": "Towers no longer need any local security controls"}
                ],
                "success_text": """
"Encryption is absolutely critical," you emphasize. "MPLS private roads
were physically isolated - only authorized travelers could access them.
The public road network has no such isolation."

"But the SD-WAN enchantments..."

"SD-WAN provides intelligent routing, failover, and traffic management.
But the underlying roads are PUBLIC. Anyone with access to those roads
can observe what passes. Without encryption, your messages are readable
to any eavesdropper."

"So we need..."

"IPSec or TLS encryption for ALL traffic between towers. The SD-WAN
solution must encrypt everything that crosses the public network. This
is not optional - it's fundamental to the security model."

"What about the tower firewalls?"

"Keep them. SD-WAN provides connectivity, not comprehensive security.
Towers still need local protection. Defense in depth doesn't disappear
just because your WAN technology changed."

You have demonstrated understanding of SD-WAN SECURITY.
                """,
                "failure_texts": {
                    0: """
Branch towers absolutely still need firewalls! SD-WAN handles connectivity
between sites but doesn't replace local security controls. Each tower
still faces local threats and still needs firewall protection for its
network perimeter. Never remove firewalls just because you changed
WAN technology.
                    """,
                    2: """
SD-WAN provides intelligent network routing - it doesn't include antivirus
or anti-malware functionality. Endpoint protection is a separate concern.
Towers still need security software just like they did with MPLS. The
critical consideration is encryption for traffic crossing public networks.
                    """,
                    3: """
Towers absolutely need local security controls. SD-WAN provides WAN
connectivity but doesn't replace defense in depth. Each site needs
firewalls, endpoint protection, and appropriate security measures.
SD-WAN is about connectivity, not comprehensive security.
                    """
                }
            },
            "corporate": {
                "title": "THE MPLS MIGRATION",
                "narrative": """
Budget cuts have struck. The expensive MPLS circuits connecting your
branch offices are being replaced with SD-WAN over commodity internet
connections. The CFO is thrilled - costs drop by 60%.

"Same functionality for a fraction of the price!" the CFO announces.

The network team looks less thrilled. "MPLS was a private network. Our
traffic never touched the public internet. Now..."

"Now your traffic crosses networks you don't control," you finish.
"Public internet infrastructure. Shared with everyone."

The CISO needs to sign off on the migration. "What security considerations
are most critical for this change?"

What is the MOST critical security consideration when moving from MPLS
to internet-based SD-WAN?
                """,
                "choices": [
                    {"text": "SD-WAN eliminates all need for branch firewalls"},
                    {"text": "All SD-WAN traffic must be encrypted since it traverses public internet"},
                    {"text": "SD-WAN automatically provides antivirus protection"},
                    {"text": "Branch offices no longer need any local security controls"}
                ],
                "success_text": """
"Encryption is non-negotiable," you state firmly for the record.

"MPLS circuits were private - our traffic traveled on infrastructure we
controlled or that our provider isolated for us. Public internet has no
such guarantees. Traffic crosses unknown networks, potentially hostile
infrastructure."

"The SD-WAN vendor says it's secure..."

"SD-WAN provides intelligent routing, failover, quality of service. Those
are valuable. But if the traffic isn't encrypted, anyone along the path
can read it. The SD-WAN solution MUST include strong encryption - IPSec,
TLS, or equivalent - for all inter-site traffic."

"And the branch firewalls?"

"Keep them. SD-WAN doesn't replace local security. Each branch still
needs firewall protection, endpoint security, the whole stack. SD-WAN
changes how sites connect, not whether they need protection."

The migration proceeds with mandatory encryption and retained branch
security controls.

You have demonstrated understanding of SD-WAN SECURITY.
                """,
                "failure_texts": {
                    0: """
Branch offices absolutely still need firewalls. SD-WAN handles WAN
connectivity but doesn't replace local perimeter security. Each branch
still needs protection from local threats, proper access control, and
defense in depth. Removing firewalls because you changed WAN technology
would be a serious security regression.
                    """,
                    2: """
SD-WAN provides network connectivity features - routing, failover, QoS.
It does not include endpoint protection or antivirus functionality.
Those are separate security layers that branches still need. The critical
SD-WAN consideration is encrypting traffic that crosses public networks.
                    """,
                    3: """
Branches absolutely need local security controls. SD-WAN replaces your
WAN connectivity technology, not your entire security architecture.
Defense in depth still applies. The critical SD-WAN-specific concern is
encrypting traffic because it now crosses public networks instead of
private MPLS circuits.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Unlike private MPLS circuits, SD-WAN typically uses public internet
connections. All traffic between sites must be encrypted (IPSec, TLS)
to maintain confidentiality, as it traverses networks you don't control.
Branch offices still need local firewalls and security controls.
        """,
        "domain_reference": "Domain 4: Communication and Network Security - SD-WAN Security"
    },

    # Scenario 16: Microsegmentation
    {
        "id": "d4_microsegmentation",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE INNER SANCTUM'S DILEMMA",
                "narrative": """
The Citadel's magical compute crystals all reside in the same chamber.
Scrying crystals, calculation engines, and archive storage - all sharing
the same protected space. When one crystal was corrupted last month,
the infection spread to adjacent crystals before anyone noticed.

"We have network segments," the Crystal Master explains. "The chamber
is isolated from other parts of the Citadel. But WITHIN the chamber,
all crystals can communicate freely with each other."

"That's the problem. Your segmentation divides the Citadel into zones,
but within each zone, there are no barriers. Once something is inside
the zone, it can reach everything."

"We need barriers between individual crystals? That seems... extreme."

"It seems extreme until one corrupted crystal compromises your entire
archive because nothing prevented lateral movement within the zone."

What approach enables security policies between individual workloads
within the same network segment?
                """,
                "choices": [
                    {"text": "Add more network segments - divide the chamber into smaller zones"},
                    {"text": "Implement microsegmentation - apply policies at the individual crystal level"},
                    {"text": "Add additional perimeter barriers at the chamber entrance"},
                    {"text": "Use address translation to hide crystal locations from each other"}
                ],
                "success_text": """
"You need microsegmentation," you explain, projecting an illustration.
"Rather than dividing spaces into zones, you apply security policies to
each individual crystal."

"How is that different from more zones?"

"Zones are coarse-grained. You separate chambers, but everything in a
chamber can still talk freely. Microsegmentation is fine-grained - you
control which SPECIFIC crystals can communicate with which others, even
if they're in the same room."

"So the scrying crystal can only talk to specific calculation engines?"

"Exactly. And if an archive crystal is corrupted, it cannot spread to
scrying crystals because your policies say archive crystals don't talk
to scrying crystals. The corruption is contained to only the systems
it legitimately needs to access."

"This seems complex to manage."

"It is. But the alternative is losing everything when one crystal falls.
Microsegmentation provides the finest-grained lateral movement prevention
available."

You have demonstrated understanding of MICROSEGMENTATION.
                """,
                "failure_texts": {
                    0: """
More VLANs/zones still operate at the network segment level. Within each
segment, systems can communicate freely. Microsegmentation provides
per-workload policies, controlling communication between individual
systems even on the same network segment. It's finer-grained than any
VLAN-based approach.
                    """,
                    2: """
Perimeter firewalls control traffic entering and leaving a zone. They
don't control internal workload-to-workload communication. Once something
is inside, perimeter controls don't help. Microsegmentation applies
controls between individual workloads regardless of their network location.
                    """,
                    3: """
Network Address Translation translates between address spaces. It doesn't
enforce security policies between workloads. Systems can still communicate
through NAT - the addresses are just translated. Microsegmentation
provides actual access control between individual workloads.
                    """
                }
            },
            "corporate": {
                "title": "THE FLAT SEGMENT PROBLEM",
                "narrative": """
The security team is reviewing last month's breach. Attackers compromised
a development VM through a vulnerable application. From there, they moved
laterally to the CI/CD servers, then to production databases. All in the
same VLAN.

"But we have network segmentation!" the network architect protests.
"Dev is in its own VLAN!"

"The VLAN stopped them from reaching HR or Finance directly," you agree.
"But within the Dev VLAN, there are no restrictions. The compromised
dev VM could freely access CI/CD servers, which could access production
databases for deployments."

"So we need more VLANs? Separate the dev VMs from CI/CD from databases?"

"That helps, but you'll always have workloads that need to be on the
same segment for performance or management reasons. The question is: how
do you enforce policies between individual workloads, not just between
network segments?"

What approach enables this fine-grained control?
                """,
                "choices": [
                    {"text": "Add more VLANs to further divide the network"},
                    {"text": "Implement microsegmentation"},
                    {"text": "Install additional perimeter firewalls"},
                    {"text": "Use network address translation"}
                ],
                "success_text": """
"Microsegmentation," you explain, pulling up a diagram. "It applies
security policies at the individual workload level - per VM, per container,
per host - not just at network segment boundaries."

"How is that different from more VLANs?"

"VLANs are binary: same segment or different segment. Microsegmentation
is granular: THIS specific VM can talk to THAT specific VM on THESE
specific ports. Even systems on the same VLAN have policies between them."

"So we could say: dev VMs only talk to specific CI/CD servers on specific
ports, and CI/CD servers only talk to specific production systems for
deployments?"

"Exactly. And if a dev VM is compromised, it can't pivot to CI/CD servers
it has no legitimate reason to access, even though they're on the same
VLAN. The attacker is contained to only the systems the workload
legitimately needs."

The microsegmentation project launches the following quarter.

You have demonstrated understanding of MICROSEGMENTATION.
                """,
                "failure_texts": {
                    0: """
More VLANs operate at the network segment level. You can divide into
smaller segments, but within each segment, systems still communicate
freely. Microsegmentation provides per-workload policies regardless of
network location - it's fundamentally finer-grained than any VLAN
approach.
                    """,
                    2: """
Perimeter firewalls control traffic at network boundaries. They don't
govern workload-to-workload communication within a segment. Once an
attacker is inside a VLAN, perimeter controls at the VLAN edge don't
help. Microsegmentation applies controls between individual workloads.
                    """,
                    3: """
NAT translates addresses between networks. It doesn't enforce access
policies between workloads. Systems can still communicate through NAT -
the connection just gets address-translated. Microsegmentation provides
actual access control at the individual workload level.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
Microsegmentation applies security controls at the individual workload
level (per VM, container, or host), enabling policies between systems
even on the same network segment. This is finer-grained than traditional
VLAN-based segmentation, which only controls traffic between segments.
        """,
        "domain_reference": "Domain 4: Communication and Network Security - Microsegmentation"
    },

    # Scenario 17: Network Flow Analysis
    {
        "id": "d4_network_flow_analysis",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE PRIVACY PROBLEM",
                "narrative": """
The Citadel's security council faces a dilemma. Recent incidents suggest
data is being smuggled out of the archives, but the council cannot agree
on how to detect it.

"We should read all messages!" one councilor demands. "Inspect every
scroll for stolen secrets!"

"That violates the privacy of every scribe in the Citadel," another
objects. "We'd be reading personal correspondence, private matters,
everything. The scribes' guild would revolt."

"Then how do we detect the theft?"

You consider the problem. Full message inspection would reveal content -
but also invade privacy on a massive scale. What you really need is
metadata: who sends how much to whom, when, how often. Patterns that
might indicate data exfiltration without reading actual content.

What technology enables detecting unusual traffic patterns and potential
data exfiltration WITHOUT capturing full message contents?
                """,
                "choices": [
                    {"text": "Full message capture with deep content inspection"},
                    {"text": "Flow data analysis - metadata about communications without content"},
                    {"text": "Message mirroring to a surveillance chamber"},
                    {"text": "Installing scrying crystals on every desk in the Citadel"}
                ],
                "success_text": """
"You need flow analysis," you explain. "Think of it as analyzing the
outside of envelopes without reading the letters inside."

"What can we learn from envelopes?"

"Who sends to whom. How often. How much data. At what times. To what
destinations. This is metadata - information ABOUT communications, not
the content itself."

"And this helps detect theft?"

"Absolutely. An archivist who normally sends five small messages per day
suddenly sending gigabytes of data to an unknown external address? That's
a red flag. The pattern is suspicious even without reading the content."

"What about privacy?"

"Flow analysis doesn't capture message contents. The privacy council
accepts metadata collection where they'd reject content inspection. You
get detection capability without the privacy nightmare of reading
everyone's correspondence."

"NetFlow analysis provides pattern detection while respecting privacy
constraints."

You have demonstrated understanding of NETWORK FLOW ANALYSIS.
                """,
                "failure_texts": {
                    0: """
Full packet capture includes complete message contents - exactly the
privacy violation the council wants to avoid. Deep packet inspection
reads everything. Flow analysis captures metadata (source, destination,
ports, bytes, timing) WITHOUT capturing payload contents.
                    """,
                    2: """
Port mirroring copies ALL traffic, including content. This is the same
as full packet capture from a privacy perspective - you're duplicating
complete messages for analysis. Flow analysis captures only metadata,
not message contents.
                    """,
                    3: """
Wireshark and similar tools capture complete packets including content.
This is impractical at scale AND creates the same privacy issues as any
full-content capture. Flow analysis specifically avoids content capture
while still enabling pattern analysis.
                    """
                }
            },
            "corporate": {
                "title": "THE LEGAL CONSTRAINT",
                "narrative": """
The security team wants to detect data exfiltration. Legal has concerns.

"We can't capture full packet contents," the General Counsel states.
"Employee communications, personal data, protected information - if we
capture it all, we're liable for a massive privacy violation."

"But we need to detect unusual traffic patterns!" the security analyst
protests. "How do we know if someone's exfiltrating data if we can't
see the data?"

"You can't see the data. Find another way."

The CISO turns to you. "There must be a way to detect suspicious patterns
without capturing content. Something that gives us traffic metadata -
who's talking to whom, how much data, when - without the actual payload."

What technology meets these requirements?
                """,
                "choices": [
                    {"text": "Full packet capture with deep packet inspection"},
                    {"text": "NetFlow/IPFIX flow data analysis"},
                    {"text": "Port mirroring to a SIEM"},
                    {"text": "Deploy Wireshark on every network segment"}
                ],
                "success_text": """
"NetFlow or IPFIX," you explain. "Flow data captures metadata ABOUT
network connections without capturing the actual content."

"What exactly do we get?"

"Source and destination IP addresses. Source and destination ports.
Protocol used. Bytes transferred. Timing - when the flow started and
ended. Packet counts. All the metadata that describes a conversation
without the conversation itself."

"And this is enough to detect exfiltration?"

"Absolutely. A user suddenly uploading 50GB to an IP in a foreign country
at 2 AM? Suspicious pattern. Regular small transfers to a cloud storage
IP? Worth investigating. We see the shapes of suspicious behavior without
needing the content."

"Legal approves?"

"Metadata collection typically gets approval where content capture
doesn't. We can detect anomalies, investigate patterns, identify
potential exfiltration - all without reading anyone's email content."

You have demonstrated understanding of NETWORK FLOW ANALYSIS.
                """,
                "failure_texts": {
                    0: """
Full packet capture includes complete content - exactly what Legal
prohibited. Deep packet inspection reads payloads. Flow data analysis
specifically captures metadata (source, destination, ports, bytes)
WITHOUT payload content, avoiding the privacy concerns.
                    """,
                    2: """
Port mirroring copies complete traffic including content to the SIEM.
This is equivalent to full packet capture from a privacy perspective -
you're duplicating all network data. Flow analysis avoids content capture
entirely.
                    """,
                    3: """
Wireshark captures complete packets including all content. It's also
completely impractical at enterprise scale - you can't run packet capture
on every segment continuously. Flow data analysis is designed for scale
and specifically avoids content capture.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
NetFlow/IPFIX captures metadata about network flows (source, destination,
ports, bytes, timing) without capturing payload contents. This enables
traffic pattern analysis, anomaly detection, and exfiltration detection
while avoiding privacy concerns of full content capture.
        """,
        "domain_reference": "Domain 4: Communication and Network Security - Network Monitoring"
    },

    # Scenario 18: Secure Remote Access (SSH)
    {
        "id": "d4_secure_remote_access",
        "domain": 4,
        "themes": {
            "fantasy": {
                "title": "THE DISTANT TOWER ACCESS",
                "narrative": """
The Citadel's arcane scribes must access enchanted calculation engines
in distant towers. Currently, they speak a password phrase, and if it
matches, the tower grants entry. Simple, but problems have emerged.

"Our passwords travel across many lands to reach the towers," the Chief
Scribe explains. "Even with basic protection, a determined adversary
could intercept and reuse them. And scribes choose weak phrases - 'magic123'
was used by three people last month."

"We need something beyond passwords," you agree. "Something that cannot
be intercepted and reused. Something stronger than words a scribe can
remember."

"The towers support magical seal verification," the Scribe continues.
"Each authorized scribe could carry a unique sealed key, protected by
a personal phrase known only to them. The tower would verify both the
seal and... require the phrase to activate it?"

What approach improves SSH security beyond password authentication?
                """,
                "choices": [
                    {"text": "Change the entry port from standard to something obscure"},
                    {"text": "Implement key-based authentication with passphrase-protected keys"},
                    {"text": "Allow access from any origin location without restriction"},
                    {"text": "Remove the protection enchantments for faster access"}
                ],
                "success_text": """
"SSH key-based authentication with passphrases," you confirm. "This
provides two-factor protection far superior to passwords alone."

"Explain how it works."

"Each scribe generates a unique key pair - a private key they keep
secret, and a public key installed on authorized towers. The private
key is protected by a passphrase only the scribe knows."

"Two factors?"

"Something you HAVE - the private key file. Something you KNOW - the
passphrase. An attacker who steals the key file still needs the
passphrase. An attacker who guesses the passphrase still needs the
key file."

"And the keys themselves?"

"Far stronger than any password a human could remember. Keys are typically
thousands of bits long. Brute-forcing them is computationally infeasible.
And they're never transmitted - only cryptographic proof of possession
crosses the network."

"No more 'magic123' passwords?"

"No more passwords at all for SSH. Just secure keys and protected
passphrases."

You have demonstrated understanding of SECURE REMOTE ACCESS.
                """,
                "failure_texts": {
                    0: """
Changing SSH from port 22 to a non-standard port is 'security through
obscurity' - easily defeated. Port scanners trivially find SSH on any
port. Attackers specifically look for non-standard ports as a sign of
amateur security. Real security comes from strong authentication like
SSH keys.
                    """,
                    2: """
Allowing SSH from any IP address INCREASES attack surface dramatically.
Every scanner on the internet can probe your SSH service. IP restrictions
provide defense in depth - limiting who can even attempt authentication.
Combined with key-based auth, this significantly hardens SSH access.
                    """,
                    3: """
Disabling SSH encryption defeats the entire purpose of SSH! Without
encryption, credentials and session content are visible to any
eavesdropper. SSH exists to provide encrypted remote access. The goal
is stronger authentication (keys), not weaker encryption.
                    """
                }
            },
            "corporate": {
                "title": "THE SSH HARDENING PROJECT",
                "narrative": """
The security audit came back with findings about your SSH configuration.
Password authentication is enabled. Weak passwords are common. The
pen test team cracked three admin accounts with dictionary attacks.

"We need to harden SSH access," the IT manager acknowledges. "But our
admins are complaining that keys are 'too complicated' and they want
to keep passwords."

"The pen testers cracked their passwords in under an hour," you point
out. "Including root on the production database server."

The color drains from the manager's face.

"Keys are more secure," you continue. "And with proper implementation,
not that complicated. The question is: what specific improvement to SSH
provides the strongest security enhancement over simple passwords?"

What should be implemented?
                """,
                "choices": [
                    {"text": "Move SSH to a non-standard port"},
                    {"text": "Implement SSH key-based authentication with passphrase-protected keys"},
                    {"text": "Allow SSH access from any IP address"},
                    {"text": "Disable SSH encryption for better performance"}
                ],
                "success_text": """
"SSH key-based authentication with passphrase-protected keys," you
recommend. "Here's why it's dramatically more secure:

"First, keys are much longer than passwords. A 4096-bit RSA key versus
a 12-character password? No comparison. Brute-forcing keys is
computationally infeasible.

"Second, keys aren't vulnerable to phishing. Users don't type them,
so attackers can't trick them into revealing them.

"Third, passphrase protection adds a second factor. Even if an attacker
steals a key file, they need the passphrase to use it. Something you
have plus something you know."

"But the admins say it's complicated..."

"SSH agents cache unlocked keys in memory. Once you authenticate in the
morning, you don't type passphrases for every connection. It's actually
more convenient AND more secure once properly configured."

Password authentication is disabled the following month.

You have demonstrated understanding of SECURE REMOTE ACCESS.
                """,
                "failure_texts": {
                    0: """
Security through obscurity is not security. Port scanners find SSH on
any port in seconds. Attackers specifically target non-standard ports
because they often indicate weaker security awareness. Real SSH
hardening means key-based authentication, not port shuffling.
                    """,
                    2: """
Allowing SSH from any IP is the opposite of hardening! You're expanding
the attack surface to include every IP address on the internet. IP
restrictions limit who can even attempt authentication. Combined with
key-based auth, this provides defense in depth.
                    """,
                    3: """
Disabling encryption would make SSH pointless - you'd be sending
everything in cleartext! The goal is stronger authentication, not
weaker encryption. SSH keys provide dramatically stronger authentication
while maintaining full encryption.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 75,
        "hp_penalty": 25,
        "failure_text": """
SSH key-based authentication is significantly stronger than passwords.
Keys are much longer and not vulnerable to brute force or phishing.
Adding passphrases to keys provides two-factor protection: something you
have (the key file) plus something you know (the passphrase).
        """,
        "domain_reference": "Domain 4: Communication and Network Security - Secure Remote Access"
    },
]
