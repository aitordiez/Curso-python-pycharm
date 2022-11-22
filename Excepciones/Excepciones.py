class TemperatureException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


class TooHotTemperatureException(TemperatureException):
    def __init__(self, mensaje):
        TemperatureException.__init__(self, mensaje = mensaje)


class TooColdTemperatureException(TemperatureException):
    def __init__(self, mensaje):
        TemperatureException.__init__(self, mensaje = mensaje)