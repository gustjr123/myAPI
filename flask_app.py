from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
# from datetime import datetime
# from werkzeug.utils import secure_filename
import dbModule
import os

app = Flask(__name__)
api = Api(app)

# UPLOAD_FOLDER_LOCATION = '/flask_api/app001/static/image'
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
# app.config['UPLOAD_FOLDER_LOCATION'] = UPLOAD_FOLDER_LOCATION

# # allowed_file 함수 > 허용된 형태의 파일 형식인지 확인
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello():
    temp = os.getcwd()
    return render_template('index.html', resultData=temp)

@app.route('/list')
def list():
    db_class = dbModule.Database()
    db_name = os.environ.get('DB_NAME')
    sql = "SELECT id, name, path FROM " + db_name + ".test"
    row = db_class.executeAll(sql)
    print(row)
    return render_template('test.html', resultData=row)

class Inputdata(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('path', type=str)
        args = parser.parse_args()

        name = args['name']
        path = args['path']
        val = (name, path)
        
        if name != "" and path != "" :
            db_class = dbModule.Database()
            db_name = os.environ.get('DB_NAME')
            sql = "INSERT INTO " + db_name + ".test(name, path) VALUES (%s, %s)"
            db_class.execute(sql, val)
            db_class.commit()

        return {'name': name, 'path': path}

api.add_resource(Inputdata, '/camera')

if __name__ == '__main__':
    app.run()

