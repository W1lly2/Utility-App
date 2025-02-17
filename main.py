import json

TAREAS_FILE = "tareas.json"

def cargar_tareas():
    try:
        with open(TAREAS_FILE, "r") as file:
            tareas_cargadas = json.load(file)
            print("Tareas cargadas desde archivo:", tareas_cargadas)  
            return tareas_cargadas
    except (FileNotFoundError, json.JSONDecodeError):
        print("No se encontró el archivo o el archivo está vacío.") 
        return []  

def guardar_tareas(tareas):
    try:
        with open(TAREAS_FILE, "w") as file:
            json.dump(tareas, file, indent=4)  
            print(f"Tareas guardadas: {tareas}")  
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")  

tareas = cargar_tareas()

def mostrar_menu():
    print("\nGestor de Tareas 1.0.0")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

def agregar_tarea():
    tarea = input("Ingresa la tarea: ").strip()
    if tarea:
        tareas.append(tarea)
        guardar_tareas(tareas)  
        print("Tarea agregada con éxito.")
    else:
        print("Tarea vacía, no se puede agregar.")

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
        try:
            indice = int(input("Ingresa el número de la tarea a eliminar: ")) - 1
            if 0 <= indice < len(tareas):
                tarea_eliminada = tareas.pop(indice)
                guardar_tareas(tareas)  
                print(f"Tarea '{tarea_eliminada}' eliminada con éxito.")
            else:
                print("Número de tarea inválido.")
        except ValueError:
            print("Por favor ingresa un número válido.")

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