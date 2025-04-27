from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send():
    message = request.json.get('message')
    if message:
        messages.append(message)
        socketio.emit('new_message', {'message': message})
    return {'status': 'ok'}

if __name__ == '__main__':
    socketio.run(app, debug=True)
