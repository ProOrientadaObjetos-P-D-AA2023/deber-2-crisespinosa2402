"""
"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Ciudad: {self.ciudad}"
# clase 02
class Animal:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Raza: {self.raza}"



