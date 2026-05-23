import subprocess
import sys
import os
requirements = """
opencv-python
requests
psutil
"""
with open("requirements.txt", "w") as file:
    file.write(requirements.strip())
subprocess.check_call([
    sys.executable,
    "-m",
    "pip",
    "install",
    "-r",
    "requirements.txt"
])
