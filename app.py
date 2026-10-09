from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Amor,quiero que sepas la persona tan importante que eres para mi, lo demasiado que significas en mi vida, lo feliz que me haces, de verdad no se que haria yo sin ti,eres el rayo de sol que ilumina mis dias, la luna que ilumina toda la oscuridad en mi vida, quiero estar contigo demasiado tiempo y de verdad no sabes lo mucho que te amo y aprecio mi niña, de verdad, aunque aveces me enoje tu tienes algo que me hace feliz, te amo demasiado mi niña hermosa <3 (perdón que se vea feito pero cuando ya aprenda java te hago uno más lindo)"
