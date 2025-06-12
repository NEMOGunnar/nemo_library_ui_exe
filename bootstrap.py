import subprocess
import sys
import os
import shutil
import tempfile
import urllib.request
import zipfile

GITHUB_ZIP_URL = "https://github.com/NEMOGunnar/nemo_library_ui/archive/refs/heads/main.zip"

def ensure_pip_package(name):
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", name], check=True)

def install_ui_from_git(zip_url):
    print(f"🌐 Downloading latest UI from GitHub...")
    with tempfile.TemporaryDirectory() as tmpdir:
        zip_path = os.path.join(tmpdir, "ui.zip")
        urllib.request.urlretrieve(zip_url, zip_path)

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(tmpdir)

        root_dir = next(
            os.path.join(tmpdir, d)
            for d in os.listdir(tmpdir)
            if os.path.isdir(os.path.join(tmpdir, d)) and d.startswith("nemo_library_ui")
        )

        print("📦 Installing UI package...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", root_dir], check=True)

def launch_ui():
    print("🚀 Launching nemo-ui...")
    subprocess.run(["nemo-ui"], check=True)

def main():
    ensure_pip_package("pip")
    install_ui_from_git(GITHUB_ZIP_URL)
    launch_ui()

if __name__ == "__main__":
    main()