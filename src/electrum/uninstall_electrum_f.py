from variables import *
from functions import *
from config_f import *
import time

def uninstall_electrum():

    global electrumpath
    electrumpath = pp / "electrum"
    electrum_config_dir = HOME / "Appdata" / "Roaming" / "electrum"

    if not yesorno("Are you sure you want to uninstall Electrum?"): return False

    set_terminal()
    time.sleep(2)
    if yesorno(f"""{orange}Do you also want to delete the directory that contains your 
    {cyan}wallets{orange} and {cyan}configuration{orange} files?"""):
        try: delete_directory(electrum_config_dir) ; ico.remove("electrum-end")   
        except: announce("Unable to delete config directory for some reason. Continuing.")

    try:
        if not delete_directory(str(electrumpath)):
            announce(fr"""Unable to emtpy {cyan} C:\....\parman_programs\electrum{orange} during uninstallation.
        The directory may be in use, eg it might be open in a folder window, or in a 
        terminal, or it could be because you have another instance of Parmanode open. 
        Aborting.""")                 
            return False
        else:
            ico.remove("electrum-")
            
    except Exception as e:
        announce(fr"""Unable to emtpy {cyan} C:\....\parman_programs\electrum{orange} during uninstallation.
        The directory may be in use, eg it might be open in a folder window, or in a 
        terminal, or it could be because you have another instance of Parmanode open. 
        Aborting.
        {e}                    """)                 
        return False 
    
    success("Electrum has been uninstalled")