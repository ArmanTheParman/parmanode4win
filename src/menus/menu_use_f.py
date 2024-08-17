from variables import *
from functions import *
from bitcoin.menu_bitcoin_f import *
from sparrow.menu_sparrow_f import *
from tor.menu_tor_f import *
from docker.menu_docker_f import *
from electrum.menu_electrum_f import *
from config_f import *

def menu_use():
    
    while True:
        try: del available
        except: pass
        available=[]

        if ico.grep("bitcoin-end"): 
            use_bitcoinmenu = f"#                  {green} (b){orange}            Bitcoin Core                                        #"
            bitcoinmenu = True
            available.append(use_bitcoinmenu)
        else: 
            bitcoinmenu = False

        if ico.grep("sparrow-end"): 
            use_sparrowmenu = f"#                  {green} (s){orange}            Sparrow Bitcoin Wallet                              #"
            sparrowmenu = True
            available.append(use_sparrowmenu)
        else: 
            sparrowmenu = False

        if ico.grep("electrum-end"): 
            use_electrummenu = f"#                  {green} (e){orange}            Electrum Bitcoin Wallet                             #"
            electrummenu = True
            available.append(use_electrummenu)
        else: 
            electrummenu = False

        if ico.grep("tor-end"): 
            use_tormenu = f"#                  {green} (t){orange}            Tor                                                 #"
            tormenu = True
            available.append(use_tormenu)
        else: 
            tormenu = False
        if ico.grep("docker-end"): 
            use_dockermenu = f"#                  {green} (d){orange}            Docker                                              #"
            dockermenu = True
            available.append(use_dockermenu)
        else: 
            dockermenu = False
        
        set_terminal(h=38)
        print(f"""
########################################################################################
#                                                                                      #
#    P A R M A N O D E --> Main Menu -->{cyan} Use Programs Menu {orange}                            #
#                                                                                      #
########################################################################################
#                                                                                      #
#                                                                                      #""")
        for i in available:
            print(f"{i}")
            print("#                                                                                      #")
        print("""#                                                                                      #
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
        elif choice.lower() in {"e", "electrum"}:
            if electrummenu == False: continue
            if not menu_electrum(): return False
            return True
        elif choice.lower() in {"t", "tor"}:
            if tormenu == False: continue
            if not menu_tor(): return False
            return True
        elif choice.lower() in {"d", "docker"}:
            if dockermenu == False: continue
            if not menu_docker(): return False
            return True
        else:
            invalid()