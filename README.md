# PortFort: Vulnerability Scanner & Report Generator with Mitigation Steps

## 📌 What is this project?

This project is an **enhanced port scanner** that scans a target system for open ports and provides a detailed **security assessment**. It generates **human-readable reports** in HTML and PDF formats, including mitigation steps for detected vulnerabilities.

## 🎯 Why did I create this?

I created this tool because existing port scanners lack key features that improve security assessments. This scanner provides:

- **Automated report generation** for easy analysis.
- **Mitigation steps** for detected vulnerabilities.
- **Explanations of open ports**, detailing their function and potential security risks.

This tool is designed to help **penetration testers, security professionals, and system administrators** better understand and secure their networks.

---

## 🚀 Features

- **Full Port Scanning**: Scans all **65,535** ports for a target IP or domain.
- **Service Detection**: Identifies services running on open ports.
- **Automated Mitigation Suggestions**: Provides security recommendations based on open ports.
- **Report Generation**:
  - **PDF format** 📄
  - **HTML format** 🌐
- **User-Friendly Output**: Displays results in a structured and easy-to-understand way.
- **Cross-Platform Support**: Works on **Windows, Linux, and macOS**.

---

## 📽️ Demo Video

https://github.com/user-attachments/assets/cd37b5d9-2439-4f41-882c-29169103d389

---

## 🖼️ Screenshots
![2](https://github.com/user-attachments/assets/b82e9fe9-ad33-4a50-a6c2-d0cb3856654c)

![4](https://github.com/user-attachments/assets/6ad344f6-ed86-47b6-995a-afc83bae4c26)

![5](https://github.com/user-attachments/assets/33bd2e14-4633-4c3c-b2a3-b4bbc6ee7299)

---

## 📽️ Demo Reports

- **PDF Report Demo**: [View Sample Report](https://github.com/Diwakarty/PortFort/blob/main/scan_report.pdf) 📄  
- **HTML Report Demo**: [View Sample Report]
---

## 🔮 Future Enhancements

- **GUI Implementation** using Kivy for a more user-friendly experience.
- **AI Integration** to suggest smarter security fixes.
- **Advanced Features**:
  - Web scanning functionality.
  - More vulnerability detection techniques.
  - Export results in more formats (JSON, CSV, etc.).

---

## 🛠 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/port-scanner.git
cd port-scanner
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Scanner

```bash
python scanner.py
```

### 5️⃣ Enter Target IP or Domain

Once the program starts, enter the target IP or domain when prompted.

---

## 📜 Requirements

- **Python 3.x**
- **nmap** (Ensure Nmap is installed on your system)
- Required Python libraries (install via `requirements.txt`):
  - `nmap`
  - `fpdf`
  - `colorama`
  - `os`

---

## 📩 Contact

For any issues or suggestions, open an **issue** reach out via email:
📧 diw.ig8@gmail.com

---

🔒 **Stay secure! Happy hacking!** 🛡️

