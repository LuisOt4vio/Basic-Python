numero = input('Digite um número: ')

try:
    print(f'{numero}(numero) é uma string')
    numero_float = float(numero)
    print(f'{numero_float}(numero float) é um float')
    print(f'O dobro de {numero} é {numero_float*2} ')
except:
    print('Não é um digito válido.')