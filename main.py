import tkinter as tk
from tkinter import messagebox
import json

TAREAS_FILE = "tareas.json"

# Cargar tareas desde el archivo JSON
def cargar_tareas():
    try:
        with open(TAREAS_FILE, "r") as file:
            tareas_cargadas = json.load(file)
            return tareas_cargadas
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Si no se encuentra el archivo o está vacío, devolvemos una lista vacía

# Guardar tareas en el archivo JSON
def guardar_tareas(tareas):
    try:
        with open(TAREAS_FILE, "w") as file:
            json.dump(tareas, file, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

# Función para agregar tarea
def agregar_tarea():
    tarea = entry_tarea.get().strip()
    if tarea:
        tareas.append(tarea)
        guardar_tareas(tareas)
        actualizar_lista_tareas()
        entry_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

# Función para ver tareas
def ver_tareas():
    if not tareas:
        messagebox.showinfo("No hay tareas", "No hay tareas guardadas aún.")
    else:
        tareas_str = "\n".join([f"{i+1}. {tarea}" for i, tarea in enumerate(tareas)])
        messagebox.showinfo("Tareas", tareas_str)

# Función para eliminar tarea
def eliminar_tarea():
    try:
        indice = int(entry_tarea.get()) - 1  # Convertir el índice a entero
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            guardar_tareas(tareas)
            actualizar_lista_tareas()
            entry_tarea.delete(0, tk.END)
            messagebox.showinfo("Tarea eliminada", f"Tarea '{tarea_eliminada}' eliminada.")
        else:
            messagebox.showwarning("Error", "Índice inválido.")
    except ValueError:
        messagebox.showwarning("Error", "Por favor ingresa un número válido.")

# Función para actualizar la lista de tareas en la interfaz
def actualizar_lista_tareas():
    lista_tareas.delete(0, tk.END)  # Limpiar la lista
    for tarea in tareas:
        lista_tareas.insert(tk.END, tarea)

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")

# Cargar las tareas al iniciar
tareas = cargar_tareas()

# Frame para contener los widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Entrada de texto para las tareas
entry_tarea = tk.Entry(frame, width=40)
entry_tarea.grid(row=0, column=0, padx=5, pady=5)

# Botón para agregar tarea
boton_agregar = tk.Button(frame, text="Agregar tarea", command=agregar_tarea)
boton_agregar.grid(row=0, column=1, padx=5, pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(root, width=50, height=10)
lista_tareas.pack(padx=10, pady=10)

# Botón para ver tareas
boton_ver = tk.Button(root, text="Ver tareas", command=ver_tareas)
boton_ver.pack(pady=5)

# Botón para eliminar tarea
boton_eliminar = tk.Button(root, text="Eliminar tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Botón para salir
boton_salir = tk.Button(root, text="Salir", command=root.quit)
boton_salir.pack(pady=5)

# Actualizar la lista de tareas al iniciar
actualizar_lista_tareas()

# Ejecutar la interfaz gráfica
root.mainloop()