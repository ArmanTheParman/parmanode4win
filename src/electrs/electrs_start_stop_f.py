import subprocess
from functions import dosubprocess, announce

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

    
    