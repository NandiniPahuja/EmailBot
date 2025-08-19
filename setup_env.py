"""
setup_env.py
Automatically installs required Python packages for EmailBot.
"""
import subprocess
import sys

REQUIREMENTS = "requirements.txt"


def install_requirements():
    print("Installing required packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", REQUIREMENTS])
    print("All packages installed.")

if __name__ == "__main__":
    install_requirements()
