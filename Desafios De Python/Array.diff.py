lista  = [1,2,2]
lista1 = [1]
listasaida = []
for item in lista:
    if item not in lista1:
        listasaida.append(item)
print(listasaida)