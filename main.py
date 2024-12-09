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

def compare_with_different_person ():
    for person in dico.keys():
        cptr = 0
        for people in dico.keys() :
            for caracter in dico[people]['info_perso'].keys ():
                if dico [person][caracter] == dico [people][caracter]:
                    cptr = cptr + 1
        percentage_of_same = (cptr - 1)/len(dico[person]['info_perso']) * 100
        print (f"{dico[person]['presentation']['prenom']} a une poucentage de compatibilité avec {dico[people]['presentation']['prenom']} de {percentage_of_same}%.")

compare_with_different_person ()




















































from flask import Flask, jsonify 

app = Flask(__name__) 

@app.route('/api', methods=['GET']) 
def home(): 
    return jsonify({'message': 'Bonjour le monde !'}) 

if __name__ == '__main__': 
    app.run(debug=True)