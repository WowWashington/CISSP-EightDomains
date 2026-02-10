# Changelog

All notable changes to The Citadel of the Eight Domains will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.1.0] - 2025-02-10

### Added
- **Starting Domain Selection**: Players can now choose which domain (1-8) to start from
  - Skipping domains awards full XP credit (500 XP per skipped domain)
  - Useful for practicing specific weak domains or continuing after a break
- **HP Regeneration**: Correct answers now restore +5 HP (when below 100%)
- **Correct Answer Display**: Wrong answer feedback now shows the correct answer
- **Per-Domain Statistics**: End-game summary shows accuracy breakdown by domain
- **CISSP Exam Readiness Guidance**: Performance-based recommendations at game end
  - 90%+: "Strong Candidate" - consider scheduling exam
  - 80-89%: "Good Foundation" - review weak domains
  - 70-79%: "More Study Needed" - focused preparation recommended
  - <70%: "Additional Preparation Recommended" - study resources provided

### Fixed
- **Critical**: Game no longer ends prematurely at 1000 XP
  - Victory now requires completing all 8 domains
  - Previously, players could "win" mid-Domain 2
- **XP Title Thresholds**: Scaled to match full 8-domain game (0-4000 XP range)
  - Titles now progress appropriately across the entire game

### Changed
- XP is now purely a scoring mechanism, not a win condition
- Title progression thresholds adjusted for 8-domain gameplay:
  - 0: Novice Scribe
  - 400: Apprentice Guardian
  - 1000: Warden of Secrets
  - 1600: Keeper of the Cipher
  - 2200: Shield Bearer
  - 2800: Master of Controls
  - 3400: High Sentinel
  - 4000: Information Systems Security Professional

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
- **Dual Theme System**: Every scenario available in two narrative styles
  - Fantasy: Medieval Citadel with magic, scribes, and ancient wards
  - Corporate: Office Space-style satire with IT disasters and TPS reports
- Theme switching mid-game with `[0]` command
- Educational domain introductions for each of the 8 domains
- Detailed wrong-answer explanations with CISSP references
- Performance tracking (XP, HP, accuracy)
- End-game performance summary with ratings
- Cross-platform support (Windows, Mac, Linux)
- Optional colorama support for colored terminal output
- `play.bat` for easy Windows launching

### Technical
- Pure Python 3.6+ with zero required dependencies
- Modular scenario architecture for easy expansion
- Theme-aware content delivery system
