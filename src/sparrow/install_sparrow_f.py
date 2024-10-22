from variables import *
from functions import *
from config_f import *
from parmanode.sned_sats_f import *

def install_sparrow():

    global sparrowversion
    sparrowversion = "1.9.1"

    if ico.grep("sparrow-end") or ico.grep("sparrow-start"):
        announce("Parmanode thinks Sparrow is already installed. Need to uninstall first.")
        return False
    
    global sparrowpath, sparrowzip, sparrowmanifest, sparrowsig, sparrowzippath, sparrowmanifestpath, sparrowsigpath
    sparrowpath = pp / "sparrow"
    sparrowzip = f"Sparrow-{sparrowversion}.zip"
    sparrowmanifest = f"sparrow-{sparrowversion}-manifest.txt"
    sparrowsig = f"sparrow-{sparrowversion}-manifest.txt.asc"
    sparrowzippath = sparrowpath / sparrowzip
    sparrowmanifestpath = sparrowpath / sparrowmanifest
    sparrowsigpath = sparrowpath / sparrowsig

    sned_sats()

    if not sparrowpath.exists():
        sparrowpath.mkdir()
    ico.add("sparrow-start") 
    if not download_sparrow(): return False 

    if not verify_sparrow(): return False

    if not make_sparrow_config(): return False

    ico.add("sparrow-end")
    success("Sparrow has been installed")
    return True

########################################################################################
########################################################################################
########################################################################################

def download_sparrow():
    url=f"https://github.com/sparrowwallet/sparrow/releases/download/1.9.1/Sparrow-{sparrowversion}.zip"
    url2=f"https://github.com/sparrowwallet/sparrow/releases/download/1.9.1/sparrow-{sparrowversion}-manifest.txt"
    url3=f"https://github.com/sparrowwallet/sparrow/releases/download/1.9.1/sparrow-{sparrowversion}-manifest.txt.asc"
    
    while True:

        please_wait(f"""{green}Downloading Sparrow, and checksums and gpg signature.
    {cyan} 
    If it freezes, someitmes hitting <enter> breathes life into it for some reason. 
    I don't know why. Windows, pfffff, I hate it.

    If that doesn't work, hit{red} <control>{green}c{cyan} and Parmanode will try again.{orange}
                        """)

        if not download(url, str(sparrowpath)): 
            answer = announce(f"""Download failed - It happens (you should be using Linux BTW)
    Tying again. {red}Q{orange} to abort""")
            if answer.upper() == "Q": return False
            else: continue
        if not download(url2, str(sparrowpath)):
            answer = announce(f"""Download failed - It happens (you should b suine using Linxux BTW)
    Tying again. {red}Q{orange} to abort""")
            if answer.upper() == "Q": return False
            else: continue
        if not download(url3, str(sparrowpath)):
            answer = announce(f"""Download failed - It happens (you should b suine using Linxux BTW)
    Tying again. {red}Q{orange} to abort""")
            if answer.upper() == "Q": return False
            else: continue
        break

    try:
        sparrowzippath
        if not sparrowzippath.exists():
            input(f"""    Download seems to have failed, Parmanode doesn't detect it. Hit <enter>.""")
            return False
        please_wait(f"{green}Unzipping Sparrow{orange}")
        try:
            unzip_file(str(sparrowzippath), directory_destination=str(sparrowpath)) 
        except Exception as e:
            input(e)
        #rename unzip folder
        sparrowunzippedpath = sparrowpath / f"Sparrow"
        try:
            returncode = subprocess.run(["mv", f"""{str(sparrowunzippedpath)}/*""" , f"""{str(sparrowpath)}/"""], check=True)
            delete_directory(sparrowunzippedpath)
        except Exception as e:
           input(e) 

        
    except Exception as e:
        input(e)
        return False
    
    return True

def verify_sparrow():
    global keyfail
    keyfail = True

    #Get Craig Raw's public key
    try:
        result = subprocess.run(["gpg", "--keyserver", "hkps://keyserver.ubuntu.com", "--recv-keys", "D4D0D3202FC06849A257B38DE94618334C674B40"], check=True)
    except Exception as e:
        pass
    try:
        checkkey = subprocess.run(["gpg", "--list-keys", "D4D0D3202FC06849A257B38DE94618334C674B40"], capture_output=True, text=True)
    except Exception as e:
        pass


    if "D4D0D3202FC06849A257B38DE94618334C674B40" in checkkey.stdout:
        keyfail = False
    else:
        announce(f"""There was a problem obtaining Craig Raw's key ring. Proceed with caution.""")
        keyfail = True

    #Hash the zip path

    hashresult = subprocess.run(["certutil", "-hashfile", str(sparrowzippath), "sha256"], text=True, capture_output=True)    
    target_hash = "e498944e31d69befd8f13a1455ab00e2e0246f5ca69ca782edde7742685fdd4e"

    with sparrowmanifestpath.open('r') as f:
        contents = f.read()
        if "e498944e31d69befd8f13a1455ab00e2e0246f5ca69ca782edde7742685fdd4e" in contents:
            pass
        else:
            announce("""Problem with SHA256SUMS file. Antcipated hash not found in document.
    Proceed with caution.""")
    
    if not target_hash in hashresult.stdout:
        announce("""checksum failed - indicates a problem with the download. Aborting.""")
        return False


    try:
        sha256sumsverify = subprocess.run(["gpg", "--verify", str(sparrowsigpath), str(sparrowmanifestpath)], text=True, capture_output=True) 
    except:
        pass

    if "Good" in sha256sumsverify.stdout or "Good" in sha256sumsverify.stderr:
        print(f"""{green}
Sparrow has been successfully downloaded and verified for authenticity using 
both sha256 and gpg.{orange}

""")
        enter_continue()
        return True
    else:
        announce(f"There was a problem verifying the SHA256SUMS file with Craig Raw's signature. Aborting.")
        return False

def make_sparrow_config():

    if not sparrow_config_dir.exists():
        sparrow_config_dir.mkdir()

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

    #can't use f string because of true/false interpretation
    sparrow_config1 = """{
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
    "publicElectrumServer": "ssl://electrum.bitaroo.net:50002|electrum.bitaroo.net",
    "coreServer": "http://127.0.0.1:8332",
    "coreAuthType": "USERPASS","""
    sparrow_config2 = f"""    "coreDataDir": "{coreDD}","""
    sparrow_config3 = f"""    "coreAuth": "{rpcuser}:{rpcpassword}",
    "useLegacyCoreWallet": false,
    "useProxy": false,
    "autoSwitchProxy": true,
    "maxServerTimeout": 34,
    "maxPageSize": 100,
    "usePayNym": false,
    "mempoolFullRbf": false,
    "appWidth": 1083.0,
    "appHeight": 805.5
  }}"""
    sparrow_config_final = f"{sparrow_config1}\n{sparrow_config2}\n{sparrow_config3}"
      
    with sparrow_config_path.open('w') as f:
        f.write(sparrow_config_final + '\n')

    return True