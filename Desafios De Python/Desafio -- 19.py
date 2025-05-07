#o programa lê quatro nomes e sorteia um aleatorio

import random
import os

os.system('cls')


nome1=input('digite um \033[35mnome\033[m -->')

nome2=input('digite mais um \033[33mnome\033[m -->')

nome3=input('mais um \033[34mnome\033[m-->')

nome4=input('o ultimo \033[32magora\033[m -->')

lista=nome1, nome2, nome3, nome4

sorteado=random.choice(lista)

print(f'o aluno sorteado foi \033[31m{sorteado}\033[m')