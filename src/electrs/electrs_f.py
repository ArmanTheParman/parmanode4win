import subprocess, os
from functions import *
from variables import *
from config_f import *
from parmanode.sned_sats_f import *

def install_electrs():

    sned_sats()
    
    #Build from dockerfile
    p4w_electrs = p4w / "src" / "electrs"
    subprocess.run(f"docker build -t electrs {p4w_electrs}/ ", shell=True)
    
    
def uninstall_electrs():
    pass