def parite(bits):
    "Fonction qui renvoie la valeur du bit de parité d'un mot binaire donné sousforme d'une lsite de 0 et de 1"
    somme_bits = 0
    for i in range (len(bits)): #calcul de la somme des bits
        somme_bits += bits[i]
        if somme_bits%2 == 0 : #test de la parité de la somme des bits
            return 0
        else :
            return 1



def encode_hamming(donnee):
    "Fonctione qui renvoie un message encodé par le code de hamming de 7 bits a partir d'un argument, nomme donnee, qui est un message de 4 bits sous forme d'une listede 1 et de 0"
    d1,d2,d3,d4 = [donnee[i] for i in range(len(donnee))]
    p1 = parite([d1,d2,d4]) #calcul de parité du triplet 1
    p2 = parite([d1,d3,d4]) #calcul de parité du triplet 2
    p3 = parite([d2,d3,d4]) #calcul de parité du triplet 1
    return [p1,p2,d1,p3,d2,d3,d4]



def decode_hamming(message):
    "Fonction qui renvoie le message décodé et corrigé en cas d'erreur detectée par la technique de hamming. On suppose que si il y a une erreur elle est unique"
    m1,m2,m3,m4,m5,m6,m7 = [message[i] for i in range (len(message))]
    c1 = parite([m4,m5,m6,m7])
    c2 = parite([m2,m3,m6,m7])
    c3 = parite([m1,m3,m5,m7])
    message_decode = [message[2], message[4], message[5], message[6]]
    if c1 == 0 and c2 == 0 and c3 == 0 :
        return message_decode #message décodé retourné s'il n'y a pas d'erreur
    else : 
        position_erreur = c1*4 + c2*2 + c3 #calcul de la position de l'erreur dans le message décodé
        print("une erreur de transmission a été détectée pour le bit en position ", position_erreur)
        if message_decode[position_erreur-1]==1: #permutation de la valeur du bit errone
            message_decode[position_erreur -1] = 0
        else : 
            message_decode[position_erreur -1] = 1
        return message_decode #message décodé retourné corrigé en cas d'erreur*
    