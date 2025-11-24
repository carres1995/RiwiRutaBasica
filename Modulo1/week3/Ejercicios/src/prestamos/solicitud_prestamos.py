from src.equipos import cargar_equipos
from src.database.archivo_csv import leer_archivo,  guardar_csv
from src.utils import id, generar_fecha
from pathlib import Path
from datetime import datetime, timedelta

RUTA_PRETAMO=Path("data/prestamos.csv")
CABECERA_PRESTAMOS=["prestamo_id", "equipo_id", "nombre_equipo", "usuario_prestatario", "tipo_usuario", "fecha_solicitud", "fecha_prestamo", "dias_autorizados", "dias_solicitados","autorizacion", "estado"]

def cargar_prestamos():
    return leer_archivo(RUTA_PRETAMO) or []

def guardar_prestamos(prestamos):
    return guardar_csv(RUTA_PRETAMO, prestamos, CABECERA_PRESTAMOS)
  

def tipos_usuarios(tipo):
    # Si llega cualquier cosa rara, devuelve 'estudiante' por defecto
    return {"1": "estudiante", "2": "instructor", "3": "administracion"}.get(tipo, "estudiante")
    
def dias_autorizados_prestamo(tipo):
    dias = {"estudiante": 3, "instructor": 7, "administracion": 10}
    # Si por error llega None o cualquier otra cosa, devuelve 3 (mínimo común)
    return dias.get(tipo, 3)

def autorizacion_solicitud(autorizado,solicitado):
    autorizados=dias_autorizados_prestamo(autorizado)
    if 0 < solicitado <= autorizados:        
        return "cumple"
    else:
        return "no cumple"
            
   

def crear_prestamo(equipo_id, usuario_prestatario, tipo_usuario,fecha_prestamo,dias_solicitados,csv_equipo=None, pr= None):
    if pr is None:    
        pr=cargar_prestamos()
        
    if not csv_equipo:
        csv_equipo=cargar_equipos()
        
    equipo=next((e for e in csv_equipo if str(e['equipo_id']) == str(equipo_id)), None)
    if not equipo:
        print("No se encontro equipo")
        return False
    fecha = generar_fecha(fecha_prestamo)
    if not fecha:
        return False
    
    nombre=equipo["nombre_equipo"]    
    tipo= tipos_usuarios(tipo_usuario) 
        
    if dias_solicitados <= 0 or dias_solicitados > dias_autorizados_prestamo(tipo):
        print("dias solicitados fuera del lmite permitido.")
        return False    
    fila= {
        "prestamo_id":str(id(pr,"prestamo_id")),
        "equipo_id":equipo_id,
        "nombre_equipo":nombre,
        "usuario_prestatario": usuario_prestatario,
        "tipo_usuario":tipo,
        "fecha_solicitud":datetime.now().strftime("%Y-%m-%d"),
        "fecha_prestamo":fecha,
        "dias_autorizados":dias_autorizados_prestamo(tipo),
        "dias_solicitados":dias_solicitados,
        "autorizacion":autorizacion_solicitud(tipo, dias_solicitados),
        "estado":"PENDIENTE"                          
    }
    pr.append(fila)
    guardar_prestamos(pr)
    print(f"Solicitud generada con exito")
    return fila