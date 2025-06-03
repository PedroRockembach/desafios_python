def maior(*num):
    from time import sleep
    vazio = 0
    try:
        maior = max(num)
    except ValueError:
        vazio = 1
        
    if vazio == 0:    
        cont = 0
        print('Analisando...')
        sleep(0.5)
        for i in num:
            print(f"{i}",end=' ')
            cont+=1
        print(F"\nForam informados {cont} valores e o maior foi {maior}")
        print('-'*30)
    else: 
        print('-'*30)
        print("A lista inserida esta vazia.")
        print('-'*30)
    
maior(3,5,8,1)
maior(7,1,3)
maior()
