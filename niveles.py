import pygame
import sys

# Inicializar Pygame
pygame.init()

# Obtener la resolución de la pantalla del usuario
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

# Definir la resolución base en la que se diseñaron los elementos
base_resolution = (800, 600)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Niveles")

# Función para calcular la posición escalada en función de la resolución
def get_scaled_position(x, y):
    scale_factor = min(SCREEN_WIDTH / base_resolution[0], SCREEN_HEIGHT / base_resolution[1])
    scaled_x = int(x * scale_factor)
    scaled_y = int(y * scale_factor)
    return (scaled_x, scaled_y)

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Definir los rectángulos para cada nivel
rect_1 = pygame.Rect(SCREEN_WIDTH // 3.75, SCREEN_HEIGHT // 2.5, 300, 200)  # Nivel 1
rect_2 = pygame.Rect(SCREEN_WIDTH // 2.25, SCREEN_HEIGHT // 2.5, 300, 200)  # Nivel 2
rect_3 = pygame.Rect(SCREEN_WIDTH // 1.6, SCREEN_HEIGHT // 2.5, 300, 200)  # Nivel 3

# Cargar las imágenes para cada nivel
nivel1_image = pygame.image.load("assets/nivel1.png")
nivel2_image = pygame.image.load("assets/nivel2.png")
nivel3_image = pygame.image.load("assets/nivel3.png")

# Escalar las imágenes para que encajen en los rectángulos
nivel1_image = pygame.transform.scale(nivel1_image, (rect_1.width, rect_1.height))
nivel2_image = pygame.transform.scale(nivel2_image, (rect_2.width, rect_2.height))
nivel3_image = pygame.transform.scale(nivel3_image, (rect_3.width, rect_3.height))

# Función para mostrar un nivel en una nueva ventana
def show_level(level_image):
    level_aspect_ratio = level_image.get_width() / level_image.get_height()
    level_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Calculate the scaled dimensions to maintain the aspect ratio
    scaled_width = int(SCREEN_HEIGHT * level_aspect_ratio)
    scaled_height = SCREEN_HEIGHT
    
    scaled_level = pygame.transform.scale(level_image, (scaled_width, scaled_height))
    
    # Calculate the position to center the image on the screen
    level_position = ((SCREEN_WIDTH - scaled_width) // 2, (SCREEN_HEIGHT - scaled_height) // 2)
    
    level_screen.blit(scaled_level, level_position)
    pygame.display.set_caption("Nivel")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        pygame.display.flip()

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

