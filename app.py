import os
from flask import Flask, request, jsonify
import uuid
from flask_restx import Resource, Api
import firebase_admin
from firebase_admin import credentials, firestore,db


# Initialize Flask App
app = Flask(__name__)
api = Api(app, title='Park Planner API',
           description='The API designed for the residential security system will focus on providing endpoints for the registration of residents, guards, vehicles, and access verification.')

# Initialize Firestore DB
# Fetch the service account key JSON file contents
cred = credentials.Certificate('key.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://park-planner-app.firebaseio.com'
})

ref=db.reference('/clients')

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        data=ref.get()
        return jsonify(data)
    
    # def post(self, Resource):
    #     try:
    #         nit = request.form.get('nit')
    #         razon_social = request.form.get('razon_social')
    #         direccion = request.form.get('direccion')
    #         estado = request.form.get('estado')
            

    #         data = {
    #             'nit':nit,
    #             'razon_social':razon_social,
    #             'direccion':direccion,
    #             'estado': estado,
    #         }
    #         ref.push().set(data)
            

    #         return jsonify({'status': str('Data add successfully!')})
        
    #     except Exception as e:
    #         return f"An error ocurred: {e}"


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port,debug=True)