# main.py

import os
from module_f import *

def whatsmyip():
    USER = os.getenv('USERNAME')
    print("Calling get_IP_variables()")
    get_IP_variables()  # Call the function to set global variables
    print("Function get_IP_variables() called")

    try:
        print(f"Debug in main: IP = {IP}")
    except NameError as e:
        print(f"Error: {e}")

    input(f"""
########################################################################################

Your computer's IP address is: {IP}

Will {IP} work?""")

# Call the function to demonstrate
whatsmyip()
