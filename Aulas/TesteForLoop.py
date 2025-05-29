import os
os.system('cls')
#listas de nomes
nomes=['pedro','joão','tiago', 'lucas', 'rock', 'matheus','jose', 'matheus', 'gustavo']

#Encontrar 'rock'!
for a in nomes:
    if a == 'rock':
        print(f'O paciente {a} foi encontrado! Interronpendo busca...')
        break
if a != 'rock':
    print('paciente não encontrado')
print('Finalizando loop.')
