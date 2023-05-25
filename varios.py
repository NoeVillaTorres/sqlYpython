import sqlite3
conexion=sqlite3.connect('ejemplo.db')
c=conexion.cursor()

movimientos= { ('24/nov2016,', 'venta', 'HPC', 50, 20.01), ('28/nov/2016', 'compra', 'sny', 100, 7.18), ('26/nov/2016', 'compra', 'xbx', 75,5.53) }
c.executemany('INSERT INTO acciones VALUES (?,?,?,?,?)', movimientos)
conexion.commit()

for row in c.execute("SELECT * FROM acciones"):
    print(row)

conexion.close()

for row in c.execute("SELECT * FROM acciones WHERE operacion='cimpra"):
    print(row)