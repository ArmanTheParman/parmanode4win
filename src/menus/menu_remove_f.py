from functions import *
from bitcoin.uninstall_bitcoin_f import *
from sparrow.uninstall_sparrow_f import *
from electrum.uninstall_electrum_f import *
from parmanode.menu_main_f import *
from config_f import *

def menu_remove():
    if ico.grep("bitcoin-"): 
        rem_bitcoin = f"#                  {green} (b){orange}            Bitcoin Core                                        #"
        bitcoinmenu = True
    else: 
        rem_bitcoin ="#                                                                                      #"
        bitcoinmenu = False

    if ico.grep("sparrow-"): 
        rem_sparrow = f"#                  {green} (s){orange}            Sparrow Bitcoin Wallet                              #"
        sparrowmenu = True
    else: 
        rem_sparrow ="#                                                                                      #"
        sparrowmenu = False

    if ico.grep("electrum-"): 
        rem_electrum = f"#                  {green} (e){orange}            Electrum Bitcoin Wallet                             #"
        electrummenu = True
    else: 
        rem_electrum ="#                                                                                      #"
        electrummenu = False

    while True:
        set_terminal()
        print(f"""
########################################################################################
#                                                                                      #
#    P A R M A N O D E --> Main Menu -->{cyan} Remove Menu {orange}                                  #
#                                                                                      #
########################################################################################
#                                                                                      #
#                                                                                      #
{rem_bitcoin}
#                                                                                      #
{rem_sparrow}
#                                                                                      #
{rem_electrum}
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
        elif choice.lower() == "b":
            if bitcoinmenu == False: continue
            if not uninstall_bitcoin(): return False
            return True
        elif choice.lower() == "b":
            if bitcoinmenu == False: continue
            if not uninstall_bitcoin(): return False
            return True
        elif choice.lower() == "s":
            if sparrowmenu == False: continue
            if not uninstall_sparrow(): return False
            return True
        elif choice.lower() == "e":
            if electrummenu == False: continue
            if not uninstall_electrum(): return False
            return True
        else:
            invalid()