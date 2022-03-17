import json
import os
print(os.listdir('.'))

def GetJsonArray(path):
    with open(path) as f:
        jsonObj = json.load(f)
        return jsonObj

array = GetJsonArray('./_data/data.json')
for el in array:
    print(el['id'], "=>", el['pickup_datetime'])
