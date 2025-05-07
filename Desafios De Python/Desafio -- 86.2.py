import os

#faça uma matriz 3x3 que recebe os valores de cada posição

os.system("cls")

matriz = [[],[],[]]

for l in range(3): #linha
    
    for c in range(3): #coluna 
        
        valor = int (input(f"digite um numero[{l},{c}] "))
        matriz[l].append(valor)
        
for linha in matriz:
    print(linha)
    
    
    
        
        