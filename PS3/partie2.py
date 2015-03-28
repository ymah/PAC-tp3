from client import *
from random import randint
import math




def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, \
                                               divmod(lastremainder,\
                                                      remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), \
        lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m




#TP

NOM='yaker'
URL='http://pac.bouillaguet.info/TP3'



server = Server(URL)
URL_PARTIE='/PS3/'

parametre='parameters/'+NOM

signer='sign/'+NOM

url_validate='validate/'+NOM
PK_url='PK/'+NOM

PK_dic = server.query(url=URL_PARTIE+PK_url)


h=PK_dic['h']
p=PK_dic['p']
g=PK_dic['g']



m0=91097 #randint(1000,100000)

s_m0 = server.query(url=URL_PARTIE+signer,parameters={'m':m0})
r0 = s_m0['signature'][0]
s0 = s_m0['signature'][1]

m1=63934 #randint(1000,100000)

s_m1 = server.query(url=URL_PARTIE+signer,parameters={'m':m1})
r1 = s_m1['signature'][0]
s1 = s_m1['signature'][1]

q = p - 1
m0_m1 = (m0 - m1)
s0_s1 = s0 - s1
inv_s0_s1=modinv(s0_s1,q)

k=(inv_s0_s1 % q)*(m0_m1 % q) % q



inv_r = modinv(r0,q)


a = (m0 % q)*(inv_r % q) % q
b = (k * s0)
c = (b % q)*(inv_r % q) % q
x = (a - c) % q
res = server.query(url=URL_PARTIE+url_validate,parameters={'x':x})

print(res)
