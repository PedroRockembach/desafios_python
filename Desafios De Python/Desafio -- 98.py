#Desafio -- 98

from os import system

system("cls")

def linha():
    print("-"*30)
def contador(inicio,fim,passo):
    from time import sleep
    '''
    se inicio > fim = decrementa
    se inicio < fim = aumenta
    se passo = 0 passo == 1
    se passo negativo -> modulo de passo 
    '''
    
    if passo < 0:
        passo = abs(passo)  
        
    if passo == 0:
        passo = 1
        
    if inicio < fim:
        for i in range (inicio,fim+1,passo): 
            print(f'{i}',end=' ',flush=True)
            sleep(0.5)
        print("Fim")
        linha()
        
    else: 
        for i in range (inicio,fim-1,-passo): 
            print(f'{i}',end=' ',flush=True)
            sleep(0.5)
        print("Fim")     
        linha() 

        
#Main()

contador(1,10,1)

contador (10,1,1)

print("É sua vez!")

continua = 1

while continua > 0:
    linha()
    
    try:
        
        inicio = int(input("inicio: "))
        fim = int(input("fim: "))
        passo = int(input("passo: "))
        
    except ValueError:
        
        print("Insira somente numeros inteiros ")
        continue
    
    linha()


    contador(inicio,fim,passo)
    
    continua = int(input("deseja continuar?[1/0] "))
    system("cls")