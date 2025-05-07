# FAÇA UM PROGRMA QUE LEIA O SEXO DE UMA PESSOA E SO DEVE ACEITAR F OU M, SE HOUVER OUTRA ENTRADA ELE DEVE PERGUNTAR MIAS UMA VEZ
import os
from time import sleep

os.system('cls')

s='x'

while not s in 'fFmM':
    
    s=input('Digite seu sexo[F/M]: ')
    
    if s in 'FfMm':
        
        print('\033[32mDado correto inserido, encerrando...\033[m')
        
    else:  
        
        print('\033[31mDigite um valor valido[F/M]\033[m')
        
    sleep(1)
print('fim')