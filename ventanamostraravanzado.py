import tkinter as tk
from tkinter import ttk
import mysql.connector
import openpyxl

# Conectar a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="valentin",
    database="redoc",
    port=3307
)

# Crear un cursor para ejecutar consultas SQL
cursor = db.cursor()

# Función para imprimir los datos en un archivo Excel
def imprimir_a_excel():
    # Ejecutar una consulta para obtener los datos de la tabla
    cursor.execute("SELECT * FROM docente")
    
    # Obtener los datos de la consulta
    datos = cursor.fetchall()
    
    # Crear un libro de Excel
    libro = openpyxl.Workbook()
    hoja = libro.active
    
    # Obtener los nombres de las columnas
    cursor.execute("SHOW COLUMNS FROM docente")
    columnas = [i[0] for i in cursor.description]
    
    # Escribir los nombres de las columnas en la hoja
    hoja.append(columnas)
    
    # Escribir los datos en la hoja
    for fila in datos:
        hoja.append(fila)
    
    # Guardar el libro de Excel
    libro.save("datos_docente.xlsx")
    
    # Mostrar un mensaje de éxito
    mensaje_exito = tk.Toplevel(ventana)
    mensaje_exito.title("Éxito")
    mensaje_exito.geometry("200x100")
    mensaje_label = tk.Label(mensaje_exito, text="Datos exportados a Excel exitosamente.")
    mensaje_label.pack(pady=20)

# Crear la ventana Tkinter
ventana = tk.Tk()
ventana.title("Datos de la tabla docente")

# Crear un Treeview para mostrar los datos
tree = ttk.Treeview(ventana)
tree.pack(pady=20)

# Crear un botón para imprimir los datos a Excel
boton_imprimir = tk.Button(ventana, text="Imprimir a Excel", command=imprimir_a_excel)
boton_imprimir.pack(pady=10)

# Ejecutar una consulta para obtener los datos de la tabla
cursor.execute("SELECT * FROM docente")

# Obtener los nombres de las columnas
columnas = [i[0] for i in cursor.description]
tree = ttk.Treeview(ventana, columns=columnas, show='headings')
tree.pack()

# Configurar las columnas del Treeview
for col in columnas:
    tree.heading(col, text=col)
    tree.column(col, width=100)

# Insertar los datos en el Treeview
datos = cursor.fetchall()
for fila in datos:
    tree.insert("", "end", values=fila)

# Cerrar el cursor y la conexión a la base de datos
cursor.close()
db.close()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()