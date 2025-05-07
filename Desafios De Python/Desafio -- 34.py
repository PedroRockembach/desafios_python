#calcula aumento de slario

import os

os.system('cls')

s=float(input('qual seu salario?'))

if s>float(1250.00):

    print(s+(s*0.10))

else:

    print(s+(s*0.15))
