# 🔍 Python Port Scanner (Beginner Friendly)

A simple **Python Port Scanner** for learning **Networking + Cybersecurity basics**.

This tool scans common TCP ports on a target **IP address / domain** and shows whether ports are **OPEN** or **CLOSED**.  
(Optional) It can also perform **Banner Grabbing** to identify services.

---

## 🚀 What This Tool Does

✅ Scans open ports on a target IP / domain  
✅ Identifies common services (FTP, SSH, HTTP, HTTPS, MySQL, etc.)  
✅ Shows OPEN / CLOSED status  
✅ (Optional) Banner grabbing for service info  
✅ (Optional) Threading for faster scanning  

---

## 🧠 Concept (Tamil + English Explanation)

**Port Scanner na enna?**  
Oru computer-la **evlo doors (ports)** open-aa irukku nu check panradhu.

- **IP address** = building address  
- **Port** = door number  
- **Service** = inside running application (SSH / Web / DB)

If port OPEN:
➡️ Connection success ✅

If port CLOSED:
➡️ Connection fail ❌

---

## ⚙️ Tech Stack

- **Python 3**
- `socket` library (built-in)
- Optional: `threading`

---

## 📌 Common Ports Scanned

| Port | Service |
|------|---------|
| 21   | FTP     |
| 22   | SSH     |
| 23   | Telnet  |
| 25   | SMTP    |
| 80   | HTTP    |
| 443  | HTTPS   |
| 3306 | MySQL   |

---

## 📂 Project Structure


python-port-scanner/
├── port_scanner.py
├── README.md
└── requirements.txt


---

## ▶️ How to Run

### 1️⃣ Clone / Download

```bash
git clone <your-repo-url>
cd python-port-scanner

2️⃣ Run

python3 port_scanner.py

3️⃣ Example Input

Enter IP or domain: scanme.nmap.org
Enable banner grabbing? (y/n): y

✅ Example Output

[OPEN]   Port 22    (SSH)
        Banner: SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.8
[CLOSED] Port 21    (FTP)
[OPEN]   Port 80    (HTTP)
        Banner: (no banner / blocked / silent)

⚠️ Legal & Ethical Warning (Important)

✅ Only scan:

Your own machines

Your lab environment (VMs)

Systems you have permission to test

❌ Do NOT scan random servers/websites without permission.

🔥 Learning Outcome

This project helps you understand:

TCP/IP basics

Port scanning logic

Reconnaissance techniques

Defensive thinking (what ports are exposed)

Learning method:
Build → Break → Fix → Rebuild → Learn deeply