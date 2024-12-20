from variables import *
from functions import *
from config_f import *
from mempool.install_mempool_f import *
def menu_mempool():

    IP = get_IP_variables()
    move_to_start = "\033[G"
    move_to_column_41 = "\033[41G"

    while True:
        
        backend = get_mempool_backend()

        if torrc_file.exists():
            onion = tor_services / "mempool-service" / "hostname"
            with open(onion, 'r') as file:
                onionADDR = file.readline().strip()

        toroutput = f"""{bright_blue}         {onionADDR}:8280:t
{yellow} {move_to_start}{move_to_column_41}(Tor from any computer in the world){orange}"""

        if _ismempoolrunning() == True:
            output1=f"""                                Mempool is{green} RUNNING{orange}"""
            ismempoolrunning = True
        else:
            ismempoolrunning = False
            output1=f"""                                Mempool is{red} NOT running{orange}""" 

        set_terminal()
        print(f"""{orange}
########################################################################################{cyan}
                                  Mempool Menu{orange}                   
########################################################################################


{output1}


 CONNECT:{cyan}    http://127.0.0.1:8180     {yellow} (From this computer only){orange}
         {cyan}    http://{IP["IP"]}:50006:s {yellow} {move_to_start}{move_to_column_41}(From any home network computer){orange}
{toroutput}

        {green}
            (start){orange}    Start Mempool
        {red}
            (stop){orange}     Stop Mempool
        {blue}
            (restart){orange}  Restart Mempool
        {blue}
            (ec){orange}       View and edit the Mempool config file
        {blue}    
            (bk){orange}       Change backend. Current: {green}{backend}{orange}
        

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
           if ismempoolrunning == True: continue
           else:
               start_mempool()
        elif choice.lower() == "stop":
           set_terminal()
           stop_mempool()
           continue 
        elif choice.lower() == "restart":
           set_terminal()
           restart_mempool()
           continue 
        elif choice.lower() == "ec":
           file = pp / "mempool" / "docker" / "docker-compose.yml"
           os.system(f"notepad {str(file)}")
        elif choice.lower() == "bk":
            if backend == "BITCOIN CORE":
                change_mempool_backend("electrum")
            else:
                change_mempool_backend("none")
            announce("Please restart mempool for the change to take effect")
        else:
           invalid()


def _ismempoolrunning():
    try: 
        if subprocess.run("docker ps | grep frontend", shell=True, capture_output=True, check=True, text=True).returncode == 0:
           if subprocess.run("docker ps | grep backend", shell=True, capture_output=True, check=True, text=True).returncode == 0:
               if subprocess.run("docker ps | grep mariadb", shell=True, capture_output=True, check=True, text=True).returncode == 0:
                    return True
    except:
        return False
            

def get_mempool_backend():
    
    fileo = config(mempool_yml)
    text = fileo.grep("MEMPOOL_BACKEND", returnline=True)
    tmpo.truncate()
    tmpo.add(text)
    if tmpo.grep("none"): return "BITCOIN CORE"
    if tmpo.grep("electrum"): return "ELECTRUM SERVER"

def change_mempool_backend(backend):
    try: os.system(f"cp {mempool_yml} {mempool_yml}.backup")
    except Exception as e: input(e)

    with open(mempool_yml, 'r') as file:
        data = file.readlines()

    with open(mempool_yml, 'w') as file:
        for i in data:
            if "MEMPOOL_BACKEND" in i:
                file.write(f"      MEMPOOL_BACKEND: \"{backend}\""+ '\n')
            else:
                file.write(i)


    