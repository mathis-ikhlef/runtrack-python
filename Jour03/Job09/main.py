def moyenne(maths, physique, sport):
    moyenne_etudiant = round((maths + physique + sport) / 3)

    TRES_BON = (15, 20)
    BON = (11, 14)
    MOYEN = (8, 10)
    EFFORTS = (0, 7)

    if TRES_BON[0] <= moyenne_etudiant <= TRES_BON[1]:
        print("Très bon élève")
    elif BON[0] <= moyenne_etudiant <= BON[1]:
        print("Bon eleve")
    elif MOYEN[0] <= moyenne_etudiant <= MOYEN[1]:
        print("Élève moyen")
    elif EFFORTS[0] <= moyenne_etudiant <= EFFORTS[1]:
        print("Élève devant faire des efforts")
    else:
        print("Moyenne non valide")
    return moyenne_etudiant

maths = float(input("Note en Maths: "))
physique = float(input("Note en Physique: "))
sport = float(input("Note en Sport: "))

print("Moyenne de l'étudiant: ", moyenne(maths, physique, sport))

