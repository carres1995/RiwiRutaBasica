"""archivos.py
 ├── guardar_csv()
 └── cargar_csv()"""
import csv
import os

ruta = "datos"

os.makedirs(ruta, exist_ok=True)

ARC_CSV=ruta + "/datos.csv"
def guardar_csv(inventario):
    try:
        with open(ARC_CSV,"w", newline="", encoding="utf-8") as f:
            guardar= csv.DictWriter(f, fieldnames=["id","producto", "precio", "cantidad", "total"])
            guardar.writeheader()
            for lista in inventario:
                guardar.writerow(lista)
        print("se guardo exitosamente") 
    except PermissionError as e:
        print(f"Error no tienes permisos: {e}")
    except Exception as e:
        print(f"Error no ubicado: {e}")               


def cargar_csv(productos):
    productos.clear()
    

    try:
        with open(ARC_CSV,"r", encoding="utf-8") as f:
            leer=csv.DictReader(f)
            encabezados_correctos = {"id", "producto", "precio", "cantidad", "total"}
            if leer.fieldnames is None:
                print("El archivo CSV está vacío o corrupto.")
                return productos
            if set(leer.fieldnames) != encabezados_correctos:
                print("Encabezados inválidos en el CSV.")
                return productos
            
            for row in leer:
                productos.append({
                    "id": row["id"],
                    "producto": row["producto"],
                    "precio": float(row["precio"]),
                    "cantidad": int(row["cantidad"]),
                    "total": float(row["total"])
                })
                
    except FileNotFoundError as e:
        print(f"No se encontro la carpeta: {e}") 
    except Exception as e:
        print(f"Error no ubicado: {e}")      
    return productos   
        
