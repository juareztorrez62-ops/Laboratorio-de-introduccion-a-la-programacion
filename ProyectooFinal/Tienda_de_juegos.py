import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

#Listas principales para el almacenamiento del inventario y ventas#
inventario = []
ventas = []

#Aqui estan las funciones para agregar los productos, actualizar las tablas, buscarlos y registrar las ventas de estos#
def agregar_producto():
    nombre = entry_nombre.get()
    precio = entry_precio.get()
    cantidad = entry_cantidad.get()

    if nombre == "" or precio == "" or cantidad == "":
        messagebox.showwarning("Error", "Completa todos los campos")
        return

    try:
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }

        inventario.append(producto)

        actualizar_tabla_inventario()

        messagebox.showinfo("Éxito", "Producto agregado correctamente")

        limpiar_campos()

    except ValueError:
        messagebox.showerror("Error", "Precio o cantidad inválidos")


def actualizar_tabla_inventario():

    tabla_inventario.delete(*tabla_inventario.get_children())

    for producto in inventario:

        tabla_inventario.insert(
            "",
            tk.END,
            values=(
                producto["nombre"],
                f"${producto['precio']}",
                producto["cantidad"]
            )
        )


def actualizar_tabla_ventas():

    tabla_ventas.delete(*tabla_ventas.get_children())

    for venta in ventas:

        tabla_ventas.insert(
            "",
            tk.END,
            values=(
                venta["nombre"],
                f"${venta['precio']}",
                venta["fecha"]
            )
        )


def buscar_producto():

    nombre = entry_buscar.get()

    for producto in inventario:

        if producto["nombre"].lower() == nombre.lower():

            messagebox.showinfo(
                "Producto encontrado",
                f"Nombre: {producto['nombre']}\n"
                f"Precio: ${producto['precio']}\n"
                f"Cantidad: {producto['cantidad']}"
            )

            return

    messagebox.showwarning("Error", "Producto no encontrado")


def registrar_venta():

    nombre = entry_buscar.get()

    for producto in inventario:

        if producto["nombre"].lower() == nombre.lower():

            if producto["cantidad"] > 0:

                producto["cantidad"] -= 1

                venta = {
                    "nombre": producto["nombre"],
                    "precio": producto["precio"],
                    "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                }

                ventas.append(venta)

                actualizar_tabla_inventario()
                actualizar_tabla_ventas()

                messagebox.showinfo("Venta", "Venta registrada correctamente")

            else:
                messagebox.showwarning("Error", "Producto agotado")

            return

    messagebox.showwarning("Error", "Producto no encontrado")


def eliminar_producto():

    nombre = entry_buscar.get()

    for producto in inventario:

        if producto["nombre"].lower() == nombre.lower():

            inventario.remove(producto)

            actualizar_tabla_inventario()

            messagebox.showinfo("Éxito", "Producto eliminado")

            return

    messagebox.showwarning("Error", "Producto no encontrado")


def limpiar_campos():

    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)

ventana = tk.Tk()

ventana.title("Tienda de Videojuegos")
ventana.geometry("900x650")
ventana.config(bg="white")

titulo = tk.Label(
    ventana,
    text="TIENDA DE VIDEOJUEGOS",
    font=("Arial", 20, "bold"),
    bg="white",
    fg="black"
)

titulo.pack(pady=10)

frame_form = tk.Frame(ventana, bg="white")
frame_form.pack(pady=10)

#se usa para añadir el nombre del producto#
tk.Label(
    frame_form,
    text="Nombre:",
    bg="white",
    fg="black"
).grid(row=0, column=0, padx=5, pady=5)

entry_nombre = tk.Entry(frame_form)
entry_nombre.grid(row=0, column=1)

#se utiliza para añadir el Precio del producto#
tk.Label(
    frame_form,
    text="Precio:",
    bg="white",
    fg="black"
).grid(row=1, column=0, padx=5, pady=5)

entry_precio = tk.Entry(frame_form)
entry_precio.grid(row=1, column=1)

#Cantidad de unidades del juego en stock#
tk.Label(
    frame_form,
    text="Cantidad:",
    bg="white",
    fg="black"
).grid(row=2, column=0, padx=5, pady=5)

entry_cantidad = tk.Entry(frame_form)
entry_cantidad.grid(row=2, column=1)

#Aqui se encuentra la opcion para agregar un juego al catalogo#
btn_agregar = tk.Button(
    frame_form,
    text="Agregar Producto",
    command=agregar_producto,
    bg="#4CAF50",
    fg="white",
    width=20
)

btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

frame_busqueda = tk.Frame(ventana, bg="white")
frame_busqueda.pack(pady=10)

tk.Label(
    frame_busqueda,
    text="Producto:",
    bg="white",
    fg="black"
).grid(row=0, column=0, padx=5)

entry_buscar = tk.Entry(frame_busqueda, width=30)
entry_buscar.grid(row=0, column=1, padx=5)

#La opcion para buscar un juego si el catalogo llega a ser muy extenso#
tk.Button(
    frame_busqueda,
    text="Buscar",
    command=buscar_producto,
    bg="#2196F3",
    fg="white"
).grid(row=0, column=2, padx=5)

#El boton para registrar la venta#
tk.Button(
    frame_busqueda,
    text="Registrar Venta",
    command=registrar_venta,
    bg="#FF9800",
    fg="white"
).grid(row=0, column=3, padx=5)

#El eliminar tiene la funcio de borrar algun producto si es nbecesario#
tk.Button(
    frame_busqueda,
    text="Eliminar",
    command=eliminar_producto,
    bg="#F44336",
    fg="white"
).grid(row=0, column=4, padx=5)

#Esta es la Tabla del inventario#
label_inventario = tk.Label(
    ventana,
    text="INVENTARIO",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="black"
)

label_inventario.pack(pady=5)

tabla_inventario = ttk.Treeview(
    ventana,
    columns=("Nombre", "Precio", "Cantidad"),
    show="headings",
    height=8
)

tabla_inventario.heading("Nombre", text="Nombre")
tabla_inventario.heading("Precio", text="Precio")
tabla_inventario.heading("Cantidad", text="Cantidad")

tabla_inventario.pack(fill="x", padx=20)

#Aqui esta la tabla de las ventas#
label_ventas = tk.Label(
    ventana,
    text="REGISTRO DE VENTAS",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="black"
)

label_ventas.pack(pady=10)

tabla_ventas = ttk.Treeview(
    ventana,
    columns=("Nombre", "Precio", "Fecha"),
    show="headings",
    height=8
)

tabla_ventas.heading("Nombre", text="Videojuego")
tabla_ventas.heading("Precio", text="Precio")
tabla_ventas.heading("Fecha", text="Fecha y Hora")

tabla_ventas.pack(fill="x", padx=20)
ventana.mainloop()