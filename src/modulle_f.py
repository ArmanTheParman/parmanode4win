# module_f.py

def get_internal_IP():
    # Dummy implementation for example purposes
    return "192.168.1.100"

def get_IP_variables():
    global IP, IP1, IP2, IP3, IP4, extIP
    IP = get_internal_IP()
    IP1 = IP.split(r'.')[0]
    IP2 = IP.split(r'.')[1]
    IP3 = IP.split(r'.')[2]
    IP4 = IP.split(r'.')[3]
    extIP = "External IP Placeholder"  # Assuming extIP is also required
    print(f"Inside get_IP_variables: IP = {IP}, IP1 = {IP1}, IP2 = {IP2}, IP3 = {IP3}, IP4 = {IP4}, extIP = {extIP}")
