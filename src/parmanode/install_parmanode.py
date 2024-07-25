from config.variables_f import *
from tools.screen_f import *
from bitcoin.uninstall_bitcoin_f import *

def install_parmanode():

    if yesorno(f"""This will install the {cyan}Parmanode{orange} executable to the Program
    files directory, and create a shortcut on your Desktop."""): 
        pass
    else:
        return False
    
    install_program()