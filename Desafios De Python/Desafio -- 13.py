#Insira o valor de um salario e ele te retornara o salario+15%
import os
os.system('cls')
salario=float(input('Qual o seu sálario? -->'))
aumento=float(salario+salario*0.15)
print('parabéns, seu novo salario é de \n --->\033[1;35m{}'.format(aumento))