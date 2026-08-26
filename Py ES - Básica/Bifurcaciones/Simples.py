import os

# ==========================================
# FUSIÓN DE CASOS EMPRESARIALES (SIN IF ANIDADOS)
# ==========================================


def limpiar_pantalla():
    """Limpia la consola según el sistema operativo (Windows o Linux/Mac)."""
    os.system("cls")


def menu():
    print("=== MENÚ DE CASOS EMPRESARIALES ===")
    print("1. Inventario de una pulpería")
    print("2. Promoción de una tienda")
    print("3. Meta de ventas")
    print("4. Entrega de un comedor")
    print("5. Peso de productos")
    print("0. Salir")


def main():
    while True:
        limpiar_pantalla()
        menu()
        opcion = input(
            "\nSelecciona el número del caso que deseas probar (0-5): "
        )

        if opcion == "1":
            limpiar_pantalla()
            # ==========================================
            # 01. Inventario de una pulpería
            # ==========================================
            print("--- CASO 01: Inventario de una pulpería ---\n")
            nombre_producto = input("Ingrese el nombre del producto: ")
            existencia = int(input("Ingrese la cantidad en existencia: "))

            if existencia < 5:
                print(
                    f"\n¡ALERTA! El producto '{nombre_producto}' tiene solo"
                    f" {existencia} unidades. Es necesario reponer."
                )
            else:
                print(
                    f"\nEl producto '{nombre_producto}' cuenta con suficiente"
                    f" existencia ({existencia} unidades)."
                )

            input("\nPresione Enter para regresar al menú...")

        elif opcion == "2":
            limpiar_pantalla()
            # ==========================================
            # 02. Promoción de una tienda
            # ==========================================
            print("--- CASO 02: Promoción de una tienda ---\n")
            monto_original = float(
                input("Ingrese el monto de la compra (en C$): ")
            )

            if monto_original > 1500:
                descuento = monto_original * 0.10
                total = monto_original - descuento
                print(f"\n¡Descuento aplicado del 10% (C${descuento:.2f})!")
                print(f"El monto total a pagar es: C${total:.2f}")
            else:
                print("\nNo aplica para descuento.")
                print(f"El monto total a pagar es: C${monto_original:.2f}")

            input("\nPresione Enter para regresar al menú...")

        elif opcion == "3":
            limpiar_pantalla()
            # ==========================================
            # 03. Meta de ventas
            # ==========================================
            print("--- CASO 03: Meta de ventas ---\n")
            meta = 4000
            total_vendido = float(
                input("Ingrese el total vendido hoy (en C$): ")
            )

            if total_vendido >= meta:
                superado = total_vendido - meta
                print(
                    "\n¡Meta alcanzada y superada!"
                    f" Superó la meta por C${superado:.2f}"
                )
            else:
                faltante = meta - total_vendido
                print(
                    "\nNo se alcanzó la meta."
                    f" Faltaron C${faltante:.2f} para llegar a los C${meta}."
                )

            input("\nPresione Enter para regresar al menú...")

        elif opcion == "4":
            limpiar_pantalla()
            # ==========================================
            # 04. Entrega de un comedor
            # ==========================================
            print("--- CASO 04: Entrega de un comedor ---\n")
            pedido = float(input("Ingrese el valor del pedido (en C$): "))

            if pedido >= 300:
                print("\n¡La entrega es totalmente gratuita!")
                print(f"Total a pagar: C${pedido:.2f}")
            else:
                recargo = 40
                total = pedido + recargo
                print(
                    "\nEl pedido es menor a C$300, se aplica un recargo por"
                    f" entrega de C${recargo}."
                )
                print(f"Total a pagar: C${total:.2f}")

            input("\nPresione Enter para regresar al menú...")

        elif opcion == "5":
            limpiar_pantalla()
            # ==========================================
            # 05. Peso de productos (Sin if anidados)
            # ==========================================
            print("--- CASO 05: Peso de productos ---\n")
            peso_esperado = 46.0
            peso_leido = float(input("Ingrese el peso del saco (en kg): "))

            if peso_leido < peso_esperado:
                print(
                    f"\n¡Atención! El saco pesa {peso_leido} kg. Debe revisarse"
                    f" por estar debajo de los {peso_esperado} kg esperados."
                )
            elif peso_leido == peso_esperado:
                print(
                    "\nEl saco cumple exactamente con el peso esperado de"
                    " 46 kg."
                )
            else:
                print(
                    f"\nEl saco pesa {peso_leido} kg (supera el peso estándar"
                    " de referencia)."
                )

            input("\nPresione Enter para regresar al menú...")

        elif opcion == "0":
            limpiar_pantalla()
            print("¡Saliendo del programa. Hasta luego!")
            break
        else:
            print(
                "\nOpción no válida. Por favor, selecciona un número entre 0"
                " y 5."
            )
            input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()