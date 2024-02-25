from gestor_tareas import *


while True:
    print("Bienvenido al Gestor de Tareas")
    print("Tarea 1: Agregar nueva tarea")
    print("Tarea 2: Mostar todas las tareas")
    print("Tarea 3: Completar tareas")
    print("Tarea 4: Guardar tareas en archivo.txt")
    print("Tarea 5: Salir de la aplicación")

    opcion=input("ingrese el número de la tarea que se desea ejecutar:")

    if opcion=='1':
        nueva_tarea=input("ingrese la nueva tarea:")
        agregar_tarea(tareas, listas_de_tareas)