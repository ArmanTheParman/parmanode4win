########################################################################################
#check preliminaries with minimal overhead before restarting
########################################################################################

import ctypes, sys, os
from pathlib import Path

if not ctypes.windll.shell32.IsUserAnAdmin(): #is admin?
    # Re-launch the script with admin privileges
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:])
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        sys.exit(0)
    except Exception as e:
        print(f"Failed to elevate: {e}")
        sys.exit(1)

########################################################################################
try: from variables import *
except Exception as e: input(e)
########################################################################################
if not pp.exists():
    pp.mkdir() 
if not dp.exists():
    dp.mkdir()
if not tmp.exists():
    tmp.touch()

if not pc.exists():
    pc.touch()

if not ic.exists():
    ic.touch()

if not db.exists():
    db.touch()

if not rp_counter.exists():
    with rp_counter.open('w') as f:
        f.write("0" + '\n')

if not motd_counter.exists():
    with motd_counter.open('w') as f:
        f.write("0" + '\n')

if not before.exists():
    before.touch()

if not after.exists():
    after.touch()

if not difference.exists():
    difference.touch()

########################################################################################
#Imports
########################################################################################

from config_f import *
try: from functions import *
except Exception as e: input(e)
try: from installation_f import *
except Exception as e: input(e)

def install_parmanode():
    textdir = str(Path.home() / "parman_programs")

    if not yesorno(f"""
{cyan}                             P A R M A N O D E 4 W I N {orange}


    {orange}This installer program will quickly and painlessley install Parmanode4Win 
    on your computer. The program will live in this directory... 

    {textdir}
{orange}
    If you choose to proceed, the following will happen next...

{green}
            1){black} The Parmanode4Win script files (readable text open source code) will be 
               downloaded to your computer under the parman_programs directory.
{green}               
            2){black} Some dependencies programs will be installed - these are programs 
               Parmanode4Win needs to function properly:

{cyan}                      - chocolatey{black} (application package manager for Windows, it's great)
{cyan}                      - python {black} 
        {cyan}              - python packages {black} 
{cyan}                      - curl {black} 
{cyan}                      - git {black} 
{cyan}                      - gpg {black}
{green}    
            3){black} A shorcut to the program will be left on your Desktop.{orange}""", h=46): 
        return False

    try:
        git_clone_parmanode4win()
        dependency_check() 
        test_installation()
        desktop_shortcut()
        ico.add("parmanode4win-end")
        success(f"Parmanode4Win has been installed. Please run from the Desktop shortcut icon.")
        sys.exit()
    except Exception as e: input(e)

########################################################################################
# Installer
if p4w.exists():
    if not yesorno("""Parmanode4Win seems to already have been installed. You can attmpet
    a full uninstall, before attempting a reinstall."""):
        sys.exit()

if p4w.exists():
    announce("""Remnants of Parmanode still exists. Aborting. 
    You can call Parman for help.""")
    sys.exit()


try: 
    if check_installer_updates("0.0.1") == "outdated":

        if not yesorno(f"""There is a newer version of this installer. You could stop and get that instead.
        Do you want to quit this and get the newer, better version?"""):
            sys.exit()
except Exception as e: input(e)        

install_parmanode()
