import sqlite3

from flask import Flask

app = Flask(__name__)

conn = sqlite3.connect('dbtest.db')
c = conn.cursor()
c.execute("select * from test")
list1 = c.fetchone()

print (list1)
print (list1[0])
print (list1[1])

conn.commit()
conn.close() 





if __name__ == "__main__":
    # Flask が持っている開発用サーバーを、実行します。
    app.run(debug=True)