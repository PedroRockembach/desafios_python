import os

#faça uma matriz 3x3 que recebe os valores de cada posição
#a -> Soma dos numeros pares
#b -> Soma dos valores da terceira coluna
#c -> Maior valor da segunda linha 

os.system("cls")

pares = 0
terceira_coluna = 0
matriz = [[],[],[]]

for l in range(3): #linha
    
    for c in range(3): #coluna 
        
        valor = int (input(f"digite um numero[{l},{c}] "))
        matriz[l].append(valor)
        
        if valor % 2 == 0:
            
            pares += valor
            
        if c == 2:
            
            terceira_coluna += valor
            
        
maior_ldois = max(matriz[1])      

print()
print("="*30)      

for linha in matriz:
    print(linha)
print("="*30)      
print(f"\na soma dos numeros pares deu {pares}")
print(f"a soma da terceira coluna deu {terceira_coluna}")
print(f"o maior valor da linha 2 foi {maior_ldois}")
    
    
    
        
        