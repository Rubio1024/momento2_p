from Persona import Persona

class Usuario(Persona):


    def __init__(self, id, nombre, apellido, correo, password, saldo=0):
        super().__init__(id, nombre, apellido, correo, password)
        self.saldo = saldo
