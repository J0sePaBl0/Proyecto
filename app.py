import uuid
from flask import Flask, render_template, request, jsonify
from backend.ConexionDB import registrar_usuario
app = Flask(__name__)

# Ruta de inicio
@app.route("/")
def index():
    return render_template('index.html')

# Ruta para el registro de usuarios
@app.route("/registro", methods=['POST'])
def registro():
    nombre = request.form.get('nombre')
    correo = request.form.get('correo')
    contraseña = request.form.get('contraseña')

    # Generar un ID manualmente
    usuario_id = str(uuid.uuid4())

    # Llamar a la función para registrar el usuario en la base de datos
    resultado = registrar_usuario(usuario_id, nombre, correo, contraseña)

    return jsonify({'message': resultado})

@app.route("/form")
def formulario():
   return render_template('login.html')

if __name__ == '__main__':
    app.run()

