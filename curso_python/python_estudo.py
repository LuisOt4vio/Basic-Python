print (1 + 1, sep=" ? ") # comando "sep" =  separação
print (1, 3, sep=" < ", end=" ## \n") #comando "end" = final do print, pode ser utilizado para quebrar linha/colocar caracter
print (1 + 2, 1, sep=" > ")
print ("Bom dia a \"todes!") #"PULA O CARACTER"
print (type('BATATINHA')) #type é uma class e mostra o tipo de uma informação do código
print (10 == 10) #Tipo boolean True or false
print (10 <= 11)
print (10 >= 11)
print (10 < 9)
print (10 > 4)
print (int('1') + 1)

nome = 'Luis Otávio'
idade = 22
maior_de_idade = idade >= 18
print ('Nome:', nome, 'Idade:', idade)
print ('É maior?', maior_de_idade)
print('\n')
#---------------------

nome = 'Luis Otávio'
sobrenome = 'Costa'
idade = 22
ano_nascimento = 2026 - idade
maior_de_idade = idade >= 18
altura_metros = 1.78

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)
print('\n')
#---------------------

adicao = 10 + 10
print ('Adição:', adicao)

subtracao = 10 - 5
print ('Subtração:', subtracao)

multiplicacao = 10 * 10
print ('Multiplicação:', multiplicacao)

divisao = 10 / 2.43 #float
print ('Divisão:', divisao)

divisao_inteira = 10 // 2.43 #inteira, corta as casas decimais
print ('Divisão Inteira:', divisao_inteira) 

modulo  = 10 % 2.32
print ('Módulo:', modulo)

exponenciacao  = 10 ** 3.5
print ('Exponenciação:', exponenciacao)
#---------------------

print('\n')
concatenacao = 'Luis' + ' ' + 'Otávio'
concatenacao2 = 'Luis' + str('1') + 'Otávio'
print(concatenacao)
print(concatenacao2)

faz_o_l = 5 * 'l'
luis_tres_vezes = 3 * 'luis'
print (faz_o_l)
print (luis_tres_vezes)
#---------------------

print('\n')
'''
1. (n+n)
2. **
3. * /  // %
4. + - 
'''

conta_matematica = (1 + int(0.5 + 0.5 ))** (5 + 5) + 4
print (conta_matematica)
#---------------------
print('\n')

nome = 'Luis Otávio'
altura = 1.78
peso = 78
imc = peso / (altura * altura)

print (nome, 'tem', altura, 'de altura')
print ('pesa', peso, 'quilos e o seu IMC é:')
print(imc)
print('\n')
linha_1 = f'{nome} tem {altura:.2f} de altura' #f strings
linha_2 = f'pesa {peso} quilos e o seu IMC é:'
linha_3 = f'{imc:.2f}'
print (linha_1)
print (linha_2)
print (linha_3)
#---------------------

print('\n')
a = 'A'
b = 'B'
c = 1.1

formato = 'a={} b={} c={}'.format(a, b, c)
print (formato)


string_formato = 'a={0} b={1} c={2:.2f} c={2:.2f} c={nome3:.2f}' #Posso trabalhar com índeces 0,1,2,3 e assim por diante
#sempre que nomeio um parametro para que não de erro eu tenho que nomear o proximo 
formato = string_formato.format(a,b, c, nome3=c) #posso nomear indices, como por exemplo nome3(PARAMETRO), a,b e c são argumentos
print (formato)

#---------------------
