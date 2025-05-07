import os 

#fala numero por extenso

os.system("cls")

numeros = ('zero','um', 'dois', 'tres', 'quatro','cinco','seis','sete', 'oito', 'nove', 'dez','onde','doze','treze', 'quatorze', 'quinze', 'dezesseis','dezessete','dezoito','dezenove','vinte' )

while True:
    
    #entrada do valor requisitado
    
    escolha = int(input("Digite um numero de 1 a 20: "))
    
    if escolha<0 or escolha>20:
        
        #print a frase "tente novamente" para limitar o intervalo que o usuario pode digitar
        
        print("Tente novamente", end = ', ')
        
    else:
        
        #printa o numero que o usuario digitando, o encontrando na tupla e citando a idexação pelo numero do usuario
        
        print(f'Você digitou o número {numeros[escolha]}')
        break
         



