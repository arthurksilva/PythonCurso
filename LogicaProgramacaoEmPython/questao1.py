print('Verificar se o númeor é par ou impar. OBS..: Tem que ser um número inteiro')
numero_um = input('Digite um númeoro..: ')

if numero_um.isnumeric():
    numero_um = int(numero_um)
    if numero_um % 2 == 0:
        print('O número {0} é par'.format(numero_um))
    else:
        print('O número {0} é impar'.format(numero_um))
else:
    print('Erro - Algum número não é válido')
