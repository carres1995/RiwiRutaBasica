from datetime import datetime
from pathlib import Path
from src.database.archivo_csv import leer_archivo, guardar_csv
from src.utils import id, tabla_general, buscar_por_id

RUTA_EQUIPOS = Path("data/equipos.csv")
CABECERAS = ["equipo_id", "nombre_equipo", "categoria",
             "estado_actual", "fecha_registro", "descripcion"]


def cargar_equipos():
    """Lee el CSV y devuelve lista de diccionarios."""
    return leer_archivo(RUTA_EQUIPOS) or []


def guardar_equipos(eq):
    """Graba la lista completa en el CSV."""
    guardar_csv(RUTA_EQUIPOS, eq, CABECERAS)



def registrar_equipo(nombre, categoria, descripcion="", eq=None):
    """Crea el equipo en memoria y lo devuelve."""
    if eq is None:
        eq = cargar_equipos()

    nuevo = {
        "equipo_id": str(id(eq, "equipo_id")),
        "nombre_equipo": nombre,
        "categoria": categoria,
        "estado_actual": "DISPONIBLE",
        "fecha_registro": datetime.now().strftime("%Y-%m-%d"),
        "descripcion": descripcion
    }
    eq.append(nuevo)
    guardar_equipos(eq)
    return nuevo



def listar_equipos(eq=None):
    """Muestra la tabla sin tocar el disco."""
    if eq is None:
        eq = cargar_equipos()

    if not eq:
        print("No hay equipos para mostrar.")
        return

    encabezados = ("id", "nombre", "categoría", "estado", "fecha", "descripción")
    anchos = (5, 15, 15, 15, 15, 30)

    datos = []
    for e in eq:
        
        try:
            fila = {
                "id": str(e["equipo_id"]),
                "nombre": e["nombre_equipo"],
                "categoría": e["categoria"],
                "estado": e["estado_actual"],
                "fecha": e["fecha_registro"],
                "descripción": e.get("descripcion", "")
            }
        except KeyError as err:
            print(f"Equipo incompleto (falta {err})  se omite de la tabla.")
            continue
        datos.append(fila)

    print("--" * 20, "Lista de Equipos", "--" * 20)
    tabla_general(datos, encabezados, anchos)
    
"""def buscar_por_id(id, eq=None):
    
    eq = eq or cargar_equipos()

    for e in eq:
        if str(e["equipo_id"]) == str(id):
            return e
    return """

def mostrar_equipo(cod,equipos):
    e=buscar_por_id(cod,RUTA_EQUIPOS, equipos)
    if not e:
        print("No se encontró un equipo con ese ID.")
        return
    """Muestra un solo equipo en formato tabla sencillo."""
    print("--" * 20, "Equipo encontrado", "--" * 20)
    print(f"ID         : {e['equipo_id']}")
    print(f"Nombre     : {e['nombre_equipo']}")
    print(f"Categoría  : {e['categoria']}")
    print(f"Estado     : {e['estado_actual']}")
    print(f"Fecha reg. : {e['fecha_registro']}")
    print(f"Descripción: {e['descripcion']}")
    print("-" * 60)


def eliminar_equipo(cod, equipos):
    equipo=buscar_por_id(cod,RUTA_EQUIPOS, equipos)
    
    if not equipo:
        print("Equipo no existente")
        return False
    equipos.remove(equipo)   
    
    guardar_equipos(equipos) 
    print("Eliminado con exito")
    return equipo
