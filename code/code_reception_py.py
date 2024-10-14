# Edited by B0z0

""" Importation des modules """
import serial # communication arduino/python
import numpy as np
import matplotlib.pyplot as plt # trace tension =f(temps)



"""Ouverture de la liaison série"""
port = "COM6"      # COM35 est le port utilisé sur notre arduino

try : arduino = serial.Serial(port,timeout=1)
except: print('Vérifier le port utilisé')



"""Initialisation des variables"""
tension_max = 5     # valeur maximale en Volt enregistrée par l'arduino
tension_low = 0     # valeur maximale en Volt lorsque la tension est basse
tension_mid = 3.5   # valeur en Volt de la tension séparant tension basse et haute

limit = int(tension_mid * 1023/tension_max) # transformation de mid_tension en val entre 0 et 1023

nb_acq = 40 #nombre de valeurs enregistrées
nb_val = 8 #☺nombre de bits devant être traités

rawdata = []        # données brutes
compt = 0



"""Réception des données"""
arduino.readline()  # on écarte la première donnée qui est vide dans notre cas

while compt < nb_acq :
    rawdata.append(str(arduino.readline()))
    compt+=1

#print('rawdata : ',rawdata)

arduino.close()


"""Nettoyage et Stockage des données"""

def nettoie(L:list)->list :
    '''
    les élements de L sont supposés de la forme : "b'xxx\\r\\n'"
    i.e. L=["b'xxx\\r\\n'", "b'xxx\\r\\n'", ...]

    cette fonction permet de ne conserver que xxx  (x entier)
    i.e. cleanL=[xxx, xxx, ...]

    La fonction fontionne !
    '''
    cleanL = []
    for elt in L :
        temp = elt[2:-5]                            # "b'xxx;y\\r\\n'" -> "xxx;yy"
        cleanL.append(int(temp))   # ["xxx","yy"] -> [xxx,yy]
    return cleanL

cleaned_data = nettoie(rawdata)
print('cleaned_data : ',cleaned_data)

def write(L:list):
    '''Si L est de la forme [xxx, xxx, ...]
    Alors write écrit dans data :
        xxx
        xxx
        ...
    '''
    compt=0
    file = open("data.txt",mode="w")
    for elt in L :
        compt+=1
        temp = str(elt)
        file.write(temp+';'+str(compt)+'\n')
    file.close()

'''
write(cleandata)    # inscription des valeurs dans le dossier data.txt

vals,temps = np.loadtxt("data.txt",delimiter=";",unpack=True)



"""Tracé des valeurs"""
plt.plot(temps,vals)
plt.show()
'''


"""Traitement des données"""

def reception(L:list,n:int)->list:
    '''
    le message reçu est de la forme [0,0,0,0,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0]
                                             ↑
            bit pour signaler le début du messsage
    n est le nombre de bits reçu
    '''
    i=0
    while L[i]==0 and i<len(L):  #élimination des premiers 0
        i+=1
    i+=1            #élimination du bit de signal (premier 1)
    if i+n>len(L):
        print('le message est coupé, veuillez réessayer')
    else :
        return L[i:i+n]

recep_data = reception(cleaned_data,nb_val)
assert type(recep_data) == list

def Tension_vers_Binaire(L:list)->list:
    """transforme les tensions (valeurs entre 0 et 1023) enregistrées dans L
    et renvoie les valeurs binaires correspondantes"""
    newL=[]
    for elt in L :
        if elt > limit :
            newL.append(1)
        else :
            newL.append(0)
    return newL

binaire_data = Tension_vers_Binaire(recep_data)
print('binaire_data : ',binaire_data)



def Binaire_vers_Texte(L:list)->str:
    """transforme une chaine binaire renvoie le texte correspondant"""
    text = "" # chaîne vide qui va contenir le texte final
    octets = [L[i:i+8] for i in range(0, len(L), 8)] # Sépare la liste en chunks de 8bits

    for octet in octets:
        ascii_val = 0

        for i in range (8):
            ascii_val += octet[7-i]*(2**i) #calcul de la valeur du chunk en base 10

        char = chr(ascii_val) # Transforme le code ascii en caractère
        text += char
    return text


message = Binaire_vers_Texte(binaire_data)
print('message : ',message)


write(binaire_data)    # inscription des valeurs dans le dossier data.txt

vals,temps = np.loadtxt("data.txt",delimiter=";",unpack=True)



"""Tracé des valeurs"""
plt.plot(temps,vals,"ob")
plt.show()