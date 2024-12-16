from flask import Flask, render_template

site = Flask(__name__)

@site.route("/submit")
def bonjour() : 
    return render_template("index.html")



if __name__ == '__main__':
    site.run(debug=True)


