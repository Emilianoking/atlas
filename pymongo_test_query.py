import tkinter as tk
from tkinter import ttk
import pandas as pd
from pymongo_get_database import get_database
from subprocess import call

def load_data():
    # Obtener la base de datos
    dbname = get_database()
    # Obtener la colección
    collection_name = dbname["user_1_items"]
    # Obtener los detalles de los ítems
    item_details = collection_name.find()
    
    # Convertir los datos a un DataFrame de Pandas
    df = pd.DataFrame(list(item_details))
    
    return df

def display_table():
    # Crear una ventana
    root = tk.Tk()
    root.title("Tabla de alimentos")
    
    # Crear un marco para la tabla
    frame = ttk.Frame(root)
    frame.pack(fill="both", expand=True)
    
    # Crear una tabla
    tree = ttk.Treeview(frame)
    tree["columns"] = tuple(load_data().columns)
    tree["show"] = "headings"
    
    # Configurar las columnas
    for column in tree["columns"]:
        tree.heading(column, text=column)
    
    # Insertar los datos en la tabla
    for index, row in load_data().iterrows():
        tree.insert("", "end", values=tuple(row))
    
    # Configurar el scroll para la tabla
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    
    tree.pack(fill="both", expand=True)
    
    # Crear botones para redireccionar a otros scripts
    update_button = ttk.Button(root, text="Actualizar", command=lambda: call(["python", "pymongo_test_actualizar.py"]))
    update_button.pack(side="left", padx=5, pady=5)
    
    delete_button = ttk.Button(root, text="Eliminar", command=lambda: call(["python", "pymongo_test_eliminar.py"]))
    delete_button.pack(side="left", padx=5, pady=5)
    
    insert_button = ttk.Button(root, text="Insertar", command=lambda: call(["python", "pymongo_test_insert.py"]))
    insert_button.pack(side="left", padx=5, pady=5)
    
    refresh_button = ttk.Button(root, text="Actualizar Tabla", command=display_table)
    refresh_button.pack(side="left", padx=5, pady=5)  # Agregar el botón para actualizar la tabla
    
    # Ejecutar la ventana
    root.mainloop()

if __name__ == "__main__":
    display_table()
