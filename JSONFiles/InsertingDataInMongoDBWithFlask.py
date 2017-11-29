from flask import Flask
from flask_pymongo import PyMongo
import json

app = Flask(__name__)

#SELECTS MONGODB DATABASE USER CREATED
app.config['MONGO_DBNAME']= 'example'

#SELECTS MONGODB URI ASSIGNED TO THE DATABASE USER CREATED
app.config['MONGO_URI'] = 'mongodb://username:password.mlab.com:12345/example'

mongo = PyMongo(app)

@app.route('/add')
def insert():
    user = mongo.db.users
    #INSERTS KEY-VALUE PAIRS OF USER'S CHOICE
    user.insert({'Company' : 'Tech' , 'JobTitle' : 'Teacher' , 'ApplicationLink' : 'https://careers.jobscore.com/careers/ATT/jobs/devops-engineer-c_EIfcNtir5RT0dG1ZS6tF'})
    return 'Added TODAY'

if __name__ == '__main__':
    app.run(debug=True)


