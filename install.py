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

def install_program(source_exe):
    program_dir = os.path.join(os.environ['ProgramFiles'], 'YourProgramName')
    desktop = winshell.desktop()
    shortcut_path = os.path.join(desktop, 'YourProgram.lnk')

    # Create program directory if it doesn't exist
    if not os.path.exists(program_dir):
        os.makedirs(program_dir)

    # Copy the executable to the program directory
    target_exe = os.path.join(program_dir, os.path.basename(source_exe))
    shutil.copyfile(source_exe, target_exe)

    # Create a shortcut on the desktop
    create_shortcut(target_exe, shortcut_path)

    print(f'Installation complete. Shortcut created at {shortcut_path}')

if __name__ == '__main__':
    source_exe = 'path_to_your_executable.exe'
    install_program(source_exe)
