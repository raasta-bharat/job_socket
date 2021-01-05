from flask import session, request
from flask_socketio import emit, join_room, leave_room
from .. import socketio
import time
import requests
from flask import copy_current_request_context

from flask_socketio import join_room, leave_room
from app.datajob.delhi_realtime_data import add_id

socket_ids = []

@socketio.on('connect')
def connect():
    @copy_current_request_context
    def start_job():
        while True:
            time.sleep(10)
            response = requests.get('https://server.nikhilvj.co.in/delhirt/VehiclePositions.pb')
            content = response.content
            for id in s:
                emit('transit_data', content, user=id)
    
    socket_ids.append(request.sid)
    if len(socket_ids) == 1:
        start_job()

    