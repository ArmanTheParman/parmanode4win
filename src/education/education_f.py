from pmodules import *

def menu_education():
    while True:
        print(f""" 
########################################################################################
 
{cyan}
                            P A R M A N O D E - Education
{black}
                    
{yellow}                    (mit){black}      2018 MIT Lecture Series (With Tagde Dryja)

{yellow}                    (w){black}        How to connect your wallet to the node

{yellow}                    (mm) {black}      Bitcoin Mentorship Info

{yellow}                    (n)     {black}   Six reasons to run a node

{yellow}                    (s)       {black} Separation of money and state


            .... more soon


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
        print(f""" 
########################################################################################
{cyan}
                           MIT Lecture Series 2018
{black}
    This is a great lecture series for improving your understanding of how Bitcoin
    works - not for the beginner. It wasn't until I watched this that I felt I truly
    understood many concepts, including Segwit.

    The link to the website is:
   {green} 
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
                os.system('cp', f"{filefrom}", f"{fileto}")
                enter_continue(f"The file has been copied to your desktop")
            except:
                announce("Something went wrong, sorry.")
            
        else:
            invalid()