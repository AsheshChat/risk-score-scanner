# 🛡️ Risk Score Scanner

**Educational cybersecurity assessment tool**  
A lightweight GUI application designed to help security practitioners, students, and blue/purple team members quickly evaluate the attack surface and basic risk level of systems using Nmap.

The tool performs automated scanning, service detection, vulnerability script execution, and generates a **heuristic risk score (0–100)** together with severity classification — making it easier to understand exposure at a glance.

**Primary purpose**:  
Educational use • Security awareness training • Initial triage & quick security posture checks  
(Always with proper authorization!)

**Important legal notice**:  
This tool may **only** be used on systems you own or on systems where you have **explicit written permission** to perform security testing.  
Unauthorized scanning is a criminal offense in most jurisdictions.

---

## 🎯 Main Security Assessment Features

- Simple, cross-platform graphical interface (Tkinter)
- Target validation & user-friendly scanning workflow
- Service & version detection (`-sV`)
- Execution of safe & vulnerability-oriented NSE scripts
- Extraction & classification of:
  - Exposed services & versions
  - Potentially vulnerable services
  - Common misconfigurations & dangerous exposures
- Heuristic **risk scoring** based on multiple security-relevant factors
- Clear severity classification with recommended urgency
- Visual feedback during scanning

### Current Risk Scoring Approach (heuristic – v1.0)

| Security Factor                         | Max Points | Trigger conditions                                      | Security context                              |
|-----------------------------------------|------------|---------------------------------------------------------|-----------------------------------------------|
| Number of open ports                    | 25         | More ports = significantly larger attack surface       | Classic exposure metric                       |
| Presence of high-risk / legacy ports    | 30         | FTP, Telnet, SMBv1, RDP, etc.                           | Services with history of severe abuse         |
| Outdated/vulnerable software versions   | 20         | Old versions with known public exploits                 | Strong exploitation signal                    |
| Positive vulnerability script findings  | 40         | `vuln`, `vulners`, `http-vuln-*`, etc. results         | Most important real-world risk indicator      |
| Common dangerous misconfigurations      | bonus      | Anonymous FTP, default creds, weak protocols, etc.      | Frequent paths of compromise                  |

**Resulting severity levels**:

| Score       | Label          | Color     | Recommended security action                           |
|-------------|----------------|-----------|-------------------------------------------------------|
| 0–29        | 🟢 Low         | Green     | Routine monitoring, good general hygiene              |
| 30–59       | 🟡 Medium      | Yellow    | Plan remediation – medium-term priority               |
| 60–84       | 🟠 High        | Orange    | Active remediation needed – short-term priority       |
| 85–100      | 🔴 Critical    | Red       | Immediate action required – very high exposure        |

> **Important**: This is **not** a professional vulnerability scanner.  
> The scoring is heuristic/educational and should be treated as a **conversation starter**, not a definitive security assessment.

---

## 🛠️ Quick Start (for authorized testing only)

### Requirements

- Python 3.8+
- [Nmap](https://nmap.org/download.html) installed and available in system PATH

### Basic usage

git clone https://github.com/YOUR_USERNAME/risk-score-scanner.git
cd risk-score-scanner

# Optional but recommended
python3 -m venv venv
source venv/bin/activate           # Linux/macOS
# or on Windows: venv\Scripts\activate

pip install -r requirements.txt    # currently very minimal

python3 risk_score_scanner.py


# ⚠️ Strict Legal & Ethical Boundaries

**This tool may only be used:**

- On systems you **legally own**, or
- On systems where you have **current, explicit, written permission** to perform security testing

**Unauthorized use** (even "just to check") is considered a **computer crime** in most jurisdictions, including but not limited to:

- **CFAA** (Computer Fraud and Abuse Act – United States)
- **Computer Misuse Act** (United Kingdom)
- Similar legislation in EU countries, Australia, Canada, and many others

**The project authors accept absolutely no responsibility** for any misuse, damage, legal consequences, or other negative outcomes.

**Use responsibly. Use ethically. Get permission in writing.**

---

## 🚀 Planned Security-focused Improvements

### Better risk understanding

- Real **CVSS / CVE** integration (automatic NVD lookup)
- Service-specific risk profiles  
  (`SSH` vs `RDP` vs `MongoDB` vs `SMB` vs …)
- Different scoring presets for various environments  
  (`IoT` • `OT` • `enterprise` • `cloud`)

### More useful security reporting

- Executive-style **one-pagers**
- **Top 5 critical findings** highlighting
- Change tracking between scans (**hardening validation**)
- Export formats:  
  • PDF  
  • JSON  
  • simple Markdown report

### Enhanced usability for security practitioners

- Multiple scan **personas**  
  `Quick check` • `Thorough audit` • `Vulnerability focus`
- Better visualization of **most concerning findings**
- **Dark mode** for late-night incident response sessions 😄

---

Contributions focused on **improving security value** and **responsible usage** are very welcome!  
❤️ Thank you for helping keep this project ethical and useful.
