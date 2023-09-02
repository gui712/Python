# Formatação básica de String
'''
s - string
d - int
f - float
.<casas decimais>f
x ou X hexadecimal
(Caractere) (><^) (quantidade)
> Esquerda
< Direita
^ Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
'''
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{variavel:-^10}.')
print(f'{1000.548962146:.2f}')
print(f'O Hexadecimal de 1500 é {1500:08x}')
