nombre = input("Ingrese el nombre del estudiante: ")
calificacion = float(input("Ingrese la calificación obtenida (0 a 100): "))

if calificacion >= 60:
    resultado = "Aprobado"
else:
    resultado = "Reprobado"

print(f"{nombre}: {resultado} con una calificación de {calificacion:.1f}")