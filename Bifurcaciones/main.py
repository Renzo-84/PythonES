import os

from Anidados import caso_credito, caso_entrega, caso_cafe, caso_hospedaje, caso_ferreteria
from Simples import caso_inventario, caso_promocion, caso_meta, caso_comedor, caso_peso

def limpiar_pantalla():
    os.system("cls")

def menu():
    print("=== MENÚ DE CASOS EMPRESARIALES ===")
    print("1. Crédito interno")
    print("2. Servicio de entrega")
    print("3. Clasificación de café")
    print("4. Reserva de hospedaje")
    print("5. Venta de ferretería")
    print("6. Inventario de una pulpería")
    print("7. Promoción de una tienda")
    print("8. Meta de ventas")
    print("9. Entrega de un comedor")
    print("10. Peso de productos")
    print("0. Salir")

def main():
    while True:
        limpiar_pantalla()
        menu()
        opcion = input("\nSelecciona el número del caso que deseas probar (0-10): ")

        if opcion == "1":
            caso_credito()
        elif opcion == "2":
            caso_entrega()
        elif opcion == "3":
            caso_cafe()
        elif opcion == "4":
            caso_hospedaje()
        elif opcion == "5":
            caso_ferreteria()
        elif opcion == "6":
            caso_inventario()
        elif opcion == "7":
            caso_promocion()
        elif opcion == "8":
            caso_meta()
        elif opcion == "9":
            caso_comedor()
        elif opcion == "10":
            caso_peso()
        elif opcion == "0":
            limpiar_pantalla()
            print("¡Saliendo del programa. Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
