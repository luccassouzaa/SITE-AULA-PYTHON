from flask import Flask, render_template
from flask_socketio import SocketIO, send

#criar variaveis
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

#funcionalidade de enviar mensagem
@socketio.on("message")
def sendMessage(message):
    send(message, broadcast=True)

#criar 1º rota
@app.route("/")
def homepage():
    return render_template("index.html")

#rodar
socketio.run(app, host="192.168.0.150")