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
    print(f"""Pausing here; you can see if the build failed or not.""")
    enter_continue()
   
    drive_choice = choose_electrs_drive()
    global electrs_dir

    if drive_choice == "external" and pco.grep("bitcoin_drive=external"): 
        electrs_dir=Path("p:/electrs_db")
        pco.add(f"electrs_dir={electrs_dir}")  

    if drive_choice == "external" and not pco.grep("bitcoin_drive=external"):
        while True:
            if yesorno(f"""Do you want to format a Parmanode drive or use an existing one?""", y=["f", "format a drive"], n=["e", "use existing"]) == True:
                pco.add("format_disk=True")
                break
                #Path(electrs_dir="p:/electrs_db") - added in format function
            else:
                drive_letter = announce("""Please connect the drive letter you wish to use and
        then type in the drive letter - eg 'D'""")
                electrs_dir=Path(f"{drive_letter}:/electrs_db")
                pco.add(f"electrs_dir={electrs_dir}")  
                try: 
                    electrs_dir.mkdir(exist_ok=True)
                    pco.add("format_disk=False")
                    break
                except:
                    announce("Unable to create the directory on this drive. Try again.")
                    continue

    if drive_choice == "internal":
        electrs_dir = Path(HOME / "electrs_db")
        pco.add(f"electrs_dir={electrs_dir}")  

########################################################################################
    pco.remove("disk_number")

    if pco.grep("format_disk=True"):
        if not detect_drive(): input("detect drive failed") ; return False

        disk_number = pco.grep("disk_number", returnline=True)
        try: disk_number = disk_number.split('=')[1].strip()
        except Exception as e: input(e)

        #input("before format") 
        if not format_disk(disk_number, program="electrs"):
            thedate = date.today().strftime("%d-%m-%y")
            dbo.add(f"{thedate}: Bitcoin format_disk exited.")
            input("format failed")
            return False 
    
########################################################################################
    pco.remove("disk_number")
    pco.remove("format_disk")
########################################################################################


    
#disk formatted
##UP TO HERE######################################################################################
   
   
   
   
   
   
   
    
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
            