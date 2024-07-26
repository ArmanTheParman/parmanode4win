from pmodules import *
from menus.menu_add_f import menu_add
from menus.menu_use_f import menu_use
from menus.menu_remove_f import menu_remove
from bitcoin.menu_bitcoin_f import *
from parmanode.uninstall_parmanode import *

def menu_main():
    import config.variables_f 
    while True:
        set_terminal(45, 88)
        print(f"""{orange}        
########################################################################################
#                                                                                      #
#    P A R M A N O D E --> {bright_blue}Main Menu{orange}                                                   #
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
        elif choice.lower() == "d":
            sned_sats()
        elif choice.lower() == "update":
            update_parmanode()
        elif choice.lower() == "uninstall":
            uninstall_parmanode()
        elif choice.lower() == "ap":
            about_parmanode()
        elif choice.lower() in {"q", "quit", "exit"}:
            quit()
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

def menu_education():
    set_terminal()
    print(f"""
########################################################################################
{cyan}
    Coming soon
{orange}
########################################################################################
""")
    enter_continue()

def menu_tools():
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

def about_parmanode():
    set_terminal()
    print(f"""
########################################################################################
{cyan}
    Coming soon
{orange}
########################################################################################
""")
    enter_continue()

def mentorship():
    set_terminal(h=45)
    print(f"""
########################################################################################
{cyan}
                           Mentorship with Parman{orange}


    Need help with Bitcoin security, self-custody, and inheritance?

    Bitcoin self-sovereignty, while maintaining high security, safety, and privacy.

    Few people will take the time to build their technical skills. It can be daunting.
    It is crucial to get your coins off the exchange (safely!), as the bare minimum,
    but progressing beyond that is also important.

    This is a one-to-one mentorship course (not a group/class), at your own pace,
    involving multiple video call meetings - it could take weeks, or if you want to
    take your time, months.

    The program includes …

            Bitcoin knowledge (understanding private keys, blockchain, mining etc)
            Running a node
            Using a hardware wallet
            Verifying Bitcoin software using gpg (public/private key cryptography
                    verification and hashes)
            Making a watching-only wallet
            Making an air-gapped computer
            Safe key generation
            Safe key storage
            Multisignature wallet generation
            How to hide your coins on the blockchain
{pink}            How to remove KYC tainting of coins {orange}
            UTXO management
            Using the Lightning Network
            Inheritance planning

########################################################################################
""")
    enter_continue()
    set_terminal(h=45)
    print(f"""
########################################################################################
{cyan}
    Reference #1/2:{orange} Identity is hidden for privacy, but available on request, on a
    case-by-case basis.

    Subject: Re: Reference for Parman (BTC mentorship program)

    Hi ZZZZ,

    Thank you for your email. A few months ago I completed my mentorship with Parman.
    I already had a relatively high level of knowledge both in theory and in practice,
    but I had reached the maximum I could learn by myself and I realised that I needed a
    more complete, structural approach with particular focus on privacy and security.

    Parman’s site was by far the best one I ever found, therefore I did not hesitate
    one moment to apply for a mentorship. It turned out to be the money best spent in
    years. Thanks to Parman I learned everything I needed to and more. Parman is an
    absolutely great teacher (being myself a university professor, I know something
    about it): he’s patient, focused on the essential, he manages to make complicated
    things very simple. In addition, he’s an extremely kind person. His in-depth
    technical knowledge about Bitcoin and his privacy/security standards in how to use
    Bitcoin are, I believe, the maximum that you can get on the market. Therefore, my
    answer to your first question is that I was extremely happy with his services.

    The Zoom sessions worked great for me because they were flexible (which was exactly
    what I needed): they lasted the time needed for the topic discussed (no more and
    no less); we fixed the appointments when we were both available. Without this
    flexibility I probably would not have managed to complete the mentorship and
    certainly I would have enjoyed it much less. The membership process lasted
    approximately two months, give or take (more intense at the beginning, spontaneously
    less intense towards the end)…. My level of privacy and security (and therefore my
    confidence) in my use of Bitcoin increased enormously after this mentorship: even
    more than I expected. I warmly recommend him.

    Kind regards,

    YYYY

########################################################################################
""")
    enter_continue()
    set_terminal()
    print(f"""
########################################################################################
{cyan}
    Reference #2/2:{orange} Identity is hidden for privacy, but available on request, on a
    case-by-case basis.

    Subject: Reference for Parman (BTC Mentorship Program)

    Hi ZZZZ,

    Glad to answer your questions regarding our experience with Parman. We had a
    unique situation that Parman helped navigate us through. He was very patient and
    kind as he helped us secure our bitcoin and he gave us sound advice on how to
    proceed with our situation. The Zoom sessions were easy, no problems. I can’t
    really answer your questions on how long the mentorship program took as our
    situation was unique, although we are going to send our son through his
    mentorship program this summer. Parman was very careful with our private
    information, often reminding us not to reveal too much.

    All that being said, I can wholeheartedly recommend Parman’s mentorship program.
    He is a rare man of intellect and integrity. He is also very patient and
    understanding. We had a great experience and learned quite a bit.

    Hope this helps, if I can answer any more questions, let me know.

    Kind regards,

    WWWW

########################################################################################
""")
    enter_continue()