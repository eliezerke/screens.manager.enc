import subprocess
import sys

def install_browsers():
    # Run 'python -m playwright install' to download browser binaries
    subprocess.check_call([sys.executable, "-m", "playwright", "install"])

install_browsers()
