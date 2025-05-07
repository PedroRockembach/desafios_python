import os 

os.system("cls")

temp = list()
principal = list()
max = min = 0

while True:
    
    nome = str(input("insira um nome: ")) #insere nome
    peso = int(input("Insira um peso: ")) #insere peso
    
    temp.append(nome) #adiciona a uma lista temporaria p agrupar em uma lista maior
    temp.append(peso) #adiciona a uma lista temporaria p agrupar em uma lista maior
    
    if len(principal) == 0: #"se a lista principal estiver vazia" verifica se tem algum valor para comparar com maior e menor, evitando erros
         
        max = min = temp[1]
        
    else:
        
        # verifica maior e menor aqui, verificando se o valor da lista temp, que vai ser limpa em seguida, é maior ou menor
        
        if temp[1] > max: 
            max = temp[1]
            
        if temp[1] < min:
            min = temp[1]        
    
    principal.append(temp[:]) #adiciona a lista maior
    temp.clear()              #limpa a temporaria
    
    saida = str(input("Voce deseja continuar? [S/N]: "))
    if saida in "NnNaoNãonãonao":
        break
    
print("-="*30)

print(f"O numero de pessoas cadastradas neste programa foi de {len(principal)}") #conta quantas pessoas foram adicionadas na lista

print(f"\nO Maior peso foi de {max}, peso de:\n",end = '')

for c in principal: # percorre cada iteração da lista buscando por valores de "max" repetidos
    
    if c[1] == max:
        print(f"{c[0]}")

print(f"\nO Menor peso foi de {min}, peso de:\n",end = '')

for p in principal: # percorre cada iteração da lista buscando por valores de "min" repetidos
    
    if p[1] == min:
        print(f"{p[0]}")

                
    