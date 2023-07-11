from flask import Flask, request
from ConexionDB import registrar_usuario

app = Flask(__name__)

@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    
    nombre = data.get('nombre')
    correo = data.get('correo')
    contraseña = data.get('contraseña')
    
    resultado = registrar_usuario(nombre, correo, contraseña)
    
    return resultado

if __name__ == '__main__':
    app.run()