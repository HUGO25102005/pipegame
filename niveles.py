import pygame
import sys

# Niveles, pantalla ancho y alto de la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Niveles")

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Definir los rectángulos para cada nivel
rect_1 = pygame.Rect(50, 50, 200, 100)  # Nivel 1
rect_2 = pygame.Rect(300, 50, 200, 100)  # Nivel 2
rect_3 = pygame.Rect(550, 50, 200, 100)  # Nivel 3

# Cargar las imágenes para cada nivel
nivel1_image = pygame.image.load("nivel1.png")
nivel2_image = pygame.image.load("nivel2.png")
nivel3_image = pygame.image.load("nivel3.png")

# Escalar las imágenes para que encajen en los rectángulos
nivel1_image = pygame.transform.scale(nivel1_image, (rect_1.width, rect_1.height))
nivel2_image = pygame.transform.scale(nivel2_image, (rect_2.width, rect_2.height))
nivel3_image = pygame.transform.scale(nivel3_image, (rect_3.width, rect_3.height))

# Función para mostrar un nivel en una nueva ventana
def show_level(level_image):
    level_aspect_ratio = level_image.get_width() / level_image.get_height()
    level_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    scaled_level = pygame.transform.scale(level_image, (int(SCREEN_HEIGHT * level_aspect_ratio), SCREEN_HEIGHT))
    level_screen.blit(scaled_level, ((SCREEN_WIDTH - scaled_level.get_width()) // 2, 0))
    pygame.display.set_caption("Nivel")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        pygame.display.flip()

# Función para mostrar texto en la pantalla principal
def mostrar_texto(texto, posicion):
    font = pygame.font.Font(None, 36)  # Puedes ajustar el tamaño de la fuente aquí
    text_surface = font.render(texto, True, BLACK)  # BLACK es un color definido o (0, 0, 0)
    text_rect = text_surface.get_rect()
    text_rect.midtop = posicion
    screen.blit(text_surface, text_rect)

# Bucle principal del juego
running = True
while running:
    screen.fill(WHITE)

    # Dibujar los rectángulos en la pantalla principal
    pygame.draw.rect(screen, RED, rect_1, 2)
    pygame.draw.rect(screen, GREEN, rect_2, 2)
    pygame.draw.rect(screen, BLUE, rect_3, 2)

    # Dibujar las imágenes dentro de los rectángulos
    screen.blit(nivel1_image, rect_1)
    screen.blit(nivel2_image, rect_2)
    screen.blit(nivel3_image, rect_3)

    # Mostrar texto debajo de los rectángulos
    mostrar_texto("Nivel 1", rect_1.midbottom)
    mostrar_texto("Nivel 2", rect_2.midbottom)
    mostrar_texto("Nivel 3", rect_3.midbottom)

    # Actualizar la pantalla
    pygame.display.flip()

    # Manejar eventos en la pantalla principal
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Si se hace clic izquierdo
            mouse_pos = pygame.mouse.get_pos()
            # Verificar si se hizo clic dentro de algún rectángulo
            if rect_1.collidepoint(mouse_pos):
                current_level = nivel1_image
            elif rect_2.collidepoint(mouse_pos):
                current_level = nivel2_image
            elif rect_3.collidepoint(mouse_pos):
                current_level = nivel3_image

            if current_level:
                show_level(current_level)

pygame.quit()

