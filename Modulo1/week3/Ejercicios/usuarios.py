from archivo_csv import crear_archivo, leer_archivo,guardar_usuario


RUTA_USUARIO="Modulo1/week3/Ejercicios/data/usuarios.csv"
CABECERAS=["usuario", "contraseña", "rol"]

crear_archivo(RUTA_USUARIO,CABECERAS,datos=[{"usuario":"ADMIN", "contraseña":"1234", "rol":"ADMIN"}])

def login():
    usuarios=leer_archivo(RUTA_USUARIO)
    intentos= 0
    max_intectos= 3
    while intentos < max_intectos:
        print("\n Inicio de sesion obligatorio")
        usuario = input("Usuario: ").strip()
        contrasena = input("Contrasena: ").strip()
        for u in usuarios:
            if u["usuario"] == usuario and u["contraseña"] == contrasena:
                print(f"Inicio de sesion exitosa {usuario}")
                return True
        intentos += 1
        print(f"INTENTO #: {intentos} de {max_intectos}")  
    print("No tienes mas oportunidades. No autorizado")
    return False  

