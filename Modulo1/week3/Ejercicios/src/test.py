"""
from src.prestamos.solicitud_prestamos import crear_prestamo, cargar_prestamos, guardar_prestamos
from src.prestamos.estado_prestamos import listar_solicitudes_pendientes
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

mis_equipos = [
    {
        "equipo_id": 1,
        "nombre_equipo": "Servidor A",
        "categoria": "Hardware",
        "estado_actual": "Activo",
        "fecha_registro": "2023-10-01",
        "descripcion": "Servidor principal de bases de datos"
    },
    {
        "equipo_id": 2,
        "nombre_equipo": "Switch Core",
        "categoria": "Red",
        "estado_actual": "Mantenimiento",
        "fecha_registro": "2023-09-15",
        "descripcion": "Switch de núcleo de la red interna"
    }
]

#listar_equipos(mis_equipos)
from src.equipos import registrar_equipo, listar_equipos, guardar_equipos, cargar_equipos, buscar_por_id, mostrar_equipo

eq = cargar_equipos()
pr= cargar_prestamos()
print("Equipos cargados:", len(eq))
print("Préstamos cargados:", len(pr))


listar_solicitudes_pendientes(pr)
# alta
#crear_prestamo(1,"Carlos","1","10/11/2025",5,eq,pr)
#guardar_equipos(eq)

# listado
#listar_equipos(eq)
#mostrar_equipo(3,eq)
#eliminar_equipo(10,eq)"""

# src/test_estado.py
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.prestamos.solicitud_prestamos import cargar_prestamos, guardar_prestamos
from src.prestamos.estado_prestamos import listar_solicitudes_pendientes, cambiar_estado_solicitud

def test_flujo_estado():
    pr = cargar_prestamos()

    # 1. Ver pendientes actuales
    print("=== PENDIENTES ANTES ===")
    listar_solicitudes_pendientes(pr)

    if not pr:
        print("No hay préstamos para probar.")
        return

    # 2. Tomar el primer préstamo pendiente
    id_prueba = pr[0]["prestamo_id"]
    print(f"\n>>> Probando cambio de estado sobre préstamo ID {id_prueba}")

    # 3. Cambiar estado (automático según autorización)
    cambiar_estado_solicitud(pr, id_prueba)
    guardar_prestamos(pr)

    # 4. Ver pendientes después
    print("\n=== PENDIENTES DESPUÉS ===")
    listar_solicitudes_pendientes(pr)

if __name__ == "__main__":
    test_flujo_estado()