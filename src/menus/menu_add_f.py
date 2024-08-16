from functions import *
from bitcoin.install_bitcoin_f import *
from sparrow.install_sparrow_f import *
from electrum.install_electrum_f import *
from tor.install_tor_f import *
from config_f import *

def menu_add():

    while True:
        try: del available
        except: pass
       
        available=[] 
        
        if not ico.grep("bitcoin-"):
            add_bitcoin = f"#                  {green} (b){orange}            Bitcoin Core                                        #"
            bitcoinmenu = True
            available.append(add_bitcoin)
        else: 
            add_bitcoin ="#                                                                                      #"
            bitcoinmenu = False

        if not ico.grep("sparrow-"):
            add_sparrow = f"#                  {green} (s){orange}            Sparrow Bitcoin Wallet                              #"
            sparrowmenu = True
            available.append(add_sparrow)
        else: 
            add_sparrow ="#                                                                                      #"
            sparrowmenu = False

        if not ico.grep("electrum-"):
            add_electrum = f"#                  {green} (e){orange}            Electrum Bitcoin Wallet                             #"
            electrummenu = True
            available.append(add_electrum)
        else: 
            add_electrum ="#                                                                                      #"
            electrummenu = False

        if not ico.grep("tor-"):
            add_tor = f"#                  {green} (t){orange}            Tor                                                 #"
            tormenu = True
            available.append(add_tor)
        else: 
            add_tor ="#                                                                                      #"
            tormenu = False

        set_terminal(h=38)
        print(f"""
########################################################################################
#                                                                                      #
#    P A R M A N O D E --> Main Menu -->{cyan} Install Menu {orange}                                 #
#                                                                                      #
########################################################################################
#                                                                                      #
#                                                                                      #
#                                                                                      #"""

for i in available:
    print(f"{i}")
    print("#                                                                                      #")

print("""#                                                                                      #
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
        elif choice.lower() == "e":
            if electrummenu == False : continue
            if not install_electrum(): return False
            return True
        elif choice.lower() == "t":
            if tormenu == False : continue
            if not install_tor(): return False
            return True
        else:
            invalid()
