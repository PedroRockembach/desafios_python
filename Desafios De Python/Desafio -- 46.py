from time import sleep
import os
os.system('cls')

#faça um programa que faça uma contagem regressiva para o estouro de fogos de artificio
#A contagem deve ir de 10 a 0 com uma pausa de 1 segundo entre cada numero

c=0

print('Preparem-se para a contagem regressiva do estouro de \033[31mFogos de artificio\033[m')

for c in range(9,-1,-1):

    print(c+1)
    sleep(1)

print('Feliz ano novo')