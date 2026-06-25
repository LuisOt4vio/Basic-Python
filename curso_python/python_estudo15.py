while True:
    try:
        numero_1 = input('Digite o primeiro valor: ')
        nmr1 = float(numero_1)
        numero_2 = input('Digite o segundo valor: ')
        nmr2 = float(numero_2)
        equacao = input('Digite qual equeação quer utilizar: ')
        operador_permitido = '+-*/'
        operador_valido = equacao in operador_permitido
        if operador_valido:
            vezes = equacao == '*'
            mais = equacao == '+'
            menos = equacao == '-'
            divisao = equacao == '/'
            if vezes:
                resultado = nmr1*nmr2
            elif mais:
                resultado = nmr1+nmr2
            elif menos:
                resultado = nmr1-nmr2  
            elif divisao:
                resultado = nmr1/nmr2
            print(f'{nmr1} {equacao} {nmr2} =',resultado)
        else:
            print('Operador invalido!')
        
        sair = input('Você deseja sair? [S]im ').upper().startswith('S')
        if sair:
            break
    except:
        print('Isso não é um número!')       