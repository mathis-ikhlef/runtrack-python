def contient_e(chaine):
    return 'e' in chaine


chaine_test = input("Entrez une chaîne de caractères : ")

if contient_e(chaine_test):
    print("La chaîne contient le caractère 'e'.")
else:
    print("La chaîne ne contient pas le caractère 'e'.")
