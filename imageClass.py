from flask_restful import Resource, request
from Firebase import storage

class Inputdata(Resource):
    def post(self):
        name = request.form['name']
        date = request.form['date']
        image = request.files['image']
        time = request.form['time']
        id = request.form['Id']

        file_name = name + '_' + date + '_' + time + '.png'

        if name != "" and date != "" :
            # database update
            storage.child(name + '/' + date + '/' + file_name).put(image)

            return {'name': name, 'date': date, 'image': 'success'}

        return {'error': 'please input data consist of [name, date, time, image, Id]'}