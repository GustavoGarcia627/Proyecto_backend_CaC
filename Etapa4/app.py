from flask import Flask,request,jsonify
from flask_cors import CORS
import mysql.connector
from werkzeug.utils import secure_filename

import os
import time

app = Flask(__name__)
CORS(app)

class Mascotas:
    #Constructor de la clase
    def __init__(self,host,user,password,database):
        self.conn = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.cursor = self.conn.cursor()
    
    #Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connecto.Error as err:
            #Si la base de datos no existe, La creamos->
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err
            
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cachorros(
            Codigo INT AUTO_INCREMENT PRIMARY KEY,
            Nombre VARCHAR(50) NOT NULL,
            Genero VARCHAR(50) NOT NULL,
            Edad VARCHAR(50) NOT NULL,
            imagen_url VARCHAR(255) NOT NULL)''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
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

    def eliminar_cachorro(self,codigo):
        sql = "DELETE FROM cachorros WHERE Codigo = %s"
        self.cursor.execute(sql,(codigo,))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------
#Creando una instancia de la clase Mascotas
mascotas = Mascotas('localhost','root','','basededatos')

#Carpeta para guardar las imagenes
ruta_destino = 'D:\ProyectoFinalBackEnd\Etapa4\static\imagenes'

@app.route("/cachorros", methods=["GET"])#passed
def listar_cachorros():
    cachorros = mascotas.listar_cachorros()
    return jsonify(cachorros)

@app.route("/cachorros/<int:codigo>", methods=["GET"])#passed
def mostrar_cachorro(codigo):
    cachorros = mascotas.consultar_cachorro(codigo)
    if cachorros:
        return jsonify(cachorros),201
    else:
        return 'Cachorro no encontrado', 404
    
@app.route("/cachorros", methods=["POST"])#Passed
def agregar_cachorro():
    #Recojo los datos del forumlario
    nombre = request.form["Nombre"]
    genero = request.form["Genero"]
    edad = request.form["Edad"]
    imagen = request.files["imagen_url"]
    nombre_imagen = ""

    #Genero el nombre de la imagen
    nombre_imagen = secure_filename(imagen.filename)  #Transforma el nombre de la imagen en uno seguro
    nombre_base,extension = os.path.splitext(nombre_imagen) #Separamos el nombre de la imagen y la extensión
    nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}" #Generamos el nombre de la imagen

    nuevo_codigo = mascotas.agregar_cachorro(nombre,genero,edad, nombre_imagen)
    if nuevo_codigo:
        imagen.save(os.path.join(ruta_destino, nombre_imagen))
        return jsonify({"mensaje" : "Producto agregado correctamente","codigo":nuevo_codigo,"imagen":nombre_imagen}),201
    else:
        return jsonify({"mensaje" : "Error al agregar el cachorro"}),500
    
@app.route("/cachorros/<int:codigo>", methods=["PUT"]) #passed  
def modificar_cachorro(codigo):
    #Se recuperan los nuevos datos del formulario
    nuevo_nombre = request.form.get("Nombre")
    nuevo_genero = request.form.get("Genero")
    nueva_edad = request.form.get("Edad")

    #Verificar si se mando una nueva imagen
    if 'imagen' in request.files:
        imagen = request.files['imagen']
        #Procesamiento de la imagen
        nombre_imagen = secure_filename(imagen.filename)
        nombre_base, extension = os.path.splitext(nombre_imagen)
        nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
        
        #guarda la imagen en el servidor
        imagen.save(os.path.join(ruta_destino, nombre_imagen))

        #Busco el cachorro guardado
        cachorro = mascotas.consultar_cachorro(codigo)

        if cachorro: #Si existe el cachorro en la base de datos...
            imagen_vieja = cachorro['imagen_url']
            #armo la ruta de la imagen
            ruta_imagen = os.path.join(ruta_destino,imagen_vieja)

            #Si existe la imagen la borro.
            if os.path.exists(ruta_imagen):
                os.remove(ruta_imagen)
    
    else:
        cachorro = mascotas.consultar_cachorro(codigo)
        if cachorro:
            nombre_imagen = cachorro['imagen_url']

    #Se llama al metodo modificar_cachorro pasando el codigo y los nuevos datos
    if mascotas.modificar_cachorro(codigo,nuevo_nombre,nuevo_genero,nueva_edad,nombre_imagen):
        return jsonify({"mensaje" : "Cachorro modificado correctamente"}),200
    else:
        return jsonify({"mensaje" : "Error al modificar el cachorro"}),403

@app.route("/cachorros/<int:codigo>", methods=["DELETE"])
def eliminar_cachorro(codigo):
    #Primero, se obtiene la informacion del cachorro para encontrar la imagen
    cachorro = mascotas.consultar_cachorro(codigo)
    if cachorro:
        #Eliminar la imagen asociada si existe
        ruta_imagen = os.path.join(ruta_destino, cachorro['imagen_url'])

        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)
        
        #Luego elimina el cachorro de la base de datos
        if mascotas.eliminar_cachorro(codigo):
            return jsonify({"mensaje" : "Cachorro eliminado correctamente"}),200
        else:
            return jsonify({"mensaje" : "Error al eliminar el cachorro"}),500
    else:
        return jsonify({"mensaje" : "Cachorro no encontrado"}),404
    
if __name__ == "__main__":
    app.run(debug=True)