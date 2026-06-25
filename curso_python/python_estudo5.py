entrada = input('[E]ntrar [S]air ')
senha_digitada = input('Digite sua senha: ')

senha_permitida = '123'

if (entrada == 'E' or entrada == 'e') and not senha_digitada == senha_permitida: #not serve para inverter o valor boolean
    print('Você entrou!')
elif entrada == 'S' or entrada == 's':
    print('Você saiu!')
else:
    print('Não digitou S nem E!')

#----------------------

nome = 'Luis Otávio'
print('t' in nome)
print('Luis' not in nome)


nome = input ('Digite o seu nome: ')
encontre = input ('Digite oque deseja encontrar: ')

if encontre in nome:
    print (f'{encontre} está dentro de {nome}')
else:
    print (f'{encontre} não está dentro de {nome}')