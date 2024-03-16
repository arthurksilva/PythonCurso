import random
import os
    
def check_exit(option):
    if option == '0':
        option = '0'
        return option
    if option == '1':
        option = '1'
        return option
    else:
        print("Enter a valid value ")
        option = input("Do you wish to continue? Yes(1) OR Not(0)")
        return option


list_peploe = []
counter = 0
qtd = 0

while(counter == 0):
    peploe = input("How may peploe? ")
    list_peploe.append(peploe)
    option = input("Do you wish to continue? Yes(1) OR Not(0)")
   
    option = check_exit(option)


    if option == '0':
        counter = 1
    


amount_peploe = len(list_peploe)



random_peplo = random.randint(0,amount_peploe-1)

os.system("cls")


for lista_peploe in list_peploe:
    print(f"Peploe: {list_peploe}")
    qtd = qtd + 1
    if qtd < amount_peploe:
        os.system("cls")


print(f"Who will pay the bill? {list_peploe[random_peplo]}")


