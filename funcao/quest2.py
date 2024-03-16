def multiplication(*args):
    for number in args:
        resul_two = number * 2
        resul_three = number * 3
        resul_four = number * 4
    return resul_two, resul_three, resul_four


multiplication_reslut = multiplication(1)
print(f"Number multipicado{multiplication_reslut}")
