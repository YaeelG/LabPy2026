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






