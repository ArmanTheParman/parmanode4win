from variables import *
from functions import *
from bitcoin.uninstall_bitcoin_f import *
from pathlib import Path
import os, sys

def delete_parmanode4win_script_directory():

    path = pp / "parmanode4win" 

    def handle_remove_readonly(func, path):
        os.chmod(path, 0o777)
        func(path)

    def delete_directory_contents(directory):
        for item in directory.iterdir():
            try:
                if item.is_dir():
                    delete_directory_contents(item)
                    item.rmdir()
                else:
                    item.chmod(0o777)  # Change the file to writable before deleting
                    item.unlink()
            except Exception as e:
                handle_remove_readonly(lambda p: path.rmdir(), path)
    
    if path.exists() and path.is_dir():
        delete_directory_contents(path)
        try:
            path.rmdir()
        except Exception as e:
            handle_remove_readonly(path.rmdir, path)
    else:
        print(f"{path} directory does not exist")



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
        #delete desktop icon
        desktop = Path(get_desktop_path())
        shortcut = desktop / "Parmanode4Win.lnk" 
        if shortcut.exists():
            try: shortcut.unlink()
            except: pass
        if yesorno("Also delete the parmanode4win script directory?"):
            delete_parmanode4win_script_directory()

    success(f"Parmanode has been uninstalled. {red}Happy now?{orange}")

    sys.exit()