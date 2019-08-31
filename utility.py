from flask import jsonify
from models import User
from models import Post
from models import Message
from app import database


def importData():
    new_user1 = User("tester1", "testing1", "tester1@email.com")
    database.session.add(new_user1)
    new_user2 = User("tester2", "testing2", "tester2@email.com")
    database.session.add(new_user2)
    new_user3 = User("tester3", "testing3", "tester3@email.com")
    database.session.add(new_user3)
    new_post1 = Post(1, "title1", "Content1 by tester1")
    database.session.add(new_post1)
    new_post2 = Post(1, "title2", "Content2 by tester1")
    database.session.add(new_post2)
    new_post2 = Post(2, "title3", "Content2 by tester2")
    database.session.add(new_post2)
    new_message1 = Message(1, 2, "Hello Tester2")
    database.session.add(new_message1)
    new_message2 = Message(2, 1, "Hello Tester1")
    database.session.add(new_message2)
    new_message3 = Message(3, 1, "Hello Tester1")
    database.session.add(new_message3)
    database.session.commit()


def jsonResponse(object, statusCode):
    response = jsonify(object)
    response.status_code = statusCode
    return response


def reset():
    database.drop_all()
    database.create_all()
    importData()
