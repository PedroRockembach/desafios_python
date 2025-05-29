import os 
os.system('cls')
s=0
for c in range(0,4):
    n=int(input('\033[36mdigite um valor:\033[m'))
    s+=n   
    print(s)
print(f'A somatorio dos valores inseridos é de {s}')
#pergunta um valor varias vezes( definido pelo range do for) e a faz a somatoria de todos eles
#usando o "+=" que faz a soma a cada contagem do loop
#s+n==s=s+n