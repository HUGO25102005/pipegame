# Description: Juego de memorama de energias renovables
import pygame
import sys
import math
import time
import random
import os
#iniciamos pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

#VARIABLES ...........................................................................
altura_boton = 30   #para iniciar el juego (tamaño)
medida_cuadro = 260  #tamaño de la imagen
nombre_imagen_oculta = "imagenes/pregunta1.png" #imagen de la tarjeta volteada
imagen_volteada = pygame.image.load(nombre_imagen_oculta)
mostrar_piezas = 2 #para ocultar las tarjetas.
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h


class cuadro:
    def __init__(self, fuente_imagen): #mostrar las imagenes falso no se ve la imagen, verdadero se ve la imagen.
        self.mostrar = True
        self.descubierto = False
        #conparador de fuente de imagen 
        self.fuente_imagen = fuente_imagen

        self.imagen_real = pygame.image.load(fuente_imagen)

cuadros = [
    [cuadro('imagenes/presa.png'), cuadro('imagenes/presa.png'), cuadro('imagenes/foco11.png'), cuadro('imagenes/foco11.png')],
    [cuadro('imagenes/hidraulica1.png'), cuadro('imagenes/hidraulica1.png'), cuadro('imagenes/gota.png'), cuadro('imagenes/gota.png')],
    [cuadro('imagenes/im11.png'), cuadro('imagenes/im11.png'), cuadro('imagenes/gota2.png'), cuadro('imagenes/gota2.png')],
    [cuadro('imagenes/rueda.png'), cuadro('imagenes/rueda.png'), cuadro('imagenes/rayo.png'), cuadro('imagenes/rayo.png')],
]

#COLORES.............................................................................................
color_blanco = (255,255,255)
color_negro = (0,0,0,0)
color_gris = (206,206,206)
color_azul = (30,136,229)

#SONIDOS.............................................
sonido_fondo = pygame.mixer.Sound('musica/musica_fondo.mp3') #falta agreagr sonidos
sonido_exito = pygame.mixer.Sound('musica/sonido_exito.mp3')
sonido_clic = pygame.mixer.Sound('musica/clic.mp3')
sonido_voltear = pygame.mixer.Sound('musica/hoja.mp3')
sonido_fracaso = pygame.mixer.Sound('musica/falla.mp3')

#TAMAÑO DE PANTALLA ..............................................
anchura_pantalla = len(cuadros[0]) * medida_cuadro
anchura_boton = SCREEN_WIDTH
altura_boton = SCREEN_HEIGHT // 20
#FUENTE DEL BOTON.................................................
tamanio_fuente = 20
fuente = pygame.font.SysFont("Arial", tamanio_fuente)
xFuente = int((anchura_boton/2.2)-(tamanio_fuente/2))
yFuente = int((SCREEN_HEIGHT - altura_boton/2))

#BOTON...............................................................
boton = pygame.Rect(0, SCREEN_HEIGHT - altura_boton, anchura_boton, altura_boton)

#OCULTAR LAS TARJETAS.................................................

puede_jugar = True #saber si ocultar piezas o no
juego_iniciado = False #saber si el juego esta iniciado
segundos_mostrar_pieza = 2 #tiempo para ocultar las piezas
x1 = None
y1 = None
x2 = None
y2 = None
ultimos_segundos = -1
#ALMACEN DE CORDENADAS...............................................

#FUNCIONES UTILES...................................................


#ocultar las cartas

def ocultar_todas_las_cartas():
    for fila in cuadros:
        for cuadro in fila:
            cuadro.mostrar = False
            cuadro.descubierto = False

def aleatorizar_cuadros():
    cantidad_filas = len(cuadros)
    cantidad_columnas = len(cuadros[0])
    for y in range(cantidad_filas):
        for x in  range(cantidad_columnas):
            x_aleatorio = random.randint(0, cantidad_columnas - 1)
            y_aleatorio = random.randint(0, cantidad_filas - 1)
            cuadro_temporal = cuadros[y][x]
            cuadros[y][x] = cuadros[y_aleatorio][x_aleatorio]
            cuadros[y_aleatorio][x_aleatorio] = cuadro_temporal

def comprobar_si_gana():
    if gana():
        pygame.mixer.Sound.play(sonido_exito)
        reiniciar_juego()

def gana():
    for fila in cuadros:
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

#INICIA PANTALLA.......................................................
# creamos la pantalla
os.environ['SDL_VIDEO_CENTERED'] = '1'
pantalla_juego = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Memorama de las energias renovables')
pygame.mixer.Sound.play(sonido_fondo, -1)  
while True:
    for event in pygame.event.get():#detenta el click del mouse
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and puede_jugar:   
            xAbsoluto, yAbsoluto = event.pos
            if boton.collidepoint(event.pos):
                if not juego_iniciado:
                    iniciar_juego()
            else:
                if not juego_iniciado:
                    continue
                x = math.floor((xAbsoluto - start_x) / medida_cuadro)
                y = math.floor((yAbsoluto - start_y) / medida_cuadro)
                cuadro = cuadros[y][x]
                if cuadro.mostrar or cuadro.descubierto:
                    continue

                if x1 is None and y1 is None:
                    x1 = x
                    y1 = y    
                    cuadros[y1][x1].mostrar = True
                    pygame.mixer.Sound.play(sonido_voltear)   
                else:
                    x2 = x
                    y2 = y
                    cuadros[y2][x2].mostrar = True
                    cuadro1 = cuadros[y1][x1]
                    cuadro2 = cuadros[y2][x2]
                    if cuadro1.fuente_imagen == cuadro2.fuente_imagen:
                        cuadros[y1][x1].descubierto = True
                        cuadros[y2][x2].descubierto = True
                        x1 = None
                        y1 = None
                        x2 = None
                        y2 = None
                        pygame.mixer.Sound.play(sonido_clic)
                    else:
                        pygame.mixer.Sound.play(sonido_fracaso)
                        ultimos_segundos = int(time.time())

                        puede_jugar = False # Si ya pasaron x segundos, ocultamos las piezas
                comprobar_si_gana()
            
    ahora = int(time.time())
    if ultimos_segundos != -1 and (ahora - ultimos_segundos) >= segundos_mostrar_pieza:
        cuadros[y1][x1].mostrar = False
        cuadros[y2][x2].mostrar = False
        x1 = None
        y1 = None
        x2 = None
        y2 = None
        ultimos_segundos = -1
        puede_jugar = True
    pantalla_juego.fill(color_blanco)

    start_x = (SCREEN_WIDTH - len(cuadros[0]) * medida_cuadro) // 2
    start_y = (SCREEN_HEIGHT - len(cuadros) * medida_cuadro) // 2

    x = start_x
    y = start_y

    for fila in cuadros:
        x = start_x
        for cuadro in fila:
            if cuadro.descubierto or cuadro.mostrar:
                pantalla_juego.blit(cuadro.imagen_real, (x, y))
            else:       
                pantalla_juego.blit(imagen_volteada, (x, y))
            x += medida_cuadro
        y += medida_cuadro

    if juego_iniciado:
        
        pygame.draw.rect(pantalla_juego, color_blanco, boton)
        pantalla_juego.blit(fuente.render('INICIAR JUEGO', True, color_gris), (xFuente, yFuente))
    else:
        pygame.draw.rect(pantalla_juego, color_azul, boton)
        pantalla_juego.blit(fuente.render('INICIAR JUEGO', True, color_blanco), (xFuente, yFuente))

    pygame.display.update()
