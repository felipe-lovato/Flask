from flask import Flask, render_template

app = Flask(__name__)

class Jogos:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route("/inicio")
def ola():
    jogo1 = Jogos('tibia', 'rpg', 'pc')
    jogo2 = Jogos('CS', 'tiro', 'Playstation')
    lista = [jogo1,jogo2]
    return render_template("lista.html", titulo='Jogos',Jogos=lista)
app.run()