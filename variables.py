import sqlite3
import time

conexion=sqlite3.connect('ejemplo.db')
c=conexion.cursor()
fecha=time.ctime()
operacion='compra'
simbolo='IMB'
cantidad=50
precio=13.23

movimientos= { (fecha, operacion, simbolo, cantidad, precio) }
c.executemany('INSERT INTO acciones VALUES (?,?,?,?,?)', movimientos)
conexion.close()