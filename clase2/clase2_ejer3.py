user = input("Ingrese su usuario:\n")
password = input("Ingrese su contraseña:\n")

user_admin = "admin"
password_admin = "1234"

if user == user_admin and password == password_admin:
    print("Bienvenido administrador")
else:
    print("Usuario o contraseña incorrectos")
