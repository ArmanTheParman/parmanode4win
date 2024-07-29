# module_f.py

def get_internal_IP():
    return "192.168.1.100"

def get_IP_variables():
    global IP, IP1, IP2, IP3, IP4, extIP
    IP = get_internal_IP()
    IP1 = IP.split('.')[0]
    IP2 = IP.split('.')[1]
    IP3 = IP.split('.')[2]
    IP4 = IP.split('.')[3]
    extIP = "External IP Placeholder"
    print(f"Debug in module_f: IP = {IP}, IP1 = {IP1}, IP2 = {IP2}, IP3 = {IP3}, IP4 = {IP4}, extIP = {extIP}")
