''' 
Listas em py
métodos úteis:
    append - adiciona um item ao final
    insert - adiciona um item no índice escolhido
    pop - remove do fina ou do índice escolhido
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
CRUD
'''
lista = [10, 20 , 30 , 40]
lista.append('Gui Ga')
nome = lista.pop()
lista.append(1233)
print(lista, 'Excluido' , nome)
del lista[-1]
lista.insert(0, 5)
print(lista)