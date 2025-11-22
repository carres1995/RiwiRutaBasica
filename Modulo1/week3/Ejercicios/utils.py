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