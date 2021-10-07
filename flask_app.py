from flask import Flask
import os
import subprocess
import time

app = Flask(__name__)

@app.route('/')
def hello():
    return os.environ['TEST_SECRET']

@app.route('/list')
def list():
    out = ""
    try:
        pid = subprocess.Popen(["ls", "-l"]).pid
        out = subprocess.check_output(["ls", "-l"])
    except EnvironmentError:
        os.kill(pid)
        print('unable to run subprocess')
        return
    return out

if __name__ == '__main__':
    app.run()



