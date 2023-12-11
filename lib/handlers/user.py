from lib.db_functions.mongo_db import *
import bcrypt
from flask import session 
from flask import abort
from functools import wraps

def create_user(username,password):
    salt = bcrypt.gensalt()
    password = str(password).encode('utf-8')
    print (password)
    hashed_pwd = bcrypt.hashpw(password, salt)

    user_data_collection.insert_one({"user_name":username,"password":hashed_pwd})


def verify_user(user_name,password):
    user_entry = user_data_collection.find_one({"user_name":user_name})
    if not (bool(user_entry)):
        return {"message":"This username is invalid"},500
    hashed_pwd = user_entry['password']
    #check password
    password = password.encode('utf-8')
    return (bool(bcrypt.checkpw(password, hashed_pwd)))

