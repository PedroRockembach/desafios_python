from os import system

system("cls")

def fatorial(n,mostra=False):
    fat = 1
    if mostra:        
        if n == 0 or n == 1:
            return f'O Fatorial de {n} é 1 por convenção matematica. '
        
        #o fatorial de 0 ou de 1 é = a 1
        
        else: 
            for i in range(n,0,-1):
                fat *= i 
                print(f'{i}', end=' x ' if i > 1 else ' = ')
            return f'{fat}'
    else:
        
        for i in range(n,0,-1):
            fat *= i
        return fat
        
print(fatorial(5,True))
print(fatorial(3))               
                
    