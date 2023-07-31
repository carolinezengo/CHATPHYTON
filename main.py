from flask import Flask, render_template
from flask_socketio import SocketIO, send
app = Flask(__name__)
socketion = SocketIO(app, cors_allowed_origins="*")
#funcao de enviar mensagem
@socketion.on("message")
def gerenciar_msg(mensagem):
   send(mensagem, broadcast=True)
   #criar a rota
@app.route('/')
def homepage():
    return render_template("homepage.html")
#rota do app
if __name__ == '__main__':
 
 socketion.run(app, host="localhost")

 #$("#lista_mensagens").append($("<p>").text(data));