# Automated Network Vulnerability Scanner (Student Project)

## Overview

This project is a Python-based automated network vulnerability scanner built as a learning exercise to understand how network scanning, service enumeration, and basic risk assessment work in practice.

The tool uses Nmap to scan a target system, parses the XML output, and presents the results through a simple graphical user interface (GUI) built with Tkinter. It identifies open ports, running services, basic vulnerability script findings, and calculates a basic risk score based on the scan results.

This project is intended for educational and defensive security purposes only.

## Features

* Automated port scanning and service detection using Nmap
* Executes Nmap vulnerability scripts (--script vuln)
* Parses Nmap XML output programmatically
* Displays:
   * Open ports and detected services
   * Vulnerability script findings (if any)
* Calculates a simple risk score (0–100) based on:
   * Number of open ports
   * Type of exposed services
   * Presence of vulnerability script results
* Categorizes risk as Low, Medium, High, or Critical
* User-friendly GUI interface using Tkinter

## How It Works (High Level)

1. The user enters an IP address or hostname into the GUI.
2. The script runs Nmap using:
   * Service detection (-sV)
   * Vulnerability scripts (--script vuln)
   * XML output (-oX -)
3. The XML output is parsed using Python's xml.etree.ElementTree.
4. The program:
   * Identifies open ports
   * Extracts detected services
   * Collects vulnerability script outputs (if present)
5. A basic risk score is calculated using simple heuristics:
   * Open ports increase the score
   * Common high-risk services increase the score further
   * Detected vulnerability scripts add more weight
6. Results are displayed in the GUI in a readable format.

## Technologies Used

* Python 3
* Nmap
* Tkinter (GUI)
* subprocess (to execute Nmap)
* xml.etree.ElementTree (XML parsing)

## Setup & Usage

### Prerequisites

* Python 3 installed
* Nmap installed and accessible from the command line
* Linux or macOS recommended (tested with Kali Linux)

### Running the Tool
```bash
python3 scanner.py
```

1. Enter an IP address or hostname (e.g., 127.0.0.1)
2. Click Run Scan
3. View scan results and calculated risk score in the output window

### Example Output
```
Risk Score: 62/100 (High)

Open Ports and Services:
 - 22 : ssh
 - 80 : http

Vulnerability Findings:

 - port 80 (http) [http-vuln-cveXXXX] => Potential vulnerability detected
```

## Risk Scoring Logic (Simplified)

* Each open port adds to the score
* Common services (e.g., SSH, FTP, HTTP, SMB, databases) add more weight
* Each vulnerability script result increases the score
* Final score is capped at 100
* Risk levels:
   * Low: < 30
   * Medium: 30–59
   * High: 60–84
   * Critical: ≥ 85

The scoring system is not industry-standard and is meant purely for learning and experimentation.

## Limitations

* Not a replacement for professional vulnerability scanners
* Risk scoring is heuristic-based and not CVSS-accurate
* Depends entirely on Nmap script output
* No authentication testing or deep exploitation
* GUI is basic and not optimized for large scans

## What I Learned

* How Nmap works internally and how to automate it
* Parsing XML data programmatically in Python
* Basics of service enumeration and vulnerability awareness
* Designing simple GUIs using Tkinter
* Translating technical scan results into human-readable output

## Future Improvements

* Integrate CVSS scoring for vulnerabilities
* Export scan results to a report file (PDF/JSON)
* Improve GUI layout and usability
* Add support for scanning multiple targets
* Add logging and error handling

## Ethical Disclaimer

This tool is intended only for educational use and authorized testing.
Do not scan systems you do not own or have explicit permission to test.



