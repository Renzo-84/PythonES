import os

def limpiar_pantalla():
    os.system("cls")

# ==========================================================
# Caso 01: Crédito interno
# ==========================================================
def caso_credito():
    print("--- CASO 01: Crédito interno ---\n")
    registrado = input("¿El cliente está registrado? (s/n): ").strip().lower()

    if registrado == "s":
        saldo_pendiente = float(input("Ingrese el saldo pendiente actual (en C$): "))
        if saldo_pendiente <= 500:
            print(f"\n¡Crédito aprobado! Saldo pendiente (C${saldo_pendiente:.2f}) dentro del límite.")
        else:
            print(f"\n¡Crédito denegado! Saldo pendiente (C${saldo_pendiente:.2f}) supera el límite.")
    else:
        print("\n¡Crédito denegado! El cliente no está registrado.")

    input("\nPresione Enter para continuar...")

# ==========================================================
# Caso 02: Servicio de entrega
# ==========================================================
def caso_entrega():
    print("--- CASO 02: Servicio de entrega ---\n")
    zona = input("Ingrese la zona de entrega (urbana / rural): ").strip().lower()
    peso = float(input("Ingrese el peso del paquete (en kg): "))

    if zona == "urbana":
        tarifa = 80 if peso > 5 else 50
        print(f"\nZona Urbana - Tarifa: C${tarifa}")
    elif zona == "rural":
        tarifa = 150 if peso > 5 else 100
        print(f"\nZona Rural - Tarifa: C${tarifa}")
    else:
        print("\nZona no válida. Ingrese 'urbana' o 'rural'.")

    input("\nPresione Enter para continuar...")

# ==========================================================
# Caso 03: Clasificación de café
# ==========================================================
def caso_cafe():
    print("--- CASO 03: Clasificación de café ---\n")
    humedad = float(input("Ingrese el porcentaje de humedad del lote (%): "))

    if 10 <= humedad <= 12:
        defectos = int(input("Ingrese la cantidad de granos defectuosos: "))
        if defectos <= 5:
            print(f"\nHumedad {humedad}%. Defectos {defectos}. Clasificación: Café de Exportación.")
        else:
            print(f"\nHumedad {humedad}%. Exceso de defectos ({defectos}). Clasificación: Consumo Local.")
    else:
        print(f"\nLote rechazado. Humedad {humedad}% fuera del rango (10-12%).")

    input("\nPresione Enter para continuar...")

# ==========================================================
# Caso 04: Reserva de hospedaje
# ==========================================================
def caso_hospedaje():
    print("--- CASO 04: Reserva de hospedaje ---\n")
    temporada = input("¿Es temporada baja? (s/n): ").strip().lower()

    if temporada == "s":
        noches = int(input("Ingrese el número de noches: "))
        if noches >= 3:
            print("\nPromoción: 30% de descuento.")
        else:
            print("\nPromoción: 10% de descuento básico.")
    else:
        print("\nTemporada alta. Tarifa regular.")

    input("\nPresione Enter para continuar...")

# ==========================================================
# Caso 05: Venta de ferretería
# ==========================================================
def caso_ferreteria():
    print("--- CASO 05: Venta de ferretería ---\n")
    tipo_cliente = input("Ingrese el tipo de cliente (mayorista / minorista): ").strip().lower()
    monto = float(input("Ingrese el monto total de la compra (en C$): "))

    if tipo_cliente == "mayorista":
        descuento = "20%" if monto >= 10000 else "10%"
        print(f"\nCliente Mayorista: Descuento aplicado del {descuento}.")
    elif tipo_cliente == "minorista":
        descuento = "5%" if monto >= 3000 else "0%"
        print(f"\nCliente Minorista: Descuento aplicado del {descuento}.")
    else:
        print("\nTipo de cliente no válido.")

    input("\nPresione Enter para finalizar...")

# ==========================================================
# Ejecución secuencial
# ==========================================================
def main():
    limpiar_pantalla()
    caso_credito()
    limpiar_pantalla()
    caso_entrega()
    limpiar_pantalla()
    caso_cafe()
    limpiar_pantalla()
    caso_hospedaje()
    limpiar_pantalla()
    caso_ferreteria()
    limpiar_pantalla()
    print("\n--- Todos los casos han finalizado ---")

if __name__ == "__main__":
    main()
