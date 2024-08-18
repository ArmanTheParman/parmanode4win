from variables import *
from functions import *
from bitcoin.bitcoin_functions_f import *
from datetime import date
from config_f import *
from parmanode.sned_sats_f import *

def install_bitcoin():

    set_terminal()

    if not yesorno("Install Bitcoin?"): return False

    if ico.grep("bitcoin-end") or ico.grep("bitcoin-start"):
        announce("Please uninstall Bitcoin first")
        return False

    try:
        pco.remove("bitcoin_dir")
        pco.remove("drive_bitcoin")
    except:
        pass

    #pre start cleanup, possibly redundant
    pco.remove("check_bitcoin_dir_flag")
    ico.add("bitcoin-start")
    
    sned_sats()

    if not choose_drive(): return False 

    if pco.grep("check_bitcoin_dir_flag"):
        if not check_default_directory_exists(): return False
        pco.remove("check_bitcoin_dir_flag")

    if pco.grep("format_disk=True"):
        if not detect_drive(): input("detect drive failed") ; return False

        disk_number = pco.grep("disk_number", returnline=True)
        disk_number = disk_number.split('=')[1].strip()
        #input("before format") 
        if format_disk(disk_number):
            # pco.add(r"bitcoin_dir=P:\bitcoin") #REDUNDANT, REMOVED, ALREADY DONE IN FORMAT_DISK()
            # REDUNDANT: if not Path(r"P:\bitcoin").exists(): Path(r"P:\bitcoin").mkdir(parents=True, exist_ok=True)
            #input("disk formatted")
            pass
        else:
            thedate = date.today().strftime("%d-%m-%y")
            dbo.add(f"{thedate}: Bitcoin format_disk exited.")
            input("format failed")
            return False 
    
    pco.remove("disk_number")
    pco.remove("format_disk")

    if not download_bitcoin(): return False #also extracts and moves, zip left, unzipped dir deleted.
    if not verify_bitcoin(): return False
    if not make_symlinks(): return False


    decision_list = check_bitcoin_conf_exists_and_decide() # returns list (bool, str, Path)
    if decision_list[0] == False: return False
    
    if not decision_list[1].lower() == "use existing conf":
        """bitcoin.conf doesn't exist or did and was delete"""
        if not prune_choice(): return False
        bitcoin_conf = Path(decision_list[2])
        if not make_bitcoin_conf(bitcoin_conf): return False #decision_list[2] is a bitcoin_conf path object
    
    ico.add("bitcoin-end") 
    bitcoin_installed_success()
    return True

def bitcoin_installed_success():
    set_terminal() 
    print(f"""
########################################################################################
   {cyan} 
                                    SUCCESS !!!
{orange}
    Bitcoin Core should have started syncing. Note, it should also continue to sync 
    after a reboot, or you can start Bitcoin Core from the Parmanode Bitcoin menu at
    any time.

    You can also access Bitcoin functions from the Parmanode menu.

{green}
    TIP:

    Make sure you turn off power saving features, particularly features that put
    the drive to sleep; Power saving is usually on by default for laptops.
{orange}

########################################################################################
""")
    enter_continue()

