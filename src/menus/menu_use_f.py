from variables import *
from functions import *
from bitcoin.menu_bitcoin_f import *
from sparrow.menu_sparrow_f import *
from config_f import *

def menu_use():

    while True:

        if ico.grep("bitcoin-end"): 
            use_bitcoinmenu = f"#                  {green} (b){orange}            Bitcoin Core                                        #"
            bitcoinmenu = True
        else: 
            use_bitcoinmenu = "#                                                                                      #"
            bitcoinmenu = False

        if ico.grep("sparrow-end"): 
            use_sparrowmenu = f"#                  {green} (s){orange}            Sparrow Bitcoin Wallet                              #"
            sparrowmenu = True
        else: 
            use_sparrow = "#                                                                                      #"
            sparrowmenu = False

        print(f"""
########################################################################################
#                                                                                      #
#    P A R M A N O D E --> Main Menu -->{cyan} Use Programs Menu {orange}                            #
#                                                                                      #
########################################################################################
#                                                                                      #
#                                                                                      #
{use_bitcoinmenu}
#                                                                                      #
{use_sparrowmenu}
#                                                                                      #
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
        elif choice.lower() in {"b", "bitcoin"}:
            if bitcoinmenu == False: continue
            if not menu_bitcoin(): return False
            return True
        elif choice.lower() in {"s", "sparrow"}:
            if sparrowmenu == False: continue
            if not menu_sparrow(): return False
            return True
        else:
            invalid()