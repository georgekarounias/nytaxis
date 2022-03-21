from ipaddress import ip_address
from math import fabs
from tkinter import E
from turtle import distance
from minio import Minio
import socket
import uuid
import json
import os
from datetime import *


BUCKETNAME = "map3output"
LOCAL_IP = "192.168.1.11"

def SetMC():
    ipaddress = LOCAL_IP
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
    os.remove(file)
    return data

def write_json(obj, filename):
    f = open(filename, 'w')
    f.write(obj)
    f.close()

def WriteToBucket(filename, trips, mc, bucketname):
    write_json(trips, filename)
    mc.fput_object(bucketname, filename, filename)
    os.remove(filename)
    return
    
def ReqFileName(req_dict):
    keyStrArray = req_dict['Key'].split('/')
    return keyStrArray[1]

def GetArea(longitude, latitude):
    if float(longitude) > float('-73.935242') and float(latitude) > float('40.730610'):
        return 1
    elif float(longitude) > float('-73.935242') and float('40.730610'):
        return 2
    elif  float(longitude) < float('-73.935242') and float('40.730610'):
        return 3
    else:
        return 4

def ReadFromBucket(inputBucket, file, mc):
    mc.fget_object(inputBucket, file, file)
    with open(file) as json_file:
        data = json.load(json_file)
    return data

def handle(req):
    mc = SetMC()
    f = json.loads(req)
    inputBucket = ReqBucketName(f)
    filename = ReqFileName(f)
    
    data =ReadFromBucket(inputBucket, filename, mc)

    routesMettingReqs = []

    for i in data:
        pickupTime = datetime.strptime(i['pickup_datetime'], '%Y-%m-%d %H:%M:%S')
        time = pickupTime.strftime("%H:%M:%S")
        #time = datetime.strptime(time, '%H:%M:%S')
        day = pickupTime.strftime("%A")

        if day != "Saturday" and day != "Sunday":

            rushHourStart1 = datetime.strptime("07:00:00", '%H:%M:%S')
            rushHourEnd1 = datetime.strptime("10:00:00", '%H:%M:%S')
            rushHourStart2 = datetime.strptime("15:00:00", '%H:%M:%S')
            rushHourEnd2 = datetime.strptime("19:00:00", '%H:%M:%S')

            if (datetime.strptime(time, '%H:%M:%S') > rushHourStart1 and datetime.strptime(time, '%H:%M:%S') < rushHourEnd1 ) or (datetime.strptime(time, '%H:%M:%S') > rushHourStart2 and datetime.strptime(time, '%H:%M:%S') < rushHourEnd2 ):
                area = GetArea(i['pickup_longitude'], i['pickup_latitude'])

                dictionary ={"Id" : i['id'], "Area" : area}
                routesMettingReqs.append(dictionary)
    if len(routesMettingReqs) == 0:
        return
    # Serializing json 
    json_object = json.dumps(routesMettingReqs)
    WriteToBucket(filename, json_object, mc, BUCKETNAME) 

    return  json_object
