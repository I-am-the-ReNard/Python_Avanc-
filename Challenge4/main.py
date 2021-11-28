import socket

###MÉTHODE : Détecte si un port est ouvert###
def portsDetecter (ip,i) :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3) #Limite de temps pour établir une connexion
    return s.connect_ex((ip,i)) #On essaie de se connecter au port : si le port est ouvert la fonction retournera 0

###PROGRAMME###
print("Veuillez entrer le nom ou l'IP d'un serveur : ")    #Demande de l'IP à scanner
ip = input()

print("\nDEMARRAGE DU SCAN...")
for i in range (1,11000) :  #Boucle pour analyser les ports entre 0 et 11000
    if not portsDetecter(ip,i) :    #Appelle à la fonction qui essaiera se connecter au port i de l'IP ip
        print(str(i) +" : Ouvert")  #Si elle a réussi à se connecter, on affichera le port
print("FIN DU SCAN")
