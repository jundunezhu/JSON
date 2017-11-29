import os
import glob
import json
import pymongo

#SELECTS MONGODB URI ASSIGNED TO THE DATABASE USER CREATED
connection = pymongo.MongoClient('mongodb://username:password.mlab.com:12345/example')
#SELECTS MONGODB URI ASSIGNED TO THE DATABASE USER CREATED
db=connection.example

#CHANGES DIRECTORY WHERE JSON FILES ARE STORED ON LOCAL HOST
os.chdir('C:/OriginFolder')

for i in glob.glob('*.json'):
        page = open(i, 'r')
        parsed = json.loads(page.read())
        collection = db[i]
        record1 = collection
        record1.insert(parsed)


	
        
        
        
        
        
