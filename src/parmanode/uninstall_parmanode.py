from pmodules import *
from bitcoin.uninstall_bitcoin_f import *

def uninstall_parmanode():

    if not yesorno(f"""Are you sure you want to uninstall {cyan}Parmanode{orange}? That's insane!

    You will have the option to individually select which applications you want to 
    remove or leave."""):
        return False

    if ico.grep("bitcoin-"):
        uninstall_bitcoin()
    
    if yesorno("One last chance, this will delete the run_parmanode file and configuration files"):
        exe_dir = Path(r"""c:\Program files"\Parmanode4win""")
        delete_directory(exe_dir)
        delete_directory(dp)
        pn_dir = pp / "parmanode"
        delete_directory(pn_dir)
        #delete desktop icon
        desktop = Path(get_desktop_path)
        shortcut = desktop / "Parmanode4Win.lnk" 
        shortcut.unlink()
        if yesorno("Also delete the parmanode4win script directory?"):
            p4w_dir = pp / "parmanode4win"
            delete_directory(p4w_dir)

    success(f"Parmanode has been uninstalled. {red}Happy now?{orange}")

    quit()

        