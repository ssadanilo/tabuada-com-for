numero = int(input('Digite um número entre 1 a 10: ')) # Escolha o número para ser feita a tabuada

# Loop For para criar a tabuada, aninhada no if
if 1 <= numero <= 10:
    print(f'Sua tabuada do número {numero}')
    for i in range(0,11):
        resposta = numero * i
        print(f'{numero} x {i} = {resposta}')
else:
        print('Por favor, informe um número inteiro entre 1 e 10')