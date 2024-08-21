import subprocess, os
from functions import *
from variables import *
from config_f import *
from parmanode.sned_sats_f import *
from electrs.make_electrs_config_f import *

electrs_dir = HOME / "electrs_db"


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

def choose_electrs_drive():
    
    if pco.grep("bitcoin_drive=external") == True:
        if yesorno(f"""Would you like to store the electrs data (50 to 100GB) on the
    external drive together with the bitcoin block data?""", y=["e", "External drive"], n=["i", "Internal drive"]) == True:
            pco.add("electrs_drive=external")
            return "external"
        else:
            pco.add("electrs_drive=internal")
            return "internal"
    else: #internal or custom
        if yesorno(f"""Would you like to store electrs data (50 to 100GB) on the
    external drive or internal drive?""", y=["e", "External drive"], n=["i", "Internal drive"]) == True:
            pco.add("electrs_drive=external")
            return "external"
        else:
            pco.add("electrs_drive=internal")
            

def electrs_db_exists():
    if not electrs_dir.exists(): return True

    choice = announce(f"""Parmanode has detected that an electrs database directory already
    exists. What would you like to do?
    

{cyan}                    u){green}    use it
                    
{cyan}                    d){red}    delete contents and start fresh
                    
{cyan}                    a){bright_blue}    abort!  {orange} """)
    
    if choice.lower() == "q": sys.exit()
    if choice.lower() == "p": return False
    if choice.lower() == "a": return False
    if choice.lower() == "u": return True
    if choice.lower() == "d": 
        try: delete_directory(electrs_dir) ; electrs_dir.mkdir() ; return True
        except Exception as e: input(e) ; return True


def docker_run_electrs(db_dir=None):

    dot_electrs = str(HOME / ".electrs")
    db_dir = str(electrs_dir)

    try: subprocess.run(["docker", "run", "-d", "--privileged", "--name", "electrs", "-p", "50005:50005", "--restart", "unless-stopped", "-p", "50006:50006", "-p", "9060:9060", "-v", f"{db_dir}:/electrs_db", "-v", f"{dot_electrs}:/home/parman/.electrs", "electrs"], check=True)
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

def start_electrs():
    start_electrs_docker()

def stop_electrs():
    try: subprocess.run(["docker", "stop", "electrs"], check=True)
    except: pass
    
def restart_electrs():
    stop_electrs()
    start_electrs_docker()

def start_electrs_docker():

    if dosubprocess("docker ps") == False:
        announce(f"""Please make sure Docker is running and try again. Aborting.""")
        return False

    try: subprocess.run("docker ps | grep electrs", check=True, shell=True) ; return True
    except : pass

    try:
        subprocess.run(["docker", "exec", "-du", "root", "electrs", "/bin/bash -c", 
                        "/home/parman/parmanode/electrs/target/release/electrs --conf /home/parman/.electrs/config.toml >> /home/parman/run_electrs.log 2>&1"], check=True)
        subprocess.run(["docker", "exec", "-d electrs", "/bin/bash -c", 
                        "/usr/bin/socat OPENSSL-LISTEN:50006,reuseaddr,fork,cert=/home/parman/.electrs/cert.pem,key=/home/parman/.electrs/key.pem,verify=0 TCP:127.0.0.1:50005"], check=True)
    except Exception as e: input(e)

    return True

    
    