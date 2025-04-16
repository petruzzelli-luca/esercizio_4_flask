from flask import Flask, request, render_template, url_for, redirect
app = Flask(__name__)

lista=[1,2,3,4,5]

@app.route("/")
def inizio():
    return render_template("index.html", lista=lista)

@app.route("/profilo")
def profilo():
    return "questa è la pagina profilo"

@app.route("/aggiungi", methods=["GET", "POST"])
def inserisci():
    if request.method == "POST":
        elemento_aggiunto = request.form["aggiunta"]
        lista.append(elemento_aggiunto)
    return redirect(url_for('inizio'))




if __name__=='__main__':
    app.run(debug=True)