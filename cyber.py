import nmap
from fpdf import FPDF
import os
from colorama import Fore, Style, init

# Initialize colorama
init()

# Function to perform the port scan
def scan_ports(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, '1-65535', arguments='-sV')  # Added -sV for service detection
    return scanner

# Function to generate mitigation steps based on open ports
def generate_mitigation_steps(open_ports):
    mitigation_steps = []
    for port in open_ports:
        if "21/tcp" in port:
            mitigation_steps.append("Port 21 (FTP): Disable FTP or switch to SFTP for secure file transfers.")
        if "22/tcp" in port:
            mitigation_steps.append("Port 22 (SSH): Use key-based authentication and disable root login.")
        if "23/tcp" in port:
            mitigation_steps.append("Port 23 (Telnet): Disable Telnet and use SSH for secure remote connections.")
        if "25/tcp" in port:
            mitigation_steps.append("Port 25 (SMTP): Use encryption (e.g., STARTTLS) for email communication.")
        if "53/tcp" in port:
            mitigation_steps.append("Port 53 (DNS): Secure DNS servers and implement rate limiting.")
        if "80/tcp" in port:
            mitigation_steps.append("Port 80 (HTTP): Redirect to HTTPS for secure communication.")
        if "443/tcp" in port:
            mitigation_steps.append("Port 443 (HTTPS): Ensure SSL/TLS configuration is up-to-date.")
        if "139/tcp" in port or "445/tcp" in port:
            mitigation_steps.append("Ports 139 and 445 (SMB): Disable SMBv1 and restrict access to trusted hosts.")
        if "3306/tcp" in port:
            mitigation_steps.append("Port 3306 (MySQL): Secure with strong credentials and restrict access.")
    return list(set(mitigation_steps))  # Remove duplicates

# Function to save results to an HTML file
def generate_html(scan_summary, mitigation_steps, common_ports_info, filename="scan_report.html"):
    with open(filename, "w") as file:
        file.write("<html><head><title>Vulnerability Scan Report</title></head><body>")
        file.write("<h1>Vulnerability Scan Report</h1>")
        file.write(f"<h2>Scan Summary:</h2><pre>{scan_summary}</pre>")
        file.write("<h2>Common Ports Information:</h2><ul>")
        for port_info in common_ports_info:
            file.write(f"<li>{port_info}</li>")
        file.write("</ul>")
        file.write("<h2>Mitigation Steps:</h2><ul>")
        for step in mitigation_steps:
            file.write(f"<li>{step}</li>")
        file.write("</ul></body></html>")
    print(f"HTML report generated: {filename}")

# Function to save results and mitigations to a PDF
def generate_pdf(scan_summary, mitigation_steps, common_ports_info, filename="scan_report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Vulnerability Scan Report", ln=True, align='C')

    # Scan summary
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=scan_summary)

    # Common Ports Information
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Common Ports Information:", ln=True)
    pdf.set_font("Arial", size=12)
    for port_info in common_ports_info:
        pdf.multi_cell(0, 10, txt=f"- {port_info}")

    # Mitigation steps
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Mitigation Steps:", ln=True)
    pdf.set_font("Arial", size=12)
    for step in mitigation_steps:
        pdf.multi_cell(0, 10, txt=f"- {step}")

    # Save the PDF
    pdf.output(filename)
    print(f"PDF report generated: {filename}")

def main():
    print(Fore.CYAN + "Welcome to the Enhanced Port Scanner" + Style.RESET_ALL)
    target = input("Enter the target IP or domain: ").strip()

    print(Fore.YELLOW + "Starting scan..." + Style.RESET_ALL)
    scanner = scan_ports(target)

    # Check if the target was scanned successfully
    if target not in scanner.all_hosts():
        print(Fore.RED + f"No results found for {target}. Please check the input and try again." + Style.RESET_ALL)
        return

    # Extract scan details
    scan_results = scanner[target]
    state = scan_results.state()
    open_ports = []
    services = []
    for proto in scan_results.all_protocols():
        for port, port_data in scan_results[proto].items():
            open_ports.append(f"{port}/{proto}")
            service = port_data.get("name", "Unknown")
            services.append((port, proto, service))

    # Display results
    print(Fore.GREEN + "Scan Results:" + Style.RESET_ALL)
    print(f"State: {state}")
    for port, proto, service in services:
        print(Fore.GREEN + f"Open Port: {port}/{proto} ({service})" + Style.RESET_ALL)

    # Generate mitigation steps
    mitigation_steps = generate_mitigation_steps(open_ports)

    # Common Ports Information
    common_ports_info = get_common_ports_info()

    # Generate reports
    scan_summary = f"State: {state}\n" + "\n".join([f"Open Port: {port}/{proto} ({service})" for port, proto, service in services])
    generate_pdf(scan_summary, mitigation_steps, common_ports_info)
    generate_html(scan_summary, mitigation_steps, common_ports_info)

def get_common_ports_info():
    """Return detailed information for common ports."""
    return [
        "Port 21/tcp: ftp - File Transfer Protocol for transferring files.",
        "Port 22/tcp: ssh - Secure Shell for secure remote access.",
        "Port 23/tcp: telnet - Unsecured remote access (obsolete).",
        "Port 25/tcp: smtp - General port for a service.",
        "Port 53/tcp: domain - General port for a service.",
        "Port 80/tcp: http - Web traffic without encryption.",
        "Port 111/tcp: rpcbind - General port for a service.",
        "Port 139/tcp: netbios-ssn - General port for a service.",
        "Port 445/tcp: netbios-ssn - General port for a service.",
        "Port 512/tcp: exec - General port for a service.",
        "Port 513/tcp: login - General port for a service.",
        "Port 514/tcp: tcpwrapped - General port for a service.",
        "Port 1099/tcp: java-rmi - General port for a service.",
        "Port 1524/tcp: bindshell - General port for a service.",
        "Port 2049/tcp: nfs - General port for a service.",
        "Port 2121/tcp: ftp - File Transfer Protocol for transferring files.",
        "Port 3306/tcp: mysql - Database management system.",
        "Port 3632/tcp: distccd - General port for a service.",
        "Port 5432/tcp: postgresql - General port for a service.",
        "Port 5900/tcp: vnc - General port for a service.",
        "Port 6000/tcp: X11 - General port for a service.",
        "Port 6667/tcp: irc - General port for a service.",
        "Port 6697/tcp: irc - General port for a service.",
        "Port 8009/tcp: ajp13 - General port for a service.",
        "Port 8180/tcp: http - Web traffic without encryption.",
        "Port 8787/tcp: drb - General port for a service.",
        "Port 34868/tcp: nlockmgr - General port for a service.",
        "Port 38004/tcp: mountd - General port for a service.",
        "Port 47905/tcp: status - General port for a service.",
        "Port 51123/tcp: java-rmi - General port for a service."
    ]

if __name__ == "__main__":
    main()
