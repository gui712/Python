'''
Faça um programa que peça ao usúario para digitar um número inteiro.
informe se este número é par ou impár. Caso usuario não digite um numero inteiro, inform que não é um número inteiro. 
'''

numero = input("Digite um número inteiro: ")
try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f'O número {numero_int} é par')
    else:
        print(f'O número {numero_int} é impar')
except:
    print('Não foi digitado um número inteiro')
