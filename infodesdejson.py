import json

with open(r'C:\Users\ricar\Desktop\estudiuo\empleados.json', encoding='utf-8', mode='r') as datos:
    empresa = json.load(datos)

def empleadospordepartamento():
    print("=== EMPLEADOS POR DEPARTAMENTO ===")
    for departamento in empresa["departamentos"]:
        print("==================================")
        print(f"Departamento: {departamento['nombre']}")
        print("------------------------")
        for empleado in departamento["empleados"]:
            estado = "Activo" if empleado["activo"] else "Inactivo"
            print(f"Nombre: {empleado['nombre']} | Puesto: {empleado['puesto']} | Estado: {estado}")

opcion = 0
while opcion != 2:
    print("======================")
    print("=== MENÚ PRINCIPAL ===")
    print("(1) Mostrar empleados por departamento")
    print("(2) Salir")
    print("======================")
    
    opcion = int(input("Ingrese su opción: "))
    
    if opcion == 1:
        empleadospordepartamento()
    elif opcion == 2:
        print("Saliendo del programa... ¡Hasta luego!")
    else:
        print("Opción no válida. Por favor ingrese 1 o 2.")
