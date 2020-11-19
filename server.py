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
CORS(app)

# os.environ.get returns None if the variable doesn't exist
DATABASE = os.environ.get('STICKA_STO_DB_NAME')
HOST = os.environ.get('STICKA_STO_DB_HOST')
PORT = os.environ.get('STICKA_STO_DB_PORT')
PASSWORD = os.environ.get('STICKA_STO_AD_PW')
USER = os.environ.get('STICKA_STO_USER')

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
      * STICKA_STO_DB_NAME
        * STICKA_STO_DB_HOST
        * STICKA_STO_DB_PORT
        * STICKA_STO_AD_PW
        * STICKA_STO_USER """
    )

@app.route('/')
def hello_world():
    return 'Hello, World!'