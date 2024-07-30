from functions import *
import subprocess
def check_chocolatey():
    if subprocess.run(["choco", "--version"], check=True):
        return True
    else: 
        return False
def install_chocolatey():
    try:
        command = (
            r'Set-ExecutionPolicy Bypass -Scope Process -Force; '
            r'[System.Net.ServicePointManager]::SecurityProtocol = '
            r'[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; '
            r'iex ((New-Object System.Net.WebClient).DownloadString("https://chocolatey.org/install.ps1"))'
        )
        if subprocess.run(["powershell", "-Command", command], check=True):
            print("Chocolatey installed successfully.")

    except subprocess.CalledProcessError as e:
        return False

    return True

def check_python():
    try:
        subprocess.run(["python", "--version"], check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_git():
    try:
        subprocess.run(["git", "--version"], check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_curl():
    try:
        subprocess.run(["curl", "--version"], check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
    
def install_python_with_chocolatey():
    try:
        subprocess.run(["choco", "install", "python", "-y"], check=True)
        print("Python installed successfully.")
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to install Python with Chocolatey: {e.stderr}")

    return True
def install_git_with_chocolatey():
    try:
        subprocess.run(["choco", "install", "git", "-y"], check=True)
        print("git installed successfully.")
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to install git with Chocolatey: {e.stderr}")

    return True

def install_curl_with_chocolatey():
    try:
        subprocess.run(["choco", "install", "curl", "-y"], check=True)
        print("curl installed successfully.")
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to install curl with Chocolatey: {e.stderr}")

    return True

def check_gpg():
    try:
        subprocess.run(["gpg", "--version"], check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
    
def install_gpg_with_chocolatey():

    try:
        subprocess.run(["choco", "install", "gpg", "-y"], check=True)
        print("gpg installed successfully.")
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to install gog with Chocolatey: {e.stderr}")

    return True

def dependency_check():

    try:
        # Check if Chocolatey is installed
        if not check_chocolatey():
            if not yesorno("OK to install Chocolatey? (Necessary)"): return False
            install_chocolatey()

        # Check if git is installed
        if not check_git():
            if not yesorno("OK to install git? (Necessary)"): return False
            install_git_with_chocolatey()

        if not check_curl():
            if not yesorno("OK to install curl? (Necessary)"): return False
            install_curl_with_chocolatey()

        # Check if gpg is installed
        if not check_gpg():
            if not yesorno("OK to install gpg? (Necessary)"): return False
            install_gpg_with_chocolatey()

        # Check if pythone is installed
        if not check_python():
            if not yesorno("OK to install python? (Necessary)"): return False
            install_python_with_chocolatey()

        

        return True
        
    except Exception as e:
        print(f"An error occurred: {e}")
