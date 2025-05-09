dados = dict()
dados = {'nome':"Pedro","idade":"25"}
print(dados['nome'])
print(dados['idade'])

#adiciona elementos a lista

dados['sexo'] = 'M'

#outro metodo de criação de dicionarios 
filmes = {
    'titulo': 'Star Wars',
    'ano':'1977',
    'diretor': 'George Lucas'        
            
        }
#os valores dentro do dicionario ex: Star wars, 1977 e George lucas, chamamos de VALORES
#ja os nomes de cada partição ex: titulo, ano e diretor, chamamos de CHAVES
#E o todo é chamado de items

print(filmes.values()) #-> retorna valores de filmes

print(filmes.keys()) #-> retorna valores de chaves

print(filmes.items()) #-> retorna valores de items