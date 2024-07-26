from pmodules import *
from dependencies.chocolatey_f import *
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

    from colorama import Fore
    red = Fore.RED
    green = Fore.GREEN
    cyan = Fore.CYAN
    orange = '\033[1m\033[38;2;255;145;0m'

    if yesorno(f"""
{cyan}                             P A R M A N O D E 4 W I N {orange}

{red}
    If you choose to proceed, the following will happen...

{green}
    1){orange} The{cyan} Parmanode4Win{orange} script files (written open source code) will be
    downloaded to your computer.
{green}    
    2){orange} An executable file which was created ('compiled') by that code will be moved 
    to the 'Program files' folder.
{green}
    3){orange} A shorcut to the program file will be left on your Desktop.
{green}               
    4){orange} Some dependencies will be installed, these are programs Parmanode4Win needs to
    function properly.
           

{cyan}              - chocolatey{orange} (application package manager for Windows, it's great)
{cyan}              - curl {orange} 
{cyan}              - git {orange} 
{cyan}              - gpg {orange}""", h=42): 
        return True
    else:
        return False
