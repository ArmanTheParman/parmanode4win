from variables import *
from functions import *
from config_f import *
import subprocess

def menu_electrum():

    while True:

        set_terminal()
        print(f"""{orange}
########################################################################################{cyan}
                            Electrum Bitcoin Wallet Menu{orange}                   
########################################################################################


{green}
                         (s){orange}    Start/open Electrum 
{black}
    CONNECTION:
         
         Currently connecting to a PUBLIC NODE. Private options coming soon. 

{orange}
########################################################################################
""")

        choice = choose("xpmq")
        set_terminal()

        if choice.upper() in {"Q", "EXIT"}: 
            sys.exit()
        elif choice.upper() == "P":
            return True
        elif choice.upper() == "M":
            return True
        elif choice.lower() in {"start", "s"}:
            electrumexe = pp / "electrum" / "electrum.exe"
            subprocess.Popen(electrumexe)
            enter_continue("Electrum will open in a moment. Hit <enter> to continue.")
            return True
        else:
            invalid()