from async_timeout import timeout
from scapy.all import *
import sys, time


def getMAC(ip): #Ether has 3 fields, 2 of those are dst and src, which contain the MAC addr of destination and source
    print(f'Getting MAC address for {ip} on interface {conf.iface}: ', end="")
    arp_packet = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip)#The sequence of 'F' is a reserved broadcast address
    ans = None
    counter = 0
    while ans == None and counter < 10:
        ans = srp1(arp_packet, verbose=False)#sends packets and recieves answers on layer 2. returns answered and unanswered
        counter += 1
        
    if ans == None:
        print("Failed to get response")
        return None
    else:
        print(ans[Ether].src)
        return ans[Ether].src

def spoof_target(target_IP, target_MAC, spoof_ipv4):
    packet = ARP


def main(target_IP:str, host_IP:str):
    print(f'Target IP = {target_IP}, host IP = {host_IP}\n')
    victim = getMAC(target_IP)
    host = getMAC(host_IP)

    # # victim.show()
    # host = getMAC(host_IP)
    # print(f'Mac of host device is: {host}')

if __name__ == '__main__':
    conf.iface = "eth0"
    if len(sys.argv) < 3:
        print(f'Missing arguments, need 2 but got {len(sys.argv)-1}')
    elif sys.argv[1] == sys.argv[2]:
        print("Cannot target two identical IPv4 addresses")
    else:
        main(sys.argv[1], sys.argv[2])
