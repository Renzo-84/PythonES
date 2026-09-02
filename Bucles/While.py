import os


def limpiar():
    os.system("cls")

def caso11():
    limpiar()
    print("--- CASO 11: Promedio de ventas ---")
    try:
        v1 = float(input("Venta 1: "))
        v2 = float(input("Venta 2: "))
        v3 = float(input("Venta 3: "))
        promedio = (v1 + v2 + v3) / 3
    except ValueError:
        print("Error: Ingrese valores numéricos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    else:
        print("Promedio de ventas:", promedio)
    input("\nPresione Enter para continuar al siguiente caso...")

def caso12():
    limpiar()
    print("--- CASO 12: Descuento proporcional ---")
    try:
        monto = float(input("Monto: "))
        base = float(input("Base: "))
        descuento = (monto / base) * 100
    except ValueError:
        print("Error: Ingrese datos numéricos válidos.")
    except ZeroDivisionError:
        print("Error: La base no puede ser cero.")
    else:
        print("Porcentaje calculated:", descuento, "%")
    input("\nPresione Enter para continuar al siguiente caso...")

def caso13():
    limpiar()
    print("--- CASO 13: Conversión de moneda ---")
    try:
        monto_moneda = float(input("Monto: "))
        tasa = float(input("Tasa de cambio: "))
        equivalente = monto_moneda * tasa
    except ValueError:
        print("Error: Debe ingresar valores numéricos para el monto y la tasa.")
    else:
        print("Equivalente:", equivalente)
    input("\nPresione Enter para continuar al siguiente caso...")

def caso14():
    limpiar()
    print("--- CASO 14: Tipos incompatibles ---")
    try:
        resultado_tipo = "El total es: " + 50
    except TypeError:
        print("Error capturado: No se puede concatenar un str y un int directamente.")
    input("\nPresione Enter para continuar al siguiente caso...")

def caso15():
    limpiar()
    print("--- CASO 15: Cálculo de comisión ---")
    try:
        ventas = float(input("Ventas totales: "))
        porcentaje_comision = float(input("Porcentaje de comisión: "))
        comision = ventas * (porcentaje_comision / 100)
    except ValueError:
        print("Error: Ingrese únicamente números.")
    else:
        print("Comisión total:", comision)
    input("\nPresione Enter para continuar al siguiente caso...")

def caso16():
    limpiar()
    print("--- CASO 16: Índice de inventario ---")
    inventario = ["Laptop", "Mouse", "Teclado", "Monitor"]
    try:
        idx = int(input("Posición en inventario: "))
        print("Producto:", inventario[idx])
    except ValueError:
        print("Error: Debe ingresar un número entero.")
    except IndexError:
        print("Error: La posición solicitada no existe en el inventario.")
    input("\nPresione Enter para continuar al siguiente caso...")

def caso17():
    limpiar()
    print("--- CASO 17: Diccionario de empleados ---")
    empleados = {"101": "Carlos", "102": "Lucía"}
    id_emp = input("ID de empleado a consultar: ")
    resultado_emp = empleados.get(id_emp)
    if resultado_emp:
        print("Empleado encontrado:", resultado_emp)
    else:
        print("Ese ID de empleado no está registrado.")
    input("\nPresione Enter para continuar al siguiente caso...")

def caso18():
    limpiar()
    print("--- CASO 18: Menú de opciones ---")
    try:
        opcion = int(input("Ingrese opción numérica: "))
    except ValueError:
        print("Error: La opción debe ser un número.")
    else:
        print("Opción exitosa procesada:", opcion)
    input("\nPresione Enter para continuar al siguiente caso...")

def caso19():
    limpiar()
    print("--- CASO 19: Archivo de reportes ---")
    try:
        archivo = open("reportes.txt", "r")
        print(archivo.read())
        archivo.close()
    except FileNotFoundError:
        print("Error: El archivo 'reportes.txt' no existe.")
    finally:
        print("Operación de archivo terminada.")
    input("\nPresione Enter para continuar al siguiente caso...")

def caso20():
    limpiar()
    print("--- CASO 20: Importación controlada ---")
    try:
        import modulo_ES
    except ModuleNotFoundError:
        print("Error: Módulo no encontrado. La persona desarrolladora debe revisar si escribió mal el nombre o si falta instalarlo.")
    input("\nPresione Enter para finalizar...")

if __name__ == "__main__":
    caso11()
    caso12()
    caso13()
    caso14()
    caso15()
    caso16()
    caso17()
    caso18()
    caso19()
    caso20()