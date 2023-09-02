nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')
encontrar =' '

if nome != '' and idade != '':  
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if encontrar in nome:
        print(f'O nome: {nome} contém espaço')
    else:
        print(f'O nome: {nome} não contém espaço')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print(f'Desculpe, você deixou campos vazios')