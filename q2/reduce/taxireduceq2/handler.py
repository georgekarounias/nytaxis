import datetime
from ipaddress import ip_address
from turtle import distance
from minio import Minio
import socket
import uuid
import json
import os

BUCKETNAME = "result2"
LOCAL_IP = "192.168.1.14"

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

def ReqFileName(req_dict):
    keyStrArray = req_dict['Key'].split('/')
    return keyStrArray[1]

def write_json(obj, filename):
    f = open(filename, 'w')
    f.write(obj)
    f.close()

def WriteToBucket(jsobj, bucketname, minioFileName, mc):
    outputfilename = minioFileName
    write_json(jsobj, "/tmp/" + outputfilename)
    mc.fput_object(bucketname, outputfilename, "/tmp/" + outputfilename)
    os.remove("/tmp/" + outputfilename)

def ProcessData(data, minioFileName, mc):
    obj = [{'count': len(data)}]
    json_object = json.dumps(obj)
    WriteToBucket(json_object, BUCKETNAME, minioFileName, mc)

def GetDataFromBucketFile(minioBucketName, minioFileName, mc):
    mc.fget_object(minioBucketName, minioFileName, "/tmp/" + minioFileName)
    with open("/tmp/" + minioFileName) as json_file:
        data = json.load(json_file)
    os.remove("/tmp/" + minioFileName)
    return data

def handle(req):
    reqJson = json.loads(req)
    minioBucketName=ReqBucketName(reqJson)
    minioFileName=ReqFileName(reqJson)
    mc = SetMC()
    data = GetDataFromBucketFile(minioBucketName, minioFileName, mc)
    ProcessData(data, minioFileName, mc)
    return req
