# Função format

a = 'AAaAa'
b = 'BbbB'
c = 1.1
formato = 'aa={} b={} C={:.2f}'.format(a, b, c)

print(formato)

nome ='Luiz'
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))

nome2 ='Gui'
idade2 = 24
formato2 = '{n} tem {i} anos'
print(formato2.format(n=nome2, i=idade2))

nome3 ='Guilherme'
idade3 = 25
formato3 = f'{nome3} tem {idade3:.2f} anos'
print(formato3)

numero_1 = 10
numero_2 = 20
resultado = numero_1 * numero_2
print(resultado)