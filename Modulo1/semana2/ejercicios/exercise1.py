"""1. Cafetería “Buen Café” – Control de tazas servidas
Como barista, quiero usar un bucle for para mostrar cuántas tazas he servido del 1 al 10, pero si el número es 5, mostrar el mensaje “¡Mitad del turno completada!”."""

"""print("CAfeteria (BuenCafe)")

for i in range(10):
    i+=1
    if i == 5:
        print("Mitad del turno completada!")
    print(f"{i}. tazas del basrista")  """ 


"""2. Cine “La Estrella” – Cuenta regresiva antes de iniciar la función
Como proyeccionista, quiero mostrar una cuenta regresiva del 5 al 1 usando for. Si llega al número 1, debe imprimir “¡Que empiece la función!”."""
"""print("Cine (La Estrella)")

numero=6
for i in range(6):
    numero-=1
    if i != 5:
        print(numero)
    else:
        print("Q ue comience la funcion")   """ 
"""3. Gimnasio “Solo Leveling Fit” – Motivación diaria
Como entrenador, quiero usar un while que repita 5 veces el mensaje “¡Tú puedes lograrlo!”, pero en la última repetición muestre “¡Excelente trabajo, terminaste!”."""

"""print("Gimnasio “Solo Leveling Fit”")  
numero= 0
while numero<= 5:
    numero+=1
    print("Tú puedes lograrlo!")
else:
    print("¡Excelente trabajo, terminaste!")   """ 

"""4. Tienda “Descuento Express” – Clientes atendidos
Como cajero, quiero usar un for que muestre “Atendiendo cliente número X” del 1 al 8. Si el cliente es el número 8, mostrar “Último cliente del día”."""

"""print("Tienda “Descuento Express”")
def cliente():
    for i in range(8):
        i+=1
        if i != 8:
            print(f"atendiento cliente {i}")
        else:    
            print("Último cliente del día")
        
cliente() """    

"""5. Escuela “Aprende Más” – Registro de tareas entregadas
Como profesor, quiero usar un while que sume tareas hasta 10. Si el contador llega a 10, mostrar “¡Todas las tareas recibidas!”. Si aún no llega, mostrar cuántas faltan."""

"""print("Escuela “Aprende Más")
tareas=0
while tareas != 10:
    tareas += 1
    print(f"Te faltan {10-tareas}")
else:
    print("Todas las tareas recibidas!") """ 

"""6. Fábrica “LoopTech” – Control de producción
Como supervisor, quiero que un for muestre los productos fabricados del 1 al número que indique el usuario.
Si el número es par, mostrar “Producto verificado”.
Si es impar, mostrar “Producto pendiente”."""

"""print("Fábrica “LoopTech")
numero=int(input("Ingrese el numero: "))
for i in range(numero):
    if i %2 == 0:
        print("Producto verificado")
    else:
        print("Producto pendiente")  """ 

"""7. Restaurante “Buen Sabor” – Revisión de limpieza
Como jefe de cocina, quiero usar un for para repetir 3 veces el mensaje “Limpia tu estación”.
Si es la última vez, mostrar “¡Revisión completada!”."""

"""print("Restaurante “Buen Sabor”")
for i in range(3):
    i+=1
    if i == 3:
        print("¡Revisión completada!")
    else:
        print("Limpia tu estación")  """  


"""lista=[1,2,3,4,5,6,7,8,9]

lista.pop()

print(lista)"""