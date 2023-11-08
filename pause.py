import pygame

class PauseButton:
    def __init__(self, x, y, image_path): #Se carga la imagen del boton, se obtiene un rectangulo, coordenadas x e y
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False #Se inicializan las variables clicked
        self.options_shown = False #y options shown a FALSE

    def draw(self, screen): #Dibujar el boton en la pantalla
        screen.blit(self.image, self.rect) 

    def is_clicked(self, mouse_pos): #Verifica si el mouse esta sobre el boton
        if self.rect.collidepoint(mouse_pos):
            self.clicked = True #Variable clicked en True o False
        else:
            self.clicked = False

# Inicializar Pygame
pygame.init()

SCREEN_WIDTH = 800 #Tamaño de la ventana
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Button Pause")

font = pygame.font.SysFont("arialblack", 40)
options_font = pygame.font.SysFont("arialblack", 24)

Color_Text = (255, 255, 255)
# Cargar la imagen del botón de pausa
pause_button = PauseButton(10, 10, "pause_button.png") #Posicion (10,10) con una imagen

def draw_text(text, font, text_col, x, y): #Dibujar el texto en la pantalla
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def show_options(): #Menu d opciones
    while True:
        screen.fill((52, 78, 91))

        # Dibuja las opciones en la pantalla
        draw_text("Resume", options_font, Color_Text, 300, 250)
        draw_text("Options", options_font, Color_Text, 300, 300)
        draw_text("Quit", options_font, Color_Text, 300, 350)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 300 <= x <= 500:
                    if 250 <= y <= 280:
                        # Acción para Resume
                        return
                    elif 300 <= y <= 330:
                        # Acción para Options
                        pass  # Puedes agregar aquí la lógica de las opciones
                    elif 350 <= y <= 380:
                        # Acción para Quit
                        pygame.quit()
                        quit()

        pygame.display.update()

# Game loop
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((52, 78, 91))
     #Dibuje el texto en pantalla con la funcion draw_text
    draw_text("Inicio del juego", font, Color_Text, 160, 250)

    # Dibuja el botón de pausa en la pantalla
    pause_button.draw(screen)

    # Detecta si se hizo clic en el botón de pausa
    #Bucle
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            if pause_button.rect.collidepoint(x, y):
                # Cuando se detecta un clic del botón izquierdo del mouse en el área del botón de pausa,
                # se llama a la función show_options, que muestra el menú de pausa y establece pause_button.options_shown en True.
                show_options()
                pause_button.options_shown = True 

    pygame.display.update() #Actualizar pantalla
