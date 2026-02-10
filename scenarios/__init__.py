"""
Scenarios module for The Citadel of the Eight Domains.
Contains scenario definitions for each of the 8 CISSP domains.
"""

from .domain1_security_risk import DOMAIN_1_SCENARIOS
from .domain2_asset_security import DOMAIN_2_SCENARIOS
from .domain3_security_architecture import DOMAIN_3_SCENARIOS
from .domain4_communication_network import DOMAIN_4_SCENARIOS
from .domain5_identity_access import DOMAIN_5_SCENARIOS
from .domain6_assessment_testing import DOMAIN_6_SCENARIOS
from .domain7_security_operations import DOMAIN_7_SCENARIOS
from .domain8_software_development import DOMAIN_8_SCENARIOS

__all__ = [
    'DOMAIN_1_SCENARIOS',
    'DOMAIN_2_SCENARIOS',
    'DOMAIN_3_SCENARIOS',
    'DOMAIN_4_SCENARIOS',
    'DOMAIN_5_SCENARIOS',
    'DOMAIN_6_SCENARIOS',
    'DOMAIN_7_SCENARIOS',
    'DOMAIN_8_SCENARIOS'
]
