import pilasengine

pilas = pilasengine.iniciar()

mono = pilas.actores.Mono()

btn_agregar = pilas.actores.Actor(imagen = "Imagenes/Agregar.png")

btn_agregar.x = -200
btn_agregar.y = -150
mono.x = -200
mono.y = 150