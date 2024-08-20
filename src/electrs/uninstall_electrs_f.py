import subprocess, os
from functions import *
from variables import *
from config_f import *

def uninstall_electrs():

    if not yesorno("Are you sure you want to uninstall electrs?"): return False

    if dosubprocess("docker ps") == False:
        announce(f"""Please make sure Docker is running and try again. Aborting.""")
        return False

    try: subprocess.run(["docker", "stop", "electrs"], check=True)
    except: pass

    try: subprocess.run(["docker", "rm", "electrs"], check=True)
    except: pass

    delete_directory(str(HOME / '.electrs'))

    if yesorno(f"If you want to clean up space, you can delete the electrs database.") == True:
        try: delete_directory(str(HOME / 'electrs_db'))
        except: pass
    
    pco.remove("electrs")
    ico.remove("electrs-start")
    ico.remove("electrs-end")
    success("Electrs has been uninstalled")




