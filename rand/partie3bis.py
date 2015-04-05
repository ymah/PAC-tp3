from client import *
from random import randint
from math import *
from ctypes import c_uint32
import sys


NOM='yaker'
URL='http://pac.bouillaguet.info/TP3'


def srand(seed):
    global nextR
    nextR = seed

def rand():
    global nextR
    nextR = nextR * 1103515245 + 12345
    return round((nextR/65536) % 32768)


# merci http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



server = Server(URL)
URL_PARTIE='/rand/'


challenge='challenge/'+NOM
solution = 'validation/'+NOM


challengeData=server.query(url=URL_PARTIE+challenge)


tabIV=challengeData['IV']
print(tabIV)



# test
# on cherche a trouver une seed qui marche avec l'IV_0 et l'IV_1
for i in range(pow(2, 32)):
    if(i%100000000 == 0):
        print("Current i = " + str(i))
    srand(i)
    if(rand() == tabIV[0]):
        if(rand() == IV_1):
            print(bcolors.OKGREEN + str(i) + bcolors.ENDC)

print(bcolors.WARNING + "aucune seed de trouve" + bcolors.ENDC)
