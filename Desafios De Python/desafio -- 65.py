import os 
os.system('cls')

#Crie um programa que leia varios numeros inteiros pelo teclado e por fim mostre a media entre todos eles, 
#apos ele dira qual foi o menor e maior valor lido e a cada iteração o programa deve perguntar se o usuario gostaria de continuar

soma = cont=0
maior = float('-inf')
menor = float('+inf')

while True:
    
    print('-=-'*20)
    n=int(input('Digite um valor inteiro: '))
    
    if n>maior:
    
        maior=n
    
    if n<menor:
    
        menor=n
    
    p=str(input('Você deseja continuar?[S/N]'))
    
    soma+=n 
    cont+=1
    
    if p in 'ssimSSim':
    
        continue
    
    else:
        print('\033[31mFinalizando...\033[m')
        break

print('-=-'*20)
    
media=soma/cont 
 
print(f'A mêdia entre estes valores é de: \033[36m{media:.2f}\033[m, o maior valor é de {maior} e o menor é {menor}')