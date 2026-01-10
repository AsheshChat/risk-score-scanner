# 🛡️ Risk Score Scanner

A lightweight **Python GUI application** that performs security scanning of a target IP or hostname using **Nmap**, analyzes open ports, services, version information, and known vulnerabilities, then calculates an overall **risk score (0–100)** with a corresponding severity label.

Perfect for students, security enthusiasts, penetration testers, and small/medium organizations performing **authorized security assessments**.

**Important**: This tool is intended **exclusively for educational purposes and authorized security testing**. Unauthorized scanning of systems you do not own or have explicit written permission to test is **illegal** in most jurisdictions.

---

## ✨ Key Features

- Modern and intuitive **Tkinter GUI** (simple, cross-platform)
- Input validation & progress feedback during scanning
- Full port scanning with service/version detection (`-sV`)
- Execution of safe/default NSE scripts + vulnerability-oriented scripts
- Parses **Nmap XML output** using `xml.etree.ElementTree`
- Extracts and classifies:
  - Open ports & associated services/versions
  - Potential vulnerabilities (from `vuln`/`vulners` scripts)
  - Misconfigurations & weak credentials warnings
- Calculates a **composite risk score** based on multiple weighted factors
- Color-coded severity classification (Low → Critical)
- Export results to **text** or **JSON** format
- Responsive status bar & error handling

### Current Risk Scoring Logic (v1.0)

The risk score (0–100) is calculated using a **weighted point system**:

| Factor                                  | Max Points | Conditions / Weighting logic                                                                                 | Rationale                                                                 |
|-----------------------------------------|------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Number of open ports                    | 25         | 1–5 → 5–10 pts, 6–15 → 15 pts, 16+ → 25 pts                                                                  | More open ports = larger attack surface                                   |
| Dangerous / high-risk ports open        | 30         | 21(FTP),23(Telnet),445(SMB),3389(RDP), etc. → +8–15 pts each                                                | Historically abused services                                              |
| Outdated/vulnerable service versions    | 20         | Detected old versions known for CVEs (basic keyword matching)                                               | Version fingerprinting gives strong hints                                 |
| Detected vulnerabilities (NSE)          | 40         | `vuln`/`vulners` scripts output → +5–20 pts per issue depending on severity/confidence (CVSS-like)         | Most important risk indicator                                             |
| **BONUS PENALTIES**                     | —          | Anonymous FTP, weak/default creds, self-signed certs, etc. → +5–15 pts                                      | Common misconfigurations that attackers love                              |

**Final severity classification**:

| Score Range | Label          | Color     | Meaning / Recommended Action                                      |
|-------------|----------------|-----------|-------------------------------------------------------------------|
| 0–29        | 🟢 **Low**     | Green     | Acceptable for most environments — routine monitoring            |
| 30–59       | 🟡 **Medium**  | Yellow    | Attention needed — plan remediation within weeks/months          |
| 60–84       | 🟠 **High**    | Orange    | Serious exposure — remediate within days                          |
| 85–100      | 🔴 **Critical**| Red       | Immediate action required — high probability of compromise       |

> **Note**: The scoring is **heuristic/not scientific**. It should be used as an **initial triage indicator**, not as a replacement for professional tools (Nessus, OpenVAS, Qualys, etc.).

---

## 📸 Preview

*(Add real screenshots here once you upload them to the repository)*

**Main window**  
![Main GUI](https://github.com/YOUR_USERNAME/risk-score-scanner/assets/gui-main.png)

**Scan results with risk score**  
![Results view](https://github.com/YOUR_USERNAME/risk-score-scanner/assets/results-example.png)

---

## 🛠️ Installation & Quick Start

### Prerequisites

- **Python 3.8+**
- **[Nmap](https://nmap.org/download.html)** installed and added to system PATH  
  • Windows → official installer  
  • Linux → `sudo apt install nmap` / `sudo dnf install nmap`  
  • macOS → `brew install nmap`
- Recommended: `python-nmap` library (optional, for easier integration in future)

### Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/risk-score-scanner.git

# Enter project directory
cd risk-score-scanner

# (Recommended) Create & activate virtual environment
python3 -m venv venv
source venv/bin/activate          # Linux/macOS
venv\Scripts\activate             # Windows

# Install requirements (very minimal for now)
pip install -r requirements.txt   # Currently almost empty

# Launch the application
python3 risk_score_scanner.py

⚠️ Legal & Ethical Disclaimer
This tool must only be used:

On systems you own
On systems where you have explicit written permission to perform security testing
In accordance with all applicable laws in your jurisdiction

Unauthorized scanning can be considered a computer crime (e.g. CFAA in US, Computer Misuse Act in UK, etc.).
The authors accept no responsibility for misuse or damage caused by this software.

🚀 Future Improvements
🔧 Technical Enhancements

CVE and CVSS score integration (NVD)

Service-based risk weighting (e.g., SSH vs FTP)

Customizable scoring logic

Multiple scan profiles (quick, full, stealth)

📊 Reporting & Export

Export results to PDF, JSON, or CSV

Scan history and comparisons

Executive-style summary reports
