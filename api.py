from resources.posts import Posts
from resources.messages import Messages
from resources.register import Register
from resources.register import EmailConfirmation
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
api.add_resource(Register, "/register/<string:username>/<string:password>/<string:email>")
api.add_resource(Login, "/login/<string:username>/<string:password>")
api.add_resource(Logout, "/logout")
api.add_resource(Profile, "/profile")
api.add_resource(EmailConfirmation, "/emailConfirmation/<string:token>")

if __name__ == "__main__":
    app.run(debug=True)
