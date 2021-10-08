import pymysql
import os

class Database():
    def __init__(self):
        DB_user = os.environ.get('DB_USER')
        DB_pass = os.environ.get('DB_PASSWORD')
        DB_name = os.environ.get('DB_NAME')
        DB_host = os.environ.get('DB_HOST')

        self.db = pymysql.connect(host=DB_host,
                                  user=DB_user,
                                  password=DB_pass,
                                  db=DB_name,
                                  charset='utf8')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()
