
def proforma(choice): 
    """Just a template"""
    choice = choose("xxxxxxxx")
    set_terminal()

    if choice.upper() in {"Q", "EXIT"}: 
        sys.exit()
    elif choice.upper() == "P":
        return True
    elif choice.upper() == "M":
        menu_main()
    else:
        invalid()