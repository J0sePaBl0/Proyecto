import uuid
from flask import Flask, render_template, request, jsonify
from backend.ConexionDB import registrar_usuario, obtener_bots, crear_bot
app = Flask(__name__)

# Ruta de inicio
@app.route("/")
def index():
    return render_template('index.html')

# Ruta para el registro de usuarios
@app.route("/registro", methods=['POST'])
def registro():
    
    datos = request.json
    nombre = datos['nombre']
    correo = datos['correo']
    contraseña = datos['contraseña']

    # Generar un ID manualmente utilizando uuid
    usuario_id = str(uuid.uuid4())

    # Llamar a la función para registrar el usuario en la base de datos
    resultado = registrar_usuario(usuario_id, nombre, correo, contraseña)

    return jsonify({'message': resultado})

@app.route("/obtener_bots")
def obtenerBots():
    bots = obtener_bots()  # Obtener los datos de los bots desde ConexionDB.py

    for bot in bots:
        bot['imagen_url'] = '/static/img/BotsAll.png'


    return jsonify(bots)


@app.route("/form")
def formulario():
   return render_template('login.html')


@app.route("/tienda")
def tienda():
   
   return render_template('tienda.html')

@app.route("/crear_bots")
def crear_bots_route():
    crear_bot()
    return "Bots dummy creados exitosamente"

if __name__ == '__main__':
    app.run()

