import scapy.all as scapy # type: ignore


# make sure the code is in the same network as the range that you want to scan
# def scan(ip):
#     scapy.arping(ip)

# scan("10.3.5.8/24") # provide the IP range/network that we want to scan


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    #print(arp_request.summary()) #prints who have the "ip" in the scanning network
    #scapy.ls(scapy.ARP()) #prints the list of fields/parameter present in ARP class
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #set the destination MAC to broadcast MAC
    arp_request_broadcast = broadcast/arp_request
    #arp_request_broadcast.show() - shows the details of the request
    answered_list= scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0] #send and recive packets
    #print(answered.summary()) - shows which clients received the ARP packet and sends their MAC

    #answered_list contains the 2 parts. 1- request, 2 - response(IP and MAC address of the receiver)
    print("IP\t\t\tMAC Address\n--------------------------")
    for element in answered_list:
        print(element[1].psrc+"\t\t\t"+element[1].hwsrc) # prints the receiver IP from 2nd part of the answered_list
        
        #print(element[1].hwsrc) #prints the MAC address of the receiver
        print("-------------------------------------------------")

