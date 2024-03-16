nome = input('Qual o seu nome? ')
qtd_de_letras_do_nome = len(nome)

if 4 <= qtd_de_letras_do_nome < 5:
    print('Seu nome é curto')
elif 5 <= qtd_de_letras_do_nome <= 6:
    print('Seu nome é normal')
elif 7 <= qtd_de_letras_do_nome:
    print('Seu nome é grande')
