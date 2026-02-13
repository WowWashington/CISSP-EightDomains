"""
SOC Analyst Certification scenario data structures and loader.

This module aggregates all SOC Analyst domain scenarios for the certification quiz.

The SOC Analyst certification covers 6 domains based on real SOC certifications
(CompTIA CySA+, GIAC GSOC, EC-Council CSA):
1. SIEM Operations & Log Management
2. Incident Response
3. Threat Intelligence
4. Network Security Monitoring
5. Endpoint Detection & Response
6. Vulnerability Management

Each scenario follows this structure:
{
    "id": str,              # Unique identifier (e.g., "soc1_alert_triage")
    "domain": int,          # SOC domain number (1-6)
    "themes": {
        "standard": {       # Professional SOC theme
            "title": str,           # Scenario title
            "narrative": str,       # The situation description
            "choices": [{"text": str}, ...],  # 4 choices
            "success_text": str,    # Explanation on correct answer
            "failure_texts": {idx: str, ...}  # Why each wrong choice is wrong
        }
    },
    "correct_index": int,   # 0-based index of correct choice
    "xp_reward": int,       # XP gained for correct answer (default: 50)
    "hp_penalty": int,      # HP lost for wrong answer (default: 15)
    "failure_text": str,    # General failure explanation (fallback)
    "domain_reference": str # Domain citation
}
"""

# The Six SOC Analyst Domains
SOC_DOMAINS = {
    1: "SIEM Operations & Log Management",
    2: "Incident Response",
    3: "Threat Intelligence",
    4: "Network Security Monitoring",
    5: "Endpoint Detection & Response",
    6: "Vulnerability Management"
}

# Import scenarios from domain-specific modules
from scenarios.soc_domain1_siem import SOC_DOMAIN_1_SCENARIOS
from scenarios.soc_domain2_incident_response import SOC_DOMAIN_2_SCENARIOS
from scenarios.soc_domain3_threat_intel import SOC_DOMAIN_3_SCENARIOS
from scenarios.soc_domain4_network import SOC_DOMAIN_4_SCENARIOS
from scenarios.soc_domain5_endpoint import SOC_DOMAIN_5_SCENARIOS
from scenarios.soc_domain6_vuln import SOC_DOMAIN_6_SCENARIOS

# Aggregate all SOC scenarios
ALL_SOC_SCENARIOS = []
ALL_SOC_SCENARIOS.extend(SOC_DOMAIN_1_SCENARIOS)
ALL_SOC_SCENARIOS.extend(SOC_DOMAIN_2_SCENARIOS)
ALL_SOC_SCENARIOS.extend(SOC_DOMAIN_3_SCENARIOS)
ALL_SOC_SCENARIOS.extend(SOC_DOMAIN_4_SCENARIOS)
ALL_SOC_SCENARIOS.extend(SOC_DOMAIN_5_SCENARIOS)
ALL_SOC_SCENARIOS.extend(SOC_DOMAIN_6_SCENARIOS)
