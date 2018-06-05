from flask import Flask, g
from flask.ext.restful import Api, Resource, reqparse, abort
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
serializer = Serializer(app.config['SECRET_KEY'], expires_in=1800)

api = Api(app)
auth = HTTPTokenAuth(scheme='Bearer')

USER_LIST = {
    1: {'name':'Michael'},
    2: {'name':'Tom'},
}

for user_id in USER_LIST.keys():
    token = serializer.dumps({'id': user_id})
    print('Token for {}: {}\n'.format(USER_LIST[user_id]['name'], token))

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)

@auth.verify_token
def verify_token(token):
    g.user = None
    try:
        data = serializer.loads(token)
    except:
        return False
    if 'id' in data:
        g.user = USER_LIST[data['id']]['name']
        return True
    return False

def abort_if_not_exist(user_id):
    if user_id not in USER_LIST:
        abort(404, message="User {} doesn't exist".format(user_id))

class User(Resource):
    decorators = [auth.login_required]

    def get(self, user_id):
        abort_if_not_exist(user_id)
        return USER_LIST[user_id]

    def delete(self, user_id):
        abort_if_not_exist(user_id)
        del USER_LIST[user_id]
        return '', 204

    def put(self, user_id):
        args = parser.parse_args(strict=True)
        USER_LIST[user_id] = {'name': args['name']}
        return USER_LIST[user_id], 201

class UserList(Resource):
    decorators = [auth.login_required]

    def get(self):
        return USER_LIST

    def post(self):
        args = parser.parse_args(strict=True)
        user_id = int(max(USER_LIST.keys())) + 1
        USER_LIST[user_id] = {'name': args['name']}
        return USER_LIST[user_id], 201

api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<int:user_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)