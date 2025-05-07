#DESAFIO 18- lê um angulo e retorna cos sen e tan

import math
import os

os.system('cls')

angulo=(float(input('digite um \033[35mângulo\033[m -->')))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'o \033[33mSENO\033[m de {angulo} é {seno:.2f}')
print(f'o \033[33mCOSSENO\033[mde {angulo} é {cosseno:.2f}')

if tangente == 16331239353195370.00:
    
    print(' a \033[33mTANGENTE\033[m não existe')
else:
    
    tangente=math.tan(math.radians(angulo))
    print(f'a \033[33mTANGENTE\033[m de {angulo} é de {tangente:.2f}')

