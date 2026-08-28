import os

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo (Windows)."""
    os.system("cls")

# ==========================================
# Caso 01: Inventario de una pulpería
# ==========================================
def caso_inventario():
    print("--- CASO 01: Inventario de una pulpería ---\n")
    nombre_producto = input("Ingrese el nombre del producto: ")
    existencia = int(input("Ingrese la cantidad en existencia: "))

    if existencia < 5:
        print(f"\n¡ALERTA! El producto '{nombre_producto}' tiene solo {existencia} unidades. Es necesario reponer.")
    else:
        print(f"\nEl producto '{nombre_producto}' cuenta con suficiente existencia ({existencia} unidades).")

    input("\nPresione Enter para continuar...")

# ==========================================
# Caso 02: Promoción de una tienda
# ==========================================
def caso_promocion():
    print("--- CASO 02: Promoción de una tienda ---\n")
    monto_original = float(input("Ingrese el monto de la compra (en C$): "))

    if monto_original > 1500:
        descuento = monto_original * 0.10
        total = monto_original - descuento
        print(f"\n¡Descuento aplicado del 10% (C${descuento:.2f})!")
        print(f"El monto total a pagar es: C${total:.2f}")
    else:
        print("\nNo aplica para descuento.")
        print(f"El monto total a pagar es: C${monto_original:.2f}")

    input("\nPresione Enter para continuar...")

# ==========================================
# Caso 03: Meta de ventas
# ==========================================
def caso_meta():
    print("--- CASO 03: Meta de ventas ---\n")
    meta = 4000
    total_vendido = float(input("Ingrese el total vendido hoy (en C$): "))

    if total_vendido >= meta:
        superado = total_vendido - meta
        print(f"\n¡Meta alcanzada y superada! Superó la meta por C${superado:.2f}")
    else:
        faltante = meta - total_vendido
        print(f"\nNo se alcanzó la meta. Faltaron C${faltante:.2f} para llegar a los C${meta}.")

    input("\nPresione Enter para continuar...")

# ==========================================
# Caso 04: Entrega de un comedor
# ==========================================
def caso_comedor():
    print("--- CASO 04: Entrega de un comedor ---\n")
    pedido = float(input("Ingrese el valor del pedido (en C$): "))

    if pedido >= 300:
        print("\n¡La entrega es totalmente gratuita!")
        print(f"Total a pagar: C${pedido:.2f}")
    else:
        recargo = 40
        total = pedido + recargo
        print(f"\nEl pedido es menor a C$300, se aplica un recargo por entrega de C${recargo}.")
        print(f"Total a pagar: C${total:.2f}")

    input("\nPresione Enter para continuar...")

# ==========================================
# Caso 05: Peso de productos
# ==========================================
def caso_peso():
    print("--- CASO 05: Peso de productos ---\n")
    peso_esperado = 46.0
    peso_leido = float(input("Ingrese el peso del saco (en kg): "))

    if peso_leido < peso_esperado:
        print(f"\n¡Atención! El saco pesa {peso_leido} kg. Debe revisarse por estar debajo de los {peso_esperado} kg esperados.")
    elif peso_leido == peso_esperado:
        print("\nEl saco cumple exactamente con el peso esperado de 46 kg.")
    else:
        print(f"\nEl saco pesa {peso_leido} kg (supera el peso estándar de referencia).")

    input("\nPresione Enter para finalizar...")

# ==========================================
# Ejecución secuencial
# ==========================================
def main():
    limpiar_pantalla()
    caso_inventario()
    limpiar_pantalla()
    caso_promocion()
    limpiar_pantalla()
    caso_meta()
    limpiar_pantalla()
    caso_comedor()
    limpiar_pantalla()
    caso_peso()
    limpiar_pantalla()
    print("\n--- Todos los casos han finalizado ---")

if __name__ == "__main__":
    main()
