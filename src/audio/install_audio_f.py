from variables import *
from functions import *
from config_f import *
import subprocess

def install_audio():

    try: subprocess.run(["pip", "install", "pygame"], check=True)
    except Exception as e: input(e)
    ico.add("audio-end")
    success("Audio for Parmanode has been installed")

def uninstall_audio():

    try: subprocess.run(["pip", "uninstall", "pgame"], check=True)
    except Exception as e: input(e)
    ico.remove("audio-")
    success("Audio for Parmanode has been uninstalled")

