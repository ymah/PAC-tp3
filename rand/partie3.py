from client import *
from random import randint
from math import *
from ctypes import c_uint32


NOM='yaker'
URL='http://pac.bouillaguet.info/TP3'



server = Server(URL)
URL_PARTIE='/rand/'


challenge='challenge/'+NOM


tabIV=server.query(url=URL_PARTIE+challenge)

print(tabIV)

def rand(n):
    next = n * 1103515245 + 12345
    return floor((next/65536) % 32768)


def invRand(n):
    res = 0
    i = 0
    while res != n:
        res = i % 32768
        i+=1
    res *= 65536
    return ((res - 12345)/ 1103515245)

next=invRand(tabIV['IV'][0])



print(next)
print(rand(next))
