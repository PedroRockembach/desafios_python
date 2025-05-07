import os 

os.system('cls')

preço=float(input('\033[36mQual o preço do produto? -->'))

print('-=-'*20)

pagamento=str(input('''E qual vai ser a forma de pagamento?\033[m
                    

\033[32m1-Dinheiro\033[m
\033[33m2-Cartão(até duas vezes sem juros\033[m
\033[36m   -=-=-=-=-=-=->\033[m''')).lower()

#a vista ou cheque= 10% de desconto
#a vista no cartão= 5% de desconto
#em até 2x no cartão sem juros
#3x ou mais no cartão= 20% de juros

if pagamento=='dinheiro' or pagamento == '1':
    
    d=preço-(preço*float(0.10))
    print('\033[35mCerto, no dinheiro tem um desconto de 10%')
    print(f'Sua compra de {preço} sairá por apenas {d}\033[m')
    
elif pagamento=='cartão' or pagamento == '2':
    
    parcelas=int(input('''\033[32mCerto, em quantas vezes o senhor gostaria de fazer? Em até duas vezes, não tem juros, a partir de 3 o valor tem um juros de 20%...
    -=--=--=--=->\033[m'''))
    juros20=preço+float(preço*0.20)
    
    if parcelas>=int(3):
        
        print(f'Certo, o valor inicial de {preço} saíra em {parcelas} vezes por R${juros20}')
        print(f'Assim, a sua parcela em {parcelas} meses sáira por R${juros20/parcelas}')
        
    elif parcelas<int(3):
        
        print(f'\033[36mCerto, sua parcela então ficara {preço/float(2.0):.1f} mensais.\033[m')
        
    else:
        
        print('\033[31mIsso não é uma opção do número de parcelas, tente novamente')
else:
    
    print('\033[31mIsso não é uma forma de pagamento valida, tente novamente.')
    