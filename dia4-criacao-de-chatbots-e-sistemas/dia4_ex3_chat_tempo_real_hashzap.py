import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY", "hashzap-dev-secret-key")
app.config["DEBUG"] = True

# Habilita comunicação bidirecional via WebSockets entre clientes na mesma rede
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("message")
def gerenciar_mensagens(mensagem: str) -> None:
    print(f"Mensagem recebida: {mensagem}")
    send(mensagem, broadcast=True)


@app.route("/")
def home() -> str:
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app, host="localhost", port=5000)
