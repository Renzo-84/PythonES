import os

# ==========================================================
# FUSIÓN DE CASOS EMPRESARIALES CON IF ANIDADOS
# ==========================================================


def limpiar_pantalla():
    """Limpia la consola según el sistema operativo (Windows o Linux/Mac)."""
    os.system("cls")


def menu():
    print("=== MENÚ DE CASOS CON IF ANIDADOS ===")
    print("1. Crédito interno (Pulpería)")
    print("2. Servicio de entrega (Emprendimiento)")
    print("3. Clasificación de café (Cooperativa)")
    print("4. Reserva de hospedaje (Granada)")
    print("5. Venta de ferretería (Mayoristas y minoristas)")
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
            # ==========================================================
            # 01. Crédito interno
            # ==========================================================
            print("--- CASO 01: Crédito interno ---\n")
            registrado = (
                input("¿El cliente está registrado? (s/n): ").strip().lower()
            )

            if registrado == "s":
                saldo_pendiente = float(
                    input("Ingrese el saldo pendiente actual (en C$): ")
                )
                if saldo_pendiente <= 500:
                    print(
                        "\n¡Crédito aprobado! El cliente está registrado y su"
                        " saldo pendiente"
                        f" (C${saldo_pendiente:.2f}) no supera el límite de"
                        " C$500."
                    )
                else:
                    print(
                        "\n¡Crédito denegado! Aunque está registrado, su saldo"
                        " pendiente"
                        f" (C${saldo_pendiente:.2f}) supera el límite de"
                        " C$500."
                    )
            else:
                print(
                    "\n¡Crédito denegado! El cliente no está registrado en el"
                    " sistema de créditos."
                )

            input("\nPresione Enter para regresar al menú...")

        elif opcion == "2":
            limpiar_pantalla()
            # ==========================================================
            # 02. Servicio de entrega
            # ==========================================================
            print("--- CASO 02: Servicio de entrega ---\n")
            zona = (
                input("Ingrese la zona de entrega (urbana / rural): ")
                .strip()
                .lower()
            )
            peso = float(input("Ingrese el peso del paquete (en kg): "))

            if zona == "urbana":
                if peso > 5:
                    tarifa = 80
                    print(
                        "\nZona Urbana - Paquete mayor a 5 kg. Tarifa total de"
                        f" envío: C${tarifa}"
                    )
                else:
                    tarifa = 50
                    print(
                        "\nZona Urbana - Paquete de 5 kg o menos. Tarifa total"
                        f" de envío: C${tarifa}"
                    )
            elif zona == "rural":
                if peso > 5:
                    tarifa = 150
                    print(
                        "\nZona Rural - Paquete mayor a 5 kg. Tarifa total de"
                        f" envío: C${tarifa}"
                    )
                else:
                    tarifa = 100
                    print(
                        "\nZona Rural - Paquete de 5 kg o menos. Tarifa total"
                        f" de envío: C${tarifa}"
                    )
            else:
                print("\nZona no válida. Por favor ingrese 'urbana' o 'rural'.")

            input("\nPresione Enter para regresar al menú...")

        elif opcion == "3":
            limpiar_pantalla()
            # ==========================================================
            # 03. Clasificación de café
            # ==========================================================
            print("--- CASO 03: Clasificación de café ---\n")
            humedad = float(
                input("Ingrese el porcentaje de humedad del lote (%): ")
            )

            if 10 <= humedad <= 12:
                defectos = int(
                    input("Ingrese la cantidad de granos defectuosos por muestra: ")
                )
                if defectos <= 5:
                    print(
                        f"\nHumedad óptima ({humedad}%). Defectos bajos"
                        f" ({defectos}). Clasificación: **Café de Exportación"
                        " (Calidad Premium)**."
                    )
                else:
                    print(
                        f"\nHumedad óptima ({humedad}%), pero exceso de"
                        f" defectos ({defectos}). Clasificación: **Café de"
                        " Consumo Local (Estándar)**."
                    )
            else:
                print(
                    f"\nLote rechazado. La humedad ({humedad}%) está fuera del"
                    " rango requerido (entre 10% y 12%)."
                )

            input("\nPresione Enter para regresar al menú...")

        elif opcion == "4":
            limpiar_pantalla()
            # ==========================================================
            # 04. Reserva de hospedaje
            # ==========================================================
            print("--- CASO 04: Reserva de hospedaje ---\n")
            temporada = (
                input("¿Es temporada baja? (s/n): ").strip().lower()
            )

            if temporada == "s":
                noches = int(
                    input("Ingrese el número de noches de la reserva: ")
                )
                if noches >= 3:
                    print(
                        "\n¡Promoción aplicada! Temporada baja con 3 o más"
                        " noches. Obtiene un **30% de descuento** en su"
                        " hospedaje."
                    )
                else:
                    print(
                        "\nTemporada baja, pero la reserva es de menos de 3"
                        " noches. Obtiene un **10% de descuento** básico."
                    )
            else:
                print(
                    "\nTemporada alta. No aplican promociones de descuento"
                    " especial, tarifa regular."
                )

            input("\nPresione Enter para regresar al menú...")

        elif opcion == "5":
            limpiar_pantalla()
            # ==========================================================
            # 05. Venta de ferretería
            # ==========================================================
            print("--- CASO 05: Venta de ferretería ---\n")
            tipo_cliente = (
                input("Ingrese el tipo de cliente (mayorista / minorista): ")
                .strip()
                .lower()
            )

            if tipo_cliente == "mayorista":
                monto = float(
                    input("Ingrese el monto total de la compra (en C$): ")
                )
                if monto >= 10000:
                    print(
                        "\nCliente Mayorista: Compra superior o igual a"
                        " C$10,000. Descuento aplicado del **20%**."
                    )
                else:
                    print(
                        "\nCliente Mayorista: Compra menor a C$10,000."
                        " Descuento aplicado del **10%**."
                    )
            elif tipo_cliente == "minorista":
                monto = float(
                    input("Ingrese el monto total de la compra (en C$): ")
                )
                if monto >= 3000:
                    print(
                        "\nCliente Minorista: Compra superior o igual a"
                        " C$3,000. Descuento aplicado del **5%**."
                    )
                else:
                    print(
                        "\nCliente Minorista: Compra menor a C$3,000. No aplica"
                        " descuento."
                    )
            else:
                print(
                    "\nTipo de cliente no válido. Ingrese 'mayorista' o"
                    " 'minorista'."
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