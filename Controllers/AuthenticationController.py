from flask import Blueprint, request, make_response
from Response import Response
from Services.AuthenticationService import AuthenticationService
from Models.User import User
from flask import current_app as app
from mongoengine import DoesNotExist

AuthenticationService = AuthenticationService()

auth = Blueprint("AuthenticationController", __name__, url_prefix="/api/auth")

@auth.route("/login", methods=["POST"])
def login():
    print("Logging in")
    session = AuthenticationService.authenticate(
        request.form["email"], request.form["password"])
    if not session:
        return Response("Incorrect username or password. Please check your credentials and try again.", status=403)
    else:
        ret = make_response("Success")
        ret.set_cookie("SID", str(session.sessionId), expires=session.dateExpires)
        return ret

@auth.route("/logout", methods=["POST"])
def logout():
    try:
        sessionId = request.form["sessionId"]
        AuthenticationService.logout(sessionId)
        return Response("Successfully logged out.", status=200)
    except:
        return Response("Unable to process request. Please reload and try again later.", status=400)


"""
Request params: first name, last name, email (will be used as username), password
Return: Success or failure codes    
"""
@auth.route("/signup", methods=["POST"])
def signup():
    user = {"firstName": request.form["firstName"],
            "lastName": request.form["lastName"],
            "email": request.form["email"],
            "password": request.form["password"]
            }

    if (not AuthenticationService.signup(user)):
        return Response("There's already an account with the provided email.", status=400)

    return Response("Signup successful", status=200)




