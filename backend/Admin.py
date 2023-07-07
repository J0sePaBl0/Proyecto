from Usuario import Usuario

class Admin(Usuario):
    def __init__(self, id, nombre, email, contrasenna):
        super().__init__(id,nombre,email)
        self.contrasenna = contrasenna
    def getContrasenna(self):
        return self.contrasenna




