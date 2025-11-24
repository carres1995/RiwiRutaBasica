from src.equipos import cargar_equipos, guardar_equipos
from src.prestamos.solicitud_prestamos import cargar_prestamos, RUTA_PRETAMO, guardar_prestamos
from src.utils import tabla_general, id, buscar_por_id
from src.database.archivo_csv import leer_archivo, crear_archivo, guardar_csv
from pathlib import Path
from datetime import datetime
import os

RUTA_ESTADOS=Path("data/aprobacion.csv")
CABECERAS_ESTADO=["id_estado","prestamo_id","nombre_usuario","fecha_cambio","estado"]

def carga_estado():
    if not RUTA_ESTADOS.exists():
        crear_archivo(RUTA_ESTADOS, CABECERAS_ESTADO)
    return leer_archivo(RUTA_ESTADOS)
    
def guardar_estados(estados):
    guardar_csv(RUTA_ESTADOS, estados, CABECERAS_ESTADO)


def listar_solicitudes_pendientes(solicitudes):
    if not solicitudes:
        print("No hay solicitudes para mostrar.")
        return
    
    cabecera=("prestamo_id", "equipo_id", "nombre_equipo", "usuario_prestatario", "tipo_usuario", "fecha_solicitud", "fecha_prestamo", "dias_autorizados", "dias_solicitados","autorizacion", "estado")  
    anchos=(11,11, 18, 18, 15, 15, 15, 11, 11, 15, 13)
    data=[]
    for s in solicitudes:
        if s["estado"] == "PENDIENTE":
            try:
                fila={
                    "prestamo_id":str(s["prestamo_id"]),
                    "equipo_id":s["equipo_id"],
                    "nombre_equipo":s["nombre_equipo"],
                    "usuario_prestatario": s["usuario_prestatario"],
                    "tipo_usuario":s["tipo_usuario"],
                    "fecha_solicitud":s["fecha_solicitud"],
                    "fecha_prestamo":str(s["fecha_prestamo"]).split()[0],
                    "dias_autorizados":s["dias_autorizados"],
                    "dias_solicitados":s["dias_solicitados"],
                    "autorizacion":s["autorizacion"],
                    "estado":s["estado"]
                }
                
            except KeyError as err:
                print(f"Solicitud incompleta (falta {err})  se omite de la tabla.")
                continue   
          
            data.append(fila)
    print("--" * 20, "Lista de Equipos", "--" * 20)
    tabla_general(data,cabecera,anchos)

def crear_estado(id_prestamo,nuevo_estado, es=None, pr=None):
    if pr is None:
        pr=cargar_prestamos()
    if es is None:
        es=carga_estado()    
    estado=next((p for p in pr if str(p["prestamo_id"]) == id_prestamo),None)
    if not estado:
        print(f"ID {id_prestamo} de solicitud no existente")
        return False
    nombre=estado["usuario_prestatario"]
    
    
    fila = {
        "id_estado":str(id(es,"id_estado")),
        "prestamo_id":id_prestamo,
        "nombre_usuario":nombre,
        "fecha_cambio":datetime.now().strftime("%Y-%m-%d"),
        "estado":nuevo_estado
    }
    
    es.append(fila)
    guardar_estados(es)
    print(f"Estado creado con exito")
    return fila
    
def buscar_autorizacion(id,pr=None):
    if pr is None:
        pr=cargar_prestamos()
    p=buscar_por_id(id, RUTA_PRETAMO, pr)
    if not p:
        print("No se encontro el id")
        return
    print("--" * 20, "Equipo encontrado", "--" * 20)
    print(f"ID         : {p['prestamo_id']}")
    print(f"Nombre     : {p['usuario_prestatario']}")
    print(f"Cumple con los tiempos  : {p['autorizacion']}") 

def cambiar_estado_solicitud(id_cambio, autorizacion, pr=None, estado=None, equipo=None):
    if pr is None:
        pr = cargar_prestamos()
    if estado is None:
        estado = carga_estado()
    if equipo is None:
        equipo = cargar_equipos()

    print("DEBUG ESTADO:")
    for e in estado:
        print(e)

    p = next((p for p in pr if str(p['prestamo_id']) == str(id_cambio)), None)
    if not p:
        print("No se encontro el préstamo")
        return False 
    es = next((e for e in estado if str(e['prestamo_id']) == str(id_cambio)), None)
    if not es:
        print("No se encontro el estado")
        return False
    eq = next((eq for eq in equipo if str(eq['equipo_id']) == str(p['equipo_id'])), None) 
    if not eq:
        print("No se encontro el equipo")
        return False

    if autorizacion.lower() == "no":
        eq["estado_actual"] = "DISPONIBLE"
        es["estado"] = "RECHAZADO"
        p["estado"] = "RECHAZADO"
        print("Prestamo denegado – equipo libre")
        
    elif autorizacion.lower() == "si":
        p["estado"] = "PRESTADO"
        es["estado"] = "PRESTADO"
        eq["estado_actual"] = "PRESTADO"
        print("Prestamo aprobado – equipo entregado")
    else:
        print("Opcion no valida")
        return

    guardar_prestamos(pr)
    guardar_equipos(equipo)
    guardar_estados(estado)
    return True





cambiar_estado_solicitud(1,"no")