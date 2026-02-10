"""
Player state management for The Citadel of the Eight Domains.
"""

from dataclasses import dataclass, field
from typing import List
from enum import Enum, auto


class GameStatus(Enum):
    """Enumeration of possible game states."""
    PLAYING = auto()
    VICTORY = auto()
    COMPLETED = auto()  # Finished all domains (replaces DEFEAT - no death in training mode)


@dataclass
class Player:
    """
    Represents the player's current state in the game.

    Attributes:
        name: The player's chosen name
        hp: Health points (can go negative - tracks performance, no death penalty)
        max_hp: Maximum health points
        xp: Experience points (1000 = mastery)
        current_domain: Which of the 8 CISSP domains player is in (1-8)
        scenarios_completed: List of scenario IDs already completed
        wrong_answers: Count of incorrect answers (for performance tracking)
        correct_answers: Count of correct answers (for performance tracking)
    """
    name: str
    hp: int = 100
    max_hp: int = 100
    xp: int = 0
    current_domain: int = 1
    scenarios_completed: List[str] = field(default_factory=list)
    wrong_answers: int = 0
    correct_answers: int = 0

    # XP thresholds for titles
    TITLES = {
        0: "Novice Scribe",
        100: "Apprentice Guardian",
        250: "Warden of Secrets",
        400: "Keeper of the Cipher",
        550: "Shield Bearer",
        700: "Master of Controls",
        850: "High Sentinel",
        1000: "Information Systems Security Professional"
    }

    WIN_XP = 1000

    @property
    def title(self) -> str:
        """Calculate current title based on XP."""
        current_title = "Novice Scribe"
        for threshold, title in sorted(self.TITLES.items()):
            if self.xp >= threshold:
                current_title = title
        return current_title

    @property
    def status(self) -> GameStatus:
        """Determine current game status. No death penalty - training mode."""
        if self.xp >= self.WIN_XP:
            return GameStatus.VICTORY
        return GameStatus.PLAYING  # Always playing until all domains complete

    @property
    def accuracy(self) -> float:
        """Calculate accuracy percentage (correct / total answers)."""
        total = self.correct_answers + self.wrong_answers
        if total == 0:
            return 0.0
        return (self.correct_answers / total) * 100

    @property
    def performance_rating(self) -> str:
        """Get performance rating based on accuracy."""
        acc = self.accuracy
        if acc >= 90:
            return "Exemplary"
        elif acc >= 80:
            return "Proficient"
        elif acc >= 70:
            return "Competent"
        elif acc >= 60:
            return "Developing"
        else:
            return "Needs Improvement"

    def take_damage(self, amount: int) -> int:
        """
        Reduce HP by amount (can go negative for performance tracking).
        No death penalty - this is training mode.
        """
        self.hp -= amount
        self.wrong_answers += 1
        return amount

    def gain_xp(self, amount: int) -> bool:
        """
        Increase XP by amount.
        Returns True if title changed.
        """
        old_title = self.title
        self.xp += amount
        self.correct_answers += 1
        new_title = self.title
        return old_title != new_title

    def heal(self, amount: int) -> int:
        """Restore HP up to max_hp, returning actual healing."""
        actual_heal = min(self.max_hp - self.hp, amount)
        self.hp += actual_heal
        return actual_heal

    def complete_scenario(self, scenario_id: str) -> None:
        """Mark a scenario as completed."""
        if scenario_id not in self.scenarios_completed:
            self.scenarios_completed.append(scenario_id)
