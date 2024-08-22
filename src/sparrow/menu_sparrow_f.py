
from variables import *
from functions import *
from config_f import *
import subprocess, json

def menu_sparrow():

    while True:

        connection = _sparrow_connection_type()

        set_terminal()
        print(f"""{orange}
########################################################################################{cyan}
                            Sparrow Bitcoin Wallet Menu{orange}                   
########################################################################################

{red}
    CONNECTION TYPE: {black}{connection}

{green}
                   (s){orange}    Start/open Sparrow
{green}
                   (w){orange}    View saved wallet files 
{green}
                   (b){orange}    Make Sparrow connect to {yellow}Bitcoin Core {orange}directly
{green}
                   (e){orange}    Make Sparrow connect to {blue}electrs {black}(better and faster)
         

{orange}
########################################################################################
""")

        choice = choose("xpmq")
        set_terminal()

        if choice.upper() in {"Q", "EXIT"}: 
            sys.exit()
        elif choice.upper() == "P":
            return True
        elif choice.upper() == "M":
            return True
        elif choice.lower() in {"start", "s"}:
            sparrowexe = pp / "sparrow" / "Sparrow.exe"
            subprocess.Popen(sparrowexe)
            enter_continue("Sparrow will open in a moment. Hit <enter> to continue.")
            return True
        elif choice.lower() == "w":
            show_sparrow_wallets()
        else:
            invalid()

        
def _sparrow_connection_type():
    return get_sparrow_config()["serverType"]
        

def show_sparrow_wallets():

    thefiles = subprocess.run(f"ls {sparrow_wallet_directory}", shell=True, capture_output=True, text=True).stdout

    set_terminal()
    print(f"""
########################################################################################


    Directory:{cyan} {sparrow_wallet_directory} {orange}


    Files: {bright_blue}

{thefiles}
{orange}
########################################################################################
""")
    enter_continue()

def get_sparrow_config():
    try:
        with open(sparrow_config_path, 'r') as file: 
            data = json.load(file)
        return data
    except:
        return False

def _sparrow_connect_electrs():
    
    if _sparrow_connection_type == "ELECTRUM_SERVER":
        return True

    configfile = get_sparrow_config()
    configfile["electrumServer"] = "tcp://127.0.0.1:50005"