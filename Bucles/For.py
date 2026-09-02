import os


def limpiar():
    os.system("cls")

def caso01():
    limpiar()
    print("--- CASO 01: Conversión de edad ---")
    try:
        edad = int(input("Edad: "))
    except ValueError:
        print("Debe ingresar un número entero")
    else:
        print("Edad registrada:", edad)
    input("\nPresione Enter para continuar al siguiente caso...")

def caso02():
    limpiar()
    print("--- CASO 02: División segura ---")
    try:
        a = float(input("Dividendo: "))
        b = float(input("Divisor: "))
        resultado = a / b
    except ValueError:
        print("Ingrese valores numéricos.")
    except ZeroDivisionError:
        print("El divisor no puede ser cero")
    else:
        print("Resultado:", resultado)
    input("\nPresione Enter para continuar al siguiente caso...")

def caso03():
    limpiar()
    print("--- CASO 03: Acceso a una lista ---")
    nombres = ["Ana", "Luis", "Marta"]
    try:
        posicion = int(input("Posición: "))
        print(nombres[posicion])
    except ValueError:
        print("La posición debe ser un entero")
    except IndexError:
        print("La posición no existe.")
    input("\nPresione Enter para continuar al siguiente caso...")

def caso04():
    limpiar()
    print("--- CASO 04: Consulta de cliente ---")
    cliente = {
        "nombre": "María",
        "telefono": "8888-8888"
    }
    try:
        clave = input("Dato a consultar: ")
        print(cliente[clave])
    except KeyError:
        print("Ese dato no está registrado.")
    input("\nPresione Enter para continuar al siguiente caso...")

def caso05():
    limpiar()
    print("--- CASO 05: Cierre garantizado ---")
    try:
        numero = int(input("Número: "))
        print(100 / numero)
    except ValueError:
        print("Debe ingresar un entero.")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    finally:
        print("Proceso finalizado.")
    input("\nPresione Enter para continuar al siguiente caso...")

def caso06():
    limpiar()
    print("--- CASO 06: Precio de un producto ---")
    try:
        precio = float(input("Precio del producto: "))
        print("Precio registrado:", precio)
    except ValueError:
        print("Error: Debe ingresar un valor numérico válido.")
    input("\nPresione Enter para continuar al siguiente caso...")

def caso07():
    limpiar()
    print("--- CASO 07: Cantidad de productos ---")
    try:
        cantidad = int(input("Cantidad de unidades: "))
        print("Cantidad registrada:", cantidad)
    except ValueError:
        print("Error: La cantidad debe ser un número entero.")
    input("\nPresione Enter para continuar al siguiente caso...")

def caso08():
    limpiar()
    print("--- CASO 08: Calificación ---")
    try:
        calificacion = float(input("Ingrese calificación: "))
    except ValueError:
        print("Error: Debe ingresar un número válido.")
    else:
        if 0 <= calificacion <= 100:
            print("Calificación válida:", calificacion)
        else:
            print("Error: La calificación debe estar entre 0 y 100.")
    input("\nPresione Enter para continuar al siguiente caso...")

def caso09():
    limpiar()
    print("--- CASO 09: Edad para registro ---")
    try:
        edad_reg = int(input("Ingrese edad: "))
    except ValueError:
        print("Error: No es un número entero.")
    else:
        if 0 < edad_reg < 120:
            print("Edad válida:", edad_reg)
        else:
            print("Error: La edad está fuera del rango permitido.")
    input("\nPresione Enter para continuar al siguiente caso...")

def caso10():
    limpiar()
    print("--- CASO 10: Tres entradas consecutivas ---")
    try:
        nombre = input("Nombre: ")
    except Exception as e:
        print("Error en nombre:", e)

    try:
        edad_t = int(input("Edad: "))
    except ValueError:
        print("Error en edad: Debe ingresar un número entero.")

    try:
        salario = float(input("Salario: "))
    except ValueError:
        print("Error en salario: Debe ingresar un valor numérico.")
    input("\nPresione Enter para finalizar...")

if __name__ == "__main__":
    caso01()
    caso02()
    caso03()
    caso04()
    caso05()
    caso06()
    caso07()
    caso08()
    caso09()
    caso10()