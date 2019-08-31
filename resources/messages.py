from flask_restful import Resource
from flask_login import login_required, current_user
from sqlalchemy import or_
from models import Message
from schemas import MessageSchema
from utility import jsonResponse


class Messages(Resource):
    @login_required
    def get(self):
        return jsonResponse({"messages": MessageSchema(many=True).dump(
            Message.query.filter(or_(Message.senderId == current_user.id, Message.receiverId == current_user.id)))}, 200)
