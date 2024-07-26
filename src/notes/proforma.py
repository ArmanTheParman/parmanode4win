
def proforma(choice): 
    """Just a template"""
    choice = choose()
    set_terminal()

    if choice.upper() in {"Q", "EXIT"}: 
        quit()
    elif choice.upper() == "P":
        return True
    elif choice.upper() == "M":
        menu_main()
    else:
        invalid()