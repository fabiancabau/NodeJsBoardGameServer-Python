from flask.ext.socketio import SocketIO, emit, join_room, leave_room

class ServerListener:

    server = None

    def __init__(self, server):
        self.server = server


    #@server.socket.on('connect', namespace='/test')
    #def test_connect():
        #emit('my response', {'data': 'Connected', 'count': 0})
