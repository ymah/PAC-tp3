from client import *
from random import randint
from math import *
from ctypes import c_uint32
import sys

NOM='yaker'
URL='http://pac.bouillaguet.info/TP3'



server = Server(URL)
URL_PARTIE='/rand/'


challenge='challenge/'+NOM
solution = 'validation/'+NOM


challengeData=server.query(url=URL_PARTIE+challenge)


tabIV=challengeData['IV']
print(tabIV)



#------------------------------------------------
# Fonctions utiles :
#------------------------------------------------
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

#------------------------------------------------
#------------------------------------------------
# Fonction de random et d'inverse de random
#------------------------------------------------
# def invRand(n,u,l):
#     ''' InvRand
#     permet de retrouver u et l ainsi que le next dans l'expression suivante :
#     next = 2^16*U + L
#     rand() = (next / 2^16) mod 2^15
#     '''
#     test = 0
#     res = 0
#     next = 0
#     # print("Demarage")
#     # print("En cours",end="")
#     while res != n:
#         if test == 0:
#             next = (2**16)*u + l
#             u +=1
#             test = 1
#         else:
#             next = (2**16)*u + l
#             l +=1
#             test = 0
#         res = (next/(2**16))% (2**15)
#         res = floor(res)
#     print(u,l,floor(next))
#     return u,l,floor(next)



def getRand(u,l):
    a = 2**16
    b = 2**15
    return (u + (l / (2**16))) % (2**15)
def getUL(n):
    u = 0
    l = 0
    test = 0
    while floor(getRand(u,l)) != n:
        if test == 1:
            u+=1
            test = 0
        else:
            l+=1
            test = 1
    return u,l

def part1(n):
    a = 1103515245
    b = 12345
    next = a*n + b
    return next

def part2(n):
    return (floor(n/65536) % 32768)


def rand(n):
    next =  part1(n)
    return part2(next)
def genNext(u,l):
    return (2**16)*u + l


def getNext(n):
    a = 1103515245
    b = 12345
    int1 = n - b
    return int1

#------------------------------------------------




#------------------------------------------------
#Tests :
#------------------------------------------------





dicSol={'key':[25038,23894,25205,13004]}



res =server.query(url=URL_PARTIE+solution,parameters=dicSol)

print(res)
