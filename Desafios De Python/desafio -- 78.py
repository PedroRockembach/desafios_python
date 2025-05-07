import os 

os.system('cls')
numeros = []

#modula uma lista com uma quantidade X de numeros

for i in range (0,5):
    
    numero = int(input("digite um numero: "))
    numeros.append(numero) #adiciona o valor no ultimo lugar da lista 
    
    maior = max(numeros) #descobre o maior e menor item da lista
    menor = min(numeros)

    
print(f"A lista final ficou da seguinte maneira = {numeros}") # printa a lsita 

print(f"O maior digito da lista foi {maior} e sua posição é {numeros.index(maior)+1}") #descobre a posição na lista daquele valor, adiconando mais 1 para desconsiderar o 0 da contagem da lista 
print(f"O menor digito da lista foi {menor} e sua posição é {numeros.index(menor)+1}")