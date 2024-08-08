umidade_int = 40
temperatura_ext = 14

temperatura_int = temperatura_ext - 1
botao_pronto = 'OFF'
exaustor = 'OFF'
aquecimento = 'OFF'

# Programa principal

# Estado pré uso
print('\nEstado do aquecimento: ', aquecimento)
print('Estado do exaustor: ', exaustor)
print('A temperatura interna é de: ', temperatura_int, 'Cº')
print('A temperatura externa é de: ', temperatura_ext, 'Cº')
print(f'A umidade interna é de: {umidade_int:.1f} %')

if temperatura_ext <= 20:
    print('Iniciando desumidificação...')


def desumidificacao(temp_int, umid_int):
    global aquecimento
    global exaustor
    if temp_int > 15 and umid_int >= 40:
        exaustor = 'ON'
    elif temp_int < 15 and umid_int >= 40:
        exaustor = 'ON'
        aquecimento = 'ON'
        print('Aquecendo...')
    while aquecimento == 'ON':
        temp_int += 1
        umid_int -= 1
        if temp_int >= 100:
            aquecimento = 'OFF'
        if umid_int <= 5:
            exaustor = 'OFF'
            aquecimento = 'OFF'
            print('Processo de desumidificação encerrado!')
    return temp_int, umid_int

# Estado pós desumidificação


temperatura_int, umidade_int = desumidificacao(temperatura_int, umidade_int)

print('\nEstado do aquecimento: ', aquecimento)
print('Estado do exaustor: ', exaustor)
print('A temperatura interna é de: ', temperatura_int, 'Cº')
print('A temperatura externa é de: ', temperatura_ext, 'Cº')
print(f'A umidade interna é de: {umidade_int:.1f} %')

# Programa principal
if temperatura_ext <= 20:
    desumidificacao(temperatura_int, umidade_int)


# Cocção

if umidade_int > 15:
    exaustor = 'ON'
if temperatura_int < 200:
    aquecimento = 'ON'
    while aquecimento == 'ON':
        temperatura_int += 2
        if temperatura_int >= 379:
            aquecimento = 'OFF'

print('\nEstado do aquecimento: ', aquecimento)
print('Estado do exaustor: ', exaustor)
print('A temperatura interna é de: ', temperatura_int, 'Cº')
print('A temperatura externa é de: ', temperatura_ext, 'Cº')
print(f'A umidade interna é de: {umidade_int:.1f} %')
