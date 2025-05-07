import os 

os.system('cls')

#Tupla com nome do produto e preço respectivo
#Mostrar em tabela

#Tupla = 

produtos = (
    'Compasso', 'R%4,50',
    'Transferidor', 'R%3,75',
    'Régua', 'R%5,10',
    'Estojo', 'R%8,80',
    'Lapiseira', 'R%3,79',
    'Borracha', 'R%2,00')
           

#print(f'{produtos}')

# Tabela = 

'''print(f"""
-=-=-=Preços 2024 Papelaria-=-=-=
PRODUTO         |      PREÇO
{produtos[0]}        |      {produtos[1]}      
{produtos[2]}    |      {produtos[3]}   
{produtos[4]}           |      {produtos[5]}   
{produtos[6]}          |      {produtos[7]}   
{produtos[8]}       |      {produtos[9]}   
{produtos[10]}        |      {produtos[11]} """)'''

for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}',end = '') 
    else:     
        print(f'{produtos[item]:.>5}') 
      
      
