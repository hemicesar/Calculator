#Cambios y aportaciones de Moi
import math

class Operators:
    def __init__(self): 
        pass
        
    def suma (self , x, y):
        return x + y
    
    def multiplicacion (self , x, y):
        return x * y
    def raiz_cuadrada(self, x):
        return x ** 0.5
    def ecuacion_lineal(self, num1, num2, num3):
        if num1 == 0:
            raise ValueError("num1 tiene que ser diferente de 0")
        x =  (num3 - num2) / num1
        return x   ### ax + b = c; x = -b/a
    def ecuacion_cuadratica(self, num1, num2, num3):
        if num1 == 0:
            raise ValueError("num1 tiene que ser diferente de 0") 
        
        x1 = (-num2 + math.sqrt(num2**2 - 4*num1*num3)) / (2*num1)
        
        x2 = (-num2 - ((num2**2 - 4*num1*num3)**0.5)) / (2*num1)
        return x1, x2
    


