#Esta es la versión final del aplicativo

#Importamos las librerías para el diseño de aplicativos en web, para invocar datos aleatorios y las ventanas con mensajes
import tkinter
import random
from tkinter import messagebox

#Creamos la interfaz con sus respectivas dimensiones
Interfaz=tkinter.Tk("Proyecto_DiseñoAlgoritmosIII_Acertijo")
Interfaz.geometry("480x374")

#Agregamos una imagen de fondo para la interfaz
Fondo_Interfaz=tkinter.PhotoImage(file="acertijo.png")
Fondo_Imagen=tkinter.Label(Interfaz,image=Fondo_Interfaz)
Fondo_Imagen.pack()

#Obtenemos la primera variable como el dato random que elige la máquina
ganador = random.randint(1, 10)

#Agregamos un texto de bienvenida
Texto_Bienvenida=tkinter.Label(Interfaz, text="¡Hola, bienvenidos al juego del acertijo!")
Texto_Bienvenida.place(x=130, y=100)

#Agregamos un texto explicando el juego
Instruccion1=tkinter.Label(Interfaz, text="Ingresa un número [1 al 10] y comprueba si adivinas el número secreto")
Instruccion1.place(x=50, y=150)

#Creamos un cuadro de texto para que la interacción del usuario y donde ingresará el número que buscará adivinar
Caja_Texto=tkinter.Entry(Interfaz)
Caja_Texto.place(x=170, y=200)

#Definimos la función principal donde comparamos el número obtenido por la máquina y el número ingresado por el usuario
#Según los escenarios definimos unos resultados
def comprobar():
    numero_random=ganador
    a=int(Caja_Texto.get())
    if numero_random == a:
        messagebox.showinfo("Ganaste","Derrotaste al acertijo")
    else:
        messagebox.showwarning("Atención", "Sigue intentando")

#Creamos un botón para ejecutar la función principal y la asociamos
Boton_Comprobar=tkinter.Button(Interfaz, text="Comprobar", command=comprobar)
Boton_Comprobar.place(x=200, y=250)

#Creamos un botón para cerrar cuando haya finalizado el juego
Boton_Cerrar=tkinter.Button(Interfaz, text="Cerrar", command=Interfaz.destroy)
Boton_Cerrar.place(x=215, y=300)

Interfaz.mainloop()
