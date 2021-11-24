import socket

from scapy.all import ARP,srp,Ether
import scapy.all as scapy


def mac(ip):
    ans,_ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip),timeout=1, verbose=0)
    if ans:
        return ans[0][1].src
    else:
        return False

interf = None
ip = scapy.get_if_addr(scapy.conf.iface)
print(ip)

print(scapy.get_working_if().description)

ip = ip.split(".")
ip = f"{ip[0]}.{ip[1]}.{ip[2]}."

print("DEMARRAGE DU SCAN")
k=1
for i in range(1,254) :
    out = mac(ip+str(i))
    if out != False :
        print("MAC Adress "+str(k)+" : "+out)
        k+=1
print("FIN DU SCAN")