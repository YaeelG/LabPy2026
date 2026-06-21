# SISTEMA DE GESTIÓN DE TORNEO AMATEUR
# Trabajo Final Integrador
#El sistema deberá permitir administrar un torneo deportivo amateur. La solución podrá contemplar registro de equipos, carga de resultados,
#cálculo automático de puntos, posiciones y estadísticas generales del torneo.
#El sistema podrá incluir control de partidos jugados, diferencia de goles y generación de tablas de posiciones básicas.
"""
Implementar:
 - estructuras condicionales
 - estructuras repetitivas
 - modularizacion(funciones, def)
 - valiaciones
 - acumuladores y contadores
 - manejo básico de errores y mensajes al usuario.
"""
# Funciones y procedimientos :
    # Menu
    # registrar equipos (contemplar carga de varios equipos de manera manual o un archivo)
    # carga de resultados (Local y visitante)
    # cálculo automático de puntos
    # posiciones
    # estadísticas generales del torneo (contemplar diferencia de goles, empates,) 
    # Editar equipos (eliminar, editar nombre )
    # Premios (habilitado una vez jugado todo los partidos, aparecen solo las primeras 3 posiciones)
    # Cantidad de partidos: cantidad de equipos - 1 (contemplamos un torneo amateur 1 solo partido de ida)
    

# mensajes de error
equipos = []

def registrar_equipos():
    cantidad = int(input("¿Cuántos equipos desea registrar? "))

    for i in range(cantidad):
        nombre = input(f"Nombre del equipo {i+1}: ")

        equipo = {
            "nombre": nombre,
            "pj": 0,
            "pg": 0,
            "pe": 0,
            "pp": 0,
            "gf": 0,
            "gc": 0,
            "dg": 0,
            "pts": 0
        }

        equipos.append(equipo)

def mostrar_equipos():
    for equipo in equipos:
        print(equipo["nombre"])

def buscar_equipo(nombre):
    for equipo in equipos:
        if equipo["nombre"] == nombre:
            return equipo

    return None



#//GESTION DE EQUIPOS // NICO


def cargar_resultado(equipos):

    print("\nEquipos disponibles:")

    for i, equipo in enumerate(equipos):
        print(i + 1, "-", equipo["nombre"])

    local = int(input("Seleccione equipo local: ")) - 1
    visitante = int(input("Seleccione equipo visitante: ")) - 1

    goles_local = int(
        input(f"Goles de {equipos[local]['nombre']}: ")
    )

    goles_visitante = int(
        input(f"Goles de {equipos[visitante]['nombre']}: ")
    )

    equipo_local = equipos[local]
    equipo_visitante = equipos[visitante]

    equipo_local["pj"] += 1
    equipo_visitante["pj"] += 1

    equipo_local["gf"] += goles_local
    equipo_local["gc"] += goles_visitante

    equipo_visitante["gf"] += goles_visitante
    equipo_visitante["gc"] += goles_local

    if goles_local > goles_visitante:

        equipo_local["pg"] += 1
        equipo_local["pts"] += 3

        equipo_visitante["pp"] += 1

    elif goles_local < goles_visitante:

        equipo_visitante["pg"] += 1
        equipo_visitante["pts"] += 3

        equipo_local["pp"] += 1

    else:

        equipo_local["pe"] += 1
        equipo_visitante["pe"] += 1

        equipo_local["pts"] += 1
        equipo_visitante["pts"] += 1
#//ACA TERMINA GESTION DE EQUIPOS



def actualizar_dg(equipos):

    for equipo in equipos:
        equipo["dg"] = equipo["gf"] - equipo["gc"]


def mostrar_tabla(equipos):

    actualizar_dg(equipos)

    tabla = sorted(
        equipos,
        key=lambda e: (e["pts"], e["dg"]),
        reverse=True
    )

    print("\nTABLA DE POSICIONES")

    for i, equipo in enumerate(tabla):

        print(
            i + 1,
            equipo["nombre"],
            "PTS:", equipo["pts"],
            "DG:", equipo["dg"]
        )
#//Estadisticas // Lautaro
Archivo: estadisticas.py
def mostrar_estadisticas(equipos):

    total_goles = 0

    for equipo in equipos:
        total_goles += equipo["gf"]

    equipo_goleador = max(
        equipos,
        key=lambda e: e["gf"]
    )

    print("\nESTADÍSTICAS")

    print("Cantidad de equipos:", len(equipos))
    print("Total de goles:", total_goles)

    print(
        "Equipo más goleador:",
        equipo_goleador["nombre"]
    )
#//FinEstadisticas //



