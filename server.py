#!/bin/env python
from app import create_app, socketio

app = create_app(debug=True)

if __name__ == '__main__':
	print("starting server")
    # socketio.run(app)
    socketio.run(app, host='0.0.0.0', debug=True)
