def multipication(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multipication_result = multipication(1, 2)
print(f"{multipication_result}")

""" def oddOrEven(x):
    if x % 2 == 0:
        print(f"O número {x} é PAR.")
    else:
        print(f"O número {x} é ÍMPAR.")


number = int(input("Digite um número..: "))
oddOrEven(number)
 """
