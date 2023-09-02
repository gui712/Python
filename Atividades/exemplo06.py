tupla = (1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5)
print(f'A tupla foi criada assim: {tupla}')

#utilizando enumerate para mostrar uma sequencia

for numero, valor in enumerate(tupla):
    print(f'No índice {numero} temos: {valor}')

#mostrando a quantidade de itens na tupla
print(f'Quantidade: {len(tupla)}')

#mostrando o valor mínimo na tupla
print(f'Mínimo: {min(tupla)}')

#mostrando o valor máximo
print(f'Máximo {max(tupla)}')

#mostrando a soma dos valores da tupla
print(f'Soma:{sum(tupla)}')

#utilizando tuple para conversão de uma lista para tupla
lista = [True, False]
print(f'Lista: {lista}')
tupla2 = tuple(lista)
print(f'Tupla: {tupla2}')

tupla3 =(1,0)

print(f'Testando a tupla2 com all: {all(tupla2)}')
print(f'Testando a tupla3 com all: {all(tupla3)}')

print(f'Testando a tupla2 com any: {any(tupla2)}')
print(f'Testando a tupla3 com all: {any(tupla3)}')