from turtle import distance
from minio import Minio
import socket
import uuid

def SetMC():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipaddress = s.getsockname()[0]
    s.close()
    mc = Minio(f"{ipaddress}:9000",
        access_key='minioadmin',
        secret_key='minioadmin',
        secure=False)
    return mc

# def GetTrips(req):
#     return

def WriteToBucket(trips, mc, bucketname):
    # write to temporary file
    file_name = str(uuid.uuid4())
    f = open("/tmp/" + file_name, "a")
    f.write(trips)
    f.close()

    # sync to Minio
    mc.fput_object(bucketname, file_name, "/tmp/"+file_name)
    return

# def CalcDistance(trip):
#     return

# def GetTripDuration(trip):
#     return

# def GetPassengers(trip):
#     return

# def DoesTripMeetingRequirements(distance, duration, passengers):
#     return

def handle(req):
    print("Mapper Q2")
    mc = SetMC()
    # trips = GetTrips(req)
    # tripsMettingReqs = []
    # for trip in trips:
    #     distance = CalcDistance(trip)
    #     duration = GetTripDuration(trip)
    #     passengers = GetPassengers(trip)
    #     doesTripMeetingRequirements = DoesTripMeetingRequirements(distance, duration, passengers)
    #     if(doesTripMeetingRequirements == True):
    #         tripsMettingReqs.append(trip)
    # WriteToBucket(trips, mc, "testbucket") 
    print("Trying write to bucket")
    WriteToBucket(req, mc, "testbucket") 
    print("Wrote to bucket")
    return req
