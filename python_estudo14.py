string = input('Digite seu nome: ')
tamanho_string = len(string)
nova_string = ''
novo_nome = ''
i = 0
try:
    while i < tamanho_string:
            nova_string = f'*{string[i]}' 
            novo_nome += nova_string       
            i+=1      
    novo_nome += '*'
    print(novo_nome)             
except:
    pass  

