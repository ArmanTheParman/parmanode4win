from functions import *
import subprocess

def check_chocolatey():
    if subprocess.run(["choco", "--version"], stdout=subprocess.DEVNULL, check=True):
        return True
    else: 
        return False
def install_chocolatey():
    try:
        command = (
            r'Set-ExecutionPolicy Bypass -Scope Process -Force; '
            r'[System.Net.ServicePointManager]::SecurityProtocol = '
            r'[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; '
            r'iex ((New-Object System.Net.WebClient).DownloadString("https://chocolatey.org/install.ps1"))'
        )
        if subprocess.run(["powershell", "-Command", command], check=True):
            print("Chocolatey installed successfully.")

    except subprocess.CalledProcessError as e:
        return False

    return True


def check_python_version():
    try:
        python_version = subprocess.run("python --version", check=True, text=True, capture_output=True).stdout
        return python_version
    except Exception as e:
        input(e)
        return False
    
def check_python():
    try:
        python_version = check_python_version()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

    if python_version == False: return False  

    else:
        if python_version > "3.12.0":
            return True
        else:
            return False

def install_python_with_chocolatey():
    try:
        subprocess.run(["choco", "install", "python", "-y"], check=True)
        print("Python installed successfully.")
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to install Python with Chocolatey: {e.stderr}")

    return True

def check_pip():
    try:
        subprocess.run(["pip", "--version"], check=True, stdout=subprocess.DEVNULL) 
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
def check_tor():
    try:
        subprocess.run(["tor", "--version"], check=True, stdout=subprocess.DEVNULL) 
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_pip_with_python():

    if not check_python(): return False

    try:
        subprocess.run(["python", "get-pip.py"], check=True)
        print("PIP installed successfully.")
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to install pip with Python: {e.stderr}")

    return True

#def python_dependencies():
def check_pip_dependencies(answer=False):
    try:
        listofpackages = subprocess.run(["pip", "list"], check=True, capture_output=True, text=True).stdout.split()
    except Exception as e:
        raise Exception(f"{e}")

    if answer == True:
       if {"colorama", "psutil", "pywin32", "requests", "urllib3", "setuptools", "winshell"}.issubset(set(listofpackages)):
           text = f"{green}All pip dependencies installed{orange}"
           return [text, True]
       else:
           text = f"{red}Some pip dependencies failed to install{orange}"
           return [text, False]

    for i in {"colorama", "psutil", "pywin32", "requests", "urllib3", "setuptools", "winshell"}:
        if i not in listofpackages:
            try: subprocess.run(["pip", "install", f"{i}"], check=True)
            except Exception as e:
                raise Exception(f"{e}")
def check_git():
    try:
        subprocess.run(["git", "--version"], check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_git_with_chocolatey():
    try:
        subprocess.run(["choco", "install", "git", "-y"], check=True)
        print("git installed successfully.")
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to install git with Chocolatey: {e.stderr}")

    return True

def check_curl():
    try:
        subprocess.run(["curl", "--version"], check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_curl_with_chocolatey():
    try:
        subprocess.run(["choco", "install", "curl", "-y"], check=True)
        print("curl installed successfully.")
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to install curl with Chocolatey: {e.stderr}")

    return True

def check_gpg():
    try:
        subprocess.run(["gpg", "--version"], check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
    
def install_gpg_with_chocolatey():

    try:
        subprocess.run(["choco", "install", "gpg4win", "--force", "-y"], check=True)
        print("""gpg installed successfully.""")
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to install gpg with Chocolatey: {e.stderr}")

    return True

def dependency_check():

    try:
        # Check if Chocolatey is installed
        if not check_chocolatey():
            install_chocolatey()

        # Check if git is installed
        if not check_git():
            install_git_with_chocolatey()

        if not check_curl():
            install_curl_with_chocolatey()

        # Check if gpg is installed
        if not check_gpg():
            install_gpg_with_chocolatey()

        # Check if python is installed
        if not check_python():
            install_python_with_chocolatey()

        # Check if pip is installed
        if not check_pip():
            install_pip_with_python()

        # Check if tor is installed
        if not check_tor():
            from tor.install_tor_f import install_tor
            install_tor(no_config=True) #parameter added to make function resiliant, so it doesn't need config to exist
        
        # Check and install a list of pip progrmams
        try: check_pip_dependencies()
        except Exception as e:
            raise Exception(f"{e}")

        return True
        
    except Exception as e:
        print(f"An error occurred: {e}")



def test_installation():

    def ending():
        print(f"""{orange}
########################################################################################""")
        enter_continue("Hit <enter> to exit")
        sys.exit()

    while True:
        set_terminal()
        print(f"""
########################################################################################{green}

    Checking installation....
{orange}
########################################################################################

    {orange}
    """)
        python_version = check_python_version().strip()
        print(f"{green}Version of {python_version}{orange}")
        
        if check_pip() == True: 
            print(f"{green}pip is installed")
        else:
            print(f"{red}pip is not installed") 
            ending()

        if check_tor() == True: 
            print(f"{green}tor is installed")
        else:
            print(f"{red}tor is not installed") 
            ending()

        if check_chocolatey() == True: 
            print(f"{green}chocolatey is installed")
        else:
            print(f"{red}chocolatey is not installed") 
            ending()
        if check_git() == True: 
            print(f"{green}git is installed")
        else:
            print(f"{red}git is not installed") 
            ending()

        if check_curl() == True: 
            print(f"{green}curl is installed")
        else:
            print(f"{red}curl is not installed") 
            ending()

        if check_gpg() == True: 
            print(f"{green}gpg is installed")
        else:
            print(f"{red}gpg is not installed") 
            ending()

        text = check_pip_dependencies(answer=True)
        print(text[0])
        if text[1] == False:
            ending()

        else:
            success("The test for installing dependencies passed.")
            break