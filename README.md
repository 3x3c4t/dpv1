Open source Python project for educational and demonstration purposes.
Sends (pretty) sensitive system information to a Discord webhook.

---

# ➜ Features

➜ System information collection
➜ CPU usage
➜ RAM usage
➜ Hostname
➜ Operating system
➜ Local IP address
➜ Camera Spying
➜ Discord webhook integration

---

# ➜ Configuration
Change the webhook variable at the beginning of the code:

```python
WEBHOOK_URL = "https://discord.com/api/webhooks/..."
```

The Discord webhook can be easily found if you decompile, be careful.
---

# ➜ Installation

```bash
pip install -r requirements.txt
```

---

# ➜ Usage

```bash
python main.py
```

---

# ➜ Build EXE

```bash
pyinstaller --onefile --icon=Icon.ico --name Program_Name main.py
```

➜ The executable will be generated inside:

```text
dist/
```

---

# ➜ Project Structure

```text
project/
│
├── main.py
├── requirements.txt
├── Icon.ico
├── README.md
└── LICENSE
```

---

Free to use, modify and distribute.

---

# ➜ Disclaimer

➜ Educational and demonstration purposes only.
Do not use on systems without permission.
