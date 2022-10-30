from async_timeout import timeout
from scapy.all import * 
import sys, time

def getMAC(ip): #Ether has 3 fields, 2 of those are dst and src, which contain the MAC addr of destination and source
    arp_packet = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip)
    answered, _ = srp(arp_packet, timeout=2, retry=5) #sends packets and recieves answers on layer 2. returns answered and unanswered
    print(f'Getting MAC address for {ip}')
    # print(f'sources address is {answered[Ether].dst}')
    answered[0].show()
    for rcv in answered:
        if rcv[Ether].src != None:
            return rcv[Ether].src #return source MAC addresses

def main(target_IP:str, host_IP:str):
    print(f'Target IP = {target_IP}, host IP = {host_IP}')
    victim = getMAC(target_IP)
    print(f'Mac of victim device is: {victim}')
    host = getMAC(host_IP)
    print(f'Mac of host device is: {host}')



if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f'Missing arguments, need 2 but got {len(sys.argv)-1}')
    else:
        main(sys.argv[1], sys.argv[2])