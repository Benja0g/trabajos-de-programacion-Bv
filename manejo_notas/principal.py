from data.asignaturas import asignaturas
from data.crear_data import crear_data
import os


#READ
def mostrar_listado_asignaturas():
    print()
    print("listado de asignatura")
    print("=====================")
    contador = 0
    for asignatura in sorted(asignaturas):
        contador += 1
        print(f"{contador}.-{asignatura}")
        
#READ
def buscar_asignatura():
    busqueda = input("ingrese asignatura a buscar: ")
    for asignatura in asignaturas:
        if busqueda.lower() in asignatura.lower():
            return asignatura
#CREATE
def agregar_asignatura():
    mostrar_listado_asignaturas()
    nueva_asignatura = input("ingrese nueva asignatura: ")
    asignaturas.append(nueva_asignatura.title())
    
    crear_data("asignaturas.py","asignaturas",asignaturas)

    mostrar_listado_asignaturas()
#UPDATE
def actualizar_asignatura():
    mostrar_listado_asignaturas()
    busqueda = input("ingrese la asignatura a buscar: ")
    for i in range(len(asignaturas)):
        if busqueda.lower() in asignaturas[i].lower():
            nuevo_dato = input(f"ingrese nuevo nombre para asignatura {asignaturas[i]}: ")
            asignaturas[i] = nuevo_dato
    crear_data("asignaturas.py","asignaturas",asignaturas)
    mostrar_listado_asignaturas()

actualizar_asignatura()



