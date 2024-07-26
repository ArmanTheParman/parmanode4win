########################################################################################
#check preliminaries with minimal overhead before restarting
########################################################################################

import platform, ctypes, sys, os

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
#DEBUG AND TESTING SECTION:
########################################################################################
from debugging_f import *
#debug(some_function=colour_check)
#debug("text")
#need "d" argument in position [1] when running

debug("pause")

########################################################################################
#Imports
########################################################################################

global version
version="0.0.1"
from pathlib import Path
make_parmanode_directories()
make_parmanode_files()
get_colours()
bitcoin_variables()
#get_IP_variables()
#get_date_variable()
from parmanode.intro_f import * 
from parmanode.motd_f import motd 
from parmanode.menu_main_f import *
from bitcoin.bitcoin_functions_f import *
from bitcoin.uninstall_bitcoin_f import *

#########################################################################################


########################################################################################

counter("rp")

if check_updates((0, 0, 1)) == "outdated":    #pass compiling version as int list argument
    suggestupdate()

########################################################################################

d = get_desktop_path()
input(d)

########################################################################################


intro()
instructions()
motd()
menu_main()

#print("intro done, exiting")