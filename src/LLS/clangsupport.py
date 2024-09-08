import os
import subprocess
import sys
import platform
from pathlib import Path
import urllib.request
import zipfile

def check_clangd_installed():
    """Check if clangd is installed."""
    try:
        subprocess.run(['clangd', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError:
        return False

def download_and_extract_clangd_windows():
    """Download and extract clangd on Windows."""
    llvm_url = 'https://github.com/llvm/llvm-project/releases/download/llvmorg-17.0.1/clangd-windows-x64.zip'
    download_path = Path.home() / 'clangd-windows-x64.zip'
    extract_path = Path.home() / '.utils' / 'llvm'

    # Create the extraction directory if it doesn't exist
    extract_path.mkdir(parents=True, exist_ok=True)

    # Download the LLVM binaries
    print("Downloading clangd...")
    urllib.request.urlretrieve(llvm_url, download_path)

    # Extract the zip file
    print("Extracting clangd...")
    with zipfile.ZipFile(download_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    # Add bin folder to PATH
    bin_folder = extract_path / 'bin'
    bin_folder = str(bin_folder)
    current_path = os.environ.get('PATH', '')
    if bin_folder not in current_path:
        new_path = f'{current_path};{bin_folder}'
        os.environ['PATH'] = new_path
        subprocess.run(f'setx PATH "{new_path}"', shell=True, check=True)
    
    # Clean up
    os.remove(download_path)

def main():
    os_type = platform.system()

    if check_clangd_installed():
        print("clangd is already installed.")
        return

    if os_type == 'Windows':
        print("clangd not found. Installing...")
        download_and_extract_clangd_windows()
    else:
        print("Unsupported operating system.")
        sys.exit(1)

    if check_clangd_installed():
        print("clangd has been installed successfully.")
    else:
        print("Failed to install clangd.")

if __name__ == '__main__':
    main()
