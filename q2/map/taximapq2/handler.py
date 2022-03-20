from ipaddress import ip_address
from turtle import distance
from minio import Minio
import socket
import uuid
import json
import os


BUCKETNAME = "testbucket"

def GetNetworkIp():
    # hostname = socket.gethostname()
    # local_ip = socket.gethostbyname(hostname)
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.connect(("8.8.8.8", 80))
    # local_ip = s.getsockname()[0]
    # s.close()
    local_ip="192.168.42.45"
    return local_ip
        

def SetMC():
    ipaddress = GetNetworkIp()
    print(f"ip: {ipaddress}")
    mc = Minio(f"{ipaddress}:9000",
        access_key='minioadmin',
        secret_key='minioadmin',
        secure=False)
    return mc

# def GetTrips(req):
#     return

def write_json(obj, filename):
    with open(filename, 'w', encoding='utf-8') as jsonf: 
        json.dump(obj, jsonf) 

def WriteToBucket(trips, mc, bucketname):
    #trips['name']=req['Key']
    filename = str(uuid.uuid4())+".json" #req['Key'].split("/")[1]
    write_json(trips, filename)
    mc.fput_object(bucketname, filename, filename)
    os.remove(filename)
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
    x="{\"name\": \"geo\"}"
    WriteToBucket(json.loads(req), mc, BUCKETNAME) 
    return req
