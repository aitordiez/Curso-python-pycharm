class Persona():
    def __init__(self,nombre,apellidos,dni):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni

    def __str__(self):
        return "El nombre del doctor es {}, su apellido es{}, dni{} y su especialidad{}".format(self.nombre,self.apellidos,self.dni)