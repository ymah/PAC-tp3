from client import *
from random import randint
import math
from ctypes import c_uint32


NOM='yaker'
URL='http://pac.bouillaguet.info/TP3'



server = Server(URL)
URL_PARTIE='/rand/'


challenge='challenge/'+NOM


tabIV=server.query(url=URL_PARTIE+challenge)

print(tabIV)
