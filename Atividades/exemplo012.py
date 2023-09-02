#Dicionario dentro de dicionario

contatos = {
    "Clark Kent":{
        "celular":"123456",
        "email":"clark@super.com"
    },
    "Bruce Wayne":{
        "celular":"7454321",
        "email":"bat@morcegao.com"
    }
}

for nome, formas_contatos in contatos.items():
    print(f'O contato {nome}')
    for forma, valor in formas_contatos.items():
        print(f'Pode ser contatado pelo seu {forma} através do {valor}')
    
    print("\n\n")