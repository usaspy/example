#!/usr/bin/python
import flask
import flask.ext.httpauth

import ssl

auth = flask.ext.httpauth.HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'ok':
        return 'python'
    return None



@auth.error_handler
def unauthorzied():
    return flask.make_response(flask.jsonify({'error':'Unauthorized access'}),401)

app = flask.Flask(__name__)
app.config['JSON_AS_ASCII'] = False

tasks = [{
        'id':1,
        'taskName':'Python',
        'description':'学习新知识',
        'done':False
    },
    {
        'id':2,
        'taskName':'stock',
        'description':'这不是一个好的爱好',
        'done':False
    }]

list = ['zhang','lulu','luran']

#测试
@app.route('/')
def index():
    return "哈喽 Restuful API!"

#查看所有任务
@app.route('/justdoit/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def getTasks():
    return flask.jsonify({'tasks': tasks})

#查看指定任务
@app.route('/justdoit/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def getTaskById(task_id):
    re = []
    for i in tasks:
        if i['id'] == task_id:
           re.append(i)

    if len(re) == 0:
        flask.abort(404)
    return flask.jsonify({'task': re})

#HTTP 404封装
@app.errorhandler(404)
def not_found(error):
    return flask.make_response(flask.jsonify({'error': 'Not found'}), 404)

#HTTP 400封装
@app.errorhandler(400)
def not_found(error):
    return flask.make_response(flask.jsonify({'error': 'Add failed','desc':'数据格式不正确'}), 404)


#添加新的任务
@app.route('/justdoit/api/v1.0/tasks', methods=['POST'])
@auth.login_required
def addTask():
    if not flask.request.json or not 'taskName' in flask.request.json:
        flask.abort(400)
    task = {
        'id':tasks[-1]['id'] + 1,
        'taskName': flask.request.json['taskName'],
        'description': flask.request.json['description'],
        'done': False
    }
    tasks.append(task)
    return flask.jsonify({'tasks':tasks}),201

#修改任务
@app.route('/justdoit/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def updateTask(task_id):
    task = {}
    for i in tasks:
        if i['id'] == task_id:
           task = i
           break
    if task == {}:
        flask.abort(404)
    if not flask.request.json:
        flask.abort(400)
    if 'taskName' not in flask.request.json or type(flask.request.json['taskName']) is not str:
        flask.abort(400)
    if 'done' not in flask.request.json or type(flask.request.json['done']) is not bool:
        flask.abort(400)
    task['taskName'] = flask.request.json['taskName']
    task['done'] = flask.request.json.get('done',task['done'])

    return flask.jsonify({'tasks':task})

#删除任务
@app.route('/justdoit/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def deleteTask(task_id):
    task = []
    for i in tasks:
        if i['id'] == task_id:
            task.append(i)
            break
    if len(task) != 1:
        flask.abort(404)
    tasks.remove(task[0])
    return flask.jsonify({'result': tasks})



if __name__ == '__main__':
    app.run(host='localhost',port=999,debug=True, ssl_context='adhoc')