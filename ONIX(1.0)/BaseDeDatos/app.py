import os
import sys
from flask import Flask, render_template, url_for, redirect, request, jsonify
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from Backend.ValidarLogin import ValidarLogin
from conectar import conexion
import bcrypt

app = Flask(__name__, template_folder='FrontEnd/templates', static_folder='FrontEnd/static')

Onix = conexion()

# Obtén la ruta de la carpeta de plantillas
template_dir = os.path.join(os.path.dirname(__file__), '..', 'FrontEnd', 'templates')
static_dir = os.path.join(os.path.dirname(__file__), '..', 'FrontEnd', 'static')

# Configura la carpeta de plantillas en la aplicación Flask
app.template_folder = template_dir
app.static_folder = static_dir

@app.route('/')
def prueba():
    return render_template('Prueba.html')

@app.route('/log')
def log():
    return render_template('login.html')

@app.route('/inicio')
def inicio():
    return render_template('Inicio.html')

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('email')
        password = request.form.get('password')
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        usuario = {
            "nombre": nombre,
            "correo": correo,
            "password": hashed_password
        }

        Onix.Usuarios.insert_one(usuario)

        return redirect(url_for('log'))

    return render_template('Registro.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':

        datos_login = request.form
        correo = datos_login.get('email')
        clave = datos_login.get('password')

        validador = ValidarLogin(correo, clave)


        if validador.validar():
            print("Login exitoso, redirigiendo al inicio...")
            return redirect(url_for('inicio'))
        else:

            print("Login fallido, redirigiendo al login con error")
            return render_template('login.html', error="Credenciales inválidas")

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
