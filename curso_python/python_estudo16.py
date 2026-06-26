frase = input('Digite uma frase: ')
i = 0 ; j = 0
cont_letra_vezes = 0
letra_apareceu_mais = ''
letra_apareceu_mais_vezes = ''
nova_string = ''
novo_nome = ''
while i < len(frase):
    atual_letra = frase[i]
    cont_letra = frase.count(f'{atual_letra}')

    if atual_letra == ' ':
        i+=1
        continue

    if cont_letra == cont_letra_vezes and atual_letra not in letra_apareceu_mais:
            letra_apareceu_mais += atual_letra

    if cont_letra > cont_letra_vezes:
        cont_letra_vezes = cont_letra
        letra_apareceu_mais = atual_letra

    i += 1

qntd = len(letra_apareceu_mais)

while j < qntd:
    nova_string = f'{letra_apareceu_mais[j]}' 
    novo_nome += nova_string
    if j < qntd-1:
        novo_nome += ','      
    j+=1            



if qntd >= 2:     
    print(f'As letras que mais apareceram foram ({novo_nome}) tendo um total de {cont_letra_vezes}x cada uma delas.')
else:
    print(f'A letra que apareceu mais vezes foi ({letra_apareceu_mais}) tendo um total de {cont_letra_vezes}x.')
     