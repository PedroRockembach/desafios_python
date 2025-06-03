from os import system


system("cls")

numeros = []

def sorteio_lista(lista,repeat=True):
    """
    Recebe uma lista e preenche de valores entre 1 e 10 

    Args:
        lista (int): _description_
        repeat (bool): Se True, valores podem se repetir; se False, valores serão únicos.
    """
    from time import sleep
    from random import randint
     
    if repeat == True:
        
        for i in range(5):      
            aleatorio = randint(1,10) 
            lista.append(aleatorio)    
            print (f'{aleatorio} ',end=' ',flush=True)
            sleep(0.5)
    if repeat == False:
        
        cont=0
        while cont < 5:      
            aleatorio = randint(1,10)
            if aleatorio not in numeros:
                numeros.append(aleatorio)
                cont+=1    
            else:
                continue
            print (f'{aleatorio} ',end=' ',flush=True)
            sleep(0.5)
        
 
def soma_par(lista):   
    
    pares = 0
    for x in lista:
        if x % 2 == 0:
            pares += x
            
    print(f"\nA soma dos numeros pares da lista: {lista} foi {pares}")
    
sorteio_lista(numeros,repeat=False)
soma_par(numeros)