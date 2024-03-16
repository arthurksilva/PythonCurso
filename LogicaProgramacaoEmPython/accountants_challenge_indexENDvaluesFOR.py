asc = range(1, 10, 1)
desc = range(10, 1, -1)
values_desc = []

for values_asc in asc:
    print(values_asc)
print('\n')
for values_desc in desc:
    print(values_desc)

print("Forma de fazer.:")
for index, values in enumerate(range(10, 1, -1)):
    print(index, values)
