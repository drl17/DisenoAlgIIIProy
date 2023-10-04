#Este es el archivo ecundario donde realizaba todas las pruebas antes de pasar a la versión final

import tkinter
import random
from tkinter import messagebox

Interfaz=tkinter.Tk()
Interfaz.geometry("960x747")

Fondo_Interfaz=tkinter.PhotoImage(file="acertijo.png")
Fondo_Imagen=tkinter.Label(Interfaz,image=Fondo_Interfaz)
Fondo_Imagen.pack()

ganador = random.randint(1, 10)

def Obtener_random():
    numero_random=ganador
    #print(numero_random)

Boton_ganador=tkinter.Button(Interfaz, text="Obtener random", command=Obtener_random)
Boton_ganador.place(x=100,y=200)

Texto_Bienvenida=tkinter.Label(Interfaz, text="¡Hola, bienvenidos al juego del acertijo!")
Texto_Bienvenida.place(x=100, y=50)

Instruccion1=tkinter.Label(Interfaz, text="Ingresa un número [1 al 10] y comprueba si adivinas el número secreto.")
Instruccion1.place(x=100, y=100)

Caja_Texto=tkinter.Entry(Interfaz)
Caja_Texto.place(x=100, y=150)

def entero():
    a=int(Caja_Texto.get())
    print(a)

Boton_Obtener_CajaTexto=tkinter.Button(Interfaz, text="Obtener de caja texto", command=entero)
Boton_Obtener_CajaTexto.place(x=100,y=250)

numero=entero

"""def Ventana_Ganador():
    Ventana=tkinter.Toplevel()
    Ventana.geometry("300x300")
    Mensaje_Ganador=tkinter.Label(Ventana_Ganador, text="Adivinaste. Derrotaste al acertijo")
    Mensaje_Ganador.pack()
    Boton_CerrarVentanaGanador=tkinter.Button(Ventana_Ganador, text="Cerrar", command=Ventana_Ganador.destroy)
    Boton_CerrarVentanaGanador.pack()"""

Contador_Intentos=0

def comprobar():
    global Contador_Intentos
    Contador_Intentos += 1
    if Contador_Intentos <= 3:
        a = int(Caja_Texto.get())
        if a == ganador:
            messagebox.showinfo("¡Ganaste!", "Has derrotado al acertijo")
            Interfaz.destroy()
        elif a > ganador:
            messagebox.showwarning('Fallaste', f'Te quedan {3 - Contador_Intentos} intentos. Tu intento ha sido alto.')
        else:
            messagebox.showwarning('Fallaste', f'Te quedan {3 - Contador_Intentos} intentos. Tu intento ha sido bajo.')
    if Contador_Intentos == 3:
        messagebox.showerror("Game Over", "Has agotado todos tus intentos.")
        Interfaz.destroy()

"""Contador_Intentos=0

def comprobar():
    numero_random=ganador
    a=int(Caja_Texto.get())
    for Intentos in (1,4):
        if a == numero_random:
            #print(f"Adivinaste. El número secreto ganador era: {ganador}")
            messagebox.showinfo("Ganaste","Derrotaste al acertijo", command=Interfaz.destroy)
        elif a > numero_random:
            #print("vuelve a intentarlo")
            messagebox.showwarning(f'¡Tienes {(3-Contador_Intentos)} intentos!', "Fallaste, Tu intento ha sido alto")
        elif a < numero_random:
            #print("vuelve a intentarlo")
            messagebox.showwarning(f'¡Tienes {(3-Contador_Intentos)} intentos!', "Fallaste, tu intento es bajo")
        else:
            messagebox.showerror("Game Over", "Has perdido todos los intentos", command=Interfaz.destroy)
Contador_Intentos+=1"""


"""def comprobar():
    numero_random=ganador
    a=int(Caja_Texto.get())
    if numero_random == a:
        #print(f"Adivinaste. El número secreto ganador era: {ganador}")
        messagebox.showinfo("Ganaste","Derrotaste al acertijo")
    else:
        #print("vuelve a intentarlo")
        messagebox.showwarning("Atención", "Sigue intentando")"""

Boton_Comprobar=tkinter.Button(Interfaz, text="Comprobar", command=comprobar)
Boton_Comprobar.place(x=100, y=300)

Boton_Cerrar=tkinter.Button(Interfaz, text="Cerrar", command=Interfaz.destroy)
Boton_Cerrar.place(x=100, y=350)

Interfaz.mainloop()

#De acuerdo con el último digito de su documento de identidad le quedara asignado el ejercicio correspondiente
#Juego de Adivinanza: Crea un juego donde el programa selecciona un número aleatorio y el usuario tiene que adivinarlo.

"""import random

print(f"Ingresa números hasta que logres adivinar el número secreto. (Rango 0 - 5)")
print()

numero = int(input("Ingresa tu número: "))

ganador = random.randint(1, 10)

while True:
    if numero == ganador:
        print(f"Adivinaste. El número ganador era: {ganador}")
        break
    elif numero < ganador:
       print(f"Demasiado bajo.")
       numero = int(input("Ingresa tu número: "))
    elif numero > ganador:
        print(f"Demasiado alto.")
        numero = int(input("Ingresa tu número: "))"""