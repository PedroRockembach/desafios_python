import os
os.system('cls')
metamorfose=('''Quando Gregor Samsa acordou de sonhos inquietos, encontrou-se em sua cama transformado em um inseto monstruoso. 
Ele estava deitado de costas, como uma casca dura, e ao erguer a cabeça, viu o segmento arqueado de seu ventre, 
franzido e pálido, e, para sua surpresa, o pensou com uma espécie de preocupação.''')
#print(metamorfose.replace(' ','-').upper())
novo=('euu deixei cair minha caneta')
print(novo.split())
print(novo[0:])
print(novo[4:])
print(novo.find('i'))
n1=novo.replace('euu','eu')
print(n1.upper())
n2=('    eU deiXeI meu láPIS com mAtheus    ')
n2corrigido=n2.rstrip().capitalize()

a=(n2corrigido.split())
print('$'.join(a))
print(a[2][3])

