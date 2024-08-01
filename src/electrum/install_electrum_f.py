from variables import *
from functions import *
from config_f import *
from parmanode.sned_sats_f import *

def install_electrum():
    
    sned_sats()

    if not electrum_warning(): return False

    global electrumversion 
    electrumversion = "4.5.5"
    
    filename = f"electrum-{electrumversion}.exe"
    url = f"https://download.electrum.org/{electrumversion}/{filename}"
    urlasc = f"{url}.asc"

    if ico.grep("electrum-end") or ico.grep("electrum-start"):
        announce("Parmanode thinks Electrum is already installed. Need to uninstall first.")
        return False
    
    global electrumpath, electrumsig, electrumsigpath

    electrumpath = pp / "electrum"
    electrumsig = f"{filename}.asc"
    electrumsigpath = electrumpath / electrumsig
    electrumexepath = electrumpath / filename

    if not electrumpath.exists():
        electrumpath.mkdir()
    ico.add("electrum-start") 
    if not download_electrum(url, urlasc): return False

    if not verify_electrum(exepath=electrumexepath): return False

    if not make_electrum_config(): return False

    ico.add("electrum-end")
    success("Electrum has been installed")
    return True

########################################################################################
########################################################################################
########################################################################################

def download_electrum(url, urlasc):
    
    while True:

        please_wait(f"""{green}Downloading Electrum and signature file.
    {cyan} 
    If it freezes, someitmes hitting <enter> breathes life into it for some reason. 
    I don't know why. Windows, pfffff, I hate it.

    If that doesn't work, hit{red} <control>{green}c{cyan} and Parmanode will try again.{orange}
                        """)

        if not download(url, str(electrumpath)): 
            answer = announce(f"""Download failed - It happens (you should be using Linux BTW)
    Tying again. {red}Q{orange} to abort""")
            if answer.upper() == "Q": return False
            else: continue
        if not download(urlasc, str(electrumpath)):
            answer = announce(f"""Download failed - It happens (you should b suine using Linxux BTW)
    Tying again. {red}Q{orange} to abort""")
            if answer.upper() == "Q": return False
            else: continue
        break
    
    return True

def verify_electrum(exepath):
    global keyfail
    keyfail = True

    #Get Thomas V's public key
    thomas = p4w / "src" / "electrum" / "ThomasV.asc"
    try:
        result = subprocess.run(["gpg", "--import", f"{thomas}"], check=True)
    except Exception as e:
        input(e)

    try:
        verifysig = subprocess.run(["gpg", "--verify", str(electrumsigpath), str(exepath)], text=True, capture_output=True) 
    except:
        pass

    if "Good" in verifysig.stdout or "Good" in verifysig.stderr:
        print(f"""{green}
Electrum has been successfully downloaded and verified for authenticity using 
both sha256 and gpg.{orange}

""")
        enter_continue()
        newpath = electrumpath / "electrum.exe"
        try: moving = subprocess.run(["mv", str(exepath), str(newpath)], check=True, capture_output=True, text=True)
        except:
            print(moving.stdout)
            enter_continue()
        return True
    else:
        announce(f"There was a problem verifying the signature file with Thomas V's signature. Aborting.")
        return False

def make_electrum_config():

    global electrum_config1
    electrum_config_dir = HOME / "Appdata" / "Roaming" / "electrum"
    electrum_config_path = electrum_config_dir / "config"
    if not electrum_config_dir.exists():
        electrum_config_dir.mkdir()

    electrum_config = """{
    "auto_connect": false,
    "check_updates": false,
    "config_version": 3,
    "decimal_point": 0,
    "is_maximized": false,
    "num_zeros": 0,
    "oneserver": true,
    "qt_gui_color_theme": "dark",
    "rpcpassword": "JWn_CSr5PVOrSqrStD9HHw==",
    "rpcuser": "user",
    "server": "wsw6tua3xl24gsmi264zaep6seppjyrkyucpsmuxnjzyt3f3j6swshad.onion:50002:s",
    "show_addresses_tab": true,
    "show_notes_tab": false,
    "show_utxo_tab": true 
}"""

    with electrum_config_path.open('w') as f:
        f.write(electrum_config + '\n')

    return True

def electrum_warning():
    if not yesorno(f"""
    Please be aware that currently, {orange}Electrum Wallet {orange}automatically connects to
    a public node.{red} DO NOT USE ELECTRUM IF YOU DON'T WANT THIS{orange}. Public nodes capture
    your wallet addresses and potentially your location - not great. 

    An alternative for now is Sparrow Bitcoin Wallet.
{black}            

    This problem exists because Electrum must connect to an Electrum SERVER, and 
    can't connect to Bitcoin Core directly the way Saprrow can. There are good 
    reasons for it and it's beside the point for now.
            
    In the future, Parmanode4Win will have an option to install your own Electrum 
    Server, but it's not available just yet - I'm working as fast as I can. If you're
    in a hurry, you can use Parmanode on a Mac or Linux - that version has many more 
    features; The Windows one is lagging behind.
{yellow}

    Continue with installtion of Electrum WALLET?""", h=42):
        return False
    else:
        return True