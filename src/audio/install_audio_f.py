from variables import *
from functions import *
import subprocess

def install_audio():

    try: subprocess.run(["pip", "install", "pygame"], check=True)
    except Exception as e: input(e)
    success("Audio for Parmanode has been installed")
