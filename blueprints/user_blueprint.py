# from flask import Blueprint,request,redirect,url_for
# from lib.handlers.user import *
# from uuid import uuid4
# user_blueprint = Blueprint("user",__name__)

# @user_blueprint.route("/user/create", methods = ['POST'])
# def user_create():
#     args = request.json
#     username = args['username']
#     # password = args['password']
#     try:
#         # create_user(username, password)
#         #create customer id hex
#         customer_id = str(uuid4().hex)
#         add_customer(customer_id, username)
#         return {"message":"User created successfully!","status":"success"}
#     except Exception as e:
#         print (e)
#         return {"message":"User creation failed!","status":"fail"}



# @user_blueprint.route("/user/login", methods = ['POST'])
# def user_login():
#     args = request.json
#     username = args['username']
#     password = args['password']
#     user_is_verified = verify_user(username,password)
#     print (user_is_verified)
#     if not (user_is_verified):
#         return {"message":"Incorrect credentials"},401
#     return {"message":"User is verified"},200


    