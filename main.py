dico = {
    "person_1": {
        "presentation" : {
        "prenom" : "Eudocie",
        "nom" : "De Khovrine"
        },
        "info_perso" : {
        "interet" : "manger",
        "age" : "16 ans",
        "taille" : "110/130 cm"
        }
        },
    "person_2":{
        "presentation" : {
        "prenom" : "Marine",
        "nom" : "Fraboulet"
        },
        "info_perso" : {
        "interet" : "dormir",
        "age" : "16 ans",
        "taille" : "110/130 cm"
        }
        },
    "person_3" : {
        "presentation" : {
        "prenom" : "Louise",
        "nom" : "Christophe"
        },
        "info_perso" : {
        "interet" : "dormir",
        "age" : "16 ans",
        "taille" : "160/180 cm"
        }
    }
}

dico_compatibilite = {}

def calcul_compatibilite (cptr,person):
    return round (cptr /len(dico[person]['info_perso']) * 100)


def compare_with_one_person (people,person):
    cptr = 0
    if dico [people]["info_perso"] == dico[person]["info_perso"]:
        pass
    else:
        for caracter in dico[people]["info_perso"].keys ():
            if dico [person]['info_perso'][caracter] == dico [people]['info_perso'][caracter]:
                cptr = cptr + 1
    return (cptr)


def compare_with_different_person (person):
    dico_compatibilite [person] = {}
    for people in dico.keys() :
        cptr = compare_with_one_person (people,person)
        percentage_of_same = calcul_compatibilite (cptr, person)
        dico_compatibilite [person][people] = percentage_of_same
    return dico_compatibilite

print (compare_with_different_person ("person_1"))