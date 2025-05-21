import random
num = random.randint(1,500) 

print(num)

lista_um = []
num = str(num)
resultado = ""
for numero in num:
    lista_um.append(numero)
lista_um.sort(reverse = True)
for element in lista_um:
    resultado+=element

print(int(resultado))