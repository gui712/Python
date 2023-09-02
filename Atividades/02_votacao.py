# https://www.cnnbrasil.com.br/perguntas-frequentes/eleicoes/titulo-de-eleitor/quem-pode-votar-no-brasil/

# Sua missão: receber dados de uma pessoa, e dizer se o voto é
# OBRIGATORIO, FACULTATIVO ou NAO PERMITIDO

# Os dados da pessoa: idade, número inteiro em anos
# Alfabetizado(a): string, com os possiveis valores "SIM" ou "NAO"

# Suas ferramentas:
# * if, elif, else, and e or
# * converter string para numero:
# a = input("digite o ano") resulta uma string, um texto, como "1984"
# a = int(input("digite o ano")) um número, como 1984
# * comparar valores

a = 20
alfa = "NAO"

if a > 10:
    print("ola")  # esse ola so é exibido se a for maior que 10. Se você mudar na linha de cima, ele não será exibido
if alfa == "SIM":
    print("alfabetizado")  # esse alfabetizado so é exibido se a variável alfa tiver a string "SIM"

# Desafio 1: aceite "Sim", "sim" como valores para alfabetizado
# Desafio 2: Reclame se o usuário digitar algo diferente de "sim" e "nao",
# mas aceitando as variações de maiúscula e minúscula
