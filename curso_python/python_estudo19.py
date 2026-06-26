"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

tentativas = 0
palavra_secreta = 'Bolinha'
palavra_secreta_2 = ''
letras_acertadas = ''

for letras in palavra_secreta:
    palavra_secreta_2 += '*'


print(f'Palavra {palavra_secreta_2}, tente adivinhar!')

while True:
    print (f'Quantidade de Tentativas: {tentativas}')
    letra_digitada = input('Digite uma letra: ')
    tamanho_digitado = len(letra_digitada)

    if tamanho_digitado > 1 or tamanho_digitado < 1:
        print('Digite apenas uma letra!')
        tentativas += 1
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'Palavra atual: {palavra_formada}')
        
    tentativas += 1

    descobrir_palavra = input('Deseja digitar a palavra? [S]im [N]ão ').upper()

    if descobrir_palavra in 'S':
        descobriu_palavra = input('Digite a palava caso tenha descoberto: ')
    else:
        continue

    if descobriu_palavra == palavra_secreta:
        print(f'Parabéns você acertou a palavra {palavra_secreta} com {tentativas} tentativas !!!!')
        break
    else:
        print('Você errou a palavra! Tente novamente!')
