# Continuando com os operadores lógicos
# Operador or
# Diferente do and ele precisa de uma condição verdadeira

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True or False or 0 or True)
print(False or False or 0 or True)