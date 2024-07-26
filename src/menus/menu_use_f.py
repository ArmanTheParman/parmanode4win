def menu_use():

    while True:

        if ico.grep("bitcoin-end"): 
            use_bitcoin = f"#                  {green} (b){orange}            Bitcoin Core                                        #"
            bitcoinmenu = True
        else: 
            use_bitcoin ="#                                                                                      #"
            bitcoinmenu = False

        print(f"""
########################################################################################
#                                                                                      #
#    P A R M A N O D E --> Main Menu -->{cyan} Use Programs Menu {orange}                            #
#                                                                                      #
########################################################################################
#                                                                                      #
#                                                                                      #
{use_bitcoin}
#                                                                                      #
#                                                                                      #
########################################################################################
""")
        choice = choose("xpmq")
        if choice in {"q", "Q", "Quit", "exit", "EXIT"}: 
            quit()
        elif choice in {"p", "P"}:
            return True
        elif choice in {"m", "M"}:
            return True
        elif choice.lower() in {"b", "bitcoin"}:
            if bitcoinmenu == False: continue
            if not use_bitcoin(): return False
            return True
        else:
            invalid()