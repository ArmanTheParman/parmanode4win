from variables import *
from functions import *
from config_f import *

def install_tor():

    set_terminal()

    try:
        subprocess.run(["choco", "install", "tor", "-y"], check=True)
        print("Tor installed successfully.")
    except subprocess.CalledProcessError as e:
        announce("Failed to install Tor")
        return False

    try:
        subprocess.run(["tor",  "--service", "start"], check=True, stdout=subprocess.DEVNULL)
        subprocess.run(["tor", "--version"], check=True, stdout=subprocess.DEVNULL) 
    except (subprocess.CalledProcessError, FileNotFoundError):
        announce("Failed to install Tor")
        return False

    ico.add("tor-end")
    return True