from BaseDeDatos.conectar import conexion
import bcrypt

class ValidarLogin():
    def __init__(self, correo, clave):
        self.correo = correo
        self.clave = clave

    def validar(self):
        db = conexion()
        print("Conexión establecida con la base de datos")

        usuario = db.Usuarios.find_one({"correo": self.correo})
        if usuario:
            print("Usuario encontrado en la base de datos:", usuario)
            clave_bd = usuario.get("password")
            print("Contraseña almacenada en la base de datos:", clave_bd)

            if bcrypt.checkpw(self.clave.encode('utf-8'), clave_bd):
                print("Las contraseñas coinciden. Inicio de sesión exitoso.")
                return True
            else:
                print("Las contraseñas no coinciden. Inicio de sesión fallido.")
                return False
        else:
            print("Usuario no encontrado en la base de datos.")
            return False