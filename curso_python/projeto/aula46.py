''' for in com lista '''

lista =['Rute', 'Carolina', 'Bete', 'Josefina','Maria']
lista.append('Camila')

#for letra in 'ABCDEF':
#    print(letra)

i = 0;
for nome in lista:
    print(i, nome, type(nome))
    i+=1

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])