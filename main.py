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

def compare_with_all_person ():
    for person in dico.keys():
        for people in dico.keys() :
            cptr = 0
            if dico [people]["info_perso"] == dico[person]["info_perso"]:
                print (f"{dico[person]['presentation']['prenom']} est à 100% compatible avec elle-même.")
            else:
                for caracter in dico[people]["info_perso"].keys ():
                    if dico [person]['info_perso'][caracter] == dico [people]['info_perso'][caracter]:
                        cptr = cptr + 1
                percentage_of_same = round (cptr /len(dico[person]['info_perso']) * 100)
                print (f"{dico[person]['presentation']['prenom']} a une poucentage de compatibilité avec {dico[people]['presentation']['prenom']} de {percentage_of_same}%.")

# compare_with_all_person ()


def compare_with_different_person (person):
    for people in dico.keys() :
        cptr = 0
        if dico [people]["info_perso"] == dico[person]["info_perso"]:
            pass
        else:
            for caracter in dico[people]["info_perso"].keys ():
                if dico [person]['info_perso'][caracter] == dico [people]['info_perso'][caracter]:
                    cptr = cptr + 1
            percentage_of_same = round (cptr /len(dico[person]['info_perso']) * 100)
            return (percentage_of_same)

compare_with_different_person ("person_1")

