from variables import *
from functions import *
from config_f import *
from parmanode.sned_sats_f import *

def install_electrum():
    
    sned_sats()

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
{cyan}{url}{orange}, trying again. {red}Q{orange} to abort""")
            if answer.upper() == "Q": return False
            else: continue
        if not download(urlasc, str(electrumpath)):
            answer = announce(f"""Download failed - It happens (you should b suine using Linxux BTW)
{cyan}{url2}{orange}, trying again. {red}Q{orange} to abort""")
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