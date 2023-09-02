'''
Interável > str, range, etc
Iterador >quem sabeentregar um valor por vez
next > me entregue o próximo valor
iter > me entregue seu iterador 
'''

texto = 'Guilherme' # iterável
iterador = iter(texto) #iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
# Explicação do que o for faz por baixo dos panos 
# for letra in texto
# print(letra)   