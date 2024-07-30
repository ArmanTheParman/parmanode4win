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

########################################################################################
#Imports
########################################################################################

try: from variables import *
except Exception as e: input(e)
try: from functions import *
except Exception as e: input(e)
try: from installation_f import *
except Exception as e: input(e)

def install_parmanode():
    textdir = str(Path.home() / "parman_programs")

    if not yesorno(f"""
{cyan}                             P A R M A N O D E 4 W I N {orange}

{red}
               If you choose to proceed, the following will happen...

{green}
    1){orange} The directory with subfolders will be created:{cyan} 
       
              {textdir}
{green}
    2){orange} The Parmanode4Win script files (readable text open source code) will be 
       downloaded to your computer under the parman_programs directory.
{green}               
    3){orange} Some dependencies programs will be installed - these are programs 
       Parmanode4Win needs to function properly:

{cyan}              - chocolatey{black} (application package manager for Windows, it's great)
{cyan}              - python {orange} 
{cyan}              - python packages {orange} 
{cyan}              - curl {orange} 
{cyan}              - git {orange} 
{cyan}              - gpg {orange}
{green}    
    4){orange} A shorcut to the program will be left on your Desktop.""", h=46): 
        return False

    make_parmanode_directories()
    make_parmanode_files()
    from config_f import ico 

    try:
        input("zzzz a")
        git_clone_parmanode4win()
        input("zzzz b")
        dependency_check() 
        input("zzzz c")
        test_installation()
        input("zzzz d")
        desktop_shortcut()
        input("zzzz e")
        ico.add("parmanode4win-end")
        input("zzzz f")
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
