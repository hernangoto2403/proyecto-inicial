"""
Esto es una calculadora  
calcula difretes tipos de ejercisios con entradas desde la consola
"""

#definiendo funciones
def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b

#creando intefaz
print("Bienvenido a la calculadora de cuatro operaciones \n \n")
print("Seleccione el ejercisio que desea realizar \n")
print("1. para sumar \n")
print("2. para restar \n")
print("3. para multiplicar \n")
print("4. para dividir \n")
print("5. para salir \n")

Opcion_Select = int(input("Ingrese una opcion: \n"))

if Opcion_Select == 5:
    print("Gracias por usar esta calculadora")
elif Opcion_Select == 1:
    suma = sumar(float(input("numero 1: ")), float(input("numero 2: ")))
    print("el resultado de la suma es:", suma)
elif Opcion_Select == 2:
    resta = restar(float(input("numero 1: ")), float(input("numero 2: ")))
    print("el resultado de la resta es:", resta)
elif Opcion_Select == 3:
    multiplicacion = multiplicar(float(input("numero 1: ")), float(input("numero 2: ")))
    print("el resultado de la multiplicacion es:", multiplicacion)
elif Opcion_Select == 4:
    divicion = dividir(float(input("numero 1: ")), float(input("numero 2: ")))
    print("el resultado de la divicion es: ", divicion)
else:
    print("Opcion no reconocida")