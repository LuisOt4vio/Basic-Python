"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

condicao = True

while condicao:
    nome = input('Qual seu nome? ')
    print(f'Seu nome é {nome}')
    condicao += 1
    if condicao == 10:
        condicao = False