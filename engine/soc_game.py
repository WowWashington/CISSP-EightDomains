"""
SOC Analyst certification game engine.

This module extends the base Game class to provide SOC-specific configuration:
- 6 domains instead of 8
- SOC-specific player titles
- Standard professional theme (no fantasy/corporate toggle)
- SOC-specific domain names and introductions
"""

from typing import Dict, List, Optional
from .game import Game, Scenario, SAVE_FILE
from .player import Player, GameStatus
from .display import Display
from .input_handler import InputHandler
from .theme_manager import ThemeManager, StoryTheme


# SOC-specific title art
SOC_TITLE_ART = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ███████╗ ██████╗  ██████╗     █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗████████╗ ║
║   ██╔════╝██╔═══██╗██╔════╝    ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝██╔════╝╚══██╔══╝ ║
║   ███████╗██║   ██║██║         ███████║██╔██╗ ██║███████║██║   ╚████╔╝ ███████╗   ██║    ║
║   ╚════██║██║   ██║██║         ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝  ╚════██║   ██║    ║
║   ███████║╚██████╔╝╚██████╗    ██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████║   ██║    ║
║   ╚══════╝ ╚═════╝  ╚═════╝    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝   ╚═╝    ║
║                                                                              ║
║                    C E R T I F I C A T I O N   T R A I N E R                ║
║                                                                              ║
║                  Security Operations Center Skills Assessment               ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

SOC_VICTORY_ART = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                     ★ ★ ★  C E R T I F I E D  ★ ★ ★                         ║
║                                                                              ║
║                        SOC ANALYST CERTIFICATION                             ║
║                              ACHIEVED                                        ║
║                                                                              ║
║                    You have proven your mastery of:                          ║
║                    • SIEM Operations & Log Management                        ║
║                    • Incident Response                                       ║
║                    • Threat Intelligence                                     ║
║                    • Network Security Monitoring                             ║
║                    • Endpoint Detection & Response                           ║
║                    • Vulnerability Management                                ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

SOC_COMPLETION_ART = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                        TRAINING COMPLETE                                     ║
║                                                                              ║
║              You've completed the SOC Analyst training program.              ║
║              Review the domains where you struggled and try again.           ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

# SOC Domain banners
SOC_DOMAIN_BANNERS = {
    1: """
╔══════════════════════════════════════════════════════════════════════════════╗
║                 DOMAIN 1: SIEM OPERATIONS & LOG MANAGEMENT                   ║
╚══════════════════════════════════════════════════════════════════════════════╝
""",
    2: """
╔══════════════════════════════════════════════════════════════════════════════╗
║                      DOMAIN 2: INCIDENT RESPONSE                             ║
╚══════════════════════════════════════════════════════════════════════════════╝
""",
    3: """
╔══════════════════════════════════════════════════════════════════════════════╗
║                      DOMAIN 3: THREAT INTELLIGENCE                           ║
╚══════════════════════════════════════════════════════════════════════════════╝
""",
    4: """
╔══════════════════════════════════════════════════════════════════════════════╗
║                  DOMAIN 4: NETWORK SECURITY MONITORING                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
""",
    5: """
╔══════════════════════════════════════════════════════════════════════════════╗
║                DOMAIN 5: ENDPOINT DETECTION & RESPONSE                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
""",
    6: """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    DOMAIN 6: VULNERABILITY MANAGEMENT                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
}


class SOCPlayer(Player):
    """
    SOC Analyst player with SOC-specific titles and 6 domains.
    """

    # SOC-specific titles (scaled for 6 domains, ~2400 max XP at 50 XP per scenario)
    TITLES = {
        0: "Trainee Analyst",
        250: "Tier 1 Analyst",
        500: "Tier 2 Analyst",
        900: "Senior Analyst",
        1300: "Threat Hunter",
        1700: "SOC Lead",
        2100: "Incident Commander",
        2400: "Certified SOC Analyst"
    }

    WIN_XP = 2400  # 6 domains × 8 scenarios × 50 XP

    def __init__(self, name: str):
        super().__init__(name)
        # Override domain_stats for 6 domains instead of 8
        self.domain_stats = {i: {"correct": 0, "wrong": 0} for i in range(1, 7)}

    @property
    def status(self) -> GameStatus:
        """SOC has 6 domains instead of 8."""
        if self.current_domain > 6:
            return GameStatus.VICTORY
        return GameStatus.PLAYING


class SOCGame(Game):
    """
    SOC Analyst certification game with 6 domains and professional theme.
    """

    SCENARIOS_PER_DOMAIN = 8  # 8 scenarios per domain for SOC
    TOTAL_DOMAINS = 6

    def __init__(self):
        # Don't call parent __init__ - we need custom initialization
        self.display = Display()
        self.input = InputHandler()
        self.theme_manager = ThemeManager()
        self.player: Optional[SOCPlayer] = None
        self.scenarios: Dict[int, List[Scenario]] = {}
        self.selected_scenarios: Dict[int, List[Scenario]] = {}
        self.current_scenario: Optional[Scenario] = None
        self._load_soc_scenarios()

    def _load_soc_scenarios(self) -> None:
        """Load SOC scenario data."""
        from data.soc_scenarios import ALL_SOC_SCENARIOS

        for domain in range(1, 7):  # 6 domains
            self.scenarios[domain] = []

        for scenario_data in ALL_SOC_SCENARIOS:
            scenario = Scenario(scenario_data)
            if scenario.domain in self.scenarios:
                self.scenarios[scenario.domain].append(scenario)

    def run(self) -> None:
        """Main entry point for SOC certification."""
        self._setup_signal_handler()

        self.display.clear_screen()
        print(SOC_TITLE_ART)

        # No theme selection for SOC - use standard theme
        self.theme_manager.set_theme(StoryTheme.FANTASY)  # Will use 'standard' theme from scenarios

        # Introduction
        self._show_soc_introduction()

        # Get player name and check for saved progress
        name = self._get_soc_player_name()
        if name is None:
            return

        self.player = SOCPlayer(name=name)

        # Check for saved progress
        save_data = self._get_player_save(name)
        if save_data:
            if self._prompt_resume(save_data):
                self._restore_soc_player_state(save_data)
                print(f"\n  Welcome back, {name}! Resuming from Domain {self.player.current_domain}...")
                self.input.wait_for_enter("\n  Press ENTER to continue your training...")
                self._show_soc_domain_introduction(self.player.current_domain)
            else:
                self._delete_player_save(name)
                self._select_soc_starting_domain()
        else:
            self._select_soc_starting_domain()

        # Main game loop
        self._soc_game_loop()

    def _restore_soc_player_state(self, save_data: Dict) -> None:
        """Restore SOC player state from save data."""
        self.player.hp = save_data.get('hp', 100)
        self.player.xp = save_data.get('xp', 0)
        self.player.current_domain = save_data.get('current_domain', 1)
        self.player.scenarios_completed = save_data.get('scenarios_completed', [])
        self.player.correct_answers = save_data.get('correct_answers', 0)
        self.player.wrong_answers = save_data.get('wrong_answers', 0)
        # Restore domain_stats with proper integer keys (6 domains)
        saved_stats = save_data.get('domain_stats', {})
        for key, value in saved_stats.items():
            domain = int(key)
            if domain in self.player.domain_stats:
                self.player.domain_stats[domain] = value

    def _show_soc_introduction(self) -> None:
        """Display SOC certification introduction."""
        intro = """
Welcome to the SOC Analyst Certification Trainer.

This program tests your knowledge across the six core domains of Security
Operations Center work:

  [1] SIEM Operations & Log Management
  [2] Incident Response
  [3] Threat Intelligence
  [4] Network Security Monitoring
  [5] Endpoint Detection & Response
  [6] Vulnerability Management

Each domain presents real-world scenarios based on actual SOC certifications
including CompTIA CySA+, GIAC GSOC, and EC-Council CSA.

Answer correctly to earn XP and advance through the ranks from Trainee Analyst
to Certified SOC Analyst.

Your choices matter. Think like an analyst.
        """
        print(self.display.render_narrative(intro, "SOC TRAINING PROGRAM"))
        self.input.wait_for_enter("\n  Press ENTER to begin your training...")

    def _get_soc_player_name(self) -> Optional[str]:
        """Get player name for SOC certification."""
        print("\n  Enter your name for the training records:")
        name = self.input.get_text("  > ")
        if name:
            print(f"\n  Welcome to the SOC, {name}. Let's see what you've got.\n")
            self.input.wait_for_enter("  Press ENTER to continue...")
        return name

    def _select_soc_starting_domain(self) -> None:
        """Allow selection of starting domain (1-6)."""
        self.display.clear_screen()

        domain_names = {
            1: "SIEM Operations & Log Management",
            2: "Incident Response",
            3: "Threat Intelligence",
            4: "Network Security Monitoring",
            5: "Endpoint Detection & Response",
            6: "Vulnerability Management"
        }

        print("\n  " + "=" * 60)
        print("  DOMAIN SELECTION")
        print("  " + "=" * 60)
        print("\n  Which domain would you like to begin?\n")

        for num, name in domain_names.items():
            print(f"    [{num}] Domain {num}: {name}")

        print(f"\n    [ENTER] Start from the beginning (Domain 1)")
        print()

        while True:
            choice = self.input.get_text("  Select starting domain (1-6 or ENTER for Domain 1): ")
            if choice is None:
                return

            choice = choice.strip()

            if choice == '':
                self.player.current_domain = 1
                break

            if choice.isdigit():
                domain = int(choice)
                if 1 <= domain <= 6:
                    self.player.current_domain = domain
                    if domain > 1:
                        skipped_domains = domain - 1
                        skipped_xp = skipped_domains * 400  # 8 scenarios × 50 XP
                        self.player.xp = skipped_xp
                        print(f"\n  Starting at Domain {domain}: {domain_names[domain]}")
                        print(f"  (Previous {skipped_domains} domain(s) marked as reviewed: +{skipped_xp} XP)")
                        self.input.wait_for_enter("\n  Press ENTER to continue...")
                    break

            print("  Please enter a number 1-6, or press ENTER for Domain 1.")

        self._show_soc_domain_introduction(self.player.current_domain)

    def _show_soc_domain_introduction(self, domain_num: int) -> None:
        """Display SOC domain introduction."""
        from data.soc_domain_intros import SOC_DOMAIN_INTRODUCTIONS

        intro = SOC_DOMAIN_INTRODUCTIONS.get(domain_num)
        if intro:
            self.display.clear_screen()
            banner = SOC_DOMAIN_BANNERS.get(domain_num, "")
            if banner:
                print(banner)

            intro_text = intro.get("introduction", "")
            narrator = intro.get("narrator", "INSTRUCTOR")

            print(self.display.render_narrative(intro_text, narrator))
            self.input.wait_for_enter("\n  Press ENTER to begin the domain scenarios...")

    def _soc_game_loop(self) -> None:
        """Core SOC gameplay loop."""
        while self.player.status == GameStatus.PLAYING:
            self.display.clear_screen()
            print(self.display.render_hud(self.player))

            scenario = self._get_next_scenario()
            if scenario is None:
                if not self._advance_soc_domain():
                    break
                continue

            self.current_scenario = scenario
            self._run_soc_scenario(scenario)

            if self.player.status != GameStatus.PLAYING:
                break

            self.input.wait_for_enter()

        self._show_soc_ending()

    def _advance_soc_domain(self) -> bool:
        """Move to next SOC domain (6 total)."""
        if self.player.current_domain < 6:
            self.player.current_domain += 1
            self._save_state()

            print(self.display.render_narrative(
                f"Excellent work! You've completed Domain {self.player.current_domain - 1}. "
                f"Time to move on to Domain {self.player.current_domain}.",
                "TRAINING COORDINATOR"
            ))
            self.input.wait_for_enter("\n  Press ENTER to continue to the next domain...")
            self._show_soc_domain_introduction(self.player.current_domain)
            return True
        return False

    def _run_soc_scenario(self, scenario: Scenario) -> None:
        """Execute a SOC scenario (uses 'standard' theme)."""
        while True:
            # Get themed content - try 'standard' first, fall back to 'fantasy'
            if 'standard' in scenario.themes:
                content = scenario.themes['standard']
            else:
                content = scenario.get_themed_content(self.theme_manager.current_theme)

            title = content.get('title', 'SCENARIO')
            narrative = content.get('narrative', '')
            choices = content.get('choices', [])

            choice_texts = []
            for c in choices:
                if isinstance(c, dict):
                    choice_texts.append(c.get('text', str(c)))
                else:
                    choice_texts.append(str(c))

            print(self.display.render_narrative(narrative, title))
            print(self.display.render_choices(choice_texts, show_theme_hint=False), end="")

            while True:
                result = self.input.get_choice(len(choices))

                if result[0] == 'quit':
                    if self.input.confirm("  Abandon your training? [y/N] "):
                        self.player.current_domain = 7  # Force game end
                        return
                    print(self.display.render_choices(choice_texts, show_theme_hint=False), end="")
                    continue

                if result[0] == 'help':
                    self._show_soc_help()
                    print(self.display.render_choices(choice_texts, show_theme_hint=False), end="")
                    continue

                if result[0] == 'status':
                    print(self.display.render_hud(self.player))
                    print(self.display.render_choices(choice_texts, show_theme_hint=False), end="")
                    continue

                if result[0] == 'theme_toggle':
                    # No theme toggle for SOC
                    print("  SOC training uses standard professional scenarios.")
                    print(self.display.render_choices(choice_texts, show_theme_hint=False), end="")
                    continue

                if result[0] == 'invalid':
                    print("  Invalid choice. Enter 1-4 or 'help'.")
                    print("  > ", end="")
                    continue

                chosen = result[1] - 1

                if chosen == scenario.correct_index:
                    self._handle_soc_success(scenario, content)
                else:
                    self._handle_soc_failure(scenario, content, chosen)

                self.player.complete_scenario(scenario.id)
                return

    def _handle_soc_success(self, scenario: Scenario, content: Dict) -> None:
        """Process correct answer for SOC scenario."""
        title_changed = self.player.gain_xp(scenario.xp_reward, scenario.domain)

        hp_healed = 0
        if self.player.hp < self.player.max_hp:
            hp_healed = self.player.heal(5)

        success_text = content.get('success_text', 'Correct!')

        print(self.display.render_success(
            success_text,
            scenario.xp_reward,
            hp_healed
        ))

        if title_changed:
            print(f"\n  *** PROMOTION! New rank: {self.player.title} ***\n")

    def _handle_soc_failure(self, scenario: Scenario, content: Dict, chosen: int) -> None:
        """Process incorrect answer for SOC scenario."""
        self.player.take_damage(scenario.hp_penalty, scenario.domain)

        failure_texts = content.get('failure_texts', {})
        failure_reason = failure_texts.get(chosen, scenario.failure_text)

        choices = content.get('choices', [])
        correct_index = scenario.correct_index
        correct_text = ""
        if correct_index < len(choices):
            choice = choices[correct_index]
            if isinstance(choice, dict):
                correct_text = choice.get('text', str(choice))
            else:
                correct_text = str(choice)

        print(self.display.render_failure(
            failure_reason,
            scenario.hp_penalty,
            scenario.domain_reference,
            correct_index + 1,
            correct_text
        ))

    def _show_soc_help(self) -> None:
        """Display SOC-specific help."""
        help_text = """
  +------------------------------------------------------------------+
  |                         COMMANDS                                 |
  +------------------------------------------------------------------+
  |  [1-4]   - Select a numbered choice                              |
  |  help    - Show this help message                                |
  |  status  - Show your current stats                               |
  |  quit    - End your session early                                |
  +------------------------------------------------------------------+
  |                           GOAL                                   |
  +------------------------------------------------------------------+
  |  Complete all Six Domains to finish your SOC training.           |
  |  Your final score reflects your readiness for SOC certification. |
  +------------------------------------------------------------------+
  |                           TIPS                                   |
  +------------------------------------------------------------------+
  |  - Consider all options carefully before choosing                |
  |  - Think about real-world SOC best practices                     |
  |  - Learn from your mistakes - the explanations are detailed      |
  |  - MTTD and MTTR matter - prioritize effectively                 |
  +------------------------------------------------------------------+
        """
        print(help_text)

    def _show_soc_ending(self) -> None:
        """Display SOC training performance summary."""
        if self.player:
            self._delete_player_save(self.player.name)

        self.display.clear_screen()

        accuracy = self.player.accuracy
        rating = self.player.performance_rating

        if accuracy >= 80:
            print(SOC_VICTORY_ART)
            print(self.display.render_narrative(
                f"Outstanding work, {self.player.name}! "
                f"You've demonstrated mastery across all SOC domains. "
                f"You're ready to take on SOC certification exams like CySA+, GSOC, or CSA. "
                f"Welcome to the ranks of Certified SOC Analysts!",
                "SOC DIRECTOR"
            ))
        elif accuracy >= 60:
            print(SOC_COMPLETION_ART)
            print(self.display.render_narrative(
                f"Good effort, {self.player.name}. You've completed the training program. "
                f"Your performance shows promise, but some areas need more work. "
                f"Review the domains where you struggled and try again.",
                "TRAINING COORDINATOR"
            ))
        else:
            print(SOC_COMPLETION_ART)
            print(self.display.render_narrative(
                f"{self.player.name}, you've completed the training but your scores "
                f"indicate you need more preparation. Focus on understanding the WHY "
                f"behind SOC decisions, not just the WHAT. Review and retry.",
                "TRAINING COORDINATOR"
            ))

        # Performance Summary
        print("\n  " + "=" * 60)
        print("  SOC ANALYST TRAINING PERFORMANCE")
        print("  " + "=" * 60)
        print(f"\n  Analyst: {self.player.name}")
        print(f"  Final Rank: {self.player.title}")
        print(f"\n  Total XP Earned: {self.player.xp}")
        print(f"  Correct Answers: {self.player.correct_answers}")
        print(f"  Incorrect Answers: {self.player.wrong_answers}")
        print(f"  Overall Accuracy: {accuracy:.1f}%")
        print(f"  Performance Rating: {rating}")

        # Domain breakdown
        print("\n  " + "-" * 60)
        print("  DOMAIN BREAKDOWN")
        print("  " + "-" * 60)

        domain_names = {
            1: "SIEM Operations",
            2: "Incident Response",
            3: "Threat Intelligence",
            4: "Network Security",
            5: "Endpoint Detection",
            6: "Vulnerability Mgmt"
        }

        weak_domains = []
        for domain in range(1, 7):
            stats = self.player.domain_stats[domain]
            total = stats["correct"] + stats["wrong"]
            if total > 0:
                dom_accuracy = (stats["correct"] / total) * 100
                status = "✓" if dom_accuracy >= 75 else "✗"
                print(f"  {status} Domain {domain}: {domain_names[domain]:<22} "
                      f"{stats['correct']:>2}/{total:<2} ({dom_accuracy:>5.1f}%)")
                if dom_accuracy < 75:
                    weak_domains.append((domain, domain_names[domain], dom_accuracy))

        print("\n  " + "=" * 60)

        # Certification Readiness
        print("\n  SOC CERTIFICATION READINESS")
        print("  " + "-" * 60)

        if accuracy >= 90:
            print("  ★ STRONG CANDIDATE")
            print("  You're well-prepared for SOC certification exams.")
            print("  Consider: CompTIA CySA+, GIAC GSOC, or EC-Council CSA")
        elif accuracy >= 80:
            print("  ◆ GOOD FOUNDATION")
            print("  You have solid SOC fundamentals.")
            if weak_domains:
                print("  Focus additional study on:")
                for d_num, d_name, d_acc in weak_domains:
                    print(f"    - Domain {d_num}: {d_name} ({d_acc:.1f}%)")
        elif accuracy >= 70:
            print("  ◇ MORE STUDY NEEDED")
            print("  You understand the basics but need more preparation.")
            if weak_domains:
                print("  Prioritize these domains:")
                for d_num, d_name, d_acc in weak_domains:
                    print(f"    - Domain {d_num}: {d_name} ({d_acc:.1f}%)")
        else:
            print("  ○ ADDITIONAL PREPARATION RECOMMENDED")
            print("  Review SOC fundamentals and retake this training.")
            print("  Resources: SANS SEC450, CompTIA CySA+ Study Guide")

        print("\n  " + "=" * 60)
        print()
