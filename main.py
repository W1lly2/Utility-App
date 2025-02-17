def mostrar_menu():
    print("\nGestor de Tareas")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

tareas = []
def agregar_tarea():
    tarea = input("Ingresa la tarea: ").strip()
    if tarea:
        tareas.append(tarea)
        print("Tarea agregada con éxito.")
    else: 
        print("Tarea vacia, no se puede agregar")
def ver_tareas():
    if not tareas:
        print("No hay tareas aún.")
    else:
        print("Tareas:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def eliminar_tareas():
    if not tareas:
        print("No hay tareas aún.")
    else:
        ver_tareas()
        indice = int(input("Ingresa el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada}' eliminada con éxito.")
        else:
            print("Número de tarea inválido.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            eliminar_tareas()
        elif opcion == "4":
            print("Saliendo del gestor de tareas...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()