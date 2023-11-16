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
# Cargar una imagen de fondo
BG = pygame.image.load("assets/background_water.png")
BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
#Inicializar el cronometro
tiempo_inicial = time.time()
duracion_temporizador = 90
tiempo_final = tiempo_inicial + duracion_temporizador
font = pygame.font.Font(None, 120)

three_stars = False
two_stars = False
one_star = False


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
    tiempo_restante = int(tiempo_final - time.time())

    for event in pygame.event.get():  # detenta el click del mouse
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and puede_jugar:
            xAbsoluto, yAbsoluto = event.pos
            if boton.collidepoint(event.pos):
                if not juego_iniciado:
                    iniciar_juego()
                    tiempo_final = time.time() + duracion_temporizador  # Set the timer only when the game starts
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
                        puede_jugar = False  # Si ya pasaron x segundos, ocultamos las piezas
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

    pantalla_juego.blit(BG, (0, 0))

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
        if tiempo_restante > 0 and not gana():
            # Actualiza y dibuja el texto del temporizador
            timer_text = font.render("Time: {}".format(tiempo_restante), True, (255, 0, 0))
            text_rect = timer_text.get_rect(topright=(SCREEN_WIDTH - 10, 10))
            pantalla_juego.blit(timer_text, text_rect)
    else:
        pygame.draw.rect(pantalla_juego, color_azul, boton)
        pantalla_juego.blit(fuente.render('INICIAR JUEGO', True, color_blanco), (xFuente, yFuente))

    # Draw stars outside the event loop
    if gana():
        # Determine stars based on time remaining
        if tiempo_restante >= 60:
            three_stars = True
        elif 30 <= tiempo_restante < 60:
            two_stars = True
        elif tiempo_restante < 30:
            one_star = True

    # Draw stars and victory message outside the event loop
    if gana():

        BG2 = pygame.image.load("assets/background_2.png")
        BG2 = pygame.transform.scale(BG2, (SCREEN_WIDTH, SCREEN_HEIGHT))
        pantalla_juego.blit(BG2, (0, 0))

        # Mostrar un mensaje de victoria
        font = pygame.font.Font(None, 120)
        text = font.render("You Won!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(pantalla_juego.get_width() // 2, pantalla_juego.get_height() // 5))
        pantalla_juego.blit(text, text_rect)

        # Dibujar estrella central
        frs_star_b = pygame.image.load("assets/starb.png")
        frs_star_b = pygame.transform.scale(frs_star_b, (200,200))
        frs_star_b_rect = frs_star_b.get_rect(center=(pantalla_juego.get_width() // 2, pantalla_juego.get_height() // 3))
        pantalla_juego.blit(frs_star_b, frs_star_b_rect)
    
        # Posicionar segunda estrella a la izquierda de la primera
        snd_star_b_rect = pygame.Rect(frs_star_b_rect.left - frs_star_b_rect.width, frs_star_b_rect.top + 20, 100, 40)
        snd_star_b = pygame.image.load("assets/starb.png")
        snd_star_b = pygame.transform.scale(snd_star_b, (200,200))
        pantalla_juego.blit(snd_star_b, snd_star_b_rect)

        # Posicionar tercera estrella a la derecha de la primera
        trd_star_b_rect = pygame.Rect(frs_star_b_rect.right - frs_star_b_rect.width + 200, frs_star_b_rect.top + 20, 100, 40)
        trd_star_b = pygame.image.load("assets/starb.png")
        trd_star_b = pygame.transform.scale(trd_star_b, (200,200))
        pantalla_juego.blit(trd_star_b, trd_star_b_rect)

        if three_stars:
            # Dibujar estrella central
            frs_star = pygame.image.load("assets/star.png")
            frs_star = pygame.transform.scale(frs_star, (200,200))
            frs_star_rect = frs_star.get_rect(center=(pantalla_juego.get_width() // 2, pantalla_juego.get_height() // 3))
            pantalla_juego.blit(frs_star, frs_star_rect)
        
            # Posicionar segunda estrella a la izquierda de la primera
            snd_star_rect = pygame.Rect(frs_star_rect.left - frs_star_rect.width, frs_star_rect.top + 20, 100, 40)
            snd_star = pygame.image.load("assets/star.png")
            snd_star = pygame.transform.scale(snd_star, (200,200))
            pantalla_juego.blit(snd_star, snd_star_rect)

            # Posicionar segunda estrella a la izquierda de la primera
            trd_star_rect = pygame.Rect(frs_star_rect.right - frs_star_rect.width + 200, frs_star_rect.top + 20, 100, 40)
            trd_star = pygame.image.load("assets/star.png")
            trd_star = pygame.transform.scale(trd_star, (200,200))
            pantalla_juego.blit(trd_star, trd_star_rect)

        if two_stars:
            # Dibujar estrella central
            frs_star = pygame.image.load("assets/star.png")
            frs_star = pygame.transform.scale(frs_star, (200,200))
            frs_star_rect = frs_star.get_rect(center=(pantalla_juego.get_width() // 2, pantalla_juego.get_height() // 3))
            pantalla_juego.blit(frs_star, frs_star_rect)
        
            # Posicionar segunda estrella a la izquierda de la primera
            snd_star_rect = pygame.Rect(frs_star_rect.left - frs_star_rect.width, frs_star_rect.top + 20, 100, 40)
            snd_star = pygame.image.load("assets/star.png")
            snd_star = pygame.transform.scale(snd_star, (200,200))
            pantalla_juego.blit(snd_star, snd_star_rect)

        if one_star:
            # Dibujar estrella central
            frs_star = pygame.image.load("assets/star.png")
            frs_star = pygame.transform.scale(frs_star, (200,200))
            frs_star_rect = frs_star.get_rect(center=(pantalla_juego.get_width() // 2, pantalla_juego.get_height() // 3))
            pantalla_juego.blit(frs_star, frs_star_rect)

        # Dibujar un botón de retorno
        back_button_text = font.render("Back", True, (255, 255, 255))
        back_button_text_rect = back_button_text.get_rect(center=(pantalla_juego.get_width() // 2, text_rect.bottom + 450))
        back_button_rect = back_button_text_rect.inflate(10, 10)  
        pantalla_juego.blit(back_button_text, back_button_text_rect)

        # Manejar eventos de clic en el botón de retorno
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and back_button_rect.collidepoint(event.pos):
                pygame.mixer.stop()
                exec(open("./main.py", "r").read(), globals()) 
                pygame.display.update()
                pygame.quit()
                sys.exit()

    if not gana() and tiempo_restante <=0:
        BG2 = pygame.image.load("assets/background_2.png")
        BG2 = pygame.transform.scale(BG2, (SCREEN_WIDTH, SCREEN_HEIGHT))
        pantalla_juego.blit(BG2, (0, 0))

        # Mostrar "Game Over"
        font = pygame.font.Font(None, 120)
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        game_over_text_rect = game_over_text.get_rect(center=(pantalla_juego.get_width() // 2, pantalla_juego.get_height() // 5))
        pantalla_juego.blit(game_over_text, game_over_text_rect)

        # Dibujar estrella central
        frs_star_b = pygame.image.load("assets/starb.png")
        frs_star_b = pygame.transform.scale(frs_star_b, (200,200))
        frs_star_b_rect = frs_star_b.get_rect(center=(pantalla_juego.get_width() // 2, pantalla_juego.get_height() // 3))
        pantalla_juego.blit(frs_star_b, frs_star_b_rect)
    
        # Posicionar segunda estrella a la izquierda de la primera
        snd_star_b_rect = pygame.Rect(frs_star_b_rect.left - frs_star_b_rect.width, frs_star_b_rect.top + 20, 100, 40)
        snd_star_b = pygame.image.load("assets/starb.png")
        snd_star_b = pygame.transform.scale(snd_star_b, (200,200))
        pantalla_juego.blit(snd_star_b, snd_star_b_rect)

        # Posicionar tercera estrella a la derecha de la primera
        trd_star_b_rect = pygame.Rect(frs_star_b_rect.right + 20, frs_star_b_rect.top + 20, 100, 40)
        trd_star_b = pygame.image.load("assets/starb.png")
        trd_star_b = pygame.transform.scale(trd_star_b, (200,200))
        pantalla_juego.blit(trd_star_b, trd_star_b_rect)

        # Dibujar un botón "Reset"
        reset_button_text = font.render("Reset", True, (255, 255, 255))
        reset_button_text_rect = reset_button_text.get_rect(center=(pantalla_juego.get_width() // 2, game_over_text_rect.bottom + 450))
        reset_button_rect = reset_button_text_rect.inflate(10, 10)
        pantalla_juego.blit(reset_button_text, reset_button_text_rect)

        # Dibujar un botón "Back"
        back_button_text = font.render("Back", True, (255, 255, 255))
        back_button_text_rect = back_button_text.get_rect(center=(pantalla_juego.get_width() // 2, game_over_text_rect.bottom + 550))
        back_button_rect = back_button_text_rect.inflate(10, 10)  
        pantalla_juego.blit(back_button_text, back_button_text_rect)

            
        # Manejar eventos de clic en el botón de retorno
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and back_button_rect.collidepoint(event.pos):
                # Código para volver al menú principal
                pygame.mixer.stop()
                exec(open("./main.py", "r").read(), globals()) 
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and reset_button_rect.collidepoint(event.pos):
                exec(open("./memorama.py", "r").read(), globals()) 
                pygame.quit()
                sys.exit()


    pygame.display.update()
