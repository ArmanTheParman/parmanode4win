import subprocess, os
from functions import *
from variables import *
from config_f import *

def make_electrs_config(db_dir=None):

    dot_electrs = HOME / ".electrs"
    dot_electrs.mkdir(exist_ok=True)

    electrs_config_file = dot_electrs / "config.toml"

    try:
        rpcuser = bco.grep("rpcuser=", returnline=True).split('=')[1].strip()
        rpcpassword = bco.grep("rpcpassword=", returnline=True).split('=')[1].strip()
    except Exception as e: 
        input(e)
        return False
     
    config_text=f"""    
daemon_rpc_addr = \"host.docker.internal:8332\"
daemon_p2p_addr = \"host.docker.internal:8333\"
db_dir = \"{db_dir}\"
network = \"bitcoin\"
electrum_rpc_addr = \"0.0.0.0:50005\"
log_filters = \"INFO\" # Options are ERROR, WARN, INFO, DEBUG, TRACE
                       # Changing this will affect parmanode menu output negatively
auth = \"{rpcuser}:{rpcpassword}\""""
    
    with open(electrs_config_file, 'w') as f:
        f.write(config_text)
 