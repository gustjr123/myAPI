from flask_restful import Resource, request
from Firebase import db, storage

class Inputdata(Resource):
    def post(self):
        name = request.form['name']
        date = request.form['date']
        image = request.files['image']

        file_name = name + '_' + date + '.png'

        if name != "" and date != "" :
            # database update
            db.child(name).child(date).push(file_name)
            storage.child(name + '/' + date + '/' + file_name).put(image)

            return {'name': name, 'date': date, 'image': 'success'}

        return {'name': name, 'date': date, 'image': 'fail'}