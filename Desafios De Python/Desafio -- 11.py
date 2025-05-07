##ler altura e largura e calcular area e a quantidade de tinta utilizada para  pinta-la
##cada lada de tinta pinta uma area de 2metros quadrados
import os 
os.system('cls')
H=float(input('Qual a altura da sua parede? '))
L=float(input('E qual a largura da parede?' ))
A=H*L
latas=A/2
print(f'Então, a aréa da sua parede é de \033[1;35m{A}\033[m e seriam usadas \033[7;40m{latas}\033[m latas de tinta para preenche-la.')
