#Desafio -- 97
import os 
os.system("cls")

def escreva(frase):
    
    t = len(frase)+4
    print("-"*(t))
    print(f'{frase:^{t}}')
    print("-"*(t))
    
frase = input("digite uma frase: ")
escreva(frase)



