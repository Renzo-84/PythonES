import os

from For import caso01, caso02, caso03, caso04, caso05, caso06, caso07, caso08, caso09, caso10
from While import caso11, caso12, caso13, caso14, caso15, caso16, caso17, caso18, caso19, caso20

def limpiar_pantalla():
    os.system("cls")

def menu():
    print("=== MENÚ DE CASOS PRÁCTICOS ===")
    print("1. Conversión de edad")
    print("2. División segura")
    print("3. Acceso a una lista")
    print("4. Consulta de cliente")
    print("5. Cierre garantizado")
    print("6. Precio de un producto")
    print("7. Cantidad de productos")
    print("8. Calificación")
    print("9. Edad para registro")
    print("10. Tres entradas consecutivas")
    print("11. Promedio de ventas")
    print("12. Descuento proporcional")
    print("13. Conversión de moneda")
    print("14. Tipos incompatibles")
    print("15. Cálculo de comisión")
    print("16. Índice de inventario")
    print("17. Diccionario de empleados")
    print("18. Menú de opciones")
    print("19. Archivo de reportes")
    print("20. Importación controlada")
    print("0. Salir")

def main():
    while True:
        limpiar_pantalla()
        menu()
        opcion = input("\nSelecciona el número del caso que deseas probar (0-20): ")

        if opcion == "1":
            caso01()
            input("\nPresione Enter para continuar...")
        elif opcion == "2":
            caso02()
            input("\nPresione Enter para continuar...")
        elif opcion == "3":
            caso03()
            input("\nPresione Enter para continuar...")
        elif opcion == "4":
            caso04()
            input("\nPresione Enter para continuar...")
        elif opcion == "5":
            caso05()
            input("\nPresione Enter para continuar...")
        elif opcion == "6":
            caso06()
            input("\nPresione Enter para continuar...")
        elif opcion == "7":
            caso07()
            input("\nPresione Enter para continuar...")
        elif opcion == "8":
            caso08()
            input("\nPresione Enter para continuar...")
        elif opcion == "9":
            caso09()
            input("\nPresione Enter para continuar...")
        elif opcion == "10":
            caso10()
            input("\nPresione Enter para continuar...")
        elif opcion == "11":
            caso11()
            input("\nPresione Enter para continuar...")
        elif opcion == "12":
            caso12()
            input("\nPresione Enter para continuar...")
        elif opcion == "13":
            caso13()
            input("\nPresione Enter para continuar...")
        elif opcion == "14":
            caso14()
            input("\nPresione Enter para continuar...")
        elif opcion == "15":
            caso15()
            input("\nPresione Enter para continuar...")
        elif opcion == "16":
            caso16()
            input("\nPresione Enter para continuar...")
        elif opcion == "17":
            caso17()
            input("\nPresione Enter para continuar...")
        elif opcion == "18":
            caso18()
            input("\nPresione Enter para continuar...")
        elif opcion == "19":
            caso19()
            input("\nPresione Enter para continuar...")
        elif opcion == "20":
            caso20()
            input("\nPresione Enter para continuar...")
        elif opcion == "0":
            limpiar_pantalla()
            print("¡Saliendo del programa. Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()