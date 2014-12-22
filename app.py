# -*- coding:utf-8 -*-
from gevent import monkey
from socketio.defaultjson import default_json_dumps
import Board
from Character import Character
from Constants import *
from Server import Server
from Util import Util

monkey.patch_all()

import time
from threading import Thread
from flask import Flask, render_template, session, request, json
from flask.ext.socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None
utility = Util()

server = Server(socketio)
print('Server %s created') % server.server_id

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        time.sleep(10)
        count += 1
        socketio.emit('my response',
                      {'data': 'Server generated event', 'count': count},
                      namespace='/test')


@app.route('/')
def index():
    #global thread
    #if thread is None:
        #thread = Thread(target=background_thread)
        #thread.start()
    return render_template('index.html')


@socketio.on('new-hero', namespace='')
def new_hero(data):
    print(data.get('nickname'))
    session['character'] = Character(unique_id=utility._generate_socket_id(), nickname=data.get('nickname'), x=data.get('x'), y=data.get('y'))
    session['character'] = server._add_user_to_board(session['character'], TEAM_GOODGUYS)
    print('Client %s connected') % session['character'].unique_id

    emit(
         'your-id',
         {
         'your_id': session['character'].to_JSON(),
         'player_turn_id': server._get_current_player_turn()
         })

    socketio.emit(
        'add-new-player',
        session['character'].to_JSON()
    )


@socketio.on('hero-move', namespace='')
def hero_move(data):
    session['character'].x = data.get('x')
    session['character'].y = data.get('y')

    server.board.move_character(session['character'].unique_id, session['character'].x, session['character'].y)

    socketio.emit('hero-update', session['character'].to_JSON())
    socketio.emit('move-queue', server._move_queue(session['character'].unique_id))


@socketio.on('my broadcast event', namespace='')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)


@socketio.on('join', namespace='')
def join(message):
    join_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'In rooms: ' + ', '.join(request.namespace.rooms),
          'count': session['receive_count']})


@socketio.on('leave', namespace='')
def leave(message):
    leave_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'In rooms: ' + ', '.join(request.namespace.rooms),
          'count': session['receive_count']})


@socketio.on('my room event', namespace='')
def send_room_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']},
         room=message['room'])


@socketio.on('connect', namespace='')
def connect():
    emit('connect-data', {'userlist': server._get_user_list()})


@socketio.on('disconnect', namespace='')
def test_disconnect():
    print('Client %s disconnected' % session['character'].unique_id)


if __name__ == '__main__':
    socketio.run(app)
