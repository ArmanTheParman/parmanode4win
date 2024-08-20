import subprocess, os
from functions import *
from variables import *
from config_f import *
from parmanode.sned_sats_f import *
from electrs.make_electrs_config_f import *

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
        announce(f"""Please make sure Bitcoin is running first, give it minute 
    to think and compose itself, then try again.""") 


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

########################################################################################   
# Can't get docker to mount the Windows drive yet, so abandoning option to
# use an external drive for now
########################################################################################
#     drive_choice = choose_electrs_drive()
    global electrs_dir
    electrs_dir = HOME / "electrs_db"
#     pco.remove(f"electrs_dir=")

#     if drive_choice == "external" and pco.grep("bitcoin_drive=external"): 
#         electrs_dir=Path("p:/electrs_db")
#         pco.add(f"electrs_dir={electrs_dir}")  
#         if electrs_db_exists == False: return False
#         electrs_dir.mkdir(exist_ok=True)


#     if drive_choice == "external" and not pco.grep("bitcoin_drive=external"):
#         while True:
#             pco.remove("format_disk") #clear first
#             pco.remove("electrs_dir") #clear first
#             if yesorno(f"""Do you want to format a Parmanode drive or use an existing one?""", y=["f", "format a drive"], n=["e", "use existing"]) == True:
#                 pco.add("format_disk=True")
#                 break
#                 #Path(electrs_dir="p:/electrs_db") - added in format function
#             else:
#                 drive_letter = announce("""Please connect the drive letter you wish to use and
#         then type in the drive letter - eg 'P'""")
#                 if drive_letter.isalpha() and len(drive_letter) == 1:
#                     pass
#                 else:
#                     announce("Please try again")
#                     continue
#                 electrs_dir=Path(f"{drive_letter}:/electrs_db")
#                 if electrs_db_exists() == False: return False
#                 try: 
#                     electrs_dir.mkdir(exist_ok=True)
#                     pco.add("format_disk=False")
#                     pco.add(f"electrs_dir={electrs_dir}")  
#                     break
#                 except:
#                     announce("Unable to create the directory on this drive. Try again.")
#                     continue


#     if drive_choice == "internal":

#         electrs_dir = Path(HOME / "electrs_db")
#         if electrs_db_exists() == False: return False
#         try: 
#             electrs_dir.mkdir(exist_ok=True)
#             pco.remove(f"electrs_dir=")
#             pco.add(f"electrs_dir={electrs_dir}")  
#         except Exception as e: input(e) ; return False

# ########################################################################################
#     pco.remove("disk_number")

#     if pco.grep("format_disk=True"):
#         if not detect_drive(): input("detect drive failed") ; return False

#         disk_number = pco.grep("disk_number", returnline=True)
#         try: disk_number = disk_number.split('=')[1].strip()
#         except Exception as e: input(e)

#         #input("before format") 
#         if not format_disk(disk_number, program="electrs"):
#             thedate = date.today().strftime("%d-%m-%y")
#             dbo.add(f"{thedate}: Bitcoin format_disk exited.")
#             input("format failed")
#             return False 
    
# ########################################################################################
#     pco.remove("disk_number")
#     pco.remove("format_disk")
########################################################################################

    if not make_electrs_config(db_dir=f"{electrs_dir}"): return False
    ico.add("electrs-start")
    if not docker_run_electrs(db_dir=f"{electrs_dir}"): return False

    #make sure /electrs_db has permissions for "parman" user

    make_electrs_ssl() 

########################################################################################
########################################################################################
########################################################################################

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
    pass

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

    
    