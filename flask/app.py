from markupsafe import escape
from flask import Flask
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def root():
    return "Hello World!"

@app.route("/about")
def about():
    return "This is the About page."

@app.route("/contact")
def contact():
    return "Contact us at contact@example.com."

@app.route("/hello/<name>")
def hello(name):
    return f"Hello {escape(name)}!"

@app.route("/search")
def search():
    query = request.args.get('name')  # Récupère la valeur du paramètre 'q'
    return f"Recherche : {query}"


if __name__ == "__main__":
    app.run()
