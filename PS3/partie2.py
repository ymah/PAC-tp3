from client import *
from random import randint
import math


NOM='yaker'
URL='http://pac.bouillaguet.info/TP3'



server = Server(URL)
URL_PARTIE='/PS3/'

parametre='parameters/'+NOM

paramElG = server.query(url=URL_PARTIE+parametre)
