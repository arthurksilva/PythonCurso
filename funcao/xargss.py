def print_car_info(**car):
    #impressão de args kwars
    for key, value in car.items():
        print(f"{key}: {value}", end=', ')
    print()  

print_car_info(marca="Gol", cor="Azul", motor=1.0, placa=1212)
print_car_info(marca="Honda", cor="Preto", motor=5.0, placa=1414)
print_car_info(marca="BMW", cor="Preto", motor=10.0, placa=1515)
