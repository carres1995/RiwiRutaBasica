from archivo_csv import crear_archivo, leer_archivo, guardar_usuario
from datetime import datetime

RUTA_EQUIPOS="Modulo1/week3/Ejercicios/data/equipos.csv"
CABECERAS= ["equipo_id", "nombre_equipo", "categoria","estado_actual","fecha_registro","descripcion"]
equipos= leer_archivo(RUTA_EQUIPOS)

def registrar_equipo(nombre, categoria, descripcion=""):
    equipo_id=max(e["equipo_id"] for e in equipos) + 1
    equipos.append({
        "equipo_id":equipo_id,
        "nombre_equipo":nombre,
        "categoria":categoria,
        "estado_actual":"DISPONIBLE",
        "fecha_registro":datetime.now().strftime("%y-%m-%d"),
        "descripcion":descripcion
    })
    guardar_usuario(RUTA_EQUIPOS,equipos,CABECERAS)
    print(f"Equipo {nombre} se registro con exito")