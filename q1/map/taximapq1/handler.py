from asyncore import write
from fileinput import filename
from minio import Minio
from minio.error import S3Error
import json
import uuid
import os

OUTBUCKETNAME = 'map1output'


def SetMC():
    mc = Minio("192.168.1.11:9000",
        access_key='minioadmin',
        secret_key='minioadmin',
        secure=False)
    return mc

mc = SetMC()

def GetMinioInfos(req_dict):
    keyStrArray = req_dict['Key'].split('/')
    return keyStrArray[0], keyStrArray[1]

def GetDataFromBucketFile(minioBucketName, minioFileName):
    mc.fget_object(minioBucketName, minioFileName, "/tmp/" + minioFileName)
    with open("/tmp/" + minioFileName) as json_file:
        data = json.load(json_file)
    return data

def ProcessData(data, minioFileName):
    objects = []
    for i in data:
        area = GetArea(i['pickup_longitude'], i['pickup_latitude'])
        dictionary ={'Id': i['id'], 'Area': area}
        objects.append(dictionary)
    
    # Serializing json 
    json_object = json.dumps(objects)
    WriteToBucket(json_object, OUTBUCKETNAME, minioFileName)

def GetArea(longitude, latitude):
    if float(longitude) > float('-73.935242') and float(latitude) > float('40.730610'):
        return 1
    elif float(longitude) > float('-73.935242') and float('40.730610'):
        return 2
    elif  float(longitude) < float('-73.935242') and float('40.730610'):
        return 3
    else:
        return 4

def WriteToBucket(jsobj, bucketname, minioFileName):
    outputfilename = minioFileName
    write_json(jsobj, "/tmp/" + outputfilename)
    mc.fput_object(bucketname, outputfilename, "/tmp/" + outputfilename)
    os.remove("/tmp/" + outputfilename)
    return

def write_json(obj, filename):
    f = open(filename, 'w')
    f.write(obj)
    f.close()
        

def handle(req):
    req_dict = json.loads(req)
    minioBucketName, minioFileName = GetMinioInfos(req_dict)

    data = GetDataFromBucketFile(minioBucketName, minioFileName)
    ProcessData(data, minioFileName)

    #return req