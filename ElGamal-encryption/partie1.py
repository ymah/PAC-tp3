from client import *
from random import randint
import math


NOM='yaker'
URL='http://pac.bouillaguet.info/TP3'



server = Server(URL)
URL_PARTIE='/ElGamal-encryption/'

parametre='parameters/'+NOM

paramElG = server.query(url=URL_PARTIE+parametre)


p = paramElG['p']
g = paramElG['g']


url_challenge='challenge/'+NOM

x = randint(1,p-1)

GpowX = pow(g,x,p)



h = {'h':GpowX}

Q1 = server.query(URL_PARTIE+url_challenge,h)


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

cipherM = Q1['ciphertext']

c1 = cipherM[0]
c2 = cipherM[1]




m = (c2 * modinv(pow(c1,x,p),p)) % p

print('c1 : '+str(c1),end="\n\n")
print('c2 : '+str(c2),end="\n\n")




print(m)


validate = 'validate/'+NOM


dicVal = {'plaintext':m}


res = server.query(URL_PARTIE+validate,dicVal)

print(res)
