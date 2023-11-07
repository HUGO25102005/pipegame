#Short Circuit

# Importación de módulos necesarios
import sys,os   
import pygame
from button import Button # Importación de la clase Button desde un módulo personalizado llamado "button"

# Inicialización de Pygame
pygame.init()

# Cargar el archivo de audio
pygame.mixer.music.load("assets/Rose_Garden.ogg")

# Reproducir el audio en bucle
pygame.mixer.music.play(-1)  # El valor -1 indica que el audio se reproducirá en bucle infinito

# Obtener la resolución de la pantalla del usuario
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

# Definir la resolución base en la que se diseñaron los elementos
base_resolution = (1280, 720)

# Configuración de la ventana principal
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("") # Puedes poner un título entre las comillas

# Cargar una imagen de fondo
BG = pygame.image.load("assets/background.png")
BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Función para obtener una fuente con el tamaño especificado
def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

# Función para comenzar el juego
def play():
    pygame.mixer.music.stop()
    # Cargar el archivo de audio
    pygame.mixer.music.load("assets/A_Lonely_Cherry_Tree.ogg")

    # Reproducir el audio en bucle
    pygame.mixer.music.play(-1)  # El valor -1 indica que el audio se reproducirá en bucle infinito

    exec(open("pipegame.py", "r").read(), globals()) # Ejecuta el archivo "pipegame.py" 
    pygame.display.update()


# Función para obtener una fuente con el tamaño escalado en función de la resolución
def get_scaled_font(size):
    base_resolution = (1280, 720)  # Resolución base en la que se diseñaron los elementos
    scale_factor = min(SCREEN_WIDTH / base_resolution[0], SCREEN_HEIGHT / base_resolution[1])
    scaled_size = int(size * scale_factor)
    return pygame.font.Font("assets/font.ttf", scaled_size)

# Función para calcular la posición escalada en función de la resolución
def get_scaled_position(x, y):
    scale_factor = min(SCREEN_WIDTH / base_resolution[0], SCREEN_HEIGHT / base_resolution[1])
    scaled_x = int(x * scale_factor)
    scaled_y = int(y * scale_factor)
    return (scaled_x, scaled_y)

# Función para mostrar el menú principal
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0)) # Dibuja la imagen de fondo en la pantalla

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        # Renderiza y muestra el título del menú principal
        MENU_TEXT = get_font(100).render("SHORT CIRCUIT", True, "#88ff3f")
        MENU_RECT = MENU_TEXT.get_rect(center=get_scaled_position(640, 100))
        
        # Crea botones para "JUGAR", "OPCIONES" y "SALIR" en el menú principal
        PLAY_BUTTON = Button(image=pygame.image.load("assets/play.png"), pos=get_scaled_position(640, 250), 
                            text_input="PLAY", font=get_scaled_font(75), base_color="White", hovering_color="Cyan")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/options.png"), pos=get_scaled_position(640, 400), 
                            text_input="OPTIONS", font=get_scaled_font(75), base_color="White", hovering_color="Cyan")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/quit.png"), pos=get_scaled_position(640, 550), 
                            text_input="QUIT", font=get_scaled_font(75), base_color="White", hovering_color="Cyan")

        SCREEN.blit(MENU_TEXT, MENU_RECT) # Dibuja el título del menú
        
        # Actualiza y muestra los botones en el menú principal
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Punto de entrada principal del programa
if __name__ == "__main__":
    main_menu()
