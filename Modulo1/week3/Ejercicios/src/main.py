import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.usuarios import login
from src.equipos import registrar_equipo, listar_equipos, mostrar_equipo, eliminar_equipo, cargar_equipos
from src.prestamos.solicitud_prestamos import crear_prestamo, cargar_prestamos
from src.prestamos.estado_prestamos import listar_solicitudes_pendientes, cambiar_estado_solicitud,buscar_autorizacion, carga_estado
from src.prestamos.devoluciones import listar_aprobados_sin_devolucion, registrar_devolucion
#from src.reportes import exportar_reporte_mes
pr=cargar_prestamos()
es=carga_estado()
eq=cargar_equipos()


def menu_principal():
    while True:
        print("\n========== MENÚ PRINCIPAL TechLab ==========")
        print("1. Gestionar equipos")
        print("2. Gestionar préstamos")
        print("3. Registrar devolución")
        print("4. Exportar reporte mensual")
        print("0. Salir")
        opc = input("Seleccione: ").strip()

        if opc == "1":
            menu_equipos()
        elif opc == "2":
            menu_prestamos()
        elif opc == "3":
            menu_devolucion()
        elif opc == "4":
            menu_reportes()
        elif opc == "0":
            print("¡Hasta pronto!")
            sys.exit()
        else:
            print("❌ Opción no válida.")

def menu_equipos():
    while True:
        print("\n----- GESTIÓN DE EQUIPOS -----")
        print("1. Registrar equipo")
        print("2. Listar equipos")
        print("3. Consultar equipo")
        print("4. Eliminar equipo")
        print("0. Volver")
        op = input("Seleccione: ").strip()

        eq = cargar_equipos()

        if op == "1":
            nombre = input("Nombre del equipo: ").strip()
            categoria = input("Categoría: ").strip()
            desc = input("Descripción (opcional): ").strip()
            registrar_equipo(nombre, categoria, desc, eq)

        elif op == "2":
            listar_equipos(eq)

        elif op == "3":
            cod = input("ID del equipo a consultar: ").strip()
            mostrar_equipo(cod, eq)

        elif op == "4":
            cod = input("ID del equipo a eliminar: ").strip()
            eliminar_equipo(cod, eq)

        elif op == "0":
            break
        else:
            print("❌ Opción no válida.")

def menu_prestamos():
    while True:
        print("\n----- GESTIÓN DE PRÉSTAMOS -----")
        print("1. Nueva solicitud")
        print("2. Listar pendientes")
        print("3. Aprobar / Rechazar")
        print("0. Volver")
        op = input("Seleccione: ").strip()

        pr = cargar_prestamos()
        eq = cargar_equipos()

        if op == "1":
            equipo_id = input("ID del equipo a prestar: ").strip()
            usuario = input("Nombre del solicitante: ").strip()
            print("Tipo de usuario:\n1. Estudiante\n2. Instructor\n3. Administrativo")
            tipo = input("Seleccione: ").strip()
            fecha_prestamo = input("Fecha de préstamo (DD/MM/YYYY): ").strip()
            dias = int(input("Días solicitados: ").strip())
            crear_prestamo(equipo_id, usuario, tipo, fecha_prestamo, dias, eq, pr)

        elif op == "2":
            listar_solicitudes_pendientes(pr)

        elif op == "3":
            id_cambio=int(input("Ingrese el id a aprobar: ").strip())
            
            pr = cargar_prestamos()
            eq = cargar_equipos()
            es = carga_estado()   
            
            buscar_autorizacion(id_cambio,pr)
            autorizacion=input("Ingrese si deseas aprobarlo (si) o rechazarlo (no): ")
            cambiar_estado_solicitud(id_cambio,autorizacion, pr,es, eq)

        elif op == "0":
            break
        else:
            print(" Opción no válida.")

def menu_devolucion():
    print("\n----- REGISTRAR DEVOLUCIÓN -----")
    pr = cargar_prestamos()
    eq = cargar_equipos()
    sin_dev = listar_aprobados_sin_devolucion(pr, eq)
    if not sin_dev:
        print("No hay préstamos APROBADOS pendientes de devolución.")
        return
    id_prestamo = input("ID del préstamo a devolver: ").strip()
    registrar_devolucion(id_prestamo, pr=pr, eq=eq)

def menu_reportes():
    print("\n----- EXPORTAR REPORTE MENSUAL -----")
    anio = input("Año (YYYY): ").strip()
    mes = input("Mes (MM): ").strip()
    #exportar_reporte_mes(anio, mes)
    
if __name__ == "__main__":
    if login():
        menu_principal()    