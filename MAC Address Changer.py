import subprocess
import optparse
import re


# interface = input("interface > ")
# new_mac = input("new MAC > ")
def get_argument():
    parser = optparse.OptionParser() #everything that starts with capital latter in python is a cloass

    parser.add_option("-i","--inetrface",dest="interface",help="Interface to change its MAC")
    parser.add_option("-m","--mac",dest="new_mac",help="new MAC address")
    (option, argument)= parser.parse_args()
    if not option.interface:
        parser.error("[-] Please specify an interface. Use --help for more details")
    elif not option.new_mac:
        parser.error("[-] Please specify a MAC address. Use --help for more details")
    return option


# NOT SECURE
# subprocess.call("ifconfig "+interface+" down",shell=True)
# subprocess.call("ifconfig "+interface+" hw ether "+new_mac,shell=True)
# subprocess.call("ifconfig "+interface+" up",shell=True)

def change_mac(interface, new_mac):
    print("[+] Changing MAC Address for "+interface+" to "+new_mac)
    # SECURE
    subprocess.call(["ifconfig", interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])


def get_current_mac(interface):
    ifconfig_result=subprocess.check_output(["ifconfig",interface])
    mac_search_result=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)

    if mac_search_result:
        return mac_search_result.group(0)
    else:
        print("[-] Couldn't read the MAC address")



#captures the value of interface and new_mac as arguments
option= get_argument()
current_mac = get_current_mac(option.interface)
print("Current MAC = "+str(current_mac))

change_mac(option.interface,option.new_mac)

current_mac = get_current_mac(option.interface)
if current_mac == option.new_mac:
    print("[+] MAC Address was successfully changed to "+ current_mac)
else:
    print("[-] MAC Address did not change")








