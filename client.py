import socketio

host = 'raasta.herokuapp.com'
port = 80
sio_client = socketio.Client()

sio_client.connect("http://" + str(host) + ":" + str(port), namespaces = ['/'])

@sio_client.event
def transit_data(data):
    print(data)

@sio_client.event
def connect():
    print("connected to server")