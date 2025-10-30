# Este es el archivo principal
# Codificado en Python
# Coders:  Fer and Moy
# Date October 14th

from fer import Operador
from moy import Operators

def main():
    operador = Operador()
    operadores = Operators()
    
    print("Hola, esta es la calculadora empleando POO y arquitectura modular")

    try:
        num1 = float(input("Indique su primer número: "))
        num2 = float(input("Indique su segundo número: "))
        operation = input("Indique la operación a realizar: [ +, -, *, / ,**, sqrt, x**1, x**2]: ")

        if operation == '+': 
            resultado = operadores.suma(num1, num2)
        elif operation == '-': 
            resultado = operador.resta(num1, num2)
        elif operation == '*': 
            resultado = operadores.multiplicacion(num1, num2)
        elif operation == '/': 
            resultado = operador.division(num1, num2)
        elif operation =='**':
            resultado = operador.potencia(num1, num2)
        elif operation == 'sqrt':
            resultado = operadores.raiz_cuadrada(num1)
        elif operation == 'x**1':
            num3 = float(input("Indique el valor de num3: "))
            resultado = operadores.ecuacion_lineal(num1, num2, num3) ### num1*x + num2 = num3
        elif operation == 'x**2':
            num3 = float(input("Indique el valor de num3: "))
            resultado = operadores.ecuacion_cuadratica(num1, num2, num3) ### num1*x^2 + num2*x + num3 = 0
        else:
            resultado = "Operación no codificada aún!"

        print(f"El resultado es: {resultado}")


    except ValueError:
        print("Error: Introduce un valor válido")    

if __name__ == "__main__":
    main()


