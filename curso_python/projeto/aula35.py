''' while/ else'''

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    print(letra)

    i+= 1
else:
    print('O else dentro do while executado.')

print('Fora do While!!')