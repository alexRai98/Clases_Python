def enviar_nota(nota):
    print(f"Enviando nota: {nota}")

def mostrar_notas(notas):    
    for nota in notas: 
        enviar_nota(nota)       
        print(nota)
    
notas_estudiante = [8.5, 9.0, 7.5, 10.0]
mostrar_notas(notas_estudiante)
