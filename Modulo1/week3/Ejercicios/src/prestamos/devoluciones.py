import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime
from src.prestamos.solicitud_prestamos import cargar_prestamos, guardar_prestamos
from src.equipos import cargar_equipos, guardar_equipos
from src.utils import tabla_general

# ----------  lógica  ----------
def dias_entre(f1, f2):
    """f1 y f2 en formato YYYY-MM-DD -> int"""
    return (datetime.strptime(f2, "%Y-%m-%d") -
            datetime.strptime(f1, "%Y-%m-%d")).days

def listar_aprobados_sin_devolucion(pr=None, eq=None):
    """Devuelve lista de préstamos APROBADOS y sin fecha_devolucion"""
    pr = pr or cargar_prestamos()
    data = []
    for p in pr:
        if p.get("estado") == "PRESTADO" and not p.get("fecha_devolucion"):
            data.append({
                "prestamo_id": str(p["prestamo_id"]),
                "equipo_id": p["equipo_id"],
                "nombre_equipo": p["nombre_equipo"],
                "usuario_prestatario": p["usuario_prestatario"],
                "fecha_prestamo": str(p["fecha_prestamo"]).split()[0],
                "dias_solicitados": p["dias_solicitados"],
                "fecha_devolucion": ""  # vacío = no devuelto
            })
    return data

def registrar_devolucion(id_prestamo, fecha_dev=None, pr=None, eq=None):
    """Alta de devolución: calcula días, retraso y actualiza estados."""
    pr = pr or cargar_prestamos()
    eq = eq or cargar_equipos()

    # 1. Buscar préstamo
    p = next((p for p in pr if str(p["prestamo_id"]) == str(id_prestamo)), None)
    if not p:
        print("❌ Préstamo no encontrado.")
        return False
    if p.get("estado") != "PRESTADO":
        print("❌ El préstamo no está en estado PRESTADO.")
        return False
    if p.get("fecha_devolucion"):
        print("❌ El préstamo ya fue devuelto.")
        return False

    # 2. Pedir fecha si no viene
    if fecha_dev is None:
        fecha_dev = input("Fecha de devolución (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(fecha_dev, "%Y-%m-%d")
    except ValueError:
        print("❌ Formato de fecha inválido.")
        return False

    # 3. Cálculos
    fecha_prestamo = str(p["fecha_prestamo"]).split()[0]
    dias_reales = dias_entre(fecha_prestamo, fecha_dev)
    dias_autor = int(p["dias_autorizados"])
    retraso = "SI" if dias_reales > dias_autor else "NO"

    # 4. Actualizar préstamo
    p["fecha_devolucion"] = fecha_dev
    p["dias_reales_usados"] = str(dias_reales)
    p["retraso"] = retraso
    p["estado"] = "DEVUELTO"

    # 5. Actualizar equipo
    equipo = next((e for e in eq if str(e["equipo_id"]) == str(p["equipo_id"])), None)
    if equipo:
        equipo["estado_actual"] = "DISPONIBLE"

    # 6. Persistir
    guardar_prestamos(pr)
    guardar_equipos(eq)

    print(f"✅ Devolución registrada. Días usados: {dias_reales}  Retraso: {retraso}")
    return True

# ----------  test rápido  ----------
if __name__ == "__main__":
    presta = cargar_prestamos()
    equipos = cargar_equipos()

    # 1. Mostrar aprobados sin devolución
    sin_dev = listar_aprobados_sin_devolucion(presta, equipos)
    if not sin_dev:
        print("No hay préstamos APROBADOS pendientes de devolución.")
    else:
        tabla_general(sin_dev,
                      ("prestamo_id", "equipo_id", "nombre_equipo",
                       "usuario_prestatario", "fecha_prestamo",
                       "dias_solicitados", "fecha_devolucion"),
                      (8, 8, 15, 15, 12, 8, 12))

        # 2. Registrar devolución del primero
        id_test = sin_dev[0]["prestamo_id"]
        registrar_devolucion(id_test, pr=presta, eq=equipos)