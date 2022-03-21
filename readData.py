from minio import Minio
from minio.error import S3Error
import csv 
import json
import os
import socket
import pandas as pd

JSON_ENTRIES_THRESHOLD = 2000000 # modify to whatever you see suitable
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
    #mc = SetMC()
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
                #mc.fput_object("commoninput", f"output-{filename_index}.json", f"{jsonFilePath}-{filename_index}.json")
                os.remove(f"{jsonFilePath}-{filename_index}.json")
                filename_index += 1
                jsonArray = []
        
        
        # Finally, write out the remainder
        write_json(jsonArray, f"{jsonFilePath}-{filename_index}.json")
        #mc.fput_object("commoninput", f"output-{filename_index}.json", f"{jsonFilePath}-{filename_index}.json")
        os.remove(f"{jsonFilePath}-{filename_index}.json")

# df = pd.read_csv (r'./_data/fares.csv')
# df.to_json (r'./_data/fares.json')

#csv_to_json('./_data/fares.csv', './_data/output')
chunk_size = 100
def write_chunk(part, lines):
    with open('./_data/fares_part_'+ str(part) +'.csv', 'w') as f_out:
        f_out.write(header)
        f_out.writelines(lines)
with open("../nyc-parking-tickets/Parking_Violations_Issued_-_Fiscal_Year_2015.csv", "r") as f:
    count = 0
    header = f.readline()
    lines = []
    for line in f:
        count += 1
        lines.append(line)
        if count % chunk_size == 0:
            write_chunk(count // chunk_size, lines)
            lines = []
    # write remainder
    if len(lines) > 0:
        write_chunk((count // chunk_size) + 1, lines)
        
source_path = "../nyc-parking-tickets/Parking_Violations_Issued_-_Fiscal_Year_2015.csv"
for i,chunk in enumerate(pd.read_csv(source_path, chunksize=40000, dtype=dtypes)):
    chunk.to_csv('../tmp/split_csv_pandas/chunk{}.csv'.format(i), index=False)
    
