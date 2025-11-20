"""app.py
 ├── inventario = []
 ├── menú principal (bucle while)
 ├── llama funciones de servicios.py
 └── llama funciones de archivos.py"""
import service
import archivos 

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
        option=(input("Escoge una opcion: "))
        if option == "1":
            nombre=input('\nIngrese nombre del producto: ')
            precio=float(input('\nIngrese precio del producto: '))
            cantidad=int(input('\nIngrese cantidad del producto: '))
            service.agregar_producto(inventarios, nombre,precio, cantidad)
        elif option == "2":
            service.mostrar_inventario(inventarios)
        elif option == '3':
            id=int(input('\nIngrese el ID a buscar: '))
            service.buscar_producto(inventarios, id)
        elif option == "4":
            id=int(input('\nIngrese el ID a actualizar: '))
            nombre=input('\nIngrese nombre del producto: ')
            precio=float(input('\nIngrese precio del producto: '))
            cantidad=int(input('\nIngrese cantidad del producto: '))
            service.actualizar_producto(inventarios, id, nombre, precio, cantidad)
        elif option == '5':
            id=int(input('\nIngrese el ID a eliminar: '))
            service.eliminar_producto(inventarios,id)
        elif option == "6":
            menu_estadisticas()
        elif option == "7":
            archivos.guardar_csv(inventarios)
        elif option == "8":
            archivos.cargar_csv(inventarios)
        elif option == "9":
            print("Gracias")
            break
        else:
            print("Opcion no valida")

def menu_estadisticas():
    while True:
        print("1. Unidades totales")
        print("2. valor total")
        print("3. producto mas caro")
        print("4. mayor stock")
        print("5. volver al menu")
        opcion=(input('Ingrese una opcion: ')) 
        if opcion == "1":
            service.unidades_totales(inventarios)
        elif opcion == "2":
            service.valor_total(inventarios)
        elif opcion == "3":
            service.producto_mas_caro(inventarios)
        elif opcion == "4":
            service.producto_mayor_stock(inventarios)
        elif opcion == "5":
            print("Gracias")
            break
        else:
            print("Opcion no valida")


if __name__=="__main__":
    menu()            
          