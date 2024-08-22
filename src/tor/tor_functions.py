from variables import *
from functions import *
from config_f import *
def start_tor():
    try:
        subprocess.run(["powershell", "Start-Service -Name tor"], check=True)
        return True
    except Exception as e:
        input(e)

def stop_tor():
    try:
        subprocess.run(["powershell", "Stop-Service -Name tor"], check=True)
        return True
    except Exception as e:
        input(e)

def restart_tor():
    stop_tor()
    start_tor()