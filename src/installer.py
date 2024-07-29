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
#Imports
########################################################################################
try: from functions import *
except Exception as e: input(e)
try: from functions import *
except Exception as e: input(e)


def install_parmanode():

    if not yesorno(f"""
{cyan}                             P A R M A N O D E 4 W I N {orange}

{red}
    If you choose to proceed, the following will happen...

{green}
    1){orange} The{cyan} Parmanode4Win{orange} script files (readable text open source code) 
      will be downloaded to your computer.
{green}    
    2){orange} An executable file which was created ('compiled') from that code will be moved 
      to the 'Program files \\ Parmanode4Win' folder.
{green}
    3){orange} A shorcut to the program file executable will be left on your Desktop.
{green}               
    4){orange} Some dependencies programs will be installed - these are programs 
      Parmanode4Win needs to function properly:

{cyan}              - chocolatey{orange} (application package manager for Windows, it's great)
{cyan}              - curl {orange} 
{cyan}              - git {orange} 
{cyan}              - gpg {orange}""", h=42): 
        return False

    git_clone_parmanode4win()
    desktop_shortcut()
    #    test_installation()
    make_parmanode_directories()
    make_parmanode_files()
    ico.add("parmanode-end")
    success(f"Parmanode4Win has been installed. Please run from the Desktop shortcut icon.")
    sys.exit()

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


if check_installer_updates() == "outdated":

    if not yesorno(f"""There is a newer version of this installer. You could stop and get that instead.
    Do you want to quit this and get the newer, better version?"""):
        sys.exit()

install_parmanode()
