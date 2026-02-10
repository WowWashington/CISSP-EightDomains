"""
Data module for The Citadel of the Eight Domains.
Contains scenario data, ASCII art assets, and game constants.
"""

from .scenarios import ALL_SCENARIOS, DOMAINS
from .ascii_art import (
    TITLE_ART, DOMAIN_BANNERS, VICTORY_ART, DEFEAT_ART,
    COMPLETION_ART, NEEDS_IMPROVEMENT_ART
)
from .domain_intros import DOMAIN_INTRODUCTIONS

__all__ = [
    'ALL_SCENARIOS', 'DOMAINS', 'TITLE_ART', 'DOMAIN_BANNERS',
    'VICTORY_ART', 'DEFEAT_ART', 'COMPLETION_ART', 'NEEDS_IMPROVEMENT_ART',
    'DOMAIN_INTRODUCTIONS'
]
