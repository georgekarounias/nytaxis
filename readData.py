from minio import Minio
from minio.error import S3Error
import csv 
import json
import os
import socket

JSON_ENTRIES_THRESHOLD = 5 # modify to whatever you see suitable
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

def write_json(json_array, filename):
    with open(filename, 'w', encoding='utf-8') as jsonf: 
        json.dump(json_array, jsonf)  # note the usage of .dump directly to a file descriptor

def csv_to_json(csvFilePath, jsonFilePath):
    mc = SetMC()
    print("Create json start")
    jsonArray = []
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 
        filename_index = 0
    
        for row in csvReader:
            jsonArray.append(row)
            if len(jsonArray) >= JSON_ENTRIES_THRESHOLD:
                # if we reached the treshold, write out
                write_json(jsonArray, f"{jsonFilePath}-{filename_index}.json")
                mc.fput_object("commoninput", f"output-{filename_index}.json", f"{jsonFilePath}-{filename_index}.json")
                os.remove(f"{jsonFilePath}-{filename_index}.json")
                filename_index += 1
                jsonArray = []
        
        
        # Finally, write out the remainder
        write_json(jsonArray, f"{jsonFilePath}-{filename_index}.json")
        mc.fput_object("commoninput", f"output-{filename_index}.json", f"{jsonFilePath}-{filename_index}.json")
        os.remove(f"{jsonFilePath}-{filename_index}.json")


csv_to_json('./_data/sampleData.csv', './_data/output')