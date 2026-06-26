texto = 'python'
nova_string = ''
for letra in texto:
    nova_string += f'*{letra}'
    print(letra)
print(nova_string + '*')

#------------------------------------

"""
For + Range
range -> range(start, stop, step)
"""
numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)

#------------------------------------

"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luis Otávio'  # iterável

iteratador = iter(texto)  # iterator

while True:
    try:
         letra = next(iteratador)
         print(letra)
    except StopIteration:
         break

for letra in texto:
    print(letra)