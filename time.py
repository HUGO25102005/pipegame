import pygame
import time
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600 #Define el ancho y alto de la ventana
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Crea la ventana
pygame.display.set_caption('Temporizador') #Titulo de la ventana

# Inicializar el reloj de Pygame
clock = pygame.time.Clock() #Crea un objecto clock

# Fuente para el temporizador
font = pygame.font.Font(None, 36) #Crea un objeto de fuente para mostrar texto en la ventana con tamaño de fuente 36.

# Inicializar el cronómetro
tiempo_inicial = time.time() # Obtiene el tiempo actual en segundos desde el epoch (tiempo de referencia) para inicializar el temporizador.
duracion_temporizador = 60
tiempo_final = tiempo_inicial + duracion_temporizador #Calcula el tiempo final sumando la duración al tiempo inicial.
game_over = False #Inicializa una bandera para controlar si el juego ha terminado o no.

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Verifica si se produce un evento de cierre de la ventana.
            game_over = True #Cambia la bandera game_over a True si se detecta el evento de cierre de la ventana.

    if not game_over:
        tiempo_restante = max(int(tiempo_final - time.time()), 0)

        if tiempo_restante <= 0:
            #si el tiempo se acaba
            print("¡Tiempo agotado!")
            game_over = True

        # Limpiar la pantalla
        screen.fill((255, 255, 255))

        # Actualizar y dibujar el texto del temporizador
        timer_text = font.render("Tiempo: {}".format(tiempo_restante), True, (255, 0, 0))
        text_rect = timer_text.get_rect(topright=(SCREEN_WIDTH - 10, 10))
        screen.blit(timer_text, text_rect)

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la frecuencia de actualización
        clock.tick(60)
# Cerrar Pygame al salir
pygame.quit()
sys.exit()
