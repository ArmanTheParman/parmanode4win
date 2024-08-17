from variables import *
from functions import *
from config_f import *
from parmanode.sned_sats_f import *
from menus.menu_add_f import menu_add
from menus.menu_use_f import menu_use
from menus.menu_remove_f import menu_remove
from bitcoin.menu_bitcoin_f import *
from bitcoin.install_bitcoin_f import *
from parmanode.uninstall_parmanode_f import *
from parmanode.about_f import *
from tools.menu_tools_f import *
from education.education_f import *
from parmanode.mentorship_f import *
import asyncio

def menu_main():
    # try: await check_docker_installed()
    # except Exception as e: input(e)
    while True:
        set_terminal(46, 88)
        print(f"""{orange}        
########################################################################################
#                                                                                      #
#    P A R M A N O D E {red}4 W I N{orange} --> {bright_blue}Main Menu{orange}                                           #
#                                                                                      #
#    Version: {bright_blue} {version_text}{orange}                                                                   #
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
        print(f"""

{blinkon}{red}                      WARNING!! YOU DON'T HAVE ENOUGH BITCOIN {orange}{blinkoff}""")
        choice = input()  
        set_terminal()
        if choice.lower() in {"a", "add"}:
            menu_add() 
        elif choice.lower() in {"use", "u"}: 
            menu_use()
        elif choice.lower() in {"b", "bitcoin"}:
            if ico.grep("bitcoin-end"):
                menu_bitcoin()
            elif ico.grep("bitcoin-start"):
                announce(f"""Parmanode has detected a faulty installation of Bitcoin. You can 
    decide to remove it or not in the next screen.""")
                uninstall_bitcoin()
                continue
            # else:
            #     install_bitcoin()
            #     continue
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
