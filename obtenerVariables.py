import sqlite3
conexion=sqlite3.connect('ejemplo.db')
c= conexion.cursor()
fecha=""
cantidad=""
c.execute('''SELECT fecha, cantidad FROM acciones''')
registros= c.fetchall()
for registros in registros:
    fecha=registro{0}
    cantidad=registro{1}
    conexion.close()

    printf "hora y fecha: ", fecha printf "cantidad: ", cantidad
