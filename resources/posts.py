from flask_restful import Resource
from models import Post
from schemas import PostSchema
from utility import jsonResponse


class Posts(Resource):
    def get(self):
        try:
            return jsonResponse({"posts": PostSchema(many=True).dump(Post.query.all())}, 200)
        except Exception as e:
            return jsonResponse({"error": str(e)}, 400)
