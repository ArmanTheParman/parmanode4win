from variables import *
from functions import *
from config_f import *

def menu_tor():
   
    while True:
        tortext = subprocess.run(["Get-Service", "-Name", "tor"], text=True, capture_output=True, check=True).stdout.strip()
        tmpo.write(tortext)
        running = tmpo.grep("tor", returnline=True)
        if "Running" in running:
            runningmenu = f"Tor is{green} running{orange}"
        else:
            runningmenu = f"Tor is{red} not running{orange}"


        set_terminal()
        print(f"""{orange}
########################################################################################{cyan}
                                   Tor Menu{orange}                   
########################################################################################


                              {runningmenu}

{green}
                    (start){orange}    Start Tor
                {red}
                    (stop){orange}     Stop Tor

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
            if isbitcoinrunning == True: continue
            else:
                start_bitcoind()
        elif choice.lower() == "stop":
            set_terminal()
            announce(f"""Use your mouse to stop Bitcoin from its window.""")
            continue 
        elif choice.lower() == "bc":
            thedir = get_bitcoin_dir()
            os.system(f"notepad {thedir}/bitcoin.conf")
        else:
            invalid()


 