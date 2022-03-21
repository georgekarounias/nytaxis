import datetime
from ipaddress import ip_address
from turtle import distance
from minio import Minio
import socket
import uuid
import json
import os
import geopy.distance

BUCKETNAME = "testbucket"

def GetNetworkIp():
    # hostname = socket.gethostname()
    # local_ip = socket.gethostbyname(hostname)
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.connect(("8.8.8.8", 80))
    # local_ip = s.getsockname()[0]
    # s.close()
    local_ip="192.168.2.11"
    return local_ip
        

def SetMC():
    ipaddress = GetNetworkIp()
    mc = Minio(f"{ipaddress}:9000",
        access_key='minioadmin',
        secret_key='minioadmin',
        secure=False)
    return mc

def ReqBucketName(req_dict):
    keyStrArray = req_dict['Key'].split('/')
    return keyStrArray[0]

def GetTrips(inputBucket, file, mc):
    mc.fget_object(inputBucket, file, file)
    with open(file) as json_file:
        data = json.load(json_file)
    return data

def write_json(obj, filename):
    with open(filename, 'w', encoding='utf-8') as jsonf: 
        jsonf.write(obj) 

def ReqFileName(req_dict):
    keyStrArray = req_dict['Key'].split('/')
    return keyStrArray[1]

def WriteToBucket(req, trips, mc, bucketname):
    filename = ReqFileName(req)
    write_json(trips, filename)
    mc.fput_object(bucketname, filename, filename)
    os.remove(filename)
    return

def CalcDistance(trip):
    coords_1 = (float(trip['pickup_latitude']), float(trip['pickup_longitude']))
    coords_2 = (float(trip['dropoff_latitude']), float(trip['dropoff_longitude']))
    dist = geopy.distance.geodesic(coords_1, coords_2).km
    return dist

def GetTripDuration(trip):
    return int(trip['trip_duration'])

def GetPassengers(trip):
    return int(trip['passenger_count'])

def DoesTripMeetingRequirements(distance, duration, passengers):
    if(distance > 1 and duration > 600 and passengers > 2):
        return True
    return False

def handle(req):
    mc = SetMC()
    jsonReq = json.loads(req)
    inputBucket = ReqBucketName(jsonReq)
    filename = ReqFileName(jsonReq)
    trips = GetTrips(inputBucket, filename, mc)
    tripsMettingReqs = []
    for trip in trips:
        distance = CalcDistance(trip)
        duration = GetTripDuration(trip)
        passengers = GetPassengers(trip)
        doesTripMeetingRequirements = DoesTripMeetingRequirements(distance, duration, passengers)
        if(doesTripMeetingRequirements == True):
            tripsMettingReqs.append(trip)
    WriteToBucket(jsonReq, tripsMettingReqs, mc, BUCKETNAME) 
    return req
