import sys

#normalmente usamos tuplas quando sabemos o numero de elementos e o tamanho 
categorias = ("Padawan", "Knight" , "Master")

teste1, teste2, teste3 = categorias
# essa técnica é chama de desempacotamento 
print(teste1)

print(f'O tipo de é {type(categorias)} e tem {sys.getsizeof(categorias)} bytes. ')

for categoria in categorias:
    print(categoria) 