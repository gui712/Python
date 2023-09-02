# Operadores lógicos
# and (e) or (ou) not (não)
# and = todas as condições precisam ser verdadeiras.
# se qualquer valor for considerado falso, a experessao inteira sera
# são considerados falsy == 0 0.0 '' False
# None é represantar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E'and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

#avaliação de curto circuito ele para de avaliar ao encontrar o primeiro valor falso
print(True and True and False and True)

#if 0 and 1:
#    print(True and 1)

#if 1 and 1:
#    print(True and 1 and False)

