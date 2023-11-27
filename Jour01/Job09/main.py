produit = {
    'nom':'lait',
    'prix': 1,
    'quantite': 20
}

print("Produit :")
print("Nom:", produit['nom'], "\nPrix/u:", produit['prix'],"\nQuantite:", produit['quantite'],)

quantite_acheter = input("Quelle quantité souhaitez-vous acheter?")

total = produit['prix'] * int(quantite_acheter)

print ("Le total s'élève à ", total, "€")

produit['quantite'] -= int(quantite_acheter)
print("Après l'achat :","\nQuantite stock:", produit['quantite'],)

produit['prix'] *=1.1
print("L'inflation augmente le prix de 10%", produit['prix'])