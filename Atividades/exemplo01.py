import sys
#importando o modulo sys

nome = "Bruce Wayne"

idade = 30

peso = 92.3

print(f'A variavel nome é do tipo {type(nome)} e tem bytes {sys.getsizeof(nome)}')
print(f'A variavel nome é do tipo {type(idade)} e tem bytes {sys.getsizeof(idade)}')
print(f'A variavel nome é do tipo {type(peso)} e tem bytes {sys.getsizeof(peso)}')