from flask import Flask, request, render_template, url_for
app = Flask(__name__)

lista=[1,2,3,4,5]

@app.route("/")
def inizio():
    return render_template("index.html", lista=lista)

@app.route("/profilo")
def profilo():
    return "questa è la pagina profilo"

if __name__=='__main__':
    app.run(debug=True)