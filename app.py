import os

import sqlite3

from flask import Flask, render_template, request, redirect, session

from werkzeug.utils import secure_filename

from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("toppage.html")

@app.route("/toppage.html")
def index2():
    return render_template("toppage.html")

@app.route("/toppage")
def index3():
    return render_template("toppage.html")

@app.route("/top")
def index4():
    return render_template("toppage.html")

@app.route("/index.html")
def index5():
    return render_template("toppage.html")

@app.route("/index")
def index6():
    return render_template("toppage.html")

@app.route("/home.html")
def index7():
    return render_template("toppage.html")

@app.route("/home")
def index8():
    return render_template("toppage.html")

@app.route("/aboutpage.html")
def about():
	return render_template("aboutpage.html")

@app.route("/aboutpage")
def about2():
	return render_template("aboutpage.html")

@app.route("/about")
def about3():
	return render_template("aboutpage.html")

step1 = "仮入れ"
step2 = "仮入れ"
step3 = "仮入れ"
step4 = "仮入れ"
step5 = "仮入れ"
step6 = "仮入れ"
step7 = "仮入れ"

@app.route("/step1money.html")
def step1money():
	return render_template("step1money.html")


@app.route("/step2health.html", methods=["POST"])
def step2health():
	global step1
	if request.form.get("q1") == "1":
		step1 = "../static/img/kate-images/step1money/1.jpg"
		return render_template("/step2health.html", step1 = step1)
	elif request.form.get("q1") == "2":
		step1 = "../static/img/kate-images/step1money/2.jpg"
		return render_template("/step2health.html", step1 = step1)
	elif request.form.get("q1") == "3":
		step1 = "../static/img/kate-images/step1money/3.jpg"
		return render_template("/step2health.html", step1 = step1)
	elif request.form.get("q1") == "4":
		step1 = "../static/img/kate-images/step1money/4.jpg"
		return render_template("/step2health.html", step1 = step1)
	elif request.form.get("q1") == "5":
		step1 = "../static/img/kate-images/step1money/5.jpg"
		return render_template("/step2health.html", step1 = step1)
	elif request.form.get("q1") == "6":
		step1 = "../static/img/kate-images/step1money/6.jpg"
		return render_template("/step2health.html", step1 = step1)
	else:
		please_select = "ボタンを選択してください"
		return render_template("/step1money.html", please_select = please_select)

@app.route("/step3family.html", methods=["POST"])
def step3family():
	global step1
	global step2
	if request.form.get("q2") == "1":
		step2 = "../static/img/kate-images/step2health/8.jpg"
		return render_template("/step3family.html", step1 = step1, step2 = step2)
	elif request.form.get("q2") == "2":
		step2 = "../static/img/kate-images/step2health/9.jpg"
		return render_template("/step3family.html", step1 = step1, step2 = step2)
	elif request.form.get("q2") == "3":
		step2 = "../static/img/kate-images/step2health/10.jpg"
		return render_template("/step3family.html", step1 = step1, step2 = step2)
	elif request.form.get("q2") == "4":
		step2 = "../static/img/kate-images/step2health/11.jpg"
		return render_template("/step3family.html", step1 = step1, step2 = step2)
	elif request.form.get("q2") == "5":
		step2 = "../static/img/kate-images/step2health/12.jpg"
		return render_template("/step3family.html", step1 = step1, step2 = step2)
	elif request.form.get("q2") == "6":
		step2 = "../static/img/kate-images/step2health/13.jpg"
		return render_template("/step3family.html", step1 = step1, step2 = step2)
	else:
		please_select = "ボタンを選択してください"
		return render_template("/step2health.html", please_select = please_select)

@app.route("/step4work.html", methods=["POST"])
def step4work():
	global step1
	global step2
	global step3
	if request.form.get("q3") == "1":
		step3 = "../static/img/kate-images/step3family/15.jpg"
		return render_template("/step4work.html", step1 = step1, step2 = step2,step3 = step3)
	elif request.form.get("q3") == "2":
		step3 = "../static/img/kate-images/step3family/16.jpg"
		return render_template("/step4work.html", step1 = step1, step2 = step2,step3 = step3)
	elif request.form.get("q3") == "3":
		step3 = "../static/img/kate-images/step3family/17.jpg"
		return render_template("/step4work.html", step1 = step1, step2 = step2,step3 = step3)
	elif request.form.get("q3") == "4":
		step3 = "../static/img/kate-images/step3family/18.jpg"
		return render_template("/step4work.html", step1 = step1, step2 = step2,step3 = step3)
	elif request.form.get("q3") == "5":
		step3 = "../static/img/kate-images/step3family/19.jpg"
		return render_template("/step4work.html", step1 = step1, step2 = step2,step3 = step3)
	elif request.form.get("q3") == "6":
		step3 = "../static/img/kate-images/step3family/20.jpg"
		return render_template("/step4work.html", step1 = step1, step2 = step2,step3 = step3)
	else:
		please_select = "ボタンを選択してください"
		return render_template("/step3family.html", please_select = please_select)

@app.route("/step5hobby.html", methods=["POST"])
def step5hobby():
	global step1
	global step2
	global step3
	global step4
	if request.form.get("q4") == "1":
		step4 = "../static/img/kate-images/step4work/22.jpg"
		return render_template("/step5hobby.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4)
	elif request.form.get("q4") == "2":
		step4 = "../static/img/kate-images/step4work/23.jpg"
		return render_template("/step5hobby.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4)
	elif request.form.get("q4") == "3":
		step4 = "../static/img/kate-images/step4work/24.jpg"
		return render_template("/step5hobby.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4)
	elif request.form.get("q4") == "4":
		step4 = "../static/img/kate-images/step4work/25.jpg"
		return render_template("/step5hobby.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4)
	elif request.form.get("q4") == "5":
		step4 = "../static/img/kate-images/step4work/26.jpg"
		return render_template("/step5hobby.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4)
	elif request.form.get("q4") == "6":
		step4 = "../static/img/kate-images/step4work/27.jpg"
		return render_template("/step5hobby.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4)
	else:
		please_select = "ボタンを選択してください"
		return render_template("/step4work.html", please_select = please_select)

@app.route("/step6modele.html", methods=["POST"])
def step6modele():
	global step1
	global step2
	global step3
	global step4
	global step5
	if request.form.get("q5") == "1":
		step5 = "../static/img/kate-images/step5hobby/29.jpg"
		return render_template("/step6modele.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5)
	elif request.form.get("q5") == "2":
		step5 = "../static/img/kate-images/step5hobby/30.jpg"
		return render_template("/step6modele.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5)
	elif request.form.get("q5") == "3":
		step5 = "../static/img/kate-images/step5hobby/31.jpg"
		return render_template("/step6modele.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5)
	elif request.form.get("q5") == "4":
		step5 = "../static/img/kate-images/step5hobby/32.jpg"
		return render_template("/step6modele.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5)
	elif request.form.get("q5") == "5":
		step5 = "../static/img/kate-images/step5hobby/33.jpg"
		return render_template("/step6modele.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5)
	elif request.form.get("q5") == "6":
		step5 = "../static/img/kate-images/step5hobby/34.jpg"
		return render_template("/step6modele.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5)
	else:
		please_select = "ボタンを選択してください"
		return render_template("/step5hobby.html", please_select = please_select)

@app.route("/step7want.html", methods=["POST"])
def step7want():
	global step1
	global step2
	global step3
	global step4
	global step5
	global step6
	if request.form.get("q6") == "1":
		step6 = "../static/img/kate-images/step6modele/36.jpg"
		return render_template("/step7want.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5, step6 = step6)
	elif request.form.get("q6") == "2":
		step6 = "../static/img/kate-images/step6modele/37.jpg"
		return render_template("/step7want.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5, step6 = step6)
	elif request.form.get("q6") == "3":
		step6 = "../static/img/kate-images/step6modele/38.jpg"
		return render_template("/step7want.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5, step6 = step6)
	elif request.form.get("q6") == "4":
		step6 = "../static/img/kate-images/step6modele/39.jpg"
		return render_template("/step7want.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5, step6 = step6)
	elif request.form.get("q6") == "5":
		step6 = "../static/img/kate-images/step6modele/40.jpg"
		return render_template("/step7want.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5, step6 = step6)
	elif request.form.get("q6") == "6":
		step6 = "../static/img/kate-images/step6modele/41.jpg"
		return render_template("/step7want.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5, step6 = step6)
	else:
		please_select = "ボタンを選択してください"
		return render_template("/step6modele.html", please_select = please_select)

@app.route("/finalpage.html", methods=["POST"])
def finalpage():
	global step1
	global step2
	global step3
	global step4
	global step5
	global step6
	global step7
	if request.form.get("q7") == "1":
		step7 = "../static/img/kate-images/step7want/43.jpg"
		return render_template("/finalpage.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5, step6 = step6, step7 = step7)
	elif request.form.get("q7") == "2":
		step7 = "../static/img/kate-images/step7want/44.jpg"
		return render_template("/finalpage.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5, step6 = step6, step7 = step7)
	elif request.form.get("q7") == "3":
		step7 = "../static/img/kate-images/step7want/45.jpg"
		return render_template("/finalpage.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5, step6 = step6, step7 = step7)
	elif request.form.get("q7") == "4":
		step7 = "../static/img/kate-images/step7want/46.jpg"
		return render_template("/finalpage.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5, step6 = step6, step7 = step7)
	elif request.form.get("q7") == "5":
		step7 = "../static/img/kate-images/step7want/47.jpg"
		return render_template("/finalpage.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5, step6 = step6, step7 = step7)
	elif request.form.get("q7") == "6":
		step7 = "../static/img/kate-images/step7want/48.jpg"
		return render_template("/finalpage.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5, step6 = step6, step7 = step7)
	else:
		please_select = "ボタンを選択してください"
		return render_template("/step7want.html", please_select = please_select)

@app.route("/visionBoard.html", methods=["POST"])
def visionBoard():
	board_name = request.form.get("user_name")
	global step1
	global step2
	global step3
	global step4
	global step5
	global step6
	global step7
	return render_template("/visionBoard.html", step1 = step1, step2 = step2,step3 = step3, step4 = step4, step5 = step5, step6 = step6, step7 = step7, board_name = board_name)

@app.errorhandler(403)
def mistake403(code):
    return 'There is a mistake in your url! 403エラーだよ'


@app.errorhandler(404)
def notfound404(code):
    return "404だよ！！見つからないよ！！！"





# ここから大城のテストの為のコード
# ここから大城のテストの為のコード

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
	if request.form.get("q1") == "はい":
		ans = "はい"
		return render_template("/imagetest.html",ans = ans)
	elif request.form.get("q1") == "いいえ":
		ans = "いいえ"
		return render_template("/imagetest.html",ans = ans)
	else:
		ans = "どちらでもない"
		return render_template("/imagetest.html",ans = ans)

@app.route("/radio2",methods=["POST"])
def radio2():
	if request.form.get("q1") == "はい":
		url = "../static/img/icon.jpeg"
		return render_template("/imagetest.html",url = url)
	elif request.form.get("q1") == "いいえ":
		url = "../static/img/画像１.jpg"
		return render_template("/imagetest.html",url = url)
	else:
		url = "../static/img/画像２.jpg"
		return render_template("/imagetest.html",url = url)

@app.route("/imagetest2.html")
def imagetest2():
	return render_template("imagetest2.html")

@app.route("/imagetest2", methods=["POST"])
def imagetest3():
	if request.form.get("q1") == "1":
		url = "../static/img/kate-images/kate1-money/1.jpg"
		return render_template("imagetest.html",url = url)
	elif request.form.get("q1") == "2":
		url = "../static/img/kate-images/kate1-money/2.jpg"
		return render_template("imagetest.html",url = url)
	elif request.form.get("q1") == "3":
		url = "../static/img/kate-images/kate1-money/3.jpg"
		return render_template("imagetest.html",url = url)
	elif request.form.get("q1") == "4":
		url = "../static/img/kate-images/kate1-money/4.jpg"
		return render_template("imagetest.html",url = url)
	elif request.form.get("q1") == "5":
		url = "../static/img/kate-images/kate1-money/5.jpg"
		return render_template("imagetest.html",url = url)
	elif request.form.get("q1") == "6":
		url = "../static/img/kate-images/kate1-money/6.jpg"
		return render_template("imagetest.html",url = url)
	else:
		inputagain = "写真を選択してください"
		return render_template("imagetest.html", inputagain = inputagain)

@app.route("/imagetest3", methods=["POST"])
def imagetest4():
	if request.form.get("q2") == "1":
		url2 = "../static/img/kate-images/kate1-money/1.jpg"
		return render_template("imagetest2.html",url2 = url2)
	elif request.form.get("q2") == "2":
		url2 = "../static/img/kate-images/kate1-money/2.jpg"
		return render_template("imagetest2.html",url2 = url2)
	elif request.form.get("q2") == "3":
		url2 = "../static/img/kate-images/kate1-money/3.jpg"
		return render_template("imagetest2.html",url2 = url2)
	elif request.form.get("q2") == "4":
		url2 = "../static/img/kate-images/kate1-money/4.jpg"
		return render_template("imagetest2.html",url2 = url2)
	elif request.form.get("q2") == "5":
		url2 = "../static/img/kate-images/kate1-money/5.jpg"
		return render_template("imagetest2.html",url2 = url2)
	elif request.form.get("q2") == "6":
		url2 = "../static/img/kate-images/kate1-money/6.jpg"
		return render_template("imagetest2.html",url2 = url2)
	else:
		inputagain = "写真を選択してください"
		return render_template("imagetest2.html", inputagain = inputagain)

@app.route("/dbtest.html")
def dbtest():
	return render_template("dbtest.html")

@app.route("/dbtest", methods=["POST"])
def dbtest2():
	if request.form.get("dbtest") == "1":
		i = 1
		conn = sqlite3.connect('vision.db')
		c = conn.cursor()
		c.execute("select path from iamges where id = ?",(i,) )
		path = c.fetchone()
		conn.commit()
		conn.close()
		return render_template("dbtest.html", path = path)
	elif request.form.get("dbtest") == "2":
		i = 2
		conn = sqlite3.connect('vision.db')
		c = conn.cursor()
		c.execute("select path from iamges where id = ?",(i,) )
		path = c.fetchone()
		conn.commit()
		conn.close()
		return render_template("dbtest.html", path = path)
	elif request.form.get("dbtest") == "3":
		i = 3
		conn = sqlite3.connect('vision.db')
		c = conn.cursor()
		c.execute("select path from iamges where id = ?",(i,) )
		path = c.fetchone()
		conn.commit()
		conn.close()
		return render_template("dbtest.html", path = path)
	elif request.form.get("dbtest") == "4":
		i = 4
		conn = sqlite3.connect('vision.db')
		c = conn.cursor()
		c.execute("select path from iamges where id = ?",(i,) )
		path = c.fetchone()
		conn.commit()
		conn.close()
		return render_template("dbtest.html", path = path)
	elif request.form.get("dbtest") == "5":
		i = 5
		conn = sqlite3.connect('vision.db')
		c = conn.cursor()
		c.execute("select path from iamges where id = ?",(i,) )
		path = c.fetchone()
		conn.commit()
		conn.close()
		return render_template("dbtest.html", path = path)
	elif request.form.get("dbtest") == "6":
		i = 6
		conn = sqlite3.connect('vision.db')
		c = conn.cursor()
		c.execute("select path from iamges where id = ?",(i,) )
		path = c.fetchone()
		conn.commit()
		conn.close()
		return render_template("dbtest.html", path = path)
	else:
		please_select = "ボタンを選択してください"
		return render_template("dbtest.html", please_select = please_select)

@app.route("/inttest", methods=["POST"])
def inttest():
	get_int = request.form.get("name")
	return_int = int(get_int) + 10
	return render_template("/imagetest2.html",return_int)


@app.route("/dbtest3",methods=["POST"])
def dbtest3():
	name = request.form.get("name")
	dbtestp = "データベースてすと"
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute("insert into testtable values(name)",(name,))
	i = c.fetchone()
	path = c.fetchone()
	conn.commit()
	conn.close()
	return render_template("dbtest.html",dbtestp)

@app.route("/dbtest4",methods=["POST"])
def dbtest4():
	name = request.form.get("name")
	password = request.form.get("password")
	conn = sqlite3.connect('dbtest.db')
	c = conn.cursor()
	c.execute("insert into test values(null,?,?)", (name,password))
	conn.commit()
	conn.close()
	return redirect('/dbtest.html')

@app.route("/dbtest5",methods=["POST"])
def dbtest5():
	image_id = int(request.form.get('dbtest','')) #ラジオボタンのvalueの値を数値にして変数に格納。DBで使う
	conn = sqlite3.connect('dbtest.db')
	c = conn.cursor()
	c.execute("select path from image where imageid = ?",(image_id,))
	image_path = c.fetchone()
	step1 = image_path[0]
	# conn.commit()
	conn.close()
	return render_template("/dbtest.html", step1 = step1)



# c.execute("select id from user where name = ? and password = ?", (name, password) )
# ここまで大城のテストの為のコード
# ここまで大城のテストの為のコード


if __name__ == "__main__":
    # Flask が持っている開発用サーバーを、実行します。
    app.run(debug=True)

