from Persona import *
class Paciente(Persona):
    def __init__(self,nombre,apellidos,dni,sintomas = {}):
        Persona.__init__(self,nombre,apellidos,dni)
        self.sintomas = sintomas

    def __str__(self):
        return "El nombre del paciente es {}, los apellidos son {}, el dni es {} y los sintomas son {}".format(self.nombre,self.apellidos,self.dni,self.sintomas)


