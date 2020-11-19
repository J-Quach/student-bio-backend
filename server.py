import os
import psycopg2
import random
import string
import sys
import codecs
import base64

from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app) #look into, need it to display data? maybe?

# os.environ.get returns None if the variable doesn't exist
DATABASE = os.environ.get('MIGHTY_PROJECT_DB_NAME')
HOST = os.environ.get('MIGHTY_PROJECT_DB_HOST')
PORT = os.environ.get('MIGHTY_PROJECT_DB_PORT')
PASSWORD = os.environ.get('MIGHTY_PROJECT_AD_PW')
USER = os.environ.get('MIGHTY_PROJECT_USER')

conn = psycopg2.connect(
    database=DATABASE,
    host=HOST,
    port=PORT,
    password=PASSWORD,
    user=USER
)

# throw error if the variables do not exist in the environment variables
if not (DATABASE and HOST and PORT and PASSWORD and USER):
    sys.exit("""You have not set all environment variables. Check for:
      * MIGHTY_PROJECT_DB_NAME
        * MIGHTY_PROJECT_DB_HOST
        * MIGHTY_PROJECT_DB_PORT
        * MIGHTY_PROJECT_AD_PW
        * MIGHTY_PROJECT_USER """
    )

@app.route('/')
def hello_world():
    return 'Hello, World!'