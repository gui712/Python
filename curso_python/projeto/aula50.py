'''
Enumerate - enumera iteráveis(indices)
'''
# O enumerate serve para isso enumerar uma lista
# [(0, 'Maria'), (1, 'Helena'), (2, ' Luiz'), (3, 'Joanna')]
lista = ['Maria', 'Helena', ' Luiz']
lista.append('Joanna')

lista_enumerada = list(enumerate(lista))    

print(lista_enumerada)

for indice, nome in enumerate(lista):
    print(indice, nome)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)