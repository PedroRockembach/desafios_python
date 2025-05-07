##insiro um valor de produto e ele me retorna o produto com um desconto de 5%
import os 
os.system('cls')
preço=float(input('qual o preço disto? '))
desconto=float((preço*0.05))
p=float(preço-desconto)
print(f'\033[36mO produto descrito tem um desconto de \033[1;33m5%\033[m\033[36m, assim ficando o preço final é de \033[1;35m{p}\033[m]')