import subprocess, os
from variables import *
from functions import *

def disable_wsl():

    _unregister_all_wsl_distributions()

    try:
        subprocess.run(["powershell", "-Command", "Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux -NoRestart"], check=True)
    except Exception as e: input(e)

    try:
        subprocess.run(["powershell", "-Command", "Disable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform"], check=True)
    except Exception as e: input(e)

def enable_wsl():
    #Ensure that virtualization is enabled in your BIOS/UEFI settings. This is required for WSL 2.


    try:
        subprocess.run(["powershell", "dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart"], check=True)
    except Exception as e: 
        pass

    try:
        subprocess.run(["powershell", "dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart"], check=True)
    except Exception as e: 
        pass
    
    try: 
        subprocess.run(["powershell", "wsl --set-default-version 2"], check=True) 
    except Exception as e: pass

    try:
        subprocess.run(["powershell", "wsl --update"], check=True)
    except Exception as e:
        pass

    try: 
        subprocess.run(["powershell", "wsl --install"], check=True) 
    except Exception as e: pass

    #after that, check if any distro installed.  May not have, but may have. If none, install debian.
    #new username and password is prompted for.
    #new session in linux entered. type 'exit' to get out.
    #wsl --list, lists distros, and also docker
    #Look vor version2 of wsl. If not, instruct user to manually enable virualisation and give a website.

    ico.add("wsl-end")
    success("WSL has been installed. Please reboot the computer, or you'll get errors.")



def install_docker():
    pass
    # """
    # WSL needs to be installed first
    # choco install docker-desktop -y
    # #restart computer to set path correctly
    # docker bin files:
    #      c:\Program files\Docker\Docker\resources\bin
    # docker desktop file:
    #      c:\Program files\Docker\Docker\"docker desktop.exe"
    # """

    

def _unregister_all_wsl_distributions():
    try:
        result = subprocess.run(['wsl', '--list', '--quiet'], capture_output=True, text=True, check=True)
        distros = result.stdout.splitlines()
        input("zzzz2a")

        for distro in distros:
            print(f"{distros}")
            print(f"{distro}")
            input("zzzz2b")
            print(f"{red}Unregistering distros...{orange}")
            subprocess.run(['wsl', '--unregister', distro])
            input("zzzz2c")

    except subprocess.CalledProcessError as e:
        input(f"An error occurred: {e}")


