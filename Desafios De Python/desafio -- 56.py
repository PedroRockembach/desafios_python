#Desenvolva um programa que pergunte a quatro pessoas as seguintes informaçoes:
#nome, idade, e sexo
#O programa deve nos retornar: a média de idade do grupo todo/Qual NOME do homem mais velho e quantas mulheres tem menos de 20 anos

import os 
os.system('cls') 
from time import sleep

#Variaveis Declaradas:

imax=0         #Idade maxima             
nvelho=''      #Nome maior(homem mais velho)
media=0        #Media das idades
nmulheres=0    #Numero de mulheres maiores de 20         

#Entrada do programa.

print('-=-'*15,'\n\033[35mBem vindo ao analisador completo.\033[m           |')
sleep(4)
print('\033[35mCarregando...\033[m                               |')
sleep(3)
print('\033[35mInsira os dados abaixo:\033[m                     |')

#for que conta de 1 a 4

for c in range(1,5):
    
    print('-=-'*15)
    n=input(f'Qual o nome do {c}° participante? ').strip()#pergunta nome
    i=float(input(f'Qual idade do {c}° participante? '))#pergunta idade
    g=input(f'Qual genêro do {c}° participante?[F/M]').lower()#pergunta genero
    
    media+=i #soma a idade ao valor de media a cada iteração(por fim divide por 4)

    
    #if que pergunta se o genero é feminino e se a participante tem 20 anos ou mais, se sim adiciona um ao numero de mulheres
    if g =='f':
        if i>=20:
            nmulheres+=1
            
    
    #elif que pergunta se é a primeira iteração e se é homem, se sim define este como o maior                    
    if c == 1 and g in 'Mm':
        imax=i
        nvelho=n  
                
    
    #elif que pergunta se é homem e se a idade do participante é maior que a idade maxima,se sim define este como maior idade e homem mais velho    
    if g in 'Mm' and i>imax:
        imax=i
        nvelho=n    
        
print('-=-'*15)

#saidas do programa 

print(f'O numero de mulheres acima de 20 anos é {nmulheres}')  #mulheres acima de 20
print(f'O homem mais velho é {nvelho}')                        #nome do homem mais velho(Erro aqui, não salva o nome na variavel 'nmaior')
print(f'A media da idade dos participantes é {media/(4)} anos')#media das idades

print('-=-'*15)

    
    