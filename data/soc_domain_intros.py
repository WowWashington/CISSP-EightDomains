"""
SOC Analyst domain introduction content.

Each domain has an introduction that sets the stage and explains
the key concepts that will be tested.
"""

SOC_DOMAIN_INTRODUCTIONS = {
    1: {
        "title": "DOMAIN 1: SIEM OPERATIONS & LOG MANAGEMENT",
        "narrator": "THE SENIOR SOC ANALYST",
        "introduction": """
Welcome to the nerve center of security operations - the SIEM.

Security Information and Event Management systems are where terabytes of logs
become actionable intelligence. Or where they become an overwhelming flood of
meaningless noise. The difference? Your skill.

In this domain, you'll master:

  - ALERT TRIAGE: Not all alerts are equal. Learn to identify high-fidelity
    signals in a sea of false positives.

  - LOG CORRELATION: A login isn't suspicious. A login from Russia followed
    by one from New York three minutes later? That's impossible travel.

  - RULE TUNING: The balance between sensitivity and noise. Too sensitive,
    you drown in alerts. Too loose, you miss the breach.

  - QUERY MASTERY: Whether it's SPL, KQL, or Lucene, knowing how to ask the
    right questions of your data is the analyst's superpower.

The SIEM sees everything. Your job is to understand what it's showing you.

Remember: every major breach has log evidence. The question is whether
anyone was watching.
        """
    },
    2: {
        "title": "DOMAIN 2: INCIDENT RESPONSE",
        "narrator": "THE INCIDENT COMMANDER",
        "introduction": """
When the alert turns red and the phone starts ringing, your training
determines whether you panic or perform.

Incident Response is the organized application of pressure to chaos.
NIST SP 800-61 gives us the framework:

  1. PREPARATION
     Before incidents happen, have your playbooks, contacts, and tools ready.
     The worst time to figure out your process is during a breach.

  2. DETECTION & ANALYSIS
     Identifying that something is wrong, then understanding what, where,
     and how bad.

  3. CONTAINMENT, ERADICATION & RECOVERY
     Stopping the bleeding, removing the threat, and returning to normal
     operations.

  4. POST-INCIDENT ACTIVITY
     Learning from what happened so it doesn't happen again.

You'll also learn evidence handling - because today's incident may be
tomorrow's court case. Chain of custody isn't bureaucracy; it's the
difference between justice and a dismissed case.

The SOC isn't just monitoring. It's defending. And defense requires response.
        """
    },
    3: {
        "title": "DOMAIN 3: THREAT INTELLIGENCE",
        "narrator": "THE THREAT INTEL LEAD",
        "introduction": """
Know your enemy. It's ancient wisdom, and it's the foundation of threat
intelligence.

We don't just react to alerts - we anticipate attacks by understanding
the adversaries who launch them.

The MITRE ATT&CK framework is your map of adversary behavior. Fourteen
tactics, hundreds of techniques - a taxonomy of how attackers actually
operate, based on real-world observations.

The PYRAMID OF PAIN teaches you where to invest:

  - Hash values? Trivial for attackers to change. Low value.
  - IP addresses? A new VPS takes five minutes. Still easy.
  - TTPs? Changing how you attack requires new skills, new tools,
    new tradecraft. That's expensive. That's where we hurt them.

You'll learn to consume and produce intelligence:

  - IOC MANAGEMENT: Indicators of Compromise - the digital fingerprints
    of evil. How to collect, validate, and operationalize them.

  - ATTRIBUTION: Understanding which threat actor is likely behind an
    attack helps predict their next moves.

  - THREAT HUNTING: Proactive search for threats that evade automated
    detection. The art of finding what no one else is looking for.

Intelligence transforms defense from reactive to proactive.
        """
    },
    4: {
        "title": "DOMAIN 4: NETWORK SECURITY MONITORING",
        "narrator": "THE NETWORK SECURITY ENGINEER",
        "introduction": """
The network doesn't lie. It can't.

Every packet, every connection, every byte transferred tells a story.
Your job is to read that story before the final chapter writes itself
as a breach.

Network security monitoring turns raw traffic into security visibility:

  - IDS/IPS ALERTS: Snort, Suricata, Zeek - these tools watch traffic and
    alert on suspicious patterns. Separating true positives from noise is
    an art form.

  - C2 DETECTION: Command and control beaconing has signatures. Regular
    intervals, consistent payloads, unusual destinations. The malware
    calls home; you intercept the call.

  - TRAFFIC ANALYSIS: Normal baseline vs. anomalous behavior. The HR
    laptop making Tor connections at 3 AM isn't updating its browser.

  - PROTOCOL AWARENESS: DNS tunneling, HTTPS covert channels, ICMP data
    exfiltration - attackers hide in legitimate protocols. You find them
    by understanding how protocols should behave.

Encrypted traffic is not invisible traffic. Metadata tells tales:
timing, volume, destinations, and patterns all reveal malicious intent
even when content is hidden.

The network sees everything. The question is: do you?
        """
    },
    5: {
        "title": "DOMAIN 5: ENDPOINT DETECTION & RESPONSE",
        "narrator": "THE EDR SPECIALIST",
        "introduction": """
The endpoint is where the battle is won or lost.

Servers, workstations, laptops - these are the targets attackers
ultimately want to compromise. EDR gives you visibility into exactly
what's happening on every protected system.

Modern attacks don't rely on malware files that antivirus can detect.
They use LIVING OFF THE LAND techniques:

  - LOLBins: Legitimate Windows binaries abused for malicious purposes.
    Certutil downloading payloads. Mshta executing scripts. All signed
    by Microsoft, all potentially deadly.

  - FILELESS ATTACKS: Code that lives only in memory, never touches disk.
    No file, no AV signature, no detection. Unless you're watching
    process behavior.

  - PROCESS TREES: The chain of parent-child relationships reveals intent.
    Word spawning PowerShell spawning cmd.exe? That's not a business process.

You'll learn to read EDR telemetry like a story:

  - What process spawned what?
  - What commands were executed?
  - What registry keys were modified?
  - What network connections were made?

The endpoint tells you everything. EDR makes it readable.
        """
    },
    6: {
        "title": "DOMAIN 6: VULNERABILITY MANAGEMENT",
        "narrator": "THE VULNERABILITY ANALYST",
        "introduction": """
There are more vulnerabilities than hours in the day.

Thousands of CVEs published yearly, millions of vulnerable systems, and
finite patching resources. Vulnerability management is the science of
prioritization.

CVSS gives you severity, but severity alone doesn't equal risk:

  - A CVSS 10.0 on an air-gapped system? Lower risk than...
  - A CVSS 8.0 on an internet-facing server with active exploitation.

EPSS (Exploit Prediction Scoring System) adds probability. What's the
likelihood this vulnerability will actually be exploited? A high-severity,
low-probability vulnerability may wait while you patch the medium-severity,
high-probability one being actively exploited.

Risk-based vulnerability management considers:

  - EXPOSURE: Internet-facing vs. internal-only?
  - EXPLOITATION: Theoretical vs. active in the wild?
  - ASSET VALUE: What's the business impact of compromise?
  - COMPENSATING CONTROLS: Does your WAF buy you time?

You can't patch everything immediately. But you can patch the right
things first.

That's the difference between vulnerability scanning and vulnerability
management.

Prioritize wisely. Your attackers certainly are.
        """
    }
}
