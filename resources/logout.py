from flask_restful import Resource
from flask_login import logout_user, login_required
from utility import jsonResponse


class Logout(Resource):

    @login_required
    def post(self):
        logout_user()
        return jsonResponse({"message": "Logged out successfully."}, 200)
