def mostrar_menu():
    print("\nGestor de Tareas")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            print("Función para agregar tarea aún no implementada.")
        elif opcion == "2":
            print("Función para ver tareas aún no implementada.")
        elif opcion == "3":
            print("Saliendo del gestor de tareas...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()