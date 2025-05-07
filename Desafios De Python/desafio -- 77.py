import os 

os.system('cls')

#contar vogais de uma tupla pré estabelecida que contenha varias palavras ( sem acento ) e mostre suas vogais 

#entrada=str(input("Digite uma palavra para ver suas vogais: "))
#opção com entrada de palavra

tupla = (
    'casa', 'coringa', 
    'computador', 'caneca', 
    'lapiseira', ' manometro')


for palavra in tupla:
    
    for letra in palavra:
          
        if letra.lower() in ("a","e","i","o","u"):
            
            print(f"\033[32m{letra}\033[m")
        else:
            
            print(f"\033[31m{letra}\033[m")
               
    print("")
    
    #a partir da segunda bateria os canais foram invertidos 