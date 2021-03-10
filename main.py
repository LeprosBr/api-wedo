from flask import Flask
from flask_restful import Api, Resource, reqpars

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", tyoer=str, help="Name of the video")
video_put_args.add_argument("views", tyoer=str, help="Views of the video")
video_put_args.add_argument("likes", tyoer=str, help="Likes of the video")


videos = {}


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        print(request.form['likes'])
        return


api.add_resource(Video, "/video/<int:video_id>")


if __name__ == "__main__":
    app.run(debug=True)
