"""1. Crea un archivo llamado `gestor_tareas.py`.
Implementa funciones para gestionar una lista de tareas. Puedes llamar a estas
funciones `agregar_tarea`, `mostrar_tareas`, `completar_tarea` y `guardar_tareas`.
3. Guarda el archivo y ejecútalo desde la consola de comandos para ver cómo se
gestionan las tareas, se completan y se guardan en un archivo de texto llamado tareas.txt`."""

def agregar_tarea(tareas, listas_de_tareas):
    listas_de_tareas.append(tareas)
    mensaje = "la tarea se ha agregado exitosamente."
    return mensaje

def mostrar_tarea(listas_de_tareas):
    if listas_de_tareas: 
        print("la lista de tareas es la siguiente:")
        for i, tarea in enumerate(listas_de_tareas, start=1):
            print(f"{i}. {tarea} ")
    else:
        print("el número de tareas no existe o no se encuentra en la lista")
    
def completar_tarea(numero_de_tareas, lista_de_tareas):
    if 1 <= numero_de_tareas <= len(lista_de_tareas):
        tareas_completadas=lista_de_tareas.pop(numero_de_tareas - 1)
        print(f"las siguientes tareas '{tareas_completadas}' estan completadas y finalizadas")
    else:
        print("numero de tareas no existe")

def guardar_tarea(nombre_del_archivo, lista_de_tareas):
    try:
        with open(nombre_del_archivo, "p") as archivo:
            for tarea in lista_de_tareas:
                archivo.write(tarea + '\n')
    except IOError:
        print("ocurrió un error al querer guardar las tareas en el archivo")

tareas=[]

while True:
    print("Bienvenido al Gestor de Tareas")
    print("Tarea 1: Agregar nueva tarea")
    print("Tarea 2: Mostar todas las tareas")
    print("Tarea 3: Completar tareas")
    print("Tarea 4: Guardar tareas en archivo.txt")
    print("Tarea 5: Salir de la aplicación")

    opcion=input("ingrese el número de la tarea que se desea ejecutar:")

    if opcion == '1':
        nueva_tarea = input("Ingrese la nueva tarea: ")
        agregar_tarea(nueva_tarea, tareas)
    elif opcion == '2':
        mostrar_tarea(tareas)
    elif opcion == '3':
        if tareas:
            mostrar_tarea(tareas)
            num_tarea_completada = int(input("Ingrese el número de la tarea completada: "))
            completar_tarea(num_tarea_completada, tareas)
        else:
            print("No hay tareas para completar.")
    elif opcion == '4':
        nombre_archivo = input("Ingrese el nombre del archivo para guardar las tareas: ")
        guardar_tarea(nombre_archivo, tareas)
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")


