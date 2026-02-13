# The Citadel of the Eight Domains

**An immersive CISSP exam preparation game with 144 scenario-based challenges across all 8 security domains.**

## What It Is

A text-based adventure game that transforms dry CISSP study material into engaging, narrative-driven scenarios. Players face real-world security dilemmas wrapped in two distinct themes:

- **Fantasy Mode**: Medieval castle intrigue with magical wards, cursed grimoires, and enchanted vaults
- **Corporate Mode**: Office Space-style satire with frustrated sysadmins, clueless executives, and 3 AM SIEM alerts

## By the Numbers

- **144 unique scenarios** (18 per domain)
- **8 CISSP domains** fully covered
- **2 theme variations** for every question
- **Detailed explanations** for both correct and incorrect answers
- **Save/resume system** — pick up where you left off

## Quick Start

```bash
git clone https://github.com/WowWashington/CISSP-EightDomains.git
cd CISSP-EightDomains
python citadel.py
```

**Windows users:** Just double-click `play.bat`

## Requirements

- Python 3.6 or higher
- Optional: `pip install colorama` for colored terminal output

## Perfect For

- CISSP exam candidates who learn better through storytelling
- Security professionals wanting an engaging refresher
- Anyone who's tired of flashcards and wants to actually *enjoy* studying
- Teams looking for a fun security awareness training alternative

## How It Works

Players navigate through each domain, making security decisions that earn XP for correct answers or cost HP for mistakes. Every scenario teaches a real CISSP concept with immediate feedback explaining *why* the answer matters—whether you're protecting a medieval treasury or securing a corporate data center.

## The Eight Domains

| Domain | Name |
|--------|------|
| 1 | Security and Risk Management |
| 2 | Asset Security |
| 3 | Security Architecture and Engineering |
| 4 | Communication and Network Security |
| 5 | Identity and Access Management (IAM) |
| 6 | Security Assessment and Testing |
| 7 | Security Operations |
| 8 | Software Development Security |

## Content Validation & Methodology

### How Were These Questions Generated?

The 144 CISSP training scenarios were developed using a **structured question bank methodology**:

1. **Theme-Neutral Foundation**: Each question starts as a core CISSP concept with:
   - Clear mapping to a specific CISSP domain (1-8)
   - 4 answer choices with detailed explanations
   - Rationale for why the correct answer is right
   - Explanations for why each wrong answer is incorrect

2. **Dual-Theme Transformation**: Each neutral question is wrapped in two narrative styles:
   - **Fantasy/Medieval**: Citadel, scribes, magic wards, ancient scrolls
   - **Corporate/Office**: IT departments, servers, office politics
   - The correct answer index remains identical across both themes

### What These Questions ARE

- ✅ Aligned with the **(ISC)² CISSP Common Body of Knowledge (CBK)** 8-domain structure
- ✅ Based on publicly available CISSP study materials and security best practices
- ✅ Designed to teach the *thinking process* required for CISSP-style questions
- ✅ Scenario-based questions that test application of concepts

### What These Questions Are NOT

- ❌ Official (ISC)² exam questions (those are proprietary and protected)
- ❌ Guaranteed to match current exam question styles exactly
- ❌ A replacement for official study materials

### How to Validate Accuracy

1. **Cross-Reference with Official Sources:**
   - Compare against the **Official (ISC)² CISSP CBK Reference** (6th Edition)
   - Check against the **(ISC)² CISSP Exam Outline** (publicly available)
   - Review against recognized study guides (Shon Harris, Mike Chapple, etc.)

2. **Expert Review:**
   - Have CISSP-certified professionals review each domain
   - Verify explanations match current industry best practices

### Disclaimer

> *These training scenarios are educational materials designed to reinforce CISSP concepts and are not official (ISC)² exam questions. While aligned with the CISSP CBK, candidates should also use official (ISC)² study materials and current exam outlines for exam preparation.*

## Commands During Gameplay

| Command | Action |
|---------|--------|
| `1-4` | Select a numbered choice |
| `help` | Show help message |
| `status` | Show your current stats |
| '0/C' | Change Theme, anytime | 
| `quit` | Abandon your quest |

## License

MIT License - See [LICENSE](LICENSE) for details.

---

**Learn security. Have fun. Pass the exam.**
