from variables import *
from functions import *
from config_f import *
from tor.tor_functions import *

def install_tor(no_config=False):

    set_terminal()

    try : initialise_torrc()
    except Exception as e: input(e)

    ico.add("tor-start")

    try:
        subprocess.run(["choco", "install", "tor", "-y"], check=True)
    except subprocess.CalledProcessError as e:
        announce("Failed to install Tor")
        return False
    try:
        subprocess.run(["tor", "--service", "install"], check=True)
        subprocess.run(["powershell", "Start-Service -Name tor"], check=True)
    except: pass

    try:
        subprocess.run(["tor", "--version"], check=True, stdout=subprocess.DEVNULL) 
    except (subprocess.CalledProcessError, FileNotFoundError):
        announce("Failed to install Tor")
        return False

    if no_config == True: return 0
    else:
        success("Tor has been installed") 
        ico.add("tor-end")
        return True

def uninstall_tor():
    set_terminal()
    stop_tor()
    
    try:
        subprocess.run(["choco", "uninstall", "tor", "-y"], check=True)
    except subprocess.CalledProcessError as e:
        announce("Failed to uninstall Tor")
        return False

    try:
        subprocess.run(["tor", "--service", "install"], check=True)
    except: pass

    try:
        delete_directory(torrc_dir)
    except: pass

    ico.remove("tor-")
    success("Tor has been uninstalled")

def initialise_torrc():

    try: tor_services.mkdir(exist_ok=True)
    except Exception as e: input(e)
    try: torrc_dir.mkdir(exist_ok=True)
    except Exception as e: input(e)

    torrc_text=f"""# Additions by Parmanode...
ControlPort 9051
CookieAuthentication 1
CookieAuthFileGroupReadable 1
DataDirectoryGroupReadable 1

HiddenServiceDir {tor_services}/btcpay-service
HiddenServicePort 7003 127.0.0.1:23001

HiddenServiceDir {tor_services}/electrs-service
HiddenServicePort 7004 127.0.0.1:50005

HiddenServiceDir {tor_services}/rtl-service
HiddenServicePort 7005 127.0.0.1:3000

HiddenServiceDir {tor_services}/mempool-service
HiddenServicePort 8280 127.0.0.1:8180

HiddenServiceDir {tor_services}/bitcoin-service
HiddenServicePort 8332 127.0.0.1:8332
""" 

    try:
        with open(torrc_file, 'w') as file:
            file.write(torrc_text)
    except: pass
    