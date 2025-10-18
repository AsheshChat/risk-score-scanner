#!/usr/bin/env python3
import subprocess
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

def run_nmap(target):
    try:
        output = subprocess.check_output(["nmap", "-sV", "--script", "vuln", "-oX", "-", target], stderr=subprocess.DEVNULL)
        return output.decode()
    except subprocess.CalledProcessError:
        return None

def parse_nmap_xml(xml_text):
    root = ET.fromstring(xml_text)
    ports = []
    vulns = []
    for host in root.findall('host'):
        for ports_el in host.findall('ports'):
            for port in ports_el.findall('port'):
                state = port.find('state').get('state')
                if state != 'open':
                    continue
                portnum = int(port.get('portid'))
                service = ''
                service_el = port.find('service')
                if service_el is not None:
                    service = service_el.get('name','')
                scripts = []
                for script in port.findall('script'):
                    scripts.append(script.get('id',''))
                    output = script.get('output','')
                    if output:
                        vulns.append((portnum, service, script.get('id',''), output))
                ports.append((portnum, service, scripts))
    return ports, vulns

def score_from_findings(ports, vulns):
    score = 0
    for portnum, service, scripts in ports:
        score += 4
        s = service.lower() if service else ''
        if s in ('ftp','telnet','smb','ms-sql','mssql','mysql','mariadb','postgresql','rdp','ssh','vnc','rpcbind','snmp','redis','memcached'):
            score += 8
        if any('http' in (service or '').lower() for ,service, in [(portnum,service,scripts)]):
            score += 2
    for _ in vulns:
        score += 12
    if score > 100:
        score = 100
    return score

def risk_label(score):
    if score < 30:
        return 'Low'
    if score < 60:
        return 'Medium'
    if score < 85:
        return 'High'
    return 'Critical'

def run_scan():
    target = entry_ip.get().strip()
    if not target:
        messagebox.showwarning('Warning','Enter an IP address or hostname')
        return
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, f'Running scan on {target}...\n')
    root.update()
    xml = run_nmap(target)
    if not xml:
        text_output.insert(tk.END, 'Failed to run nmap. Make sure nmap is installed and you have permission.')
        return
    ports, vulns = parse_nmap_xml(xml)
    score = score_from_findings(ports, vulns)
    label = risk_label(score)
    result = f'Risk Score: {score}/100 ({label})\n\n'
    if ports:
        result += 'Open Ports and Services:\n'
        for p, s, _ in sorted(ports):
            result += f' - {p} : {s or "unknown"}\n'
    else:
        result += 'No open ports found.\n'
    if vulns:
        result += '\nVulnerability Findings:\n'
        for p, s, sid, output in vulns:
            short = output.strip().split('\n')[0]
            result += f' - port {p} ({s or "unknown"}) [{sid}] => {short}\n'
    else:
        result += '\nNo vulnerabilities found.\n'
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, result)

root = tk.Tk()
root.title('Risk Score Calculator')
root.geometry('650x500')
frame = ttk.Frame(root, padding=10)
frame.pack(fill='both', expand=True)
label_ip = ttk.Label(frame, text='Enter IP Address or Hostname:')
label_ip.pack(anchor='w')
entry_ip = ttk.Entry(frame, width=50)
entry_ip.pack(anchor='w', pady=5)
button_scan = ttk.Button(frame, text='Run Scan', command=run_scan)
button_scan.pack(pady=10)
text_output = scrolledtext.ScrolledText(frame, wrap='word', height=20)
text_output.pack(fill='both', expand=True)
root.mainloop()

