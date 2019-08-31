from flask_restful import Resource, reqparse
from flask_login import login_user, current_user
from models import User
from utility import jsonResponse

parser = reqparse.RequestParser()

class Login(Resource):

    def post(self):
        parser.add_argument("username", required=True, help="Username required")
        parser.add_argument("password", required=True, help="Password required")
        args = parser.parse_args()
        username = args.get("username")
        password = args.get("password")
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
