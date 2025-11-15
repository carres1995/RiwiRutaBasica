"""1. Sistema de Biblioteca Virtual
Descripción:
Crea un programa que permita gestionar una pequeña biblioteca.

Debe permitir:

Ver los libros disponibles.
Agregar nuevos libros.
Prestar libros (cambiar su estado a “prestado”).
Devolver libros.
Ver el historial de préstamos."""

def menu():
    while True:
        print("1. Agregar nuevos libros")
        print("2. Ver libros")
        print("3. Prestamos libros")
        print("4. Ver historial de prestamos")
        print("5. Salir")
        try:
            option=int(input("\nEscoge una opcion: "))
        except ValueError:
            print("Option not validate")  
            continue

        if option == 1:
            nombre=input("\nIngresa nombre del libro: ")
            autor=input("Ingresa nombre del autor: ")
            editor= input("Ingresar editorial ")
            createBooks(nombre,autor,editor)
        elif option == 2:
            readBooks()
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            print("\nThanks you for logging!")
            break
        else:
            print("option not validate.\n")

libros= []

def createBooks(nombre, autor, editor):
    id=len(libros)+1
    
    libros.append({
        "id":id,
        "name": nombre,
        "author":autor,
        "editor":editor,
        "state":"disponible"
    })
    return print(f"\nID: {id} | Book: {nombre} | Author | {autor} | Editor: {editor}\n")

def readBooks():
    if not libros:
        print("Empty list")
    else:
        print(f"\n------------------------------LISTA LIBROS------------------------------------------------")
        for i in libros:
            print(f"| ID: {i["id"]:5} | Book: {i["name"]:15} | Author | {i["author"]:15} | Editor: {i["editor"]:15} | State: {i["state"]} |")
        print("------------------------------------------------------------------------------------------\n")  
historial=[]

def menuLedingBooks():
    while True:
        print("1. Leding Book")
        print("2. Return book")
        try:
            option=int(input("\nEscoge una opcion: "))
        except ValueError:
            print("Option not validate")  
            continue
        if option == 1:
            pass
        elif option == 2:
            pass

def historialBook():
    if not libros:
        print("Empty list")
    else:
        for l in libros:
            pass

def lendingBooks(lend, repay):
    if lend == True:
        estado="no disponible"
        return 
    if repay == False:
        estado="disponible"
        return 
 #guardar historial de prestamo de libros ver de forma cambiar y actualizar el readbook()   
    

if __name__=="__main__":
    menu()

