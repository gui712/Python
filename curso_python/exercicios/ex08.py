'''
Interando Strings com while 
'''

nome = "Guilherme Costa"

tamanho_nome= len(nome)
print(nome)
print(tamanho_nome)

print(nome[3])

contador = 0
novo_nome = ''
while contador < tamanho_nome:
    letra = nome[contador]
    novo_nome += f'* {letra}'
    contador += 1
novo_nome += '*'

print(novo_nome)