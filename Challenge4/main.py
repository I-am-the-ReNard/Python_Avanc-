import socket


def main(obj,i):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :
        s.settimeout(0.3)
        s.connect((obj, i)) #connect_ex
        return True
    except :
        return False
     #   return False
    #request = b'CONNECT google.com HTTP/1.1\n\n'
    #s.send(request)
    #print(s.recv(4096).decode())

print("Veuilliez vous entrer le nom ou l'IP d'un serveur ?")
objectif = input()

print("DEMARRAGE DU SCAN")
for i in range (79,11000) :
    if main(objectif, i) :
        print(str(i) +" : Ouvert")
print("FIN DU SCAN")