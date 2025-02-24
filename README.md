Port Scanner & Vulnerability Report Generator

📌 What is this project?

This project is an enhanced port scanner that scans a target system for open ports and provides a detailed security assessment. It generates human-readable reports in HTML and PDF formats, including mitigation steps for detected vulnerabilities.

🎯 Why did I create this?

I created this tool because existing port scanners lack key features that improve security assessments. This scanner provides: have port scanners, but this tool addresses key issues by:

Automating report generation for easy analysis.

Providing mitigation steps for detected vulnerabilities.

Explaining open ports by detailing their function and potential security risks.
This tool is designed to help penetration testers, security professionals, and system administrators better understand and secure their networks.

🚀 Features

Full Port Scanning: Scans all 65,535 ports for a target IP or domain.

Service Detection: Identifies services running on open ports.

Automated Mitigation Suggestions: Provides security recommendations based on open ports.

Report Generation:

PDF format 📄

HTML format 🌐

User-Friendly Output: Displays results in a structured and easy-to-understand way.

Cross-Platform Support: Works on Windows, Linux, and macOS.

📽️ Demo Video

(To be added after upload)

🖼️ Screenshots

(To be added after capturing screenshots)

🔮 Future Enhancements

GUI Implementation using Kivy for a more user-friendly experience.

AI Integration to suggest smarter security fixes.

Advanced Features:

Web scanning functionality.

More vulnerability detection techniques.

Export results in more formats (JSON, CSV, etc.).

🛠 Installation & Usage

1️⃣ Clone the Repository

git clone https://github.com/your-username/port-scanner.git
cd port-scanner

2️⃣ Create a Virtual Environment (Recommended)

python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the Scanner

python scanner.py

5️⃣ Enter Target IP or Domain

Once the program starts, enter the target IP or domain when prompted.

📜 Requirements

Python 3.x

nmap (Ensure Nmap is installed on your system)

Required Python libraries (install via requirements.txt):

nmap

fpdf

colorama

os

📄 License

This project is licensed under the MIT License.

🤝 Contributing

Contributions are welcome! Feel free to fork the repository, create a new branch, and submit a pull request.

📩 Contact

For any issues or suggestions, open an issue on GitHub or reach out via email.

🔒 Stay secure! Happy hacking! 🛡️

