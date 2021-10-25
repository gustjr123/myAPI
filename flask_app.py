from flask import Flask, render_template, request
from flask_restful import Resource, Api, reqparse
import numpy as np
import cv2
# from datetime import datetime
import werkzeug
import dbModule
import os

app = Flask(__name__)
api = Api(app)
Image_Path = os.getcwd() + '/images/'
# UPLOAD_FOLDER_LOCATION = '/flask_api/app001/static/image'
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
# app.config['UPLOAD_FOLDER_LOCATION'] = UPLOAD_FOLDER_LOCATION

# # allowed_file 함수 > 허용된 형태의 파일 형식인지 확인
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello():
    return render_template('index.html', resultData=Image_Path)

@app.route('/list')
def list():
    db_class = dbModule.Database()
    db_name = os.environ.get('DB_NAME')
    sql = "SELECT id, name, path FROM " + db_name + ".test"
    row = db_class.executeAll(sql)
    print(row)
    return render_template('test.html', resultData=row)

@app.route('/images', method)
def images() :
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        file_list = os.listdir(Image_Path)
        return render_template('image.html', File_List = file_list, Isfile = 0)

    return render_template('image.html', filepath = Image_Path + request.args['image'], Isfile = 1)

class Inputdata(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('path', type=str)
        parser.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files')
        args = parser.parse_args()

        name = args['name']
        path = args['path']
        image = args['image'].read()
        val = (name, path)

        if name != "" and path != "" :
            db_class = dbModule.Database()
            db_name = os.environ.get('DB_NAME')
            sql = "INSERT INTO " + db_name + ".test(name, path) VALUES (%s, %s)"
            db_class.execute(sql, val)
            db_class.commit()

            # convert to numpy array
            npimg = np.fromstring(image, np.uint8)
            # convert numpy array to image
            img = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)
            cv2.imwrite(Image_Path + name + '.png', img)

            return {'name': name, 'path': path, 'image': 'success'}

        return {'name': name, 'path': path}

# class Deletedata(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('name', type=str)
#         parser.add_argument('path', type=str)
#         args = parser.parse_args()
#
#         name = args['name']
#         path = args['path']
#         val = (name, path)
#
#         if name != "" and path != "" :
#             db_class = dbModule.Database()
#             db_name = os.environ.get('DB_NAME')
#             sql = "INSERT INTO " + db_name + ".test(name, path) VALUES (%s, %s)"
#             db_class.execute(sql, val)
#             db_class.commit()
#
#         return {'name': name, 'path': path}

api.add_resource(Inputdata, '/camera')

if __name__ == '__main__':
    app.run()

