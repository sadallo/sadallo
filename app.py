from flask import Flask, render_template, g
from functools import wraps
import sqlite3

app = Flask(__name__)

app.database = "sample.db"


@app.route('/')
def home():
	g.db = connect_db()
	cur = g.db.execute('select * from posts')
	posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
	g.db.close()
	return render_template("index.html", posts=posts)

@app.route('/universidade/<sigla>/')
def universidade_busca(sigla):
	return 'vou pesquisar %s' % sigla

@app.route('/universidade/')
def universidade():
	return 'Insira uma sigla de alguma universidade federal na url. <br>Exemplo: sadallo.herokuapp.com/universidade/ufmg'

'''@app.route('/welcome/')
def welcome():
	return render_template("welcome.html")'''
def connect_db():
	return sqlite3.connect(app.database)


if __name__ == "__main__":
	app.run(debug=True)
