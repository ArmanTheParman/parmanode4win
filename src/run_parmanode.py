
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
#do update version variable in variables_f also
if check_updates([0, 3, 0]) == "outdated":    #pass compiling version as int list argument
    try: suggestupdate()
    except Exception as e: input(e)

check_for_emergency("s")

########################################################################################
# from wsl.wsl_f import *
# input("pause")
# choice = announce("e for enable, d for disable, anything else for skip")

# if choice == "e":
#     enable_wsl()
# elif choice == "d":
#     disable_wsl()
########################################################################################

tidy_up_before_starting() #currently just manages Tor installation

try: from electrs.electrs_f import *
except Exception as e: input(e)

temp_patch()
input("temp patch done")
hello()
input("hello done")

if yesorno("""install electrs?""") == True:
    try: install_electrs() 
    except Exception as e: input(e)
    input("quitting")
    sys.exit()
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

