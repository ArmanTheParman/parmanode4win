from installation_f import *
from functions import *
import subprocess

username = "YourUsername"
password = "YourPassword"

# Run the command to update the service to use your user account
subprocess.run([
    "sc", "config", "Tor Win32 Service",
    "obj=", username,
    "password=", password
], check=True)