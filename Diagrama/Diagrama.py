import os

def limpiar_pantalla():
    os.system("cls")



def calcular_total_con_descuento(subtotal, descuento):
    monto_resultante = subtotal - descuento
    return monto_resultante


def calcular_descuento(subtotal, porcentaje):
    
    #Calcula el monto del descuento y llama a calcular_total_con_descuento().
    
    descuento = subtotal * (porcentaje / 100)
    # Envía subtotal y descuento a calcular_total_con_descuento()
    subtotal_con_descuento = calcular_total_con_descuento(subtotal, descuento)
    return descuento, subtotal_con_descuento


def calcular_subtotal(precio, cantidad):
    #Calcula el subtotal multiplicando precio por cantidad.
    subtotal = precio * cantidad
    return subtotal


def calcular_total_productos(subtotal, productos, porcentaje):
    #Envía subtotal y porcentaje a calcular_descuento()
    descuento, subtotal_con_descuento = calcular_descuento(subtotal, porcentaje)
    return descuento, subtotal_con_descuento


def calcular_total(precio, cantidad, datos, porcentaje, impuesto, productos):
    #Módulo principal de cálculo que coordina la obtención del subtotal,
    #descuento, IVA y total final.
    # 1. Obtener subtotal
    subtotal = calcular_subtotal(precio, cantidad)

    # 2. Obtener descuento y subtotal con descuento aplicado
    descuento, subtotal_con_descuento = calcular_total_productos(
        subtotal, productos, porcentaje
    )

    # 3. Calcular IVA sobre el monto resultante y el Total Final
    iva = subtotal_con_descuento * (impuesto / 100)
    total = subtotal_con_descuento + iva

    return total, subtotal, descuento, iva


def leer_datos(mensaje):
    
    #Muestra el mensaje inicial y lee la información del cliente y productos.
    
    print(mensaje)
    print("=" * 40)

    nombre = input("Nombre del cliente: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad de productos: "))
    porcentaje = float(input("Porcentaje de descuento (%): "))
    impuesto = float(input("Porcentaje de IVA (%): "))

    datos = "Datos de cliente procesados"
    productos = "Lista de productos procesada"

    return datos, productos, nombre, precio, cantidad, porcentaje, impuesto


def mostrar_factura(
    nombre,
    precio,
    cantidad,
    porcentaje,
    impuesto,
    total,
    subtotal,
    descuento,
    iva,
):
    #Muestra en pantalla el desglose completo de la factura.
    print("\n" + "=" * 40)
    print("           FACTURA DE VENTA           ")
    print("=" * 40)
    print(f"Cliente:               {nombre}")
    print(f"Precio unitario:       ${precio:,.2f}")
    print(f"Cantidad:              {cantidad}")
    print("-" * 40)
    print(f"Subtotal:              ${subtotal:,.2f}")
    print(f"Descuento ({porcentaje:.0f}%):       -${descuento:,.2f}")
    print(f"IVA ({impuesto:.0f}%):             +${iva:,.2f}")
    print("=" * 40)
    print(f"TOTAL A PAGAR:         ${total:,.2f}")
    print("=" * 40)


def main():
    # Limpia la pantalla al iniciar la ejecución del programa
    limpiar_pantalla()

    mensaje = "=== SISTEMA DE FACTURACIÓN ==="

    # 1. Leer los datos necesarios
    datos, productos, nombre, precio, cantidad, porcentaje, impuesto = (
        leer_datos(mensaje)
    )

    # 2. Calcular los montos según la jerarquía de funciones
    total, subtotal, descuento, iva = calcular_total(
        precio, cantidad, datos, porcentaje, impuesto, productos
    )

    # 3. Imprimir el resumen de la factura
    mostrar_factura(
        nombre,
        precio,
        cantidad,
        porcentaje,
        impuesto,
        total,
        subtotal,
        descuento,
        iva,
    )


# Punto de entrada del programa
if __name__ == "__main__":
    main()