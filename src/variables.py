from pathlib import Path
from win32com.client import Dispatch #for shortcut creation on install
from classes import config

########################################################################################
#parmanode_variables
########################################################################################

global version 
version = "0.0.1"

from datetime import datetime
global date
date=datetime.now().date().strftime("%y-%m-%d")

#directory related variables 
global HOME, pp, dp, bitcoinpath, p4w
HOME=Path.home()
pp = HOME / "parman_programs"     
dp = pp / "parmanode_config"
bitcoinpath = pp / "bitcoin"
p4w = pp / "parmanode4win" 

#file related variables
global tmp, pc, ic, rp_counter, motd_counter, pco, ico, dbo, db, before, after, difference, lockfile, tmpo, beforeo, aftero, differenceo 

tmp = dp / "for_copying-can_delete.tmp"
pc = dp / "parmanode.conf"
ic = dp / "installed.conf"
db = dp / "debug.log"
rp_counter = dp / "rp_counter.conf"
motd_counter = dp / "motd_counter.conf"
before = dp / "before.log"
after = dp / "after.log"
difference = dp/ "difference.log"
lockfile = dp / "lockfile"

pco = config(pc) #parmanode conf object
ico = config(ic) #installed conf object
dbo = config(db) #debug log object
tmpo = config(tmp) #temp config object - not config, but useful methods
beforeo = config(before)
aftero = config(after)
differenceo = config(difference)

from colorama import Fore, Style, init #init need to toggle autoreset on/off
global black, red, green, yellow, blue, magenta, cyan, white, reset

#if colour resets after print statment, enable this: 
#init(autoreset=True)

# Basic colors
black = Fore.BLACK
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
magenta = Fore.MAGENTA
cyan = Fore.CYAN
white = Fore.WHITE
reset = Style.RESET_ALL

global orange, pink, bright_black, grey, bright_red, bright_green, bright_yellow, bright_blue, bright_magenta, bright_cyan, bright_white
# Additional colors
orange = '\033[1m\033[38;2;255;145;0m'  # Manual for colors not in colorama
pink = '\033[38;2;255;0;255m'
bright_black = '\033[90m'
grey = Fore.LIGHTBLACK_EX
bright_red = Fore.LIGHTRED_EX
bright_green = Fore.LIGHTGREEN_EX
bright_yellow = Fore.LIGHTYELLOW_EX
bright_blue = Fore.LIGHTBLUE_EX
bright_magenta = Fore.LIGHTMAGENTA_EX
bright_cyan = Fore.LIGHTCYAN_EX
bright_white = Fore.LIGHTWHITE_EX

global blinkon, blinkoff

# Blink effects
blinkon = '\033[5m'
blinkoff = Style.RESET_ALL


global drive_bitcoin, default_bitcoin_data_dir, bitcoin_dir, bitcoinversion

bitcoinversion="26.1"

drive_bitcoin = None

# Default Windows Bitcoin data directory
default_bitcoin_data_dir = Path.home() / "AppData" / "Roaming" / "Bitcoin"

# get Bitcoin data dir variable
if pc.exists() and pco.grep("bitcoin_dir") == True:
    bitcoin_dir = pco.grep("bitcoin_dir=", returnline=True).split('=')[0].strip()
    bitcoin_dir = Path(bitcoin_dir)
else:
    bitcoin_dir = None

