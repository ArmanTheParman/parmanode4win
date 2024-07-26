from parmanode.install_parmanode import install_parmanode
if not install_parmanode():
    quit()

import platform, ctypes, sys, os
if platform.system() == "Windows":
    if sys.getwindowsversion().major < 10:
        print(f"{red}You need at least Windows 10 to run Parmanode. Exiting.")
        input("Hit enter") 
        quit()

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

    try:
        from dependencies.chocolatey_f import *
        dependency_check()
    except Exception as e:
        input(e)


########################################################################################
#Imports
########################################################################################
from pathlib import Path
from pmodules import *
from parmanode.intro_f import * 
from parmanode.install_parmanode import *
from parmanode.motd_f import motd 
from parmanode.menu_main_f import *
from bitcoin.bitcoin_functions_f import *
from bitcoin.uninstall_bitcoin_f import *
import subprocess




##### Main installtion program begins #####

#directories made with variables module
git_clone_parmanode4win()
desktop_shortcut()
#    test_installation()
success(f"Parmanode4Win has been installed")
quit()
