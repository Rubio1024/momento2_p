

class Vehiculo:

    def __init__(self, marca, modelo, color, ruedas, ref):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ruedas = ruedas
        self.ref = ref

    def ver_vehiculo(self):
        print(f"Marca: {self.marca} \n  Modelo: {self.modelo} \n Color: {self.color}")



moto = Vehiculo("yamaha", 2023, "negra", 2, "n-max150")

carro = Vehiculo("Mazda", 2024, "blanco", 4, "CX-5")

print(carro.marca)
print(moto.marca)

carro.ver_vehiculo()
moto.ver_vehiculo()
