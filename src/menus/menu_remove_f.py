from functions import *
from bitcoin.uninstall_bitcoin_f import *
from sparrow.uninstall_sparrow_f import *
from electrum.uninstall_electrum_f import *
from tor.install_tor_f import *
from wsl.wsl_f import *
from docker.docker_f import *
from electrs.uninstall_electrs_f import *
from mempool.install_mempool_f import * 
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
            bitcoinmenu = False

        if ico.grep("sparrow-"): 
            rem_sparrow = f"#                  {green} (s){orange}            Sparrow Bitcoin Wallet                              #"
            sparrowmenu = True
            available.append(rem_sparrow)
        else: 
            sparrowmenu = False

        if ico.grep("electrum-"): 
            rem_electrum = f"#                  {green} (e){orange}            Electrum Bitcoin Wallet                             #"
            electrummenu = True
            available.append(rem_electrum)
        else: 
            electrummenu = False

        if ico.grep("tor-"): 
            rem_tor = f"#                  {green} (t){orange}            Tor                                                 #"
            tormenu = True
            available.append(rem_tor)
        else: 
            tormenu = False

        if ico.grep("wsl-"): 
            rem_wsl = f"#                  {green} (w){orange}            WSL                                                 #"
            wslmenu = True
            available.append(rem_wsl)
        else: 
            wslmenu = False
        
        if ico.grep("docker-"): 
            rem_docker = f"#                  {green} (d){orange}            Docker                                              #"
            dockermenu = True
            available.append(rem_docker)
        else: 
            dockermenu = False

        if ico.grep("electrs-"): 
            rem_electrs = f"#                  {green} (ers){orange}          Electrs                                             #"
            electrsmenu = True
            available.append(rem_electrs)
        else: 
            electrsmenu = False

        if ico.grep("mempool-"): 
            rem_mempool = f"#                  {green} (mem){orange}          Mempool                                             #"
            mempoolmenu = True
            available.append(rem_mempool)
        else: 
            mempoolmenu = False

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
        elif choice.lower() == "w":
            if wslmenu == False: continue
            if not disable_wsl(): return False
            return True
        elif choice.lower() == "d":
            if dockermenu == False: continue
            if not uninstall_docker(): return False
            return True
        elif choice.lower() == "ers":
            if electrsmenu == False: continue
            if not uninstall_electrs(): return False
            return True
        elif choice.lower() == "mem":
            if mempoolmenu == False: continue
            if not uninstall_mempool(): return False
            return True
        else:
            invalid()