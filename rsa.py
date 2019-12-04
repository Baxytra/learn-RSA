import math
import random as rd
import sys

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
codageAlphabet = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
    
def estPremier(nombre):
    """
    Renvoie True si nombre est premier

    @param int : nombre
    
    @return Boolean
    """

    for diviseur in range(2,int(math.sqrt(nombre)+1)):
        if(nombre%diviseur == 0):
            return False
    return True

def sontPremierEntreEux(p,q):
    """
    Renvoie True si p et q sont premiers entre eux

    @param int : p
    @param int : q
    
    @return Boolean
    """

    if pgcd(p,q) == 1:
        return True

    return False

def pgcd(a,b):
    """
    Calcule le PGCD de a et b de manière récursive
    
    @param int : a
    @param int : b

    @return int : pgcd(b,a%b)
    """

    if b == 0:
        return a
    else:
        return pgcd(b,a%b)

def trouvePremier(maxEntier):
    """
    Trouve un nombre premier inférieur à maxEntier
    
    @param int : maxEntier

    @return int : nombre
    """

    nombre = 4
    while not estPremier(nombre):
        nombre = rd.randint(maxEntier-maxEntier/2, maxEntier)
    return nombre


def euclideEtendu(b, mod):
    """
    Applique euclide étendu sur b et mod pour obtenir : u*b + v*mod = 1

    @param int : mod
    @param int : b

    @return int : u
    """

    # Première étape
    u = 1
    v = 0
    d = b 

    # Deuxième étape
    u2 = 0
    v2 = 1
    d2 = mod

    while d2 != 0:
        q = d//d2
        (u, u2, v, v2, d, d2) = (u2, -q*u2+u, v2, -q*v2+v, d2, -q*d2+d)
    return u

def calculeInverse(b, mod):
    """
    Calcule l'inverse modulaire d'un nombre

    @param int : b
    @param int : mod

    @return int : res
    """
    res = euclideEtendu(b, mod)
    while res <= 0:
        res += mod
    return res

def initialisation():
    """ Initialise l'alphabet à utiliser et sa correspondance ASCII """
    
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    codageAlphabet = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
    
def entierLettre(lettre):
    """
    Détermine le code ASCII appliqué à une lettre

    @param str : lettre
    
    @return codeAscii
    """
    
    codeAscii = str(ord(lettre))
    return codeAscii

def decodageAlphabet(i):
    """
    Retourne le rang k du code de la lettre dans la liste Alphabet
    
    @param int : i

    @return int : k
    """
    
    for k in range(len(codageAlphabet)):
        if int(codageAlphabet[k]) == int(i):
            return k

def aPuisBModuloN(a, b, mod):
    """
    Calcule la puissance modulaire: (a**b)%mod

    @param int : a
    @param int : b
    @param int : mod

    @return int : result
    """
    
    result = 1
    while b>0:
        if b&1>0:
            result = (result*a)%mod
        b >>= 1
        a = (a*a)%mod
    return result

def convertAscii(message):
    """
    Conversion vers ASCII de chaque lettre du message en récursif

    @param str : message

    @return 
    """

    if len(message) == 0:
        return ""
    else:
        return entierLettre(message[0])+convertAscii(message[1:])

def chiffre(message):
    """
    Fonction de chiffrement RSA

    @param str : message

    @return int : messageChiffre
    """

    M = convertAscii(message)
    messageChiffre = aPuisBModuloN(int(M), _e, _n)
    return messageChiffre

def dechiffre(messageChiffre):
    """
    Fonction de déchiffrement RSA

    @param int : messageChiffre

    @return str : message
    """

    d = calculeInverse(_e, _phin)
    message = aPuisBModuloN(int(messageChiffre), d, _n)
    return message

def trouveE(n, phin):
    """
    Trouve une clé publique première à phi(n)

    @param int : n
    @param int : phin

    @return int : i
    """

    for e in range(2,_phin):
        if sontPremierEntreEux(e, _phin):
            return e

def parseASCII(messageCode):
    """
    Parse le message déchiffré pour le décoder

    @param int : messageCode
    
    @return str : messageCode
    """

    messageDecode = ""
    messageCode = str(messageCode)
    for k in range(0,len(messageCode), 2):
        code = messageCode[k] + messageCode[k+1]
        messageDecode += alphabet[decodageAlphabet(code)]
    return messageDecode

# Variable globales
_p = trouvePremier(100000000000000) # On prend de grands nombres p et q pour que la clé soit un minimum robuste
_q = trouvePremier(100000000000000)
_n = _p*_q
_phin = (_p-1)*(_q-1)
_e = trouveE(_n, _phin)

print("--------- DEBUG: -----------------")
print("P : "+str(_p))
print("Q : "+str(_q))
print("N : "+str(_n))
print("PHIN :"+str(_phin))
print("E : "+str(_e))

print("-------------- CHIFFRE -----------")
messageChiffre = chiffre('ENSIBS')
print(messageChiffre)
print("-------------- DECHIFFRE ---------")
messageDechiffre = dechiffre(messageChiffre)
messageDecode = parseASCII(messageDechiffre) 
print(messageDecode)
