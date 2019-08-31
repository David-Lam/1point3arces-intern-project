from flask_restful import Resource
from flask_login import login_required, current_user
from schemas import UserSchema
from models import User
from utility import jsonResponse


class Profile(Resource):
    @login_required
    def get(self):
        return jsonResponse({"user": UserSchema().dump(User.query.filter_by(id=current_user.id).first())}, 200)
