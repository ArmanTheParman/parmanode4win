from variables import *
from functions import *
from electrs.install_electrs_f import *
from config_f import *

def menu_electrs():

    while True:
       if _iselectrsrunning() == True:
           output1=f"""                                Electrs is{green} RUNNING{orange}"""
       else:
           output1=f"""                                Electrs is{red} NOT running{orange}""" 

       set_terminal()
       print(f"""{orange}
########################################################################################{cyan}
                                  Electrs Menu{orange}                   
########################################################################################


{output1}

        {green}
            (start){orange}    Start electrs 
        {red}
            (stop){orange}     Stop electrs
        {blue}
            (restart){orange}  Restart electrs 
        {blue}
            (ec){orange}       View and edit the electrs config file


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
       elif choice.lower() == "ec":
           file = HOME / ".electrs" / "config.toml"
           os.system(f"notepad {str(file)}")
       else:
           invalid()







# {orange}
#       (n)        Access Bitcoin node information ....................(bitcoin-cli)

#       (bc)       Inspect and edit bitcoin.conf file 

#       (up)       Set, remove, or change RPC user/pass
# {bright_blue}
#       (tor){orange}      Tor menu options for Bitcoin...

#       (mm)       Migrate/Revert an external drive...

#       (delete)   Delete blockchain data and start over (eg if data corrupted)

#       (update)   Update Bitcoin wizard
# {output3}
#       (o)        OTHER...


# ########################################################################################
# "


def _iselectrsrunning():
    try: 
        output = subprocess.run(["docker", "exec", "electrs", "ps"], capture_output=True, check=True, text=True).stdout.splitlines()
        for i in output:
            if "electrs" in i:
                return True
        return False
    except Exception as e:
        input(e)
        return False