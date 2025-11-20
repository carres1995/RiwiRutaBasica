"""archivos.py
 ├── guardar_csv()
 └── cargar_csv()"""
import csv

ARC_CSV="Modulo1/week3/moodle/datos/datos.csv"
def guardar_csv(inventario):
    with open(ARC_CSV,"w") as f:
        guardar= csv.DictWriter(f, fieldnames=["id","producto", "precio", "cantidad", "Total"])
        guardar.writeheader()
        for lista in inventario:
            guardar.writerow(lista)
    print("se guardo exitosamente")        


def cargar_csv(inventario):
    try:
        with open(ARC_CSV,"r") as f:
            leer=csv.DictReader(f)
            for l in leer:
                inventario.append(l)
    except FileNotFoundError as e:
        raise ("Archivo no existente")  
    return leer   
        
