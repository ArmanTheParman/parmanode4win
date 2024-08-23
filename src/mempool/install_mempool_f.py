import subprocess
from functions import *
from variables import *
from config_f import *
from electrs.install_electrs_f import check_server_1 
from parmanode.sned_sats_f import *
from parmanode.uninstall_parmanode_f import *
from mempool.make_docker_compose_mempool_f import *

def install_mempool():
    if ico.grep("docker-end") == False:
        announce(f"""Must install Docker first. Aborting.""")
        return False
    
    if dosubprocess("docker ps") == False:
        announce(f"""Please make sure Docker is running and try again. Aborting.""")
        return False

    if ico.grep("bitcoin-end") == False:
        announce(f"""Please install Bitcoin first and try again. Aborting.""")
        return False
    
    if yesorno(f"""Install Mempool?""") == False: return False

    if bc.exists() == False:
        announce("""The bitcoin.conf file could not be detected. Can happen if Bitcoin is
    supposed to sync to the external drive and it is not connected and mounted. Aborting.""")
        return False

    if not check_server_1(): return False

    if not check_tx_index_1: return False

    sned_sats()
    please_wait() 

    clone_mempool()
    ico.add("mempool-start")

    make_mempool_docker_compose()
    start_mempool()

    ico.add("mempool-end")
    success("Mempool has been installed")

def uninstall_mempool():

    if not yesorno(f"""Are you sure you want to uninstall Mempool?"""): return False

    thedir = str(pp / "mempool") 
    try: delete_directory_force(thedir)
    except Exception as e: input(e)

    ico.remove("mempool-")
    success("Mempool has been uninstalled")

    
def check_tx_index_1():
    if bco.grep("txindex=1") == True: 
        return True
    else:
        announce(f"""{cyan}'txindex=1'{orange} needs to be included in the bitcoin.conf 
    file. Please do that, restart Bitcoin, and try again. Note, this will
    resync the index which will take a long time. Aborting.""")
        return False

def clone_mempool():

    command=["git", "clone", "--depth", "1", "https://github.com/mempool/mempool.git", f"{pp}/mempool"]

    try:
        subprocess.run(command, check=True, capture_output=True) 
    except Exception as e: input(e)
    
def start_mempool():

    if dosubprocess("docker ps") == False:
        announce(f"""Please make sure Docker is running and try again. Aborting.""")
        return False

    os.chdir(pp / "mempool" / "docker")
    command = ["docker", "compose", "up", "-d"]

    try:
        subprocess.run(command, check=True)

    except Exception as e: input(e)

def stop_mempool():
    

    if dosubprocess("docker ps") == False:
        announce(f"""Please make sure Docker is running and try again. Aborting.""")
        return False

    os.chdir(pp / "mempool" / "docker")
    command = ["docker", "compose", "down"]

    try:
        subprocess.run(command, check=True)

    except Exception as e: input(e)

