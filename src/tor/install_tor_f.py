from variables import *
from functions import *
from config_f import *

def install_tor(no_config=False):

    set_terminal()

    try:
        subprocess.run(["choco", "install", "tor", "-y"], check=True)
    except subprocess.CalledProcessError as e:
        announce("Failed to install Tor")
        return False
    try:
        subprocess.run(["tor", "--service", "install"], check=True)
        subprocess.run(["powershell", "Start-Service -Name tor"], check=True)
    except: pass

    ico.add("tor-end")
    success("Tor has been installed") 

    try:
        subprocess.run(["tor", "--version"], check=True, stdout=subprocess.DEVNULL) 
    except (subprocess.CalledProcessError, FileNotFoundError):
        announce("Failed to install Tor")
        return False

    initialise_torrc()

    if no_config == True: return 0
    else:
        ico.add("tor-end")
        return True

def uninstall_tor():
    set_terminal()
    
    try:
        subprocess.run(["choco", "uninstall", "tor", "-y"], check=True)
    except subprocess.CalledProcessError as e:
        announce("Failed to uninstall Tor")
        return False

    try:
        delete_directory(torrc_dir)
    except: pass

    ico.remove("tor-")
    success("Tor has been uninstalled")

def initialise_torrc():

    if not tor_directory.exists(): tor_directory.mkdir()

    torrc_text=f"""# Additions by Parmanode...
ControlPort 9051
CookieAuthentication 1
CookieAuthFileGroupReadable 1
DataDirectoryGroupReadable 1

HiddenServiceDir {tor_directory}/btcpay-service
HiddenServicePort 7003 127.0.0.1:23001

HiddenServiceDir {tor_directory}/electrs-service
HiddenServicePort 7004 127.0.0.1:50005

HiddenServiceDir {tor_directory}/rtl-service
HiddenServicePort 7005 127.0.0.1:3000

HiddenServiceDir {tor_directory}/mempool-service
HiddenServicePort 8280 127.0.0.1:8180

HiddenServiceDir {tor_directory}/bitcoin-service
HiddenServicePort 8332 127.0.0.1:8332
""" 

    with open(torrc_file, 'w') as file:
        file.write(torrc_text)