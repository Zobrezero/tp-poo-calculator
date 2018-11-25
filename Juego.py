import sys
sys.path.insert(0, "..")
import pilasengine
import random

pilas = pilasengine.iniciar()

b = 0
a = []
a.append(pilas.actores.Mono())
#btn_agregar = pilas.interfaz.Boton(imagen = "Imagenes/Agregar.png")
btn_agregar = pilas.interfaz.Boton()

btn_agregar.x = -200
btn_agregar.y = -150
a[-1].x = -200
a[-1].y = 150

def click_de_mouse1():
   a.append(pilas.actores.Mono())
   a[-1].x = a[-2].x + 30
   pilas.tareas.agregar(5, click_de_mouse1) 

#btn_agregar.conectar.click_de_mouse(click_de_mouse1)
#pilas.eventos.click_de_mouse.conectar(click_de_mouse1)
btn_agregar.conectar(click_de_mouse1)


