# This is a sample Python script.

# Press Alt+Mayús+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
from Consulta import *
from Enfermo import *
from Enfermeros import *
from Paciente import *

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

    #Añadir consultas
    def addConsulta(self,doctores):
        self.consultas.append(doctores)

    def hay_enfermos(self):
        return len(self.enfermos) > 0
    #Funcion para meter a los enfermos en las habitaciones
    def enfermedades(self):
        for habitaciones in range(len(self.habitacion)):
            enfermos_habitacion = self.enfermos.pop(0)
            if habitaciones == 3:
                print("Todas las habitaciones estan completas")
            else:
                self.habitacion.append(enfermos_habitacion)
                print("El enfermo ", enfermos_habitacion, " ha ocupado la habitacion", habitaciones)




    def hay_consultas(self):
        return len(self.consultas) > 0

    def hay_doctor(self):
        return len(self.doctor) > 0

    def consultas_doctor_enfermero(self):
        for pacientess in self.sala_espera:
            self.enfermeros.append(pacientess)
            self.sala_espera.pop(0)
            print("El paciente: ", pacientess, " ha sido atendido por el enfermero ")
        for consultass in range(len(self.consultas)):
            if consultass == 2:
                print("todas las consultas estan ocupadas por los doctores")
            else:
                self.consultas.append(pacientess)
                print("El doctor esta consultando al paciente: ", pacientess)
                self.consultas.pop(0)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    persona1 = Persona("Aitor", "Diez", "45201963")
    persona2 = Persona("Paco", "Fernandez", "5690147")
    persona3 = Persona("Francisco", "Perez", "10302986")
    persona4 = Persona("Felipe", "Fernandez", "5309741")
    doctor1 = Doctores("Christian", "Blanco", "75230149", "Otorrinolaringologo")
    doctor1.fichar()
    doctor2 = Doctores("Pedro", "Garcia", "4530298", "Oftamologo")
    paciente1 = Paciente(persona1.nombre, persona1.apellidos, persona1.dni, {8: "Covid"})
    paciente2 = Paciente(persona2.nombre, persona2.apellidos, persona2.dni, {4: "Catarro"})
    paciente3 = Paciente(persona3.nombre, persona3.apellidos, persona3.dni, {8: "Lepra"})
    paciente4 = Paciente(persona4.nombre, persona4.apellidos, persona4.dni, {4: "Infeccion de oidos"})
    enfermero = Enfermero(persona2.nombre, persona2.apellidos, persona2.dni, "Quirofano")
    enfermero.fichar()
    enfermero1 = Enfermero(persona1.nombre, persona1.apellidos, persona1.dni, "Rayos")
    enfermo1 = Enfermo(persona1.nombre, persona1.apellidos, persona1.dni, {random.randint(7, 10), "covid"})
    enfermo2 = Enfermo(persona2.nombre, persona2.apellidos, persona2.dni, {random.randint(7, 10): "Malaria"})
    enfermo3 = Enfermo(persona3.nombre, persona3.apellidos, persona3.dni, {random.randint(0, 5): "catarro"})
    enfermo4 = Enfermo(persona4.nombre, persona4.apellidos, persona4.dni, {random.randint(0, 5): "Gastroenteritis"})
    hospital = Hospital([enfermero.nombre,enfermero1.nombre],[paciente1.nombre,paciente2.nombre,paciente3.nombre,paciente4.nombre],[paciente1.nombre,paciente2.nombre,paciente3.nombre,paciente4.nombre],[doctor1.nombre,doctor2.nombre],["consulta 1","consulta 2","consulta 3"],["Habitacion 1","Habitacion 2","Habitacion 3"],[enfermo1.nombre,enfermo2.nombre,enfermo3.nombre,enfermo4.nombre])
    hospital.enfermedades()
    hospital.consultas_doctor_enfermero()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
