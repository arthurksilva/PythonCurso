array = 'o Brasil'
new_values = array.split(' ')
print(f"Split: {new_values}")
#new_values_two = ' '.join(array)
#print(f"Join: {new_values_two}")


for indece, valor in enumerate(new_values):
    print(indece, valor, new_values[indece])
