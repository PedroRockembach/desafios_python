#Crie um analisador de pessoas, ele deve perguntar: idade e sexo, além disso, o programa deve perguntar a cada 
#pessoa cadastrada se o usuario quer contininuar ou não 
#por fim, o programa deve nos voltar as seguintes informações: quantas pessoas tem mais de dezoito anos,
#quantos homens foram cadastrados e quantas mulheres tem menos de 20 anos.

import os 
os.system('cls')

cont = 1
idade = homens = pessoavelha = menosvinte = 0

print('-'*20)
print('Analisador v.4')
print('-'*20)

while True:
    
    print('='*20)
    
    print(f'{cont}° Pessoa')
    idade=int(input('Qual a idade dessa pessoa?'))
    sexo=str(input('Qual genero dessa pessoa?[H/M]')).lower().strip()
    
    cont += 1
    
    if sexo not in 'hm':
        print('Opção inválida! Por favor digite H ou M.')
        continue
    
    if idade >= 18:
        pessoavelha += 1
        
    if sexo == 'm' and idade < 20:
        menosvinte += 1
        
    if sexo == 'h':
        homens += 1
    maisum = str(input('Deseja continuar?[Y/N]')).lower().strip()
    if maisum == 'n':
        print(f'O numéro de homens cadastradas foi {homens}, o numéro de mulheres com menos de vinte anos é {menosvinte} e o numero de pessoas com mais de dezoite anos foi de {pessoavelha}')
        break
        
    
        