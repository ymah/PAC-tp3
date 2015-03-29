from client import *
from random import randint
from math import *
from ctypes import c_uint32


NOM='yaker'
URL='http://pac.bouillaguet.info/TP3'



server = Server(URL)
URL_PARTIE='/rand/'


challenge='challenge/'+NOM
solution = 'prediction/'+NOM


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


def getNextp(n):
    a = 1103515245
    b = 12345
    return a * n + b % pow(2,32)



key3 = rand(getNextp(invRand(tabIV[0])))
print(key3)

key2 = rand(getNextp(invRand(key3)))
print(key2)

key1 = rand(getNextp(invRand(key2)))
print(key1)

key0 = rand(getNextp(invRand(key1)))
print(key0)


dicSol={'key':[key0,key1,key2,key3]}



res =server.query(url=URL_PARTIE+solution,parameters=dicSol)

print(res)
