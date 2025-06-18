matriz = [[],[],[]]
for c in range (1,10):
    
    valor = int(input(f'Digite o {c}ª valor: '))
    if c <=3 :
        matriz[0].append(valor)
    elif c <= 6 :
        matriz[1].append(valor)
    else:
        matriz[2].append(valor)
        
print('=-'*20)
for i in range(3):
    print(f'{matriz[0][i]}',end='    ')
print("\n")
for i in range(3):
    print(f'{matriz[1][i]}',end='    ')
print("\n")
for i in range(3):
    print(f'{matriz[2][i]}',end='    ')