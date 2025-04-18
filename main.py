from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tajna'
socketio = SocketIO(app)

class Main():
    def random_port():
        return random.randint(1000,9999)

class server_settings():
    HOST = '127.0.0.1'
    PORT = Main.random_port()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_message(data):
    print("Primljena poruka:", data)
    emit('receive_message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host = server_settings.HOST, port = server_settings.PORT, debug=True)