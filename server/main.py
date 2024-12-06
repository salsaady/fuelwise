from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv 
from userLocation import *
load_dotenv()                    

import os 

app = Flask(__name__)
cors = CORS(app, origins='*')

app.register_blueprint(user_location)

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True, port=8080)
