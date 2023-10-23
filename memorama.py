import pygame
import sys
import math
import time
import random
#iniciamos pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

#VARIABLES ...........................................................................
altura_boton = 30   #para iniciar el juego (tamaño)
medida_cuadro = 200  #tamaño de la imagen
nombre_imagen_volteada = "imagenes/pregunta.png" #imagen de la tarjeta volteada
imagen_volteada = pygame.image.load(nombre_imagen_volteada)
mostrar_piezas = 2 #para ocultar las tarjetas.


class cuadro:
    def __init__(self, fuente_imagen): #mostrar las imagenes falso no se ve la imagen, verdadero se ve la imagen.
        self.mostrar = True
        self.descubierto = False
        #conparador de fuente de imagen 
        self.fuente_imagen = fuente_imagen
        self.imagen_real = pygame.image.load(fuente_imagen)

acomodo = [
    [cuadro("imagenes/eolica.png"), cuadro("imagenes/eolica.png"), cuadro("imagenes/foco.png"), cuadro("imagenes/foco.png")]
    [cuadro("imagenes/hidraulica.png"), cuadro("imagenes/.hidraulica.png"), cuadro("imagenes/hoja.png"), cuadro("imagenes/hoja.png")]
    [cuadro("imagenes/im1.png"), cuadro("imagenes/im1.png"), cuadro("imagenes/im2.png"), cuadro("imagenes/im2.png")]
    [cuadro("imagenes/panel_solar.png"), cuadro("imagenes/panel_solar.png"), cuadro("imagenes/sol.png"), cuadro("imagenes/sol.png")]
]
#COLORES.............................................................................................
color_blanco = (255,255,255)
color_negro = (0,0,0,0)
color_gris = (206,206,206)
color_azul = (30,136,229)

#SONIDOS.............................................
sonido_fondo = pygame.mixer.sound() #falta agreagr sonidos
sonido_exito = pygame.mixer.sound()
sonido_clic = pygame.mixer.sound()
sonido_fondo = pygame.mixer.sound()
sonido_fondo = pygame.mixer.sound()

#TAMAÑO DE PANTALLA ..............................................
anchura_pantalla = len(acomodo[0]) * medida_cuadro
altura_pantalla = (len(acomodo * medida_cuadro) + altura_boton)
anchura_boton = anchura_pantalla
#FUENTE DEL BOTON.................................................
tamanio_fuente = 20
fuente = pygame.font.SysFont("Arial", tamanio_fuente)
xFuente = int((anchura_boton/2)-(tamanio_fuente)/2)
yFuente = int((altura_pantalla - altura_boton))

#BOTON...............................................................
boton = pygame.Rect(0,altura_pantalla-altura_boton,
                    anchura_boton, altura_pantalla)

#OCULTAR LAS TARJETAS.................................................
ultimos_segundos = None
puede_jugar = True #saber si ocultar piezas o no
juego_iniciado = False

#ALMACEN DE CORDENADAS...............................................
x1 = None
y1 = None

x2 = None
y2 = None

#FUNCIONES UTILES...................................................


#ocultar las cartas
def ocultar_todas_las_cartas():
    for fila in acomodo:
        for acomodo in fila:
            cuadro.mostrar = False
            cuadro.descubierto = False

def aleatorizar_cuadros():
    cantidad_filas = len(acomodo)
    cantidad_columnas = len(acomodo[0])
    for y in range(cantidad_filas):
        for x in  range(cantidad_columnas):
            x_aleatorio = random.randint(0, cantidad_columnas - 1)
            y_aleatorio = random.randint(0, cantidad_filas - 1)
            cuadro_temporal = acomodo[y][x]
            acomodo[y][x] = acomodo[y_aleatorio][x_aleatorio]
            acomodo[y_aleatorio][x_aleatorio] = cuadro_temporal

def comprobar_si_gana():
    if gana():
        pygame.mixer.Sound.play(sonido_exito)
        reiniciar_juego()

def gana():
    for fila in acomodo:
        for cuadro in fila:
            if not cuadro.descubierto:
                return False
    return True

def reiniciar_juego():
    global juego_iniciado
    juego_iniciado = False

def iniciar_juego():
    pygame.mixer.Sound.play(sonido_clic)
    global juego_iniciado

    for i in range(3):
        aleatorizar_cuadros()
        ocultar_todas_las_cartas()
        juego_iniciado = True

#INICIA PANTALLA......................................
                   