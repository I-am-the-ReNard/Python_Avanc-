from scapy.all import ARP,srp,Ether,get_if_addr,get_working_if

###MÉTHODE : Identification de l'adresse MAC de l'IP envoyée###
def mac(ip):
    ans,_ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip),timeout=1, verbose=0)
    if ans:
        return ans[0][1].src
    else:
        return False

###PROGRAMME###
ip = get_if_addr(scapy.conf.iface)    #On obtient l'IP de notre interface
print(ip)

print(get_working_if().description)   #On obtient le type d'interface réseau

ip = ip.split(".")  #Pour chercher les autres machines de notre réseau on va effacer le dernier octet de notre adresse IP
ip = f"{ip[0]}.{ip[1]}.{ip[2]}."

print("DEMARRAGE DU SCAN")  #Avec une boucle, on trouvera toutes les adresses MAC des adresses IP trouvées
k=1
for i in range(1,254) :
    out = mac(ip+str(i))    #On appelle la méthode qui trouve l'adresse MAC pour chaque IP
    if out != False :
        print("MAC Adresse "+str(k)+" : "+out)   #On affiche en console le résultat
        k+=1
print("FIN DU SCAN")
