#while loop
import random
import os 
os.system('cls')
c=1        
print('advinhe o numero que estou pensando, o numero estara entre um e dez, voce tem 5 chances')
p=random.randint(1,10)
print(p)
a=1
while a<6:
    c=int(input('Faça sua tentativa:'))
    a+=1
    if c==p:
       print('Voce me venceu')
       
    else:
        print('Voce não acertou')
print('Voce perdeu')
