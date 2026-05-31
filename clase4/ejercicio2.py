ventas = []

def registrar_venta():
    venta_str = input("Ingrese el monto de la venta: ")
    ventas.append(float(venta_str))
    print("Venta registrada.")

def mostrar_ventas():
    if len(ventas)== 0:
        print("No hay ventas registradas.")
        return

    for index, venta in enumerate(ventas):
        print(f"Venta {index + 1}: S/",venta)

def total_vendido():
    total = sum(ventas)
    print(f"Total vendido: S/{total}")

def promedio_venta():
    total_ventas = len(ventas)
    if total_ventas == 0:
        print("No hay ventas registradas.")
        return
    
    promedio = sum(ventas) / total_ventas
    print(f"Promedio de venta: S/{promedio:.2f}")

def menu():
    print("1. Registrar venta")
    print("2. Mostrar ventas")
    print("3. Mostrar total vendido")
    print("4. Mostrar promedio de venta")
    print("5. Salir")


opcion = ""
menu()
while opcion != "5":
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            registrar_venta()
        case "2":
            mostrar_ventas()
        case "3":
            total_vendido()
        case "4":
            promedio_venta()
        case "5":
            print("Saliendo del programa.")
        case _:
            print("Opción no válida. Intente nuevamente.")