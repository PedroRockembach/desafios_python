from os import system
system("cls")

def leiaINT(msg):
    
    while True:
        n=str(input(msg))
        try:
            if n.isnumeric():
                print(f"\033[32mDado Aceito.\033[m")
                valor=int(n)
                return valor
        except: (ValueError,TypeError)
        else:
            print(f"\033[31mERRO! Digite apenas inteiros.\033[m")

def leiaFLOAT(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError,ValueError):
            print(f'\033[31mDigite um numero real valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('O usuario parou de transmitir valores.')
            return 0
        else:
            return n
        

n = leiaFLOAT('Digite um FLOAT: ')
print(f'o valor digitado foi {n}')

    