def difference(nombre):
    if nombre > 0:
        return 'positif'
    elif nombre < 0:
        return 'negatif'
    else:
        return 'nul'

print(difference(21))
print(difference(-3))
print(difference(0))