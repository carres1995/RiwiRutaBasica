"""app.py
 ├── inventario = []
 ├── menú principal (bucle while)
 ├── llama funciones de servicios.py
 └── llama funciones de archivos.py"""
inventarios= []
def menu():
    while True:
        print("1. Agregar")
        print("2. Mostrar")
        print("3. Buscar")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Estadisticas")
        print("7. Guardar CSV")
        print("8. Cargar csv")
        print("9. salir")
        option=int(input("Escoge una opcion: "))
        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        elif option == 6:
            pass
        elif option == 7:
            pass
        elif option == 8:
            pass
        elif option == 9:
            print("Gracias")
            break
        else:
            print("Opcion no valida")