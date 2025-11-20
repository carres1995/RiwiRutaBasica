"""servicios.py
 ├── agregar_producto()
 ├── mostrar_inventario()
 ├── buscar_producto()
 ├── actualizar_producto()
 ├── eliminar_producto()
 └── calcular_estadisticas()"""
import archivos

def generar_id(inventario):
    if not inventario:
        return 1
    return max(i["id"] for i in inventario) + 1

def agregar_producto(inventario, nombre, precio, cantidad):
    id=generar_id(inventario)
    total=precio * cantidad
    new={
        "id":id,
        "producto":nombre,
        "precio":precio,
        "cantidad":cantidad,
        "total":total
    }
    inventario.append(new)
    print(f"Producto agregado con exito ID: {id}")
    
def mostrar_inventario(inventario):
    if not inventario:
        print("Lista vacia")
        return
    print(f"| {'ID':5} | {'Producto':15} | {'Precio':10} | {'Cantidad':10} | {'Total':10} |")
    for i in inventario:
        print(f'| {i['id']:5} | {i['producto']:15} | {i['precio']:10} | {i['cantidad']:10} | {i['total']:10} |')  
                    
def buscar_producto(inventario, id):#devuelve dict o none
    if not inventario:
        print("Lista vacia")
    for i in inventario:
        if not i['id'] == id:    
            print(f'ID: {id} no existente')
        else:
            print(f'| {i['id']} | {i['producto']} | {i['precio']} | {i['cantidad']} | {i['total']} |')
    return None             
def actualizar_producto(inventario, id, nombre=None, nuevo_precio=None, nueva_cantidad=None):
    producto=buscar_producto(inventario, id)
    if producto is None:
        print("No existe un producto con ese ID.")
        return
    if nombre is not None and nombre != "":
        producto["producto"] = nombre

    if nuevo_precio is not None and nuevo_precio != "":
        producto["precio"] = float(nuevo_precio)

    if nueva_cantidad is not None and nueva_cantidad != "":
        producto["cantidad"] = int(nueva_cantidad)
    producto["total"] = producto["precio"] * producto["cantidad"]
    print("Producto actualizado corectamente")
    
def eliminar_producto(inventario, id):
    producto=buscar_producto(inventario, id)
    if not producto:
        print("No existe un producto con ese ID.")
    inventario.remove(producto)   
     
def unidades_totales(inventario):
    suma = sum(int(i['cantidad']) for i in inventario)
    print(f'Cantidades totales: {suma}')    

def valor_total(inventario):
    suma = sum(int(i['total']) for i in inventario)
    print(f'Costo total de todo el inventario: {suma}')
   
def producto_mas_caro(inventario):
    if not inventario:
        print("No hay productos en el inventario.")
        return
    
    mas_caro = max(inventario, key=lambda i: float(i["precio"]))
    print(f"El productomas caro es: {mas_caro['producto']} con un precio de {mas_caro['precio']}")  
    
def producto_mayor_stock(inventario):
    if not inventario:
        print("No hay productos en el inventario.")
        return  
    mayor_stock=max(inventario, key=lambda i: int(i['cantidad']))
    
    print(f'El producto con el stock mas alto es: {mayor_stock['producto']} con un stock de: {mayor_stock['cantidad']}')       