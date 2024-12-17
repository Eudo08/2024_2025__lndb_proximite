from interface import *
from data import *
from flask import Flask, request

site = Flask(__name__)

@site.route('/submit', methods=['POST'])

def save_info():
    
    prenom = request.form.get('prenom')
    nom = request.form.get('nom')
    genre = request.form.get('genre')

    personne1 = {
        "name": name,
        "email": email,
        "phone": phone
    }

    return personne1

if __name__ == '__main__':
    # Lancer le serveur Flask
    site.run(debug=True) 