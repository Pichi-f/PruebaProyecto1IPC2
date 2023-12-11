import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename


class PantallaPrincipal:
    def __init__(self):
        principal = tk.Tk()
        principal.title("IPCMusic")
        principal.resizable(0, 0)
        principal.geometry("700x300")
        principal.config(bg="#F2E7E7")

        def cargarBiblioteca():
            try:
                global filename
                filename = askopenfilename(
                    title="Selecciona un Archivo XML",
                    filetypes=[("All files", "*.xml*")],
                )

                tree_xml = ET.parse(filename)
                root = tree_xml.getroot()

                for cancion in root.findall("cancion"):
                    nombre = cancion.get("nombre")
                    artista = (
                        cancion.find("artista").text
                        if cancion.find("artista") is not None
                        else ""
                    )
                    album = (
                        cancion.find("album").text
                        if cancion.find("album") is not None
                        else ""
                    )

                    # Utilizar una lista para los valores y asegurar que estén en el orden correcto
                    values_list = [nombre, artista, album]

                    # Agregar los datos a la tabla
                    tv.insert("", "end", text=nombre, values=values_list[1:])
            except Exception as e:
                mensaje_error = messagebox.showerror(
                    title="Mensaje de Alerta",
                    message=f"Error al cargar el archivo: {str(e)}",
                )
                return

        def salir():
            principal.destroy()

        submenu = tk.Menu(principal)

        # Primer submenú
        menuBiblioteca = tk.Menu(submenu, tearoff=0)
        menuBiblioteca.add_command(label="Cargar Biblioteca", command=cargarBiblioteca)
        menuBiblioteca.add_separator()
        menuBiblioteca.add_command(label="Salir", command=salir)
        submenu.add_cascade(label="Biblioteca", menu=menuBiblioteca)

        tv = ttk.Treeview(principal, columns=("col0", "col1"))
        tv.column("#0", width=200)
        tv.column("col0", width=200, anchor=CENTER)
        tv.column("col1", width=200, anchor=CENTER)

        tv.heading("#0", text="Canción", anchor=CENTER)
        tv.heading("col0", text="Artista", anchor=CENTER)
        tv.heading("col1", text="Álbum", anchor=CENTER)

        tv.pack()

        principal.config(menu=submenu)
        principal.mainloop()


if __name__ == "__main__":
    r = PantallaPrincipal()
