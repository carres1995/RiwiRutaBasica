from src.database.archivo_csv import leer_archivo
from datetime import datetime


def id(lista, llave:str):
    return max((int(item[llave]) for item in lista), default=0) + 1

def tabla_general(datos, encabezados, anchos):
    sep = "-" * (sum(anchos) + 3 * (len(anchos)))
    fmt = " | ".join(f"{{:<{a}}}" for a in anchos)
    print(sep)
    print("| " + fmt.format(*encabezados) + " |")
    print(sep)
    for fila in datos:
        print("| " + fmt.format(*(fila.get(c, "") for c in encabezados)) + " |")
    print(sep)
    
    
def buscar_por_id(id, ruta,eq=None):
    """Busca un equipo por ID y devuelve el dict o None."""
    if eq is None:
        if ruta is None:
            return None
        eq = leer_archivo(ruta)

    for e in eq:
        if str(e["equipo_id"]) == str(id):
            return e
    return None   
def generar_fecha(fecha):
    try:
        fechas=datetime.strptime(fecha, "%d/%m/%Y")
        if fechas.date() < datetime.now().date():
            print("Fecha no valida")
            return False
        return fechas.strftime("%Y-%m-%d")
    except ValueError:
        print("Formato incorrecto. Intente de nuevo.")   
        return False 

  
