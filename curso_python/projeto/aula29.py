'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito -> quando um código não tem fim. 
'''

condicao = True

while condicao:
    nome = input('Qual é o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou!!!!')