#!/usr/bin/env python3
"""
Export all CISSP questions and answers to a text file.
This creates a plain-text study guide from the game scenarios.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scenarios.domain1_security_risk import DOMAIN_1_SCENARIOS
from scenarios.domain2_asset_security import DOMAIN_2_SCENARIOS
from scenarios.domain3_security_architecture import DOMAIN_3_SCENARIOS
from scenarios.domain4_communication_network import DOMAIN_4_SCENARIOS
from scenarios.domain5_identity_access import DOMAIN_5_SCENARIOS
from scenarios.domain6_assessment_testing import DOMAIN_6_SCENARIOS
from scenarios.domain7_security_operations import DOMAIN_7_SCENARIOS
from scenarios.domain8_software_development import DOMAIN_8_SCENARIOS

DOMAIN_NAMES = {
    1: "Security and Risk Management",
    2: "Asset Security",
    3: "Security Architecture and Engineering",
    4: "Communication and Network Security",
    5: "Identity and Access Management",
    6: "Security Assessment and Testing",
    7: "Security Operations",
    8: "Software Development Security"
}

ALL_DOMAINS = [
    (1, DOMAIN_1_SCENARIOS),
    (2, DOMAIN_2_SCENARIOS),
    (3, DOMAIN_3_SCENARIOS),
    (4, DOMAIN_4_SCENARIOS),
    (5, DOMAIN_5_SCENARIOS),
    (6, DOMAIN_6_SCENARIOS),
    (7, DOMAIN_7_SCENARIOS),
    (8, DOMAIN_8_SCENARIOS),
]


def extract_text(text):
    """Clean up multiline text."""
    if not text:
        return ""
    lines = text.strip().split('\n')
    # Remove excessive leading whitespace while preserving structure
    cleaned = []
    for line in lines:
        cleaned.append(line.strip())
    return '\n'.join(cleaned)


def export_questions(output_file):
    """Export all questions to a text file."""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("THE CITADEL OF THE EIGHT DOMAINS\n")
        f.write("CISSP Training Questions - Complete Export\n")
        f.write("=" * 80 + "\n\n")

        f.write("Total Questions: 144 (18 per domain × 8 domains)\n")
        f.write("Covers all 8 CISSP CBK Domains\n")
        f.write("\n" + "=" * 80 + "\n\n")

        question_num = 0

        for domain_num, scenarios in ALL_DOMAINS:
            domain_name = DOMAIN_NAMES[domain_num]

            f.write("\n")
            f.write("#" * 80 + "\n")
            f.write(f"# DOMAIN {domain_num}: {domain_name.upper()}\n")
            f.write("#" * 80 + "\n\n")

            for i, scenario in enumerate(scenarios, 1):
                question_num += 1

                # Get the fantasy theme content (primary)
                themes = scenario.get('themes', {})
                fantasy = themes.get('fantasy', {})
                corporate = themes.get('corporate', {})

                # Basic info
                scenario_id = scenario.get('id', f'd{domain_num}_q{i}')
                correct_index = scenario.get('correct_index', 0)
                domain_ref = scenario.get('domain_reference', '')

                f.write("-" * 80 + "\n")
                f.write(f"QUESTION {question_num} (Domain {domain_num}.{i})\n")
                f.write(f"ID: {scenario_id}\n")
                f.write("-" * 80 + "\n\n")

                # Title
                title = fantasy.get('title', scenario.get('title', 'Untitled'))
                f.write(f"TITLE: {title}\n\n")

                # Narrative/Scenario
                narrative = fantasy.get('narrative', scenario.get('narrative', ''))
                f.write("SCENARIO:\n")
                f.write(extract_text(narrative) + "\n\n")

                # Choices
                choices = fantasy.get('choices', scenario.get('choices', []))
                f.write("CHOICES:\n")
                for j, choice in enumerate(choices, 1):
                    choice_text = choice.get('text', choice) if isinstance(choice, dict) else choice
                    marker = "✓" if j - 1 == correct_index else " "
                    f.write(f"  [{j}] {marker} {choice_text}\n")
                f.write("\n")

                # Correct Answer
                f.write(f"CORRECT ANSWER: {correct_index + 1}\n\n")

                # Success explanation
                success_text = fantasy.get('success_text', scenario.get('success_text', ''))
                if success_text:
                    f.write("WHY CORRECT:\n")
                    f.write(extract_text(success_text) + "\n\n")

                # Wrong answer explanations
                failure_texts = fantasy.get('failure_texts', {})
                if failure_texts:
                    f.write("WHY OTHERS ARE WRONG:\n")
                    for idx, explanation in sorted(failure_texts.items()):
                        if int(idx) != correct_index:
                            f.write(f"\n  Choice {int(idx) + 1}:\n")
                            f.write("  " + extract_text(explanation).replace('\n', '\n  ') + "\n")
                    f.write("\n")

                # Domain reference
                if domain_ref:
                    f.write(f"CISSP REFERENCE: {domain_ref}\n")

                # Corporate theme alternative (brief)
                if corporate:
                    corp_title = corporate.get('title', '')
                    if corp_title:
                        f.write(f"\nALTERNATE THEME (Corporate): {corp_title}\n")

                f.write("\n")

            f.write(f"\n[End of Domain {domain_num}: {domain_name}]\n\n")

        # Summary
        f.write("\n" + "=" * 80 + "\n")
        f.write("SUMMARY\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total Questions Exported: {question_num}\n\n")
        f.write("Questions by Domain:\n")
        for domain_num, scenarios in ALL_DOMAINS:
            f.write(f"  Domain {domain_num}: {len(scenarios)} questions\n")

        f.write("\n" + "-" * 80 + "\n")
        f.write("DISCLAIMER\n")
        f.write("-" * 80 + "\n")
        f.write("""
These training scenarios are educational materials designed to reinforce CISSP
concepts and are NOT official (ISC)² exam questions. While aligned with the
CISSP Common Body of Knowledge (CBK), candidates should also use official
(ISC)² study materials and current exam outlines for exam preparation.

The questions were developed using a structured methodology:
1. Theme-neutral CISSP concepts mapped to each domain
2. Scenario-based questions testing application of knowledge
3. Detailed explanations for correct and incorrect answers
4. Dual-theme presentation (Fantasy/Corporate) for engagement

For validation, cross-reference with:
- Official (ISC)² CISSP CBK Reference
- (ISC)² CISSP Exam Outline
- Recognized study guides (Shon Harris, Mike Chapple, etc.)
""")
        f.write("\n" + "=" * 80 + "\n")
        f.write("END OF EXPORT\n")
        f.write("=" * 80 + "\n")

    return question_num


if __name__ == "__main__":
    output_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "CISSP_Questions_Export.txt"
    )

    print(f"Exporting CISSP questions to: {output_path}")
    count = export_questions(output_path)
    print(f"Successfully exported {count} questions!")
    print(f"\nFile created: {output_path}")
    print("Note: This file is excluded from git tracking.")
