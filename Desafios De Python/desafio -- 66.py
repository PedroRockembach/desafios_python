#refaça o desafio 64 agora utilizando o while true e break 

import os 

os.system('cls')

somador = contador = media = 0

while True:
    
    s=int(input('Digite um valor inteiro [999 para parar]: '))
    
    if s == 999:
        break
    
    somador+=s
    contador+=1
media = somador/contador  
  
print(f'A soma entre os {contador} é igual a {somador} e a media entre eles é {media}')
    