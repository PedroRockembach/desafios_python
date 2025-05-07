import os 

#faça uma matriz 3x3 que recebe os valores de cada posição

os.system("cls")

matriz = [[],[],[]]

for c in range(1,10):
    
    valor = int (input("digite um numero: "))
    
    if c in range(1,4):
        
        matriz[0].append(valor)
    if c in range(4,7):
        
        matriz[1].append(valor)  
    if c in range(7,10):
        
        matriz[2].append(valor)  
    
print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}\n")