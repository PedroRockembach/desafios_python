#crie um programa que aprove um imprestimo ou não. O programa deve perguntar-> O valor da casa
#o salario do comprador e em quantos anos ele pretende pagar. O programa deve calcular as parcelas mensais e 
#verificar se 30% do salario do comprador é suficiente para pagar ou não

import os

os.system('cls')

v=float(input('\033[35mBom dia! Qual o valor da casa que o senhor(a) gostario de comprar? -->\033[m'))
s=float(input('\033[35mCerto! E qual seu sálario? -->\033[m'))
a=float(input('\033[35mE em quantos anos o senhor gostaria de pagar? -->\033[m'))
p=float(v/(a*12))

if p<0.30*s:
    
    print(f'\033[36mOk, se o senhor estiver de acordo com a parcela de {p:.2f}')
    print('\033[33mAdiantaremos os papeis do seu emprestimo!\033[m')
    
else:
    
    print('\033[31minfelizmente seu emprestimo foi negado\033[m')