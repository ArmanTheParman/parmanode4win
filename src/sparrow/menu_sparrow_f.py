
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
    
    with open(sparrow_config_path, 'r') as file: 
        data = json.load(file)

    return data["serverType"]
        

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