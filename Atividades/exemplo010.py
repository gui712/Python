dicionario = {}

#incluindo dados no dicionario
dicionario["André David"] = "Professor"

#pedindo para o user add dados

nova_chave = input("Informe o nome do colaborador: ")

novo_valor = input("Informe a função do colaborador: ")

dicionario [nova_chave] = novo_valor

for chave, valor in dicionario.items():
    print(f"O colaborador {chave} desempenha a função de {valor}")
