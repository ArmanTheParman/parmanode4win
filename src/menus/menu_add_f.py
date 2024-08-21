from functions import *
from bitcoin.install_bitcoin_f import *
from sparrow.install_sparrow_f import *
from electrum.install_electrum_f import *
from tor.install_tor_f import *
from wsl.wsl_f import *
from docker.docker_f import *
from electrs.electrs_f import install_electrs 
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
            bitcoinmenu = False

        if not ico.grep("sparrow-"):
            add_sparrow = f"#                  {green} (s){orange}            Sparrow Bitcoin Wallet                              #"
            sparrowmenu = True
            available.append(add_sparrow)
        else: 
            sparrowmenu = False

        if not ico.grep("electrum-"):
            add_electrum = f"#                  {green} (e){orange}            Electrum Bitcoin Wallet                             #"
            electrummenu = True
            available.append(add_electrum)
        else: 
            electrummenu = False

        if not ico.grep("tor-"):
            add_tor = f"#                  {green} (t){orange}            Tor                                                 #"
            tormenu = True
            available.append(add_tor)
        else: 
            tormenu = False

        if not ico.grep("wsl-"):
            add_wsl = f"#                  {green} (w){orange}            WSL{grey} (requires restart){orange}                              #"
            wslmenu = True
            available.append(add_wsl)
        else: 
            wslmenu = False

        if not ico.grep("docker-"):
            add_docker= f"#                  {green} (d){orange}            Docker Desktop {grey}(requires WSL){orange}                       #"
            dockermenu = True
            available.append(add_docker)
        else: 
            dockermenu = False

        if not ico.grep("electrs-"):
            add_electrs= f"#                  {green} (ers){orange}          Electrs {grey}(requires Docker){orange}                           #"
            electrsmenu = True
            available.append(add_electrs)
        else: 
            electrsmenu = False

        set_terminal(h=38)
        print(f"""
########################################################################################
#                                                                                      #
#    P A R M A N O D E --> Main Menu -->{cyan} Install Menu {orange}                                 #
#                                                                                      #
########################################################################################
#                                                                                      #
#                                                                                      #
#                                                                                      #""")

        for i in available:
            print(f"{i}")
            print("#                                                                                      #")

        print(f"""#                                                                                      #
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
        elif choice.lower() == "w":
            if wslmenu == False : continue
            if not enable_wsl(): return False
            return True
        elif choice.lower() == "d":
            if dockermenu == False : continue
            if not install_docker(): return False
            return True
        elif choice.lower() == "ers":
            if electrsmenu == False : continue
            try: 
                install_electrs()
            except Exception as e: input(e)
            return True
        else:
            invalid()
