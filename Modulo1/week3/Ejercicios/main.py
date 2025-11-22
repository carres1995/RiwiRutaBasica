from equipos import listar_equipos

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
from equipos import registrar_equipo, listar_equipos, guardar_equipos, cargar_equipos, buscar_por_id, mostrar_equipo

eq = cargar_equipos()

# alta
registrar_equipo("Proyector Epson", "Audiovisual", "Full HD", eq)
guardar_equipos(eq)

# listado
#listar_equipos(eq)
mostrar_equipo(buscar_por_id(4,eq))