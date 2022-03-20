from fileinput import filename
from minio import Minio
from minio.error import S3Error
import json

def SetMC():
    mc = Minio("192.168.1.11:9000",
        access_key='minioadmin',
        secret_key='minioadmin',
        secure=False)
    return mc

def GetMinioInfos(req_dict):
    keyStrArray = req_dict['Key'].split('/')
    return keyStrArray[0], keyStrArray[1]

def handle(req):
    SetMC()

    req_dict = json.loads(req)
    minioBucketName, minioFileName = GetMinioInfos(req_dict)

    print(minioBucketName)
    print(minioFileName)

    return req