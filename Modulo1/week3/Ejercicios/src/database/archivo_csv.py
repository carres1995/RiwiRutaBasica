"""Iniciar sesión con un usuario administrador."""
"""generar permisos totales"""
import csv
import os





def crear_archivo(ruta,cabeceras,datos=None):
    if not os.path.exists(ruta):
        with open(ruta, "w", newline="", encoding="utf-8") as a:
            escribir = csv.DictWriter(a, fieldnames=cabeceras)
            escribir.writeheader()
            if datos:
                for dato in datos:
                    escribir.writerow(dato)
        print(f"Archivo creado: {ruta}.")


def leer_archivo(ruta):
    if not os.path.exists(ruta):
        return []
    
    with open(ruta,"r",newline="",encoding="utf-8") as a:
        leer=csv.DictReader(a)
        return list(leer)

def guardar_csv(ruta, lista ,cabeceras):
    with open(ruta, "w", newline="", encoding="utf-8") as a:
        escribir=csv.DictWriter(a, fieldnames=cabeceras)
        escribir.writeheader()
        for row in lista: 
            escribir.writerow(row)
       

 