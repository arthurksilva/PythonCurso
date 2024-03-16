nameOne = "Escola"
nameComparation = 'E'
name_later_temporary = ''


for name_later_Comparation in nameOne:
    print(f"letter testing {name_later_Comparation}")
    if name_later_Comparation in nameComparation:
        name_later_temporary += name_later_Comparation
    if name_later_Comparation not in nameComparation:
        name_later_temporary += '*'
print(f'{name_later_temporary}')
