# PortScannerApp - Port Scanning and Vulnerability Mitigation Tool

## What Is Port Scanning and Vulnerability Mitigation?

Port scanning is the process of identifying open ports and services available on a networked system. Security professionals and ethical hackers use port scanning to detect vulnerabilities in a system that could be exploited by attackers. Once open ports are identified, mitigation steps can be taken to secure the system.

This tool performs a comprehensive port scan of a given IP or domain, identifies open ports and services, and provides a report with mitigation steps for securing those services.

## Objective

The objective of this project is to create a tool that:
1. Scans the open ports of a given IP or domain.
2. Detects the services running on these ports.
3. Provides mitigation steps for common vulnerabilities associated with open ports.
4. Generates reports in various formats, including PDF and HTML.

## Skills Learned

- **Port Scanning**: Understanding the process of scanning and detecting open ports.
- **Network Security**: Learning about common vulnerabilities associated with network services.
- **Python Programming**: Writing Python scripts for network scanning and report generation.
- **Kivy GUI**: Implementing a graphical user interface for the command-line tool.
- **Report Generation**: Using `FPDF` and HTML generation libraries to create professional reports.
- **Git & GitHub**: Managing code versions and sharing the project.

## Tools Used

- **Python 3.x**: The programming language used for development.
- **nmap**: A tool for network discovery and security auditing (used for port scanning).
- **Kivy**: Python framework used to build the graphical user interface.
- **FPDF**: A Python library for generating PDF files.
- **colorama**: A Python library for colored terminal text output.
- **os**: A module for interacting with the operating system to create files and directories.

## How It Works

### Port Scanning:
- The tool uses `nmap` to scan a target IP or domain for open ports and running services.
- The scan covers all 65,535 ports (1-65535) and detects the services running on each open port.

### Mitigation Steps:
- Once the open ports are identified, the tool provides a list of common mitigation steps to secure each service.
  - For example, for an open FTP port (21), it suggests using SFTP instead of FTP for secure file transfers.

### Report Generation:
- The user can choose to generate a report in either HTML or PDF format.
- The report includes a summary of the scan, details of the open ports, and the recommended mitigation steps.

### GUI (Graphical User Interface):
- The command-line interface has been enhanced with a GUI using the Kivy framework.
- The GUI allows users to input the target IP or domain, select the report format, and view the results in an interactive window.

## Steps

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Diwakarty/PortScannerApp.git
