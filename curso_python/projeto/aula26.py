'''
Constante = "Variáveis" que não vão mudar normalmente quando queremos indicar aldo que não vai mudar no codigo usamos letras maisculas
Muitas condições no mesmo if (ruim)
<- contagem de complexidade (ruim)
'''
velocidade = 65 # velocidade atual do carro
local_carro = 99 # local em que o carro está na estrada

RADAR_1 = 60 #velocidade káxima do radar 1
LOCAL_1 = 100 #Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
print(velocidade_carro_passou_radar_1)

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
print(carro_passou_radar_1)

carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1
print(carro_multado_radar_1)

if velocidade_carro_passou_radar_1:
    print('Velocidade do carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou no radar 1')

if carro_multado_radar_1:
    print('Carro passou no radar 1 acima do lime permitido!')
