from variables import *
from functions import *
import subprocess

def menu_sparrow():

    while True:

        set_terminal()
        print(f"""{orange}
########################################################################################{cyan}
                            Sparrow Bitcoin Wallet Menu{orange}                   
########################################################################################


{green}
                         (s){orange}    Start/open Sparrow
{black}
    CONNECTION:
         
         Parmanode has already configured to connect Sparrow to Bitcoin Core
         running on this machine.

         If having connection issues, try the oldest trick in the book...
         
                                - Sparrow restart
                                - Bitcoin Core restart
                                - Computer restart
{blue}

         More connection options will come in the future.

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
            sparrowexe = pp / "sparrow" / "Sparrow.exe"
            subprocess.run(sparrowexe)
            return True
        else:
            invalid()
