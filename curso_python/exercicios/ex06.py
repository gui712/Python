'''
Faça um programa que a hora ao usuário e, baseando-se no horario descrito, exibaa saudação apropriada. Ex.
bom dia 0 - 11, boa tarde 12 - 17 e boa noite 18 - 23  
'''

hora = input('Digite que horas são: ')
try:
    hora_int = int(hora)

    if hora_int >= 0 and hora_int <= 11:
        print('Olá, bom dia!!')
    elif hora_int >= 12 and hora_int <= 17:
        print('Olá, boa tarde!!')
    elif hora_int >= 18 and hora_int <= 23:
        print('Olá, Boa noite')
    else:
        print("Hora digitada inválida!!")
except:
    print("Não foi digitado um número inteiro!!")
