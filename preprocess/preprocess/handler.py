from minio import Minio
import pandas as pd
import json
import csv
import os

BUCKETNAME = "commoninput"
LOCAL_IP = "192.168.1.14"
       

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

def write_json(json_array, filename):
    with open(filename, 'w', encoding='utf-8') as jsonf: 
        json.dump(json_array, jsonf)

def csv_to_json(req):
    bucketname, csvfilename = GetMinioInfos(req)
    csvFilePath = req['Key']
    mc.fget_object(bucketname, csvfilename, csvFilePath)

    jsonArray = []
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 
        for row in csvReader:
            jsonArray.append(row)

        jsonFilename = csvfilename.replace(".csv", "")    
        write_json(jsonArray, f"{jsonFilename}.json")
        mc.fput_object(BUCKETNAME, f"{jsonFilename}.json", f"{jsonFilename}.json")
    
    os.remove(csvFilePath)
    os.remove(f"{jsonFilename}.json")
 
def handle(req):
    req_dict = json.loads(req)
    csv_to_json(req_dict)
    return req
