from functions import *
from bitcoin.uninstall_bitcoin_f import *
from sparrow.uninstall_sparrow_f import *
from electrum.uninstall_electrum_f import *
from tor.install_tor_f import *
from parmanode.menu_main_f import *
from config_f import *

def menu_remove():

    while True:

        try: del available
        except: pass
        available=[] 

        if ico.grep("bitcoin-"): 
            rem_bitcoin = f"#                  {green} (b){orange}            Bitcoin Core                                        #"
            bitcoinmenu = True
            available.append(rem_bitcoin)
        else: 
            rem_bitcoin ="#                                                                                      #"
            bitcoinmenu = False

        if ico.grep("sparrow-"): 
            rem_sparrow = f"#                  {green} (s){orange}            Sparrow Bitcoin Wallet                              #"
            sparrowmenu = True
            available.append(rem_sparrow)
        else: 
            rem_sparrow ="#                                                                                      #"
            sparrowmenu = False

        if ico.grep("electrum-"): 
            rem_electrum = f"#                  {green} (e){orange}            Electrum Bitcoin Wallet                             #"
            electrummenu = True
            available.append(rem_electrum)
        else: 
            rem_electrum ="#                                                                                      #"
            electrummenu = False

        if ico.grep("tor-"): 
            rem_tor = f"#                  {green} (t){orange}            Tor                                                 #"
            tormenu = True
            available.append(rem_tor)
        else: 
            rem_tor ="#                                                                                      #"
            tormenu = False

        set_terminal()
        print(f"""
########################################################################################
#                                                                                      #
#    P A R M A N O D E --> Main Menu -->{cyan} Remove Menu {orange}                                  #
#                                                                                      #
########################################################################################
#                                                                                      #
#                                                                                      #""")

        for i in available:
            print(f"{i}")
            print("#                                                                                      #")
        print("""
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
        elif choice.lower() == "t":
            if tormenu == False: continue
            if not uninstall_tor(): return False
            return True
        else:
            invalid()