import os

import sqlite3

from flask import Flask, render_template, request, redirect, session

from werkzeug.utils import secure_filename

from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("toppage.html")









# ファイル容量上限 : 1MB
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

@app.route('/imageadd', methods=['GET'])
def get():
	return render_template('index.html', \
		title = 'Form Sample(get)', \
		message = '画像を選択して下さい。', \
		flag = False)

@app.route("/imageadd.html")
def imageadd():
	return render_template("imageadd.html")

@app.route('/imageadd', methods=['POST'])
def post():
	# ファイルのリクエストパラメータを取得
	f = request.files.get('image')
	# ファイル名を取得
	filename = secure_filename(f.filename)
	# ファイルを保存するディレクトリを指定
	filepath = 'static/img/' + filename
	# ファイルを保存する
	f.save(filepath)
	
	return render_template('index.html', \
		title = 'Form Sample(post)', \
		message = 'アップロードされた画像({})'.format(filename), \
		flag = True, \
		image_name = filename, \
		image_url = filepath)


@app.route("/imagetest.html")
def imagetest():
	return render_template("imagetest.html")

#送信てすと#
@app.route('/submitted', methods=['GET'])
def yetsubmitted():
	return render_template('imagetest.html', \
		title = 'Form Sample(get)', \
		message = '名前を入力して下さい。')

# postのときの処理	
@app.route('/submitted', methods=['POST'])
def submitted():
	name = request.form['name']
	return render_template('imagetest.html', \
		title = '入力ありがとう', \
		message = 'こんにちは、{}さん'.format(name))


@app.route("/imagebottun", methods=["POST"])
def imgbtn_post():
	name = request.form['imagebottun']
	return render_template('imagetest.html', \
	message2 = '{}'.format(name))

@app.route("/imagebottun2", methods=["POST"])
def imgbtn_post2():
	message3 = "あいうえお"
	return render_template('imagetest.html', message3 = message3)

@app.route("/radio",methods=["POST"])
def radio():
	if request.form.get("name") == "q10":
		


if __name__ == "__main__":
    # Flask が持っている開発用サーバーを、実行します。
    app.run(debug=True)