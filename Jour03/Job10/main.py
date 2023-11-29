def verifie_pair_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            return "Le nombre est pair."
        else:
            return "Le nombre est impair."
    else:
        return "Le nombre n'est pas un entier positif."


nombre1 = 14
nombre2 = 27
nombre3 = -5.5
nombre4 = "Bonjour"

resultat1 = verifie_pair_impair(nombre1)
resultat2 = verifie_pair_impair(nombre2)
resultat3 = verifie_pair_impair(nombre3)
resultat4 = verifie_pair_impair(nombre4)

print(resultat1)
print(resultat2)
print(resultat3)
print(resultat4)
