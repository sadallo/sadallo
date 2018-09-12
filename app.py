from flask import Flask, render_template, g
from functools import wraps
import sqlite3

app = Flask(__name__)

app.database = "sample.db"

@app.route('/')
def home():
	return "Hello world"

@app.route('/universidade/<sigla>/')
def universidade_busca(sigla):
	g.db = connect_db()
	cur = g.db.execute("select * from universidades where sigla='%s'" % sigla.upper())
	universidades = [dict(sigla=row[2], nome=row[1]) for row in cur.fetchall()]
	g.db.close()
	return render_template("index.html", universidades=universidades)

def connect_db():
	return sqlite3.connect(app.database)


if __name__ == "__main__":
	app.run(debug=True)
