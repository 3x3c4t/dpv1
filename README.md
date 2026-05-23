Open source Python project made for educational and demonstration purposes.
➜ Sends system information to a Discord webhook.

---

## Features

- System information collection
- CPU usage
- RAM usage
- Hostname
- Operating system
- Local IP address
- Webcam capture demo
- Discord webhook integration

---

## Configuration

➜ Change the webhook variable at the beginning of the code:

```python
WEBHOOK_URL = "https://discord.com/api/webhooks/..."
```

Keep your webhook private.

Anyone with access to the executable or source code may recover the webhook URL.

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```

---

## Build EXE

```bash
pyinstaller --onefile --icon=Icon.ico --name Program_Name main.py
```

➜ The executable will be generated inside:

```text
dist/
```

---

## Project Structure

```text
project/
│
├── main.py
├── requirements.txt
├── install_requirements.py
├── Icon.ico
├── README.md
└── LICENSE
```

---

## Example Payload

```json
{
  "hostname": "DESKTOP-XXXX",
  "os": "Windows 11",
  "cpu_usage": "12%",
  "ram_usage": "43%"
}
```

---

## License

➜ MIT License

Free to use, modify and distribute.

---

## Disclaimer

This project is intended for educational, testing and demonstration purposes only.

➜ Do not use on systems without permission.
