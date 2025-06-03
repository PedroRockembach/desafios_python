from os import system


system("cls")
numeros = []
def sorteio_lista(lista):
    from time import sleep
    from random import randint
    for i in range(5):      
        aleatorio = randint(1,10) 
        lista.append(aleatorio)    
        print (f'{aleatorio} ',end=' ',flush=True)
        sleep(0.5)
 
def soma_par(lista):   
    
    pares = 0
    for x in lista:
        if x % 2 == 0:
            pares += x
            
    print(f"\nA soma dos numeros pares da lista: {lista} foi {pares}")
    
sorteio_lista(numeros)
soma_par(numeros)