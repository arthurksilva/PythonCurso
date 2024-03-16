# Só pode fazer emprestimo se for maior de 18 anos

idade = int(input('Qual a sua idade? '))

if idade > 18:
    print('Pode fazzer')
if idade == 18:
    print('Não tem dinheiro')
else:
    print('Menor de idade')
