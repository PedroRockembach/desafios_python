import os 
from random import *

os.system("cls")

numeros = [p for p in range(1, 61)]
palpite = []

#palpites - > O programa deve sortear a quantidade X de jogos decidida pelo jogador e deve retornar uma lista de 6 numeros de 1 a 60 sem repetir nenhum numero dentro do mesmo jogo

jogos = int(input("Quantos jogos devo sortear?"))

for a  in range (jogos):
    
    shuffle(numeros)
    _palpite = []
    
    for c in numeros[:6]:
        

        _palpite.append(c)
    
    palpite.append(_palpite)
    print(f"{_palpite}")

#print(f"{palpite}\n")