from os import system
system("cls")

def fatorial(num,show=False):
    """_summary_

    Args:
        num (int): Inteiro 
        show (bool, optional): 
                    True = Mostra a operação do fatorial
                    False = só retorna o valor final

    Returns:
        fat: fatorial de num
    """
    fat = 1
    from time import sleep
    
    if show == False:
        for i in range(num,1,-1):
            fat *= i
        return f'O resultado para o fatorial de {num} é {fat}'
        
    if show == True:
        for i in range(num,0,-1):
            sleep(0.5)   
            print(f"{i} ",end='',flush=True)
            if i>1:
                print(f"x ",end='',flush=True)
            else:
                print(f"= ",end='',flush=True)        
            fat *= i
            
        return fat
            
print(fatorial(5,show=True))