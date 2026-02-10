"""
Theme management for The Citadel of the Eight Domains.

Supports multiple story themes that present the same CISSP concepts
in different narrative styles.
"""

from enum import Enum
from typing import Dict


class StoryTheme(Enum):
    """Available story themes for the game."""
    FANTASY = "fantasy"
    CORPORATE = "corporate"


class ThemeManager:
    """
    Manages the current story theme and provides theme-related utilities.

    Attributes:
        current_theme: The currently active story theme
    """

    THEME_DISPLAY_NAMES: Dict[StoryTheme, str] = {
        StoryTheme.FANTASY: "Medieval Fantasy",
        StoryTheme.CORPORATE: "Corporate Office"
    }

    THEME_SHORT_NAMES: Dict[StoryTheme, str] = {
        StoryTheme.FANTASY: "Fantasy",
        StoryTheme.CORPORATE: "Corporate"
    }

    THEME_DESCRIPTIONS: Dict[StoryTheme, str] = {
        StoryTheme.FANTASY: (
            "Explore the Citadel of the Eight Domains, an ancient fortress "
            "where scribes guard secrets and magic protects the realm..."
        ),
        StoryTheme.CORPORATE: (
            "Navigate InfoSec challenges at Initech Corporation, where "
            "TPS reports meet cybersecurity and coffee fuels compliance..."
        )
    }

    THEME_GAME_TITLES: Dict[StoryTheme, str] = {
        StoryTheme.FANTASY: "The Citadel of the Eight Domains",
        StoryTheme.CORPORATE: "InfoSec Adventures at Initech"
    }

    def __init__(self):
        """Initialize with default theme (Fantasy)."""
        self.current_theme = StoryTheme.FANTASY

    def set_theme(self, theme: StoryTheme) -> None:
        """Set the current story theme."""
        self.current_theme = theme

    def toggle_theme(self) -> StoryTheme:
        """
        Toggle between Fantasy and Corporate themes.

        Returns:
            The new current theme after toggling
        """
        if self.current_theme == StoryTheme.FANTASY:
            self.current_theme = StoryTheme.CORPORATE
        else:
            self.current_theme = StoryTheme.FANTASY
        return self.current_theme

    def get_display_name(self) -> str:
        """Get the display name of the current theme."""
        return self.THEME_DISPLAY_NAMES[self.current_theme]

    def get_short_name(self) -> str:
        """Get the short name of the current theme."""
        return self.THEME_SHORT_NAMES[self.current_theme]

    def get_game_title(self) -> str:
        """Get the game title for the current theme."""
        return self.THEME_GAME_TITLES[self.current_theme]

    def get_theme_key(self) -> str:
        """Get the theme key (for accessing theme-specific content in scenarios)."""
        return self.current_theme.value

    @classmethod
    def get_all_themes(cls) -> list:
        """Return list of all available themes."""
        return list(StoryTheme)
