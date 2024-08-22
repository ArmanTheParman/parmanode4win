from variables import *
from functions import *
from electrs.install_electrs_f import *
from config_f import *

def menu_electrs():

    IP = get_IP_variables()
    move_to_start = "\033[G"
    move_to_column_41 = "\033[41G"

    while True:

        if torrc_file.exists():
            onion = tor_directory / "electrs-service" / "hostname"
            with open(onion, 'r') as file:
                onionADDR = file.readline().strip()

        toroutput = f"""{bright_blue}         {onionADDR}:70004:t
{yellow} {move_to_start}{move_to_column_41}(Tor from any computer in the world){orange}"""

        if _iselectrsrunning() == True:
            output1=f"""                                Electrs is{green} RUNNING{orange}"""
            iselectrsrunning = True
        else:
            iselectrsrunning = False
            output1=f"""                                Electrs is{red} NOT running{orange}""" 

        set_terminal()
        print(f"""{orange}
########################################################################################{cyan}
                                  Electrs Menu{orange}                   
########################################################################################


{output1}


 CONNECT:{cyan}    127.0.0.1:50005:t         {yellow} (From this computer only){orange}
         {cyan}    127.0.0.1:50006:s         {yellow} (From this computer only){orange} 
         {cyan}    {IP["IP"]}:50006:s          {yellow} {move_to_start}{move_to_column_41}(From any home network computer){orange}

{toroutput}

        {green}
            (start){orange}    Start electrs 
        {red}
            (stop){orange}     Stop electrs
        {blue}
            (restart){orange}  Restart electrs 
        {blue}
            (ec){orange}       View and edit the electrs config file
        {blue}
            (log){orange}      View electrs log
        


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
           if iselectrsrunning == True: continue
           else:
               start_electrs()
        elif choice.lower() == "stop":
           set_terminal()
           stop_electrs()
           continue 
        elif choice.lower() == "restart":
           set_terminal()
           restart_electrs()
           continue 
        elif choice.lower() == "ec":
           file = HOME / ".electrs" / "config.toml"
           os.system(f"notepad {str(file)}")
        elif choice.lower() == "log":
           subprocess.run(f"start cmd /C tail -f {str(HOME / ".electrs" / "run_electrs.log")}", shell=True)
        else:
           invalid()


def _iselectrsrunning():
    try: 
        output = subprocess.run(["docker", "exec", "electrs", "ps"], capture_output=True, check=True, text=True).stdout.splitlines()
        for i in output:
            if "electrs" in i:
                return True
        return False
    except Exception as e:
        return False