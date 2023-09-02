# Uma introdução sobre f-string
# f string usamos o f'' para formar o numero de casas decimais
# fo usado o após a variável o :.numero de casasf 

nome = 'Guilherme Costa'
altura = 1.70
peso =  65

imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura '
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)