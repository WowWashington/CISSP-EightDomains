#!/usr/bin/env python3
"""
The Citadel of the Eight Domains
A CISSP Training Adventure

Usage:
    python citadel.py

Commands during gameplay:
    [1-4]   - Select a numbered choice
    help    - Show help message
    status  - Show your current stats
    quit    - Abandon your quest
"""

import sys
import os

# Add the current directory to the path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main():
    """Main entry point for the game."""
    from engine.game import Game

    game = Game()

    try:
        game.run()
    except KeyboardInterrupt:
        print("\n\n  Your journey has been interrupted. Farewell, Seeker.\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
