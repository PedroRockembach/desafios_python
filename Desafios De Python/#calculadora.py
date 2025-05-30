#calculadora

import os 
os.system("Cls")

#projeto de uma calculadora

def soma(*num):
    resultado = 0
    for i in num:
        resultado += i
    print(resultado)



num_1 = int(input("num: "))
os.system("cls")
num_2 = int(input("num: "))