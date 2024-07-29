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
    print(f"Debug in module_f: IP = {IP}, IP1 = {IP1}, IP2 = {IP2}, IP3 = {IP3}, IP4 = {IP4}, extIP = {extIP}")

# Test function to ensure it's working standalone
if __name__ == "__main__":
    get_IP_variables()
