from minio import Minio
from minio.error import S3Error
import json
import os

OUTBUCKETNAME = 'result3'
LOCAL_IP = "192.168.1.14"

countArea1 = 0
countArea2 = 0
countArea3 = 0
countArea4 = 0

def SetMC():
    ipaddress = LOCAL_IP
    mc = Minio(f"{ipaddress}:9000",
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
    os.remove("/tmp/" + minioFileName)
    return data

def ProcessData(data, minioFileName):
    for i in data:
        UpdateAreaCounter(i['Area'])
    
    if((countArea1 + countArea2 + countArea3 + countArea4) == 0):
        return

    objects = {'Area1': countArea1,'Area2': countArea2,'Area3': countArea3,'Area4': countArea4}
    max_key = max(objects, key=objects.get)
        
    response = 'Best area is: ' + max_key

    responseJson = [{'Response': response}]
    # Serializing json 
    json_object = json.dumps(responseJson)
    WriteToBucket(json_object, OUTBUCKETNAME, minioFileName)
    
    return json_object

def UpdateAreaCounter(area):
    if area == 1:
        global countArea1
        countArea1 = countArea1 + 1
    if area == 2:
        global countArea2
        countArea2 = countArea2 + 1
    if area == 3:
        global countArea3
        countArea3 = countArea3 + 1
    else:
        global countArea4
        countArea4 = countArea4 + 1

def WriteToBucket(jsobj, bucketname, minioFileName):
    outputfilename = minioFileName
    write_json(jsobj, "/tmp/" + outputfilename)
    mc.fput_object(bucketname, outputfilename, "/tmp/" + outputfilename)
    os.remove("/tmp/" + outputfilename)
    
def write_json(obj, filename):
    f = open(filename, 'w')
    f.write(obj)
    f.close()

def handle(req):
    req_dict = json.loads(req)
    minioBucketName, minioFileName = GetMinioInfos(req_dict)

    data = GetDataFromBucketFile(minioBucketName, minioFileName)
    response = ProcessData(data, minioFileName)

    return response
