import json 
import multiprocessing
import os

lock = multiprocessing.Lock()
dbpath = os.path.join(os.path.join(os.getcwd(), "serverBE"), "serverInfo.txt")

async def write(details={}):
    print(details)
    with lock: 
        with open(dbpath, 'w') as convert_file: 
            convert_file.write(json.dumps(details))

async def read():
    with lock: 
        with open(dbpath, 'r') as convert_file:
            data = convert_file.read()
    js = json.loads(data)
    return js
