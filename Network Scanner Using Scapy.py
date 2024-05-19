import scapy.all as scapy
#import optparse -> Deprecated
import argparse


# make sure the code is in the same network as the range that you want to scan
# def scan(ip):
#     scapy.arping(ip)

# scan("10.3.5.8/24") # provide the IP range/network that we want to scan

def get_argument():
    #parser = optparse.OptionParser() #everything that starts with capital latter in python is a cloass
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip","--iprange",dest="ip",help="Ip Address or network range to scan")
    option=parser.parse_args()


    # parser.add_option("-ip","--iprange",dest="ip",help="Ip Address or range to scan")
    # (option, argument)= parser.parse_args()
    if not option.ip:
        parser.error("[-] Please specify an IP Range. Use --help for more details")
    
    return option


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
    #print("IP\t\t\tMAC Address\n--------------------------")
    clients_list =[]

    for element in answered_list:
        client_dict= {"ip":element[1].psrc, "mac":element[1].hwsrc}
        clients_list.append(client_dict)
        #print(element[1].psrc+"\t\t\t"+element[1].hwsrc) # prints the receiver IP from 2nd part of the answered_list
        #print(element[1].hwsrc) #prints the MAC address of the receiver
        print("-------------------------------------------------")
    return clients_list

def print_result(result_list):
    print("IP\t\t\tMAC Address\n--------------------------")
    for client in result_list:
        print(client["ip"]+"\t\t\t"+client["mac"])

Scan_ip = get_argument()

scan_result=scan(Scan_ip.ip)
print_result(scan_result)
