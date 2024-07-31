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

    global electrum_config1, electrum_config2, electrum_config3
    electrum_config_dir = HOME / "Appdata" / "Roaming" / "electrum"
    electrum_config_path = electrum_config_dir / "config"
    if not electrum_config_dir.exists():
        electrum_config_dir.mkdir()

    bitcoin_dir = pco.grep("bitcoin_dir=", returnline=True).strip().split('=')[1]
    coreDD = ""
    for i in bitcoin_dir:
       if i == "\\":
         i = '/'
       coreDD = coreDD + i

    #can't use f string because of true/false interpretation
    electrum_config1 = """{
    "mode": "ONLINE",
    "bitcoinUnit": "BTC",
    "unitFormat": "DOT",
    "blockExplorer": "https://mempool.space",
    "feeRatesSource": "MEMPOOL_SPACE",
    "fiatCurrency": "USD",
    "exchangeSource": "COINGECKO",
    "loadRecentWallets": true,
    "validateDerivationPaths": true,
    "groupByAddress": true,
    "includeMempoolOutputs": true,
    "notifyNewTransactions": true,
    "checkNewVersions": false,
    "theme": "LIGHT",
    "openWalletsInNewWindows": false,
    "hideEmptyUsedAddresses": false,
    "showTransactionHex": true,
    "showLoadingLog": true,
    "showAddressTransactionCount": false,
    "showDeprecatedImportExport": false,
    "signBsmsExports": false,
    "preventSleep": false,
    "dustAttackThreshold": 1000,
    "enumerateHwPeriod": 30,
    "useZbar": true,
    "serverType": "BITCOIN_CORE",
    "publicElectrumServer": "ssl://bitcoin.lu.ke:50002|bitcoin.lu.ke",
    "coreServer": "http://127.0.0.1:8332",
    "coreAuthType": "USERPASS","""
    electrum_config2 = f"""    "coreDataDir": "{coreDD}","""
    electrum_config3 = """    "coreAuth": "parman:parman",
    "useLegacyCoreWallet": false,
    "useProxy": false,
    "autoSwitchProxy": true,
    "maxServerTimeout": 34,
    "maxPageSize": 100,
    "usePayNym": false,
    "mempoolFullRbf": false,
    "appWidth": 1083.0,
    "appHeight": 805.5
  }"""
    electrum_config_final = f"{electrum_config1}\n{electrum_config2}\n{electrum_config3}"
      
    with electrum_config_path.open('w') as f:
        f.write(electrum_config_final + '\n')

    return True