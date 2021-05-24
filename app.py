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

@app.route("/step1money.html")
def step1money():
	return render_template("step1money.html")

@app.route("/step1money")
def step1money2():
	return render_template("step1money.html")

@app.route("/step1")
def step1money3():
	return render_template("step1money.html")

@app.route("/money")
def step1money4():
	return render_template("step1money.html")

@app.route("/step2health.html")
def step2health():
	return render_template("step2health.html")

@app.route("/step2health")
def step2healt2h():
	return render_template("step2health.html")

@app.route("/step2")
def step2health3():
	return render_template("step2health.html")

@app.route("/health")
def step2health4():
	return render_template("step2health.html")

@app.route("/step3family.html")
def step3family():
	return render_template("step3family.html")

@app.route("/step3family")
def step3family2():
	return render_template("step3family.html")

@app.route("/step3")
def step3family3():
	return render_template("step3family.html")

@app.route("/family")
def step3family4():
	return render_template("step3family.html")

@app.route("/step4work.html")
def step4work():
	return render_template("step4work.html")

@app.route("/step4work")
def step4work2():
	return render_template("step4work.html")

@app.route("/step4")
def step4work3():
	return render_template("step4work.html")

@app.route("/work")
def step4work4():
	return render_template("step4work.html")

@app.route("/step5hobby.html")
def step5hobby():
	return render_template("step5hobby.html")

@app.route("/step5hobby")
def step5hobby2():
	return render_template("step5hobby.html")

@app.route("/step5")
def step5hobby3():
	return render_template("step5hobby.html")

@app.route("/hobby")
def step5hobby4():
	return render_template("step5hobby.html")

@app.route("/step6modele.html")
def step6modele():
	return render_template("step6modele.html")

@app.route("/step6modele")
def step6modele2():
	return render_template("step6modele.html")

@app.route("/step6")
def step6modele3():
	return render_template("step6modele.html")

@app.route("/modele")
def step6modele4():
	return render_template("step6modele.html")

@app.route("/step7want.html")
def step7want():
	return render_template("step7want.html")

@app.route("/step7want")
def step7want2():
	return render_template("step7want.html")

@app.route("/step7")
def step7want3():
	return render_template("step7want.html")

@app.route("/want")
def step7want4():
	return render_template("step7want.html")






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




# ここまで大城のテストの為のコード
# ここまで大城のテストの為のコード


if __name__ == "__main__":
    # Flask が持っている開発用サーバーを、実行します。
    app.run(debug=True)