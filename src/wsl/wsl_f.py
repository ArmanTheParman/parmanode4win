import subprocess, os
from variables import *
from functions import *

def disable_wsl():

    set_terminal()

    if ico.grep("docker-end") == True:
        if yesorno("Disabling WSL will also disable Docker. Do it?") == False : return False
    else:
        if yesorno("Are you sure you want to disable WSL?") == False: return False

    _unregister_all_wsl_distributions()

    try:
        subprocess.run(["powershell", "-Command", "Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux -NoRestart"], check=True)
    except Exception as e: input(e)

    try:
        subprocess.run(["powershell", "-Command", "Disable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform"], check=True)
    except Exception as e: input(e)

    ico.remove("wsl-")
    success("WSL has been removed")

def enable_wsl():
    #Ensure that virtualization is enabled in your BIOS/UEFI settings. This is required for WSL 2.

    if yesorno(f"""You are about to install {cyan}WINDOWS SUBSYSTEM FOR LINUX.{orange}
            
    During the installation, you may or may not be asked to create a Linux username
    and password. If that happens, you'll then automatically be logged in to the Linux
    Terminal. You need to type {red}'exit'{orange} and then hit {cyan}<enter>{orange} to continue back to 
    Parmanode, and the installation.
    {red}
    You'll also need to restart the computer once installation is done, AND, 
    if an update is needed, testing has shown you need to do that too, but 
    I could be wrong.

    {orange} 
    Continue?""", h=48) == False: return False
    
    try:
        subprocess.run(["powershell", "dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart"], check=True)
    except Exception as e: 
        pass

    try:
        subprocess.run(["powershell", "dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart"], check=True)
    except Exception as e: 
        pass
    
    try: 
        subprocess.run(["powershell", "wsl --set-default-version 2"], check=True) 
    except Exception as e: pass

    try:
        subprocess.run(["powershell", "wsl --update"], check=True) #necessary, install can fail without it
    except Exception as e:
        pass

    try: 
        subprocess.run(["powershell", "wsl --install"], check=True) 
    except Exception as e: pass

    #after that, check if any distro installed.  May not have, but may have. If none, install debian.
    #new username and password is prompted for.
    #new session in linux entered. type 'exit' to get out.
    #wsl --list, lists distros, and also docker
    #Look vor version2 of wsl. If not, instruct user to manually enable virualisation and give a website.

    ico.add("wsl-end")
    success("WSL has been installed. You may need to reboot the computer for it to take effect.")
    return True



def _unregister_all_wsl_distributions():
    try:
        result = subprocess.run(["powershell", "wsl --list --quiet"], capture_output=True, text=True, check=True).stdout.strip()
        tmpo.truncate()
        tmpo.add(result)

        try: del distros
        except: pass
        distros = []

        with open(tmp, 'r') as f:
            for i in f.readlines():
                if len(i) < 3: continue
                i = i.replace('\x00', '')  # Remove any null bytes
                distros.append(i.strip())

        for distro in distros:
            print(distro, type(distro))
            print(f"{red}Unregistering distro {distro}...{orange}")
            try: subprocess.run(["powershell", f"wsl --unregister {distro}"], capture_output=True, check=True)
            except Exception as e: input(e)

    except subprocess.CalledProcessError as e:
        input(f"An error occurred: {e}")


# wsl --list
# if no distros and wsl enabled...
# Line 0...
# "Windows Subsystem for Linux has no installed distributions.""

# wsl --list
# if wsl disabled
# Line 0 ...
# "This application requires the Windows Subsystem for Linux Optionsl Component."

# wsl --list
# if wsl enabled with no distributions
# Line 0 ...
# "Windows Subsystem for Linux has no installed distributions"