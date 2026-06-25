#identificador = id
#o python se for a mesma variavel == valor, ele vai retornar o mesmo id da memoria, diferentes vai mudar.
variavel1 = 'a'
variavel2 = 'a'

print(f'{id(variavel1)}\n{id(variavel2)}')


"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
