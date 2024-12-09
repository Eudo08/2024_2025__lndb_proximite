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
        cptr = compare_with_one_person (people,person)
        percentage_of_same = calcul_compatibilite (cptr, person)
        dico_compatibilite [person][people] = percentage_of_same
    return dico_compatibilite

print (compare_with_different_person ("person_1"))








































































from flask import Flask, jsonify 

app = Flask(__name__) 

@app.route('/api', methods=['GET']) 
def home(): 
    return jsonify({'message': 'Bonjour le monde !'}) 

if __name__ == '__main__': 
    app.run(debug=True)