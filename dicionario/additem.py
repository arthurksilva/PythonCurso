# Criando um dicionário
dict = {}
print(dict)

# Add itens
dict[0] = 'Geeks'  # name key + values
dict[1] = 'For'
dict[2] = '1'
print(dict)

# Uddate dictionary
dict['Update'] = 'Update'
print(dict)

# Array
dict['Array'] = [1, 2, 3]
print(dict)
print(dict['Array'])

# Add key caso não exita
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car)
x = car.setdefault("color", "white")

print(x)
print(car)
print(car['color'])

# dictionary join dictionary
d1 = [
    {
        'Pergunta': 'Quanto é 5*5?',
    },
    {
        'Array': [1, 2, 3]
    },
]
print(d1)
print(d1[1]['Array'])  # dictionary specific
print(d1[1]['Array'][0])  # dictionary specific and value
