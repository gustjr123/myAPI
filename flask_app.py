from flask import Flask, render_template
import dbModule
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/list')
def list():
    db_class = dbModule.Database()
    db_name = os.environ.get('DB_NAME')
    sql = "SELECT id, name FROM " + db_name + ".members"
    row = db_class.executeAll(sql)

    print(row)

    return render_template('test.html', resultData=row)

if __name__ == '__main__':
    app.run()

