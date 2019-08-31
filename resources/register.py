from flask_restful import Resource
from flask_mail import Message
from sqlalchemy import exc
from smtplib import SMTPRecipientsRefused
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature
from app import mail, api
from models import User
from schemas import UserSchema
from app import database
from config import SECRET_KEY
from utility import jsonResponse

serializer = URLSafeTimedSerializer(SECRET_KEY)

class Register(Resource):
    def get(self, username, password, email):
        return self.post(username, password, email)

    def post(self, username, password, email):
        if (username == None or password == None or email == None):
            return jsonResponse({"error": "Information can't be null."}, 400)
        if (len(username) > 255 or len(password) > 255 or len(email) > 255):
            return jsonResponse({"error": "The length of information can't excess 255 characters."}, 400)
        if User.query.filter_by(username=username).first() is not None:
            return jsonResponse({"error": "Username had been taken"}, 400)
        elif User.query.filter_by(email=email).first() is not None:
            return jsonResponse({"error": "Email had been taken"}, 400)
        newUser = User(username, password, email)
        token = serializer.dumps(UserSchema().dump(newUser), salt="emailConfirmation")
        msg = Message("Confirm Email", sender="yuensengd@gmail.com", recipients=[email])
        link = api.url_for(EmailConfirmation, token=token, _external=True)
        msg.body = ("Click on the link:" + link + " to confirm your email.")
        try:
            mail.send(msg)
        except SMTPRecipientsRefused:
            return jsonResponse({"error": "Invalid email."}, 400)
        return jsonResponse({"message": "The email confirmation was sent"}, 202)


class EmailConfirmation(Resource):
    def get(self, token):
        try:
            accountInfo = serializer.loads(token, salt="emailConfirmation", max_age=600)
            newUser = User(accountInfo["username"], accountInfo["password"], accountInfo["email"])
            database.session.add(newUser)
            database.session.commit()
        except SignatureExpired:
            return jsonResponse({"error": "Token expired"}, 498)
        except BadTimeSignature:
            return jsonResponse({"error": "Token is invalid"}, 400)
        except exc.IntegrityError:
            return jsonResponse({"error": "Account is already created"}, 400)
        except Exception as e:
            return jsonResponse({"error": str(e)}, 400)
        return jsonResponse({"message": "Account created successfully"}, 201)