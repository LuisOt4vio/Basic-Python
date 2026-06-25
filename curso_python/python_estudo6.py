nome = 'Luís Otávio'
preco = 1000.504555
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04X' % (1765, 1765))
print('O hexadecimal de %d é %04x' % (1765, 1765))

variavel = 'LUIS'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.872837213702793472794:0=+10,.2f}')
print(f'O hexadecimal de 1765 é {1765:08X}')