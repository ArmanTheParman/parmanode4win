from pmodules import *
from menus.menu_add_f import menu_add
from menus.menu_use_f import menu_use
from menus.menu_remove_f import menu_remove
from bitcoin.menu_bitcoin_f import *
from parmanode.uninstall_parmanode import *
from parmanode.about import *
from tools.menu_tools_f import *
from education.education_f import *
from parmanode.mentorship_f import *

def menu_main():
    while True:
        set_terminal(45, 88)
        print(f"""{orange}        
########################################################################################
#                                                                                      #
#    P A R M A N O D E {red}4 W I N{orange} --> {bright_blue}Main Menu{orange}                                           #
#                                                                                      #
#    Version: {bright_blue} {version}{orange}                                                                   #
#                                                                                      #
########################################################################################
#                                                                                      #
#{cyan}    (add)    {orange}            Add more Programs                                            #
#                                                                                      #
#{cyan}    (b)  {orange}                Bitcoin menu                                                 #
#                                                                                      #
#{cyan}    (u)            {orange}      Use Programs                                                 #
#                                                                                      #
#{cyan}    (remove)     {orange}        Remove/Uninstall Programs                                    #
#                                                                                      #
#--------------------------------------------------------------------------------------#
#                                                                                      #
#{cyan}    (t)        {orange}          Tools                                                        #
#                                                                                      #
#{cyan}    (s)              {orange}    Settings                                                     #
#                                                                                      #
#{cyan}    (mm){orange}                 Mentorship with Parman - Info                                #
#                                                                                      #
#{cyan}    (i){orange}                  Inhericance planning with Parman                             #
#                                                                                      #
#{cyan}    (e)       {orange}           Education                                                    #
#                                                                                      #
#{cyan}    (d)             {orange}     Donate                                                       #
#                                                                                      #
#{cyan}    (update)  {orange}           Update Parmanode                                             #
#                                                                                      #
#{cyan}    (uninstall)     {orange}     Uninstall Parmanode                                          #
#                                                                                      #
#{cyan}    (ap){orange}                 About Parmanode                                              #
#                                                                                      #
########################################################################################

 Type your{cyan} choice{orange} without the brackets, and hit{green} <enter>{orange} 
 Or to quit, either hit{green} <control>-c{orange}, or type{cyan} q{orange} then{green} <enter>{orange}.
""")
        input("main zzzz")
        print(f"""

{blinkon}{red}                      WARNING!! YOU DON'T HAVE ENOUGH BITCOIN {orange}{blinkoff}""")
        choice = input()  
        set_terminal()
        if choice.lower() in {"a", "add"}:
            menu_add() 
        elif choice.lower() in {"use", "u"}: 
            menu_use()
        elif choice.lower() in {"b", "bitcoin"}:
            menu_bitcoin()
        elif choice.lower() in {"remove"}: 
            menu_remove()
        elif choice.lower() == "t":
            menu_tools()
        elif choice.lower() == "s":
            menu_settings()
        elif choice.lower() == "mm":
            mentorship()
        elif choice.lower() == "e":
            menu_education()
        elif choice.lower() == "i":
            internetbrowser("https://armantheparman.com/parmanvault/")
            announce(f"Browser should have open the page.")
        elif choice.lower() == "d":
            sned_sats()
        elif choice.lower() == "update":
            update_parmanode()
        elif choice.lower() == "uninstall":
            uninstall_parmanode()
        elif choice.lower() == "ap":
            about_parmanode()
        elif choice.lower() in {"q", "quit", "exit"}:
            sys.exit()
        else:
            invalid()

        continue 
        #end of menu loop 

def menu_log_config():
    set_terminal()
    print(f"""
########################################################################################
{cyan}
    Coming soon
{orange}
########################################################################################
""")
    enter_continue()

def menu_settings():
    set_terminal()
    print(f"""
########################################################################################
{cyan}
    Coming soon
{orange}
########################################################################################
""")
    enter_continue()

def sned_sats():
    set_terminal(h=38)
    print(f"""
    
########################################################################################

                         Isn't this awesome? And it's{green} FREE{orange}

             If you love this, please send some of that love to Parman :)
{red}{blinkon}




                                     ,sats.sats,
                                     SSSSSSSSSSS
                                     'YaaaaaaaY'
                                       'YtttY'    
                                         'S'


{blinkoff}
{orange}                 Lightning Address:{cyan} dandysack84@walletofsatoshi.com
{orange}
                 BTCPAY POS:{cyan} https://armantheparman.com/donations/ {orange}

           NOSTR:{cyan} 1ltt9gry09lf2z6396rvzmk2a8wkh3yx5xhgkjzzg5znh62yr53rs0hk97y {orange}



{bright_blue}
       Please join the other Parmanode users on Telegram: https://t.me/parmanode
{orange}
########################################################################################

""")
    enter_continue()

def update_parmanode():
    set_terminal()
    print(f"""
########################################################################################
{cyan}
    Coming soon
{orange}
########################################################################################
""")
    enter_continue()

