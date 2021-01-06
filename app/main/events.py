from flask import session, request
from flask_socketio import emit, join_room, leave_room
from .. import socketio
import time
import requests
from flask import copy_current_request_context

from flask_socketio import join_room, leave_room
import threading

socket_ids = []

def repeat_every(n, func, *args, **kwargs):
    def and_again():
        func(*args, **kwargs)
        t = threading.Timer(n, and_again)
        t.daemon = True
        t.start()
    t = threading.Timer(n, and_again)
    t.daemon = True
    t.start()

@socketio.on('connect')
def connect():
    @copy_current_request_context
    def start_job():
        print("Starting job")
        print("Requesting Data")
        response = requests.get('https://server.nikhilvj.co.in/delhirt/VehiclePositions.pb')
        content = response.content
        for sid in socket_ids:
            print("Sending data to " + sid)
            try:
                emit('transit_data', content, room=sid)
            except Exception as e:
                print(e)
    
    print("Connecting socket")
    socket_ids.append(request.sid)
    if len(socket_ids) == 1:
        repeat_every(10.0, start_job)
