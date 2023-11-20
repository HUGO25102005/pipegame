#Short Circuit

# Importación de módulos necesarios
import sys,os   
import pygame
from button import Button # Importación de la clase Button desde un módulo personalizado llamado "button"

# Inicialización de Pygame
pygame.init()

en = False

# Leer el valor desde el archivo la próxima vez que ejecutes el programa
with open('./__pycache__/en.txt', 'r') as archivo:
   en = bool(int(archivo.read()))

volume = 0.5  # Initial volume
min_volume = 0.0
max_volume = 1.0

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

def get_language():
    if en: 
        return "assets/flag1.png"
    else:
        return "assets/flag2.png"

def get_language_text():
    if en: 
        return "LANGUAGE:"
    else:
        return "IDIOMA:"

def get_back_text():
    if en:
        return "BACK"
    if not en:
        return "ATRAS"

def get_credits_image():
    if en:
        return "assets/credits.jpg"
    if not en:
        return "assets/creditos.jpg"

def options():
    global volume, en

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        # Carga la imagen del volumen al comienzo de la función
        volumen_image = pygame.image.load("./assets/volumen_menu.png")

        # Define bar position and dimensions
        bar_x = SCREEN_WIDTH // 4  # Ajustar la posición de la barra según la resolución
        bar_y = SCREEN_HEIGHT // 4
        bar_width = SCREEN_WIDTH // 2
        bar_height = 20

        OPTIONS_ID = Button(image=pygame.image.load("assets/options.png"), pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.5),
                            text_input=get_language_text(), font=get_font(75), base_color="Black", hovering_color="")

        OPTIONS_ID.update(SCREEN)

        # Dibuja la imagen del volumen al lado izquierdo de la barra
        SCREEN.blit(volumen_image, (bar_x - 100, bar_y - 40))  # Ajusta las coordenadas

        OPTIONS_EN = Button(image=pygame.image.load(get_language()), pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.8),
                            text_input="", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_EN.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_EN.update(SCREEN)

        # Draw the volume bar
        bar_color = (255, 255, 255)  # White color
        pygame.draw.rect(SCREEN, bar_color, (bar_x, bar_y, bar_width, bar_height))

        # Draw a volume indicator on the bar
        indicator_pos = bar_x + int(volume * bar_width)
        indicator_color = (0, 255, 0)  # Green color
        pygame.draw.rect(SCREEN, indicator_color, (indicator_pos, bar_y - 5, 10, 30))

        OPTIONS_BACK = Button(image=pygame.image.load("assets/play.png"), pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.2),
                              text_input=get_back_text(), font=get_font(75), base_color="Black", hovering_color="Cyan")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # Get mouse position
                if bar_x <= mouse_pos[0] <= bar_x + bar_width and bar_y <= mouse_pos[1] <= bar_y + bar_height:
                    volume = calculate_volume(mouse_pos, bar_x, bar_y, bar_width)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_EN.checkForInput(OPTIONS_MOUSE_POS):
                    if en:
                        en = False
                    else:
                        en = True

                    # Guardar el valor en un archivo
                    with open('./__pycache__/en.txt', 'w') as archivo:
                        archivo.write(str(int(en)))

        pygame.display.update()

def credits():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        # Cargar una imagen de fondo
        CR = pygame.image.load(get_credits_image())
        CR = pygame.transform.scale(CR, (SCREEN_WIDTH, SCREEN_HEIGHT))

        SCREEN.blit(CR, (0, 0))

        OPTIONS_BACK = Button(image=pygame.image.load("assets/play.png"), pos=(SCREEN_WIDTH // 5, SCREEN_HEIGHT // 1.2),
                              text_input=get_back_text(), font=get_font(75), base_color="Black", hovering_color="Cyan")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def calculate_volume(mouse_pos, bar_x, bar_y, bar_width):
    global volume  # Declare volume as a global variable

    # Calculate volume based on mouse position within the bar
    volume_pos = (mouse_pos[0] - bar_x) / bar_width
    volume = min(max(volume_pos, 0), 1)

    # Set the volume for the music
    pygame.mixer.music.set_volume(volume)

    return volume

def get_play_text():
    if en:
        return "PLAY"
    else:
        return "JUGAR"

def get_option_text():
    if en:
        return "OPTIONS"
    else:
        return "OPCIONES"

def get_quit_text():
    if en:
        return "QUIT"
    else:
        return "SALIR"

def get_credits_text():
    if en:
        return "CREDITS"
    else:
        return "CREDITOS"

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
                            text_input=get_play_text(), font=get_scaled_font(75), base_color="White", hovering_color="Cyan")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/options.png"), pos=get_scaled_position(640, 350), 
                            text_input=get_option_text(), font=get_scaled_font(75), base_color="White", hovering_color="Cyan")
        CREDITS_BUTTON = Button(image=pygame.image.load("assets/options.png"), pos=get_scaled_position(640, 450), 
                            text_input=get_credits_text(), font=get_scaled_font(75), base_color="White", hovering_color="Cyan")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/quit.png"), pos=get_scaled_position(640, 550), 
                           text_input=get_quit_text(), font=get_scaled_font(75), base_color="White", hovering_color="Cyan")

        SCREEN.blit(MENU_TEXT, MENU_RECT) # Dibuja el título del menú
        
        # Actualiza y muestra los botones en el menú principal
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, CREDITS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Punto de entrada principal del programa
if __name__ == "__main__":
    main_menu()
