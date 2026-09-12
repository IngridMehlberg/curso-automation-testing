"""
Refactorizar el script de la calculadora lineal en al menos 4 funciones separadas. una por cada tipo de operación. 
Como ser: Sumar(), Restar(), Multiplicar() y Dividir()

Añadir manejo de excepciones para entradas inválidas y división por cero.
"""

def sumar(valor1, valor2):
    return valor1 + valor2

def restar(valor1, valor2):
    return valor1 - valor2

def multiplicar(valor1, valor2):
    return valor1 * valor2

def dividir(valor1, valor2):
    if valor2 == 0:
        # Lo que hace raise es lanzar una excepción y cortar la ejecución de la función.
        raise ZeroDivisionError("No se puede dividir por cero")
    return valor1 / valor2

def calculadora():
    """Ejecuta la calculadora interactiva y maneja las entradas del usuario."""
    try:    
        num1 = float(input("Primer numero: "))
        num2 = float(input("Segundo numero: "))
        opcion = input("Indique 1) Sumar  2) Restar  3) Multiplicar  4) Dividir ")
        if opcion == "1":
            resultado = sumar(num1,num2)
        elif opcion == "2": 
            resultado = restar(num1,num2)
        elif opcion == "3": 
            resultado = multiplicar(num1,num2)
        elif opcion == "4": 
            resultado = dividir(num1,num2)
        else:
            print("Opcion invalida")
        return print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: debe ingresar números válidos")
    except ZeroDivisionError as error:
        print(f"Error: {error}")
    # Aunque no voy a tener acceso a objeto de la excepcion, podria tambien haber puesto esto directamente:
    # except ZeroDivisionError:
        # print("No se puede dividir por cero")
    finally:
        print("Operacion finalizada")

### if __name__ == '__main__': --> para que el programa se ejecute solo si lo ejecutamos directamente (buena práctica en Python).
if __name__ == '__main__':
 calculadora()