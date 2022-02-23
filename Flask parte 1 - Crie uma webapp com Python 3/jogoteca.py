from flask import Flask, render_template

app = Flask(__name__)

@app.route("/inicio")
def ola():
    lista_cursos = ["css", "java", "html", "python"]
    lista_jogos = ['Tibia', 'CS', 'Lol', 'Combats']
    return render_template("lista.html", titulo="JOGOS", jogos=lista_jogos, cursos=lista_cursos)
app.run()