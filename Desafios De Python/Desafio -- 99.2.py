#Desafio -- 99
def maior(*num):
    """
    Função que recebe uma lista e encontra o maior valor informado
    """
    from time import sleep
    
    if not num: 
        print('-'*30)
        print("A lista inserida esta vazia.")
        print('-'*30)    
    else:    
        print('Analisando...')
        sleep(0.5)
        for i in num:
            print(f"{i}",end=' ')
        print(F"\nForam informados {len(num)} valores e o maior foi {max(num)}")
        print('-'*30)

    
maior(3,5,8,1)
maior(7,1,3)
maior()