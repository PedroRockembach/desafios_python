import os 


os.system('cls')


mais1000 = total = 0

cont = menor = 0

menorproduto = ' '

print('='*20)
print('   SUPER BARATÂO')
print('='*20)

while True:
    
    produto = str(input('Qual produto você deseja levar? '))
    
    preço = float(input('E qual seu preço? R$ '))
    
    print('='*20)
    
    total += preço
    cont += 1
    if preço >= float(1000):
        
        mais1000 +=1
        
    if cont == 1 or preço < menor:    
            
        menor = preço 
        menorproduto = produto
        
    continua = str(input('Você deseja continuar? [S/N]'))
    
    print('='*20)
    
    if continua in 'Nn':
        print('Finalizando...')
        break
    
print(f'''
O preço total da sua compra foi de \033[35m{total}\033[m 
o numero de produtos que ultrapassaram mil reais foi de \033[35m{mais1000}\033[m
e o produto mais barato foi \033[35m{menorproduto}\033[m''')