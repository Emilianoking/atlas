import tkinter as tk
from tkinter import ttk
from pymongo_get_database import get_database
from dateutil import parser
from bson import ObjectId

def update_data():
    # Obtener la base de datos
    dbname = get_database()
    # Obtener la colección
    collection_name = dbname["user_1_items"]
    
    # Obtener el ID del ítem a actualizar
    item_id = item_id_entry.get()
    item_id = ObjectId(item_id)  # Convertir a ObjectId
    
    # Obtener los nuevos datos ingresados por el usuario desde los campos de entrada
    new_item_name = new_item_name_entry.get()
    new_quantity = int(new_quantity_entry.get())
    new_ingredients = new_ingredients_entry.get()
    new_expiry_date_str = new_expiry_date_entry.get()
    
    # Convertir la fecha de vencimiento a un objeto datetime
    new_expiry = parser.parse(new_expiry_date_str)
    
    # Crear los nuevos datos del ítem
    new_data = {
        "item_name": new_item_name,
        "quantity": new_quantity,
        "ingredients": new_ingredients,
        "expiry_date": new_expiry
    }
    
    # Actualizar el documento en la colección
    collection_name.update_one({"_id": item_id}, {"$set": new_data})
    
    # Limpiar los campos de entrada después de la actualización
    item_id_entry.delete(0, tk.END)
    new_item_name_entry.delete(0, tk.END)
    new_quantity_entry.delete(0, tk.END)
    new_ingredients_entry.delete(0, tk.END)
    new_expiry_date_entry.delete(0, tk.END)

# Crear una ventana principal
root = tk.Tk()
root.title("Actualización de Datos")

# Crear campos de entrada para el ID del ítem y los nuevos datos
item_id_label = ttk.Label(root, text="ID del ítem (_id):")
item_id_label.grid(row=0, column=0, padx=5, pady=5)
item_id_entry = ttk.Entry(root)
item_id_entry.grid(row=0, column=1, padx=5, pady=5)

new_item_name_label = ttk.Label(root, text="Nuevo nombre:")
new_item_name_label.grid(row=1, column=0, padx=5, pady=5)
new_item_name_entry = ttk.Entry(root)
new_item_name_entry.grid(row=1, column=1, padx=5, pady=5)

new_quantity_label = ttk.Label(root, text="Nueva cantidad:")
new_quantity_label.grid(row=2, column=0, padx=5, pady=5)
new_quantity_entry = ttk.Entry(root)
new_quantity_entry.grid(row=2, column=1, padx=5, pady=5)

new_ingredients_label = ttk.Label(root, text="Nuevos ingredientes:")
new_ingredients_label.grid(row=3, column=0, padx=5, pady=5)
new_ingredients_entry = ttk.Entry(root)
new_ingredients_entry.grid(row=3, column=1, padx=5, pady=5)

new_expiry_date_label = ttk.Label(root, text="Nueva fecha de vencimiento (YYYY-MM-DD):")
new_expiry_date_label.grid(row=4, column=0, padx=5, pady=5)
new_expiry_date_entry = ttk.Entry(root)
new_expiry_date_entry.grid(row=4, column=1, padx=5, pady=5)

# Botón para actualizar los datos
update_button = ttk.Button(root, text="Actualizar", command=update_data)
update_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Ejecutar la ventana principal
root.mainloop()
