# https://pt.wikipedia.org/wiki/Ano_bissexto#Calend%C3%A1rio_Gregoriano

# Sua missão: escrever um programa que recebe o número de um ano, e determina se
# ele é ou não bissexto

# suas ferramentas:
# * if, elif, else
# * operador modulo: para saber se um número é multiplo de 4, podemos fazer
# n%4. Isso devolve o resto da divisão por 4. Se esse resto for zero, o número
# é multiplo de 4
# * converter string para numero:
# a = input("digite o ano") resulta uma string, um texto, como "1984"
# a = int(input("digite o ano")) um número, como 1984

a = int(input("digite o ano"))
print(a % 4)
if a % 4 == 0:
    print("o numero {} é multiplo de 4".format(a))
