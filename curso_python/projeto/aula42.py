''' 
listas em py:
métodos úteis: append, insert, pop, del, clear, extend
Create, read, Update, Delete
'''
lista = [10, 20, 30, 40]

#lista[2] = 300
#del lista[2]
#print(lista[2])
lista.append(50) #append adiciona algo ao final da lista
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop() #pop remove o ultimo
print(lista, 'Removido: ', ultimo_valor)