import mysql.connector

class Cachorros:
    def __init__(self,host,user,password,database):
        self.conn = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cachorros(
            Codigo INT AUTO_INCREMENT PRIMARY KEY,
            Nombre VARCHAR(50) NOT NULL,
            Genero VARCHAR(50) NOT NULL,
            Edad VARCHAR(50) NOT NULL,
            imagen_url VARCHAR(255) NOT NULL)''')
        self.conn.commit()

    def agregar_cachorro(self,nombre,genero,edad,imagen_url):
        sql = "INSERT INTO cachorros (Nombre,Genero,Edad,imagen_url) VALUES (%s,%s,%s,%s)"
        valores = (nombre,genero,edad,imagen_url)
        self.cursor.execute(sql,valores)
        self.conn.commit()
        return self.cursor.lastrowid
    
    def consultar_cachorro(self,codigo):
        self.cursor.execute(f"SELECT * FROM cachorros WHERE Codigo = {codigo}")
        return self.cursor.fetchone()

    def modificar_cachorro(self,codigo,nuevo_nombre,nuevo_genero,nueva_edad,nueva_imagen_url):
        sql = "UPDATE cachorros SET Nombre = %s, Genero = %s, Edad = %s, imagen_url = %s WHERE codigo = %s"
        valores = (nuevo_nombre,nuevo_genero,nueva_edad,nueva_imagen_url,codigo)
        self.cursor.execute(sql,valores)
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def mostrar_cachorro(self,codigo):
        cachorro = self.consultar_cachorro(codigo)
        if cachorro:
            print('-'*50)
            print(f'Codigo....: {cachorro["Codigo"]}')
            print(f'Nombre....: {cachorro["Nombre"]}')
            print(f'Apellido..: {cachorro["Genero"]}')
            print(f'Email.....: {cachorro["Edad"]}')
            print(f'Imagen....: {cachorro["imagen_url"]}')
            print('-'*50)
        else:
            print('Cachorro no encontrado')

    def listar_cachorros(self):
        self.cursor.execute("SELECT * FROM cachorros")
        return self.cursor.fetchall()

    def borrar_cachorro(self,codigo):
        sql = "DELETE FROM cachorros WHERE Codigo = %s"
        self.cursor.execute(sql,(codigo,))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
