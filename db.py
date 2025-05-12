import cx_Oracle

def obtener_productos():
    conn = cx_Oracle.connect("usuario/contraseña@localhost/XE")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, precio FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return productos
