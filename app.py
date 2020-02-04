from flask import Flask, request
from flask_restful import Api, Resource
from redis import Redis

app = Flask(__name__)
api = Api(app)
redis = Redis(host='redis', port=6379)


# shows a single todo item and lets you delete a todo item
class Message(Resource):
    def get(self, id):
        # abort_if_todo_doesnt_exist(id)
        return redis.get(id)

    def post(self, id):
        print(request.data)
        redis.set(id, request.data)
        return redis.get(id)


##
# Actually setup the Api resource routing here
##
# api.add_resource(TodoList, '/todos')
api.add_resource(Message, '/todos/<id>')


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
