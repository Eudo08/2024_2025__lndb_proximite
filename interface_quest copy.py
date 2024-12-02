from flask import Flask

site = Flask(__name__)

@site.route("/")
def bonjour() : 
    return "<p>Bienvenue </p>"

if __name__ == '__main__':
    site.run(debug=True)