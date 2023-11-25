from Usuario import Usuario

class Cajero:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_usuario(self, id, nombre):
        for usuario in self.usuarios:
            if usuario.id == id and usuario.nombre == nombre:
                return usuario
        return None

    def retirar_dinero(self, id, nombre, cantidad):
        usuario = self.buscar_usuario(id, nombre)
        if usuario is None:
            print("Usuario no encontrado")
        elif cantidad > usuario.saldo:
            print("Saldo insuficiente")
        else:
            usuario.saldo -= cantidad
            print(f"Retiro exitoso. Saldo actual: {usuario.saldo}")

    def depositar_dinero(self, id, nombre, cantidad):
        usuario = self.buscar_usuario(id, nombre)
        if usuario is None:
            print("Usuario no encontrado")
        else:
            usuario.saldo += cantidad
            print(f"Depósito exitoso. Saldo actual: {usuario.saldo}")

    def iniciar_sesion(self, id, nombre):
        usuario = self.buscar_usuario(id, nombre)
        if usuario is None:
            print("Usuario no encontrado")
        else:
            print(f"Bienvenido {usuario.nombre}. Tu saldo es: {usuario.saldo}")

    def registrar(self, id, nombre, apellido, correo, password):
        nuevo_usuario = Usuario(id, nombre, apellido, correo, password)
        self.agregar_usuario(nuevo_usuario)
        print(f"Usuario {nombre} registrado con éxito")

def menu():
    cajero = Cajero()

    while True:
        print("\n1.Iniciar Sesion\n2.Registrarse\n3.Retiros\n4.Depositos\n5.Salir")
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            id = int(input("Ingresa tu ID: "))
            nombre = input("Ingresa tu nombre: ")
            cajero.iniciar_sesion(id, nombre)
        elif opcion == 2:
            id = int(input("Ingresa tu ID: "))
            nombre = input("Ingresa tu nombre: ")
            apellido = input("Ingresa tu apellido: ")
            correo = input("Ingresa tu correo: ")
            password = input("Ingresa tu contraseña: ")
            cajero.registrar(id, nombre, apellido, correo, password)
        elif opcion == 3:
            id = int(input("Ingresa tu ID: "))
            nombre = input("Ingresa tu nombre: ")
            cantidad = float(input("Ingresa la cantidad a retirar: "))
            cajero.retirar_dinero(id, nombre, cantidad)
        elif opcion == 4:
            id = int(input("Ingresa tu ID: "))
            nombre = input("Ingresa tu nombre: ")
            cantidad = float(input("Ingresa la cantidad a depositar: "))
            cajero.depositar_dinero(id, nombre, cantidad)
        elif opcion == 5:
            break


menu()