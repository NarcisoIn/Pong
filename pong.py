import pygame as pg
import random
import sys
import os

# Función para rutas correctas en PyInstaller
def ruta_recurso(nombre):
    if hasattr(sys, "_MEIPASS"):
        # Para cuando se ejecuta como .exe
        return os.path.join(sys._MEIPASS, nombre)
    else:
        ruta = os.path.join(r"C:\Users\guzma\OneDrive\Documentos\Cursos\Python Aplicado 5 Proyectos Reales de Principio a Fin\Proyecto 2 PONG", nombre)

    if not os.path.exists(ruta):
        print(f"¡Archivo no encontrado!: {ruta}")
    return ruta


pg.init()
pg.mixer.init()
# Ventana
ANCHO_VENTANA = 900
ALTO_VENTANA = 600

# Configura ancho y allto de la pantalla
pantalla = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

# cambiar icono y titulo de la ventana
pg.display.set_caption("Pong")
icono = pg.image.load(ruta_recurso("pong.png"))
pg.display.set_icon(icono)

# Variables sonido
golpePaleta = pg.mixer.Sound(ruta_recurso("golpe_paleta.mp3"))
golpePared = pg.mixer.Sound(ruta_recurso("golpe_pared.mp3"))
punto = pg.mixer.Sound(ruta_recurso("punto2.mp3"))

# Volumen de los sonidos
punto.set_volume(0.5)
golpePared.set_volume(0.6)
golpePaleta.set_volume(0.5)

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
COLORFONDO = (150, 200, 170)
AZUL = (70, 130, 180)
ROJO = (200, 70, 90)


# Coordenadas y dimensiones
altoPaleta = 100
anchoPaleta = 30
# Paleta 1: Jugador 1
x_paleta1 = 50
y_paleta1 = 250  # centrada aproximadamente
# Paleta 2: Jugador 2
x_paleta2 = ANCHO_VENTANA - 50 - anchoPaleta
y_paleta2 = 250  # centrada aproximadamente
velocidad_paleta = 5

# Coordenadas y dimensiones de la Pelota
anchoPelota = 10
altoPelota = 10
x_pelota = 450  # centro de la pantalla
y_pelota = 300
velocidad_x = 4
velocidad_y = 4

# Marcador
puntosPaleta1 = 0
puntosPaleta2 = 0
gana = None

# Fuente personalizada
calibri_30 = pg.font.SysFont("Calibri", 30, bold=True, italic=True)
calibri_35 = pg.font.SysFont("Calibri", 35, bold=True, italic=True)
calibri_120 = pg.font.SysFont("Calibri", 120, bold=True, italic=True)

# Creacion de los objetos
paleta1 = pg.Rect(x_paleta1, y_paleta1, anchoPaleta, altoPaleta,)
paleta2 = pg.Rect(x_paleta2, y_paleta2, anchoPaleta, altoPaleta)
pelota = pg.Rect(x_pelota, y_pelota, anchoPelota, altoPelota)

# Funcion que determina que Jugador Ganó
def ganador():
    if puntosPaleta1 >= gana:
        return "Jugador 1"
    elif puntosPaleta2 >= gana:
        return "Jugador 2"
    else:
        return None

# Funcion que muestra el Ganador
def mostGanador(ganador):
    # loop exclusivo para pantalla ganador 
    relojGanador = pg.time.Clock()
    ejecutandoGanador = True

    # Texto Ganador
    textoGanador = calibri_35.render(f"¡Gana {ganador}!", True, BLANCO)
    # Texto Pregunta si quiere volver a jugar
    preguntaJugar = calibri_35.render("¿Quieres volver a jugar?", True, BLANCO)
    # Tecla a presionar para volver a jugar
    teclaVolverJugar = calibri_35.render("SÍ (s)", True, BLANCO)
    # Tecla para cerrar el juego
    teclaCerrar = calibri_35.render("NO (n)", True, BLANCO)

    while ejecutandoGanador:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                ejecutandoGanador = False
            
            if evento.type == pg.KEYDOWN:
                # Evento para determinar si vuelve a jugar o se cierra el juego
                if evento.key == pg.K_s:
                    return True
                elif evento.key == pg.K_n:
                    return False


        # Rellena el fondo
        pantalla.fill(NEGRO)
        # Muestra mensaje ganador centrado
        pantalla.blit(textoGanador, (ANCHO_VENTANA//2 - textoGanador.get_width()//2, (ALTO_VENTANA//2 - textoGanador.get_height()//2) - 130))
        pantalla.blit(preguntaJugar, ((ANCHO_VENTANA//2 - preguntaJugar.get_width()//2), (ALTO_VENTANA//2 - preguntaJugar.get_height()//2) - 60))
        pantalla.blit(teclaVolverJugar, ((ANCHO_VENTANA//2 - teclaVolverJugar.get_width()//2) - 90, (ALTO_VENTANA//2 - preguntaJugar.get_height()//2) - 10))
        pantalla.blit(teclaCerrar, ((ANCHO_VENTANA//2 - teclaCerrar.get_width()//2) + 85, (ALTO_VENTANA//2 - preguntaJugar.get_height()//2) - 10))

        pg.display.flip()
        relojGanador.tick(10)


def dibujarObjeto():
    # Cambia Color de Fondo
    pantalla.fill(COLORFONDO)
    # Dibuja los objetos
    pg.draw.rect(pantalla, AZUL, paleta1)  # Rectangulo Izquier
    pg.draw.rect(pantalla, ROJO, paleta2)  # Rectangulo Derecho
    pg.draw.rect(pantalla, BLANCO, pelota)  # Pelota

    textoJugador1 = calibri_35.render(f"Puntos: {puntosPaleta1}", True, AZUL)
    textoJugador2 = calibri_35.render(f"Puntos: {puntosPaleta2}", True, ROJO)

    pantalla.blit(textoJugador1, (130, 20))
    pantalla.blit(textoJugador2, (620, 20))

    pg.display.flip()  # Actualiza la pantalla

# Resetea los valores
def resetPocision(direccion):
    global y_paleta1, y_paleta2, velocidad_x, velocidad_y
    y_paleta1 = 250
    y_paleta2 = 250  # centrada aproximadamente
    # Paleta 2: Jugador 2
    paleta1.y = y_paleta1
    paleta2.y = y_paleta2
    # Después de anotar un punto
    pelota.x = x_pelota
    pelota.y = y_pelota
    velocidad_x = 4 * direccion
    velocidad_y = random.choice([-4, 4])

# Variables de inicializacion
ejecutando = True
reloj = pg.time.Clock()

# Funcion Menu Principal
def menuPrincipal():
    relojMenu = pg.time.Clock()
    ejecutandoMenu = True
    global gana

    titulo = calibri_120.render("PONG", True, BLANCO)
    iconoEscalado = pg.transform.scale(icono, (titulo.get_height(), titulo.get_height()))
    subtitulo = calibri_35.render("Selecciona la meta de puntos:", True, BLANCO)
    opc1 = calibri_30.render("5 puntos (1)", True, AZUL)
    opc2 = calibri_30.render("10 puntos (2)", True, AZUL)
    opc3 = calibri_30.render("15 puntos (3)", True, AZUL)

    # Seleccion de usuario
    seleccion = None

    while ejecutandoMenu:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_1:
                    return 5
                elif evento.key == pg.K_2:
                    return 10
                elif evento.key == pg.K_3:
                    return 15

            pantalla.fill(NEGRO)
            pantalla.blit(titulo, (ANCHO_VENTANA//2 - (titulo.get_width()//2) - 45, 150))
            pantalla.blit(iconoEscalado, (ALTO_VENTANA//2 - (titulo.get_width()//2) + 405, 150))
            pantalla.blit(subtitulo, (ANCHO_VENTANA//2 - subtitulo.get_width()//2, 280))
            pantalla.blit(opc1, (ANCHO_VENTANA//2 - opc1.get_width()//2, 340))
            pantalla.blit(opc2, (ANCHO_VENTANA//2 - opc2.get_width()//2, 380))
            pantalla.blit(opc3, (ANCHO_VENTANA//2 - opc3.get_width()//2, 420))

            pg.display.flip()
            relojMenu.tick(60)
    return seleccion


# Llamamos al menu principal antes que el Loop del juego
estado = "MENU"

quiengano = None

# Loop Juego
while ejecutando:

    # Verificar cierre de ventana
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            ejecutando = False

    if estado == "MENU":
        gana = menuPrincipal()
        estado = "JUGANDO"

    elif estado == "JUGANDO":

        # Determinamos que tecla esta presionada
        tecla = pg.key.get_pressed()

        # Actualiza la pocision de las paletas
        paleta1.y = y_paleta1
        paleta2.y = y_paleta2

        # Paleta 1
        if tecla[pg.K_w] and y_paleta1 > 0:
            y_paleta1 -= velocidad_paleta
        if tecla[pg.K_s] and y_paleta1 + altoPaleta < ALTO_VENTANA:
            y_paleta1 += velocidad_paleta

        # Paleta 2
        if tecla[pg.K_UP] and y_paleta2 > 0:
            y_paleta2 -= velocidad_paleta
        if tecla[pg.K_DOWN] and y_paleta2 + altoPaleta < ALTO_VENTANA:
            y_paleta2 += velocidad_paleta

        # Actualizamos el movimiento de la pelota
        pelota.x += velocidad_x
        pelota.y += velocidad_y

        # Colision Pelota con Paletas
        # Paleta 1
        if pelota.colliderect(paleta1) and velocidad_x < 0:
            velocidad_x *= -1
            pelota.left = paleta1.right  # Evita que la pelota se quede pegada
            golpePaleta.play()
        # Paleta 2
        if pelota.colliderect(paleta2) and velocidad_x > 0:
            velocidad_x *= -1
            pelota.right = paleta2.left  # Evita que la paleta se quede pegada
            golpePaleta.play()

        # Colision Pelota con bordes Superior e Inferior
        if pelota.top <= 0 or pelota.bottom >= ALTO_VENTANA:
            velocidad_y *= -1
            golpePared.play()

        # Colisiones Pelota con bordes Laterales
        if pelota.left <= 0:
            resetPocision(1)
            punto.play()
            puntosPaleta2 += 1
        elif pelota.right >= ANCHO_VENTANA:
            resetPocision(-1)
            punto.play()
            puntosPaleta1 += 1

        quiengano = ganador()
        if quiengano:
            estado = "GANADOR"

    elif estado == "GANADOR":
        volverJugar = mostGanador(quiengano)
        if volverJugar:
            # Resetear puntos y posiciones
            puntosPaleta1 = 0
            puntosPaleta2 = 0
            resetPocision(random.choice([-1, 1]))
            estado = "JUGANDO"
        else:
            ejecutando = False

    if estado == "JUGANDO":
        dibujarObjeto()

    reloj.tick(60)

pg.quit()
sys.exit()