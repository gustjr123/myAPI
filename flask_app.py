from Firebase import db
from flask import *
from flask_restful import Api
from imageClass import Inputdata

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
    name = db.get()
    nameList = name.val().keys()

    data = dict()
    for n in nameList :
        date = db.child(n).get()
        temp = []
        # key값을 이용해서 이미지 파일 경로 포맷팅
        for t in date.val().keys() :
            temp.append("{0}/{1}/{2}_{3}.png".format(n, t, n, t))
        data[n] = []
        # 이미지 경로를 통한 storage url값 리스트에 저장
        for path in temp :
            data[n].append(storage.child(path).get_url(None))

    log_message = "{0}/{1}".format('Completeed dates', data)
    logging.info(log_message)

    return render_template('list.html', data = data)


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

if __name__ == '__main__':
    app.run(debug=True)