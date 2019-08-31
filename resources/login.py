from flask_restful import Resource
from flask_login import login_user, current_user
from models import User
from utility import jsonResponse


class Login(Resource):
    def get(self, username, password):
        return self.post(username, password)

    def post(self, username, password):
        if current_user.is_authenticated:
            return jsonResponse({"error": "You are already logged in."}, 400)
        try:
            user = User.query.filter_by(username=username).first()
        except Exception as e:
            return jsonResponse({"error": str(e)}, 400)
        if user != None and user.password == password:
            login_user(user)
            return jsonResponse({"message": "Logged in successfully."}, 200)
        else:
            return jsonResponse({"error": "Invalid username or password."}, 400)
