from functions import *
from variables import *
from config_f import *

def choose_electrs_drive():
    
    if pco.grep("bitcoin_drive=external") == True:
        if yesorno(f"""Would you like to store the electrs data (50 to 100GB) on the
    external drive together with the bitcoin block data?""", y=["e", "External drive"], n=["i", "Internal drive"]) == True:
            pco.add("electrs_drive=external")
            return "external"
        else:
            pco.add("electrs_drive=internal")
            return "internal"
    else: #internal or custom
        if yesorno(f"""Would you like to store electrs data (50 to 100GB) on the
    external drive or internal drive?""", y=["e", "External drive"], n=["i", "Internal drive"]) == True:
            pco.add("electrs_drive=external")
            return "external"
        else:
            pco.add("electrs_drive=internal")
            

def electrs_db_exists():
    if not electrs_dir.exists(): return True

    choice = announce(f"""Parmanode has detected that an electrs database directory already
    exists. What would you like to do?
    

{cyan}                    u){green}    use it
                    
{cyan}                    d){red}    delete contents and start fresh
                    
{cyan}                    a){bright_blue}    abort!  {orange} """)
    
    if choice.lower() == "q": sys.exit()
    if choice.lower() == "p": return False
    if choice.lower() == "a": return False
    if choice.lower() == "u": return True
    if choice.lower() == "d": 
        try: delete_directory(electrs_dir) ; electrs_dir.mkdir() ; return True
        except Exception as e: input(e) ; return True



########################################################################################   
# Can't get docker to mount the Windows drive yet, so abandoning option to
# use an external drive for now
########################################################################################
#     drive_choice = choose_electrs_drive()
#     pco.remove(f"electrs_dir=")

#     if drive_choice == "external" and pco.grep("bitcoin_drive=external"): 
#         electrs_dir=Path("p:/electrs_db")
#         pco.add(f"electrs_dir={electrs_dir}")  
#         if electrs_db_exists == False: return False
#         electrs_dir.mkdir(exist_ok=True)


#     if drive_choice == "external" and not pco.grep("bitcoin_drive=external"):
#         while True:
#             pco.remove("format_disk") #clear first
#             pco.remove("electrs_dir") #clear first
#             if yesorno(f"""Do you want to format a Parmanode drive or use an existing one?""", y=["f", "format a drive"], n=["e", "use existing"]) == True:
#                 pco.add("format_disk=True")
#                 break
#                 #Path(electrs_dir="p:/electrs_db") - added in format function
#             else:
#                 drive_letter = announce("""Please connect the drive letter you wish to use and
#         then type in the drive letter - eg 'P'""")
#                 if drive_letter.isalpha() and len(drive_letter) == 1:
#                     pass
#                 else:
#                     announce("Please try again")
#                     continue
#                 electrs_dir=Path(f"{drive_letter}:/electrs_db")
#                 if electrs_db_exists() == False: return False
#                 try: 
#                     electrs_dir.mkdir(exist_ok=True)
#                     pco.add("format_disk=False")
#                     pco.add(f"electrs_dir={electrs_dir}")  
#                     break
#                 except:
#                     announce("Unable to create the directory on this drive. Try again.")
#                     continue


#     if drive_choice == "internal":

#         electrs_dir = Path(HOME / "electrs_db")
#         if electrs_db_exists() == False: return False
#         try: 
#             electrs_dir.mkdir(exist_ok=True)
#             pco.remove(f"electrs_dir=")
#             pco.add(f"electrs_dir={electrs_dir}")  
#         except Exception as e: input(e) ; return False

# ########################################################################################
#     pco.remove("disk_number")

#     if pco.grep("format_disk=True"):
#         if not detect_drive(): input("detect drive failed") ; return False

#         disk_number = pco.grep("disk_number", returnline=True)
#         try: disk_number = disk_number.split('=')[1].strip()
#         except Exception as e: input(e)

#         #input("before format") 
#         if not format_disk(disk_number, program="electrs"):
#             thedate = date.today().strftime("%d-%m-%y")
#             dbo.add(f"{thedate}: Bitcoin format_disk exited.")
#             input("format failed")
#             return False 
    
# ########################################################################################
#     pco.remove("disk_number")
#     pco.remove("format_disk")
########################################################################################