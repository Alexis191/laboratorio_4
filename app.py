#Importar la clase desde el archivo .py
from libro_diario_refactor import LibroDiario

#Crear un objeto y agregar loa datos al objeto.
lb = LibroDiario()
lb.agregar_datos("11/06/2025", "Compra de PC", 19, "ingreso")

#Imprimir el resultado de la función.
print(lb.resumen())