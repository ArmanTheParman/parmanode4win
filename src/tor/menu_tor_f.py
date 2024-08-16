from variables import *
from functions import *
from config_f import *
from tor.tor_functions import *
def menu_tor():
    while True:
        tortext = subprocess.run(["powershell", "Get-Service -Name tor"], text=True, capture_output=True, check=True).stdout.strip()
        tortext = tortext.splitlines()
        for line in tortext:
            if "tor" in line:
                if "Running" in line:
                    runningmenu = f"Tor is{green} running{orange}"
                    torrunning = True
                    flag = 1
                    break
                else:
                    runningmenu = f"Tor is{red} not running{orange}"
                    torrunning = False
                    flag = 2
                    break
        
        if flag is not 1: 
            runningmenu = f"Tor is{red} not running{orange}"
            torrunning = False

        tmpo.write("")


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
            if torrunning == True: continue
            else:
                start_tor()
        elif choice.lower() == "stop":
            if torrunning == False: continue
            else:
                stop_tor()
        else:
            invalid()


 