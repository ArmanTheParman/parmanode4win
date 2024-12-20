
from variables import *
from functions import *
from config_f import *
import subprocess, json

def menu_sparrow():

    while True:

        try:
            connection = _sparrow_connection_type()
        except Exception as e :input(e)

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
                   (b){orange}    Connect to {yellow}Bitcoin Core {orange}directly
{green}
                   (e){orange}    Connect to {blue}electrs {black}(better and faster)
{green}
                   (pp){orange}   Connect to {red}PUBLIC electrs {black}(avoid)
{green}
                   (w){orange}    Show saved wallet files 

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

def _sparrow_connection_type():
    try:
        return get_sparrow_config()["serverType"]
    except:
        return False 

def get_sparrow_config():
    try:
        with open(sparrow_config_path, 'r') as file: 
            data = json.load(file)
        return data
    except Exception as e:
        input(e) 
        return False

def _sparrow_connect_electrs():
    
    if _sparrow_connection_type == "ELECTRUM_SERVER":
        return True

    try:

        configfile = get_sparrow_config()
        configfile["serverType"] = "ELECTRUM_SERVER"
        configfile["electrumServer"] = "tcp://127.0.0.1:50005"
        configfile["useProxy"] = "false"

        with open(sparrow_config_path, 'w') as file:
            json.dump(configfile, file, indent=4)

    except: return False
    
    success("Sparrow connection changed to your private electrs Server")
    return True

def _sparrow_connect_public():
    
    if not yesorno("""This is bad for privacy, try to avoid it unless you know exactly
    what you are doing, or if it's an emergency.
    
    Really connect to a public server?"""): return False

    if _sparrow_connection_type == "PUBLIC_ELECTRUM_SERVER":
        return True
    
    configfile = get_sparrow_config()
    configfile["serverType"] = "PUBLIC_ELECTRUM_SERVER"

    with open(sparrow_config_path, 'w') as file:
        json.dump(configfile, file, indent=4)
    
    success("Sparrow connection changed to a Public Electrum Server")
    return True

def _sparrow_connect_bitcoin():

    if _sparrow_connection_type == "BITCOIN_CORE":
        return True

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

    try:
        configfile = get_sparrow_config()
        configfile["serverType"] = "BITCOIN_CORE"
        configfile["coreServer"] = "http://127.0.0.1:8332"
        configfile["coreAuthType"] = "USERPASS"
        configfile["useProxy"] = "false"
        configfile["coreDataDir"] = f"{coreDD}"
        configfile["coreAuth"] = f"{rpcuser}:{rpcpassword}"

        with open(sparrow_config_path, 'w') as file:
            json.dump(configfile, file, indent=4)

    except Exception as e: input(e) ; return False

    success("Sparrow connection changed to Bitcoin Core")
    return True