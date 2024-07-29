# main.py

import os
from module_f import *

def whatsmyip():
    USER = os.getenv('USERNAME')
    print("Calling get_IP_variables...")
    get_IP_variables()  # Call the function to set global variables
    print("Called get_IP_variables.")

    try:
        print(f"Accessing global variables after function call: IP = {IP}")
    except NameError as e:
        print(f"Error: {e}")

    input(f"""
########################################################################################

Your computer's IP address is: {IP}

Will {IP} work?""")

# Call the function to demonstrate
whatsmyip()
