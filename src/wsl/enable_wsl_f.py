import subprocess, os

def enable_wsl():
    #Ensure that virtualization is enabled in your BIOS/UEFI settings. This is required for WSL 2.

    subprocess.run(["wsl", "--install"], check=True)
    #after that, check if any distro installed.  May not have, but may have. If none, install debian.
    #new username and password is prompted for.
    #new session in linun entered. type 'exit' to get out.
    #wsl --list, lists distros, and also docker
    #Look vor version2 of wsl. If not, instruct user to manually enable virualisation and give a website.
    input("Install wsl done. Reboot needed.")
    subprocess.run(["wsl", "--install", "-d", "debian"], check=True)
    input("install debian done. Hit <enter>")
    subprocess.run(["wsl", "--set-default-version", "2"], check=True)
    input("Default set. Hit <enter>")



def install_docker():
    pass
    """
    WSL needs to be installed first
    choco install docker-desktop -y
    #restart computer to set path correctly
    docker bin files:
         c:\Program files\Docker\Docker\resources\bin
    docker desktop file:
         c:\Program files\Docker\Docker\"docker desktop.exe"
    """

    

def _unregister_all_wsl_distributions():
    try:
        result = subprocess.run(['wsl', '--list', '--quiet'], capture_output=True, text=True, check=True)
        distros = result.stdout.splitlines()

        for distro in distros:
            print(f"{red}Unregistering distros...{orange}")
            subprocess.run(['wsl', '--unregister', distro], check=True)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


def disable_wsl():
    _unregister_all_wsl_distributions()
    try:
        subprocess.run(["powershell", "-Command", "Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux"], check=True)
        subprocess.run(["powershell", "-Command", "Disable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform"], check=True)
    except Exception as e: input(e)
