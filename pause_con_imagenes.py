import pygame

class PauseButton:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False
        self.options_shown = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class OptionsScreen:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Options Screen")

        self.font = pygame.font.SysFont("arialblack", 24)
        self.volume = 50

    def draw_text(self, text, x, y, text_col):
        img = self.font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def draw_slider(self, x, y, width, height):
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, width, height))
        pygame.draw.rect(self.screen, (0, 0, 0), (x + self.volume, y, 10, height))

    def show(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 50 <= x <= 750 and 200 <= y <= 250:
                        self.volume = x - 50
                    elif 250 <= x <= 550 and 300 <= y <= 350:
                        print("Nivel reiniciado")
                    elif 300 <= x <= 500 and 400 <= y <= 450:
                        return

            self.screen.fill((52, 78, 91))
            self.draw_text("Volumen", 50, 150, (255, 255, 255))
            self.draw_slider(50, 200, 700, 50)
            self.screen.blit(return_image, (300, 260))  #Coordenadas x, y
            # Reemplaza el texto "Volver al Juego" con la imagen
            self.screen.blit(back_menu_image, (300, 380))

            pygame.display.update()

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Button Pause")

font = pygame.font.SysFont("arialblack", 40)
options_font = pygame.font.SysFont("arialblack", 24)

Color_Text = (255, 255, 255)
pause_button = PauseButton(10, 10, "pause_button.png")

# Cargar las imágenes
resume_image = pygame.image.load("resume_menu.png")
options_image = pygame.image.load("options_menu.png")
quit_image = pygame.image.load("quit_menu.png")
return_image = pygame.image.load("return.png")
# Nueva imagen para "Volver al Juego"
back_menu_image = pygame.image.load("back_menu.png")

def draw_text(text, font, text_col, rect):
    img = font.render(text, True, text_col)
    text_rect = img.get_rect(center=rect.center)
    screen.blit(img, text_rect)

def show_options():
    options_screen = OptionsScreen(800, 600)
    options_screen.show()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            if pause_button.rect.collidepoint(x, y):
                pause_button.options_shown = not pause_button.options_shown

            if pause_button.options_shown:
                if 300 <= x <= 500 and 200 <= y <= 250:
                    print("Resuming game")
                    pause_button.options_shown = False  

                elif 300 <= x <= 500 and 300 <= y <= 350:
                    show_options()

                elif 300 <= x <= 500 and 400 <= y <= 450:
                    pygame.quit()
                    quit()

    screen.fill((52, 78, 91))
    draw_text("Inicio del juego", font, Color_Text, pygame.Rect(160, 250, 400, 50))
    pause_button.draw(screen)

    if pause_button.options_shown:
        screen.blit(resume_image, (300, 160)) #Mover las imagenes x, y
        screen.blit(options_image, (300, 260))
        screen.blit(quit_image, (300, 360))

    pygame.display.update()

pygame.quit()


