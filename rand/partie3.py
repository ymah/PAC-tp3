from client import *
from random import randint
from math import *
from ctypes import c_uint32


NOM='yaker'
URL='http://pac.bouillaguet.info/TP3'



server = Server(URL)
URL_PARTIE='/rand/'


challenge='challenge/'+NOM
solution = 'validation/'+NOM


challengeData=server.query(url=URL_PARTIE+challenge)


tabIV=challengeData['IV']
print(tabIV)


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



def invRand(n):
    test = 0
    u = 0
    l = 0
    res = 0
    next = 0
    print("Demarage...")
    while res != n:
        if test == 0:
            next = pow(2,16)*u + l
            u +=1
            test = 1
        else:
            next = pow(2,16)*u + l
            l +=1
            test = 0
        res = (next/pow(2,16))% pow(2,15)
        res = floor(res)
    print("fin")
    return u,l

def getNextPrime(n):
    a = 1103515245
    b = 12345
    int1 = n - b
    int2 = (int1 % pow(2,32))*(modinv(a,pow(2,32)))%pow(2,32)
    return int2

u,l = invRand(tabIV[1])
print("\n")
next = pow(2,16)*u + l
nextp = getNextPrime(next)
print(nextp)
res = (floor(nextp/pow(2,15))% pow(2,16))
print(tabIV[0])
print(floor(res))

# dicSol={'key':[key0,key1,key2,key3]}



# res =server.query(url=URL_PARTIE+solution,parameters=dicSol)

# print(res)
