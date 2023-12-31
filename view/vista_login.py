# View login
import sqlite3
import tkinter as tk
from tkinter import  Label, ttk, PhotoImage, messagebox as mb
from PIL import Image, ImageTk
from ttkthemes import ThemedTk

class Login:
    def __init__(self, ventana, modelo_stock):
        # Inicializa los atributos de la clase.
        self.ventana = ThemedTk(theme="arc")
        self.ventana.title("AlaNorte")
        self.ventana.geometry("400x600")
        self.modelo_stock = modelo_stock
        self.ventana.resizable(width=False, height=False)

        # Carga el logo de la aplicación.
        self.ruta_imagen_logo = "view/images/logo.png"
        self.logo = Image.open(self.ruta_imagen_logo)
        self.logo = self.logo.resize((250, 250))
        self.logo_imagen = ImageTk.PhotoImage(self.logo)
        self.logo_posicion = Label(self.ventana, image=self.logo_imagen).place(x=72, y=5)

        # Etiquetas de los campos de texto usuario.
        ttk.Label(self.ventana, text="Usuario:").place(x=130, y=270)
        self.entry_usuario = ttk.Entry(self.ventana)
        self.entry_usuario.place(x=130, y=290)
        # Etiquetas de los campos de texto contraseña.
        ttk.Label(self.ventana, text="Contraseña:").place(x=130, y=320)
        self.entry_contraseña = ttk.Entry(self.ventana,show="*")
        self.entry_contraseña.place(x=130, y=340)
        
        # Boton 'Ingresar'
        self.btn_ingresar = ttk.Button(self.ventana, text="Ingresar", command=self.verificar_ingreso)
        self.btn_ingresar.place(x=159, y=390)
    
    def verificar_ingreso(self): # Esta funcion dentro de esta vista no hace nada pero si se borra no funcionara la funcion echa en el controlador con el mismo nombre NO BORRREN LOCO
        pass