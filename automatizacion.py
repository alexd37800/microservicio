
'''
Alumno: Alejandro Tadeo Martínez
Grupo: GRIC3091
'''
# Importar las librerías necesarias
from flask import Flask, jsonify, request, session, redirect, url_for
import pymysql

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Configuración de la aplicación Flask
app.secret_key = 'Alex1275$'  # Clave secreta utilizada para cifrar datos de sesión
app.config['MYSQL_DATABASE_HOST'] = 'localhost'  # Dirección del servidor de base de datos
app.config['MYSQL_DATABASE_USER'] = 'root'  # Usuario de la base de datos
app.config['MYSQL_DATABASE_PASSWORD'] = 'linux'  # Contraseña del usuario de la base de datos
app.config['MYSQL_DATABASE_DB'] = 'automatizacion'  # Nombre de la base de datos

# Conexión a la base de datos MySQL utilizando las configuraciones previamente definidas
mysql = pymysql.connect(
    host=app.config['MYSQL_DATABASE_HOST'],
    user=app.config['MYSQL_DATABASE_USER'],
    password=app.config['MYSQL_DATABASE_PASSWORD'],
    db=app.config['MYSQL_DATABASE_DB']
)

# Definir una ruta para el inicio de sesión de usuario
@app.route('/login', methods=['POST'])
def login():
    """
    Realiza el inicio de sesión de un usuario.
    """
    datos = request.get_json()  # Obtener los datos enviados en la solicitud
    correo_usuario = datos.get('correo_usuario')  # Obtener el correo del usuario
    contrasena = datos.get('contrasena')  # Obtener la contraseña del usuario

    cursor = mysql.cursor(pymysql.cursors.DictCursor)  # Crear un cursor para interactuar con la base de datos
    cursor.execute('SELECT * FROM estudiantes WHERE correo = %s', (correo_usuario,))
    estudiante = cursor.fetchone()  # Obtener los datos del estudiante con el correo proporcionado

    if estudiante:
        stored_password = estudiante['contrasena']  # Obtener la contraseña almacenada en la base de datos

        if stored_password == contrasena:
            session['logged_in'] = True  # Establecer la sesión como iniciada
            return {'message': 'Inicio de sesión exitoso'}  # Devolver un mensaje de éxito
        else:
            return {'error': 'Credenciales inválidas'}, 401  # Devolver un error de credenciales inválidas
    else:
        return {'error': 'Usuario no encontrado'}, 404  # Devolver un error de usuario no encontrado

# Ruta para ver la tabla de estudiantes en formato JSON
@app.route('/ver_tabla', methods=['GET'])
def ver_tabla():
    """
    Mostrar la tabla de estudiantes en formato JSON.
    """
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))  # Redirigir al inicio de sesión si no se ha iniciado sesión

    cursor = mysql.cursor(pymysql.cursors.DictCursor)  # Crear un cursor para interactuar con la base de datos
    cursor.execute('SELECT * FROM estudiantes')
    estudiantes = cursor.fetchall()  # Obtener todos los registros de estudiantes

    return jsonify(estudiantes)  # Devolver los registros de estudiantes en formato JSON


@app.route('/agregar_usuario', methods=['POST'])
def agregar_usuario():
    """
    Agregar un nuevo usuario a la base de datos.
    """
    try:
        datos = request.get_json()  # Obtener los datos enviados en la solicitud
        numero_control = datos.get('numero_control')  # Obtener el número de control del usuario
        nombre = datos.get('nombre')  # Obtener el nombre del usuario
        edad = datos.get('edad')  # Obtener la edad del usuario
        correo = datos.get('correo')  # Obtener el correo del usuario
        carrera = datos.get('carrera')  # Obtener la carrera del usuario
        semestre = datos.get('semestre')  # Obtener el semestre del usuario
        telefono = datos.get('telefono')  # Obtener el teléfono del usuario
        ciudad = datos.get('ciudad')  # Obtener la ciudad del usuario
        genero = datos.get('genero')  # Obtener el género del usuario
        promedio = datos.get('promedio')  # Obtener el promedio del usuario
        contrasena = datos.get('contrasena')  # Obtener la contraseña del usuario

        cursor = mysql.cursor()  # Crear un cursor para interactuar con la base de datos
        cursor.execute('INSERT INTO estudiantes (numero_control, nombre, edad, correo, carrera, semestre, telefono, ciudad, genero, promedio, contrasena) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (numero_control, nombre, edad, correo, carrera, semestre, telefono, ciudad, genero, promedio, contrasena))
        mysql.commit()  # Confirmar los cambios en la base de datos

        return {'message': 'Usuario agregado exitosamente'}, 201  # Devolver un mensaje de éxito
    except Exception as e:
        return {'error': 'Error al agregar usuario', 'details': str(e)}, 400  # Devolver un mensaje de error con detalles

@app.route('/actualizar_usuario', methods=['PUT'])
def actualizar_usuario():
    """
    Actualizar los datos de un usuario en la base de datos.
    """
    try:
        datos = request.get_json()  # Obtener los datos enviados en la solicitud
        numero_control = datos.get('numero_control')  # Obtener el número de control del usuario
        nombre = datos.get('nombre')  # Obtener el nuevo nombre del usuario
        edad = datos.get('edad')  # Obtener la nueva edad del usuario
        correo = datos.get('correo')  # Obtener el nuevo correo del usuario
        carrera = datos.get('carrera')  # Obtener la nueva carrera del usuario
        semestre = datos.get('semestre')  # Obtener el nuevo semestre del usuario
        telefono = datos.get('telefono')  # Obtener el nuevo teléfono del usuario
        ciudad = datos.get('ciudad')  # Obtener la nueva ciudad del usuario
        genero = datos.get('genero')  # Obtener el nuevo género del usuario
        promedio = datos.get('promedio')  # Obtener el nuevo promedio del usuario
        contrasena = datos.get('contrasena')  # Obtener la nueva contraseña del usuario

        cursor = mysql.cursor()  # Crear un cursor para interactuar con la base de datos
        cursor.execute('UPDATE estudiantes SET nombre = %s, edad = %s, correo = %s, carrera = %s, semestre = %s, telefono = %s, ciudad = %s, genero = %s, promedio = %s, contrasena = %s WHERE numero_control = %s',
                       (nombre, edad, correo, carrera, semestre, telefono, ciudad, genero, promedio, contrasena, numero_control))
        mysql.commit()  # Confirmar los cambios en la base de datos

        if cursor.rowcount > 0:
            return {'message': 'Usuario actualizado exitosamente'}, 200  # Devolver un mensaje de éxito
        else:
            return {'error': 'Usuario no encontrado'}, 404  # Devolver un mensaje de error si el usuario no se encontró
    except Exception as e:
        return {'error': 'Error al actualizar usuario', 'details': str(e)}, 400  # Devolver un mensaje de error con detalles

@app.route('/eliminar_usuario', methods=['DELETE'])
def eliminar_usuario():
    """
    Eliminar un usuario de la base de datos.
    """
    try:
        datos = request.get_json()  # Obtener los datos enviados en la solicitud
        numero_control = datos.get('numero_control')  # Obtener el número de control del usuario

        cursor = mysql.cursor()  # Crear un cursor para interactuar con la base de datos
        cursor.execute('DELETE FROM estudiantes WHERE numero_control = %s', (numero_control,))
        mysql.commit()  # Confirmar los cambios en la base de datos

        if cursor.rowcount > 0:
            return {'message': 'Usuario eliminado exitosamente'}, 200  # Devolver un mensaje de éxito
        else:
            return {'error': 'Usuario no encontrado'}, 404  # Devolver un mensaje de error si el usuario no se encontró
    except Exception as e:
        return {'error': 'Error al eliminar usuario', 'details': str(e)}, 400  # Devolver un mensaje de error con detalles

