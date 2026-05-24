lista_notas = []
suma_notas = 0

for i in range(1,6):
    nota_str = input(f"Ingrese la nota {i} : ")
    nota = float(nota_str)
    lista_notas.append(nota)
    suma_notas += nota

print(lista_notas)

promedio = suma_notas / len(lista_notas)    
print(f"El promedio es: {promedio}")

if promedio >= 11:
    print("Aprobado")
else:
    print("Desaprobado")


    