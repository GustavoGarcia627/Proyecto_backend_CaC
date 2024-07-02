clientes = []

#FUNCIONES A DESRROLLAR:
#1. Registrar un cliente
#2. Consultar un cliente a partir de su codigo único
#3. Modificar un cliente a partir de su codigo único
#4. Mostrar todos los clientes que existen en el arreglo
#5. Eliminar un cliente del arreglo

def agregar_cliente(codigo,nombre,apellido,email,contraseña,cumpleaños,pais,terminos):
    #PreCondicion: Recibe parametros únicos de un cliente (Codigo,nombre,apellido,email,contraseña,cumpleaños,pais,terminos)
    #PostCondicion: Agrega un nuevo cliente a la base de datos devolviendo True si se agregó exitosamente y False si el cliente ya existía
    if consultar_cliente(codigo):
        return False
    
    nuevo_cliente = {
        'Codigo': codigo,
        'Nombre': nombre,
        'Apellido': apellido,
        'Email': email,
        'Contraseña': contraseña,
        'Cumple': cumpleaños,
        'Pais': pais,
        'Términos': terminos
    }
    clientes.append(nuevo_cliente)
    return True

def consultar_cliente(codigo):
    #PreCondicion: Recibe un cliente por su Codigo
    #PostCondicion: Devuelve el cliente si existe o False si no existe
    for cliente in clientes:
        if cliente['Codigo'] == codigo:
            return cliente
    return False

def modificar_cliente(codigo,nombre,apellido,email,contraseña,cumpleaños,pais,terminos):
    #PreCondicion: Recibe un cliente por su Codigo
    #PostCondicion: Modifica el cliente si existe o False si no existe
    for cliente in clientes:
        if cliente['Codigo'] == codigo:
            cliente['Nombre'] = nombre
            cliente['Apellido'] = apellido
            cliente['Email'] = email
            cliente['Contraseña'] = contraseña
            cliente['Cumple'] = cumpleaños
            cliente['Pais'] = pais
            cliente['Términos'] = terminos
            return True
    return False

def mostrar_clientes():
    #PreCondicion: No recibe argumentos
    #PostCondicion: Al llamarse muestra todos los clientes registrados en el arreglo
    print('-'*50)
    for cliente in clientes:
        print(f'Codigo....: {cliente["Codigo"]}')
        print(f'Nombre....: {cliente["Nombre"]}')
        print(f'Apellido..: {cliente["Apellido"]}')
        print(f'Email.....: {cliente["Email"]}')
        print(f'Contraseña: {cliente["Contraseña"]}')
        print(f'Cumple....: {cliente["Cumple"]}')
        print(f'Pais......: {cliente["Pais"]}')
        print(f'Terminos..: {cliente["Términos"]}')
        print('-'*50)

def eliminar_cliente(codigo):
    #PreCondicion: Recibe un cliente por su Codigo
    #PostCondicion: Elimina el cliente si existe o False si no existe
    for cliente in clientes:
        if cliente['Codigo'] == codigo:
            clientes.remove(cliente)
            return True
    return False