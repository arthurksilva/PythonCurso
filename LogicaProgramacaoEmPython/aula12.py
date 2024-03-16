num1 = input('Número 1..: ')
num2 = input('Número 2..: ')

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Algum valor não é número')
