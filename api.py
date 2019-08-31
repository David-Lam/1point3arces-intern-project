from resources.posts import Posts
from resources.messages import Messages
from resources.register import Register, EmailConfirmation
from resources.login import Login
from resources.logout import Logout
from resources.profile import Profile
from models import User
from app import app, api
from app import loginManger
import utility

utility.reset()


@loginManger.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


api.add_resource(Posts, "/posts")
api.add_resource(Messages, "/messages")
api.add_resource(Register, "/register")
api.add_resource(EmailConfirmation, "/register/emailConfirmation/<string:token>")
api.add_resource(Login, "/login")
api.add_resource(Logout, "/logout")
api.add_resource(Profile, "/profile")

if __name__ == "__main__":
    app.run(debug=True)
