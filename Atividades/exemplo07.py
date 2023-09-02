#Criando duas listas

personagens = []
categorias = []

for x in range(3):
    personagens.append(input("Informe o nome do personagem: "))
    categorias.append(input("Informe a categoria do personagem: "))

for indice in range(3):
    print(f'O personagem {personagens[indice]} é um {categorias[indice]}')