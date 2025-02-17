import tkinter as tk
from tkinter import messagebox
import json

TAREAS_FILE = "tareas.json"

def cargar_tareas():
    try:
        with open(TAREAS_FILE, "r") as file:
            tareas_cargadas = json.load(file)
            return tareas_cargadas
    except (FileNotFoundError, json.JSONDecodeError):
        return []  

def guardar_tareas(tareas):
    try:
        with open(TAREAS_FILE, "w") as file:
            json.dump(tareas, file, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

def agregar_tarea():
    tarea = entry_tarea.get().strip()
    if tarea:
        tareas.append(tarea)
        guardar_tareas(tareas)
        actualizar_lista_tareas()
        entry_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

def ver_tareas():
    if not tareas:
        messagebox.showinfo("No hay tareas", "No hay tareas guardadas aún.")
    else:
        tareas_str = "\n".join([f"{i+1}. {tarea}" for i, tarea in enumerate(tareas)])
        messagebox.showinfo("Tareas", tareas_str)

def eliminar_tarea():
    if not tareas:
        messagebox.showinfo("No hay tareas", "No hay tareas para eliminar.")
        return
    try:
        indice = int(entry_tarea.get()) - 1  
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

def actualizar_lista_tareas():
    lista_tareas.delete(0, tk.END)  
    for tarea in tareas:
        lista_tareas.insert(tk.END, tarea)

root = tk.Tk()
root.title("Gestor de Tareas")

tareas = cargar_tareas()

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_tarea = tk.Entry(frame, width=40)
entry_tarea.grid(row=0, column=0, padx=5, pady=5)

boton_agregar = tk.Button(frame, text="Agregar tarea", command=agregar_tarea)
boton_agregar.grid(row=0, column=1, padx=5, pady=5)

lista_tareas = tk.Listbox(root, width=50, height=10)
lista_tareas.pack(padx=10, pady=10)

boton_ver = tk.Button(root, text="Ver tareas", command=ver_tareas)
boton_ver.pack(pady=5)

boton_eliminar = tk.Button(root, text="Eliminar tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

boton_salir = tk.Button(root, text="Salir", command=root.quit)
boton_salir.pack(pady=5)

actualizar_lista_tareas()

root.mainloop()