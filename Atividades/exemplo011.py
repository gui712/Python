#exemplos de remoção de dados em dicionario

dicionario = {
    "Yoda":"Mestre Jedi",
    "Mace Windu": "Mestre Jedi",
    "Anakin Skywalker":"Cavaleiro Jedi",
    "R2-D2" : "Dróide",
    "Dex" : "Balconista"
}

for chave, valor in dicionario.items():
    print(f'O personagem {chave} é da categoria {valor}')

#removendo item pela chave

dicionario.pop("R2-D2")
print('-------------')

for chave, valor in dicionario.items():
    print(f'O personagem {chave} é da categoria {valor}')

#Removendo o ultimo item do dicionario
dicionario.popitem()

print('/////////////////////')

for chave, valor in dicionario.items():
    print(f'O personagem {chave} é da categoria {valor}')

#Remover todos os items do dicionario

dicionario.clear()

print(dicionario)