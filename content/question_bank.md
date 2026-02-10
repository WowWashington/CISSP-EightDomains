# CISSP Question Bank - Domains 3-8

This file contains theme-neutral questions that will be transformed into dual-theme scenarios (Fantasy and Corporate).

**Total Questions:** 108 (18 per domain × 6 domains)

---

# Domain 3: Security Architecture and Engineering

## Q3.01 - Defense in Depth
**Domain:** 3 - Security Architecture and Engineering
**Concept:** Defense in Depth / Layered Security
**Difficulty:** Easy

**Situation:** Your organization's security relies entirely on a single, highly advanced firewall at the network perimeter. A security consultant recommends implementing additional controls. What is the PRIMARY reason for this recommendation?

**Choices:**
1. The firewall vendor might go out of business
2. Single points of failure can be bypassed, leaving no additional protection
3. Multiple firewalls are always better than one
4. Compliance regulations require exactly three security layers

**Correct Answer:** 2

**Why Correct:** Defense in depth ensures that if one control fails or is bypassed, additional layers provide continued protection. Relying on a single control creates a single point of failure - once an attacker gets past it, there's nothing else stopping them.

**Why Others Wrong:**
- Choice 1: While vendor stability matters, it's not the primary security concern with single-layer defense
- Choice 3: Simply adding more of the same control doesn't provide defense in depth - you need diverse, complementary controls at different layers
- Choice 4: No regulation mandates exactly three layers; the principle is about multiple complementary controls, not a specific number

**Domain Reference:** Domain 3: Security Architecture and Engineering - Defense in Depth

---

## Q3.02 - Bell-LaPadula Model
**Domain:** 3 - Security Architecture and Engineering
**Concept:** Security Models - Bell-LaPadula (Confidentiality)
**Difficulty:** Medium

**Situation:** You're implementing an access control system for classified documents. Users with "Secret" clearance should be able to read "Confidential" documents but not "Top Secret" ones. They should only be able to write to documents at their own level or higher. Which security model principle applies?

**Choices:**
1. Biba Model - "No read down, no write up"
2. Bell-LaPadula Model - "No read up, no write down"
3. Clark-Wilson Model - Separation of duties
4. Brewer-Nash Model - Chinese Wall

**Correct Answer:** 2

**Why Correct:** Bell-LaPadula enforces confidentiality through "no read up" (can't read above your clearance) and "no write down" (can't write to lower classifications, preventing information leakage). This matches the scenario's requirements exactly.

**Why Others Wrong:**
- Choice 1: Biba focuses on integrity (opposite rules) - prevents corruption of higher-integrity data
- Choice 3: Clark-Wilson focuses on integrity through well-formed transactions and separation of duties, not classification levels
- Choice 4: Brewer-Nash (Chinese Wall) prevents conflicts of interest, not classification-based access

**Domain Reference:** Domain 3: Security Architecture and Engineering - Security Models

---

## Q3.03 - Symmetric vs Asymmetric Encryption
**Domain:** 3 - Security Architecture and Engineering
**Concept:** Cryptography Fundamentals
**Difficulty:** Easy

**Situation:** You need to establish secure communication with 100 different external partners. Each communication channel must be independently secured. Using symmetric encryption, how many unique keys would need to be managed?

**Choices:**
1. 100 keys (one per partner)
2. 200 keys (two per partner)
3. 4,950 keys (n(n-1)/2 formula)
4. 10,000 keys (n² formula)

**Correct Answer:** 1

**Why Correct:** For point-to-point communication with external partners (hub-and-spoke model), you need one symmetric key per partner relationship. Your organization shares one unique key with each of the 100 partners = 100 keys. The n(n-1)/2 formula applies only when all parties need to communicate with each other (full mesh).

**Why Others Wrong:**
- Choice 2: You don't need two keys per partner; one shared symmetric key handles both directions
- Choice 3: This formula (4,950) applies to full mesh communication where all 100 parties need to talk to each other - not hub-and-spoke
- Choice 4: The n² formula doesn't apply to symmetric key distribution in any standard model

**Domain Reference:** Domain 3: Security Architecture and Engineering - Cryptography

---

## Q3.04 - Hash Functions
**Domain:** 3 - Security Architecture and Engineering
**Concept:** Hash Functions and Integrity
**Difficulty:** Medium

**Situation:** A critical software update is being distributed. To ensure the file hasn't been tampered with during download, the vendor publishes a SHA-256 hash on their secure website. What security property does this verification provide?

**Choices:**
1. Confidentiality - the file contents are encrypted
2. Integrity - the file hasn't been modified
3. Authentication - the file is from the genuine vendor
4. Non-repudiation - the vendor cannot deny creating the file

**Correct Answer:** 2

**Why Correct:** Hash functions provide integrity verification. By comparing the computed hash of your downloaded file against the published hash, you can verify the file wasn't modified during transit. If even one bit changes, the hash will be completely different.

**Why Others Wrong:**
- Choice 1: Hashes don't encrypt anything - the file is transmitted in plaintext
- Choice 3: A hash alone doesn't prove authenticity - an attacker could publish both a malicious file AND its valid hash. Digital signatures (hash + private key) provide authentication
- Choice 4: Non-repudiation requires digital signatures with private keys, not just hashes

**Domain Reference:** Domain 3: Security Architecture and Engineering - Cryptographic Hash Functions

---

## Q3.05 - PKI Certificate Validation
**Domain:** 3 - Security Architecture and Engineering
**Concept:** PKI and Certificate Management
**Difficulty:** Medium

**Situation:** A user reports that their browser shows a certificate warning when accessing an internal application. Investigation reveals the certificate was issued by your organization's internal Certificate Authority (CA), which isn't in the browser's trust store. What is the BEST solution?

**Choices:**
1. Instruct users to click "proceed anyway" when they see the warning
2. Purchase a certificate from a public CA for the internal application
3. Deploy your internal CA's root certificate to all organization devices
4. Disable certificate validation for internal network traffic

**Correct Answer:** 3

**Why Correct:** Deploying your internal CA's root certificate to managed devices establishes trust properly. The browser will then validate certificates issued by your internal CA without warnings, maintaining security while enabling internal PKI use.

**Why Others Wrong:**
- Choice 1: Training users to ignore security warnings is dangerous - they'll ignore warnings for actual threats too
- Choice 2: Public CAs shouldn't issue certificates for internal-only resources; this exposes internal infrastructure details and may violate CA policies
- Choice 4: Disabling certificate validation removes protection against man-in-the-middle attacks entirely

**Domain Reference:** Domain 3: Security Architecture and Engineering - PKI and Certificate Management

---

## Q3.06 - Digital Signatures
**Domain:** 3 - Security Architecture and Engineering
**Concept:** Digital Signatures
**Difficulty:** Medium

**Situation:** A contract must be digitally signed to ensure authenticity and prevent the signer from later denying they signed it. Which cryptographic operation should be used?

**Choices:**
1. Encrypt the document with the signer's public key
2. Encrypt a hash of the document with the signer's private key
3. Encrypt the document with a symmetric key shared with the recipient
4. Compute a hash of the document and send it alongside

**Correct Answer:** 2

**Why Correct:** Digital signatures use the signer's private key to encrypt a hash of the document. Only the private key holder could create this signature (authentication), and the signature is bound to the exact document contents (integrity). The recipient verifies using the signer's public key.

**Why Others Wrong:**
- Choice 1: Encrypting with the recipient's public key provides confidentiality, not signatures - anyone could do this
- Choice 3: Symmetric encryption doesn't provide non-repudiation since both parties share the key
- Choice 4: A hash alone proves integrity but not who created it - no authentication or non-repudiation

**Domain Reference:** Domain 3: Security Architecture and Engineering - Digital Signatures

---

## Q3.07 - Physical Security Layers
**Domain:** 3 - Security Architecture and Engineering
**Concept:** Physical Security Controls
**Difficulty:** Easy

**Situation:** A new data center is being designed. Security zones are planned from the outer perimeter to the server room. What is the correct order of physical security layers from OUTERMOST to INNERMOST?

**Choices:**
1. Server cage → Building entrance → Parking lot → Data hall
2. Parking lot → Building entrance → Data hall → Server cage
3. Building entrance → Parking lot → Server cage → Data hall
4. Data hall → Server cage → Building entrance → Parking lot

**Correct Answer:** 2

**Why Correct:** Physical security uses concentric layers from outside to inside: perimeter (parking lot/fence) → building access → restricted areas (data hall) → high-security zones (individual server cages). Each layer requires passing through the previous one.

**Why Others Wrong:**
- Choice 1: Server cage is innermost, not outermost; this order is scrambled
- Choice 3: Parking lot should come before building entrance, not after
- Choice 4: This is completely reversed - data hall and server cage are innermost layers

**Domain Reference:** Domain 3: Security Architecture and Engineering - Physical Security

---

## Q3.08 - Fire Suppression Systems
**Domain:** 3 - Security Architecture and Engineering
**Concept:** Environmental Controls
**Difficulty:** Medium

**Situation:** A server room requires fire suppression that won't damage electronic equipment and allows personnel to safely evacuate. Which system is MOST appropriate?

**Choices:**
1. Wet pipe sprinkler system
2. Clean agent gas suppression (FM-200/Novec)
3. Dry chemical extinguisher system
4. CO2 flooding system

**Correct Answer:** 2

**Why Correct:** Clean agent systems like FM-200 or Novec 1230 suppress fires without damaging electronics (no water, no residue) and are safe for occupied spaces at design concentrations, allowing evacuation time. They're specifically designed for data centers and server rooms.

**Why Others Wrong:**
- Choice 1: Water damages electronics severely - inappropriate for server rooms
- Choice 3: Dry chemical leaves corrosive residue that damages sensitive electronics
- Choice 4: CO2 displaces oxygen and can be lethal to personnel - requires immediate evacuation and isn't ideal for occupied spaces

**Domain Reference:** Domain 3: Security Architecture and Engineering - Environmental Controls

---

## Q3.09 - Hardware Security Modules
**Domain:** 3 - Security Architecture and Engineering
**Concept:** Hardware Security (HSM)
**Difficulty:** Medium

**Situation:** Your organization processes payment card transactions and must protect cryptographic keys used for PIN encryption. Auditors require that keys never exist in plaintext outside of tamper-resistant hardware. What solution meets this requirement?

**Choices:**
1. Store keys in an encrypted database with strong access controls
2. Use a Hardware Security Module (HSM) for all key operations
3. Keep keys on encrypted USB drives in a physical safe
4. Implement software-based key encryption with regular rotation

**Correct Answer:** 2

**Why Correct:** HSMs are tamper-resistant hardware devices that perform cryptographic operations internally. Keys are generated, stored, and used within the HSM without ever being exposed in plaintext to the host system - meeting PCI DSS and similar requirements for payment security.

**Why Others Wrong:**
- Choice 1: Keys must be decrypted to use them, meaning they exist in plaintext in memory - doesn't meet the requirement
- Choice 3: Keys would need to be loaded into memory for use, exposing them in plaintext
- Choice 4: Software encryption still requires plaintext keys in memory during operations

**Domain Reference:** Domain 3: Security Architecture and Engineering - Hardware Security

---

## Q3.10 - Buffer Overflow Prevention
**Domain:** 3 - Security Architecture and Engineering
**Concept:** Vulnerability Types - Buffer Overflow
**Difficulty:** Hard

**Situation:** A legacy application is vulnerable to buffer overflow attacks. Rewriting the application isn't immediately feasible. Which combination of controls provides the BEST mitigation?

**Choices:**
1. Address Space Layout Randomization (ASLR) + Data Execution Prevention (DEP)
2. Intrusion Detection System (IDS) + Web Application Firewall (WAF)
3. Input validation at the web tier + Database encryption
4. Network segmentation + Endpoint antivirus

**Correct Answer:** 1

**Why Correct:** ASLR randomizes memory addresses, making it hard to predict where to inject code. DEP marks memory regions as non-executable, preventing injected code from running. Together, they significantly raise the bar for successful buffer overflow exploitation without code changes.

**Why Others Wrong:**
- Choice 2: IDS/WAF may detect some attacks but don't prevent exploitation if an attack gets through
- Choice 3: Input validation helps but doesn't protect against all overflow vectors; database encryption is unrelated
- Choice 4: Network segmentation limits lateral movement but doesn't prevent the initial exploit; AV may miss novel exploits

**Domain Reference:** Domain 3: Security Architecture and Engineering - Vulnerability Mitigation

---

## Q3.11 - Cloud Shared Responsibility
**Domain:** 3 - Security Architecture and Engineering
**Concept:** Cloud Security Models
**Difficulty:** Medium

**Situation:** Your organization is deploying a web application on Infrastructure as a Service (IaaS). In the shared responsibility model, which security control is the CUSTOMER'S responsibility?

**Choices:**
1. Physical security of the data center
2. Hypervisor patching and security
3. Operating system hardening and patching
4. Network infrastructure redundancy

**Correct Answer:** 3

**Why Correct:** In IaaS, the customer is responsible for everything "in" the cloud: operating systems, applications, data, and their configurations. The provider handles the infrastructure "of" the cloud: physical, network, and virtualization layers.

**Why Others Wrong:**
- Choice 1: Physical security is always the cloud provider's responsibility
- Choice 2: Hypervisor security is the provider's responsibility in IaaS
- Choice 4: Network infrastructure is provider responsibility; customer manages their virtual network configurations

**Domain Reference:** Domain 3: Security Architecture and Engineering - Cloud Security

---

## Q3.12 - Virtualization Security
**Domain:** 3 - Security Architecture and Engineering
**Concept:** Virtualization Security
**Difficulty:** Hard

**Situation:** A critical security vulnerability allows a process in one virtual machine to read memory from another VM on the same hypervisor. What type of attack is this?

**Choices:**
1. Container escape
2. VM escape / Hypervisor breakout
3. Side-channel attack
4. Privilege escalation

**Correct Answer:** 2

**Why Correct:** VM escape (or hypervisor breakout) occurs when code running in a VM can break out of its isolation to access the hypervisor or other VMs. This violates the fundamental security boundary that VMs are supposed to enforce.

**Why Others Wrong:**
- Choice 1: Container escape is specific to container technology, not VMs - different isolation mechanism
- Choice 3: Side-channel attacks extract information through indirect observations (timing, power), not direct memory access
- Choice 4: Privilege escalation is gaining higher privileges within a system, not crossing VM boundaries

**Domain Reference:** Domain 3: Security Architecture and Engineering - Virtualization Security

---

## Q3.13 - Zero Trust Principles
**Domain:** 3 - Security Architecture and Engineering
**Concept:** Zero Trust Architecture
**Difficulty:** Medium

**Situation:** Your organization is implementing Zero Trust architecture. A user on the corporate network attempts to access a sensitive application. Under Zero Trust principles, what should happen?

**Choices:**
1. Grant access automatically since they're on the trusted corporate network
2. Require authentication and verify device health before granting access
3. Deny access until a manager approves the request
4. Allow read-only access from the corporate network, full access from VPN

**Correct Answer:** 2

**Why Correct:** Zero Trust eliminates implicit trust based on network location. "Never trust, always verify" means every access request must be authenticated, authorized, and validated (including device posture) regardless of where it originates - even from inside the corporate network.

**Why Others Wrong:**
- Choice 1: This is the opposite of Zero Trust - it assumes network location implies trust
- Choice 3: Manager approval might be part of authorization but isn't the core Zero Trust principle
- Choice 4: Zero Trust doesn't grant different trust levels based on network location

**Domain Reference:** Domain 3: Security Architecture and Engineering - Zero Trust Architecture

---

## Q3.14 - Trusted Computing Base
**Domain:** 3 - Security Architecture and Engineering
**Concept:** Trusted Computing Base (TCB)
**Difficulty:** Hard

**Situation:** A security architect is designing a highly secure system. They aim to minimize the Trusted Computing Base (TCB). What is the PRIMARY reason for minimizing the TCB?

**Choices:**
1. Smaller systems are faster and more efficient
2. Fewer components mean lower licensing costs
3. A smaller TCB is easier to verify, audit, and secure
4. Regulatory compliance requires minimal system footprint

**Correct Answer:** 3

**Why Correct:** The TCB includes all hardware, firmware, and software critical to security. A smaller TCB has less code that needs to be trusted, making it easier to verify correctness, audit for vulnerabilities, and ensure security properties. Complexity is the enemy of security.

**Why Others Wrong:**
- Choice 1: Performance isn't the primary security motivation for minimizing TCB
- Choice 2: Cost reduction is a side benefit, not the security rationale
- Choice 4: No specific regulation mandates TCB size; it's a security design principle

**Domain Reference:** Domain 3: Security Architecture and Engineering - Trusted Computing Base

---

## Q3.15 - Common Criteria Evaluation
**Domain:** 3 - Security Architecture and Engineering
**Concept:** Security Evaluation Criteria
**Difficulty:** Hard

**Situation:** Your organization requires a firewall certified to Common Criteria Evaluation Assurance Level 4 (EAL4). What does EAL4 certification indicate?

**Choices:**
1. The firewall has no known vulnerabilities
2. The product was methodically designed, tested, and reviewed
3. The firewall passed penetration testing by government hackers
4. All source code was formally verified mathematically

**Correct Answer:** 2

**Why Correct:** EAL4 means "Methodically Designed, Tested, and Reviewed." It indicates rigorous development practices, design documentation, and independent testing. It's the highest level commonly achieved for commercial products without requiring specialized development techniques.

**Why Others Wrong:**
- Choice 1: No certification guarantees zero vulnerabilities; EAL4 indicates process rigor, not perfection
- Choice 3: EAL4 involves independent testing labs, not specifically government penetration testers
- Choice 4: Formal mathematical verification is EAL7 level, not EAL4

**Domain Reference:** Domain 3: Security Architecture and Engineering - Security Evaluation Criteria

---

## Q3.16 - Side-Channel Attacks
**Domain:** 3 - Security Architecture and Engineering
**Concept:** Side-Channel Attacks
**Difficulty:** Hard

**Situation:** Researchers demonstrate they can extract encryption keys by precisely measuring the time it takes a server to respond to different inputs. What type of attack is this?

**Choices:**
1. Brute force attack
2. Timing side-channel attack
3. SQL injection attack
4. Man-in-the-middle attack

**Correct Answer:** 2

**Why Correct:** Timing attacks are side-channel attacks that extract secrets by analyzing timing variations in operations. If cryptographic operations take different amounts of time based on key bits, attackers can deduce the key through careful measurement.

**Why Others Wrong:**
- Choice 1: Brute force tries all possible keys; this attack uses timing information instead
- Choice 3: SQL injection manipulates database queries; unrelated to timing analysis
- Choice 4: MITM intercepts communications; timing attacks work through normal observation

**Domain Reference:** Domain 3: Security Architecture and Engineering - Side-Channel Attacks

---

## Q3.17 - IoT Security Challenges
**Domain:** 3 - Security Architecture and Engineering
**Concept:** IoT/ICS Security
**Difficulty:** Medium

**Situation:** Your organization is deploying IoT sensors throughout manufacturing facilities. What is the GREATEST security challenge specific to IoT devices?

**Choices:**
1. IoT devices typically have limited resources for security controls
2. IoT devices are more expensive than traditional computers
3. IoT sensors cannot connect to corporate networks
4. IoT devices always require wired connections

**Correct Answer:** 1

**Why Correct:** IoT devices often have constrained CPU, memory, and power, limiting their ability to run robust security software, use strong encryption, or receive updates. This resource limitation is a fundamental challenge in IoT security architecture.

**Why Others Wrong:**
- Choice 2: IoT devices are typically cheaper, which is part of the problem (cost-cutting on security)
- Choice 3: IoT devices do connect to networks; that's actually a security concern
- Choice 4: Most IoT devices use wireless connectivity; wired isn't required

**Domain Reference:** Domain 3: Security Architecture and Engineering - IoT Security

---

## Q3.18 - Secure Design Principles
**Domain:** 3 - Security Architecture and Engineering
**Concept:** Secure Design Principles - Fail Secure
**Difficulty:** Medium

**Situation:** A building's electronic access control system loses power. What should happen to the doors according to fail-secure design principles for a data center?

**Choices:**
1. All doors should unlock to allow evacuation
2. All doors should remain locked to protect assets
3. Exterior doors should unlock; interior secure areas should remain locked
4. The system should switch to backup power indefinitely

**Correct Answer:** 3

**Why Correct:** Secure design balances safety and security. Exterior doors must allow egress (life safety - fail-safe), while interior high-security areas like data centers should remain locked (fail-secure) to protect assets. This layered approach addresses both requirements.

**Why Others Wrong:**
- Choice 1: Unlocking all doors compromises security of sensitive areas unnecessarily
- Choice 2: Locking all doors creates life safety hazards - people must be able to evacuate
- Choice 4: Backup power eventually fails; the design must handle complete power loss

**Domain Reference:** Domain 3: Security Architecture and Engineering - Secure Design Principles

---

# Domain 4: Communication and Network Security

## Q4.01 - OSI Model Layers
**Domain:** 4 - Communication and Network Security
**Concept:** OSI Model
**Difficulty:** Easy

**Situation:** A network engineer is troubleshooting connectivity issues. They can ping a server by IP address but cannot access it by hostname. At which OSI layer is the problem MOST likely occurring?

**Choices:**
1. Layer 1 - Physical
2. Layer 3 - Network
3. Layer 4 - Transport
4. Layer 7 - Application

**Correct Answer:** 4

**Why Correct:** DNS resolution (hostname to IP) operates at the Application layer (Layer 7). Since IP connectivity works (ping succeeds), layers 1-3 are functional. The problem is with DNS lookup, which is an application-layer service.

**Why Others Wrong:**
- Choice 1: Physical layer issues would prevent all connectivity, including ping
- Choice 3: Network layer (IP) is working since ping by IP succeeds
- Choice 3: Transport layer issues would affect both IP and hostname connectivity

**Domain Reference:** Domain 4: Communication and Network Security - OSI Model

---

## Q4.02 - Network Segmentation
**Domain:** 4 - Communication and Network Security
**Concept:** Network Segmentation (VLANs)
**Difficulty:** Medium

**Situation:** After a malware outbreak, investigation reveals the infection spread rapidly from the accounting department to R&D servers. Both segments are on the same network. What control would BEST prevent this lateral movement in the future?

**Choices:**
1. Install additional antivirus on all systems
2. Implement network segmentation with firewall rules between segments
3. Require stronger passwords for all users
4. Encrypt all network traffic with VPN

**Correct Answer:** 2

**Why Correct:** Network segmentation separates different departments/functions into distinct network zones with firewall rules controlling traffic between them. This limits lateral movement - even if accounting is compromised, firewall rules would block unauthorized access to R&D servers.

**Why Others Wrong:**
- Choice 1: Antivirus may catch malware but doesn't prevent lateral movement once a system is compromised
- Choice 3: Stronger passwords don't prevent malware spread through network vulnerabilities
- Choice 4: VPN encrypts traffic but doesn't restrict which systems can communicate with each other

**Domain Reference:** Domain 4: Communication and Network Security - Network Segmentation

---

## Q4.03 - Stateful Firewall
**Domain:** 4 - Communication and Network Security
**Concept:** Firewalls - Stateful Inspection
**Difficulty:** Medium

**Situation:** An attacker attempts to send packets that appear to be responses to connections that were never initiated from inside the network. What type of firewall would BEST detect and block this attack?

**Choices:**
1. Packet filtering firewall (stateless)
2. Stateful inspection firewall
3. Web application firewall (WAF)
4. Circuit-level gateway

**Correct Answer:** 2

**Why Correct:** Stateful firewalls track connection state (established, related, new). They recognize that "response" packets without a corresponding outbound request are illegitimate because there's no matching connection in the state table. Stateless firewalls only examine individual packets without connection context.

**Why Others Wrong:**
- Choice 1: Stateless packet filters examine each packet independently and can't detect packets claiming to be part of non-existent connections
- Choice 3: WAFs focus on HTTP/web application attacks, not TCP connection state spoofing
- Choice 4: Circuit-level gateways work at session layer and have limited packet inspection capabilities

**Domain Reference:** Domain 4: Communication and Network Security - Firewall Technologies

---

## Q4.04 - VPN Technologies
**Domain:** 4 - Communication and Network Security
**Concept:** VPN Technologies
**Difficulty:** Medium

**Situation:** Remote employees need secure access to internal resources. The solution must work from hotel networks, coffee shops, and home connections without requiring special client software beyond a web browser. Which VPN approach is MOST appropriate?

**Choices:**
1. IPSec tunnel mode VPN
2. SSL/TLS VPN (browser-based)
3. PPTP VPN
4. L2TP VPN without encryption

**Correct Answer:** 2

**Why Correct:** SSL/TLS VPNs can work through a standard web browser without installing specialized client software. They use HTTPS (port 443), which typically isn't blocked by hotel/cafe networks. This makes them ideal for diverse, uncontrolled network environments.

**Why Others Wrong:**
- Choice 1: IPSec typically requires client software and may be blocked by firewalls that don't allow ESP/AH protocols
- Choice 3: PPTP requires client software and has known security vulnerabilities; often blocked by networks
- Choice 4: L2TP without encryption provides no confidentiality - unsuitable for untrusted networks

**Domain Reference:** Domain 4: Communication and Network Security - VPN Technologies

---

## Q4.05 - Wireless Security
**Domain:** 4 - Communication and Network Security
**Concept:** Wireless Security
**Difficulty:** Medium

**Situation:** Users report that their laptops automatically connected to a network called "CompanyWifi" in the parking lot, but it wasn't the real corporate network. What type of attack is this?

**Choices:**
1. MAC spoofing attack
2. Evil twin / Rogue access point attack
3. Bluetooth hijacking
4. WPS PIN attack

**Correct Answer:** 2

**Why Correct:** An evil twin attack creates a fake access point with the same SSID as a legitimate network. Devices configured to auto-connect will join the malicious AP, allowing attackers to intercept traffic, steal credentials, or launch further attacks.

**Why Others Wrong:**
- Choice 1: MAC spoofing changes a device's MAC address but doesn't create a fake network
- Choice 3: Bluetooth hijacking targets Bluetooth connections, not WiFi
- Choice 4: WPS attacks target the WiFi Protected Setup feature to crack the real network's password

**Domain Reference:** Domain 4: Communication and Network Security - Wireless Security

---

## Q4.06 - DNS Security
**Domain:** 4 - Communication and Network Security
**Concept:** DNS Security
**Difficulty:** Medium

**Situation:** Users attempting to visit the legitimate banking website are redirected to a fake site, even though they typed the correct URL. Investigation reveals the DNS server returned a malicious IP address. What security measure would BEST prevent this?

**Choices:**
1. Install SSL certificates on the web server
2. Implement DNSSEC to validate DNS responses
3. Use a web application firewall
4. Enable MAC address filtering

**Correct Answer:** 2

**Why Correct:** DNSSEC (DNS Security Extensions) cryptographically signs DNS records, allowing clients to verify that responses are authentic and haven't been tampered with. This prevents DNS spoofing and cache poisoning attacks.

**Why Others Wrong:**
- Choice 1: SSL certificates authenticate the web server but don't prevent DNS redirection - users still go to the wrong IP
- Choice 3: WAF protects web applications, not DNS infrastructure
- Choice 4: MAC filtering controls network access, not DNS resolution

**Domain Reference:** Domain 4: Communication and Network Security - DNS Security

---

## Q4.07 - Email Security
**Domain:** 4 - Communication and Network Security
**Concept:** Email Security (SPF, DKIM, DMARC)
**Difficulty:** Hard

**Situation:** Your organization receives phishing emails that appear to come from your own domain (spoofed sender addresses). Which combination of controls would BEST prevent external attackers from spoofing your domain?

**Choices:**
1. Spam filter + antivirus scanning
2. SPF + DKIM + DMARC
3. SSL/TLS for email transmission
4. Email encryption with S/MIME

**Correct Answer:** 2

**Why Correct:** SPF validates which servers can send email for your domain. DKIM cryptographically signs emails proving origin. DMARC provides policy enforcement and reporting. Together, they allow receiving servers to reject spoofed emails claiming to be from your domain.

**Why Others Wrong:**
- Choice 1: Spam filters may catch some phishing but don't specifically prevent domain spoofing
- Choice 3: TLS encrypts email in transit but doesn't authenticate the sender domain
- Choice 4: S/MIME encrypts content and signs individual emails but doesn't prevent domain-level spoofing

**Domain Reference:** Domain 4: Communication and Network Security - Email Security

---

## Q4.08 - Man-in-the-Middle Attack
**Domain:** 4 - Communication and Network Security
**Concept:** Network Attacks - MITM
**Difficulty:** Medium

**Situation:** An attacker on the same network segment intercepts ARP requests and responds with their own MAC address, causing traffic intended for the gateway to route through their machine. What attack is this?

**Choices:**
1. DNS poisoning
2. ARP spoofing/poisoning
3. SYN flood attack
4. IP fragmentation attack

**Correct Answer:** 2

**Why Correct:** ARP spoofing (or ARP poisoning) involves sending fake ARP replies to associate the attacker's MAC address with legitimate IP addresses (like the gateway). This redirects traffic through the attacker's machine, enabling man-in-the-middle interception.

**Why Others Wrong:**
- Choice 1: DNS poisoning targets name resolution, not layer 2 ARP tables
- Choice 3: SYN flood is a denial-of-service attack, not traffic interception
- Choice 4: IP fragmentation attacks exploit packet reassembly, not address resolution

**Domain Reference:** Domain 4: Communication and Network Security - Network Attacks

---

## Q4.09 - IDS vs IPS
**Domain:** 4 - Communication and Network Security
**Concept:** IDS/IPS Systems
**Difficulty:** Easy

**Situation:** A security device detected malicious traffic and generated an alert, but the attack was still successful because the traffic wasn't blocked. What type of device was this, and what should be implemented instead?

**Choices:**
1. It was an IPS; implement a firewall instead
2. It was an IDS; implement an IPS for active blocking
3. It was a WAF; implement network segmentation instead
4. It was a firewall; implement an IDS for better detection

**Correct Answer:** 2

**Why Correct:** An Intrusion Detection System (IDS) monitors and alerts but doesn't block traffic. An Intrusion Prevention System (IPS) sits inline and can actively block detected threats. If detection occurred but blocking didn't, an IDS was in use.

**Why Others Wrong:**
- Choice 1: IPS would have blocked the traffic; the problem is having IDS instead of IPS
- Choice 3: WAF is specific to web applications; the scenario describes general intrusion detection
- Choice 4: Firewalls block based on rules, not behavioral detection; IDS provides detection, not blocking

**Domain Reference:** Domain 4: Communication and Network Security - IDS/IPS

---

## Q4.10 - Network Access Control
**Domain:** 4 - Communication and Network Security
**Concept:** NAC and 802.1X
**Difficulty:** Medium

**Situation:** A contractor connects their personal laptop to an office network jack. The network should verify the device's identity and security posture before granting access. What technology enables this?

**Choices:**
1. DHCP snooping
2. Port mirroring
3. 802.1X with NAC
4. MAC address table

**Correct Answer:** 3

**Why Correct:** 802.1X provides port-based network access control, requiring authentication before granting network access. Combined with NAC (Network Access Control), it can also verify device health/posture (patches, antivirus, compliance) before allowing connection.

**Why Others Wrong:**
- Choice 1: DHCP snooping prevents rogue DHCP servers but doesn't authenticate devices
- Choice 2: Port mirroring copies traffic for monitoring but doesn't control access
- Choice 4: MAC tables are used for switching decisions, not access control or authentication

**Domain Reference:** Domain 4: Communication and Network Security - Network Access Control

---

## Q4.11 - Secure Protocols
**Domain:** 4 - Communication and Network Security
**Concept:** Secure Protocols
**Difficulty:** Easy

**Situation:** A developer is building a system that needs to transfer files to a remote server. Security requirements mandate encryption of data in transit and server authentication. Which protocol is MOST appropriate?

**Choices:**
1. FTP (File Transfer Protocol)
2. TFTP (Trivial File Transfer Protocol)
3. SFTP (SSH File Transfer Protocol)
4. Telnet with file transfer commands

**Correct Answer:** 3

**Why Correct:** SFTP runs over SSH, providing encryption for data in transit and server authentication through SSH host keys. It meets both security requirements while providing full file transfer functionality.

**Why Others Wrong:**
- Choice 1: FTP transmits data and credentials in cleartext - no encryption
- Choice 2: TFTP has no authentication or encryption - designed for simple, trusted environments
- Choice 4: Telnet transmits everything in cleartext, including file contents

**Domain Reference:** Domain 4: Communication and Network Security - Secure Protocols

---

## Q4.12 - DDoS Mitigation
**Domain:** 4 - Communication and Network Security
**Concept:** DDoS Attacks
**Difficulty:** Medium

**Situation:** Your web application is experiencing a distributed denial-of-service attack with traffic volume exceeding your internet connection capacity. What is the MOST effective mitigation approach?

**Choices:**
1. Increase local firewall rules to block malicious IPs
2. Add more bandwidth to your internet connection
3. Use a cloud-based DDoS mitigation service
4. Enable rate limiting on your web server

**Correct Answer:** 3

**Why Correct:** Cloud-based DDoS mitigation services have massive capacity distributed globally. They absorb attack traffic at their edge locations before it reaches your network, handling volumes that would overwhelm any single-location defense.

**Why Others Wrong:**
- Choice 1: If traffic exceeds your connection capacity, packets are dropped before reaching your firewall
- Choice 2: Attackers can typically scale faster than you can buy bandwidth; not economically viable
- Choice 4: Rate limiting helps with application-layer attacks but can't stop volumetric attacks that saturate your connection

**Domain Reference:** Domain 4: Communication and Network Security - DDoS Mitigation

---

## Q4.13 - Load Balancing Security
**Domain:** 4 - Communication and Network Security
**Concept:** Load Balancing and HA
**Difficulty:** Medium

**Situation:** A load balancer distributes traffic across multiple web servers. To enable SSL/TLS inspection and web application firewall functionality on the load balancer, how should SSL/TLS be configured?

**Choices:**
1. SSL passthrough - encrypted end-to-end without inspection
2. SSL offloading/termination - decrypt at load balancer
3. Disable SSL entirely for better performance
4. Use different SSL certificates for each backend server

**Correct Answer:** 2

**Why Correct:** SSL offloading (termination) decrypts traffic at the load balancer, allowing it to inspect content, apply WAF rules, and make intelligent routing decisions. Traffic can be re-encrypted to backend servers if needed (SSL re-encryption).

**Why Others Wrong:**
- Choice 1: Passthrough maintains encryption but prevents the load balancer from inspecting traffic
- Choice 3: Disabling SSL removes security entirely - unacceptable for sensitive applications
- Choice 4: Different certificates per server doesn't enable inspection at the load balancer

**Domain Reference:** Domain 4: Communication and Network Security - Load Balancing

---

## Q4.14 - CDN Security
**Domain:** 4 - Communication and Network Security
**Concept:** CDN and Edge Security
**Difficulty:** Medium

**Situation:** Your organization uses a Content Delivery Network (CDN) for its public website. From a security perspective, what is a key benefit the CDN provides beyond performance?

**Choices:**
1. CDNs automatically encrypt all backend databases
2. CDN edge nodes absorb attack traffic and hide origin server IPs
3. CDNs eliminate the need for SSL certificates
4. CDNs provide automatic code vulnerability scanning

**Correct Answer:** 2

**Why Correct:** CDNs distribute traffic across many edge locations globally. During DDoS attacks, this distributed infrastructure absorbs malicious traffic. Additionally, properly configured CDNs hide origin server IP addresses, making direct attacks on your infrastructure harder.

**Why Others Wrong:**
- Choice 1: CDNs don't interact with databases; they cache and deliver content
- Choice 3: CDNs require SSL certificates (often provide them) but don't eliminate the need
- Choice 4: CDNs deliver content; code scanning is a separate function (SAST/DAST tools)

**Domain Reference:** Domain 4: Communication and Network Security - CDN Security

---

## Q4.15 - SD-WAN Security
**Domain:** 4 - Communication and Network Security
**Concept:** SD-WAN Security
**Difficulty:** Hard

**Situation:** Your organization is replacing traditional MPLS connections with SD-WAN for branch offices. What security consideration is MOST critical when using internet-based SD-WAN connections?

**Choices:**
1. SD-WAN eliminates all need for branch firewalls
2. All SD-WAN traffic must be encrypted since it traverses public internet
3. SD-WAN automatically provides antivirus protection
4. Branch offices no longer need any local security controls

**Correct Answer:** 2

**Why Correct:** Unlike private MPLS circuits, SD-WAN typically uses public internet connections. All traffic between sites must be encrypted (IPSec, TLS) to maintain confidentiality, as it traverses networks you don't control.

**Why Others Wrong:**
- Choice 1: Branch offices still need firewalls for local protection and internet access control
- Choice 3: SD-WAN handles connectivity, not endpoint protection
- Choice 4: Branches need local security; SD-WAN doesn't replace defense in depth

**Domain Reference:** Domain 4: Communication and Network Security - SD-WAN Security

---

## Q4.16 - Microsegmentation
**Domain:** 4 - Communication and Network Security
**Concept:** Microsegmentation
**Difficulty:** Hard

**Situation:** Traditional network segmentation divides the network into zones. Your security team wants to enforce security policies between individual workloads in the same network segment. What approach enables this?

**Choices:**
1. Add more VLANs
2. Implement microsegmentation
3. Install additional perimeter firewalls
4. Use network address translation

**Correct Answer:** 2

**Why Correct:** Microsegmentation applies security controls at the individual workload level (per VM, container, or host), enabling policies between systems even on the same network segment. This is finer-grained than traditional VLAN-based segmentation.

**Why Others Wrong:**
- Choice 1: More VLANs still operate at the network segment level, not between individual workloads within a segment
- Choice 3: Perimeter firewalls control traffic entering/leaving the network, not internal workload-to-workload communication
- Choice 4: NAT translates addresses but doesn't enforce security policies between workloads

**Domain Reference:** Domain 4: Communication and Network Security - Microsegmentation

---

## Q4.17 - Network Flow Analysis
**Domain:** 4 - Communication and Network Security
**Concept:** Network Monitoring and Flow Analysis
**Difficulty:** Medium

**Situation:** The security team needs to detect unusual traffic patterns and potential data exfiltration without capturing full packet contents (which would raise privacy concerns). What technology is MOST appropriate?

**Choices:**
1. Full packet capture with deep packet inspection
2. NetFlow/IPFIX flow data analysis
3. Port mirroring to a SIEM
4. Wireshark on every network segment

**Correct Answer:** 2

**Why Correct:** NetFlow/IPFIX captures metadata about network flows (source, destination, ports, bytes, timing) without capturing payload contents. This enables traffic pattern analysis, anomaly detection, and exfiltration detection while avoiding privacy concerns of full content capture.

**Why Others Wrong:**
- Choice 1: Full packet capture includes payload contents, raising the privacy concerns mentioned
- Choice 3: Port mirroring copies all traffic including content; still has privacy issues
- Choice 4: Wireshark captures full packets; also impractical at scale

**Domain Reference:** Domain 4: Communication and Network Security - Network Monitoring

---

## Q4.18 - Secure Remote Access
**Domain:** 4 - Communication and Network Security
**Concept:** Secure Remote Access
**Difficulty:** Medium

**Situation:** An organization allows remote access to internal servers via SSH. To improve security beyond password authentication, what should be implemented?

**Choices:**
1. Change SSH from port 22 to a non-standard port
2. Implement SSH key-based authentication with passphrase-protected keys
3. Allow SSH access from any IP address
4. Disable SSH encryption for better performance

**Correct Answer:** 2

**Why Correct:** SSH key-based authentication is significantly stronger than passwords - keys are much longer and not vulnerable to brute force or phishing. Adding passphrases to keys provides two-factor protection (something you have + something you know).

**Why Others Wrong:**
- Choice 1: Security through obscurity; port scanning easily finds SSH on non-standard ports
- Choice 3: Unrestricted access increases attack surface; source IP restrictions add defense in depth
- Choice 4: Disabling encryption defeats the purpose of SSH security entirely

**Domain Reference:** Domain 4: Communication and Network Security - Secure Remote Access

---

# Domain 5: Identity and Access Management (IAM)

## Q5.01 - Authentication Factors
**Domain:** 5 - Identity and Access Management
**Concept:** Authentication Factors
**Difficulty:** Easy

**Situation:** A system requires users to enter a password and then enter a code from a hardware token. What type of authentication is this?

**Choices:**
1. Single-factor authentication
2. Two-factor authentication
3. Biometric authentication
4. Risk-based authentication

**Correct Answer:** 2

**Why Correct:** This uses two different factors: something you know (password) and something you have (hardware token). Using two distinct factor types constitutes two-factor authentication (2FA), which is stronger than single-factor.

**Why Others Wrong:**
- Choice 1: Two factors are used, not one
- Choice 3: No biometrics (fingerprint, face, etc.) are involved
- Choice 4: Risk-based authentication adapts based on context; this scenario describes standard 2FA

**Domain Reference:** Domain 5: Identity and Access Management - Authentication Factors

---

## Q5.02 - Single Sign-On
**Domain:** 5 - Identity and Access Management
**Concept:** Single Sign-On (SSO)
**Difficulty:** Medium

**Situation:** After implementing SSO, users authenticate once and gain access to multiple applications. The security team is concerned about risk. What is the PRIMARY security concern with SSO?

**Choices:**
1. SSO makes applications slower
2. Compromised credentials grant access to all connected applications
3. SSO requires users to remember more passwords
4. SSO doesn't work with cloud applications

**Correct Answer:** 2

**Why Correct:** SSO creates a single point of compromise - if an attacker steals SSO credentials or session tokens, they gain access to ALL applications integrated with SSO, not just one. This requires strong authentication (MFA) and session management for the SSO system.

**Why Others Wrong:**
- Choice 1: SSO typically improves user experience, not degrades it
- Choice 3: SSO reduces passwords (users remember one, not many)
- Choice 4: Modern SSO (SAML, OIDC) works well with cloud applications

**Domain Reference:** Domain 5: Identity and Access Management - Single Sign-On

---

## Q5.03 - Federated Identity
**Domain:** 5 - Identity and Access Management
**Concept:** Federated Identity
**Difficulty:** Medium

**Situation:** Your organization needs to allow employees to access a partner company's application using their corporate credentials, without sharing the actual credentials with the partner. What should be implemented?

**Choices:**
1. Share a master password with the partner organization
2. Create duplicate accounts for users in the partner's system
3. Implement federated identity using SAML or OIDC
4. Give the partner access to your user database

**Correct Answer:** 3

**Why Correct:** Federated identity (using SAML, OAuth, or OIDC) allows users to authenticate with their home organization (Identity Provider) and access partner services (Service Providers) through trusted assertions/tokens, without sharing actual credentials with the partner.

**Why Others Wrong:**
- Choice 1: Sharing passwords is a fundamental security violation; no accountability or individual identity
- Choice 2: Duplicate accounts create management overhead and synchronization issues
- Choice 4: Exposing your user database to partners is a massive security risk

**Domain Reference:** Domain 5: Identity and Access Management - Federated Identity

---

## Q5.04 - Access Control Models
**Domain:** 5 - Identity and Access Management
**Concept:** Access Control Models - RBAC
**Difficulty:** Medium

**Situation:** A new employee joins the accounting department. They should automatically receive the same system access as other accountants. What access control model BEST supports this requirement?

**Choices:**
1. Discretionary Access Control (DAC)
2. Mandatory Access Control (MAC)
3. Role-Based Access Control (RBAC)
4. Rule-Based Access Control

**Correct Answer:** 3

**Why Correct:** RBAC assigns permissions to roles (like "Accountant"), and users are assigned to roles. New accountants automatically inherit all permissions associated with the Accountant role, making access management efficient and consistent.

**Why Others Wrong:**
- Choice 1: DAC requires resource owners to individually grant permissions to each new user
- Choice 2: MAC is based on security labels/classifications, not job functions
- Choice 4: Rule-based uses conditional rules (time, location), not job role groupings

**Domain Reference:** Domain 5: Identity and Access Management - Access Control Models

---

## Q5.05 - Principle of Least Privilege
**Domain:** 5 - Identity and Access Management
**Concept:** Least Privilege
**Difficulty:** Easy

**Situation:** A developer requests permanent administrator access to production servers "in case of emergencies." What is the BEST response based on least privilege principles?

**Choices:**
1. Grant the permanent admin access as requested
2. Deny all access to production systems for developers
3. Provide time-limited, just-in-time elevated access when needed
4. Grant read-only admin access permanently

**Correct Answer:** 3

**Why Correct:** Least privilege means granting minimum access needed for the minimum time needed. Just-in-time (JIT) access provides elevated privileges only when required, with automatic revocation, maintaining security while enabling necessary work.

**Why Others Wrong:**
- Choice 1: Permanent admin access violates least privilege; excess access increases risk
- Choice 2: Completely denying access may impair legitimate emergency response
- Choice 4: "Read-only admin" is contradictory; either unnecessary or insufficient

**Domain Reference:** Domain 5: Identity and Access Management - Least Privilege

---

## Q5.06 - Privileged Access Management
**Domain:** 5 - Identity and Access Management
**Concept:** Privileged Access Management (PAM)
**Difficulty:** Medium

**Situation:** System administrators currently know the passwords to all critical servers and use them directly. Audit findings require better control and accountability for privileged access. What solution addresses this?

**Choices:**
1. Require admins to change passwords monthly
2. Implement a PAM solution with password vaulting and session recording
3. Share one admin account among all administrators
4. Remove all administrator accounts

**Correct Answer:** 2

**Why Correct:** PAM solutions vault privileged credentials (admins don't know actual passwords), provide just-in-time checkout, record sessions for accountability, and automatically rotate passwords. This provides control and audit trails for privileged access.

**Why Others Wrong:**
- Choice 1: Password rotation alone doesn't address accountability or credential sharing
- Choice 3: Shared accounts eliminate individual accountability - opposite of the requirement
- Choice 4: Removing admin accounts would prevent necessary system administration

**Domain Reference:** Domain 5: Identity and Access Management - PAM

---

## Q5.07 - Account Lifecycle
**Domain:** 5 - Identity and Access Management
**Concept:** Account Lifecycle Management
**Difficulty:** Easy

**Situation:** An employee's last day is Friday. When should their access to corporate systems be terminated?

**Choices:**
1. Immediately when they give notice
2. On their last day, coordinated with their departure
3. One week after they leave, to ensure transition
4. Only when they request deactivation

**Correct Answer:** 2

**Why Correct:** Access should be terminated on the employee's last day, ideally coordinated with their physical departure. Premature revocation may prevent completion of duties; delayed revocation creates insider threat risk from former employees.

**Why Others Wrong:**
- Choice 1: May prevent completing necessary work during notice period
- Choice 3: Leaving access active after departure creates security risk - former employees shouldn't retain access
- Choice 4: Users should never control their own access termination; this is an organizational decision

**Domain Reference:** Domain 5: Identity and Access Management - Account Lifecycle

---

## Q5.08 - Identity Proofing
**Domain:** 5 - Identity and Access Management
**Concept:** Identity Proofing
**Difficulty:** Medium

**Situation:** Before issuing credentials for a high-security system, you need to verify that applicants are who they claim to be. What process is this?

**Choices:**
1. Authentication
2. Authorization
3. Identity proofing
4. Access certification

**Correct Answer:** 3

**Why Correct:** Identity proofing is the process of verifying a person's identity BEFORE credentials are issued. This might involve document verification, background checks, or in-person verification. Authentication uses credentials; proofing establishes identity to CREATE credentials.

**Why Others Wrong:**
- Choice 1: Authentication verifies identity using existing credentials; proofing happens before credentials exist
- Choice 2: Authorization determines what an authenticated user can access
- Choice 4: Access certification reviews existing access rights, not initial identity verification

**Domain Reference:** Domain 5: Identity and Access Management - Identity Proofing

---

## Q5.09 - Session Management
**Domain:** 5 - Identity and Access Management
**Concept:** Session Management
**Difficulty:** Medium

**Situation:** A user authenticates to a web application. After 15 minutes of inactivity, they find they're still logged in. What security control is missing?

**Choices:**
1. Password complexity requirements
2. Session timeout / idle timeout
3. Multi-factor authentication
4. Account lockout policy

**Correct Answer:** 2

**Why Correct:** Session timeout (idle timeout) automatically terminates sessions after a period of inactivity, reducing the window for session hijacking or unauthorized access if a user walks away from their workstation.

**Why Others Wrong:**
- Choice 1: Password complexity controls password strength, not session duration
- Choice 3: MFA strengthens initial authentication but doesn't address idle sessions
- Choice 4: Account lockout prevents brute force attacks, not unauthorized session persistence

**Domain Reference:** Domain 5: Identity and Access Management - Session Management

---

## Q5.10 - Access Recertification
**Domain:** 5 - Identity and Access Management
**Concept:** Access Review and Recertification
**Difficulty:** Medium

**Situation:** Auditors found that many users have access to systems they no longer need due to job changes. What process should be implemented to prevent this?

**Choices:**
1. More frequent password changes
2. Periodic access reviews/recertification
3. Stronger authentication requirements
4. Network segmentation

**Correct Answer:** 2

**Why Correct:** Access recertification requires managers to periodically review and confirm that their employees' access rights are still appropriate. This catches access that's no longer needed due to role changes and enforces least privilege over time.

**Why Others Wrong:**
- Choice 1: Password changes don't address whether users should have access
- Choice 3: Stronger authentication doesn't reduce excessive permissions
- Choice 4: Network segmentation controls network traffic, not user permissions

**Domain Reference:** Domain 5: Identity and Access Management - Access Recertification

---

## Q5.11 - Just-In-Time Access
**Domain:** 5 - Identity and Access Management
**Concept:** Just-In-Time Access
**Difficulty:** Medium

**Situation:** Developers need occasional access to production systems for troubleshooting but shouldn't have standing access. What approach implements this securely?

**Choices:**
1. Give all developers permanent production access
2. Require developers to create personal production accounts
3. Implement just-in-time access with time-limited approval workflow
4. Block all developer access to production

**Correct Answer:** 3

**Why Correct:** Just-in-time (JIT) access grants temporary, time-limited elevated access only when needed, with approval workflow and automatic expiration. This enables necessary work while maintaining least privilege.

**Why Others Wrong:**
- Choice 1: Permanent access violates least privilege; unnecessary standing risk
- Choice 2: Personal accounts bypass accountability and centralized control
- Choice 4: Completely blocking access may prevent necessary troubleshooting

**Domain Reference:** Domain 5: Identity and Access Management - Just-In-Time Access

---

## Q5.12 - Service Accounts
**Domain:** 5 - Identity and Access Management
**Concept:** Service Accounts and Non-Human Identities
**Difficulty:** Hard

**Situation:** An application uses a service account with a password to connect to a database. The password has never been changed and is stored in a configuration file. What is the BEST improvement?

**Choices:**
1. Change the password once per year
2. Use managed identities or certificate-based authentication without stored passwords
3. Encrypt the configuration file containing the password
4. Use a shorter, simpler password for ease of rotation

**Correct Answer:** 2

**Why Correct:** Managed identities (in cloud) or certificate-based authentication eliminate stored passwords entirely. The identity is tied to the compute resource, credentials are managed automatically, and there's no password to steal or rotate.

**Why Others Wrong:**
- Choice 1: Annual rotation still leaves passwords vulnerable to theft; doesn't address storage issue
- Choice 3: Encrypted config files still require storing and managing the encryption key; adds complexity
- Choice 4: Weaker passwords are easier to crack; opposite of security improvement

**Domain Reference:** Domain 5: Identity and Access Management - Service Accounts

---

## Q5.13 - Biometric Authentication
**Domain:** 5 - Identity and Access Management
**Concept:** Biometric Authentication
**Difficulty:** Medium

**Situation:** Your organization is implementing fingerprint authentication. What is a key concern about biometric credentials compared to passwords?

**Choices:**
1. Fingerprints are too easy to guess
2. Biometrics cannot be changed if compromised
3. Fingerprint scanners are too expensive
4. Biometrics require users to remember complex patterns

**Correct Answer:** 2

**Why Correct:** Unlike passwords, biometrics (fingerprints, face, iris) cannot be changed if compromised. If someone's fingerprint data is stolen, they can't get new fingerprints. This makes biometric database protection critical and argues for local-only biometric storage.

**Why Others Wrong:**
- Choice 1: Fingerprints have billions of possible patterns; not guessable like passwords
- Choice 3: Cost is a practical concern but not the key security issue
- Choice 4: Biometrics don't require memorization - that's their advantage

**Domain Reference:** Domain 5: Identity and Access Management - Biometric Authentication

---

## Q5.14 - Password Policies
**Domain:** 5 - Identity and Access Management
**Concept:** Password Policies
**Difficulty:** Medium

**Situation:** Your organization's password policy requires 8 characters, quarterly changes, and prohibits reusing the last 5 passwords. Users complain and write passwords on sticky notes. What change would BEST improve both security and usability?

**Choices:**
1. Reduce minimum length to 6 characters
2. Require monthly password changes instead of quarterly
3. Require longer passphrases with less frequent changes
4. Remove all password requirements

**Correct Answer:** 3

**Why Correct:** Modern guidance (NIST 800-63B) recommends longer passwords/passphrases with infrequent changes. Frequent rotation causes users to choose weak, predictable passwords or write them down. Longer passphrases are more secure and memorable.

**Why Others Wrong:**
- Choice 1: Shorter passwords are easier to crack; reduces security
- Choice 2: More frequent changes worsen the usability problem, leading to weaker passwords
- Choice 4: No requirements would result in very weak passwords being used

**Domain Reference:** Domain 5: Identity and Access Management - Password Policies

---

## Q5.15 - Directory Services
**Domain:** 5 - Identity and Access Management
**Concept:** Directory Services
**Difficulty:** Medium

**Situation:** An organization uses Active Directory for user management. A security assessment reveals that LDAP queries are transmitted in cleartext. What should be implemented?

**Choices:**
1. Disable LDAP entirely
2. Enable LDAPS (LDAP over SSL/TLS)
3. Use a different directory service
4. Store passwords in plaintext to avoid encryption issues

**Correct Answer:** 2

**Why Correct:** LDAPS encrypts LDAP communications using TLS, protecting credentials and directory information from network eavesdropping. This maintains AD functionality while adding transport security.

**Why Others Wrong:**
- Choice 1: Disabling LDAP would break AD-dependent applications
- Choice 3: Switching directory services doesn't inherently solve the cleartext problem
- Choice 4: Plaintext password storage is the worst possible approach - severe security violation

**Domain Reference:** Domain 5: Identity and Access Management - Directory Services

---

## Q5.16 - Attribute-Based Access Control
**Domain:** 5 - Identity and Access Management
**Concept:** ABAC
**Difficulty:** Hard

**Situation:** Access decisions need to consider multiple factors: user department, document classification, time of day, and user location. What access control model provides this flexibility?

**Choices:**
1. Role-Based Access Control (RBAC)
2. Discretionary Access Control (DAC)
3. Attribute-Based Access Control (ABAC)
4. Mandatory Access Control (MAC)

**Correct Answer:** 3

**Why Correct:** ABAC evaluates multiple attributes (subject attributes, resource attributes, environment attributes) to make access decisions. This enables policies like "Finance users can access Confidential-Finance documents during business hours from office locations."

**Why Others Wrong:**
- Choice 1: RBAC uses roles only; doesn't easily incorporate time, location, or resource classification
- Choice 2: DAC is based on resource ownership, not attribute evaluation
- Choice 3: MAC uses fixed security labels, not flexible attribute combinations

**Domain Reference:** Domain 5: Identity and Access Management - ABAC

---

## Q5.17 - Identity Governance
**Domain:** 5 - Identity and Access Management
**Concept:** Identity Governance
**Difficulty:** Hard

**Situation:** The organization struggles with orphaned accounts, excessive permissions, and no clear view of who has access to what. What solution addresses these governance challenges?

**Choices:**
1. Implement stronger password policies
2. Deploy an Identity Governance and Administration (IGA) solution
3. Add more firewalls
4. Require MFA for all applications

**Correct Answer:** 2

**Why Correct:** IGA solutions provide visibility into access across systems, automate access reviews, identify policy violations (orphaned accounts, excessive access), and manage the identity lifecycle. They address governance challenges holistically.

**Why Others Wrong:**
- Choice 1: Password policies don't address orphaned accounts or excessive permissions
- Choice 3: Firewalls control network traffic, not user access governance
- Choice 4: MFA strengthens authentication but doesn't address access governance issues

**Domain Reference:** Domain 5: Identity and Access Management - Identity Governance

---

## Q5.18 - Credential Stuffing Defense
**Domain:** 5 - Identity and Access Management
**Concept:** Credential Management
**Difficulty:** Medium

**Situation:** Attackers are using credentials stolen from other websites to attempt logins on your application. What is the MOST effective defense?

**Choices:**
1. Require longer passwords
2. Implement MFA and detect/block credential stuffing attempts
3. Change the login page URL
4. Disable the "forgot password" feature

**Correct Answer:** 2

**Why Correct:** MFA defeats credential stuffing because stolen passwords alone aren't sufficient. Additionally, implementing detection (unusual login patterns, known-breached credential checking) and blocking mechanisms (rate limiting, CAPTCHA) adds defense in depth.

**Why Others Wrong:**
- Choice 1: Longer passwords don't help if the exact credentials were stolen from elsewhere
- Choice 3: Security through obscurity; attackers easily find login pages
- Choice 4: Disabling password recovery creates usability issues without addressing credential stuffing

**Domain Reference:** Domain 5: Identity and Access Management - Credential Management

---

# Domain 6: Security Assessment and Testing

## Q6.01 - Vulnerability Assessment vs Penetration Testing
**Domain:** 6 - Security Assessment and Testing
**Concept:** VA vs Pen Testing
**Difficulty:** Easy

**Situation:** Management wants to understand the organization's security weaknesses but is concerned about potential system disruption. They want a comprehensive view with minimal risk. What should be performed?

**Choices:**
1. Full penetration test with exploitation
2. Vulnerability assessment (scanning without exploitation)
3. Red team exercise
4. Social engineering campaign

**Correct Answer:** 2

**Why Correct:** Vulnerability assessments identify weaknesses through scanning without attempting exploitation. This provides comprehensive visibility into vulnerabilities with minimal risk of system disruption. Penetration tests actively exploit vulnerabilities, which carries higher risk.

**Why Others Wrong:**
- Choice 1: Penetration tests with exploitation carry higher disruption risk
- Choice 3: Red team exercises are adversarial and may involve disruption
- Choice 4: Social engineering tests people, not systems, and doesn't provide comprehensive technical weakness inventory

**Domain Reference:** Domain 6: Security Assessment and Testing - Vulnerability Assessment

---

## Q6.02 - Penetration Test Types
**Domain:** 6 - Security Assessment and Testing
**Concept:** Pen Test Types (Black/White/Gray Box)
**Difficulty:** Medium

**Situation:** A penetration test is planned where testers will be given network diagrams, system documentation, and source code access. What type of test is this?

**Choices:**
1. Black box test
2. White box test
3. Gray box test
4. Blind test

**Correct Answer:** 2

**Why Correct:** White box (clear box) testing provides testers with full information including documentation, architecture, and even source code. This enables thorough testing of known systems and finds issues that black box testing might miss due to time constraints.

**Why Others Wrong:**
- Choice 1: Black box provides no information; testers simulate external attackers
- Choice 3: Gray box provides partial information (some knowledge, not full access)
- Choice 4: Blind testing is similar to black box - no information provided

**Domain Reference:** Domain 6: Security Assessment and Testing - Penetration Testing Types

---

## Q6.03 - Vulnerability Scanning
**Domain:** 6 - Security Assessment and Testing
**Concept:** Vulnerability Scanning
**Difficulty:** Easy

**Situation:** A vulnerability scan reports 500 critical findings. Upon investigation, 400 of them are false positives - the vulnerabilities don't actually exist on those systems. What should be done?

**Choices:**
1. Report all 500 as genuine findings
2. Ignore the entire scan since it's unreliable
3. Validate findings and tune the scanner to reduce false positives
4. Only fix the ones that seem most dangerous

**Correct Answer:** 3

**Why Correct:** Vulnerability scan results require validation. False positives are common due to version detection limitations or configuration differences. Proper validation confirms actual vulnerabilities, and scanner tuning (credentials, updated plugins, exclusions) improves accuracy.

**Why Others Wrong:**
- Choice 1: Reporting unvalidated findings wastes remediation effort and undermines credibility
- Choice 2: The scan still found 100 real issues; dismissing it entirely is dangerous
- Choice 4: "Seem most dangerous" is subjective; validation provides factual basis for prioritization

**Domain Reference:** Domain 6: Security Assessment and Testing - Vulnerability Scanning

---

## Q6.04 - Security Audit Types
**Domain:** 6 - Security Assessment and Testing
**Concept:** Security Audits
**Difficulty:** Medium

**Situation:** A regulatory requirement mandates an annual security audit by parties with no vested interest in the findings. What type of audit is required?

**Choices:**
1. Internal audit by the security team
2. Self-assessment by system owners
3. Independent third-party audit
4. Peer review by another department

**Correct Answer:** 3

**Why Correct:** "No vested interest" requires auditors who are organizationally independent and won't benefit from favorable findings. Third-party auditors (external firms) meet this independence requirement - they have no stake in the results.

**Why Others Wrong:**
- Choice 1: Internal auditors, while independent of operations, still work for the organization
- Choice 2: Self-assessments inherently have vested interest in positive outcomes
- Choice 4: Peer reviewers are internal and may have interdepartmental relationships affecting objectivity

**Domain Reference:** Domain 6: Security Assessment and Testing - Security Audits

---

## Q6.05 - Log Review
**Domain:** 6 - Security Assessment and Testing
**Concept:** Log Analysis
**Difficulty:** Medium

**Situation:** During log review, you notice a user account generating thousands of failed login attempts across multiple systems at 3 AM, when that employee doesn't work. What should this indicate?

**Choices:**
1. Normal automated system activity
2. The user forgot their password
3. Possible credential compromise or brute force attack
4. A logging system malfunction

**Correct Answer:** 3

**Why Correct:** Mass failed logins outside normal hours strongly suggests either credential stuffing (attacker trying stolen credentials), brute force attack, or compromised account being used for lateral movement. This requires immediate investigation.

**Why Others Wrong:**
- Choice 1: Legitimate automation uses service accounts and shouldn't fail repeatedly
- Choice 2: Forgetting a password doesn't cause thousands of attempts across multiple systems
- Choice 4: Logging malfunctions don't generate failed authentication events

**Domain Reference:** Domain 6: Security Assessment and Testing - Log Analysis

---

## Q6.06 - Static Code Analysis
**Domain:** 6 - Security Assessment and Testing
**Concept:** Code Review - Static Analysis
**Difficulty:** Medium

**Situation:** A development team wants to find security vulnerabilities in code before deployment, without executing the code. What type of testing should be used?

**Choices:**
1. Dynamic Application Security Testing (DAST)
2. Static Application Security Testing (SAST)
3. Penetration testing
4. Stress testing

**Correct Answer:** 2

**Why Correct:** SAST analyzes source code without executing it, finding vulnerabilities like SQL injection, buffer overflows, or hard-coded credentials by examining code patterns. It integrates into development pipelines for early detection.

**Why Others Wrong:**
- Choice 1: DAST tests running applications (dynamic = executing)
- Choice 3: Penetration testing tests deployed/running systems
- Choice 4: Stress testing evaluates performance under load, not security vulnerabilities

**Domain Reference:** Domain 6: Security Assessment and Testing - Static Analysis

---

## Q6.07 - Dynamic Testing
**Domain:** 6 - Security Assessment and Testing
**Concept:** Dynamic Application Security Testing
**Difficulty:** Medium

**Situation:** Security testing is needed against a running web application to find vulnerabilities that only manifest during execution, such as authentication flaws and session management issues. What approach is needed?

**Choices:**
1. Review the application source code
2. Perform dynamic application security testing (DAST)
3. Conduct a code review
4. Analyze the application design documents

**Correct Answer:** 2

**Why Correct:** DAST tests running applications by sending requests and analyzing responses, finding runtime vulnerabilities like authentication bypasses, session fixation, and configuration issues that can't be found by looking at code alone.

**Why Others Wrong:**
- Choice 1: Source code review (SAST) doesn't test runtime behavior
- Choice 3: Code review is static analysis, not runtime testing
- Choice 4: Design documents don't reveal implementation or configuration vulnerabilities

**Domain Reference:** Domain 6: Security Assessment and Testing - DAST

---

## Q6.08 - Compliance Testing
**Domain:** 6 - Security Assessment and Testing
**Concept:** Compliance Testing
**Difficulty:** Easy

**Situation:** Your organization processes credit card payments and must demonstrate adherence to PCI DSS requirements. What type of assessment demonstrates this compliance?

**Choices:**
1. General vulnerability scan
2. PCI DSS compliance assessment/audit
3. Performance load test
4. Usability assessment

**Correct Answer:** 2

**Why Correct:** Compliance assessments specifically evaluate adherence to regulatory or standard requirements (PCI DSS in this case). They verify that required controls are implemented and functioning according to the standard's specifications.

**Why Others Wrong:**
- Choice 1: General vulnerability scans don't map to specific compliance requirements
- Choice 3: Load testing evaluates performance, not security compliance
- Choice 4: Usability assessments focus on user experience, not security compliance

**Domain Reference:** Domain 6: Security Assessment and Testing - Compliance Testing

---

## Q6.09 - Security Metrics
**Domain:** 6 - Security Assessment and Testing
**Concept:** Security Metrics and KPIs
**Difficulty:** Medium

**Situation:** Management asks for metrics to understand vulnerability management effectiveness. Which metric BEST indicates remediation performance?

**Choices:**
1. Total number of vulnerabilities ever discovered
2. Mean time to remediate critical vulnerabilities
3. Number of security tools purchased
4. Size of the security team

**Correct Answer:** 2

**Why Correct:** Mean time to remediate (MTTR) for critical vulnerabilities measures how quickly dangerous issues are fixed - directly indicating remediation effectiveness. Lower MTTR means faster risk reduction.

**Why Others Wrong:**
- Choice 1: Total discoveries without context of remediation doesn't show effectiveness
- Choice 3: Tool count doesn't indicate program effectiveness
- Choice 4: Team size is an input metric, not an outcome metric

**Domain Reference:** Domain 6: Security Assessment and Testing - Security Metrics

---

## Q6.10 - Red Team vs Blue Team
**Domain:** 6 - Security Assessment and Testing
**Concept:** Red Team vs Blue Team
**Difficulty:** Medium

**Situation:** The security team wants to test both the organization's defenses AND the defensive team's detection and response capabilities. What type of exercise accomplishes this?

**Choices:**
1. Automated vulnerability scanning
2. Red team vs blue team exercise
3. Policy review
4. Control self-assessment

**Correct Answer:** 2

**Why Correct:** Red team (attackers) vs blue team (defenders) exercises test both technical controls AND human response capabilities. The red team attempts to achieve objectives while the blue team tries to detect, respond, and stop them.

**Why Others Wrong:**
- Choice 1: Automated scanning doesn't test human detection/response capabilities
- Choice 3: Policy review is documentation assessment, not active testing
- Choice 4: Self-assessments don't involve active attack simulation

**Domain Reference:** Domain 6: Security Assessment and Testing - Red Team / Blue Team

---

## Q6.11 - Bug Bounty Programs
**Domain:** 6 - Security Assessment and Testing
**Concept:** Bug Bounty Programs
**Difficulty:** Medium

**Situation:** Your organization wants continuous security testing from a diverse group of researchers worldwide, paying only when valid vulnerabilities are found. What program supports this?

**Choices:**
1. Annual penetration test contract
2. Bug bounty program
3. Internal security audit
4. Compliance certification

**Correct Answer:** 2

**Why Correct:** Bug bounty programs invite external researchers to find vulnerabilities, paying rewards ("bounties") only for valid findings. This provides continuous testing from diverse perspectives with pay-for-results economics.

**Why Others Wrong:**
- Choice 1: Annual contracts are periodic, not continuous, and pay regardless of findings
- Choice 3: Internal audits use internal staff, not external researchers worldwide
- Choice 4: Certifications are point-in-time assessments, not ongoing testing

**Domain Reference:** Domain 6: Security Assessment and Testing - Bug Bounty Programs

---

## Q6.12 - Tabletop Exercises
**Domain:** 6 - Security Assessment and Testing
**Concept:** Tabletop Exercises
**Difficulty:** Easy

**Situation:** The incident response team needs to practice handling a ransomware attack without affecting production systems. What type of exercise is MOST appropriate?

**Choices:**
1. Full-scale disaster recovery test
2. Tabletop exercise / walkthrough
3. Production penetration test
4. Automated backup restoration

**Correct Answer:** 2

**Why Correct:** Tabletop exercises are discussion-based walkthroughs where participants talk through their responses to hypothetical scenarios. No actual systems are affected, making them safe for practicing incident response.

**Why Others Wrong:**
- Choice 1: Full-scale DR tests may affect systems and are more complex to execute
- Choice 3: Penetration tests target real systems, potentially causing disruption
- Choice 4: Backup restoration tests recovery, not incident response procedures

**Domain Reference:** Domain 6: Security Assessment and Testing - Tabletop Exercises

---

## Q6.13 - Disaster Recovery Testing
**Domain:** 6 - Security Assessment and Testing
**Concept:** Disaster Recovery Testing
**Difficulty:** Medium

**Situation:** The DR plan says systems can be recovered in 4 hours (RTO). This has never been validated. What type of test BEST validates this claim?

**Choices:**
1. Review the DR documentation
2. Conduct a full-scale DR test with actual failover
3. Ask the IT team if they think it's achievable
4. Compare RTO to industry benchmarks

**Correct Answer:** 2

**Why Correct:** Only actual failover testing validates whether stated RTOs are achievable. Documentation review and opinions don't prove real-world recovery capability. Full-scale tests reveal gaps between plans and reality.

**Why Others Wrong:**
- Choice 1: Document review doesn't validate actual recovery capability
- Choice 3: Opinions aren't evidence of capability
- Choice 4: Benchmarks are comparisons, not validation of your specific capability

**Domain Reference:** Domain 6: Security Assessment and Testing - DR Testing

---

## Q6.14 - Control Testing
**Domain:** 6 - Security Assessment and Testing
**Concept:** Control Testing and Validation
**Difficulty:** Medium

**Situation:** The organization implemented a new firewall rule blocking outbound connections to known malicious IPs. How should this control be validated?

**Choices:**
1. Review the firewall configuration file
2. Test by attempting connections to known-bad IPs and verifying they're blocked
3. Ask the firewall administrator if it's working
4. Check if any malware infections occurred

**Correct Answer:** 2

**Why Correct:** Effective control testing requires actually testing the control. Attempting blocked connections and verifying they fail demonstrates the control works as intended - this is positive testing validation.

**Why Others Wrong:**
- Choice 1: Configuration review shows intent but doesn't prove operational effectiveness
- Choice 3: Administrator opinion isn't evidence of control effectiveness
- Choice 4: Absence of infections doesn't prove the specific control is working; other factors may be involved

**Domain Reference:** Domain 6: Security Assessment and Testing - Control Validation

---

## Q6.15 - Breach Attack Simulation
**Domain:** 6 - Security Assessment and Testing
**Concept:** Breach Attack Simulation
**Difficulty:** Hard

**Situation:** Your organization wants continuous automated testing that simulates real attack techniques across the kill chain to validate security controls. What solution provides this?

**Choices:**
1. Monthly vulnerability scans
2. Breach and Attack Simulation (BAS) platform
3. Annual penetration test
4. Antivirus software

**Correct Answer:** 2

**Why Correct:** BAS platforms continuously and automatically simulate attack techniques (MITRE ATT&CK framework) to test whether security controls detect and prevent them. They provide ongoing validation without manual testing effort.

**Why Others Wrong:**
- Choice 1: Vulnerability scans find known weaknesses but don't simulate attacks
- Choice 3: Annual tests are point-in-time; BAS provides continuous validation
- Choice 4: Antivirus is a control being tested, not a testing platform

**Domain Reference:** Domain 6: Security Assessment and Testing - Breach Attack Simulation

---

## Q6.16 - Software Composition Analysis
**Domain:** 6 - Security Assessment and Testing
**Concept:** Software Composition Analysis
**Difficulty:** Medium

**Situation:** Your development team uses many open-source libraries. You need to identify known vulnerabilities in these third-party components. What type of tool addresses this?

**Choices:**
1. Static Application Security Testing (SAST)
2. Software Composition Analysis (SCA)
3. Interactive Application Security Testing (IAST)
4. Web Application Firewall (WAF)

**Correct Answer:** 2

**Why Correct:** SCA tools analyze third-party dependencies (libraries, packages) to identify known vulnerabilities (CVEs) in those components. They maintain databases of vulnerable versions and alert when your project uses them.

**Why Others Wrong:**
- Choice 1: SAST analyzes your code, not third-party components
- Choice 3: IAST tests running applications, not dependency analysis
- Choice 4: WAF blocks attacks at runtime but doesn't analyze code composition

**Domain Reference:** Domain 6: Security Assessment and Testing - Software Composition Analysis

---

## Q6.17 - Continuous Security Testing
**Domain:** 6 - Security Assessment and Testing
**Concept:** Continuous Security Testing
**Difficulty:** Medium

**Situation:** Security testing currently happens only before major releases. Development teams want to find issues earlier. What approach integrates security testing into the development pipeline?

**Choices:**
1. More frequent annual audits
2. Integrate SAST/DAST into CI/CD pipeline
3. Hire more security auditors
4. Delay releases until security approves

**Correct Answer:** 2

**Why Correct:** Integrating security testing (SAST, DAST, SCA) into CI/CD pipelines provides continuous, automated security feedback. Developers find issues immediately when code is committed, enabling faster remediation.

**Why Others Wrong:**
- Choice 1: Annual audits, even if more frequent, don't provide continuous feedback
- Choice 3: More auditors don't address the timing issue; testing still happens late
- Choice 4: Delays don't shift testing left; they slow delivery without improving timing

**Domain Reference:** Domain 6: Security Assessment and Testing - Continuous Security Testing

---

## Q6.18 - Reporting and Remediation Tracking
**Domain:** 6 - Security Assessment and Testing
**Concept:** Reporting and Remediation
**Difficulty:** Easy

**Situation:** A penetration test identified 50 vulnerabilities three months ago. Management wants to know the current status. What should be provided?

**Choices:**
1. The original penetration test report
2. Remediation status report showing which findings are fixed, in progress, or open
3. A new penetration test
4. Verbal assurance that everything is fine

**Correct Answer:** 2

**Why Correct:** A remediation status report tracks the current state of each finding - fixed, in progress, risk-accepted, or still open. This provides the accountability and visibility management needs.

**Why Others Wrong:**
- Choice 1: The original report is outdated; it doesn't show current remediation status
- Choice 3: A new test would find new issues but doesn't report on remediation of known issues
- Choice 4: Verbal assurance lacks documentation and accountability

**Domain Reference:** Domain 6: Security Assessment and Testing - Remediation Tracking

---

# Domain 7: Security Operations

## Q7.01 - Incident Response Lifecycle
**Domain:** 7 - Security Operations
**Concept:** Incident Response Lifecycle
**Difficulty:** Medium

**Situation:** A security incident has been detected. The response team has identified affected systems. What is the NEXT phase in the standard incident response lifecycle?

**Choices:**
1. Preparation
2. Lessons learned / Post-incident review
3. Containment, eradication, and recovery
4. Detection and analysis

**Correct Answer:** 3

**Why Correct:** The incident response lifecycle is: Preparation → Detection/Analysis → Containment/Eradication/Recovery → Post-Incident. After detection and identifying affected systems (analysis), the next phase is containment to stop the spread.

**Why Others Wrong:**
- Choice 1: Preparation happens before incidents occur
- Choice 2: Lessons learned is the final phase, after recovery
- Choice 4: Detection and analysis was just completed per the scenario

**Domain Reference:** Domain 7: Security Operations - Incident Response Lifecycle

---

## Q7.02 - Evidence Handling
**Domain:** 7 - Security Operations
**Concept:** Evidence Handling and Chain of Custody
**Difficulty:** Medium

**Situation:** During a forensic investigation, you need to ensure that collected evidence can be used in legal proceedings. What documentation is ESSENTIAL?

**Choices:**
1. Employee performance reviews
2. Chain of custody documentation
3. Annual budget reports
4. Vendor contracts

**Correct Answer:** 2

**Why Correct:** Chain of custody documents everyone who handled the evidence, when, why, and what they did with it. This proves evidence integrity and is required for legal admissibility - it shows evidence wasn't tampered with.

**Why Others Wrong:**
- Choice 1: Performance reviews are unrelated to evidence handling
- Choice 3: Budget reports don't establish evidence integrity
- Choice 4: Vendor contracts don't document evidence handling

**Domain Reference:** Domain 7: Security Operations - Chain of Custody

---

## Q7.03 - Digital Forensics
**Domain:** 7 - Security Operations
**Concept:** Digital Forensics Fundamentals
**Difficulty:** Medium

**Situation:** A hard drive needs to be examined as part of an investigation. What should be done FIRST to preserve evidence integrity?

**Choices:**
1. Open files directly on the original drive to review them
2. Create a forensic image (bit-for-bit copy) of the drive
3. Delete suspicious files to prevent further damage
4. Format the drive and install analysis tools

**Correct Answer:** 2

**Why Correct:** Creating a forensic image preserves the original evidence in pristine condition. All analysis is performed on the copy, ensuring the original can always be verified and maintaining evidence integrity for legal proceedings.

**Why Others Wrong:**
- Choice 1: Direct access modifies timestamps and metadata, compromising evidence
- Choice 3: Deleting files destroys evidence permanently
- Choice 4: Formatting destroys all evidence

**Domain Reference:** Domain 7: Security Operations - Digital Forensics

---

## Q7.04 - SIEM Operations
**Domain:** 7 - Security Operations
**Concept:** SIEM and Log Management
**Difficulty:** Medium

**Situation:** Multiple systems generate security logs, but analysts struggle to correlate events across systems and identify attack patterns. What solution addresses this?

**Choices:**
1. Delete older logs to reduce volume
2. Implement a SIEM for centralized log correlation
3. Disable logging on less critical systems
4. Email all logs to the security team

**Correct Answer:** 2

**Why Correct:** SIEM (Security Information and Event Management) collects logs centrally, normalizes them, and correlates events across systems to identify patterns and attacks that individual logs wouldn't reveal. This is exactly what the scenario needs.

**Why Others Wrong:**
- Choice 1: Deleting logs loses visibility and may violate retention requirements
- Choice 3: Disabling logging reduces visibility; attackers target "less critical" systems
- Choice 4: Email can't correlate or analyze logs effectively

**Domain Reference:** Domain 7: Security Operations - SIEM

---

## Q7.05 - Threat Intelligence
**Domain:** 7 - Security Operations
**Concept:** Threat Intelligence
**Difficulty:** Medium

**Situation:** Your security team wants to proactively block connections to known malicious infrastructure before attacks occur. What should be implemented?

**Choices:**
1. Reactive incident response only
2. Threat intelligence feeds integrated with security controls
3. Remove all internet connectivity
4. Ignore external threats and focus on insiders

**Correct Answer:** 2

**Why Correct:** Threat intelligence feeds provide indicators of compromise (IPs, domains, hashes) of known threats. Integrating these with firewalls, proxies, and EDR enables proactive blocking of known-bad infrastructure before attacks succeed.

**Why Others Wrong:**
- Choice 1: Reactive only means waiting until attacks succeed
- Choice 3: Removing internet isn't feasible for most organizations
- Choice 4: External threats are significant; ignoring them is dangerous

**Domain Reference:** Domain 7: Security Operations - Threat Intelligence

---

## Q7.06 - Malware Analysis
**Domain:** 7 - Security Operations
**Concept:** Malware Analysis
**Difficulty:** Hard

**Situation:** A suspicious executable was found on a workstation. The security team wants to understand its behavior without risking infection of other systems. How should this be analyzed?

**Choices:**
1. Run it on a production workstation and observe
2. Execute it in an isolated sandbox environment
3. Email it to colleagues to see if their antivirus detects it
4. Delete it immediately without analysis

**Correct Answer:** 2

**Why Correct:** Sandbox environments are isolated (often virtual) systems where malware can be safely executed and observed. The sandbox captures behavior (file changes, network connections, registry modifications) without risk to production systems.

**Why Others Wrong:**
- Choice 1: Running on production risks infection spread
- Choice 3: Emailing potential malware could infect colleagues and violates security practices
- Choice 4: Deletion without analysis loses intelligence about the threat

**Domain Reference:** Domain 7: Security Operations - Malware Analysis

---

## Q7.07 - Patch Management
**Domain:** 7 - Security Operations
**Concept:** Patch Management
**Difficulty:** Easy

**Situation:** A critical security patch is released for a vulnerability being actively exploited. However, the standard change process requires 2-week testing. What is the BEST approach?

**Choices:**
1. Strictly follow the 2-week process regardless of risk
2. Use emergency change procedures to expedite critical patches
3. Ignore the patch since testing isn't complete
4. Apply the patch to production immediately without any testing

**Correct Answer:** 2

**Why Correct:** Organizations should have emergency change procedures for critical situations. These allow expedited approval and testing while maintaining appropriate controls. Actively exploited vulnerabilities warrant emergency procedures.

**Why Others Wrong:**
- Choice 1: Rigid process adherence during active exploitation increases risk unnecessarily
- Choice 3: Ignoring patches for actively exploited vulnerabilities is dangerous
- Choice 4: No testing at all risks causing outages; emergency procedures still include abbreviated testing

**Domain Reference:** Domain 7: Security Operations - Patch Management

---

## Q7.08 - Change Management
**Domain:** 7 - Security Operations
**Concept:** Change Management
**Difficulty:** Easy

**Situation:** An administrator makes a firewall change that accidentally blocks critical business traffic. This happened because the change wasn't reviewed or approved. What control failure does this represent?

**Choices:**
1. Incident response failure
2. Change management failure
3. Access control failure
4. Encryption failure

**Correct Answer:** 2

**Why Correct:** Change management requires changes to be reviewed, approved, tested, and documented before implementation. Unapproved changes bypass these controls and can cause outages - exactly what happened here.

**Why Others Wrong:**
- Choice 1: Incident response handles events after they occur; this is about prevention
- Choice 3: Access control determines who can make changes, not whether changes are appropriate
- Choice 4: Encryption is unrelated to change approval processes

**Domain Reference:** Domain 7: Security Operations - Change Management

---

## Q7.09 - Configuration Management
**Domain:** 7 - Security Operations
**Concept:** Configuration Management
**Difficulty:** Medium

**Situation:** An audit reveals that servers have inconsistent configurations - some have unnecessary services enabled, others have outdated settings. What should be implemented?

**Choices:**
1. Rebuild all servers from scratch
2. Implement configuration management with defined baselines
3. Document current configurations as-is
4. Allow each administrator to configure systems their preferred way

**Correct Answer:** 2

**Why Correct:** Configuration management defines standard baselines and uses automation to ensure consistency. Systems are configured according to approved standards and drift is detected and corrected automatically.

**Why Others Wrong:**
- Choice 1: Rebuilding is expensive and doesn't prevent future drift without proper management
- Choice 3: Documenting inconsistent configs doesn't fix the problem
- Choice 4: Individual preferences cause the inconsistency problem

**Domain Reference:** Domain 7: Security Operations - Configuration Management

---

## Q7.10 - Business Continuity
**Domain:** 7 - Security Operations
**Concept:** Business Continuity Operations
**Difficulty:** Medium

**Situation:** A data center experiences complete power failure. The business continuity plan activates operations at an alternate site. What type of site allows IMMEDIATE failover with no data loss?

**Choices:**
1. Cold site
2. Warm site
3. Hot site with synchronous replication
4. Mobile site

**Correct Answer:** 3

**Why Correct:** Hot sites are fully equipped and running, with synchronous replication ensuring data is identical in real-time. Failover is immediate with zero data loss (RPO=0). This is the most expensive but provides the fastest recovery.

**Why Others Wrong:**
- Choice 1: Cold sites have space and power but no equipment; days to become operational
- Choice 2: Warm sites have some equipment but aren't current; hours to become operational
- Choice 4: Mobile sites are transportable but take time to deploy

**Domain Reference:** Domain 7: Security Operations - Business Continuity

---

## Q7.11 - Disaster Recovery
**Domain:** 7 - Security Operations
**Concept:** Disaster Recovery Procedures
**Difficulty:** Medium

**Situation:** The Recovery Time Objective (RTO) is 4 hours and Recovery Point Objective (RPO) is 1 hour. What do these mean?

**Choices:**
1. RTO: how often to test recovery; RPO: how often to backup
2. RTO: maximum acceptable downtime; RPO: maximum acceptable data loss
3. RTO: time to detect disasters; RPO: time to notify staff
4. RTO: budget for recovery; RPO: budget for backups

**Correct Answer:** 2

**Why Correct:** RTO (Recovery Time Objective) is the maximum time systems can be down. RPO (Recovery Point Objective) is the maximum acceptable data loss, measured in time (1-hour RPO means losing up to 1 hour of data is acceptable).

**Why Others Wrong:**
- Choice 1: These are objectives for recovery, not testing or backup frequency
- Choice 3: RTO and RPO define recovery goals, not detection or notification times
- Choice 4: These are time-based objectives, not budget metrics

**Domain Reference:** Domain 7: Security Operations - Disaster Recovery

---

## Q7.12 - Physical Security Operations
**Domain:** 7 - Security Operations
**Concept:** Physical Security Operations
**Difficulty:** Easy

**Situation:** A visitor tailgates through a secure door behind an authorized employee. What control BEST prevents this?

**Choices:**
1. Installing additional cameras
2. Implementing a mantrap/airlock entry system
3. Posting "No Tailgating" signs
4. Requiring stronger passwords

**Correct Answer:** 2

**Why Correct:** Mantraps (airlocks) are enclosed entry systems where only one door opens at a time, ensuring only one person passes per authentication. This physically prevents tailgating by design.

**Why Others Wrong:**
- Choice 1: Cameras detect tailgating but don't prevent it
- Choice 3: Signs are awareness measures; determined violators ignore them
- Choice 4: Passwords are logical controls unrelated to physical tailgating

**Domain Reference:** Domain 7: Security Operations - Physical Security

---

## Q7.13 - Personnel Security
**Domain:** 7 - Security Operations
**Concept:** Personnel Security
**Difficulty:** Medium

**Situation:** An employee with access to financial systems has been exhibiting signs of financial stress and has been working unusual hours. What security principle addresses this risk?

**Choices:**
1. Mandatory vacations
2. Immediately terminate the employee
3. Remove all access permanently
4. Ignore personal issues as not security-relevant

**Correct Answer:** 1

**Why Correct:** Mandatory vacations force employees to be away while others perform their duties, potentially revealing fraud or unauthorized activities. Combined with job rotation, this is a detective control for insider threats. It addresses the situation without unfair immediate action.

**Why Others Wrong:**
- Choice 2: Immediate termination based on personal circumstances would be unfair and potentially illegal
- Choice 3: Complete access removal without evidence is excessive
- Choice 4: Personal circumstances can indicate insider threat risk; ignoring them is negligent

**Domain Reference:** Domain 7: Security Operations - Personnel Security

---

## Q7.14 - Media Sanitization
**Domain:** 7 - Security Operations
**Concept:** Media Management and Sanitization
**Difficulty:** Medium

**Situation:** Old hard drives containing sensitive customer data are being decommissioned. The drives will be sold or donated. What sanitization method ensures data cannot be recovered?

**Choices:**
1. Quick format of the drives
2. Deleting all files and emptying recycle bin
3. Degaussing or physical destruction
4. Removing the drive label

**Correct Answer:** 3

**Why Correct:** Degaussing (for magnetic media) or physical destruction (shredding) ensures data is unrecoverable. These methods meet DoD and NIST standards for media sanitization of sensitive data before disposal or reuse.

**Why Others Wrong:**
- Choice 1: Quick format only clears file tables; data is fully recoverable
- Choice 2: File deletion doesn't remove data from disk; easily recovered
- Choice 4: Label removal has nothing to do with data sanitization

**Domain Reference:** Domain 7: Security Operations - Media Sanitization

---

## Q7.15 - Investigations
**Domain:** 7 - Security Operations
**Concept:** Investigations and E-Discovery
**Difficulty:** Hard

**Situation:** The legal department notifies IT of upcoming litigation requiring preservation of all emails from certain employees. What is IT's IMMEDIATE obligation?

**Choices:**
1. Delete the emails to protect employee privacy
2. Issue a legal hold to preserve relevant data
3. Continue normal retention policies
4. Let the legal department handle it without IT involvement

**Correct Answer:** 2

**Why Correct:** Legal hold (litigation hold) suspends normal data destruction and requires preservation of potentially relevant evidence. Failure to preserve data after legal hold notice can result in severe sanctions for spoliation of evidence.

**Why Others Wrong:**
- Choice 1: Deleting data after litigation notice is spoliation - a serious offense
- Choice 3: Normal retention might delete relevant data, violating legal obligations
- Choice 4: IT controls the data; they must implement the preservation

**Domain Reference:** Domain 7: Security Operations - E-Discovery

---

## Q7.16 - Security Monitoring
**Domain:** 7 - Security Operations
**Concept:** Security Monitoring and Alerting
**Difficulty:** Medium

**Situation:** The SOC receives 10,000 alerts daily but can only investigate 100. Most alerts are false positives or low priority. What should be done?

**Choices:**
1. Ignore all alerts since there are too many
2. Tune alert thresholds and implement alert prioritization
3. Investigate alerts randomly
4. Disable monitoring to eliminate alerts

**Correct Answer:** 2

**Why Correct:** Alert tuning reduces false positives, and prioritization ensures high-severity alerts get attention first. This makes the alert volume manageable and ensures critical issues aren't lost in noise.

**Why Others Wrong:**
- Choice 1: Ignoring all alerts means missing genuine incidents
- Choice 3: Random investigation doesn't prioritize critical issues
- Choice 4: Disabling monitoring eliminates visibility entirely

**Domain Reference:** Domain 7: Security Operations - Security Monitoring

---

## Q7.17 - Problem Management
**Domain:** 7 - Security Operations
**Concept:** Problem Management
**Difficulty:** Medium

**Situation:** The same type of security incident has occurred three times in two months. Each time, the incident was handled, but it keeps recurring. What process should address the ROOT CAUSE?

**Choices:**
1. Incident management (handle each occurrence)
2. Problem management (identify and fix root cause)
3. Change management (approve changes)
4. Release management (deploy updates)

**Correct Answer:** 2

**Why Correct:** Problem management focuses on identifying root causes of recurring incidents and implementing permanent fixes. Incident management handles individual occurrences; problem management prevents recurrence.

**Why Others Wrong:**
- Choice 1: Incident management addresses symptoms repeatedly but doesn't fix root causes
- Choice 3: Change management approves changes but doesn't identify what changes are needed
- Choice 4: Release management deploys solutions but doesn't perform root cause analysis

**Domain Reference:** Domain 7: Security Operations - Problem Management

---

## Q7.18 - Resource Protection
**Domain:** 7 - Security Operations
**Concept:** Resource Protection
**Difficulty:** Easy

**Situation:** A former employee's access card still works two weeks after their termination. What operational process failure does this indicate?

**Choices:**
1. Background check process failure
2. Account/access provisioning and deprovisioning failure
3. Training program failure
4. Encryption key management failure

**Correct Answer:** 2

**Why Correct:** Deprovisioning (access removal upon departure) failed. Proper offboarding procedures should revoke all access - logical and physical - on or before the employee's last day. This gap leaves the organization vulnerable to former employee access.

**Why Others Wrong:**
- Choice 1: Background checks are pre-employment, not termination-related
- Choice 3: Training doesn't affect access revocation processes
- Choice 4: Encryption keys are unrelated to physical access card deactivation

**Domain Reference:** Domain 7: Security Operations - Resource Protection

---

# Domain 8: Software Development Security

## Q8.01 - SDLC Security
**Domain:** 8 - Software Development Security
**Concept:** SDLC Security Integration
**Difficulty:** Medium

**Situation:** Security requirements are currently addressed only during final testing before deployment. This results in expensive fixes. When should security FIRST be integrated into the development lifecycle?

**Choices:**
1. During final user acceptance testing
2. At the requirements and design phase
3. Only after the first security incident
4. Security is only IT's responsibility, not development

**Correct Answer:** 2

**Why Correct:** "Shift left" security integrates security from the earliest phases (requirements, design). Identifying security needs early is exponentially cheaper than fixing issues found in testing or production. Security requirements should be defined alongside functional requirements.

**Why Others Wrong:**
- Choice 1: Final testing is too late; issues found here are expensive to fix
- Choice 3: Reactive security after incidents is the most expensive approach
- Choice 4: Security is everyone's responsibility; developers must build secure code

**Domain Reference:** Domain 8: Software Development Security - SDLC Security

---

## Q8.02 - Secure Coding Practices
**Domain:** 8 - Software Development Security
**Concept:** Secure Coding Practices
**Difficulty:** Easy

**Situation:** A developer asks what the MOST important principle is for preventing injection attacks. What should they prioritize?

**Choices:**
1. Use the fastest database available
2. Validate and sanitize all input
3. Write more comments in code
4. Use longer variable names

**Correct Answer:** 2

**Why Correct:** Input validation and sanitization is the primary defense against injection attacks (SQL injection, command injection, XSS). Never trust user input - validate format, type, length, and sanitize or parameterize before use.

**Why Others Wrong:**
- Choice 1: Database speed is unrelated to security
- Choice 3: Comments improve readability but don't prevent attacks
- Choice 4: Variable naming conventions don't affect security

**Domain Reference:** Domain 8: Software Development Security - Secure Coding

---

## Q8.03 - Input Validation
**Domain:** 8 - Software Development Security
**Concept:** Input Validation
**Difficulty:** Medium

**Situation:** An application accepts user input for a search field. What is the BEST approach for input validation?

**Choices:**
1. Blacklist known malicious patterns
2. Whitelist acceptable input patterns
3. Accept all input and log it for review
4. Limit input to 1000 characters with no other validation

**Correct Answer:** 2

**Why Correct:** Whitelist validation (allow only known-good patterns) is more secure than blacklisting. Blacklists can be bypassed with novel patterns, while whitelists explicitly define what's acceptable and reject everything else.

**Why Others Wrong:**
- Choice 1: Blacklists can be bypassed; attackers find patterns not in the blacklist
- Choice 3: Accepting all input without validation enables attacks; logging doesn't prevent them
- Choice 4: Length limits alone don't prevent injection attacks within those limits

**Domain Reference:** Domain 8: Software Development Security - Input Validation

---

## Q8.04 - SQL Injection Prevention
**Domain:** 8 - Software Development Security
**Concept:** SQL Injection Prevention
**Difficulty:** Medium

**Situation:** A developer writes SQL queries by concatenating user input directly into query strings. What vulnerability does this create, and what is the FIX?

**Choices:**
1. Buffer overflow; use longer buffers
2. SQL injection; use parameterized queries/prepared statements
3. Cross-site scripting; encode output
4. Denial of service; add rate limiting

**Correct Answer:** 2

**Why Correct:** String concatenation in SQL enables SQL injection. Parameterized queries (prepared statements) separate SQL code from data, preventing user input from being interpreted as SQL commands. This is the definitive fix.

**Why Others Wrong:**
- Choice 1: Buffer overflow is a different vulnerability class
- Choice 3: XSS involves browser output, not SQL queries
- Choice 4: DoS is about availability, not query manipulation

**Domain Reference:** Domain 8: Software Development Security - SQL Injection Prevention

---

## Q8.05 - XSS Prevention
**Domain:** 8 - Software Development Security
**Concept:** Cross-Site Scripting Prevention
**Difficulty:** Medium

**Situation:** A web application displays user-submitted comments. An attacker posts a comment containing JavaScript that steals other users' session cookies. What vulnerability is this, and what is the PRIMARY fix?

**Choices:**
1. SQL injection; use parameterized queries
2. Cross-Site Scripting (XSS); encode output before displaying
3. CSRF; implement anti-CSRF tokens
4. Broken authentication; use stronger passwords

**Correct Answer:** 2

**Why Correct:** This is Stored XSS - malicious script is stored and executed in other users' browsers. The primary fix is output encoding - converting special characters to HTML entities so scripts display as text rather than executing.

**Why Others Wrong:**
- Choice 1: SQL injection targets databases, not browser script execution
- Choice 3: CSRF tricks users into performing actions; doesn't involve script injection
- Choice 4: Authentication issues don't cause script execution

**Domain Reference:** Domain 8: Software Development Security - XSS Prevention

---

## Q8.06 - Code Review
**Domain:** 8 - Software Development Security
**Concept:** Code Review Processes
**Difficulty:** Medium

**Situation:** A development team wants to catch security issues before code is merged. Manual review takes too long for all changes. What combination provides efficient coverage?

**Choices:**
1. Skip reviews for faster releases
2. Automated SAST tools with manual review for high-risk changes
3. Only review code after production incidents
4. Have developers review only their own code

**Correct Answer:** 2

**Why Correct:** Automated SAST provides broad coverage for common issues on all code changes. Manual review focuses on high-risk changes (authentication, authorization, data handling) where human insight adds value. This balances coverage and efficiency.

**Why Others Wrong:**
- Choice 1: Skipping reviews increases vulnerability risk
- Choice 3: Post-incident review is too late; issues should be found before deployment
- Choice 4: Self-review misses many issues; different perspectives catch more problems

**Domain Reference:** Domain 8: Software Development Security - Code Review

---

## Q8.07 - OWASP Top 10
**Domain:** 8 - Software Development Security
**Concept:** OWASP Top 10
**Difficulty:** Easy

**Situation:** Development teams are asked to focus on the most common web application vulnerabilities. What resource provides a consensus list of critical web application security risks?

**Choices:**
1. Company's internal style guide
2. OWASP Top 10
3. Programming language documentation
4. Database vendor manual

**Correct Answer:** 2

**Why Correct:** The OWASP Top 10 is an industry-standard awareness document listing the most critical web application security risks. It's updated periodically based on real-world data and provides guidance on prevention for each risk category.

**Why Others Wrong:**
- Choice 1: Internal style guides may not cover security comprehensively
- Choice 3: Language docs focus on functionality, not security vulnerabilities
- Choice 4: Database manuals address database features, not application security

**Domain Reference:** Domain 8: Software Development Security - OWASP Top 10

---

## Q8.08 - Buffer Overflow
**Domain:** 8 - Software Development Security
**Concept:** Buffer Overflow Prevention
**Difficulty:** Hard

**Situation:** A C application crashes when processing long inputs. Investigation reveals memory is being overwritten beyond allocated buffer boundaries. What is this vulnerability, and what is the BEST prevention?

**Choices:**
1. Memory leak; add garbage collection
2. Buffer overflow; use bounds checking and safe string functions
3. Race condition; add locking
4. Integer overflow; use larger integer types

**Correct Answer:** 2

**Why Correct:** Buffer overflow occurs when data exceeds allocated buffer size, overwriting adjacent memory. Prevention includes bounds checking, safe string functions (strncpy vs strcpy), and compiler protections (stack canaries, ASLR).

**Why Others Wrong:**
- Choice 1: Memory leaks are resource issues, not memory corruption
- Choice 3: Race conditions involve timing, not buffer boundaries
- Choice 4: Integer overflow is a different vulnerability (numeric wrap-around)

**Domain Reference:** Domain 8: Software Development Security - Buffer Overflow

---

## Q8.09 - DevSecOps
**Domain:** 8 - Software Development Security
**Concept:** DevSecOps Principles
**Difficulty:** Medium

**Situation:** Development, security, and operations teams work in silos with different goals. Security is seen as a blocker to releases. What cultural and process change addresses this?

**Choices:**
1. Give security veto power over all releases
2. Implement DevSecOps to integrate security into development and operations
3. Remove security from the release process
4. Only involve security after major incidents

**Correct Answer:** 2

**Why Correct:** DevSecOps integrates security into DevOps culture and processes. Security becomes everyone's responsibility, automated into pipelines, and involved early rather than as a late-stage gate. This replaces adversarial relationships with collaboration.

**Why Others Wrong:**
- Choice 1: Veto power perpetuates adversarial relationships
- Choice 3: Removing security creates unacceptable risk
- Choice 4: Post-incident involvement is reactive and costly

**Domain Reference:** Domain 8: Software Development Security - DevSecOps

---

## Q8.10 - CI/CD Pipeline Security
**Domain:** 8 - Software Development Security
**Concept:** CI/CD Pipeline Security
**Difficulty:** Medium

**Situation:** An attacker gains access to the CI/CD pipeline and modifies build scripts to inject malicious code into compiled applications. What type of attack is this?

**Choices:**
1. SQL injection
2. Supply chain / pipeline attack
3. Denial of service
4. Phishing

**Correct Answer:** 2

**Why Correct:** Compromising the CI/CD pipeline is a supply chain attack. By injecting malicious code into the build process, attackers can compromise all software built through that pipeline, affecting many downstream users.

**Why Others Wrong:**
- Choice 1: SQL injection targets databases, not build pipelines
- Choice 3: DoS affects availability, not code integrity
- Choice 4: Phishing targets users directly, not build infrastructure

**Domain Reference:** Domain 8: Software Development Security - CI/CD Security

---

## Q8.11 - Container Security
**Domain:** 8 - Software Development Security
**Concept:** Container Security
**Difficulty:** Medium

**Situation:** Your organization deploys applications in Docker containers. Base images haven't been updated in a year and contain known vulnerabilities. What is the BEST remediation?

**Choices:**
1. Containers don't need patching since they're isolated
2. Regularly update base images and scan for vulnerabilities
3. Run containers as root for easier management
4. Disable container security features for performance

**Correct Answer:** 2

**Why Correct:** Container images include operating system components and libraries that need updates like any software. Regular base image updates and vulnerability scanning (in registries and CI/CD) ensure containers don't deploy with known vulnerabilities.

**Why Others Wrong:**
- Choice 1: Containers need patching; isolation doesn't eliminate vulnerabilities within containers
- Choice 3: Root in containers increases risk if container is compromised
- Choice 4: Security features exist for good reasons; disabling them increases risk

**Domain Reference:** Domain 8: Software Development Security - Container Security

---

## Q8.12 - API Security
**Domain:** 8 - Software Development Security
**Concept:** API Security
**Difficulty:** Medium

**Situation:** Your REST API exposes sensitive data. Currently, anyone with the endpoint URL can access it. What security controls should be implemented?

**Choices:**
1. Make URLs longer and harder to guess
2. Implement authentication, authorization, and rate limiting
3. Only use POST requests instead of GET
4. Add "private" to the API name

**Correct Answer:** 2

**Why Correct:** API security requires authentication (who is accessing), authorization (what they can access), and rate limiting (prevent abuse). These controls ensure only authorized users access appropriate data and prevent brute force/DoS attacks.

**Why Others Wrong:**
- Choice 1: Security through obscurity; URLs are discoverable
- Choice 3: HTTP method doesn't provide access control
- Choice 4: Naming conventions don't enforce access control

**Domain Reference:** Domain 8: Software Development Security - API Security

---

## Q8.13 - Secure Software Deployment
**Domain:** 8 - Software Development Security
**Concept:** Secure Software Deployment
**Difficulty:** Medium

**Situation:** Attackers might replace legitimate software packages with malicious versions during deployment. What control ensures software integrity during deployment?

**Choices:**
1. Deploy faster to reduce exposure time
2. Use code signing and verify signatures before deployment
3. Keep deployment scripts secret
4. Only deploy on weekends

**Correct Answer:** 2

**Why Correct:** Code signing cryptographically signs software packages. Verifying signatures before deployment ensures packages are authentic (from the expected source) and haven't been tampered with (integrity).

**Why Others Wrong:**
- Choice 1: Speed doesn't verify authenticity
- Choice 3: Script secrecy doesn't ensure package integrity
- Choice 4: Timing doesn't verify software authenticity

**Domain Reference:** Domain 8: Software Development Security - Secure Deployment

---

## Q8.14 - Third-Party Software Risk
**Domain:** 8 - Software Development Security
**Concept:** Third-Party Software Risks
**Difficulty:** Medium

**Situation:** Your application uses 50 open-source libraries downloaded from public repositories. One library is later found to contain malware. What process should have detected this risk?

**Choices:**
1. Only use libraries with more than 1000 GitHub stars
2. Software composition analysis with vulnerability and integrity checking
3. Read all source code manually before use
4. Avoid all third-party software

**Correct Answer:** 2

**Why Correct:** Software composition analysis (SCA) tools identify third-party components, check for known vulnerabilities, and can verify package integrity against expected hashes. This systematically manages third-party risk.

**Why Others Wrong:**
- Choice 1: Popularity doesn't ensure security (popular packages have had malware)
- Choice 3: Manual review of all library code isn't scalable for 50+ dependencies
- Choice 4: Avoiding third-party software isn't practical and leads to reinventing wheels

**Domain Reference:** Domain 8: Software Development Security - Third-Party Risk

---

## Q8.15 - Software Supply Chain
**Domain:** 8 - Software Development Security
**Concept:** Software Supply Chain Security
**Difficulty:** Hard

**Situation:** A widely-used build tool was compromised, affecting thousands of organizations who used it. What type of attack is this, and what is a KEY defense?

**Choices:**
1. DDoS attack; implement redundancy
2. Supply chain attack; verify tool integrity and use signed releases
3. Phishing attack; train users
4. Insider threat; background checks

**Correct Answer:** 2

**Why Correct:** Supply chain attacks compromise software developers/tools to attack downstream users. Defenses include verifying integrity of all build tools, using signed releases, pinning dependency versions, and monitoring for unexpected changes.

**Why Others Wrong:**
- Choice 1: DDoS is availability attack, not software compromise
- Choice 3: Phishing targets individuals, not build infrastructure
- Choice 4: This is external attacker, not insider

**Domain Reference:** Domain 8: Software Development Security - Supply Chain Security

---

## Q8.16 - Static vs Dynamic Testing
**Domain:** 8 - Software Development Security
**Concept:** SAST vs DAST
**Difficulty:** Easy

**Situation:** A security tool analyzes running applications by sending requests and examining responses. Another tool analyzes source code without executing it. What are these tools called?

**Choices:**
1. Running application: SAST; Source code: DAST
2. Running application: DAST; Source code: SAST
3. Both are called SAST
4. Both are called penetration testing

**Correct Answer:** 2

**Why Correct:** DAST (Dynamic Application Security Testing) tests running applications through requests/responses. SAST (Static Application Security Testing) analyzes source code without execution. "Dynamic" = running; "Static" = code analysis.

**Why Others Wrong:**
- Choice 1: This reverses the definitions
- Choice 3: They are different tools with different approaches
- Choice 4: Penetration testing is broader; SAST/DAST are automated scanning approaches

**Domain Reference:** Domain 8: Software Development Security - SAST vs DAST

---

## Q8.17 - Output Encoding
**Domain:** 8 - Software Development Security
**Concept:** Output Encoding
**Difficulty:** Medium

**Situation:** User-generated content must be displayed on a web page. How should special characters like < and > be handled to prevent XSS?

**Choices:**
1. Strip all special characters from input
2. HTML-encode output so < becomes &lt; and > becomes &gt;
3. Display content inside hidden div elements
4. Use JavaScript to process the content

**Correct Answer:** 2

**Why Correct:** Output encoding converts special characters to safe representations. HTML encoding ensures < and > display as text rather than being interpreted as HTML tags. Context-appropriate encoding (HTML, JavaScript, URL) is essential for XSS prevention.

**Why Others Wrong:**
- Choice 1: Stripping characters may break legitimate content; encoding is preferred
- Choice 3: Hidden elements don't prevent XSS; code still executes
- Choice 4: Client-side JavaScript processing doesn't prevent XSS

**Domain Reference:** Domain 8: Software Development Security - Output Encoding

---

## Q8.18 - Secure Configuration
**Domain:** 8 - Software Development Security
**Concept:** Secure Configuration
**Difficulty:** Easy

**Situation:** A new web application is deployed with default administrator credentials and debug mode enabled. What security principle was violated?

**Choices:**
1. Principle of least privilege
2. Secure by default / Secure configuration
3. Defense in depth
4. Separation of duties

**Correct Answer:** 2

**Why Correct:** "Secure by default" means applications should ship in a hardened state - no default credentials, debugging disabled, minimal permissions. Requiring explicit action to reduce security (rather than increase it) prevents this class of vulnerability.

**Why Others Wrong:**
- Choice 1: Least privilege is about minimal permissions, not default configurations
- Choice 3: Defense in depth is layered controls, not secure defaults
- Choice 4: Separation of duties divides responsibilities, not related to default settings

**Domain Reference:** Domain 8: Software Development Security - Secure Configuration

---

# Summary

## Questions by Domain

| Domain | Name | Questions |
|--------|------|-----------|
| 3 | Security Architecture and Engineering | Q3.01 - Q3.18 |
| 4 | Communication and Network Security | Q4.01 - Q4.18 |
| 5 | Identity and Access Management | Q5.01 - Q5.18 |
| 6 | Security Assessment and Testing | Q6.01 - Q6.18 |
| 7 | Security Operations | Q7.01 - Q7.18 |
| 8 | Software Development Security | Q8.01 - Q8.18 |

**Total: 108 Questions**

## Next Steps

1. Review questions for CISSP accuracy
2. Generate dual-theme scenarios for each domain
3. Create Python scenario files
4. Integrate with game engine
5. Test all scenarios
