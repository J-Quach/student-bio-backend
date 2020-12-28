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


@app.route('/all_User', methods=['GET'])
def all_User():
    """
    all_User reads all the Users from the url 127.0.0.1:5000/all_User 
    and queries the database for all Users

    Parameters:
        None

    Returns:
        returns [
            list of IDTable objects (userID, firstName, lastName, userRole, hobby, bio, favNum)
        ]
    """

    cur = conn.cursor()

    # This queries for all Users by userRole
    query = """
        SELECT *
        FROM IDTable
        ORDER BY IDTable.userRole
    """
    cur.execute(query)

    res = cur.fetchall()
    all_users = []

    for col in res:
        res_dict = {
            "userID": col[0],
            "firstName": col[1],
            "lastName": col[2],
            "userRole": col[3],
            "hobby": col[4],
            "bio": col[5],
            "favNum": col[6]
        }
        all_users.append(res_dict)

    # Handle if User doesn't exist
    if all_users is None:
        return jsonify({
            "result": False,
            "message": "Users doesn't exist"
        })
    else:
        return jsonify({
            "result": True,
            "user_list": all_users
        })

    cur.close()

    return jsonify({
        "result": True,
        "message": "Completed printing all users"
    })






@app.route("/IDTable/<userID>", methods=['GET'])
def get_user(userID):
    """
    get_user takes the userID from the url 127.0.0.1/IDTable/<userID> and queries the database for the user for the given userID

    Parameters:
        userID: ID of the user
    
    Returns:
        returns JSON(userID, firstName, lastName, userRole, hobby, bio, favNum)
    """

    cur = conn.cursor()

    query = """
        SELECT *
        FROM IDTable
        WHERE IDTable.userID = %s
    """

    cur.execute(query, (userID))

    res = cur.fetchone()

    res_dict = {
        "userID": res[0],
        "firstName": res[1],
        "lastName": res[2],
        "userRole": res[3],
        "hobby": res[4],
        "bio": res[5],
        "favNum": res[6]
    }
    cur.close()

    # Handle if UserID doesn't exist
    if res is None:
        return jsonify({
            "result": False,
            "message": "Error, UserID doesn't exist"
        })
    else:
        return jsonify({
            "result": True,
            "user": res_dict
        })
    
    return jsonify({
        "result": True,
        "message": "Completed printing user information"
    })


@app.route("/create_user", methods = ["POST"]) 
def create_user():

    rec = request.get_json()
    
    FIRSTNAME = rec['firstName'] or None
    LASTNAME = rec['lastName'] or None
    USERROLE = 'student'
    HOBBY = rec['hobby'] or None
    BIO = rec['bio'] or None
    FAVNUM = rec['favNum'] or None

    if( FIRSTNAME is None 
        or LASTNAME is None
        or HOBBY is None
        or BIO is None
        or FAVNUM is None
    ):
        return jsonify({
            "result": False,
            "message": "Missing one or more information."
        })
    
    cur = conn.cursor()

    user_query = """
        INSERT INTO IDTable(firstName, lastName, hobby, bio, favNum)
        VALUES (%s, %s, %s, %s, %s)
        """
    try:
        cur.execute(user_query,FIRSTNAME,LASTNAME,USERROLE,HOBBY,BIO,FAVNUM)
        conn.commit()
        cur.close()
        return jsonify({
            "result": True,
            "message": "Successfully updated database"
        })
    except:
        print("Error inserting in Database!")
        conn.rollback()
        return jsonify({
            "result": False,
            "message": "There was an error updating the database." 
        })




# 11/23/2020 TODO: Create a post endpoint to accept data into Database