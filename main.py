# This is a sample Python script.

# Press Alt+Mayús+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import copy
class Persona():
    def __init__(self,nombre,apellidos,dni):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni

    def __str__(self):
        return "El nombre del doctor es {}, su apellido es{}, dni{} y su especialidad{}".format(self.nombre,self.apellidos,self.dni)
class Doctores(Persona):
    def __init__(self,nombre,apellidos,dni,especialidad):
        Persona.__init__(self,nombre,apellidos,dni)
        self.especialidad = especialidad

    def _str_(self):
        return "El nombre del doctor es {}, su apellido es{}, dni{} y su especialidad{}".format(self.nombre,self.apellidos,self.dni,self.especialidad)

    def fichar(self):
        print("El doctor ha sido fichado")

class Enfermo(Persona):
    def __init__(self,nombre,apellidos,dni,enfermedades  = {}):
        Persona.__init__(self,nombre,apellidos,dni)
        self.enfermedades = enfermedades

    def __str__(self):
        return "El nombre es {}, el apellido es {}, el dni {} y la enfermedad {}".format(self.nombre,self.apellidos,self.dni,self.enfermedades)



class Paciente(Persona):
    def __init__(self,nombre,apellidos,dni,sintomas = {}):
        Persona.__init__(self,nombre,apellidos,dni)
        self.sintomas = sintomas

    def __str__(self):
        return "El nombre del paciente es {}, los apellidos son {}, el dni es {} y los sintomas son {}".format(self.nombre,self.apellidos,self.dni,self.sintomas)


class Enfermero(Persona):
    def __init__(self,nombre, apellidos, dni,planta):
        Persona.__init__(self,nombre,apellidos,dni)
        self.planta = planta

    def __str__(self):
        return "El nombre del enfermero es {}, los apellidos son {}, el dni {}, los sintomas son {}".format(self.nombre,self.apellidos,self.dni,self.planta)

    def fichar(self):
        print("El enfermero ha sido fichado")


class Consulta(Doctores):
    def __init__(self,nombre,apellidos,dni,especialidad,doctores =[]):
        Doctores.__init__(self,nombre,apellidos,dni,especialidad)
        self.doctores = doctores

class Hospital():
    def __init__(self,enfermeros = [], pacientes = [], sala_espera = [], doctor = [],consultas = [], habitacion =[],enfermos = []):
        self.enfermeros = enfermeros
        self.pacientes = pacientes
        self.sala_espera = sala_espera
        self.doctor = doctor
        self.consultas = consultas
        self.habitacion = habitacion
        self.enfermos = enfermos

    def add_enfermero(self,pacientees):
        self.enfermeros.append(pacientees)
    def add_sala_espera(self,paciente):
        if len(self.sala_espera) > 4:
            print("No se puede añadir mas pacientes")
        else:
            self.sala_espera.append(paciente)

    def hay_sala_espera(self):
        return len(self.sala_espera) > 0

    def hay_habitaciones(self):
        return len(self.habitacion) > 0

    def addHabitaciones(self,enfermos_total):
        if self.hay_habitaciones():
            self.habitacion.append(enfermos_total)
        else:
            print("Todas las habitaciones estan ocupadas")

    def addConsulta(self,doctores):
        self.consultas.append(doctores)

    def hay_enfermos(self):
        return len(self.enfermos) > 0

    def enfermedades(self):
        try:
            habitacion_libres = self.hay_habitaciones()
            while habitacion_libres:
                for habitaciones in self.habitacion:
                    enfermos_habitacion = self.enfermos.pop(0)
                    self.habitacion.append(enfermos_habitacion)
                    print("El enfermo ",enfermos_habitacion," ha ocupado la ",habitaciones)
                habitacion_libres = self.hay_habitaciones()
            else:
                print("Todas las habitaciones estan completas")
        except IndexError:
            print("Lista vacia")


    def hay_consultas(self):
        return len(self.consultas) > 0

    def hay_doctor(self):
        return len(self.doctor) > 0

    def consultas_doctor_enfermero(self):
        hay_paciente = self.hay_sala_espera()
        while hay_paciente:
            for pacientess in self.sala_espera:
                self.enfermeros.append(pacientess)
                self.sala_espera.pop(0)
                print("El paciente: ", pacientess, " ha sido atendido por el enfermero ")
                self.enfermeros.pop(0)
                self.consultas.append(pacientess)
                print("El doctor esta consultando al paciente: ", pacientess)
                hay_paciente = self.hay_sala_espera()
        else:
            print("todas las consultas estan ocupadas por los doctores")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    persona1 = Persona("Aitor", "Diez", "45201963")
    persona2 = Persona("Paco", "Fernandez", "5690147")
    persona3 = Persona("Francisco", "Perez", "10302986")
    persona4 = Persona("Felipe", "Fernandez", "5309741")
    doctor1 = Doctores("Christian", "Blanco", "75230149", "Otorrinolaringologo")
    doctor2 = Doctores("Pedro", "Garcia", "4530298", "Oftamologo")
    paciente1 = Paciente(persona1.nombre, persona1.apellidos, persona1.dni, {8: "Covid"})
    paciente2 = Paciente(persona2.nombre, persona2.apellidos, persona2.dni, {4: "Catarro"})
    paciente3 = Paciente(persona3.nombre, persona3.apellidos, persona3.dni, {8: "Lepra"})
    paciente4 = Paciente(persona4.nombre, persona4.apellidos, persona4.dni, {4: "Infeccion de oidos"})
    enfermero = Enfermero(persona2.nombre, persona2.apellidos, persona2.dni, "Quirofano")
    enfermero1 = Enfermero(persona1.nombre, persona1.apellidos, persona1.dni, "Rayos")
    enfermo1 = Enfermo(persona1.nombre, persona1.apellidos, persona1.dni, {random.randint(7, 10), "covid"})
    enfermo2 = Enfermo(persona2.nombre, persona2.apellidos, persona2.dni, {random.randint(7, 10): "Malaria"})
    enfermo3 = Enfermo(persona3.nombre, persona3.apellidos, persona3.dni, {random.randint(0, 5): "catarro"})
    enfermo4 = Enfermo(persona4.nombre, persona4.apellidos, persona4.dni, {random.randint(0, 5): "Gastroenteritis"})
    hospital = Hospital([enfermero.nombre,enfermero1.nombre],[paciente1.nombre,paciente2.nombre,paciente3.nombre,paciente4.nombre],[paciente1.nombre,paciente2.nombre,paciente3.nombre,paciente4.nombre],[doctor1.nombre,doctor2.nombre],["consulta 1","consulta 2","consulta 3"],["Habitacion 1","Habitacion 2","Habitacion 3"],[enfermo1.nombre,enfermo2.nombre,enfermo3.nombre,enfermo4.nombre])
    hospital.enfermedades()
    hospital.consultas_doctor_enfermero()


    enfermo1 = Enfermo(persona1.nombre, persona1.apellidos, persona1.dni, {random.randint(0, 3): "covid"})




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
