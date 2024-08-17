from pathlib import Path
from variables import *
from config_f import *
import winshell
import requests, time, atexit, platform, sys, ctypes, psutil, os
import zipfile, subprocess, os, ctypes, subprocess
from win32com.client import Dispatch

########################################################################################

def get_bitcoin_dir():
    if not pc.exists():
        raise Exception("Parmanode config file does not exist")

    if pc.exists() and pco.grep("bitcoin_dir") == True:
        bitcoin_dir = pco.grep("bitcoin_dir=", returnline=True).split('=')[1].strip()
        bitcoin_dir = Path(bitcoin_dir)
    else:
        bitcoin_dir = None

    return bitcoin_dir
########################################################################################

def cleanup():
    """Will execute when Parmanode quits"""
    print(f"{reset}")

    lockfile.unlink()
    #tmp.unlink() 


def lockfilefunction(once=False):

   if not lockfile.exists():
        with lockfile.open('w') as f:
            pid = os.getpid()
            f.write(str(pid) + '\n')
        atexit.register(cleanup)            ##################### this needs to be exactly here so that lockfile exit doesn't delete the lockfile
        return True
   else:
        try:
            with lockfile.open('r') as f:
                pid = f.readline().strip()
        except Exception as e:
                pid = None
                input(e)
                return True
        if int(pid) == os.getpid():
             return True    

        if int(pid) in psutil.pids():
            os.system('cls') # I think this clears the colours
            print(f"""{orange}

########################################################################################


    Parmanode seems to be running already.

    You shouldn't run a second instance at the same time, bad things can happen.
    {cyan}    
    Override?

{cyan}                            y){orange}      Yeah


{cyan}                            n){orange}      Nah


########################################################################################

    Make a choice then hit{red} <enter>{orange}""")
            choice = input() 
            if choice.lower() == "y": lockfile.unlink() ; return True
            else: sys.exit()
        else:
            lockfile.unlink()
            if once == True: 
                return True
            else:
                lockfilefunction(once=True) # 'once=True' prevents riks of infinite loop

def get_internal_IP(toprint:bool=None):
    try:
        import socket 
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))  
        ip_address = s.getsockname()[0]
        s.close()
        if toprint == True: 
            print(f"The IP addres is: {ip_address}")
            input() 
        return ip_address 
    except Exception as e:
        input(e)

def get_IP_variables():
    IP = get_internal_IP()
    IP1 = IP.split(r'.')[0]
    IP2 = IP.split(r'.')[1]
    IP3 = IP.split(r'.')[2]
    IP4 = IP.split(r'.')[3]
    
    
    try: extIP = subprocess.run(['curl', '-s', 'ifconfig.me'], text=True, capture_output=True, check=True).stdout.strip()
    except: extIP = "N/A"

    return {"IP": f"{IP}", "IP1": f"{IP1}", "IP2": f"{IP2}", "IP3": f"{IP3}", "IP4": f"{IP4}", "extIP": f"{extIP}"}


def searchin(the_string, the_file: Path) -> bool:

    if not the_file.is_file():
        return False 

    with the_file.open() as f:
        contents = f.read()

    return the_string in contents

def addline(the_string, the_file):
    if not isinstance(the_file, Path):
        input(f"the file {the_file} needs to be a Path object")
        return False
    if not the_file.is_file():
        input(f"addline function - file, f{the_file} does not exist")
        return False
    with the_file.open('a') as f:
        f.write(the_string + '\n')

def deleteline(the_string, the_file):
    
    if not isinstance(the_file, Path):
        input(f"the file {the_file} needs to be a Path object")
        return False

    if not the_file.is_file():
        input(f"addline function - file, f{the_file} does not exist")
        return False

    try:
        with the_file.open('r') as f_in, tmp.open('w') as f_out:
            for line in f_in.readlines():
                if the_string not in line:
                    f_out.write(line)
        tmp.replace(the_file)
        return True

    except Exception as e:
        input(f"Exception when doing deleteline - {e}")
        return False

def download(url, dir, silent=False):
    try:
        initial_dir = os.getcwd()
        os.chdir(dir)
        try:
            if silent == False:
               subprocess.run(['curl', '-LO', url], check=True)  # other options: stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
            else:
               subprocess.run(['curl', '-LOs', url], check=True)  # other options: stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            os.chdir(initial_dir)
        except Exception as e:
            announce("download failed")
            os.chdir(initial_dir)
            return False
        os.chdir(initial_dir)
        return True
    except:
        os.chdir(initial_dir)
        return False

def unzip_file(zippath: str, directory_destination: str):
    try:
        with zipfile.ZipFile(zippath, 'r') as z:
            z.extractall(directory_destination) 
        return True
    except:
        return False

def delete_directory_contents(path_given):

    if isinstance(path_given, str):
        try: path = Path(path_given)
        except Exception as e: input(e) ; return False
        print(type(path))

    if isinstance(path_given, Path):
        try: path = Path(path_given)
        except Exception as e: input(e) ; return False


    if isinstance(path, Path): 

        if not path.exists(): return True

        for item in path.iterdir(): 

            if item.is_dir(): 
                delete_directory(item)  # Recursively delete contents of subdirectories
                if item.exists(): 
                    try: item.rmdir()            # Remove the now-empty SUBdirectory
                    except: os.chmod(item, 0o77) ; item.rmdir()

            else:
                if item.exists(): 
                    try: item.unlink()  # Remove the file
                    except: os.chmod(item, 0o77) ; item.unlink()
        return True
    else:
        raise ValueError(f"""unexpect type in delete_directory_contents()""")


def delete_directory(path_given):

    if isinstance(path_given, str):
        try: path = Path(path_given)
        except Exception as e: input(e) ; return False

    if isinstance(path_given, Path): 
        try: path = Path(path_given) 
        except Exception as e: input(e) ; return False

    if not isinstance(path, Path):
        raise Exception ("Error with Path object")

    if path.is_symlink():
        path.unlink()  # Remove symbolic link
        return True

    if not path.exists():
        return True 

    if not path.is_dir():
        raise Exception(f"{path} passed to delete_directory, but it is not a dir, nor symlink") 

    for item in path.iterdir(): #for a non-empty directory

        if item.is_dir(): 
            try: delete_directory(item)  # Recursively delete contents of subdirectories
            except: os.chmod(item, 0o777) ; delete_directory(item)
            if item.exists():
                try: item.rmdir()            # Remove the now-empty SUBdirectory
                except: os.chmod(item, 0o77) ; item.rmdir()

        else:
            if item.exists(): 
                try: item.unlink()  # Remove the file
                except: os.chmod(item, 0o77) ; item.unlink()

    if path.exists(): 
       try: path.rmdir()  # Path directory should be empty now, can delete
       except: os.chmod(path, 0o77) ; path.rmdir()
    
    return True
       

def get_directory_size(directory, units="MB"):

    if isinstance(directory, str):
        directory = Path(directory)

    if isinstance(directory, Path):

        if not directory.exists(): announce(f"""{directory} does not exist.""") ; return False

        try: size_bytes = sum(f.stat().st_size for f in directory.rglob('*') if f.is_file()) 
        except Exception as e: announce(e) ; return False

        if units == "MB": 
            size_bytes_MB = size_bytes / (1024 * 1024) 
            return round(size_bytes_MB, 2) #round to two decimal places, MB

        elif units == "GB": 
            size_bytes_GB = size_bytes / (1024 * 1024 * 2014) 
            return round(size_bytes_GB, 2) #round to two decimal places, MB
        
        elif units =="raw":
            size_bytes_raw = size_bytes 
            return round(size_bytes_raw, 2) #round to two decimal places, MB
    
    return False

def get_directory_items(directory):
    
    if isinstance(directory, str):
        directory = Path(directory)
    
    if not directory.exists(): announce (f"""{directory} does not exist.""") ; return False

    directory_sorted = sorted(directory.iterdir())
    pages = int(len(directory_sorted) / 30 )
    if pages % 1 > 0: pages += 1
    
    set_terminal()
    
    print(f"""
######################################################################################## 

    Contents of {directory}
{cyan}
""")

    count = 0
    for i in range(pages+1):
        if count != 0: #means j loop has gone through at least once
            print(f"""{orange}
########################################################################################

     Page {i + 1}
 {cyan}
 """)
        count = 0
        for j in directory_sorted:
            count +=  1
            min = i * 30 #when i is 0, min is 0, when is 1 min is 30
            max = min + 30
            if count > min and count < max:
                print(f"    {j}")
        if i == pages: break
        print(f""""
    {orange}Hit <enter> for next page{cyan}
              """, pages, "count: ", count, "i is: ", i)
        input()
        set_terminal()

    print(f"""{orange}

########################################################################################
""")
    enter_continue()

def set_terminal_size(rows, cols):

    try:
        # Get handle to standard output
        std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)  # -11 is STD_OUTPUT_HANDLE

        # Define struct for setting console screen buffer size
        class COORD(ctypes.Structure):
            _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

        # Set console screen buffer size
        coords = COORD(cols, rows)
        ctypes.windll.kernel32.SetConsoleScreenBufferSize(std_out_handle, coords)

        # Set console window size
        rect = ctypes.wintypes.SMALL_RECT(0, 0, cols - 1, rows - 1)
        ctypes.windll.kernel32.SetConsoleWindowInfo(std_out_handle, True, ctypes.byref(rect))

    except Exception as e:
        print(f"Error setting terminal size: {e}")

def set_terminal(h=40, w=88):
    os.system('cls')
    set_terminal_size(h, w)
    print(f"{orange}") #Orange colour setting.


def choose(message=None):

    if message == "xpmq":
        print(f"{yellow}Type your{cyan} choice{yellow} from above options, or:{pink} (p){yellow} for previous,{green} (m){yellow} for main,{red} (q){yellow} to quit.")
    if message == "xmpq":
        print(f"{yellow}Type your{cyan} choice{yellow} from above options, or:{pink} (p){yellow} for previous,{green} (m){yellow} for main,{red} (q){yellow} to quit.")
    if message == "xeq":
        print(f"{yellow}Type your{cyan} choice{yellow}, or{green} <enter>{yellow} to continue, or {red}(q){yellow} to quit.")
    if message == "xmq":
        print(f"{yellow}Type your{cyan} choice{yellow} from above options, or:{green} (m){yellow} for main,{red} (q){yellow} to quit.")
    if message == "xq":
        print(f"{yellow}Type your{cyan} choice{yellow} from above options, or:{red} (q){yellow} to quit.")
    if message == "eq":
        print(f"{yellow}Hit {cyan} <enter>{yellow} to continue, or:{red} (q){yellow} to quit.")

    choice = input()
    return choice 

def invalid():
    set_terminal()
    return input(f"""{red}INVALID ENTRY {orange}
                 
Hit {cyan}<enter>{orange} to go back and try again""") 

def please_wait(text=None):
    set_terminal()
    print()
    if text is not None: print(text)
    print(f"{cyan}Please wait...{orange}")
    print()

def announce(text, ec_text=None):
    set_terminal()
    print("""########################################################################################
          """)
    print(f"    {text}")
    print("""
########################################################################################

          """)
    return enter_continue(ec_text)

def enter_continue(text=None):
    if text == None:
       print(f"{yellow}Hit{cyan} <enter>{yellow} to continue...{orange}") 
       return input()
    if text.upper() == "TRY AGAIN":
       print(f"{yellow}Hit{cyan} <enter>{yellow} to try again...{orange}") 
       return input()
    if text.lower() == "q":
       print(f"{yellow}Hit{cyan} <enter>{yellow} to continue...{orange}") 
       thechoice = input()
       if thechoice.lower() == 'q': sys.exit()
       return thechoice
    else:
       print(text)
       return input()

def success(text):
    set_terminal()
    print(f"""
########################################################################################
{cyan}
                                 S U C C E S S ! {orange}

    {text}

########################################################################################
""")
    enter_continue()


def colour_check():
    print(f"{black}black {reset}\"black\"")
    print(f"{red}red {reset}\"red\"")
    print(f"{green}green {reset}\"green\"")
    print(f"{orange}green {reset}\"green\"")
    print(f"{bright_blue}green {reset}\"green\"")
    


def yesorno(message, h=40, Q=False):
    while True:
        set_terminal(h)
        print(f"""{orange}
########################################################################################

    {message}

                

{cyan}                                y){orange}        yeah
                               

{cyan}                                n){orange}        nah    


########################################################################################   
""")
        choice = choose("xq")    
        set_terminal()

        if choice.upper() in {"Q", "EXIT"}: 
            if Q == True: quit()
            invalid()
        elif choice.upper() == "Y":
            return True
        elif choice.upper() == "N":
            return False
        else:
            os.system('cls')
            print(f"""Invalid choice. Hit{cyan} <enter>{orange} first, and then try again.""") 
            input()


def detect_drive():
    
    set_terminal()
    beforeo.truncate() ; aftero.truncate() ; differenceo.truncate()
    input(f"""{orange}    Please make sure the drive you want to use with Parmanode
    is{cyan} DISCONNECTED{orange}. Then hit <enter>.
    
    """)

    get_all_disks("before")

    input(f"""{orange}    Now go ahead and{cyan} CONNECT{orange} The drive, wait a few seconds. Then
    hit <enter>""")
    
    for count in range(5):
        get_all_disks("after")
        try:
            with before.open('r') as bb, after.open('r') as aa:
                bblines = tuple(bb.readlines())
                aalines = tuple(aa.readlines()) 
                unique_lines = [line for line in aalines if line not in bblines]
        except Exception as e:
            print(f"{e}")

        with difference.open('w') as f:
            for line in unique_lines:
                f.write(line)
        if len(unique_lines) > 1: input("Something went wrong with drive detection") ; return False
        if len(unique_lines) == 0:
            set_terminal()
            time.sleep(0.86)
            if count == 4: input("Something went wrong with drive detection") ; return False
            continue
        elif len(unique_lines) == 1:
            break
        else:
            input("Something went wrong with drive detection") ; return False

    try:
        disk_number = unique_lines[0].split()[1]
        pco.add(f"disk_number={disk_number}")
    except Exception as e:
        print(f'{e}')
        input("get disk number failed")
        
    return True

def get_all_disks(when):
    tmpo.truncate()
    diskpart_commands = """list disk"""
    tmpo.add(diskpart_commands)
    diskpart_script_path = tmpo.file
    result = subprocess.run(['diskpart', '/s', diskpart_script_path], capture_output=True, text=True, shell=True).stdout.strip().split('\n')
    
    if when == "before":
        for line in result:
            beforeo.add(line)
    if when == "after":
        for line in result:
            aftero.add(line)

    return True


def format_disk(disk_number, file_system='NTFS', label="parmanode"):
    if disk_number is None:
        return False
    
    # Create the diskpart script
    script = f"""
    select disk {disk_number}
    clean
    create partition primary
    select partition 1
    format fs={file_system} label={label} quick
    """

    # Save the script to a temporary file
    script_path = dp / 'diskpart_script.txt'
    with open(script_path, 'w') as file:
        file.write(script)
    
    # Run the diskpart command with the script
    command = ['diskpart', '/s', script_path]
    
    try:
        # Check for existing drive letters
        existing_drive_letters = get_connected_disks()

        # Find an unused drive letter
        for letter in "PARMANSAYSGFYJKQTUVWXZBCDEHILNO":
            if f"{letter}:" not in existing_drive_letters:
                assign_letter = letter
                break
  
        # Add the assign letter command to the script
        with open(script_path, 'a') as file:
            file.write(f"assign letter={assign_letter}\n")
       
        #make bitcoin directory  
        bitcoin_dir = Path(f"{assign_letter}:\\bitcoin")
        bitcoin_dir.mkdir(parents=True, exist_ok=True)
        bitcoin_dir = str(bitcoin_dir)
        pco.add(f"bitcoin_dir={bitcoin_dir}")

        subprocess.run(command, check=True)
        return True
    except Exception as e:
        print(f"{e}")
        input()
        return False


def get_connected_disks():
    try:
       diskpart_command = "list volume"
       diskpart_script_path = tmpo.file
       tmpo.truncate()
       tmpo.add(diskpart_command)
       result = subprocess.run(['diskpart', '/s', diskpart_script_path], capture_output=True, text=True, check=True)
       existing_drive_letters = {line.split()[0] for line in result.stdout.splitlines() if line and line[0].isalpha() and line[1] == ':'}
       return existing_drive_letters
    except Exception as e:
        print(f"{e}")

def check_drive_is_c():
    import os
    if os.getenv('SystemDrive').upper() == 'C:':
        return True
    else:
        return False

def get_system_drive_letter():
    return os.getenv('SystemDrive') 

def counter(type):
    if type == "rp":
        with rp_counter.open('r') as f:
            rpcount = f.read().strip()
            newcount = int(rpcount) + 1
        with rp_counter.open('w') as f:
            f.write(str(newcount) + '\n')
        return True
    if type == "motd":
        with motd_counter.open('r') as f:
            motdcount = f.read().strip()
            newcount = int(motdcount) + 1
        with motd_counter.open('w') as f:
            f.write(str(newcount) + '\n')


def check_installer_updates(compiled_version):
    url = "https://raw.githubusercontent.com/ArmanTheParman/parmanode4win/main/installer_version"
    params = {'_': int(time.time())}  # Adding a unique timestamp parameter
    try:
        response = requests.get(url, params=params).text.split('.')
        latest_winMajor = int(response[0])
        latest_winMinor = int(response[1])
        latest_winPatch = int(response[2])

        if [latest_winMajor, latest_winMinor, latest_winPatch] > compiled_version:
            return "outdated"
        else:
            return "uptodate"

    except:
        return "error"


    
def check_updates(compiled_version, nah=False):
    if pco.grep("update_reminders_off"):
        return True
    
    if nah == False:
        if pco.grep(f"{date}"): return True #check updates only once a day to save loading time checking url

    pco.remove("last_used=")
    pco.add(f"last_used={date}")
    url = "https://raw.githubusercontent.com/ArmanTheParman/parmanode4win/main/version"

    params = {'_': int(time.time())}  # Adding a unique timestamp parameter
    try:
        response = requests.get(url, params=params).text.split('.')
        latest_winMajor = int(response[0])
        latest_winMinor = int(response[1])
        latest_winPatch = int(response[2])

        if [latest_winMajor, latest_winMinor, latest_winPatch] > compiled_version:
            return "outdated"
        else:
            return "uptodate"

    except Exception as e:
        print(f"error when checking update, {e}")
        return "error"


def os_is():
    """Windows, Darwin, or Linux is returned"""
    return platform.system()


def run_as_admin(command, params=""):
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", command, params, None, 1)
    except Exception as e:
        input(f"Error: {e}")


def is_process_running(process_name):
    # Iterate over all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Check if process name matches
            if process_name.lower() in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False



def get_desktop_path():

    return winshell.desktop()

def git_clone_parmanode4win():
    
    p4w_dir = pp / "parmanode4win"
    delete_directory(p4w_dir)
    os.chdir(pp)

    try:
        subprocess.run(["git", "clone", f"https://github.com/armantheparman/parmanode4win"])
    
    except Exception as e:
        input(e)


def desktop_shortcut():
    source = p4w / "src" / "run_parmanode.py"
    icon_path = str(p4w / "src" / "parmanode" / "pn_icon.ico")
    install_program(source, icon_path)

def install_program(source=None, icon_path=None):
    desktop = Path(winshell.desktop())
    shortcut_path = str(desktop / 'Parmanode4Win.lnk')
    target = str(source)

    # Create a shortcut on the desktop
    create_shortcut(target, shortcut_path, icon_path)
    return True

def create_shortcut(target, shortcut_path, icon_path):
    try:
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortcut(shortcut_path)
        shortcut.TargetPath = target
        if icon_path:
            shortcut.IconLocation = f"{icon_path},0"
        shortcut.save()
    except Exception as e:
        input(e)


def internetbrowser(url):
    try:
        # Attempt to open the URL using webbrowser and suppress output
        subprocess.run(['python', '-m', 'webbrowser', '-t', url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception as e:
        return False

def suggestupdate():

    set_terminal()
    print(f"""
########################################################################################

    Parmanode has detected there is a newer version of itself.

    Have Parmanode update itself now?

{cyan}
                y){orange}             Yeah, this is cool
{cyan}
                n){orange}             Nah, I don't like improvements

    
    Type{pink} 'Free Ross'{orange} to never be reminded of updates again. 

    Otherwise, just hit{green} <enter>{orange} to continue.

########################################################################################
""")
    choice = choose("xeq")
    if choice in {'free ross', 'Free Ross'}:
        pco.add("update_reminders_off=True")#tested at the start of check_updates()
    if choice.lower() == "y":
        update_parmanode()
        return True 
    if choice.lower() == "n":
        return True
    elif choice == "q": quit()
    return True


def update_parmanode():
    try:
        current_dir = os.getcwd()
        os.chdir(p4w)
        os.system('git config pull.rebase false')
        os.system('git config user.name winuser')
        os.system('git config user.email winuser@parmanode.com')
        os.system('git stash')
        os.system('git pull')
        os.chdir(current_dir)
    except:
        announce("Parmanode encountered an error updating itself.")
    finally:
        os.chdir(current_dir)
    success("Parmanode has been updated. Please restart Parmanode for changes to take effect.")

def check_for_emergency(silence):

    if silence == "s": x=True

    url = "https://raw.githubusercontent.com/ArmanTheParman/parmanode4win/main/emergency.py"
    download(url, str(p4w), silent=x)
    target = p4w / "emergency.py" 
    if target.exists():
        try: import emergency
        except: pass
    
def tidy_up_before_starting():

    # Manage Tor installation. Some Parmanodes may have been installed before the installer 
    # installed Tor by default as a dependency. Newer versions won't need this.
    from installation_f import check_tor
    torstatus = check_tor()
    if torstatus == True and ico.grep("tor-end") == False:
        ico.add("tor-end")
    if torstatus == False:
        if yesorno(f"""Parmanode has detected that{bright_blue} Tor {orange}is not installed on your system.

    Tor is needed for enhancing your privacy, and for future Parmanode features. It
    runs in the background and you won't notice it. It'll take a minute to install.
   {green} 
    Allow Parmanode to install Tor for you now? """):
            from tor.install_tor_f import install_tor
            install_tor()
    
    result = subprocess.run(["wsl", "--list", "--quiet"], check=True, capture_output=True, text=True).stdout.strip().splitlines()
    for i in result:
        print(repr(i))
        if "do" in i:
            input("it's true")
        else:
            input("not true")