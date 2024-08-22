from variables import *
from config_f import *
from functions import *
from tor.install_tor_f import *


# Delete after a while - added with electrum tor option made available
if ico.grep("tor-end"):
    initialise_torrc()