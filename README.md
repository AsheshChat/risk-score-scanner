# 🛡️ Risk Score Scanner

A simple Python-based GUI tool that scans a target IP or hostname using **Nmap**, detects open ports, potential vulnerabilities, and calculates an overall **risk score (out of 100)** based on the findings.

---

## ⚙️ Features

- GUI built with **Tkinter**
- Uses **Nmap** for service and vulnerability scanning
- Parses Nmap’s XML output using **ElementTree**
- Generates a **risk score and severity label**
- Displays:
  - Open ports & detected services
  - Known vulnerabilities from Nmap scripts

---

## 🖥️ Preview
![GUI Preview](https://github.com/YOUR_USERNAME/risk-score-scanner/assets/preview.png)  
*(Optional: Add a screenshot once uploaded)*

---

## 🧩 Installation

### Prerequisites
- Python 3.x  
- [Nmap](https://nmap.org/download.html) installed and added to PATH  
- Linux / macOS / Windows supported

### Setup
```bash
git clone https://github.com/YOUR_USERNAME/risk-score-scanner.git
cd risk-score-scanner
python3 risk_score_scanner.py

| Score  | Label       |
| ------ | ----------- |
| 0–29   | 🟢 Low      |
| 30–59  | 🟡 Medium   |
| 60–84  | 🟠 High     |
| 85–100 | 🔴 Critical |

⚠️ Disclaimer

This tool is for educational and authorized security assessment purposes only.
Do not use it to scan systems you don’t own or have explicit permission to test.
