from  pmodules import *

def menu_tools():
    while True:
        set_terminal()
        print(f"""
########################################################################################
{cyan}
                                   T O O L S
 

{green}          ppp) {black}      Connect to Parman's node over Tor 

{green}          ip) {black}       What's my computer's IP?


{orange}
########################################################################################
""")
        choice = choose ("xpmq")
        set_terminal()

        if choice.upper() in {"Q", "EXIT"}: 
            sys.exit()
        elif choice.upper() == "P":
            return True
        elif choice.upper() == "M":
            return True
        elif choice.lower() == "ppp":
            connect_to_parman()
            return True
        elif choice.lower() == "ip":
            whatsmyip()
            return True
        else:
            invalid()

def connect_to_parman():
    print(f"""
########################################################################################
{cyan}
                            CONNECT TO PARMAN'S NODE
{orange}
    This is for emergency or testing purposes only. What's the point of having a node
    if you're going to connect to someone else's?

    Nevertheless, this option is available to you, just in case. I can't promise
    100% up time, because someitmes shit happens. If for whatever reason, my connection
    details change, it will be renewed in Parmanode when you update Parmanode.

    I promise to not collect any data or spy on your transactions. I can confidently
    make that promise because I don't even know how to do that. Your IP address will
    be unknown because you're connecting over Tor anyway.
    
    You'll have to manually tweak your wallet settings and include the following 
    onion address to connect to my server:
{green}
    ajbiipbqjwzvr2xjgcanugsox3q2aqc36pgecf2hx6th2azvta3bf4ad.onion:700{red}4{green}:t 

{orange}
    You must use the port number after the onion address or you can't connect.

    For Electrum wallet, you must turn on your Tor proxy, and you must add the \":t\"
    part of the the 7002 port. This specifies TCP over Tor. (:s, for SSL won't work.)

    For Sparrow wallet, you must have SSL turned off, and you must have the Tor proxy
    turned on.

########################################################################################
""")
    enter_continue()

def whatsmyip():
    import os
    USER = os.getenv('USERNAME')

    input(f"""
########################################################################################


{black}    Your computer's IP address is:                   {cyan}             {IP} {orange}


{black}    Your computer's \"self\" IP address should be:   {yellow}               127.0.0.1


{black}    For reference, every computer's default self IP address is  {yellow}  127.0.0.1 
{black}                                                            and  {yellow} localhost


{black}    To access this computer from another computer ON THE SAME NETWORK, you can type 
{black}    in the terminal of the other computer:


{blue}    ssh {USER}@{IP}


{black}    Note that ssh needs to be enabled on this system. If it's a Windows machine, you 
{black}    may need to install a program called Putty to use it.


{black}    The EXTERNAL IP for your router 
{black}    (Your Home's IP not just this device):              {red}           {extIP}{orange}



########################################################################################
""")
    enter_continue("q")