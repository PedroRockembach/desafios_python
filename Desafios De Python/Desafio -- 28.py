#faça o programa gerar um numero de 0 a 5 e insira uma entrada para o usuario tentar advinhar o numero
#o programa deve indicar se o usuario acertou ou não

import os
import random 

os.system('cls')
n=random.randint(0, 5)

#print(n) Numero escolhido pelo computador

a=int(input('tente advinhar o numero que estou pensando! está entre 0 e 5 -->'))

if a == n:
    
    print('parabéns, você acertou!')
else:
    
    print(f'ops, foi por pouco, eu pensei em {n} não em {a}')
    