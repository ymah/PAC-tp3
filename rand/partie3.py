from client import *
from random import randint
from math import *
from ctypes import c_uint32


NOM='yaker'
URL='http://pac.bouillaguet.info/TP3'



server = Server(URL)
URL_PARTIE='/rand/'


challenge='challenge/'+NOM


challengeData=server.query(url=URL_PARTIE+challenge)


tabIV=challengeData['IV']
print(tabIV)


def partie1(n):
    return n * 1103515245 + 12345


def partie2(n):
    return floor((n/65536) % 32768)



def rand(n):
    next = partie1(n)
    return partie2(next)


def invRand(n):
    res = 0
    i = 0
    while rand(i) != n:
        i+= 1
    return i


next=invRand(tabIV[1])

print(next)
print(rand(next))
