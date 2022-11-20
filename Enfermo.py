from Persona import *
class Enfermo(Persona):
    def __init__(self,nombre,apellidos,dni,enfermedades  = {}):
        Persona.__init__(self,nombre,apellidos,dni)
        self.enfermedades = enfermedades

    def __str__(self):
        return "El nombre es {}, el apellido es {}, el dni {} y la enfermedad {}".format(self.nombre,self.apellidos,self.dni,self.enfermedades)



