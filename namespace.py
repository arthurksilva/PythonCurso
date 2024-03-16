"""
Em Python, um namespace é um contexto que contém um conjunto de 
nomes de variáveis e suas associações com objetos. 
Eles são usados para evitar conflitos de nomes e organizar o 
código de maneira mais eficiente. Aqui está um exemplo simples de namespace em Python:
"""

# Namespace global
global_var = 10

def minha_funcao():
    # Namespace local à função
    local_var = 5
    print(global_var)  # Acesso a uma variável do namespace global
    print(local_var)   # Acesso a uma variável do namespace local

minha_funcao()

# Tentar acessar local_var fora da função resultará em um erro, pois não está no namespace global
print(local_var)  # Isso resultará em um NameError

"""
Neste exemplo, global_var está no namespace global e 
pode ser acessado tanto dentro da função minha_funcao 
quanto fora dela. Por outro lado, local_var está no namespace local da 
função e só pode ser acessado dentro da função. Quando tentamos acessar 
local_var fora da função, ocorre um erro porque ele não está no namespace global.
"""