def saludar(nombre:str="Mundo"):
    print(f"Hola, {nombre}")

def suma(numero1:int, numero2:int)->int:
    resultado = numero1 + numero2
    return resultado 

saludar()
saludar("Juan")