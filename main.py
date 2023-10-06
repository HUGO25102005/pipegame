#Short Circuit

# Importación de módulos necesarios
import sys,os   
import pygame
from button import Button # Importación de la clase Button desde un módulo personalizado llamado "button"

# Inicialización de Pygame
pygame.init()

# Obtener la resolución de la pantalla del usuario
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

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
    exec(open("pipegame.py", "r").read(), globals()) # Ejecuta el archivo "pipegame.py" 
    pygame.display.update()

# Función para mostrar la pantalla de opciones
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white") # Rellena la pantalla de blanco    

        # Renderiza y muestra un texto en la pantalla de opciones   
        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        
        # Crea un botón de "VOLVER" en la pantalla de opciones
        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

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

# Función para mostrar el menú principal
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0)) # Dibuja la imagen de fondo en la pantalla

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        # Renderiza y muestra el título del menú principal
        MENU_TEXT = get_font(100).render("SHORT CIRCUIT", True, "#88ff3f")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        
        # Crea botones para "JUGAR", "OPCIONES" y "SALIR" en el menú principal
        PLAY_BUTTON = Button(image=pygame.image.load("assets/play.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#bbbbbb", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/options.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#bbbbbb", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/quit.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#bbbbbb", hovering_color="White")

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
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Punto de entrada principal del programa
if __name__ == "__main__":
    main_menu()
