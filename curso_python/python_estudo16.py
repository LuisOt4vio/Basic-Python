frase = input('Digite uma frase: ')
i = 0
cont_letra_vezes = 0
letra_apareceu_mais = ''
letra_apareceu_mais_vezes = ''
while i < len(frase):
    atual_letra = frase[i]
    cont_letra = frase.count(f'{atual_letra}')

    if atual_letra == ' ':
        i+=1
        continue

    if cont_letra > cont_letra_vezes:
        cont_letra_vezes = cont_letra
        letra_apareceu_mais = atual_letra

    i += 1
 
print(f'A letra que apareceu mais vezes foi ({letra_apareceu_mais}) tendo um total de {cont_letra_vezes}x')