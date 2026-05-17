saldo_string = input("Escribe tu saldo disponible:\n")
saldo = float(saldo_string)

precio_producto = 100

if saldo >= precio_producto :
    print("Tienes suficiente saldo para comprar el producto")
else:
    print("No tienes suficiente saldo para comprar el producto")