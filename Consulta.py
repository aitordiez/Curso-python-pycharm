from Doctores import *
class Consulta(Doctores):
    def __init__(self,nombre,apellidos,dni,especialidad,doctores =[]):
        Doctores.__init__(self,nombre,apellidos,dni,especialidad)
        self.doctores = doctores
