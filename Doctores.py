from Persona import *
from modulos2.modulo_date import *
class Doctores(Persona):
    def __init__(self,nombre,apellidos,dni,especialidad):
        Persona.__init__(self,nombre,apellidos,dni)
        self.especialidad = especialidad

    def _str_(self):
        return "El nombre del doctor es {}, su apellido es{}, dni{} y su especialidad{}".format(self.nombre,self.apellidos,self.dni,self.especialidad)

    def fichar(self):
        dt = datetime.datetime.now()
        print("El doctor ",self.nombre," ha fichado en esta fecha",dt.day,"/",dt.month,"/",dt.year)