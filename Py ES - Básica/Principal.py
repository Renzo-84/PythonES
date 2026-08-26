import os
def main():
    os.system("cls")
    #La variable nombre_producto es de tipo str
    nombre_producto = input("Ingrese el nombre del producto: ")
    #La variable precio_producto es de tipo float
    precio_producto = float(input("Ingrese el precio del producto: ")) 
    #La variable cantidad_producto es de tipo int
    cantidad_producto = int(input("Ingrese la cantidad del producto: ")) 
    #La variable descuento es de tipo bool
    respuesta = input("¿El producto tiene descuento? (s/n): ").strip().upper()
    descuento = respuesta in ["S","SI","YES","Y", "VERDADERO","TRUE", "T" , "V" ,"1"] 

    os.system("cls") 
    print(f"---RESUMEN DE FACTURA---")
    print(f"Producto: {nombre_producto}")
    print(f"Precio: ${precio_producto:}")
    print(f"Cantidad: {cantidad_producto}")
    print(f"Descuento: {descuento}")

main()
