import os

os.system('cls')

from time import sleep

pmax=pmin=0

print('\033[35mPrograma comparador de pesos! \033[m')
sleep(2)
print('\033[34mCarregando...\033[m')
sleep(3)

for p in range(1,6):
    peso=float(input(f'\033[35mQual peso da {p} pessoa?\033[m'))
    
    if p == 1:
        pmax=peso
        pmin=peso
        
    else: 
        
        if peso>pmax:
            pmax=peso
            
        elif peso<pmin:
            pmin=peso
            
print(f'O maior peso entre estas pessoas foi o {pmax}\nE o menor peso dentre esses foi o {pmin}')
        