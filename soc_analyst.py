#!/usr/bin/env python3
"""
SOC Analyst Certification Trainer

A scenario-based training tool for Security Operations Center analysts.
Tests knowledge across 6 core SOC domains based on real certifications
(CompTIA CySA+, GIAC GSOC, EC-Council CSA).

Usage:
    python soc_analyst.py

Domains covered:
    1. SIEM Operations & Log Management
    2. Incident Response
    3. Threat Intelligence
    4. Network Security Monitoring
    5. Endpoint Detection & Response
    6. Vulnerability Management
"""

import sys


def main():
    """Main entry point for SOC Analyst certification trainer."""
    try:
        from engine.soc_game import SOCGame
        game = SOCGame()
        game.run()
    except KeyboardInterrupt:
        print("\n\n  Training session ended. Progress saved.")
        sys.exit(0)
    except ImportError as e:
        print(f"\nError loading game modules: {e}")
        print("Make sure you're running from the project root directory.")
        sys.exit(1)


if __name__ == "__main__":
    main()
