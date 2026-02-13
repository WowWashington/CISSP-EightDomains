"""
Domain 6: Vulnerability Management scenarios.

Key SOC concepts tested:
- CVSS interpretation and scoring
- EPSS probability scoring
- Risk-based prioritization
- Patch management decisions
- Zero-day response
- Vulnerability scanner interpretation
- Asset criticality assessment
- Remediation verification

Each scenario uses a single "standard" professional theme.
"""

SOC_DOMAIN_6_SCENARIOS = [
    # Scenario 1: Risk-Based Prioritization
    {
        "id": "soc6_vuln_priority",
        "domain": 6,
        "themes": {
            "standard": {
                "title": "THE WEDNESDAY PATCH MEETING",
                "narrative": """
Your weekly vulnerability review meeting has arrived. The scanner found 327 new
vulnerabilities. Your patch window allows approximately 30 systems this weekend.

Four critical findings require attention:

A) CVE-2024-XXXX: CVSS 9.8, RCE in public-facing web server
   - Affects: 2 production web servers (customer portal)
   - EPSS: 0.87 (87% probability of exploitation)
   - Exploit: Public PoC available, active exploitation observed

B) CVE-2024-YYYY: CVSS 9.1, SQL injection in internal HR application
   - Affects: 1 server (internal HR system, no internet exposure)
   - EPSS: 0.12 (12% probability of exploitation)
   - Exploit: Theoretical, no public PoC

C) CVE-2024-ZZZZ: CVSS 7.5, DoS vulnerability in print servers
   - Affects: 15 print servers across all offices
   - EPSS: 0.05 (5% probability of exploitation)
   - Exploit: Requires local network access

D) CVE-2024-AAAA: CVSS 10.0, RCE in legacy system
   - Affects: 1 manufacturing control system (air-gapped)
   - EPSS: 0.91 (91% probability in exposed systems)
   - Exploit: Actively exploited, but system has no network connectivity

Which vulnerability should be your TOP priority?
                """,
                "choices": [
                    {"text": "Option D - CVSS 10.0 is the highest possible severity"},
                    {"text": "Option A - Internet-facing RCE with active exploitation"},
                    {"text": "Option C - It affects the most systems (15 servers)"},
                    {"text": "Option B - SQL injection could expose sensitive HR data"}
                ],
                "success_text": """
"Option A," you recommend. "Internet-facing, actively exploited, high EPSS score.
This is our biggest exposure."

Your prioritization framework:
1. EXPOSURE: A is internet-facing; D is air-gapped
2. EXPLOITABILITY: A has active exploitation; B is theoretical
3. IMPACT: Both A and D are RCE, but A is reachable
4. EPSS: A's 87% probability indicates real-world exploitation

The CVSS 10.0 for option D is misleading in context - an air-gapped system
can't be exploited remotely. Meanwhile, your public web server is actively
being targeted.

Your weekend patch prioritizes the web servers. Monday, threat intel reports
widespread exploitation of that exact CVE. Your systems were patched in time.

PRIORITIZATION PRINCIPLE: Context beats raw CVSS scores. Exposure + exploitability
+ business impact = actual risk priority.
                """,
                "failure_texts": {
                    0: """
CVSS 10.0 is scary, but the system is AIR-GAPPED. Zero network connectivity
means zero remote exploitation risk.

Would you treat a rifle behind locked doors the same as one on the sidewalk?
Same severity, very different risk based on accessibility.

LESSON: CVSS measures theoretical severity, not contextual risk.
                    """,
                    2: """
Volume matters, but a DoS vulnerability in print servers (CVSS 7.5, 5% EPSS,
requires local access) doesn't threaten your organization like an actively
exploited RCE in your customer portal.

If print servers go down, people use email. If your portal is compromised,
attackers have your customer data.

LESSON: Impact and exploitability trump volume.
                    """,
                    3: """
SQL injection is serious, but this is INTERNAL with no internet exposure and
no public exploit. The attacker would need to already be on your network.

Your internet-facing web server has a public exploit being actively used.
Attackers can hit it from anywhere.

LESSON: Exposure is a key risk factor. Internal < internet-facing.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Risk-based vulnerability prioritization:
- CVSS: How severe? (theoretical maximum)
- EPSS: How likely to be exploited? (real-world probability)
- EXPOSURE: Reachable by attackers?
- EXPLOITATION: Actively being used in the wild?

Risk = Likelihood x Impact x Exposure
        """,
        "domain_reference": "SOC Domain 6: Vulnerability Management - Risk-Based Prioritization"
    },

    # Scenario 2: CVSS Environmental Scoring
    {
        "id": "soc6_cvss_environmental",
        "domain": 6,
        "themes": {
            "standard": {
                "title": "THE SCANNER RESULTS",
                "narrative": """
Your vulnerability scanner identifies a critical finding on a newly deployed
web application server:

Vulnerability: CVE-2024-EXAMPLE
CVSS 3.1 Base Score: 9.8 (Critical)
- Attack Vector: Network (AV:N)
- Attack Complexity: Low (AC:L)
- Privileges Required: None (PR:N)
- User Interaction: None (UI:N)
- Confidentiality/Integrity/Availability Impact: High

However, your security architect points out:
- The application is behind a WAF with virtual patching enabled
- The vulnerable component is only accessible after authentication
- The server runs in an isolated network segment with strict egress filtering

The vendor patch requires a 4-hour maintenance window. Management wants to know
if this is truly urgent or if compensating controls reduce the risk.

Based on CVSS 3.1, what changes?
                """,
                "choices": [
                    {"text": "Nothing - CVSS Base Score is authoritative and cannot be modified"},
                    {"text": "The score decreases - WAF, auth requirement, and network controls are mitigating factors"},
                    {"text": "The score increases - production systems should have higher scores"},
                    {"text": "CVSS doesn't apply - it's only for theoretical vulnerabilities"}
                ],
                "success_text": """
"The Environmental Score should be lower," you explain. "CVSS 3.1 includes
Environmental metrics specifically for this situation."

Your adjusted assessment:
- Modified Attack Vector: Requires internal access (network isolation)
- Modified Attack Complexity: Higher (WAF virtual patching)
- Modified Privileges Required: Low (requires authentication)

The Base Score of 9.8 assumes worst-case: direct network access, no mitigations.
Your environment has compensating controls that reduce exploitability.

Recalculated Environmental Score: ~6.7 (Medium)

"This doesn't mean we skip the patch," you clarify. "But it means we can schedule
it for the next maintenance window rather than emergency downtime. The controls
buy us time."

CVSS PRINCIPLE: Base Score is theoretical maximum. Environmental Score reflects
YOUR organization's specific context and controls.
                """,
                "failure_texts": {
                    0: """
CVSS Base Score is NOT the final word! CVSS 3.1 includes three metric groups:

1. BASE: Intrinsic vulnerability characteristics
2. TEMPORAL: Current state (exploit availability, patch status)
3. ENVIRONMENTAL: Your specific deployment context

Environmental metrics exist precisely for your situation.

LESSON: CVSS Base Score is a starting point, not gospel.
                    """,
                    2: """
Production status doesn't automatically increase CVSS scores. Environmental
metrics consider controls and context, not arbitrary labels.

A production system WITH compensating controls may have LOWER environmental
risk than a dev system with NO controls.

LESSON: "Production = higher score" isn't how CVSS works.
                    """,
                    3: """
CVSS absolutely applies to real vulnerabilities - it's the industry standard!

The Base Score comes from the CVE itself. Environmental Score adapts it to
YOUR context. Both are valid CVSS applications.

LESSON: CVSS is designed for exactly this use case.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
CVSS 3.1 metric groups:
- BASE: Intrinsic characteristics (vendor-provided)
- TEMPORAL: Current state (exploit maturity, patch status)
- ENVIRONMENTAL: Your context (controls, requirements)

Environmental Score = Base Score adjusted for YOUR deployment reality.
        """,
        "domain_reference": "SOC Domain 6: Vulnerability Management - CVSS Environmental Scoring"
    },

    # Scenario 3: Patch Management Timing
    {
        "id": "soc6_patch_timing",
        "domain": 6,
        "themes": {
            "standard": {
                "title": "THE ZERO-DAY PATCH",
                "narrative": """
Microsoft releases an out-of-band security update for a critical Windows
vulnerability. The patch bulletin indicates:
- Severity: Critical (CVSS 9.8)
- Exploitation: Actively exploited in the wild
- Impact: Remote Code Execution
- Affected: All supported Windows versions

Your organization's patch policy specifies:
- Critical patches: 7-day deployment window after testing
- Standard test cycle: 3 days in dev, 2 days in staging

It's Friday afternoon. The patch was released 2 hours ago. Your change advisory
board (CAB) doesn't meet until Monday.

What patch deployment approach do you recommend?
                """,
                "choices": [
                    {"text": "Follow standard policy - deploy after 7-day testing cycle"},
                    {"text": "Emergency deployment - immediate rollout to critical systems, then full testing"},
                    {"text": "Wait for CAB meeting Monday - document the risk for approval"},
                    {"text": "Deploy to 10% of systems as an informal test before proceeding"}
                ],
                "success_text": """
"Emergency deployment to critical systems," you recommend. "Active exploitation
of a Critical RCE requires immediate action. Standard policy wasn't designed
for this scenario."

Your emergency patch plan:
1. IMMEDIATE: Deploy to internet-facing systems (web servers, VPN, email)
2. NEXT 24 HOURS: Deploy to high-value internal systems (DCs, file servers)
3. PARALLEL: Run abbreviated testing in isolated environment
4. WEEKEND: Rollout to general population with monitoring
5. MONDAY: CAB reviews actions taken, full post-deployment verification

You document the risk-based justification:
- Exploitation is ACTIVE (not theoretical)
- RCE vulnerability allows full compromise
- Waiting 7 days exposes all Windows systems
- Business risk of breach > risk of patch instability

The patch deploys without incident. Monday, threat intel shows mass exploitation
began Saturday morning. Your systems were protected.

PATCH TIMING PRINCIPLE: Policies provide guidance for normal operations. Active
exploitation of Critical vulnerabilities requires emergency procedures.
                """,
                "failure_texts": {
                    0: """
Following standard 7-day policy for an ACTIVELY EXPLOITED Critical RCE means
7 days of exposure while attackers compromise organizations worldwide.

Policies exist for normal operations. Active exploitation is not normal.

LESSON: Emergency situations require emergency procedures.
                    """,
                    2: """
Waiting until Monday while attackers actively exploit a Critical RCE gives them
the entire weekend to compromise your organization.

CAB processes exist for planned changes, not emergency security responses.
Document and proceed; CAB can ratify the decision Monday.

LESSON: Don't let process prevent response to active threats.
                    """,
                    3: """
An "informal" 10% rollout:
- Has no defined success criteria
- No clear escalation path
- No documentation for compliance
- Arbitrary sample size

Either follow the emergency process (which bypasses normal testing with
documented justification) or follow standard process. "Informal testing"
is neither.

LESSON: Emergency patching needs structure, just compressed.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Patch management timing:
- STANDARD: Follow policy (7-day testing typical)
- ELEVATED: Compress timeline for confirmed active threats
- EMERGENCY: Immediate deployment for actively exploited criticals

Active exploitation + Critical severity = emergency response, not normal process.
        """,
        "domain_reference": "SOC Domain 6: Vulnerability Management - Patch Management Timing"
    },

    # Scenario 4: Zero-Day Response
    {
        "id": "soc6_zero_day",
        "domain": 6,
        "themes": {
            "standard": {
                "title": "THE ZERO-DAY ALERT",
                "narrative": """
Security researchers publicly disclose a critical vulnerability in Apache Log4j
(Log4Shell). The disclosure includes:
- Severity: CVSS 10.0
- Exploitation: Trivially exploitable, public PoC available
- Impact: Remote Code Execution
- Affected: Log4j 2.0 through 2.14.1
- Patch: Available (Log4j 2.15.0)

Your organization uses Log4j extensively in Java applications. Your asset
inventory shows 47 applications using various Log4j versions. Full patching
will take 2-3 weeks due to application dependencies and testing requirements.

What is your IMMEDIATE response?
                """,
                "choices": [
                    {"text": "Begin patching immediately starting with the most critical applications"},
                    {"text": "Implement compensating controls while planning systematic patching"},
                    {"text": "Wait for vendor-specific patches from your application vendors"},
                    {"text": "Take all 47 applications offline until patched"}
                ],
                "success_text": """
"Implement compensating controls immediately," you recommend. "Patching 47
applications takes weeks. We need protection NOW."

Your immediate response:
1. WAF RULES: Block ${jndi: patterns in HTTP headers, URLs, and bodies
2. EGRESS FILTERING: Block LDAP/RMI outbound from application servers
3. ENVIRONMENT VARIABLE: Set LOG4J_FORMAT_MSG_NO_LOOKUPS=true
4. NETWORK MONITORING: Alert on LDAP/RMI connections from app servers
5. INCIDENT HUNTING: Search logs for exploitation attempts

Your patching plan (parallel to controls):
- Week 1: Internet-facing applications
- Week 2: Internal critical applications
- Week 3: Remaining applications

Two days later, your WAF blocks 3,000+ exploitation attempts. Network monitoring
catches one successful exploitation attempt - contained within minutes because
egress filtering blocked the callback.

ZERO-DAY PRINCIPLE: When patching takes time, compensating controls provide
immediate protection. Layer defenses: WAF + egress + monitoring + patching.
                """,
                "failure_texts": {
                    0: """
"Begin patching immediately" is the right eventual action, but 47 applications
can't be patched in hours. Meanwhile, exploitation is trivially easy with
public PoCs.

Without compensating controls, you're vulnerable for 2-3 weeks while methodically
patching.

LESSON: Implement immediate mitigations while planning systematic remediation.
                    """,
                    2: """
Waiting for vendor patches means waiting for 47 different vendors to respond.
Some will patch in days. Some in weeks. Some never.

Log4Shell is in a library YOUR applications use. You can patch the library
independently or implement mitigations NOW.

LESSON: Don't wait for vendors when you can act immediately.
                    """,
                    3: """
Taking 47 applications offline means:
- Email (if using Log4j): offline
- Customer portal: offline
- Internal tools: offline
- Business operations: severely impacted

The cure is worse than the disease. Compensating controls allow continued
operations while addressing the vulnerability.

LESSON: Business continuity matters. Protect AND operate, don't just stop.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Zero-day response strategy:
1. ASSESS scope immediately
2. IMPLEMENT compensating controls (WAF, egress, monitoring)
3. HUNT for exploitation attempts
4. PATCH systematically while controls provide coverage

Don't wait for perfect patching when immediate mitigation is possible.
        """,
        "domain_reference": "SOC Domain 6: Vulnerability Management - Zero-Day Response"
    },

    # Scenario 5: Scanner Interpretation
    {
        "id": "soc6_scanner_interpretation",
        "domain": 6,
        "themes": {
            "standard": {
                "title": "THE SCAN RESULTS",
                "narrative": """
Your vulnerability scanner reports the following for a production web server:

Finding: SSL/TLS Certificate Issues
- SSL Certificate Signed Using Weak Hash (SHA-1)
- SSL Certificate Expiring Soon (30 days)
- SSL Self-Signed Certificate

Severity: HIGH (per scanner default settings)
CVSS: 4.3 (Medium)

The server hosts an internal application used only by employees on the corporate
network. The application doesn't process sensitive data. The security team
inherited this server last month.

How do you interpret and act on these findings?
                """,
                "choices": [
                    {"text": "Critical priority - HIGH severity means immediate action"},
                    {"text": "Context-adjusted priority - certificate issues are lower risk for internal apps"},
                    {"text": "Ignore completely - scanners always over-report certificate issues"},
                    {"text": "Report as compliant - CVSS 4.3 is Medium, not High"}
                ],
                "success_text": """
"Context-adjusted priority," you assess. "These are valid findings, but the
scanner's HIGH severity doesn't account for our specific environment."

Your contextual analysis:
- SELF-SIGNED CERT: Concern for public sites (user trust). Internal app with
  enterprise-managed browsers? Lower risk.
- SHA-1: Cryptographic weakness, but exploitation requires active MITM. On
  internal network with existing controls? Reduced risk.
- EXPIRING CERT: Valid concern, but 30 days is notice, not emergency.
- INTERNAL ONLY: No internet exposure reduces attack surface significantly.

Your recommendation:
- PRIORITY: Medium (not emergency, not ignore)
- TIMELINE: Address within standard maintenance window
- ACTION: Replace certificate with enterprise CA-issued cert (solves all three)

The scanner defaults to HIGH for certificate issues because they're critical
for public-facing sites. Adjust severity based on YOUR context.

SCANNER PRINCIPLE: Scanner severity is a starting point. Apply organizational
context to determine actual priority. CVSS + Environment = Real Risk.
                """,
                "failure_texts": {
                    0: """
"HIGH severity = immediate action" ignores context:
- Internal application (not internet-facing)
- No sensitive data processing
- Certificate issues, not remote code execution

HIGH is the scanner's DEFAULT for cert issues. Context matters more than
default severity labels.

LESSON: Scanner severity reflects generic assessment. Apply your context.
                    """,
                    2: """
"Ignore completely" goes too far. Certificate issues ARE real:
- Self-signed certs don't establish proper trust
- SHA-1 IS cryptographically weak
- Expiring certs WILL cause outages

The findings are VALID. The priority is context-dependent, not the validity.

LESSON: Adjust priority, don't ignore valid findings.
                    """,
                    3: """
"CVSS 4.3 is Medium so we're compliant" misses several points:
- Compliance and risk aren't the same thing
- The findings still need remediation
- Certificate issues affect availability (expiration)

Medium CVSS doesn't mean "ignore" - it means "lower priority than critical."

LESSON: Medium priority isn't no priority.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Vulnerability scanner interpretation:
- SCANNER SEVERITY: Generic assessment based on finding type
- CVSS: Standardized vulnerability scoring
- ENVIRONMENTAL CONTEXT: Your specific deployment
- ACTUAL PRIORITY: Scanner + CVSS + Context

Always apply organizational context to scanner output.
        """,
        "domain_reference": "SOC Domain 6: Vulnerability Management - Scanner Result Interpretation"
    },

    # Scenario 6: Risk Acceptance
    {
        "id": "soc6_risk_acceptance",
        "domain": 6,
        "themes": {
            "standard": {
                "title": "THE LEGACY SYSTEM",
                "narrative": """
Your vulnerability scanner identifies 23 HIGH and CRITICAL vulnerabilities on
a legacy manufacturing control system:
- Windows Server 2008 R2 (end of life)
- Multiple unpatched vulnerabilities (no patches available)
- Application software from defunct vendor (no support)
- Controls production line worth $50M in annual revenue

The system owner requests risk acceptance: "We can't patch without breaking
production. The vendor is gone. Upgrading the entire production line costs
$3M and takes 18 months."

What elements are REQUIRED for proper risk acceptance documentation?
                """,
                "choices": [
                    {"text": "Just get management signature - they're accepting the risk"},
                    {"text": "Complete risk assessment with compensating controls, review timeline, and management approval"},
                    {"text": "No documentation needed - legacy systems are exempt from compliance"},
                    {"text": "Reject the acceptance request - all vulnerabilities must be patched"}
                ],
                "success_text": """
"Complete risk assessment with compensating controls," you confirm. "Risk
acceptance isn't a bypass - it's a documented decision with mitigations."

Your risk acceptance package:
1. VULNERABILITY DETAILS: 23 findings with severity and potential impact
2. BUSINESS JUSTIFICATION: Production criticality, upgrade costs, timeline
3. COMPENSATING CONTROLS:
   - Network isolation (VLAN with strict ACLs)
   - No internet connectivity
   - Limited administrative access
   - Enhanced monitoring for anomalies
   - Annual penetration testing
4. RESIDUAL RISK: After controls, what risk remains?
5. REVIEW TIMELINE: Re-assess annually until upgrade completes
6. MANAGEMENT APPROVAL: Business owner and CISO sign-off

The system remains in production with documented risk acceptance and
compensating controls. When auditors ask, you have complete documentation.

RISK ACCEPTANCE PRINCIPLE: Accepting risk doesn't mean ignoring it. Document
the decision, implement mitigations, review periodically, get appropriate
approval levels.
                """,
                "failure_texts": {
                    0: """
"Just get a signature" creates compliance nightmares:
- No documented justification
- No compensating controls
- No review timeline
- No evidence of due diligence

When auditors or regulators ask, "we got a signature" isn't sufficient.

LESSON: Risk acceptance is a process, not just a signature.
                    """,
                    2: """
"Legacy systems are exempt" is not how compliance works. PCI-DSS, HIPAA, SOX,
and other frameworks don't exempt legacy systems.

If anything, legacy systems require MORE documentation: why you can't patch,
what compensating controls exist, when you'll remediate.

LESSON: Legacy doesn't mean exempt. It means documented exception.
                    """,
                    3: """
"All vulnerabilities must be patched" ignores business reality:
- The vendor no longer exists
- The system controls $50M in revenue
- The upgrade takes 18 months

Risk management includes accepting some risks with appropriate controls.
Zero risk isn't achievable.

LESSON: Security serves the business. Managed risk is acceptable.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Risk acceptance requirements:
1. DETAILED VULNERABILITY ASSESSMENT
2. BUSINESS JUSTIFICATION
3. COMPENSATING CONTROLS
4. RESIDUAL RISK ANALYSIS
5. REVIEW TIMELINE
6. APPROPRIATE MANAGEMENT APPROVAL

Risk acceptance is a documented decision, not a bypass.
        """,
        "domain_reference": "SOC Domain 6: Vulnerability Management - Risk Acceptance Documentation"
    },

    # Scenario 7: Asset Criticality
    {
        "id": "soc6_asset_criticality",
        "domain": 6,
        "themes": {
            "standard": {
                "title": "THE CRITICALITY ASSESSMENT",
                "narrative": """
Your organization is implementing risk-based vulnerability management. You need
to assign criticality ratings to assets for prioritization. Consider these systems:

System A: Email server
- Affects all 5,000 employees
- Contains sensitive communications
- Internet-facing

System B: Domain Controller
- Authenticates all users and systems
- Compromise = complete domain takeover
- Internal only

System C: CEO's laptop
- Single user
- Contains strategic documents
- Mobile, sometimes off-network

System D: Development server
- Used by 50 developers
- No production data
- Internal only

Which system should have the HIGHEST criticality rating?
                """,
                "choices": [
                    {"text": "System A - Affects most users and is internet-facing"},
                    {"text": "System B - Domain controller compromise is catastrophic"},
                    {"text": "System C - CEO's strategic documents are extremely valuable"},
                    {"text": "System D - Developer access could lead to supply chain attacks"}
                ],
                "success_text": """
"System B - Domain Controller," you assess. "DC compromise provides complete
domain control - every system, every account, every secret."

Your criticality analysis:

SYSTEM B (HIGHEST - Domain Controller):
- Authentication backbone for entire organization
- Compromise = attacker controls all accounts
- Can create admin accounts, access any system, deploy malware everywhere
- Recovery requires complete domain rebuild

System A (High - Email):
- Widespread impact but doesn't grant infrastructure control
- Compromise is serious but contained

System C (High - CEO Laptop):
- Valuable data but single-point compromise
- Doesn't provide infrastructure access

System D (Medium - Dev Server):
- Important but no production access
- Supply chain risk exists but requires additional steps

The Domain Controller is the "keys to the kingdom." Its compromise affects not
just itself but EVERY OTHER SYSTEM in the domain.

ASSET CRITICALITY PRINCIPLE: Consider both DIRECT impact (this system) and
TRANSITIVE impact (what else becomes vulnerable). Infrastructure systems that
control other systems are highest priority.
                """,
                "failure_texts": {
                    0: """
Email affects many users, but compromise doesn't grant infrastructure control.
An attacker with email access can phish, but they don't automatically own the
domain.

The Domain Controller, compromised, gives attackers control over email AND
everything else.

LESSON: Infrastructure control > user count.
                    """,
                    2: """
The CEO's laptop contains valuable data, but:
- It's a single endpoint
- Compromise doesn't grant infrastructure access
- Strategic documents are valuable but contained

The Domain Controller controls the CEO's access AND everyone else's.

LESSON: Don't conflate high-value data with infrastructure criticality.
                    """,
                    3: """
Supply chain attacks via development servers are a real concern, but:
- Requires additional steps (compromising builds, deploying to prod)
- Doesn't immediately grant infrastructure access
- Production data access requires more movement

The DC provides immediate, complete domain control with no additional steps.

LESSON: Indirect attack paths are important but rank below direct infrastructure
compromise.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Asset criticality factors:
1. BLAST RADIUS - What's affected if compromised?
2. TRANSITIVE IMPACT - Does this control other systems?
3. DATA SENSITIVITY - What information is at risk?
4. RECOVERY COMPLEXITY - How hard to remediate?

Infrastructure control systems (DCs, PKI) rank highest because their compromise
affects everything else.
        """,
        "domain_reference": "SOC Domain 6: Vulnerability Management - Asset Criticality Assessment"
    },

    # Scenario 8: Remediation Verification
    {
        "id": "soc6_remediation_verification",
        "domain": 6,
        "themes": {
            "standard": {
                "title": "THE VERIFICATION SCAN",
                "narrative": """
Last week, you identified a critical vulnerability (CVE-2024-XXXXX) on your
public-facing web server. The system administrator reports the patch has been
applied. You need to verify remediation.

Your verification scan shows:
- Original vulnerability: CVE-2024-XXXXX (CVSS 9.8)
- Current scan: "No vulnerabilities found"
- Last scan date: Today
- Scanner: Same scanner used for detection

The admin says "See? It's fixed. Close the ticket."

What additional verification should you perform before closing?
                """,
                "choices": [
                    {"text": "Close the ticket - the scanner confirmed remediation"},
                    {"text": "Verify patch installation, test application functionality, check for regression"},
                    {"text": "Run a second scanner to confirm - one scanner might miss something"},
                    {"text": "Request penetration testing before closing critical findings"}
                ],
                "success_text": """
"Verify patch installation and test functionality," you confirm. "Scanner
confirmation is necessary but not sufficient."

Your verification process:
1. PATCH VERIFICATION:
   - Check installed update history (KB number present)
   - Verify vulnerable component version changed
   - Confirm no rollback occurred

2. FUNCTIONAL TESTING:
   - Application still works correctly
   - No broken functionality from patch
   - Performance within normal parameters

3. REGRESSION CHECK:
   - Patch didn't reintroduce old vulnerabilities
   - No new issues created

4. DOCUMENTATION:
   - Update vulnerability ticket with evidence
   - Record patch version, verification date, tester

Your checks reveal: The scan shows "no vulnerabilities" because the web server
is temporarily offline for maintenance. The vulnerability isn't patched - the
service isn't running!

You flag the ticket: "Verification incomplete - service offline during scan.
Reschedule verification when service restored."

VERIFICATION PRINCIPLE: Scanners can miss vulnerabilities for many reasons
(service down, network issues, scan scope). Multi-factor verification confirms
true remediation.
                """,
                "failure_texts": {
                    0: """
"Scanner says fixed, close it" is dangerous because:
- Scanner might not have reached the service
- Service might be temporarily down
- Patch might have been rolled back
- Different scan configuration might miss it

The scanner is ONE data point, not proof of remediation.

LESSON: Verify through multiple methods, not just scanner output.
                    """,
                    2: """
Running a second scanner doesn't verify the PATCH - it verifies the scanner
finding. Two scanners agreeing the vulnerability isn't detected doesn't mean
the patch was applied.

Both could be failing to detect for the same reason (service down, network
issue, evasion technique).

LESSON: Verify the REMEDIATION ACTION, not just the scan result.
                    """,
                    3: """
Penetration testing for every critical finding isn't scalable:
- Pen tests take time and expertise
- Critical findings may number in dozens or hundreds
- Creates bottleneck in remediation flow

Pen testing is valuable for validation of security posture, but not for
routine patch verification.

LESSON: Match verification effort to the situation. Patch verification
doesn't require full pen test.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Remediation verification:
1. SCANNER CONFIRMATION - Necessary but not sufficient
2. PATCH VERIFICATION - Check installed updates
3. VERSION VERIFICATION - Confirm vulnerable component updated
4. FUNCTIONAL TESTING - Application still works
5. REGRESSION CHECK - No new issues introduced

Multiple verification methods provide confidence. Scanner alone doesn't.
        """,
        "domain_reference": "SOC Domain 6: Vulnerability Management - Remediation Verification"
    }
]
