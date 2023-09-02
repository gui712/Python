#Criando dicionario

dicionario = {
    "Yoda":"Mestre Jedi",
    "Mace Windu": "Mestre Jedi",
    "Anakil Skywalker": "Cavaleiro Jedi",
    "R2-D2":"Dróide",
    "Dex":"Balconista"
    }

#print(f'O objeto criado é do tipo {type(dicionario)}')
#print(dicionario["R2-D2"])

#for valor in dicionario.values():
#    print(valor)
print(dicionario.values())
#for chave in dicionario.keys():
#    print(chave)
print(dicionario.keys())
print(dicionario.items())
for chave, valor in dicionario.items():
    print(f'O Personagem {chave} é da categoria {valor}')