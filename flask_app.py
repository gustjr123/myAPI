from Firebase import db
from flask import *
from flask_restful import Api
from imageClass import Inputdata
from personClass import Updateperson

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        db.child('todo').push(name)
        todo = db.child('todo').get()
        todo_list = todo.val()
        return render_template('index.html', todo=todo_list.values())
    return render_template('index.html')

@app.route('/list', methods=['POST', 'GET'])
def list():
    name = db.child('person').get()
    nameList = name.val().keys()

    data = dict()
    for n in nameList:
        urls = db.child('person').child(n).child('data').get()
        temp = []
        for url in urls.each():
            temp.append(url.val())
        data[n] = temp

    return render_template('list.html', data=data)


@app.route('/test', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        name = request.form['name']
        db.child('todo').push(name)
        todo = db.child('todo').get()
        todo_list = todo.val()
        return render_template('index.html', todo=todo_list.values())
    return render_template('index.html')

api.add_resource(Inputdata, '/image')
api.add_resource(Updateperson, '/person')

if __name__ == '__main__':
    app.run(debug=True)