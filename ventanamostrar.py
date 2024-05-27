import tkinter as tk
from tkinter import ttk
import mysql.connector

# Conectar a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="valentin",
    database="redoc",
    port="3307"
)

# Crear un cursor para ejecutar consultas SQL
cursor = db.cursor()

# Ejecutar una consulta para obtener los datos de la tabla
cursor.execute("SELECT * FROM docente")

# Obtener los nombres de las columnas
columnas = [i[0] for i in cursor.description]

# Obtener los datos de la consulta
datos = cursor.fetchall()

# Crear la ventana Tkinter
ventana = tk.Tk()
ventana.title("Datos de la tabla")

# Crear un Treeview para mostrar los datos
tree = ttk.Treeview(ventana, columns=columnas, show='headings')
tree.pack()

# Configurar las columnas del Treeview
for col in columnas:
    tree.heading(col, text=col)
    tree.column(col, width=100)

# Insertar los datos en el Treeview
for fila in datos:
    tree.insert("", "end", values=fila)

# Cerrar el cursor y la conexión a la base de datos
cursor.close()
db.close()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()