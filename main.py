#Short Circuit

# Importación de módulos necesarios
import sys,os   
import pygame
from button import Button # Importación de la clase Button desde un módulo personalizado llamado "button"

# Inicialización de Pygame
pygame.init()

en = False

dif = False

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

# Función para mostrar texto en la pantalla principal
def mostrar_texto(texto, posicion):
    # Definir colores
    main_color = (255, 255, 255)  # Color principal del texto (negro)
    border_color = (0, 0, 0)  # Color del borde (blanco)

    # Crear superficie de texto principal
    font = pygame.font.Font(None, 75)
    text_surface = font.render(texto, True, main_color)

    # Crear superficie de texto con borde
    border_size = 2  # Ajusta el tamaño del borde aquí
    border_surface = font.render(texto, True, border_color)
    border_rect = border_surface.get_rect(center=text_surface.get_rect().center)

    # Ajustar la posición del borde
    border_rect.x -= border_size
    border_rect.y -= border_size

    # Crear una superficie transparente para combinar texto y borde
    combined_surface = pygame.Surface(text_surface.get_size(), pygame.SRCALPHA)
    combined_surface.blit(border_surface, border_rect)
    combined_surface.blit(text_surface, (0, 0))

    # Obtener el rectángulo de la superficie combinada
    combined_rect = combined_surface.get_rect()
    combined_rect.midtop = posicion

    # Blit la superficie combinada en la pantalla
    SCREEN.blit(combined_surface, combined_rect)

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

def get_level1_text():
    if en: 
        return "LEVEL 1"
    else:
        return "NIVEL 1"

def get_level2_text():
    if en: 
        return "LEVEL 2"
    else:
        return "NIVEL 2"

def get_level3_text():
    if en: 
        return "LEVEL 3"
    else:
        return "NIVEL 3"

def get_dif1_text():
    if en and not dif: 
        return "DIFFICULTY: EASY"
    if not en and not dif:
        return "DIFICULTAD: FACIL"
    if en and dif:
        return "DIFFICULTY: HARD"
    if not en and dif:
        return "DIFICULTAD: DIFICIL"


# Función para comenzar el juego
def play():
    global dif

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        # Dibujar los rectángulos en la pantalla principal
        pygame.draw.rect(SCREEN, RED, rect_1, 2)
        pygame.draw.rect(SCREEN, GREEN, rect_2, 2)
        pygame.draw.rect(SCREEN, BLUE, rect_3, 2)

        # Dibujar las imágenes dentro de los rectángulos
        SCREEN.blit(nivel1_image, rect_1)
        SCREEN.blit(nivel2_image, rect_2)
        SCREEN.blit(nivel3_image, rect_3)

        # Mostrar texto debajo de los rectángulos
        mostrar_texto(get_level1_text(), (rect_1.centerx, rect_1.bottom + 10))  
        mostrar_texto(get_level2_text(), (rect_2.centerx, rect_2.bottom + 10))  
        mostrar_texto(get_level3_text(), (rect_3.centerx, rect_3.bottom + 10))  

        OPTIONS_BACK = Button(image=pygame.image.load("assets/play.png"), pos=(SCREEN_WIDTH // 5, SCREEN_HEIGHT // 1.2),
                              text_input=get_back_text(), font=get_font(75), base_color="Black", hovering_color="Cyan")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        OPTIONS_DIF = Button(image=pygame.image.load("assets/difficulty.png"), pos=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 10),
                             text_input=get_dif1_text(), font=get_font(75), base_color="Black", hovering_color="Cyan")

        OPTIONS_DIF.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_DIF.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Si se hace clic izquierdo
                mouse_pos = pygame.mouse.get_pos()
                # Verificar si se hizo clic dentro de algún rectángulo
                if rect_1.collidepoint(mouse_pos) and not dif:
                    pygame.mixer.music.stop()
                    exec(open("pipegame.py", "r").read(), globals()) # Ejecuta el archivo "pipegame.py" 
                    pygame.display.update()
                if rect_1.collidepoint(mouse_pos) and dif:
                    pygame.mixer.music.stop()
                    exec(open("pipegame1.py", "r").read(), globals()) # Ejecuta el archivo "pipegame1.py" 
                    pygame.display.update()
                if rect_2.collidepoint(mouse_pos) and not dif:
                    pygame.mixer.music.stop()
                    exec(open("memorama.py", "r").read(), globals()) # Ejecuta el archivo "memorama.py" 
                    pygame.display.update()
                if rect_2.collidepoint(mouse_pos) and dif:
                    pygame.mixer.music.stop()
                    exec(open("memorama1.py", "r").read(), globals()) # Ejecuta el archivo "memorama1.py" 
                    pygame.display.update()
                if rect_3.collidepoint(mouse_pos) and not dif:
                    pygame.mixer.music.stop()
                    exec(open("Sopa2.1.py", "r").read(), globals()) # Ejecuta el archivo "pipegame.py" 
                    pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_DIF.checkForInput(OPTIONS_MOUSE_POS):
                    if dif:
                        dif = False
                    else:
                        dif = True

        # Actualizar la pantalla
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
