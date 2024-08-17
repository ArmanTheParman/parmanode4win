import subprocess, os
from variables import *
from functions import *


def install_docker():

    if yesorno(f"""Do you want install Docker? It takes several minutes.""") == False: return False

    if yesorno(f"""    {bright_blue}
    ANOTHER THING... 
    
    For Docker to work properly, the computer needs 'virtalisation' enabled on
    the bios. You can see after installation if Docker works, and if it doesn't
    you can investigate...
    
    You'd enter the bios menu (look up how to do that on line for your specific
    computer model), then look for the virtualisation option. Change it from
    <disabled> to <enabled>, save, reboot, and then see if Docker loads up.

    Unfortunately, there is no way for Parmanode to modify the BIOS for you. 
    You can do a search online or ask an AI bot like ChatGPT if you're having 
    trouble.{orange}""") == False: return False

    if ico.grep("wsl-end") == False:
        announce(f"""To install Docker, you need to install/enable{cyan} WSL {orange}first. You'll find that
    option in the add menu.""")
        return False
    else:
        try: 
            subprocess.run(["wsl", "--list", "--quiet"], check=True)
        except:
            announce("""It looks like you've installed WSL, but may not have rebooted yet?
    Whatever the reason, WSL isn't working properly and Docker can't be installed.
    When in doubt, turn it off and on again.""")
            return False

    set_terminal()
    please_wait()
    try: subprocess.run(["powershell", "choco install docker-desktop -y"], check=True, capture_output=True)
    except Exception as e: input(e)
    ico.add("docker-end")
    subprocess.Popen('c:/Program files/Docker/Docker/Docker Desktop.exe')
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
    please_wait()

    try: subprocess.run(["powershell", "wsl --unregister docker-desktop"], capture_output=True, check=True)
    except: pass

    try: 
        subprocess.run(["powershell", "choco uninstall docker-desktop -y"], capture_output=True, check=True)
        ico.remove("docker-")
        set_terminal()
        success("Docker has been uninstalled")
        return True
    except: return False

    

     



    