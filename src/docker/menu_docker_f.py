from variables import *
from functions import *
from config_f import *
from docker.docker_f import *

def menu_docker():

    while True:

        set_terminal()
        print(f"""{orange}
########################################################################################{cyan}
                                  Docker Menu{orange}                   
########################################################################################


{green}
                         (s)   {orange}    Start Docker
                         
{green}
                         (list){orange}    See a list of running containers


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
        elif choice.lower() in {"start", "s"}:
            try: start_dockerdesktop()
            except Exception as e: input(e)
            announce("""Docker will open in a moment. You can close the pop-up and Docker
    will continue to runin the background.""")
        elif choice.lower() in {"l", "list"}:
            set_terminal()
            try: print(dosubprocess("docker ps"))
            except: pass
            enter_continue()
            return True
        else:
            invalid()

