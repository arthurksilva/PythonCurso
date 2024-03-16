frase = 'O rato'
tamanho = len(frase)
contador = 0
nova_frase = ''
contador_troca = 0
input_do_usuario = input('Qual letra deseja deixar MAIÙSCULA? ')
while contador < tamanho:
    letra = frase[contador]
    if letra == input_do_usuario:
        if len(input_do_usuario) > 1:
            while contador_troca < input_do_usuario:
                trocar_letra = input_do_usuario[contador_troca]
                trocar_letra.upper()
        else:
            nova_frase += input_do_usuario.upper()
    else:
        nova_frase = nova_frase + letra
    contador += 1
print(nova_frase)
