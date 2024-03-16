# Gerando os valores
# importando a biblioteca
import random
# Definir número inteiro que vai servir de base para geração de números
random.seed(1)
# Vai armazenar os valores gerados
number = random.getstate()
# Retorna determinado trecho da sequência
number_random = int(random.sample(range(50), k=50)) % 10

print(number_random)

qtd = 0
for i in range(0, 50):
    if number_random[i] == number_random[i]:
        qtd += 1
        print(f"Qtd {qtd}")
number_input = int(input("D"))

for n in range(0, 50):
    if number_input == number_random[n]:
        print('Ok')
