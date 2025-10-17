# Este es el archivo principal
# Codificado en Python
# Coders:  Fer and Moy
# Date October 14th

<<<<<<< HEAD
from fer import Operator
from moy import Operators

def main():
    operador = Operator()
    operadores = Operators()
    
    print("Hola, esta es la calculadora empleando POO y arquitectura modular")

    try:
        num1 = float(input("Indique su primer número: "))
        num2 = float(input("Indique su segundo número: "))
        operation = input("Indique la operación a realizar: [ +, -, *, / ]")

        if operation == '+': 
            resultado = operadores.suma(num1, num2)
        elif operation == '-': 
            resultado = operador.resta(num1, num2)
        elif operation == '*': 
            resultado = operadores.multiplicacion(num1, num2)
        elif operation == '/': 
            resultado = operador.divicion(num1, num2)
        else:
            resultado = "Operación no codificada aún!"

        print(f"El resultado es: {resultado}")


    except ValueError:
        print("Error: Introduce un valor válido")    

if __name__ == "__main__":
    main()
=======
import fer
import suma from moy
import multiplicacion from moy

print("Hola, esta es la calculadora POO")
>>>>>>> 0e5a87d26cf4861f97750903d914ec5788fa1f7c
