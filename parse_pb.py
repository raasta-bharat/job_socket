from google.transit import gtfs_realtime_pb2

feed = gtfs_realtime_pb2.FeedMessage()

file_name = "VehiclePositions.pb"
file = open(file_name,"rb")
content = file.read()

number_of_rows = feed.ParseFromString(content)

co = 0

for entity in feed.entity:
	co += 1
	print(entity)
	if co == 5:
		break
