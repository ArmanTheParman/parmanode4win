import subprocess, os
from functions import *
from variables import *
from config_f import *
from parmanode.sned_sats_f import *
from electrs.make_electrs_config_f import *

electrs_dir = HOME / "electrs_db"

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


