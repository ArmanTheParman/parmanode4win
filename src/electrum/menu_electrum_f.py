from variables import *
from functions import *
from config_f import *
import subprocess, json

def menu_electrum():

    while True:

        try:
            connection = _electrum_connection_type()
        except Exception as e :input(e)

        if connection == False: connection = "NONE"
        set_terminal()
        print(f"""{orange}
########################################################################################{cyan}
                            Electrum Bitcoin Wallet Menu{orange}                   
########################################################################################

{red}
    CONNECTION TYPE: {black}{connection}

{green}
                   (s){orange}    Start/open Electrum 
{green}
                   (e){orange}    Connect to {blue}YOUR electrs {black}
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
            electrumexe = pp / "electrum" / "electrum.exe"
            subprocess.Popen(electrumexe)
            enter_continue("Electrum will open in a moment. Hit <enter> to continue.")
            return True
        elif choice.lower() == "e":
            _electrum_connect_electrs()
        elif choice.lower() == "pp":
            _electrum_connect_public()
        else:
            invalid()
       
def show_electrum_wallets():

    try: thefiles = subprocess.run(f"ls {electrum_wallet_directory}", shell=True, capture_output=True, text=True).stdout
    except: announce(f"""Directory does not exists.""") ; return False

    set_terminal()
    print(f"""
########################################################################################


    Directory:{cyan} {electrum_wallet_directory} {orange}


    Files: {bright_blue}

{thefiles}
{orange}
########################################################################################
""")
    enter_continue()

def get_electrum_config():
    try:
        with open(electrum_config_path, 'r') as file: 
            data = json.load(file)
        return data
    except Exception as e:
        input(e) 
        return False        

def _electrum_connection_type():            
    try:
        return get_electrum_config()["server"]
    except:
        return False  

def _electrum_connect_electrs():

    if _electrum_connection_type == "ELECTRUM_SERVER":
        return True

    try:

        configfile = get_electrum_config()
        configfile["server"] = "\"127.0.0.1:50005:t\""
        configfile["oneserver"] = "true"

        with open(electrum_config_path, 'w') as file:
            json.dump(configfile, file, indent=4)

    except: return False
    
    success("Electrum connection changed to your private electrs Server")
    return True

def _electrum_connect_public():
    
    if not yesorno("""This is bad for privacy, try to avoid it unless you know exactly
    what you are doing, or if it's an emergency.
    
    Really connect to a public server?"""): return False

    configfile = get_electrum_config()
    configfile["server"] = "\"electrum.bitaroo.net:50002:s\""

    with open(electrum_config_path, 'w') as file:
        json.dump(configfile, file, indent=4)
    
    success("Electrum connection changed to a Public Electrum Server")
    return True