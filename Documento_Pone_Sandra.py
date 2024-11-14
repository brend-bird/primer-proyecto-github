def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: División por cero"

def potencia(a, b):
    return a ** b

# Función principal para realizar operaciones
def calcular(a, b, operacion):
    if operacion == '+':
        return suma(a, b)
    elif operacion == '-':
        return resta(a, b)
    elif operacion == '*':
        return multiplicacion(a, b)
    elif operacion == '/':
        return division(a, b)
    elif operacion == '%':
        return modulo(a, b)
    elif operacion == '^':
        return potencia(a, b)
    else:
        return "Operación no válida"

# Interfaz de usuario
while True:
    print("\nCalculadora de operaciones básicas")
    print("Operaciones disponibles: +, -, *, /, %, ^")
    print("Para salir, escriba 'salir'")

    operacion = input("Ingrese la operación deseada: ")
    
    if operacion.lower() == 'salir':
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break

    if operacion not in ['+', '-', '*', '/', '%', '^']:
        print("Operación no válida. Por favor, intente de nuevo.")
        continue

    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Por favor, ingrese números válidos.")
        continue

    resultado = calcular(num1, num2, operacion)
    print(f"Resultado: {resultado}")