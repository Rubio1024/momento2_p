class Persona:
    def __init__(self, id, nombre, apellido, correo, password):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._password = password

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

        ##para nombre:

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    ##para apellido

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    ##para correo

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    ##para password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password



