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
        xp: Experience points (tracks progress, max ~4000 for perfect game)
        current_domain: Which of the 8 CISSP domains player is in (1-8)
        scenarios_completed: List of scenario IDs already completed
        wrong_answers: Count of incorrect answers (for performance tracking)
        correct_answers: Count of correct answers (for performance tracking)
        domain_stats: Per-domain tracking of correct/wrong answers
    """
    name: str
    hp: int = 100
    max_hp: int = 100
    xp: int = 0
    current_domain: int = 1
    scenarios_completed: List[str] = field(default_factory=list)
    wrong_answers: int = 0
    correct_answers: int = 0
    domain_stats: dict = field(default_factory=lambda: {
        i: {"correct": 0, "wrong": 0} for i in range(1, 9)
    })

    # XP thresholds for titles (scaled for full 8-domain game: ~4000 max XP)
    TITLES = {
        0: "Novice Scribe",
        400: "Apprentice Guardian",
        1000: "Warden of Secrets",
        1600: "Keeper of the Cipher",
        2200: "Shield Bearer",
        2800: "Master of Controls",
        3400: "High Sentinel",
        4000: "Information Systems Security Professional"
    }

    WIN_XP = 4000  # Max possible XP (for display purposes)

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
        """Determine current game status. Victory requires completing all 8 domains."""
        if self.current_domain > 8:
            return GameStatus.VICTORY
        return GameStatus.PLAYING  # Keep playing until all domains complete

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

    def take_damage(self, amount: int, domain: int = None) -> int:
        """
        Reduce HP by amount (can go negative for performance tracking).
        No death penalty - this is training mode.
        Tracks per-domain statistics if domain is provided.
        """
        self.hp -= amount
        self.wrong_answers += 1
        if domain and domain in self.domain_stats:
            self.domain_stats[domain]["wrong"] += 1
        return amount

    def gain_xp(self, amount: int, domain: int = None) -> bool:
        """
        Increase XP by amount.
        Returns True if title changed.
        Tracks per-domain statistics if domain is provided.
        """
        old_title = self.title
        self.xp += amount
        self.correct_answers += 1
        if domain and domain in self.domain_stats:
            self.domain_stats[domain]["correct"] += 1
        new_title = self.title
        return old_title != new_title

    def get_domain_accuracy(self, domain: int) -> float:
        """Calculate accuracy percentage for a specific domain."""
        if domain not in self.domain_stats:
            return 0.0
        stats = self.domain_stats[domain]
        total = stats["correct"] + stats["wrong"]
        if total == 0:
            return 0.0
        return (stats["correct"] / total) * 100

    def heal(self, amount: int) -> int:
        """Restore HP up to max_hp, returning actual healing."""
        actual_heal = min(self.max_hp - self.hp, amount)
        self.hp += actual_heal
        return actual_heal

    def complete_scenario(self, scenario_id: str) -> None:
        """Mark a scenario as completed."""
        if scenario_id not in self.scenarios_completed:
            self.scenarios_completed.append(scenario_id)
