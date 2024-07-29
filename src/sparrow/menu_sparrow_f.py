from pmodules import *
import subprocess

def menu_sparrow():

    while True:

        set_terminal()
        print(f"""{orange}
########################################################################################{cyan}
                            Sparrow Bitcoin Wallet Menu{orange}                   
########################################################################################


{green}
                         (start){orange}    Start/open Sparrow
{cyan}
    CONNECTION:
{black}     
         Parmanode has already configured to connect Sparrow to Bitcoin Core
         running on this machine.
         
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
        elif choice.lower() == "start":
            sparrowexe = pp / "sparrow" / "Sparrow.exe"
            subprocess.run(sparrowexe)
            return True
        else:
            invalid()
