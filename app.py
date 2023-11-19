import os
from flask import Flask
from flask_restx import Resource, Api
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Flask App
app = Flask(__name__)
api = Api(app)

# Initialize Firestore DB
# Fetch the service account key JSON file contents
cred = credentials.Certificate('key.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://park-planner-ul-800c9-default-rtdb.firebaseio.com'
})

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'World'}


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)