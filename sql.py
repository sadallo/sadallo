import sqlite3

with sqlite3.connect("sample.db") as connection:
	c = connection.cursor()
	c.execute("""DROP TABLE universidades""")
	c.execute("CREATE TABLE universidades(id INT, nome TEXT, sigla TEXT)")
	c.execute('INSERT INTO universidades VALUES(1, "UNIVERSIDADE FEDERAL DE ITAJUBA", "UNIFEI")')
	c.execute('INSERT INTO universidades VALUES(2, "UNIVERSIDADE FEDERAL DE JUIZ DE FORA", "UFJF")')
	c.execute('INSERT INTO universidades VALUES(3, "UNIVERSIDADE FEDERAL DE LAVRAS", "UFLA")')
	c.execute('INSERT INTO universidades VALUES(4, "UNIVERSIDADE FEDERAL DE MATO GROSSO", "UFMT")')
	c.execute('INSERT INTO universidades VALUES(5, "UNIVERSIDADE FEDERAL DE MINAS GERAIS ", "UFMG")')
	