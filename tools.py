from interface import *
from data import *
from flask import Flask, request

site = Flask(__name__)

@site.route('/submit', methods=['POST'])

def save_info():
    
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')

    # Insérer les données dans un dictionnaire
    client_data = {
        "name": name,
        "email": email,
        "phone": phone
    }

    # Afficher le dictionnaire pour vérification
    print(client_data)

    return f"Données reçues : {client_data}"

if __name__ == '__main__':
    # Lancer le serveur Flask
    site.run(debug=True) 