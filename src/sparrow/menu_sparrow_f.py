
from variables import *
from functions import *
from config_f import *
import subprocess, json

def menu_sparrow():

    while True:

        connection = _sparrow_connection_type()
        if connection == False: connection = "NONE"

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
                   (b){orange}    Make Sparrow connect to {yellow}Bitcoin Core {orange}directly
{green}
                   (e){orange}    Make Sparrow connect to {blue}electrs {black}(better and faster)
{green}
                   (pp){orange}   Make Sparrow connect to {red}PUBLIC electrs {black}(avoid)
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
        elif choice.lower() == "b":
            _sparrow_connect_bitcoin()
        elif choice.lower() == "e":
            _sparrow_connect_electrs()
        elif choice.lower() == "pp":
            _sparrow_connect_public()
        elif choice.lower() == "w":
            show_sparrow_wallets()
        else:
            invalid()

        
def _sparrow_connection_type():
    try:
        return get_sparrow_config()["serverType"]
    except:
        return False 
        

def show_sparrow_wallets():

    try: thefiles = subprocess.run(f"ls {sparrow_wallet_directory}", shell=True, capture_output=True, text=True).stdout
    except: announce(f"""Directory does not exists.""") ; return False

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

    try:

        configfile = get_sparrow_config()
        configfile["serverType"] = "ELECTRUM_SERVER"
        configfile["electrumServer"] = "tcp://127.0.0.1:50005"
        configfile["useProxy"] = "false"

    except: return False

def _sparrow_connect_public():
    
    if not yesorno("""This is bad for privacy, try to avoid it unless you know exactly
    what you are doing, or if it's an emergency.
    
    Really connect to a public server?"""): return False

    if _sparrow_connection_type == "PUBLIC_ELECTRUM_SERVER":
        return True

def _sparrow_connect_bitcoin():

    bitcoin_dir = pco.grep("bitcoin_dir=", returnline=True).strip().split('=')[1]

    coreDD = ""
    for i in bitcoin_dir:
       if i == "\\":
         i = '/'
       coreDD = coreDD + i 

    while True:
        try: bco.grep("rpcuser") 
        except: 
           rpcpassword="parman"
           rpcuser="parman"
           break
        rpcuser = bco.grep("rpcuser=", returnline=True).strip().split('=')[1]
        rpcpassword = bco.grep("rpcpassword=", returnline=True).strip().split('=')[1]
        break
    if _sparrow_connection_type == "BITCOIN_CORE":
        return True

    configfile = get_sparrow_config()
    configfile["coreServer"] = "http://127.0.0.1:8332"
    configfile["coreAuthType"] = "USERPASS"
    configfile["useProxy"] = "false"
    configfile["coreDataDir"] = f"{coreDD}"
    configfile["coreAuth"] = f"{rpcuser}:{rpcpassword}"