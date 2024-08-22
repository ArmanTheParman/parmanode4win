
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
from debugging import *
#debug(some_function=colour_check)
#debug("text")
#need "d" argument in position [1] when running

debug("pause")

########################################################################################
#Imports
########################################################################################
try: from variables import *
except Exception as e: input(e)

try: from config_f import *
except Exception as e: input(e)

try: from functions import *
except Exception as e: input(e)

try: lockfilefunction()
except Exception as e: input(e)
########################################################################################

counter("rp")
if check_updates([int(version[0]), int(version[1]), int(version[2])]) == "outdated":    #pass compiling version as int list argument
    try: suggestupdate()
    except Exception as e: input(e)

check_for_emergency("s")

tidy_up_before_starting() #currently just manages Tor installation

parmanode_ssl()
hello()

########################################################################################

try: from parmanode.intro_f import * 
except Exception as e: input(e)

try: intro()
except Exception as e: input(e)

try: instructions()
except Exception as e: input(e)

try: from parmanode.motd_f import motd ; motd()
except Exception as e: input(e)

try: from parmanode.menu_main_f import * ; menu_main()
except Exception as e: input(e)

