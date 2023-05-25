import sqlite3
conexion= sqlite3.connect('ejemplo.db')
c=conexion.cursor()
c.execute("SELECT * FROM acciones")
print (c.fetchone())
conexion.close()