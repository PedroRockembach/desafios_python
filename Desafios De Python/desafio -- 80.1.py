import os 

os.system('cls')

numeros = []

#crie um programa que: o usuario digite 5 valores e os cadastre em uma lista ja na posição correta de inserção(sem usar .sort) 
#por fim mostre a lista ordenada



for c in range(0,5):
    
    entrada = int (input("digite numero: "))
    
    if c == 0 or entrada > numeros[-1]:
        
        numeros.append(entrada)
        
    else:
        pos = 0
        while pos < len(numeros):
            
            if entrada <= numeros[pos]:
                numeros.insert(pos, entrada)
                break 
            pos+=1
               
print(numeros)
