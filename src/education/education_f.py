from pmodules import *
import subprocess

def menu_education():
    while True:
        set_terminal()
        print(f""" 
########################################################################################
 
{cyan}
                                  E D U C A T I O N
{black}
                    
{yellow}                 (mit){black}      2018 MIT Lecture Series (With Tagde Dryja)

{yellow}                 (w){black}        How to connect your wallet to the node

{yellow}                 (mm) {black}      Bitcoin Mentorship Info

{yellow}                 (n)     {black}   Six reasons to run a node

{yellow}                 (s)       {black} Separation of money and state

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
            pass
        elif choice.lower() == "n":
            pass
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