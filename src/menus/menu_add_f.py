from bitcoin.install_bitcoin_f import *
from sparrow.install_sparrow_f import *

def menu_add():
    if not ico.grep("bitcoin-end"):
        add_bitcoin = f"#                  {green} (b){orange}            Bitcoin Core                                        #"
        bitcoinmenu = True
    else: 
        add_bitcoin ="#                                                                                      #"
        bitcoinmenu = False

    if not ico.grep("sparrow-end"):
        add_sparrow = f"#                  {green} (s){orange}            Sparrow                                             #"
        sparrowmenu = True
    else: 
        add_sparrow ="#                                                                                      #"
        sparrowmenu = False

    while True:
        set_terminal()
        print(f"""
########################################################################################
#                                                                                      #
#    P A R M A N O D E --> Main Menu -->{cyan} Install Menu {orange}                                 #
#                                                                                      #
########################################################################################
#                                                                                      #
#                                                                                      #
#                                                                                      #
{add_bitcoin}
#                                                                                      #
{add_sparrow}
#                                                                                      #
#                                                                                      #
#                                                                                      #
#                                   {red}          ... more programs soon {orange}                  #
#                                                                                      #
########################################################################################
""")
        choice = choose("xpmq")
        if choice in {"q", "Q", "Quit", "exit", "EXIT"}: 
            sys.exit()
        elif choice in {"p", "P"}:
            return True
        elif choice in {"m", "M"}:
            return True 
        elif choice in {"b", "B", "Bitcoin", "bitcoin"}:
            if bitcoinmenu == False : continue
            if not install_bitcoin(): return False
            return True
        elif choice.lower() == "s":
            if sparrowmenu == False : continue
            if not install_sparrow(): return False
            return True
        else:
            invalid()
