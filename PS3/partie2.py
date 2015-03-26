from client import *
from random import randint
import math




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




#tP

NOM='yaker'
URL='http://pac.bouillaguet.info/TP3'



server = Server(URL)
URL_PARTIE='/PS3/'

parametre='parameters/'+NOM

signer='sign/'+NOM

PK_url='PK/'+NOM
PK_dic = server.query(url=URL_PARTIE+PK_url)


h=PK_dic['h']
p=PK_dic['p']
g=PK_dic['g']



m1=12345
s_m1 = server.query(url=URL_PARTIE+signer,parameters={'m':m1})
r1 = s_m1['signature'][0]
s1 = s_m1['signature'][1]


m2=67890
s_m2 = server.query(url=URL_PARTIE+signer,parameters={'m':m2})
r2 = s_m2['signature'][0]
s2 = s_m2['signature'][1]



def getK(m1,m2,s1,s2,p):
    a = (m1 - m2)%p
    b = (s1 - s2)%p

    return (a/b) % (p - 1)


print(getK(m1,m2,s1,s2,p))
