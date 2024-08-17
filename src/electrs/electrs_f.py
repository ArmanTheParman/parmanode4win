import subprocess, os
from functions import *
from variables import *
from config_f import *
from parmanode.sned_sats_f import *

def install_electrs():

    if ico.grep("docker-end") == False:
        announce(f"""Must install Docker first. Aborting.""")
        return False
    
    if dosubprocess("docker ps") == False:
        announce(f"""Please make sure Docker is running and try again. Aborting.""")
        return False

    if ico.grep("bitcoin-end") == False:
        announce(f"""Please install Bitcoin first and try again. Aborting.""")
        return False

    if yesorno(f"""Install electrs? This will use Docker to compile the program in a
    container - it can a while.""") == False: return False

    if bc.exists() == False:
        announce("""The bitcoin.conf file could not be detected. Can happen if Bitcoin is
    supposed to sync to the external drive and it is not connected and mounted.
    Hit{cyan} <enter>{orange} to try again once you connect the drive. Aborting.""")
        return False

    sned_sats()
    set_terminal()
    please_wait() 

    #Build from dockerfile
    p4w_electrs = p4w / "src" / "electrs"
    showsubprocess(f"docker build -t electrs {p4w_electrs}/ ")
    
    
def uninstall_electrs():
    pass