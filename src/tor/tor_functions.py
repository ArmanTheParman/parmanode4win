from variables import *
from functions import *
from config_f import *
def start_tor():
    try:
        subprocess.run(["Start-Service", "-Name", "tor"], check=True)
        return True
    except Exception as e:
        input(e)

def stop_tor():
    try:
        subprocess.run(["Stop-Service", "-Name", "tor"], check=True)
        return True
    except Exception as e:
        input(e)