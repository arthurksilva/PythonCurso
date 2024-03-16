nome = 'arthur'
idade = 19
altura = 1.80
e_maior = idade > 18
peso = 68

print(nome, 'tem', idade, 'seu peso', peso, 'imc é', peso/(altura*altura))

print(f'{nome} tem {idade:.2f}')
print('{0} tem {1:.2f}'.format(nome, idade))
print('{n} tem {i:.2f}'.format(n=nome, i=idade),)
