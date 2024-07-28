from pmodules import *
import time

def uninstall_sparrow():

    global sparrowpath
    sparrowpath = pp / "sparrow"
    sparrow_config_dir = HOME / "Appdata" / "Roaming" / "Sparrow"

    if not yesorno("Are you sure you want to uninstall Sparrow?"): return False

    set_terminal()
    time.sleep(2)
    if yesorno(f"""{orange}Do you also want to delete the directory that contains your 
    {cyan}wallets{orange} and {cyan}configuration{orange} files?"""):
        try: delete_directory(sparrow_config_dir) ; ico.remove("sparrow-end")   
        except: announce("Unable to delete config directory for some reason. Continuing.")

    try:
        if not delete_directory_contents(str(sparrowpath)):
            announce(fr"""Unable to emtpy {cyan} C:\....\parman_programs\sparrow{orange} during uninstallation.
        The directory may be in use, eg it might be open in a folder window, or in a 
        terminal, or it could be because you have another instance of Parmanode open. 
        Aborting.""")                 
            return False
        else:
            ico.remove("sparrow-")
            
    except Exception as e:
        announce(fr"""Unable to emtpy {cyan} C:\....\parman_programs\sparrow{orange} during uninstallation.
        The directory may be in use, eg it might be open in a folder window, or in a 
        terminal, or it could be because you have another instance of Parmanode open. 
        Aborting.
        {e}                    """)                 
        return False 
    
    success("Sparrow has been uninstalled")