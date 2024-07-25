import os
import shutil
import winshell
from win32com.client import Dispatch

def create_shortcut(target, shortcut_path, icon_path=None):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = target
    if icon_path:
        shortcut.IconLocation = icon_path
    shortcut.save()

def install_program(source_exe:str):
    program_dir = os.path.join(os.environ['ProgramFiles'], 'Parmanode4Win')
    desktop = winshell.desktop()
    shortcut_path = os.path.join(desktop, 'Parmanode4Win.lnk')
    input("zzzz variables set")

    # Create program directory if it doesn't exist
    if not os.path.exists(program_dir):
        os.makedirs(program_dir)
    
    input("zzzz dir created")

    # Copy the executable to the program directory
    target_exe = os.path.join(program_dir, os.path.basename(source_exe))
    shutil.copyfile(source_exe, target_exe)

    input("zzzz copy")

    # Create a shortcut on the desktop
    create_shortcut(target_exe, shortcut_path)
    input("zzzz shortcut created")
    print(f'Installation complete. Shortcut created at {shortcut_path}')

# usage
# install_program('path_to_exe')