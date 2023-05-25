import sqlite3
conexion= sqlite3.connect('ejemplo.db')

c=conexion.cursor()
c.execute('''create table acciones (fecha text, operacion text, simbolo text, cantidad real, precio real)''')
c.execute("INSERT INTO acciones VALUES ('24/NOV/2016', 'compra', 'INV', 100, 15.43)" )