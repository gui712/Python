# Operadores in e not in
# Strings são iteráveis(pode navegar por index)
# O t á v i o
# 0 1 2 3 4 5
# -6 -5 -4 -3 -2 -1

nome = 'Otávio'

print(nome[2])
print(nome[-5])

print('á' in nome)
print('z' in nome)
print(10 * '-')
print('vio' not in nome)
print('zero' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

variavel_a = 1 or 0
variavel_b = 0 or 1

print(variavel_a, variavel_b)

nome_2 = 'Maria Carmo'
if ' ' in nome:
    print(f'o nome {nome_2} tem espaços.')
else:
    print(f'o nome {nome_2} não tem espaços.')
