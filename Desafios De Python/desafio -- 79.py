import os 

os.system('cls')

numeros = []

while True:
    
    numero = int(input("digite um numero: "))
    
    if numero in numeros: #e o programa deve verificar se algum foi repetido
        
        print("Valor duplicado.")
        # o valor repetido deve ser desconsiderado,
    
    else:
        
        print("Valor valido")
        
        numeros.append(numero) #adiciona o valor no ultimo lugar da lista 
        
    saida = input("Voce deseja continuar?[S/N]")
    
    if saida in "Ss":
        
        continue
    if saida in "Nn":
        
        break
    else:
        
        print("invalido")
        
        continue
    
print(f"{sorted(numeros)}") #por fim ele deve printar somente os vlaores unicos em ordem crescentex