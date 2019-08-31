from flask_login import UserMixin
from app import database
import datetime


class User(database.Model, UserMixin):
    __tablename__ = "user"
    id = database.Column("id", database.Integer, primary_key=True, autoincrement=True)
    username = database.Column("username", database.String(255), unique=True, nullable=False)
    password = database.Column("password", database.Text, nullable=False)
    email = database.Column("email", database.String(255), unique=True, nullable=False)
    posts = database.relationship("Post", backref="poster")
    sentMessages = database.relationship("Message", backref="sender", lazy="dynamic", foreign_keys="Message.senderId")
    receivedMessages = database.relationship("Message", backref="receiver", lazy="dynamic",
                                            foreign_keys="Message.receiverId")

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class Post(database.Model):
    __tablename__ = "post"
    id = database.Column("id", database.Integer, primary_key=True, autoincrement=True)
    posterId = database.Column("posterId", database.Integer, database.ForeignKey("user.id"))
    title = database.Column("title", database.Text, nullable=True)
    content = database.Column("content", database.Text, nullable=True)
    dateCreated = database.Column("dateCreated", database.DateTime, nullable=False, default=datetime.datetime.utcnow())
    dateUpdated = database.Column("dateUpdated", database.DateTime, nullable=False, default=datetime.datetime.utcnow(),
                                  onupdate=datetime.datetime.utcnow())

    def __init__(self, posterId, title, content):
        self.posterId = posterId
        self.title = title
        self.content = content


class Message(database.Model):
    __tablename__ = "message"
    id = database.Column("id", database.Integer, primary_key=True, autoincrement=True)
    senderId = database.Column("senderId", database.Integer, database.ForeignKey("user.id"))
    receiverId = database.Column("receiverId", database.Integer, database.ForeignKey("user.id"))
    content = database.Column("content", database.Text, nullable=True)
    date = database.Column("date", database.DateTime, nullable=False, default=datetime.datetime.utcnow())

    def __init__(self, senderId, receiverId, content):
        self.senderId = senderId
        self.receiverId = receiverId
        self.content = content
