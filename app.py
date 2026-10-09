from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Amor,quiero que sepas la persona tan importante que eres para mi, lo demasiado que significas en mi vida, lo feliz que me haces, de verdad no se que haria yo sin ti, teamo demasiado mi flakita hermosa"
