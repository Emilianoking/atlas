import tkinter as tk
from tkinter import ttk
from pymongo_get_database import get_database
from bson import ObjectId

def delete_data():
    # Obtener la base de datos
    dbname = get_database()
    # Obtener la colección
    collection_name = dbname["user_1_items"]
    
    # Obtener el ID del ítem a eliminar
    item_id = item_id_entry.get()
    item_id = ObjectId(item_id)  # Convertir a ObjectId
    
    # Eliminar el documento de la colección
    result = collection_name.delete_one({"_id": item_id})
    
    # Verificar si se eliminó correctamente
    if result.deleted_count == 1:
        result_label.config(text="Documento eliminado correctamente", foreground="green")
    else:
        result_label.config(text="No se encontró ningún documento con ese ID", foreground="red")

# Crear una ventana principal
root = tk.Tk()
root.title("Eliminación de Datos")

# Crear campo de entrada para el ID del ítem
item_id_label = ttk.Label(root, text="ID del ítem (_id):")
item_id_label.grid(row=0, column=0, padx=5, pady=5)
item_id_entry = ttk.Entry(root)
item_id_entry.grid(row=0, column=1, padx=5, pady=5)

# Botón para eliminar los datos
delete_button = ttk.Button(root, text="Eliminar", command=delete_data)
delete_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Etiqueta para mostrar el resultado de la eliminación
result_label = ttk.Label(root, text="", foreground="green")
result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Ejecutar la ventana principal
root.mainloop()
