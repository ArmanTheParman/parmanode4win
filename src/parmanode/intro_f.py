########################################################################################
#intro()
#dirty_shitcoiner()
#suggestupdate()
#instructions()
########################################################################################
from pmodules import *
import time, sys
def intro():

    #later; hide messages option
    set_terminal(h=46)
    if pco.grep("hide_intro"):
        return True

    while True:
        print(f"""{orange}
              
########################################################################################

        {cyan}               P  A  R  M  A  N  O  D  E{red}  4  W  I  N  {orange}

########################################################################################

{black}        
    Welcome to{green} PARMANODE4WIN {black}, an easy AF way to install and run Bitcoin on your 
    Windows desktop computer. Parmanode is Free Open Source Software {pink}(FOSS){black}.

{cyan}
    REQUIREMENTS: {black}

            1) This version is for{green} Windows{black}, tested on version 10 and above.
            
            2) An external OR internal drive (1 Tb SSD recommended)

            3) Users must not hold ANY shitcoins! (honesty system)

            4) Also, another requirement is that you promise to evenually {red} 
               stop using Windows{black} for Bitcoin tasks, and migrate to 
               Parmanode 4 Linux. Even Mac is better, I'll allow it, but it's 
               not great. C'mon, you're a Bitcoiner.

{cyan}
    TO REPORT BUGS:
 {black}                  - armantheparman@protonmail.com

                   - Telegram chat: https:/t.me/parmanode

{orange}
########################################################################################

    Hit{cyan} <enter>{orange} to continue, or{cyan} (q){orange} to quit, then <enter>.

    If you hold{red} shitcoins{orange}, please hit{cyan} (s){orange} - be honest!

    To hide this screen next time, type{pink} \"Free Ross\"{orange} then <enter>.
""")
        choice = input()

        if choice in {'s', 'S'}:
            dirty_shitcoiner() 
            set_terminal()
            return True
        elif choice in {'q', 'Q'}:
            sys.exit()
        elif choice in {'Free Ross', 'free ross'}:
            pco.add("hide_intro=True")
            set_terminal()
            return True
        elif choice == "":
            return True
        else:
            set_terminal()
            continue

def dirty_shitcoiner():
    set_terminal()
    while True: 
        set_terminal()
        print(f"""
########################################################################################
########################################################################################
{red}
             Shame on you.{orange} We're on the battle field, fighting tyranny, and
             you're using vital weapons to shoot ducks. Don't be a traitor to 
             your descendents and humanity. Stack bitcoin and help end tyranny.
		     
             Here's some reading material to help you understand...


     1) Why Bitcoin Only           {cyan}
                                    - http://www.armantheparman.com/why-bitcoin-only  {orange}
     2) Why money tends towards one {cyan}
                                    - http://www.armantheparman.com/onemoney {orange}

     3) We are separating money and state - Join us {cyan}
                                    -  http://www.armantheparman.com/joinus {orange}
     4) Debunking Bitcoin FUD {cyan}
                                    - http://www.armantheparman.com/fud {orange}

    
     Have a nice day.
    {green}
     To abort, type: (I'm sorry), then hit <enter>                 
{orange}
########################################################################################
######################################################################################## 
""") 
        repent = input()
        if "I'm sorry" in repent: 
            break 
        else:   
            set_terminal()
            print("Please wait patiently for computer to destroy itself, mwahaha!")
            time.sleep(3)
            input("Or, hit <enter> to have another go.") 
            set_terminal()
            continue 

    set_terminal()
    return True


def suggestupdate():

    set_terminal()
    print(f"""
########################################################################################

    Parmanode has detected there is a newer version of itself. You could get that
    and replace the current executable you're using. All the installed programs and
    configuration won't be affected, jut the Parmanode wizard itself.
    
    Type{pink} 'Free Ross'{orange} to never be reminded of updates again. 

    Otherwise, just hit{green} <enter>{orange} to continue.

########################################################################################
""")
    choice = choose("xeq")
    if choice in {'free ross', 'Free Ross'}:
        pco.add("update_reminders_off=True")#tested at the start of check_updates()
    elif choice == "q": quit()
    return True


def instructions():
    if pco.grep("hide_instructions"):
        return True

    set_terminal()
    print(f"""
########################################################################################

                               {cyan}     INSTRUCTIONS{black}


{yellow}    1.{black} Use the KEYBOARD to make choices and <enter> to confirm. Your mouse is 
       no good here.

{yellow}    2.{black} Add individual programs from the{green} \"add\"{black} menu. You don't need to install them 
       all.

{yellow}    3.{black} Each program has its{green} own menu{black} nested under the \"use\" menu; various 
       functions are available for you to make it easier to interact with the program.
       
{yellow}    4.{black} Explore all the options from the main menu, there are hidden gems.

{yellow}    5.{black} You should reguarly{green} update{black} Parmanode (the best way is from the Parmanode
       menu). 
{orange}

########################################################################################


{black}
    To hide this message next time, type in{pink} \"Free Ross\"{black} then{cyan} <enter>{black}.

    To continue on, just hit{cyan} <enter>{black}.{orange}
""")
    choice = input()
    if choice in {'free ross' , "Free Ross"}:   
        pco.add("hide_instructions=True")
        return True
    elif choice in {"q", "Q", "quit"}:
        sys.exit()
    else:
        return True
