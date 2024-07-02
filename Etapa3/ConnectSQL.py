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

    def consultar_cliente(self,codigo):
        #PreCondicion: Recibe un codigo de algúnn cliente
        #PostCondicion: Devuelve el cliente si existe o False si no existe
        self.cursor.execute(f"SELECT * FROM clientes WHERE Codigo = {codigo}")
        return self.cursor.fetchone()
    
    def modificar_cliente(self,codigo,nuevo_nombre,nuevo_apellidio,nuevo_email,nuevo_contraseña,nuevo_cumpleaños,nuevo_pais,nuevo_términos):
        #PreCondicion: Recibe un codigo de cliente junto a nuevos parametros a cambiar sobre este
        #PosCondicion: Devuelve el cliente modificiado sobre la base de datos
        sql = "UPDATE clientes SET nombre = %s, apellido = %s, email = %s, contraseña = %s, cumple = %s, pais = %s, términos = %s WHERE Codigo = %s"
        valores = (nuevo_nombre,nuevo_apellidio,nuevo_email,nuevo_contraseña,nuevo_cumpleaños,nuevo_pais,nuevo_términos)
        self.cursor.execute(sql,valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def mostrar_cliente(self,codigo):
        #PreCondicion: Recibe un cliente por su Codigo
        #PostCondicion: Devuelve el cliente si existe o "Cliente no encontrado" si no existe
        cliente = self.consultar_cliente(codigo)
        if cliente:
            print('-'*50)
            print(f'Codigo....: {cliente["Codigo"]}')
            print(f'Nombre....: {cliente["Nombre"]}')
            print(f'Apellido..: {cliente["Apellido"]}')
            print(f'Email.....: {cliente["Email"]}')
            print(f'Contraseña: {cliente["Contraseña"]}')
            print(f'Cumple....: {cliente["Cumple"]}')
            print(f'Pais......: {cliente["Pais"]}')
            print(f'Terminos..: {cliente["Términos"]}')
            print('-'*50)
        else:
            print('Cliente no encontrado')

    def listar_cliente(self):
        #PreCondicion: No recibe argumentos
        #PostCondicion: Al llamarse muestra todos los clientes registrados en la base de datos
        self.cursor.execute("SELECT * FROM clientes")
        clientes = self.cursor.fetchall()
        return clientes
    
    def eliminar_cliente(self,codigo):
        #PreCondicion: Recibe un cliente por su Codigo
        #PostCondicion: Elimina el cliente si existe y devuelvo True, o False si no existe
        self.cursor.execute(f"DELETE FROM clientes WHERE Codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0
    