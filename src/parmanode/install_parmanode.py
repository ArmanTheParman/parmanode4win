from config.variables_f import *
from tools.screen_f import *
from bitcoin.uninstall_bitcoin_f import *
import os
import shutil
import winshell
from win32com.client import Dispatch

# usage - install_program('path_to_exe', 'icon_path')

def create_shortcut(target, shortcut_path, icon_path=None):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = target
    if icon_path:
        shortcut.IconLocation = icon_path
    shortcut.save()

def install_program(source_exe:str, icon_path=None):
    program_dir = os.path.join(os.environ['ProgramFiles'], 'Parmanode4Win')
    desktop = winshell.desktop()
    shortcut_path = os.path.join(desktop, 'Parmanode4Win.lnk')

    if not os.path.exists(program_dir):
        os.makedirs(program_dir)
    
    # Copy the executable to the program directory
    target_exe = os.path.join(program_dir, os.path.basename(source_exe))
    shutil.copyfile(source_exe, target_exe)

    # Create a shortcut on the desktop
    create_shortcut(target_exe, shortcut_path, icon_path)
    input("zzzz shortcut created")
    print(f'Installation complete. Shortcut created at {shortcut_path}')

########################################################################################

def install_parmanode():

    if yesorno(f"""This will install the {cyan}Parmanode{orange} executable to the Program
    files directory, and create a shortcut on your Desktop."""): 
        pass
    else:
        return False

    exe = HOME / "parmanode4win" / "run_parmanode.exe"
    icon = pp / "parmanode4win" / "src" / "parmanode" / "pn_icon.png"
    install_program(exe, icon)
    success(f"Parmanode has been installed")