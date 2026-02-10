"""
Core game loop and orchestration for The Citadel of the Eight Domains.
"""

import random
from typing import Dict, List, Optional
from .player import Player, GameStatus
from .display import Display
from .input_handler import InputHandler
from .theme_manager import ThemeManager, StoryTheme
from data.ascii_art import (
    TITLE_ART, TITLE_ART_CORPORATE, DOMAIN_BANNERS, DOMAIN_BANNERS_CORPORATE,
    VICTORY_ART, VICTORY_ART_CORPORATE, COMPLETION_ART, COMPLETION_ART_CORPORATE,
    NEEDS_IMPROVEMENT_ART, NEEDS_IMPROVEMENT_ART_CORPORATE
)


class Scenario:
    """
    Represents a single scenario/encounter in the game.

    A scenario presents a situation and choices, with consequences
    based on CISSP knowledge. Supports multiple themes for presenting
    the same CISSP concepts in different narrative styles.
    """

    def __init__(self, data: Dict):
        self.id: str = data['id']
        self.domain: int = data['domain']
        self.xp_reward: int = data.get('xp_reward', 50)
        self.hp_penalty: int = data.get('hp_penalty', 20)
        self.correct_index: int = data['correct_index']  # 0-based
        self.failure_text: str = data.get('failure_text', '')  # Generic fallback
        self.domain_reference: str = data['domain_reference']

        # Theme-aware content
        self.themes: Dict = data.get('themes', {})

        # Legacy support: if no themes dict, treat as fantasy-only
        if not self.themes and 'title' in data:
            self.themes['fantasy'] = {
                'title': data['title'],
                'narrative': data['narrative'],
                'choices': data['choices'],
                'success_text': data['success_text'],
                'failure_texts': self._extract_failure_texts(data['choices'])
            }

        # Keep legacy attributes for backward compatibility during transition
        if 'title' in data:
            self.title = data['title']
            self.narrative = data['narrative']
            self.choices = data['choices']
            self.success_text = data['success_text']

    def _extract_failure_texts(self, choices: List[Dict]) -> Dict[int, str]:
        """Extract failure reasons from legacy choice format."""
        failure_texts = {}
        for i, choice in enumerate(choices):
            if choice.get('failure_reason'):
                failure_texts[i] = choice['failure_reason']
        return failure_texts

    def get_themed_content(self, theme: StoryTheme) -> Dict:
        """
        Return theme-specific content, with fallback to fantasy.

        Returns dict with: title, narrative, choices, success_text, failure_texts
        """
        theme_key = theme.value
        if theme_key in self.themes:
            return self.themes[theme_key]
        # Fallback to fantasy theme
        return self.themes.get('fantasy', {
            'title': getattr(self, 'title', 'SCENARIO'),
            'narrative': getattr(self, 'narrative', ''),
            'choices': getattr(self, 'choices', []),
            'success_text': getattr(self, 'success_text', ''),
            'failure_texts': {}
        })

    def get_failure_text(self, theme: StoryTheme, chosen_index: int) -> str:
        """Get the failure text for a specific wrong choice."""
        content = self.get_themed_content(theme)
        failure_texts = content.get('failure_texts', {})

        # Try theme-specific failure text first
        if chosen_index in failure_texts:
            return failure_texts[chosen_index]

        # Try legacy choice format (failure_reason in choice dict)
        choices = content.get('choices', [])
        if chosen_index < len(choices):
            choice = choices[chosen_index]
            if isinstance(choice, dict) and choice.get('failure_reason'):
                return choice['failure_reason']

        # Fall back to generic failure text
        return self.failure_text


class Game:
    """
    Main game controller that orchestrates the gameplay loop.
    """

    # Configuration
    SCENARIOS_PER_DOMAIN = 10  # How many scenarios to randomly select per domain

    def __init__(self):
        self.display = Display()
        self.input = InputHandler()
        self.theme_manager = ThemeManager()
        self.player: Optional[Player] = None
        self.scenarios: Dict[int, List[Scenario]] = {}  # domain -> all scenarios
        self.selected_scenarios: Dict[int, List[Scenario]] = {}  # domain -> selected for this playthrough
        self.current_scenario: Optional[Scenario] = None
        self._load_scenarios()

    def _load_scenarios(self) -> None:
        """Load all scenario data from the data modules."""
        from data.scenarios import ALL_SCENARIOS

        for domain in range(1, 9):
            self.scenarios[domain] = []

        for scenario_data in ALL_SCENARIOS:
            scenario = Scenario(scenario_data)
            self.scenarios[scenario.domain].append(scenario)

    def run(self) -> None:
        """Main entry point - run the complete game."""
        self.display.clear_screen()
        print(TITLE_ART)

        # Theme selection
        self._select_theme()

        # Introduction
        self._show_introduction()

        # Get player name
        name = self._get_player_name()
        if name is None:
            return

        self.player = Player(name=name)

        # Domain selection (optional - start at a specific domain)
        self._select_starting_domain()

        # Main game loop
        self._game_loop()

    def _select_starting_domain(self) -> None:
        """Allow player to choose which domain to start from."""
        self.display.clear_screen()

        domain_names = {
            1: "Security & Risk Management",
            2: "Asset Security",
            3: "Security Architecture & Engineering",
            4: "Communication & Network Security",
            5: "Identity & Access Management",
            6: "Security Assessment & Testing",
            7: "Security Operations",
            8: "Software Development Security"
        }

        if self.theme_manager.current_theme == StoryTheme.CORPORATE:
            print("\n  " + "=" * 60)
            print("  TRAINING MODULE SELECTION")
            print("  " + "=" * 60)
            print("\n  Which department would you like to start your training in?\n")
        else:
            print("\n  " + "=" * 60)
            print("  DOMAIN SELECTION")
            print("  " + "=" * 60)
            print("\n  Which domain would you like to begin your trials?\n")

        for num, name in domain_names.items():
            print(f"    [{num}] Domain {num}: {name}")

        print(f"\n    [ENTER] Start from the beginning (Domain 1)")
        print()

        while True:
            choice = self.input.get_text("  Select starting domain (1-8 or ENTER for Domain 1): ")
            if choice is None:
                return

            choice = choice.strip()

            # Default to domain 1 if just pressing enter
            if choice == '':
                self.player.current_domain = 1
                break

            # Validate numeric input
            if choice.isdigit():
                domain = int(choice)
                if 1 <= domain <= 8:
                    self.player.current_domain = domain
                    if domain > 1:
                        # Award XP credit for skipped domains (500 XP per domain = 10 scenarios × 50 XP)
                        skipped_domains = domain - 1
                        skipped_xp = skipped_domains * 500
                        self.player.xp = skipped_xp

                        if self.theme_manager.current_theme == StoryTheme.CORPORATE:
                            print(f"\n  Starting at Level {domain}: {domain_names[domain]}")
                            print(f"  (Previous {skipped_domains} module(s) marked as reviewed: +{skipped_xp} XP)")
                        else:
                            print(f"\n  Beginning at Domain {domain}: {domain_names[domain]}")
                            print(f"  (Earlier {skipped_domains} domain(s) acknowledged as mastered: +{skipped_xp} XP)")
                        self.input.wait_for_enter("\n  Press ENTER to continue...")
                    break

            print("  Please enter a number 1-8, or press ENTER for Domain 1.")

        # Show educational introduction for the starting domain
        self._show_domain_introduction(self.player.current_domain)

    def _select_theme(self) -> None:
        """Let the player choose their preferred story theme."""
        print("\n  Choose your story style:\n")
        print("    [1] Medieval Fantasy - The Citadel of the Eight Domains")
        print("        Explore an ancient fortress where scribes guard secrets")
        print("        and magical wards protect the realm's deepest knowledge...")
        print()
        print("    [2] Corporate Office - InfoSec Adventures at Initech")
        print("        Navigate office politics, IT disasters, and TPS reports")
        print("        in this satirical take on corporate security life...")
        print()
        print("    (You can switch themes anytime during scenarios by pressing 0)")
        print()

        while True:
            choice = self.input.get_text("  Select theme (1 or 2): ")
            if choice is None:
                return
            choice = choice.strip()
            if choice == '1':
                self.theme_manager.set_theme(StoryTheme.FANTASY)
                break
            elif choice == '2':
                self.theme_manager.set_theme(StoryTheme.CORPORATE)
                break
            print("  Please enter 1 or 2.")

        self.display.clear_screen()
        self._show_theme_title()

    def _show_theme_title(self) -> None:
        """Display the title art for the current theme."""
        if self.theme_manager.current_theme == StoryTheme.CORPORATE:
            print(TITLE_ART_CORPORATE)
        else:
            print(TITLE_ART)

    def _show_introduction(self) -> None:
        """Display the game's opening narrative (theme-aware)."""
        if self.theme_manager.current_theme == StoryTheme.CORPORATE:
            intro = """
Welcome to Initech Corporation, where "synergy" isn't just a buzzword -
it's a way of life. You've just joined the Information Security team,
and boy, do they need help.

Eight departments await your security guidance. Navigate office politics,
survive compliance audits, and maybe - just maybe - prevent a data breach
that would make the evening news.

Complete your training with flying colors, and you'll earn the coveted
title of Information Systems Security Professional.

Fail... and you'll be explaining to HR why the entire customer database
is now on a hacker forum.

No pressure.
            """
            print(self.display.render_narrative(intro, "YOUR NEW BOSS (via Slack)"))
        else:
            intro = """
The year is unspecified. The place: The Citadel of the Eight Domains.

Within these ancient walls, knowledge is power, and security is sacred.
You have been summoned to prove your worth as a guardian of information.

Eight domains await you, each a trial of wisdom and judgment.
Make wise choices, and you shall ascend to the rank of
Information Systems Security Professional.

Fail... and you shall face THE AUDIT.
            """
            print(self.display.render_narrative(intro, "THE VOICE OF THE CITADEL"))

        self.input.wait_for_enter("\n  Press ENTER to begin your journey...")

    def _get_player_name(self) -> Optional[str]:
        """Prompt player for their character name (theme-aware)."""
        if self.theme_manager.current_theme == StoryTheme.CORPORATE:
            print("\n  What name should we put on your desk nameplate?")
        else:
            print("\n  What name shall the Chronicles record for you, Seeker?")

        name = self.input.get_text("  > ")
        if name:
            if self.theme_manager.current_theme == StoryTheme.CORPORATE:
                print(f"\n  Welcome aboard, {name}. HR says your benefits kick in after 90 days.\n")
            else:
                print(f"\n  Welcome, {name}. May your judgment be sound.\n")
            self.input.wait_for_enter("  Press ENTER to continue...")
        return name

    def _game_loop(self) -> None:
        """Core gameplay loop."""
        while self.player.status == GameStatus.PLAYING:
            self.display.clear_screen()

            # Show HUD
            print(self.display.render_hud(self.player))

            # Get next scenario
            scenario = self._get_next_scenario()
            if scenario is None:
                # No more scenarios in current domain, advance
                if not self._advance_domain():
                    # No more domains, check if we've won
                    break
                continue

            self.current_scenario = scenario

            # Run the scenario
            self._run_scenario(scenario)

            # Check for game end conditions
            if self.player.status != GameStatus.PLAYING:
                break

            # Pause before next scenario
            self.input.wait_for_enter()

        # Game over
        self._show_ending()

    def _select_scenarios_for_domain(self, domain: int) -> None:
        """Randomly select scenarios for a domain from the available pool."""
        all_domain_scenarios = self.scenarios.get(domain, [])
        count = min(self.SCENARIOS_PER_DOMAIN, len(all_domain_scenarios))
        if count > 0:
            self.selected_scenarios[domain] = random.sample(all_domain_scenarios, count)
        else:
            self.selected_scenarios[domain] = []

    def _get_next_scenario(self) -> Optional[Scenario]:
        """Get the next unplayed scenario from the randomly selected pool."""
        domain = self.player.current_domain

        # Select scenarios for this domain if not already done
        if domain not in self.selected_scenarios:
            self._select_scenarios_for_domain(domain)

        for scenario in self.selected_scenarios.get(domain, []):
            if scenario.id not in self.player.scenarios_completed:
                return scenario

        return None

    def _advance_domain(self) -> bool:
        """Move player to the next domain. Returns False if no more domains."""
        if self.player.current_domain < 8:
            self.player.current_domain += 1
            if self.theme_manager.current_theme == StoryTheme.CORPORATE:
                print(self.display.render_narrative(
                    f"Congratulations! You've completed that department's training. "
                    f"Time to move on to Level {self.player.current_domain}. "
                    f"The CISO just sent you a calendar invite...",
                    "HR NOTIFICATION"
                ))
            else:
                print(self.display.render_narrative(
                    f"You have proven yourself in this domain. "
                    f"The path to Domain {self.player.current_domain} opens before you...",
                    "THE CITADEL"
                ))
            self.input.wait_for_enter("\n  Press ENTER to enter the next domain...")
            # Show educational introduction for the new domain
            self._show_domain_introduction(self.player.current_domain)
            return True
        return False

    def _show_domain_introduction(self, domain_num: int) -> None:
        """Display educational content when entering a new domain (theme-aware)."""
        from data.domain_intros import DOMAIN_INTRODUCTIONS

        intro = DOMAIN_INTRODUCTIONS.get(domain_num)
        if intro:
            self.display.clear_screen()
            # Show the domain banner first (theme-aware)
            if self.theme_manager.current_theme == StoryTheme.CORPORATE:
                banner = DOMAIN_BANNERS_CORPORATE.get(domain_num, "")
            else:
                banner = DOMAIN_BANNERS.get(domain_num, "")
            if banner:
                print(banner)

            # Get theme-appropriate intro text
            theme_key = self.theme_manager.get_theme_key()
            if theme_key in intro:
                intro_text = intro[theme_key]["introduction"]
                narrator = intro[theme_key]["narrator"]
            else:
                # Fall back to default (fantasy) intro structure
                intro_text = intro.get("introduction", "")
                narrator = intro.get("narrator", "NARRATOR")

            # Then show the educational introduction
            print(self.display.render_narrative(intro_text, narrator))
            self.input.wait_for_enter("\n  Press ENTER to begin the trials of this domain...")

    def _run_scenario(self, scenario: Scenario) -> None:
        """Execute a single scenario encounter with theme support."""
        while True:
            # Get themed content for current theme
            content = scenario.get_themed_content(self.theme_manager.current_theme)
            title = content.get('title', 'SCENARIO')
            narrative = content.get('narrative', '')
            choices = content.get('choices', [])

            # Extract choice texts (handle both dict and string formats)
            choice_texts = []
            for c in choices:
                if isinstance(c, dict):
                    choice_texts.append(c.get('text', str(c)))
                else:
                    choice_texts.append(str(c))

            # Display scenario narrative
            print(self.display.render_narrative(narrative, title))

            # Show choices with theme toggle hint
            print(self.display.render_choices(choice_texts, show_theme_hint=True), end="")

            # Get player choice
            while True:
                result = self.input.get_choice(len(choices))

                if result[0] == 'quit':
                    if self.input.confirm("  Abandon your quest? [y/N] "):
                        self.player.current_domain = 9  # Force game end
                        return
                    print(self.display.render_choices(choice_texts, show_theme_hint=True), end="")
                    continue

                if result[0] == 'help':
                    self._show_help()
                    print(self.display.render_choices(choice_texts, show_theme_hint=True), end="")
                    continue

                if result[0] == 'status':
                    print(self.display.render_hud(self.player))
                    print(self.display.render_choices(choice_texts, show_theme_hint=True), end="")
                    continue

                if result[0] == 'theme_toggle':
                    # Toggle theme and redisplay the scenario
                    new_theme = self.theme_manager.toggle_theme()
                    self.display.clear_screen()
                    print(self.display.render_hud(self.player))
                    theme_name = self.theme_manager.get_display_name()
                    print(f"\n  [Theme switched to: {theme_name}]\n")
                    break  # Break inner loop to redisplay with new theme

                if result[0] == 'invalid':
                    print("  Invalid choice. Enter 1-4, 0 to switch theme, or 'help'.")
                    print("  > ", end="")
                    continue

                # Valid choice - process it
                chosen = result[1] - 1  # Convert to 0-based

                # Process the choice
                if chosen == scenario.correct_index:
                    self._handle_success(scenario)
                else:
                    self._handle_failure(scenario, chosen)

                # Mark scenario complete
                self.player.complete_scenario(scenario.id)
                return  # Exit the method

            # If we get here, theme was toggled - continue outer loop to redisplay

    def _handle_success(self, scenario: Scenario) -> None:
        """Process a correct answer (theme-aware)."""
        title_changed = self.player.gain_xp(scenario.xp_reward, scenario.domain)

        # HP regeneration: restore 5 HP on correct answer if below max
        hp_healed = 0
        if self.player.hp < self.player.max_hp:
            hp_healed = self.player.heal(5)

        # Get themed success text
        content = scenario.get_themed_content(self.theme_manager.current_theme)
        success_text = content.get('success_text', 'Correct!')

        print(self.display.render_success(
            success_text,
            scenario.xp_reward,
            hp_healed
        ))

        if title_changed:
            if self.theme_manager.current_theme == StoryTheme.CORPORATE:
                print(f"\n  *** PROMOTION! New title: {self.player.title} ***\n")
            else:
                print(f"\n  *** You have earned a new title: {self.player.title} ***\n")

    def _handle_failure(self, scenario: Scenario, chosen: int) -> None:
        """Process an incorrect answer (theme-aware)."""
        self.player.take_damage(scenario.hp_penalty, scenario.domain)

        # Get the specific reasoning for this wrong choice (theme-aware)
        failure_reason = scenario.get_failure_text(self.theme_manager.current_theme, chosen)

        # Get the correct answer text for display
        content = scenario.get_themed_content(self.theme_manager.current_theme)
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
            correct_index + 1,  # Convert to 1-based for display
            correct_text
        ))

    def _show_help(self) -> None:
        """Display help information."""
        help_text = """
  +------------------------------------------------------------------+
  |                         COMMANDS                                 |
  +------------------------------------------------------------------+
  |  [1-4]   - Select a numbered choice                              |
  |  [0]     - Switch story theme (Fantasy/Corporate)                |
  |  help    - Show this help message                                |
  |  status  - Show your current stats                               |
  |  quit    - End your session early                                |
  +------------------------------------------------------------------+
  |                           GOAL                                   |
  +------------------------------------------------------------------+
  |  Complete all Eight Domains to finish your training.             |
  |  Your final score reflects your mastery of CISSP concepts.       |
  |  There is no penalty for wrong answers - this is training!       |
  +------------------------------------------------------------------+
  |                           TIPS                                   |
  +------------------------------------------------------------------+
  |  - Consider all options carefully before choosing                |
  |  - Remember: LIFE SAFETY is always the #1 priority in CISSP      |
  |  - Learn from your mistakes - the Post-Mortem explains why       |
  |  - Press 0 anytime to see the same scenario in a different style |
  +------------------------------------------------------------------+
        """
        print(help_text)

    def _show_ending(self) -> None:
        """Display performance summary at the end of training (theme-aware)."""
        self.display.clear_screen()

        accuracy = self.player.accuracy
        rating = self.player.performance_rating
        is_corporate = self.theme_manager.current_theme == StoryTheme.CORPORATE

        # Choose ending based on performance and theme
        if accuracy >= 80:
            print(VICTORY_ART_CORPORATE if is_corporate else VICTORY_ART)
            if is_corporate:
                print(self.display.render_narrative(
                    f"Outstanding work, {self.player.name}! "
                    f"The board is impressed. You've demonstrated mastery across all departments. "
                    f"The CISO is recommending you for the Security Architect role, "
                    f"and there's talk of actual stock options. "
                    f"Welcome to the elite ranks of Information Systems Security Professionals!",
                    "EXECUTIVE ANNOUNCEMENT"
                ))
            else:
                print(self.display.render_narrative(
                    f"Congratulations, {self.player.name}! "
                    f"You have demonstrated mastery of the Eight Domains. "
                    f"The Citadel recognizes you as an Information Systems Security Professional. "
                    f"Go forth and protect the realm of information!",
                    "THE HIGH COUNCIL"
                ))
        elif accuracy >= 60:
            print(COMPLETION_ART_CORPORATE if is_corporate else COMPLETION_ART)
            if is_corporate:
                print(self.display.render_narrative(
                    f"Good effort, {self.player.name}. You've completed the training program. "
                    f"Your performance review mentions 'shows potential' - which in corporate speak "
                    f"means you passed but should probably review those modules you struggled with. "
                    f"The good news: you still have a job. The better news: free coffee in the break room.",
                    "HR PERFORMANCE REVIEW"
                ))
            else:
                print(self.display.render_narrative(
                    f"Well done, {self.player.name}. You have completed your training. "
                    f"Your understanding of the Eight Domains shows promise, though "
                    f"some areas would benefit from further study. "
                    f"Review the domains where you struggled and return stronger.",
                    "THE COUNCIL OF REVIEW"
                ))
        else:
            print(NEEDS_IMPROVEMENT_ART_CORPORATE if is_corporate else NEEDS_IMPROVEMENT_ART)
            if is_corporate:
                print(self.display.render_narrative(
                    f"{self.player.name}, we need to talk. HR has scheduled a 'development opportunity' "
                    f"meeting for Monday. Your training scores suggest some... gaps. "
                    f"Don't worry - we've all been there. Well, not ME, but you know what I mean. "
                    f"Review the material, retake the training, and maybe lay off the cat videos "
                    f"during the compliance modules.",
                    "YOUR MANAGER (via passive-aggressive email)"
                ))
            else:
                print(self.display.render_narrative(
                    f"{self.player.name}, you have walked the halls of the Citadel "
                    f"and faced its trials. While your journey is complete, "
                    f"the knowledge has not yet taken root. "
                    f"Return to your studies, review the Post-Mortem analyses, "
                    f"and attempt the trials again when you are ready.",
                    "THE MENTORS"
                ))

        # Performance Summary
        print("\n  " + "=" * 60)
        print("  TRAINING PERFORMANCE SUMMARY")
        print("  " + "=" * 60)
        print(f"\n  Seeker: {self.player.name}")
        print(f"  Final Title: {self.player.title}")
        print(f"\n  Total XP Earned: {self.player.xp}")
        print(f"  Correct Answers: {self.player.correct_answers}")
        print(f"  Incorrect Answers: {self.player.wrong_answers}")
        print(f"  Overall Accuracy: {accuracy:.1f}%")
        print(f"  Performance Rating: {rating}")

        # Per-domain breakdown
        print("\n  " + "-" * 60)
        print("  DOMAIN BREAKDOWN")
        print("  " + "-" * 60)

        domain_names = {
            1: "Security & Risk Mgmt",
            2: "Asset Security",
            3: "Security Architecture",
            4: "Network Security",
            5: "Identity & Access Mgmt",
            6: "Assessment & Testing",
            7: "Security Operations",
            8: "Software Dev Security"
        }

        weak_domains = []
        for domain in range(1, 9):
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

        # CISSP Exam Readiness Guidance
        print("\n  CISSP EXAM READINESS")
        print("  " + "-" * 60)

        if accuracy >= 90:
            print("  ★ STRONG CANDIDATE")
            print("  You've demonstrated excellent mastery across all domains.")
            print("  Consider scheduling your CISSP exam soon while the")
            print("  material is fresh. Review any domains below 90% briefly.")
        elif accuracy >= 80:
            print("  ◆ GOOD FOUNDATION")
            print("  You have a solid understanding of CISSP concepts.")
            if weak_domains:
                print("  Focus additional study on these domains before your exam:")
                for d_num, d_name, d_acc in weak_domains:
                    print(f"    - Domain {d_num}: {d_name} ({d_acc:.1f}%)")
            print("  Consider 2-4 more weeks of targeted review.")
        elif accuracy >= 70:
            print("  ◇ MORE STUDY NEEDED")
            print("  You're building a foundation, but need more preparation.")
            if weak_domains:
                print("  Prioritize these domains in your study plan:")
                for d_num, d_name, d_acc in weak_domains:
                    print(f"    - Domain {d_num}: {d_name} ({d_acc:.1f}%)")
            print("  Recommend 4-8 weeks of additional study before the exam.")
        else:
            print("  ○ ADDITIONAL PREPARATION RECOMMENDED")
            print("  The CISSP exam requires comprehensive domain knowledge.")
            print("  Consider these study resources:")
            print("    - Official (ISC)² CISSP Study Guide")
            print("    - CISSP All-in-One Exam Guide (Shon Harris)")
            print("    - Practice exams and study groups")
            print("  Retake this training after completing additional study.")

        print("\n  " + "=" * 60)
        print()
