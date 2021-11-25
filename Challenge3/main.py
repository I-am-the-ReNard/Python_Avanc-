from scapy.all import ARP,srp,Ether
import scapy.all as scapy

###MÉTHODE : Idéntification de la MAC de l'IP envoyé###
def mac(ip):
    ans,_ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip),timeout=1, verbose=0)
    if ans:
        return ans[0][1].src
    else:
        return False

###PROGRAMME###
ip = scapy.get_if_addr(scapy.conf.iface)    #On obtient notre IP
print(ip)

print(scapy.get_working_if().description)   #On cherche le type d'interface de réseau

ip = ip.split(".")  #Pour chercher les autres machines de notre réseau, on va efacer le dernier numéro de notre IP
ip = f"{ip[0]}.{ip[1]}.{ip[2]}."

print("DEMARRAGE DU SCAN")  #Avec une boucle, on trouvera toutes les adresses MAC
k=1
for i in range(1,254) :
    out = mac(ip+str(i))    #Appelle à la méthode qui trouve les MAC par IP
    if out != False :
        print("MAC Adress "+str(k)+" : "+out)   #On affiche en console le résultat
        k+=1
print("FIN DU SCAN")
