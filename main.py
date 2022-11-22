# This is a sample Python script.
from abc import ABC
import random
import logging_Bar as log
from Excepciones.Excepciones import TemperatureException
from Excepciones.Excepciones import TooHotTemperatureException
from Excepciones.Excepciones import TooColdTemperatureException


# Press Alt+Mayús+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class TazaCafe:
    def __init__(self, temperatura, tipo_cafe):
        self.temperatura = temperatura
        self.tipo_cafe = tipo_cafe


class Persona(ABC):
    def __init__(self,nombre):
        self.nombre = nombre


class Camarero(Persona):

    def servirTazaCafe(self):
        log.info("El camarero está poniendo el café")
        tazaCafe = TazaCafe(random.randint(0,100),"Cafe solo")
        log.debug("Taza de café {} creada a {} grados".format(tazaCafe.temperatura, tazaCafe.tipo_cafe))
        return tazaCafe

class Cliente(Persona):

    def tomar_taza_cafe(self,taza_cafe):
        log.info("El cliente {} se está tomado la taza de cafe".format(self.nombre))
        if taza_cafe.temperatura > 40:
            raise TooHotTemperatureException("El cafe esta demasiado caliente")
        elif taza_cafe.temperatura < 20:
            raise TooColdTemperatureException("El cafe esta demasiado caliente")
        else:
            log.info("El cafe se lo toma a gusto")

class Bar:
    def __init__(self,camareros, clientes):
        self.camareros = camareros
        self.clientes = clientes


    def arranca_bar(self):
        cafe_taza = self.camareros.servirTazaCafe()
        try:
            self.clientes.tomar_taza_cafe(cafe_taza)
        except TooHotTemperatureException as caliente:
            log.error(caliente.mensaje)
            log.error("El camarero le pone un vaso de agua")
        except TooColdTemperatureException as frio:
            log.error(frio.mensaje)
            log.error("El camarero le pone un vaso de agua")
        except Exception as e:
            log.error("Al cliente le pasa algo")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    camarero1 = Camarero("Camarero1")
    cliente1 = Cliente("Cliente1")
    bar1 = Bar(camarero1,cliente1)
    bar1.arranca_bar()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
