import hashlib

###MÉTHODE : Cherche le mdp###
def breakPass (motPass) :
    with open(r"mots.txt","r") as fp :    #On ouvre le document avec les possibles mdp
        #md5
        for line in fp :
            if motPass == hashlib.md5(line[:-1].encode("UTF-8")).hexdigest() :  #Le mdp == le mot de la ligne "i", encrypté en md5 ?
                return line[:-1]    #Si le mdp est trouvé, on le retourne et on finit la boucle

        #sha256
        fp.seek(0)  #On retourne au début du document txt
        for line in fp :
            if motPass == hashlib.sha256(line[:-1].encode("UTF-8")).hexdigest() :
                return line[:-1]

        #sha512
        fp.seek(0)
        for line in fp :
            if motPass == hashlib.sha512(line[:-1].encode("UTF-8")).hexdigest() :
                return line[:-1]

        return ""   #Si on n'a pas trouvé le mot de passe, on e


###PROGRAME###

print("Veuilliez écriver un mot de pas faible : ")  #Définition du mdp
motPass = input()

print("Selectionnez une méthode d'encryptation : \n\t1) md5\n\t2) sha256\n\t3) sha512") #Définition de la méthode d'encryptation
sel = input()
if sel == 3 :
    motPass = hashlib.sha512(motPass.encode("UTF-8")).hexdigest()   #md5
elif sel == 2 :
    motPass = hashlib.sha256(motPass.encode("UTF-8")).hexdigest()   #sha256
else :    #Par défaut
    motPass = hashlib.md5(motPass.encode("UTF-8")).hexdigest()   #sha512


mp = breakPass(motPass) #On appelle la fonction qui essayera d'obtenir le mdp

if mp == "" :   #Résultats
    print("Le mot de pas n'est pas trouvé")
else :
    print("Le mot de pass est : "+mp)