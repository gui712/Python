#função input para coleta de dados do usuario
# sempre retorna uma string
nome = input('Qual é o seu nome? ')
print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
# o resultado é a concatenação entre os dados por ser duas string
print(f'A soma dos números é: {numero_1 + numero_2}')
# fazendo a conversão dos tipos
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A Soma dos números é = {int_numero_1 + int_numero_2}')