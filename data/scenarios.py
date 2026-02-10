"""
Scenario data structures and loader for The Citadel of the Eight Domains.

Each scenario follows this structure:
{
    "id": str,              # Unique identifier (e.g., "d1_fire_scroll_room")
    "domain": int,          # CISSP domain number (1-8)
    "title": str,           # Scenario title for display
    "narrative": str,       # The story/situation description
    "choices": [            # List of 3-4 choices
        {
            "text": str,           # Choice text shown to player
            "failure_reason": str  # Explanation if this wrong choice is selected (None for correct)
        },
        ...
    ],
    "correct_index": int,   # 0-based index of correct choice
    "xp_reward": int,       # XP gained for correct answer (default: 50)
    "hp_penalty": int,      # HP lost for wrong answer (default: 20)
    "success_text": str,    # Narrative shown on success
    "failure_text": str,    # General failure explanation (fallback)
    "domain_reference": str # CISSP domain citation
}
"""

# The Eight CISSP Domains for reference
DOMAINS = {
    1: "Security and Risk Management",
    2: "Asset Security",
    3: "Security Architecture and Engineering",
    4: "Communication and Network Security",
    5: "Identity and Access Management (IAM)",
    6: "Security Assessment and Testing",
    7: "Security Operations",
    8: "Software Development Security"
}

# Import scenarios from domain-specific modules
from scenarios.domain1_security_risk import DOMAIN_1_SCENARIOS
from scenarios.domain2_asset_security import DOMAIN_2_SCENARIOS
from scenarios.domain3_security_architecture import DOMAIN_3_SCENARIOS
from scenarios.domain4_communication_network import DOMAIN_4_SCENARIOS
from scenarios.domain5_identity_access import DOMAIN_5_SCENARIOS
from scenarios.domain6_assessment_testing import DOMAIN_6_SCENARIOS
from scenarios.domain7_security_operations import DOMAIN_7_SCENARIOS
from scenarios.domain8_software_development import DOMAIN_8_SCENARIOS

# Aggregate all scenarios
ALL_SCENARIOS = []
ALL_SCENARIOS.extend(DOMAIN_1_SCENARIOS)
ALL_SCENARIOS.extend(DOMAIN_2_SCENARIOS)
ALL_SCENARIOS.extend(DOMAIN_3_SCENARIOS)
ALL_SCENARIOS.extend(DOMAIN_4_SCENARIOS)
ALL_SCENARIOS.extend(DOMAIN_5_SCENARIOS)
ALL_SCENARIOS.extend(DOMAIN_6_SCENARIOS)
ALL_SCENARIOS.extend(DOMAIN_7_SCENARIOS)
ALL_SCENARIOS.extend(DOMAIN_8_SCENARIOS)
