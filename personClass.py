from flask_restful import Resource, request
from Firebase import db, storage

class Updateperson(Resource):
    def post(self):
        name = request.form['name']
        date = request.form['date']
        time = request.form['time']
        id = request.form['Id']

        file_name = name + '_' + date + '_' + time + '.png'

        if name != "" and date != "" and id != "" and time != "":
            # 추가된 이미지 url 소스
            url = storage.child(name + '/' + date + '/' + file_name).get_url(None)

            # 현재 입력 사람이 존재하는지 확인
            all_users = db.child("person").get()
            existUser = False
            for user in all_users.each():
                if (user.key() == name) :
                    existUser = True
                    break
            # 존재여부에 따라 입력값 설정
            datas = dict()
            if existUser :
                all_user_data = db.child("person").child(name).child("data").get()
                for data in all_user_data.each() :
                    datas[data.key()] = data.val()
            datas[date] = url

            # database update
            db.child("person").child(name).child("id").set(id)
            db.child("person").child(name).child("name").set(name)
            db.child("person").child(name).child("data").set(datas)

            return {'name': name, 'date': date}

        return {'error': 'please input data consist of [name, date, time, Id]'}