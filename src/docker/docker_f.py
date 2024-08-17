import subprocess, os
from variables import *
from functions import *


def install_docker():
    try: subprocess.run(["powershesll", "choco install docker-desktop -y"], check=True, capture_output=True)
    except Exception as e: input(e)
    ico.add("docker-end")
    os.system('c:/Program files/Docker/Docker/"docker desktop.exe')
    success(f"""Docker has been installed. Before it can work, a window (docker-desktop app) 
    will pop up and you need to accept the terms and conditions, and do it's stupid
    survey - it's ok to click 'skip'.""") 

r"""
    # WSL needs to be installed first

    # choco install docker-desktop -y

    # #restart computer to set path correctly -- maybe. test it

    # docker bin files:
    #      c:\Program files\Docker\Docker\resources\bin

    Run docker desktop, user needs to accept terms first...
    #      c:\Program files\Docker\Docker\"docker desktop.exe"
    
 """

def uninstall_docker():
    if yesorno(f"""Are you sure you want to uninstall Docker?""") == False: return False

    try: subprocess.run(["powershell", "wsl --unregister docker-desktop"], capture_output=True, check=True)
    except: pass

    try: 
        subprocess.run(["powershell", "choco uninstall docker-desktop -y"])
        ico.remove("docker-")
        success("Docker has been uninstalled")
        return True
    except: return False

    

     



    