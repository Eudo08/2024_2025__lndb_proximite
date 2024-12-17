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

def list_of_compatibilite (person):
    list_compatibility_number = []
    dico_compatibilite = compare_with_different_person (person)
    for values in dico_compatibilite[person].keys ():
        compatibility = dico_compatibilite[person][values]
        list_compatibility_number. append (compatibility)
    return list_compatibility_number,

def list_of_people (person):
    list_compatibility_person = []
    dico_compatibilite = compare_with_different_person (person)
    for values in dico_compatibilite[person].keys ():
        list_compatibility_person. append (values)
    return list_compatibility_person


def sort_compatibility_between_users (person):
    sort_number = []
    sort_people = []
    list_number = list_of_compatibilite (person)
    list_person = list_of_people (person)
    while list_number:
        max_value = list_number[0] 
        max_index = 0 
        for i in range(1, len(list_number)):
            if list_number[i] > max_value:
                max_value = list_number[i]
                max_index = i
        sort_number.append(max_value)
        del list_number[max_index]
        sort_people. append (list_person(max_index))
        list_person.remove (list_person(max_index))
    return sort_number, sort_people

print ( sort_compatibility_between_users ("person_1"))