import copy
# copy, sorted, produtos.sort
# Exercícios
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Aumente os preços dos produtos a seguir em 10%
novo_produtos = [
    {**produtos, 'preco': round(produtos['preco'] * 1.1, 2)}
    for produtos in produtos
]
print(*novo_produtos, sep='\n')

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)
print('\n')
print('Ordenação dos produtos...: \n')

ordem_produtos = sorted(copy.deepcopy(novo_produtos), key=lambda x: x["preco"])

for ordem_produtos in ordem_produtos:   
   print(ordem_produtos)



# Ordene os produtos por nome decrescente (do maior para menor)
print('\n')
print('Ordenação dos produtos...: \n')

ordem_produtos = sorted(novo_produtos, key=lambda x: x["preco"],reverse=True)

for ordem_produtos in ordem_produtos:   
   print(ordem_produtos)

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
print("\nOrdenação por nome do produto..:",sep='\n')

#produtos_ordenados_por_nome = copy.deepcopy(ordem_produtos)

produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), key=lambda x:x['nome'])

for produtos_ordenados_por_nome in produtos_ordenados_por_nome:
   print(produtos_ordenados_por_nome)






