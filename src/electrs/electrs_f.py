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
    supposed to sync to the external drive and it is not connected and mounted. Aborting.""")
        return False

    if check_pruning_off() == False: return False
    if check_server_1() == False: return False
    if check_rpc_bitcoin() == False: return False

    sned_sats()
    set_terminal()
    please_wait() 

    #Build from dockerfile
    p4w_electrs = p4w / "src" / "electrs"
    showsubprocess(f"docker build -t electrs {p4w_electrs}/ ")
    
    
def uninstall_electrs():
    pass

def check_pruning_off():
    try: 
        prunevalue = bco.grep("purne=", returnline=True).split('=')[1].strip()
    except: 
        return True 

    if announce(f"""Parmanode has detected you are using pruning with Bitcoin.
    Electrum Server won't work if Bitcoin is pruned. You'll have to completely start 
    bitcoin sync again without pruning to use Electrs. Sorry. If you think this is 
    wrong and want to proceed, type{cyan} 'yolo'{orange} before hitting{cyan} <enter>{orange}""") == "yolo":
        return True
    else:
        return False


def check_server_1():
    if bco.grep("server=1") == True: 
        return True
    else:
        announce(f"""{cyan}'server=1'{orange} needs to be included in the bitcoin.conf 
    file. Please do that, restart Bitcoin, and try again. Note, this will
    resync the index which will take a long time. Aborting.""")
        return False

def check_rpc_bitcoin():
    if bco.grep("rpcuser=") == True and bco.grep("rpcpassword=") == True:
        return True
    else:
        announce(f"""Electrs wont work unless the bitcoin.conf file has a username
    and password set. You need{cyan} 'rpcuser=someusername' {orange}and{cyan} 'rpcpassword=somepassword'{orange} 
    in the file. Aborting.""")
        return False