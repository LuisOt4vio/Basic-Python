"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

usuario_numero_digitado = input('Digite um número inteiro: ')

try:
    usuario_numero_inteiro = int(usuario_numero_digitado)
    numero_par_ou_impar = usuario_numero_inteiro % 2 == 0
    if numero_par_ou_impar:
        print('Par')
    else:
        print('Impar')
except:
    print('Não foi digitado um numero inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
digite_a_hora = input('Digite o horario: ')

try:
    hora_positivo = int(digite_a_hora)
    hora_digitada = hora_positivo >= 0 and hora_positivo < 24 
    if hora_digitada:
        saudacao_apropriada_bom_dia =  hora_positivo <= 11
        saudacao_apropriada_boa_tarde =  hora_positivo > 11 and hora_positivo <= 17
        saudacao_apropriada_boa_noite =  hora_positivo > 17 and hora_positivo <= 23
    if saudacao_apropriada_bom_dia:
            print('Bom dia!')
    elif saudacao_apropriada_boa_tarde:
            print('Boa tarde!')
    elif saudacao_apropriada_boa_noite:
            print('Boa noite!')
except:
    print('Horario digitado não corresponde')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

try:
    nome_usuario = input('Digite seu nome: ')
    contagem_nome_usuario= len(nome_usuario)
    curto_nome = contagem_nome_usuario >= 0 and contagem_nome_usuario <=4
    medio_nome = contagem_nome_usuario >=5 and contagem_nome_usuario <=6
    grande_nome = contagem_nome_usuario > 6 
    if curto_nome:
        print('Seu nome é curto')
    if medio_nome:
        print('Seu nome é normal')
    if grande_nome:
        print('Seu nome é muito grande')
except:
    print('Nome digitado invalido')
