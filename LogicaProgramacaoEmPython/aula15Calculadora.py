numero_um = 0
numero_dois = 0
soma = 0
aux = 0
opcao = 1

while opcao != 0:
    numero_um = int(input('Digite um numero..: '))
    numero_dois = int(input('Digite um numero..: '))
    aux = numero_um + numero_dois
    soma = soma + aux
    opcao = int(input('Deseja continuar? 1-SIM / 0-NÃO'))
print('A soma dos valores..: {0}'.format(soma))
