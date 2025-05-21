#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
import os
os.system('cls')

celsius=float(input('Digite um valor determinado em graus \033[36mcelsius -->'))
fahrenheit = celsius*(9/5)+int(32)
print(f'O seu valor em graus fanrenheit é de \033[1;31m{fahrenheit}\033[m')