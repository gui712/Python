''' 
introdução ao desempacotamento
'''

nomes = ['Maria', 'Helena', 'Luiz']

#precisa ter o mesmo numero de variaveis que lista caso queira desempacotar um valor
nome1, nome2, nome3 = nomes

numeros = [10, 17, 92 , 98, 96]
# neste caso a variavel *_ serve para armazenar o resto dos valores indica que não vamos usar ela _
numero1, *_ = numeros


print(nome2 , numero1)