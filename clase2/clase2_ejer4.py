name = input("¿Ingresa tu nombre?\n")
age_str = input("Ingresa tu edad:\n")
premium = input("¿Eres cliente premium? (S/N)\n")

age = int(age_str)

premium_apper = premium.upper()

if age >= 18 and premium_apper == "S":
    if name == "Juan":
        print("Bienvenido Juan, tienes acceso completo")
    else:
        print("Bienvenido", name, "tienes acceso completo")

elif age <= 18 and premium_apper == "S":
    print("Acceso liminitado por edad")
else:
    print("Acceso denegado")


