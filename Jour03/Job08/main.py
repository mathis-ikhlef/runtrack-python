def fruit_et_legumes( type, saison):
    if type == "fruit":
        if saison == "hiver":
            return "orange, mandarine et kiwi"
        elif saison == "ete":
            return "Poire, fraise, cassis"
    elif type == "legume":
        if saison == "hiver":
            return "carotte, topinambour, endive"
        elif saison == "ete":
            return "artichaut, aubergine, navet"
        else:
            return "Mangez cinq fruits et légumes par jour"

print(fruit_et_legumes("fruit", "hiver"))
print(fruit_et_legumes("fruit", "ete"))
print(fruit_et_legumes("legume", "hiver"))
print(fruit_et_legumes("legume", "ete"))
print(fruit_et_legumes("legume", "printemps"))

