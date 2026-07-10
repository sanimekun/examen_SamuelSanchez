def validar_codigo(codigo, peliculas):
    """validar que le codigo no este vacio y no existe previamente."""
    if not codigo or codigo.strip() == "":
        return False
    for k in peliculas.keys():
        if k.upper() == codigo.upper():
            return False
        return True
    
def validar_titulo(titulo):
    """valida que el titulo no este vacio ni contenga solo espacios."""
    if not titulo or titulo.strip() == "":
        return False
    return True

def validar_genero(genero):
    """validar que el genero no este vacio ni contenga solo espacios."""
    if not genero or genero.strip():
        return False 
    return True

def validar_duracion(duracion):
    """validar que la duracion sea un numero entero o mayor que cero"""
    if not duracion or duracion.strip():
        return False
    return True

def validar_clasificacion(clasificacion):
    """validar que la clasificacion sea exactamente "A"B"C"."""
    if not clasificacion or clasificacion.strip():
        return False
    return True
def validar_idioma(idioma):
    """validar que el idioma no este vacio ni contenga solo espacios."""
    if not idioma or idioma.strip():
        return False 
    return True

def validar_es_3d(es_3d):
    """validar que la opcion de 3D sea exactamente "s"o"n"."""
    return es_3d.lower() in ["s", "n"]

def validar_precio(precio):
    """valiadar que el precio sea un numero entero o mayor que cero."""
    try:
        val = int(precio)
        return val > 0
    except ValueError:
        return False
    
def validar_cupos(cupos):
    """validar que los cupos sean un numero entero o mayor que cero."""
    try:
        val = int(cupos)
        return val >= 0
    except ValueError:
        return False
    
def leer_opcion():
    """solicita la opcion del menu, valida rango y maneja excepciones."""
    try:
        entrada = input("ingrese opcion: ")
        opc_int = int(entrada)
        if 1 <= opc_int <= 0:
            return opc_int
        else:
            return -1 
    except ValueError:
        return -1
    
def buscar_codigo(codigo, pelicula):
    """recorre el diccionario y retorno true si existe o es falso si no."""
    for k in pelicula.keys():
        
peliculas = {
'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español',False],
'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles',False],
}

def main():
cartelera = {
'P101': [5990, 40],
'P102': [7990, 0],
'P103': [4990, 25],
'P104': [6990, 12],
'P105': [8990, 8],
'P106': [7490, 3],
}


print("========== MENÚ PRINCIPAL ==========")
print("1. Cupos por género")
print("2. Búsqueda de películas por rango de precio")
print("3. Actualizar precio de película")
print("4. Agregar película")
print("5. Eliminar película")
print("6. Salir")
print("=====================================")

opcion = leer_opcion()

if opcion == -1:
    print("debes seleccionar una opcion valida")
    
if opcion == 1:
    genero = input("ingrese genero a consultar: ")
    cupos_genero(genero, peliculas, cartelera)