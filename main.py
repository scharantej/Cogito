
# main.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/explore/<concept_name>")
def explore(concept_name):
    return render_template("explore.html", concept_name=concept_name)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
