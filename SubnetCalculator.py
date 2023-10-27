import sys

def make_ip_num(IP_Str):
    IP_Address_StringList = IP_Str.split('.')
    IP_Integer = 0
    for i in IP_Address_StringList:
        IP_Integer = (IP_Integer << 8 ) + int(i)
    return IP_Integer

def calculate(IP_Str, CIDR):
    hostBits = 32 - CIDR
    integer_returned = make_ip_num(IP_Str)
    networkID = (integer_returned  >> hostBits) << hostBits
    firstHost = networkID + 1
    subnet2 = CIDR * '0' + hostBits * '1'
    subnet2 = int(subnet2, 2)
    broadcast = integer_returned | subnet2
    lastHost = broadcast - 1
    return (integer_returned, networkID, firstHost, lastHost, broadcast)

def make_ip_str(ip_num):
    octets = [0, 0, 0, 0]
    ip_binary = format(ip_num, '032b')
    for i in range(4):
        octets[i] = str(int(ip_binary[i*8:i*8+8], 2))
    ip_str = '.'.join(octets)
    return ip_str

def pretty_print(subnet_tuple):
    label_tuple = ("IP Address:", "Network ID:", "First Host:", "Last Host:", "Broadcast:")
    for i in range(len(subnet_tuple)):
        print(label_tuple[i], make_ip_str(subnet_tuple[i]))
    return None

if __name__ == "__main__":
    if len(sys.argv) == 3:
        print("Usage: python subnet_calculator.py <IP_Str> <CIDR>")
    IP_Str = sys.argv[1]
    CIDR = int(sys.argv[2])
    results = calculate(IP_Str, CIDR)
    pretty_print(results)
