# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.2.0] - 2026-02-13

### Added
- **Save/Resume System**: Progress persists across sessions
  - Auto-saves after each domain completion
  - Saves on Ctrl+C (graceful exit)
  - Name-based save lookup (case-insensitive)
  - Restores HP, XP, domain progress, and per-domain stats
  - Save file automatically deleted on game completion

---

## [1.1.0] - 2025-02-10

### Added
- **Starting Domain Selection**: Choose which domain (1-8) to begin from
  - Skipping domains awards full XP credit (500 XP per skipped domain)
- **HP Regeneration**: Correct answers restore +5 HP (when below 100%)
- **Correct Answer Display**: Wrong answer feedback now shows the correct answer
- **Per-Domain Statistics**: End-game summary shows accuracy breakdown by domain
- **CISSP Exam Readiness Guidance**: Performance-based recommendations at game end
  - 90%+: Strong Candidate
  - 80-89%: Good Foundation
  - 70-79%: More Study Needed
  - <70%: Additional Preparation Recommended
- **MIT License** file for proper GitHub recognition

### Fixed
- Game no longer ends prematurely at 1000 XP — victory requires completing all 8 domains
- XP title thresholds scaled to match full 8-domain game (0-4000 XP range)

---

## [1.0.0] - 2025-02-10

### Added
- Initial release with 144 CISSP scenario-based challenges
- All 8 CISSP domains fully covered (18 scenarios each):
  1. Security and Risk Management
  2. Asset Security
  3. Security Architecture and Engineering
  4. Communication and Network Security
  5. Identity and Access Management
  6. Security Assessment and Testing
  7. Security Operations
  8. Software Development Security
- **Dual Theme System**: Every scenario in two narrative styles
  - Fantasy: Medieval Citadel with magic, scribes, and ancient wards
  - Corporate: Office Space-style satire with IT disasters and TPS reports
- Theme switching mid-game with `[0]` command
- Educational domain introductions for each domain
- Detailed wrong-answer explanations with CISSP references
- Performance tracking (XP, HP, accuracy)
- End-game performance summary
- Cross-platform support (Windows, Mac, Linux)
- Optional colorama support for colored terminal output
