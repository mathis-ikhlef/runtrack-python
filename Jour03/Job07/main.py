def developpeur(langage):
    if langage == 'Javascript':
        return 'Tu es un developpeur web'
    elif langage == 'Python':
        return 'Tu es un developpeur IA'
    elif langage =='C':
        print("tu es un dev c")
    elif langage == 'Java':
        return 'Tu es un developpeur logiciel'
    elif langage == 'reactjs':
        return 'Tu es un developpeur mobile'
    else:
        return 'Un jour je serais le meilleur developpeur'

developpeur("C")
test = developpeur("")
print(test)
