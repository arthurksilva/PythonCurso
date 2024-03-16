from os import system
from turtle import end_fill


saudacao_do_usuairo = input('Que horas são? ')
nome_do_usuairo = input('Qual o seu nome? ')

if saudacao_do_usuairo.isnumeric():
    print(' Seja bem-vindo \n')
    saudacao_do_usuairo = int(saudacao_do_usuairo)
else:
    print('Não é número -> {0}'.format(saudacao_do_usuairo))
    exit(0)

if 0 <= saudacao_do_usuairo <= 11:
    print('Bom-dia, {0}'.format(nome_do_usuairo))
if 12 <= saudacao_do_usuairo <= 17:
    print('Bom-tarde, {0}'.format(nome_do_usuairo))
if 18 <= saudacao_do_usuairo <= 23:
    print('Bom-noie, {0}'.format(nome_do_usuairo))
