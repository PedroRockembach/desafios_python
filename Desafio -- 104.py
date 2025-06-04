from os import system
system("cls")
def leiaINT(msg):
    ok = False
    valor = 0
    while True:
        n=str(input(msg))
    
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print(f"\033[31mERRO! Digite apenas inteiros.\033[m")
        if ok:
            print(f"\033[32mDado correto\033[m")
            break
    return valor
n = leiaINT('Digite um numero inteiro ')

    