from variables import *
from functions import *
from config_f import *

def install_tor(no_config=False):

    set_terminal()

    try:
        subprocess.run(["choco", "install", "tor", "-y"], check=True)
        subprocess.run(["tor", "--service", "install"], check=True)
        subprocess.run(["powershell", "Start-Service -Name tor"], check=True)

        ico.add("tor-end")
        success("Tor has been installed") 
    except subprocess.CalledProcessError as e:
        announce("Failed to install Tor")
        return False

    try:
        subprocess.run(["tor", "--version"], check=True, stdout=subprocess.DEVNULL) 
    except (subprocess.CalledProcessError, FileNotFoundError):
        announce("Failed to install Tor")
        return False

    if no_config == True: return 0
    else:
        ico.add("tor-end")
        return True

def uninstall_tor():
    set_terminal()
    
    try:
        subprocess.run(["choco", "uninstall", "tor", "-y"], check=True)
        ico.remove("tor-")
        success("Tor has been uninstalled")
    except subprocess.CalledProcessError as e:
        announce("Failed to uninstall Tor")
        return False