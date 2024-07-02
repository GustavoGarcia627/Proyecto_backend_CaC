import mysql.connector

class Clientela:
    def __init__(self,host,user,password,database):

        self.conn = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes(
            Codigo INT AUTO_INCREMENT PRIMARY KEY,
            Nombre VARCHAR(50) NOT NULL,
            Apellido VARCHAR(50) NOT NULL,
            Email VARCHAR(50) NOT NULL,
            Contraseña VARCHAR(50) NOT NULL,
            Cumple DATE NOT NULL,
            Pais VARCHAR(50) NOT NULL,
            Términos BOOLEAN NOT NULL)''')
        self.conn.commit()

    def agregar_cliente(self,nombre,apellido,email,contraseña,cumpleaños,pais,terminos):
        sql = "INSERT INTO clientes (nombre,apellido,email,contraseña,cumple,pais,términos) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        valores = (nombre,apellido,email,contraseña,cumpleaños,pais,terminos)
        self.cursor.execute(sql,valores)
        self.conn.commit()
        return self.cursor.lastrowid

prueba = Clientela(host="localhost",user="root",password="",database="basededatos")

prueba.agregar_cliente('Jonathan','Perez','perez@perez','1234','1998-12-05','Colombia',True)