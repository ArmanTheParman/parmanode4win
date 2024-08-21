import subprocess
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

    if is_process_running("bitcoind.exe") == False:
        announce(f"""Please make sure Bitcoin is running first.""") 
        return False


    if yesorno(f"""Install electrs? This will use Docker to compile the program in a
    container - it can take a while.""") == False: return False

    if bc.exists() == False:
        announce("""The bitcoin.conf file could not be detected. Can happen if Bitcoin is
    supposed to sync to the external drive and it is not connected and mounted. Aborting.""")
        return False

    if check_pruning_off() == False: return False
    if check_server_1() == False: return False
    if check_rpc_bitcoin() == False: return False

    sned_sats()
    set_terminal()
    if not yesorno(f"""Please be aware that currently, and external drive to hold the electrs data
    is not yet supported with Parmanode - mounting a Windows formatted drive to a Linux 
    Docker container has proven tricky so far. That means electrs will only work 
    syncing to the internal drive.
    
    You need about{cyan} 100GB free space on the INTERNAL Drive{orange}. In the future, I
    may find a way to make the external drive option available, stay tuned.

    Go ahead?"""): return False

    please_wait() 

    #Build from dockerfile
    p4w_electrs = p4w / "src" / "electrs"
    showsubprocess(f"docker build -t electrs {p4w_electrs}/ ")
    print(f"""Pausing here; you can see if the build failed or not.""")
    enter_continue()


    if not make_electrs_config(db_dir=f"{electrs_dir}"): return False

    ico.add("electrs-start")
    if not docker_run_electrs(): return False #change function later to pass db dir variable

    #make sure /electrs_db has permissions for "parman" user

    make_electrs_ssl() 

#Set permissions
    please_wait()

    try: subprocess.run(["powershell", "docker exec -itu root electrs bash -c 'chown -R parman:parman /home/parman/parmanode/electrs/'"], check=True)
    except: pass

    if not start_electrs_docker(): return False


    ico.add("electrs-end")
    success("Electrs has been installed")
    return True

#################################################################################################################################    

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

def docker_run_electrs():

    try: subprocess.run(["docker", "run", "-d", "--privileged", "--name", "electrs", "-p", "50005:50005", "--restart", "unless-stopped", "-p", "50006:50006", "-p", "9060:9060", "-v", f"{electrs_dir}:/electrs_db", "-v", f"{dot_electrs}:/home/parman/.electrs", "electrs"], check=True)
    except Exception as e:
#        print(command)
        input(e)
        return False

    return True

def make_electrs_ssl():
    
    IP=get_IP_variables()
    address=f"{IP["IP"]}"
    try:
        subprocess.run(["docker", "exec", "-d", "electrs",
                        "bash", "-c",
                        f"openssl req -newkey rsa:2048 -nodes -x509 -keyout /home/parman/.electrs/key.pem -out /home/parman/.electrs/cert.pem -days 36500 -subj /C=/L=/O=/OU=/CN={address}/ST/emailAddress="],
                        check=True)
    except Exception as e: input(e)                    
    return True

def make_electrs_config(db_dir=None):

    dot_electrs = HOME / ".electrs"
    dot_electrs.mkdir(exist_ok=True)

    electrs_config_file = dot_electrs / "config.toml"

    try:
        rpcuser = bco.grep("rpcuser=", returnline=True).split('=')[1].strip()
        rpcpassword = bco.grep("rpcpassword=", returnline=True).split('=')[1].strip()
    except Exception as e: 
        input(e)
        return False

    config_text=f"""    
    daemon_rpc_addr = \"host.docker.internal:8332\"
    daemon_p2p_addr = \"host.docker.internal:8333\"
    db_dir = \"/electrs_db\"
    network = \"bitcoin\"
    electrum_rpc_addr = \"0.0.0.0:50005\"
    log_filters = \"INFO\" # Options are ERROR, WARN, INFO, DEBUG, TRACE
                        # Changing this will affect parmanode menu output negatively
    auth = \"{rpcuser}:{rpcpassword}\""""

    with open(electrs_config_file, 'w') as f:
        f.write(config_text)

    return True 
    
def start_electrs():
    start_electrs_docker()
    input("end start electrs")

def stop_electrs():
    try: subprocess.run(["docker", "stop", "electrs"], check=True)
    except: pass
    input("end stop electrs")
    
def restart_electrs():
    stop_electrs()
    start_electrs_docker()
    input("end restart electrs")

def start_electrs_docker():
    input("begin start_electrs_docker")
    #check Docker desktop running
    if dosubprocess("docker ps") == False:
        announce(f"""Please make sure Docker is running and try again. Aborting.""")
        return False

    #check check container running
    try:
        if not subprocess.run("docker ps | grep electrs", check=True, shell=True, capture_output=True).returncode == 0:
           subprocess.run("docker start electrs", shell=True, check=True, capture_output=True) 

    #start processes in the container
    try:
        subprocess.run(["docker", "exec", "-du", "root", "electrs", "/bin/bash -c", 
                        "/home/parman/parmanode/electrs/target/release/electrs --conf /home/parman/.electrs/config.toml >> /home/parman/run_electrs.log 2>&1"], check=True)
        subprocess.run(["docker", "exec", "-d electrs", "/bin/bash -c", 
                        "/usr/bin/socat OPENSSL-LISTEN:50006,reuseaddr,fork,cert=/home/parman/.electrs/cert.pem,key=/home/parman/.electrs/key.pem,verify=0 TCP:127.0.0.1:50005"], check=True)
    except Exception as e: input(e)


    input("end start_electrs_docker")
    return True

    
    
