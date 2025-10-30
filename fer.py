#Cambios y aportaciones de Fer
#caluladora
#Cambios y aportaciones de Fer
import math

class Operador:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def division(self, a, b):
        if b == 0:
            return "Error: división entre cero"
        return a / b

    def potencia(self, a, b):
        return a ** b

