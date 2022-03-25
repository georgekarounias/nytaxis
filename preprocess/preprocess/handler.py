from minio import Minio
import pandas as pd


BUCKETNAME = "commoninput"
LOCAL_IP = "192.168.42.230"
       

def SetMC():
    ipaddress = LOCAL_IP
    mc = Minio(f"{ipaddress}:9000",
        access_key='minioadmin',
        secret_key='minioadmin',
        secure=False)
    return mc

#TODO
#Manualy upload csv file to minio bucket prepeocess and then preprocess function will be 
#triggered and it will convert the csv to json and upload the result to commoninput
def handle(req):
    
    return req
