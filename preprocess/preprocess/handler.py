from minio import Minio
import pandas as pd
import json
import csv
import os

BUCKETNAME = "commoninput"
LOCAL_IP = "192.168.2.9"
       

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

# def write_json(json_array, filename):
#     with open(filename, 'w', encoding='utf-8') as jsonf: 
#         json.dump(json_array, jsonf)  # note the usage of .dump directly to a file descriptor

def csv_to_json(req):
    bucketname, csvfilename = GetMinioInfos(req)
    csvFilePath = req['Key']
    mc.fget_object(bucketname, csvfilename, csvFilePath)
    csv = pd.read_csv (csvFilePath)
    csv.to_json (f"{csvfilename}.json")
    mc.fput_object(BUCKETNAME, f"{csvfilename}.json", f"{csvfilename}.json")
    os.remove(csvFilePath)
    os.remove(f"{csvfilename}.json")

    #jsonArray = []
    # with open(csvFilePath, encoding='utf-8') as csvf: 
    #     csvReader = csv.DictReader(csvf) 
    #     for row in csvReader:
    #         jsonArray.append(row)
            
    #     write_json(jsonArray, f"{jsonFilePath}-{filename_index}.json")
    #     mc.fput_object(BUCKETNAME, f"output-{filename_index}.json", f"{jsonFilePath}-{filename_index}.json")
 
#TODO
#Manualy upload csv file to minio bucket prepeocess and then preprocess function will be 
#triggered and it will convert the csv to json and upload the result to commoninput
def handle(req):
    req_dict = json.loads(req)
    csv_to_json(req_dict)
    return req
