import os 

#crie um programa que simule um caixa eletronico, no inicio pergunte ao usuario qual será a quantidade de dinheiro sacado(int)
#considere que o programa possui notas de: 50 20 10 e 1

os.system('cls')
dindin = nota1 = nota10 = nota20 = nota50 = 0

#resto da divisao ser 0 = true = nota valida 

print('-'*25)
print('¦    Caixa eletrônico   ¦')
print('-'*25)

while True:
    dindin = int(input('\nQuanto dinheiro você quer sacar? R$'))
   
    dinheiro = dindin
    
    notas50 = dinheiro // 50
    dinheiro = dinheiro % 50
    
    notas20 = dinheiro // 20
    dinheiro = dinheiro % 20
    
    notas10 = dinheiro // 10
    dinheiro = dinheiro % 10
    
    notas1 = dinheiro // 1
    dinheiro = dinheiro % 1
    


    if dindin == 0 or dindin<0:
        a=print('dinheiro insuficiente para retirada, selecione um valor valido')
    else: 
        a= print(f'Para chegar ao valor de R${dindin} precisamos de: ')
        
    print('='*20)
        
    if notas50 == 0:
        print('',end='')    
    else:
        print(f'{notas50} Cédulas de R$50')
        
    if notas20 == 0:   
        print('',end='')    
    else:
        print(f'{notas20} Cédulas de R$20')     
    
    if notas10 == 0:
        print('',end='')     
    else:
        print(f'{notas10} Cédulas de R$10')
    
    if notas1 == 0:
        print('',end='')     
    else:
        print(f'{notas1} Cédulas de R$01')   
    
    print('='*20)
    
    resp = str(input('Deseja continuar?[S/N]')).lower().strip()
    
    print('='*20)
    
    if resp in 'NnnaoNaoNAO':
        
        print('Fechando conta do banco')
        break