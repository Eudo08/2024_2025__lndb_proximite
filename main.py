from data import *
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
        if dico [people]["info_perso"] == dico[person]["info_perso"]:
            pass
        else:
            cptr = compare_with_one_person (people,person)
            percentage_of_same = calcul_compatibilite (cptr, person)
            dico_compatibilite [person][people] = percentage_of_same
    return dico_compatibilite

def list_of_people (person):
    list_compatibility_with_every_person = []
    dico_compatibilite = compare_with_different_person (person)
    for values in dico_compatibilite[person].keys ():
        compatibility = dico_compatibilite[person][values] 
        list_compatibility_with_every_person. append (compatibility)
    return list_compatibility_with_every_person


def tri_compatibility_between_users (person):
    the_closest_to_the_furthest = []
    list_compatibility_with_every_person = list_of_people (person)
    while list_compatibility_with_every_person:
        max_value = list_compatibility_with_every_person[0] 
        max_index = 0 
        for i in range(1, len(list_compatibility_with_every_person)):
            if list_compatibility_with_every_person[i] > max_value:
                max_value = list_compatibility_with_every_person[i]
                max_index = i
        the_closest_to_the_furthest.append(max_value)
        del list_compatibility_with_every_person[max_index]
    return the_closest_to_the_furthest

print ( tri_compatibility_between_users ("person_1"))