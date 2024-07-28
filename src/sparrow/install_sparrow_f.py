from pmodules import *

def install_sparrow():

    global sparrowversion
    sparrowversion = "1.9.1"

    if ico.grep("sparrow-end") or ico.grep("sparrow-start"):
        announce("Parmanode thinks sparrow is already installed. Need to uninstall first.")
        return False
    
    global sparrowpath, sparrowzip, sparrowmanifest, sparrowsig, sparrowzippath, sparrowmanifestpath, sparrowsigpath
    sparrowpath = pp / "sparrow"
    sparrowzip = f"Sparrow-{sparrowversion}.zip"
    sparrowmanifest = f"sparrow-{sparrowversion}-manifest.txt"
    sparrowsig = f"sparrow-{sparrowversion}-manifest.txt.asc"
    sparrowzippath = sparrowpath / sparrowzip
    sparrowmanifestpath = sparrowpath / sparrowmanifest
    sparrowsigpath = sparrowpath / sparrowsig

    if not sparrowpath.exists():
        sparrowpath.mkdir()
    
    if not download_sparrow(): return False #also extracts and moves, zip left, unzipped dir deleted.

    if not verify_sparrow(): return False

    # does .sparrow wallet dir exist?


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

    If that doesn't work, hit{red} <control>{yellow}c{cyan} and Parmanode will try again.{orange}
                        """)

        if not download(url, str(sparrowpath)): 
            answer = announce(f"""Download failed - It happens (you should be using Linux BTW)
{cyan}{url}{orange}, trying again. {red}Q{orange} to abort""")
            if answer.upper() == "Q": return False
            else: continue
        if not download(url2, str(sparrowpath)):
            answer = announce(f"""Download failed - It happens (you should b suine using Linxux BTW)
{cyan}{url2}{orange}, trying again. {red}Q{orange} to abort""")
            if answer.upper() == "Q": return False
            else: continue
        if not download(url3, str(sparrowpath)):
            answer = announce(f"""Download failed - It happens (you should b suine using Linxux BTW)
{cyan}{url3}{orange}, trying again. {red}Q{orange} to abort""")
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
        #rename unzip folder to "bitcoin"
        sparrowunzippedpath = sparrowpath / f"Sparrow-{sparrowversion}"

        try:
            returncode = subprocess.run(["mv", f"""{str(sparrowunzippedpath)}/*""" , f"""{str(sparrowpath)}/*"""], check=True)
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
        input(e)
    try:
        checkkey = subprocess.run(["gpg", "--list-keys", "D4D0D3202FC06849A257B38DE94618334C674B40"], capture_output=True, text=True)
    except Exception as e:
        input(e)
        pass
    try:
        print(checkkey.stdout)
    except Exception as e:
        input(e)


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