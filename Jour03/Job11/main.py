def time_to_text(minutes):
    # Vérifier si l'argument est un nombre entier positif
    if type(minutes) != int or minutes < 0:
        print("Veuillez entrer un nombre entier positif.")
        return

    # Calculer les heures et les minutes
    heures = minutes // 60
    minutes_restantes = minutes % 60

    # Afficher le temps en console
    if heures == 0:
        print(f"{minutes} minutes")
    elif heures == 1:
        print(f"{heures} heure et {minutes_restantes} minutes")
    else:
        print(f"{heures} heures et {minutes_restantes} minutes")


time_to_text(120)
time_to_text(75)
time_to_text(45)
time_to_text(0)
time_to_text(-30)
