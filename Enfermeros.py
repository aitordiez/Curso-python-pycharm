from Persona import *
from modulos2.modulo_date import *
class Enfermero(Persona):
    def __init__(self,nombre, apellidos, dni,planta):
        Persona.__init__(self,nombre,apellidos,dni)
        self.planta = planta

    def __str__(self):
        return "El nombre del enfermero es {}, los apellidos son {}, el dni {}, los sintomas son {}".format(self.nombre,self.apellidos,self.dni,self.planta)

    def fichar(self):
        dt = datetime.datetime.now()
        print("El enfermero ",self.nombre," ha fichado en esta fecha",dt.day,"/",dt.month,"/",dt.year)
