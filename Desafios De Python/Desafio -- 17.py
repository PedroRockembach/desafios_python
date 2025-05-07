#Faça um programa que leia o valor de dois catetos(oposto e adjacente) de um triangulo retangulo e após calcule a hipotenusa

import math
import os

os.system('cls')


oposto=float(input('indique o valor do \033[36mcateto oposto\033[m -->'))

adjacente=float(input('indique agora o valor do \033[36mcateto adjacente\033[m -->'))

hipotenusa=math.hypot(oposto, adjacente)

print(f'''
O valor da hipotenusa de um triangulo retangulo que: 
Cateto adjacente é \033[36m{adjacente} 
Cateto oposto é \033[36m{oposto} 
É igual a \033[31m{hipotenusa:.2f}\033[m''')