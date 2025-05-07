import os
from pygame import *

#encontrar uma biblioteca que abra e execute um arquivo.mp3

os.system('cls')


mixer.init()                 #inicia o toca musicas
mixer.music.load('joao.mp3') #carrega o arquivo#CUIDAR NOME DO ARQUIVO
mixer.music.play()           #começa a tocar  #Usar () no fim de todos

event.wait()