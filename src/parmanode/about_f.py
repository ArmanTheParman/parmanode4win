from variables import *
from functions import enter_continue, set_terminal

def about_parmanode():
    
    set_terminal(h=46, w=110)
    print(f"""{orange}
##############################################################################################################
                                
{cyan}                                          About Parmanode4Win {orange}
            
        Version:              {black}   {version}          {orange}

        Websites: {black}               www.parmanode.com {orange}
                     {black}            github.com/armantheparman/parmanode4win{orange}
{orange}
        Developer:  {black}             Arman The Parman{orange}
{orange}
        Contact:           {black}      Email:    armantheparman@protonmail.com{orange}
                              {black}   Nostr:    pub1ltt9gry09lf2z6396rvzmk2a8wkh3yx5xhgkjzzg5znh62yr53rs0hk97y{orange}
  {black}                               Twitter:  @parman_the{orange}
         {black}                        Telegram: @parman_the{orange}
{orange}
        Telegram group{orange}
        chat/help:   {black}            https://t.me/parmanode{orange}
        {orange}
        gpg Public key{orange}
        fetch:              {black}     gpg --keyserver keyserver.ubuntu.com --recv-key E7C061D4C5E5BC98{orange}
                                {orange}
{orange}
        Donations:         {black}      Website:  armantheparman.com/donations{orange}
                  {black}               Nostr:    pub1ltt9gry09lf2z6396rvzmk2a8wkh3yx5xhgkjzzg5znh62yr53rs0hk97y{orange}
                         {black}        Lightning address:  dandysack84@walletofsatoshi.com{orange}
{orange}
        Licence:               {black}  MIT (Free open source){orange}
{orange}
        Conditions of use:       {red}Only one rule - users who own shitcoins (\"alt\"coins), {orange}
  {red}                               aka \"shitcoiners\", are not permitted to use this {orange}
     {red}                            software.{orange}

##############################################################################################################
""")
    enter_continue()