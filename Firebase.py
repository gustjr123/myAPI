import pyrebase
import os

apiKey = os.environ.get('API_KEY')
authDomain = os.environ.get('AUTH_DOMAIN')
projectID = os.environ.get('PROJECT_ID')
storageBucket = os.environ.get('STORAGE_BUCKET')
messagingSenderId = os.environ.get('MESSAGING_SENDER_ID')
appID = os.environ.get('APP_ID')
databaseURL = os.environ.get('DATABASE_URL')

config = {
  "apiKey" : apiKey,
  "authDomain" : authDomain,
  "projectId" : projectID,
  "storageBucket" : storageBucket,
  "messagingSenderId" : messagingSenderId,
  "appId" : appID,
  "databaseURL" : databaseURL
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
storage = firebase.storage()