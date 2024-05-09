import tkinter as tk
from tkinter import ttk
from pymongo_get_database import get_database
from dateutil import parser

def insert_data():
    # Obtener la base de datos
    dbname = get_database()
    # Obtener la colección
    collection_name = dbname["user_1_items"]
    
    # Obtener los datos ingresados por el usuario desde los campos de entrada
    item_name = item_name_entry.get()
    quantity = int(quantity_entry.get())
    ingredients = ingredients_entry.get()
    expiry_date_str = expiry_date_entry.get()
    
    # Convertir la fecha de vencimiento a un objeto datetime
    expiry = parser.parse(expiry_date_str)
    
    # Crear el documento del ítem
    item = {
        "item_name": item_name,
        "quantity": quantity,
        "ingredients": ingredients,
        "expiry_date": expiry
    }
    
    # Insertar el documento en la colección
    collection_name.insert_one(item)
    
    # Limpiar los campos de entrada después de la inserción
    item_name_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    ingredients_entry.delete(0, tk.END)
    expiry_date_entry.delete(0, tk.END)

# Crear una ventana principal
root = tk.Tk()
root.title("Ingreso de Items")

# Crear campos de entrada para los datos del ítem
item_name_label = ttk.Label(root, text="Nombre del ítem:")
item_name_label.grid(row=0, column=0, padx=5, pady=5)
item_name_entry = ttk.Entry(root)
item_name_entry.grid(row=0, column=1, padx=5, pady=5)

quantity_label = ttk.Label(root, text="Cantidad:")
quantity_label.grid(row=1, column=0, padx=5, pady=5)
quantity_entry = ttk.Entry(root)
quantity_entry.grid(row=1, column=1, padx=5, pady=5)

ingredients_label = ttk.Label(root, text="Ingredientes:")
ingredients_label.grid(row=2, column=0, padx=5, pady=5)
ingredients_entry = ttk.Entry(root)
ingredients_entry.grid(row=2, column=1, padx=5, pady=5)

expiry_date_label = ttk.Label(root, text="Fecha de vencimiento (YYYY-MM-DD):")
expiry_date_label.grid(row=3, column=0, padx=5, pady=5)
expiry_date_entry = ttk.Entry(root)
expiry_date_entry.grid(row=3, column=1, padx=5, pady=5)

# Botón para insertar los datos
insert_button = ttk.Button(root, text="Insertar", command=insert_data)
insert_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Ejecutar la ventana principal
root.mainloop()
