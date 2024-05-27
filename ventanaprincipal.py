import tkinter as tk
import mysql.connector

# Función para insertar datos en la base de datos
def insertar_datos():
    # Obtener los valores de los campos de texto
    cedula = entry_cedula.get()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    cargo = entry_cargo.get()
    
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
    
    # Preparar la consulta SQL para insertar datos
    sql = "INSERT INTO docente (cedula, nombre, apellido, cargo) VALUES (%s, %s, %s, %s)"
    values = (cedula, nombre, apellido, cargo)
    
    # Ejecutar la consulta SQL
    cursor.execute(sql, values)
    
    # Confirmar los cambios y cerrar la conexión
    db.commit()
    db.close()
    
    # Limpiar los campos de texto
    entry_cedula.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_cargo.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Insertar datos de docente")

# Crear los campos de texto
label_cedula = tk.Label(ventana, text="Cédula:")
label_cedula.pack()
entry_cedula = tk.Entry(ventana)
entry_cedula.pack()

label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_apellido = tk.Label(ventana, text="Apellido:")
label_apellido.pack()
entry_apellido = tk.Entry(ventana)
entry_apellido.pack()

label_cargo = tk.Label(ventana, text="Cargo:")
label_cargo.pack()
entry_cargo = tk.Entry(ventana)
entry_cargo.pack()

# Crear el botón de "Insertar"
boton_insertar = tk.Button(ventana, text="Insertar", command=insertar_datos)
boton_insertar.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()