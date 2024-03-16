perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
qtd_hit = 0
qtd_wrong = 0

print("Pergunta 1 :" + perguntas[0]['Pergunta'])
for n in range(0, 4):
    print("Opções:" + perguntas[0]['Opções'][n])
result = int(input("Qual a respota certa?"))
if result == 4:
    print("Você acertou, Resposta correta " + perguntas[0]['Resposta'])
    qtd_hit += 1
else:
    print("Errou")
    qtd_wrong += 1

print("\nPergunta2:" + perguntas[1]['Pergunta'])
for n in range(0, 4):
    print("Opções:" + perguntas[1]['Opções'][n])
result = int(input("Qual a respota certa?"))
if result == 25:
    print("Você acertou, Resposta correta " + perguntas[1]['Resposta'])
    qtd_hit += 1
else:
    print("Errou")
    qtd_wrong += 1

print("\nPergunta3:" + perguntas[2]['Pergunta'])
for n in range(0, 4):
    # dicionário + lista + key obs.: Se tiver lista tem que rodar tudo
    print("Opções:" + perguntas[2]['Opções'][n])
result = int(input("Qual a respota certa?"))
if result == 5:
    print("Você acertou, Resposta correta " + perguntas[2]['Resposta'])
    qtd_hit += 1
else:
    print("Errou")
    qtd_wrong += 1
print(f"\n Acertos:{qtd_hit} e Erros: {qtd_wrong}")
