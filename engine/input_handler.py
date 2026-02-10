"""
Input validation and command processing for The Citadel of the Eight Domains.
"""

from typing import Optional, Tuple


class InputHandler:
    """Handles all player input with validation."""

    QUIT_COMMANDS = {'quit', 'exit', 'q', 'bye'}
    HELP_COMMANDS = {'help', 'h', '?'}
    STATUS_COMMANDS = {'status', 'stats', 's'}
    THEME_COMMANDS = {'0', 'c', 'change', 'theme', 'switch'}

    @staticmethod
    def get_choice(num_choices: int, prompt: str = "") -> Tuple[str, Optional[int]]:
        """
        Get and validate a numbered choice from the player.

        Returns:
            Tuple of (command_type, value) where:
            - ('choice', int) for valid numbered choice
            - ('quit', None) for quit command
            - ('help', None) for help command
            - ('status', None) for status command
            - ('invalid', None) for invalid input
        """
        try:
            raw_input = input(prompt).strip().lower()
        except EOFError:
            return ('quit', None)
        except KeyboardInterrupt:
            print()  # Newline after ^C
            return ('quit', None)

        # Check for special commands
        if raw_input in InputHandler.QUIT_COMMANDS:
            return ('quit', None)
        if raw_input in InputHandler.HELP_COMMANDS:
            return ('help', None)
        if raw_input in InputHandler.STATUS_COMMANDS:
            return ('status', None)
        if raw_input in InputHandler.THEME_COMMANDS:
            return ('theme_toggle', None)

        # Try to parse as number
        try:
            choice = int(raw_input)
            if 1 <= choice <= num_choices:
                return ('choice', choice)
            else:
                return ('invalid', None)
        except ValueError:
            return ('invalid', None)

    @staticmethod
    def get_text(prompt: str = "> ", allow_empty: bool = False) -> Optional[str]:
        """
        Get free-form text input from the player.

        Returns:
            The input string, or None if quit command entered.
        """
        try:
            raw_input = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            return None

        if raw_input.lower() in InputHandler.QUIT_COMMANDS:
            return None

        if not allow_empty and not raw_input:
            return InputHandler.get_text(prompt, allow_empty)

        return raw_input

    @staticmethod
    def confirm(prompt: str = "Continue? [Y/n] ") -> bool:
        """Get yes/no confirmation from player."""
        try:
            raw_input = input(prompt).strip().lower()
        except (EOFError, KeyboardInterrupt):
            return False

        return raw_input in ('', 'y', 'yes', 'yeah', 'yep', 'ok', 'sure')

    @staticmethod
    def wait_for_enter(prompt: str = "\n  Press ENTER to continue...") -> None:
        """Wait for the player to press Enter."""
        try:
            input(prompt)
        except (EOFError, KeyboardInterrupt):
            pass
