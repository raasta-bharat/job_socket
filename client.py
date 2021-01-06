import socketio

host = 'raasta.herokuapp.com'
port = 80

# host = '0.0.0.0'
# port = 5000

sio_client = socketio.Client(reconnection=True)

sio_client.connect("http://" + str(host) + ":" + str(port), namespaces = ['/'])

@sio_client.event
def transit_data(data):
    print(data)

@sio_client.event
def connect():
    print("connected to server")