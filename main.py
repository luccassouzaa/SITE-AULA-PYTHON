from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

#funcionalidade de enviar mensagem
@socketio.on("message")
def sendMessage(message):
    send(message, broadcast=True)

@app.route("/")
def homepage():
    return render_template("index.html")

SocketIO.run(app, host="localhost")