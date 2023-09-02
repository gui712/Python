'''
Listas em py 
Concatena lista e extend
'''

lista_a = [1,2,3, 8]
lista_b = [4, 5, 6 , 9]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)

print(lista_c)
print(lista_a)