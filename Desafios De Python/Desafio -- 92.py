import os 
from datetime import datetime
from time import sleep

os.system("cls")

#faça um programa que cadastre uma pessoa e pergunte: nome, ano de nascimento e ctps(se o usuario digitar 0 significa que o mesmo não possui.)
#os itens devem ser cadastrados em um dicionario e se, o ctps for diferente de 0 o mesmo deve pedir ano de contratação e salario. 
# o mesmo deve calcular a idade e quando vai ser a aposentadoria da pessoa 

__trabalador__ = {"nome":[],"idade":[],"ctps":[],"aposenta":[],"salario":[]}
__today__ = datetime.now().year

nome = str(input("Digite o seu nome: "))

idade = int(input("Digite seu ano de nascimento: "))
idade = __today__ - idade

ctps = int(input("Possui carteira de trabalho? Se sim digite seu numero, se não digite 0: "))

if len(str(ctps)) < 6 and ctps != 0 :
    
    while len(str(ctps)) <6 and ctps != 0:
        print("="*20)
        print("Digitos insuficentes, digite 6 digitos ou 0.")
        ctps = int(input("Possui carteira de trabalho? Se sim digite seu numero, se não digite 0: "))
    
__trabalador__["nome"].append(nome)
__trabalador__["idade"].append(idade)
__trabalador__["ctps"].append(ctps)

if ctps != 0:
    
    contrato = int(input("Quando você foi contratado? "))
    aposenta = idade + contrato + 35 - __today__
    
    salario = float(input("Qual seu salario? "))
    
    __trabalador__["aposenta"].append(aposenta)
    __trabalador__["salario"].append(salario)
    
    sleep(2)
    print('CARREGANDO...')
    sleep(2)
    
    print(f'''
          
Nome: {__trabalador__["nome"][0]}
Idade: {__trabalador__["idade"][0]} Anos.
Ctps: {__trabalador__["ctps"][0]}
Salario:R${__trabalador__["salario"][0]:.2f}
Aposentadoria: {__trabalador__["aposenta"][0]} Anos.
''')
    
else: 
    print("="*20)
    print(f"Nome: {__trabalador__["nome"][0]}\nIdade: {__trabalador__["idade"][0]}")
    