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
make_parmanode_directories()
make_parmanode_files()
get_colours()
bitcoin_variables()
#get_IP_variables()
#get_date_variable()

#########################################################################################


########################################################################################



########################################################################################

counter("rp")

if check_updates((0, 0, 1)) == "outdated":    #pass compiling version as int list argument
    suggestupdate()

from parmanode.intro_f import * 
intro()
instructions()

from parmanode.motd_f import motd 
motd()

from parmanode.menu_main_f import *
menu_main()

#print("intro done, exiting")