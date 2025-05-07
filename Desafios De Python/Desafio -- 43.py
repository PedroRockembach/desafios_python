#faça uma logica de programacao que leia altura e peso e calcule imc e mostre seu status de acordo com os dados fornecidos
#abaixo de 18.5- abaixo do peso
#entre 18.5 e 25- peso ideal
#entre 25 e 30- sobrepeso
#entre 30 e 40- obesidade
#acima de 40-obesidade morbida

import os

os.system('cls')

altura=float(input('Bom dia, Qual sua altura? -->'))
peso=float(input('E qual seu peso?'))
imc=peso/altura**float(2)

print(f'Seu imc é {imc:.2f}')

if imc<18.5:
    
    print('Se cuide! Seu imc está ABAIXO DO PESO, você pode estar em desnutrição')
    
elif 18.5<imc<25:
    
    print('Parabéns, você esta no peso IDEAL.')
    
elif 25<imc<30:
    
    print('Você está em SOBREPESO. Se cuide ou poderá desenvolver doenças como a diabetes. Não desista.')
    
elif 30<imc<40:
    
    print('Você está em OBESIDADE, você precisa se cuidar com a ajuda de profissionais como nutricionistas e começar uma rotina de treinos.')

elif imc>40:
    
    print('Você corre perigo, seu imc indica OBESIDADE MORBIDA, você precisa ir atrás de ajuda imediatamente, seu estado pode lhe levar a doenças fatais.')
