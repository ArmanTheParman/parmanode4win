from variables import *
from functions import *
from parmanode.intro_f import *
from parmanode.mentorship_f import *
import subprocess
def menu_education():
    while True:
        set_terminal(h=44)
        print(f""" 
########################################################################################
 
{cyan}
                                  E D U C A T I O N
{black}
                    
{yellow}               (mm) {black}      Bitcoin Mentorship Info

{yellow}               (o) {black}      Not too technical overview of Bitcoin

{yellow}               (wbo) {black}      Why Bitcoin Only

{yellow}               (om) {black}      Why money trends towards only one

{yellow}               (fud) {black}      Debunking Bitcoin FUD

{yellow}               (z) {black}      Parman's ZeroTrust Bitcoin Storage System 

{yellow}               (prv) {black}      Bitcoin private key info

{yellow}               (n)     {black}   Six reasons to run a node 

{yellow}               (s)       {black} Separation of money and state 

{yellow}               (utxo)       {black} What is a Bitcoin UTXO?

{yellow}               (blk)       {black} What's the point of a blockchain?

{yellow}               (mine)       {black} What's the point of mining?

{yellow}               (dec)       {black} What's the point of decentralisation?

{yellow}               (mit){black}      2018 MIT Lecture Series (With Tagde Dryja) - {red}advanced
 
{cyan}
            .... more soon

{orange}
########################################################################################
""")
        choice = choose("xpmq")
        set_terminal()
        if choice.upper() in {"Q", "EXIT"}: 
            sys.exit()
        elif choice.upper() == "P":
            return True
        elif choice.upper() == "M":
            return True
        elif choice.lower() == "mit":
            if not mit_lectures(): return False
            else: continue
        elif choice.lower() == "w":
            pass
        elif choice.lower() == "mm":
            internetbrowser("https://armantheparman.com/mentorship/")
            announce(f"Browser should have opened the page.")
            continue
        elif choice.lower() == "o":
            internetbrowser("https://armantheparman.com/bitcoin-english")
            announce(f"Browser should have opened the page.")
            continue
        elif choice.lower() == "wbo":
            internetbrowser("https://armantheparman.com/why-bitcoin-only/")
            announce(f"Browser should have opened the page.")
            continue
        elif choice.lower() == "om":
            internetbrowser("https://armantheparman.com/onemoney/")
            announce(f"Browser should have opened the page.")
            continue
        elif choice.lower() == "fud":
            internetbrowser("https://armantheparman.com/fud/")
            announce(f"Browser should have opened the page.")
            continue
        elif choice.lower() == "n":
            internetbrowser("https://armantheparman.com/why-should-you-run-your-own-bitcoin-node/")
            announce(f"Browser should have opened the page.")
            continue
        elif choice.lower() == "s":
            internetbrowser("https://armantheparman.com/joinus/")
            announce(f"Browser should have opened the page.")
            continue
        elif choice.lower() == "z":
            internetbrowser("https://armantheparman.com/zerotrust/")
            announce(f"Browser should have opened the page.")
            continue
        elif choice.lower() == "prv":
            internetbrowser("https://armantheparman.com/private-key-info/")
            announce(f"Browser should have opened the page.")
            continue
        elif choice.lower() == "utxo":
            internetbrowser("https://armantheparman.com/utxo/")
            announce(f"Browser should have opened the page.")
            continue
        elif choice.lower() == "blk":
            internetbrowser("https://armantheparman.com/blockchain/")
            announce(f"Browser should have opened the page.")
            continue
        elif choice.lower() == "mine":
            internetbrowser("https://armantheparman.com/mining/")
            announce(f"Browser should have opened the page.")
            continue
        elif choice.lower() == "s":
            pass
        else:
            invalid()

def mit_lectures():
    while True:
        set_terminal()
        print(f""" 
########################################################################################
{cyan}
                           MIT Lecture Series 2018
{black}
    This is a great lecture series for improving your understanding of how Bitcoin
    works - not for the beginner. It wasn't until I watched this that I felt I truly
    understood many concepts, including Segwit.

    The link to the website is (highlight and copy with <control>c):
   {blue} 
    https://ocw.mit.edu/courses/mas-s62-cryptocurrency-engineering-and-design-spring-2018/video_galleries/lecture-videos/
{black}
    One day this might be taken down so I have also included a torrent to my own
    copies which you can download yourself and seed to others using torrent software
    like qbittorrent (can download this with Parmanode).
{green}
                   d)    Copy the torrent to your Desktop
{black}
########################################################################################
""")
        choice = choose("xpmq")
        set_terminal()
        if choice.upper() in {"Q", "EXIT"}: 
            sys.exit()
        elif choice.upper() == "P":
            return True 
        elif choice.upper() == "M":
            return False 
        elif choice.lower() == "d":
            filefrom = p4w / "src" / "education" / "MIT_lectures.torrent"
            desktop = get_desktop_path()
            fileto = Path(desktop)
            try:
                result = subprocess.run(["cp", f"{filefrom}", f"{fileto}/"], check=True, capture_output=True)
                enter_continue(f"The file has been copied to your desktop")
            except Exception as e:
                input(e)
            
        else:
            invalid()
