from marshmallow import fields
from app import ma
from models import User
from models import Post
from models import Message


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        ordered = True

    posts = ma.Nested("PostSchema", many=True, exclude=["poster"])
    sentMessages = ma.Nested("MessageSchema", many=True, exclude=["sender"])
    receivedMessages = ma.Nested("MessageSchema", many=True, exclude=["receiver"])


class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post
        ordered = True

    poster = ma.Nested("UserSchema", only=["username"])


class MessageSchema(ma.ModelSchema):
    class Meta:
        model = Message
        ordered = True

    sender = ma.Nested("UserSchema", only=["username"])
    receiver = ma.Nested("UserSchema", only=["username"])
