"""1. Validación de datos con condicionales:
Crea un menú que pregunte al usuario qué acción desea realizar:
Agregar producto
Mostrar inventario
Calcular estadísticas
Salir
Usa condicionales if, elif y else para procesar la opción elegida.
Si el usuario ingresa una opción inválida, muestra un mensaje de error y pide nuevamente la entrada."""


while True:
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    while True:
        try:
            ingresa=int(input("Ingresa una de las opciones: "))
            break
        except ValueError:
            print("La opcion debe ser un numero")
    if ingresa == 1:
        while True:
            producto=input("ingrese Producto: ")
            try:    
                cantidad=int(input("Ingrese las cantidades: "))
            except ValueError:
                print("La opcion debe ser un numero")    
                break
            try:    
                precio=int(input("Ingrese el precio: "))
                print(f"Producto: {producto} | Cantidades: {cantidad} | Precio: {precio}")
                break
            except ValueError:
                print("La opcion debe ser un numero") 
                break            