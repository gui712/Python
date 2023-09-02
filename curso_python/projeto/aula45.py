''' 
Cuidado com dados mutaveis
= - copiando o valor (imutaveis)
= - apontando para o mesmo valor na memoria (mútavel)
'''

lista_a = ['Luiz', 'Joana', 1, True, 10.7]
lista_b = lista_a.copy()

lista_a[0] = 'Guilherme'

print(lista_a)
print(lista_b)
 