from flask import Flask , render_template
from flask_socketio import SocketIO

app = Flask("application",template_folder="",static_folder="")
socket = SocketIO(app)

@app.route("/")
def home():
    return render_template("index.html")

@socket.on("connect")
def connection():
    print("A new client connected !!")
    socket.emit("message",f"Welcome to the server !!")

@socket.on("message")
def message(data):
    socket.emit("message",f"ECHO : {data}")

@socket.on("disconnect")
def disconnecting():
    print("A client disconnected !!")

if __name__ == "__main__":
    socket.run(app)