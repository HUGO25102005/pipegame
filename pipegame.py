#Short Circuit

#Importación de módulos necesarios
import os,sys,time
import pygame

pygame.init()

# Definición de constantes
NUM_CELLS = 6
CELL_SIZE = 68

#Detectar si el juego ha terminado
game_over = False

#Inicializar el cronometro
tiempo_inicial = time.time()
duracion_temporizador = 60
tiempo_final = tiempo_inicial + duracion_temporizador

# Set initial background
current_background = 0

# Crear un objeto de fuente para el temporizador
font = pygame.font.Font(None, 120)

# Obtener la resolución de la pantalla del usuario
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

# Calcula el ancho y alto de la tabla
TABLE_WIDTH = NUM_CELLS * CELL_SIZE
TABLE_HEIGHT = NUM_CELLS * CELL_SIZE

# Calcula la posición inicial para centrar la tabla en la pantalla
TABLE_X = (SCREEN_WIDTH - TABLE_WIDTH) // 2 - 8
TABLE_Y = (SCREEN_HEIGHT - TABLE_HEIGHT) // 2 + 4

# Configuración de la ventana principal
Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("") 

# Cargar una imagen de fondo
BG = pygame.image.load("assets/image.png")
BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Definición de la clase "Object"
class Object:
    def __init__(self, rect, cell_pos):
        self.rect = pygame.Rect(rect) # Crear un cuadrado con las dimensiones especificadas
        self.cell_pos = cell_pos # Posición de la celda en la cuadrícula
        self.original_cell_pos = cell_pos
        self.click = False # Variable para rastrear si el objeto está siendo arrastrado
        self.clickable = True # Variable para habilitar/deshabilitar la interacción con el objeto
        self.image = pygame.Surface(self.rect.size).convert() # Crear una superficie del tamaño del rectángulo
        self.image = pygame.image.load("./assets/vert_block.png") # Cargar una imagen para el objeto
        self.collide_rect = self.rect # Cuadrado de colisión

    def update(self, surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos() # Actualizar la posición del objeto según la posición del ratón
            self.cell_pos = (self.rect.centerx // CELL_SIZE, self.rect.centery // CELL_SIZE)
            self.rect.centerx = self.cell_pos[0] * CELL_SIZE + CELL_SIZE // 2
            self.rect.centery = self.cell_pos[1] * CELL_SIZE + CELL_SIZE // 2
        surface.blit(self.image, self.rect) # Dibujar la imagen del objeto en la superficie

# Definición de funciones para actualizar objetos específicos
def update_obj2(Surface):
    Surface.blit(obj2.image,obj2.rect)  
    obj2.alpha = 255

def update_obj3(Surface):
    Surface.blit(obj3.image,obj3.rect)
    obj3.alpha = 255

def update_obj4(Surface):
    Surface.blit(obj4.image,obj4.rect)
    obj4.alpha = 255

def update_obj5(Surface):
    Surface.blit(obj5.image,obj5.rect)
    obj5.alpha = 255

def update_obj6(Surface):
    Surface.blit(obj6.image,obj6.rect)
    obj6.alpha = 255

def update_obj7(Surface):
    Surface.blit(obj7.image,obj7.rect)
    obj7.alpha = 255

def update_obj8(Surface):
    Surface.blit(obj8.image,obj8.rect)
    obj8.alpha = 255

def update_obj9(Surface):
    Surface.blit(obj9.image,obj9.rect)
    obj9.alpha = 255

def objects_in_same_cell(obj1, obj2):
    return obj1.cell_pos == obj2.cell_pos

# Function to draw a red.png image on top of a cell
def draw_red_image(surface, cell_position):
    red_image = pygame.image.load("assets/red.png")
    red_image = pygame.transform.scale(red_image, (CELL_SIZE, CELL_SIZE))  # Scale the red image to the cell size
    red_rect = red_image.get_rect(topleft=(cell_position[0] * CELL_SIZE, cell_position[1] * CELL_SIZE))
    surface.blit(red_image, red_rect)

# Definición de un botón de retorno
back_button = pygame.Rect(10, 500, 100, 40)

# Función principal
def main(Surface, obj, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9,obj10,obj11):
    global game_over
    game_event_loop(obj, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9) # Capturar eventos del juego
    Surface.blit(BG, (0, 0)) # Dibujar el fondo del nivel

    # Dibujar todas las celdas como blancas
    for x in range(NUM_CELLS):
        for y in range(NUM_CELLS):
                white_rect = pygame.Rect(TABLE_X + x * CELL_SIZE, TABLE_Y + y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(Surface, (255, 255, 255), white_rect)

    for x in range(NUM_CELLS):
        for y in range(NUM_CELLS):
            cell_position = (x, y)
            objects_in_cell = [obj, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9]
            objects_in_cell = [obj for obj in objects_in_cell if obj.cell_pos == cell_position]
        
            if len(objects_in_cell) > 1:
                draw_red_image(Screen, cell_position)

     # Dibujar líneas de cuadrícula
    for i in range(NUM_CELLS + 1):
        # Dibuja líneas horizontales centradas en la tabla
        pygame.draw.line(Surface, (0, 0, 0), (TABLE_X, TABLE_Y + i * CELL_SIZE), (TABLE_X + TABLE_WIDTH, TABLE_Y + i * CELL_SIZE))
        # Dibuja líneas verticales centradas en la tabla
        pygame.draw.line(Surface, (0, 0, 0), (TABLE_X + i * CELL_SIZE, TABLE_Y), (TABLE_X + i * CELL_SIZE, TABLE_Y + TABLE_HEIGHT))  

    # Actualizar y dibujar objetos en la superficie
    obj10.update(Surface)
    obj11.update(Surface)
    obj.update(Surface)
    obj2.update(Surface)
    obj3.update(Surface)
    obj4.update(Surface)
    obj5.update(Surface)
    obj6.update(Surface)
    obj7.update(Surface)
    obj8.update(Surface)
    obj9.update(Surface)
    update_obj2(Surface)
    update_obj3(Surface)
    update_obj4(Surface)
    update_obj5(Surface)
    update_obj6(Surface)        
    update_obj7(Surface)
    update_obj8(Surface)
    update_obj9(Surface)

    # Check if two or more objects are in the same cell
    cell_occupancy = {}
    for move_obj in [obj, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9]:
        if move_obj.cell_pos in cell_occupancy:
            cell_occupancy[move_obj.cell_pos].append(move_obj)
        else:
            cell_occupancy[move_obj.cell_pos] = [move_obj]

    # Draw red image in front of cells with multiple objects
    for cell, objects_in_cell in cell_occupancy.items():
        if len(objects_in_cell) >= 2:
            draw_red_image(Surface, cell)

    # Cargar una nueva imagen y aplicarla a los objetos 6 al 9
    new_image = pygame.image.load("./assets/hori_block.png")
    for obj6_9 in [obj6, obj7, obj8, obj9]:
        obj6_9.image = new_image 
    
    # Verificar si se ha completado el juego
    if (
        obj.cell_pos[0] == 11 and 6 <= obj.cell_pos[1] <= 9 and
        obj2.cell_pos[0] == 11 and 6 <= obj2.cell_pos[1] <= 9 and
        obj3.cell_pos[0] == 11 and 6 <= obj3.cell_pos[1] <= 9 and
        obj4.cell_pos[0] == 11 and 6 <= obj4.cell_pos[1] <= 9 and
        obj5.cell_pos == (11, 10) and
        12 <= obj6.cell_pos[0] <= 15 and obj6.cell_pos[1] == 10 and
        12 <= obj7.cell_pos[0] <= 15 and obj7.cell_pos[1] == 10 and
        12 <= obj8.cell_pos[0] <= 15 and obj8.cell_pos[1] == 10 and
        12 <= obj9.cell_pos[0] <= 15 and obj9.cell_pos[1] == 10 and
        pygame.mouse.get_pressed()[0] == False
    ):
        game_over = True
        obj.clickable = False
        obj2.clickable = False
        obj3.clickable = False
        obj4.clickable = False
        obj5.clickable = False
        obj6.clickable = False
        obj7.clickable = False
        obj8.clickable = False
        obj9.clickable = False
        
    if game_over:
        global current_background

        # Load background images or create surfaces for animation
        background_images = [
        pygame.image.load("assets/image.png"),
        pygame.image.load("assets/image-2.png"),
        pygame.image.load("assets/image-3.png"),
        pygame.image.load("assets/image-4.png"),
        pygame.image.load("assets/image-5.png"),
        pygame.image.load("assets/image-6.png"),
        pygame.image.load("assets/image-7.png"),
        pygame.image.load("assets/image-8.png"),
        ]

        current_background = (current_background + 1) % len(background_images)
        
        BG1 = pygame.transform.scale(background_images[current_background], (SCREEN_WIDTH, SCREEN_HEIGHT))
        Screen.blit(BG1, (0, 0))

        BG2 = pygame.image.load("assets/background_2.png")
        BG2 = pygame.transform.scale(BG2, (SCREEN_WIDTH, SCREEN_HEIGHT))
        Screen.blit(BG2, (0, 0))

        three_stars = False
        two_stars = False
        one_star = False

        # Mostrar un mensaje de victoria
        font = pygame.font.Font(None, 120)
        text = font.render("You Won!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(Surface.get_width() // 2, Surface.get_height() // 5))
        Surface.blit(text, text_rect)

        # Dibujar estrella central
        frs_star_b = pygame.image.load("assets/starb.png")
        frs_star_b = pygame.transform.scale(frs_star_b, (200,200))
        frs_star_b_rect = frs_star_b.get_rect(center=(Surface.get_width() // 2, Surface.get_height() // 3))
        Surface.blit(frs_star_b, frs_star_b_rect)
        
        # Posicionar segunda estrella a la izquierda de la primera
        snd_star_b_rect = pygame.Rect(frs_star_b_rect.left - frs_star_b_rect.width, frs_star_b_rect.top + 20, 100, 40)
        snd_star_b = pygame.image.load("assets/starb.png")
        snd_star_b = pygame.transform.scale(snd_star_b, (200,200))
        Surface.blit(snd_star_b, snd_star_b_rect)

        # Posicionar segunda estrella a la izquierda de la primera
        trd_star_b_rect = pygame.Rect(frs_star_b_rect.right - frs_star_b_rect.width + 200, frs_star_b_rect.top + 20, 100, 40)
        trd_star_b = pygame.image.load("assets/starb.png")
        trd_star_b = pygame.transform.scale(trd_star_b, (200,200))
        Surface.blit(trd_star_b, trd_star_b_rect)

        if tiempo_restante >= 40:
            three_stars = True
         
        if tiempo_restante >= 20 and tiempo_restante < 40:
            two_stars = True

        if tiempo_restante < 20:
            one_star = True

        if three_stars:
            # Dibujar estrella central
            frs_star = pygame.image.load("assets/star.png")
            frs_star = pygame.transform.scale(frs_star, (200,200))
            frs_star_rect = frs_star.get_rect(center=(Surface.get_width() // 2, Surface.get_height() // 3))
            Surface.blit(frs_star, frs_star_rect)
        
            # Posicionar segunda estrella a la izquierda de la primera
            snd_star_rect = pygame.Rect(frs_star_rect.left - frs_star_rect.width, frs_star_rect.top + 20, 100, 40)
            snd_star = pygame.image.load("assets/star.png")
            snd_star = pygame.transform.scale(snd_star, (200,200))
            Surface.blit(snd_star, snd_star_rect)

            # Posicionar segunda estrella a la izquierda de la primera
            trd_star_rect = pygame.Rect(frs_star_rect.right - frs_star_rect.width + 200, frs_star_rect.top + 20, 100, 40)
            trd_star = pygame.image.load("assets/star.png")
            trd_star = pygame.transform.scale(trd_star, (200,200))
            Surface.blit(trd_star, trd_star_rect)

        if two_stars:
            # Dibujar estrella central
            frs_star = pygame.image.load("assets/star.png")
            frs_star = pygame.transform.scale(frs_star, (200,200))
            frs_star_rect = frs_star.get_rect(center=(Surface.get_width() // 2, Surface.get_height() // 3))
            Surface.blit(frs_star, frs_star_rect)
        
            # Posicionar segunda estrella a la izquierda de la primera
            snd_star_rect = pygame.Rect(frs_star_rect.left - frs_star_rect.width, frs_star_rect.top + 20, 100, 40)
            snd_star = pygame.image.load("assets/star.png")
            snd_star = pygame.transform.scale(snd_star, (200,200))
            Surface.blit(snd_star, snd_star_rect)

        if one_star:
            # Dibujar estrella central
            frs_star = pygame.image.load("assets/star.png")
            frs_star = pygame.transform.scale(frs_star, (200,200))
            frs_star_rect = frs_star.get_rect(center=(Surface.get_width() // 2, Surface.get_height() // 3))
            Surface.blit(frs_star, frs_star_rect)
        
        # Dibujar un botón de retorno
        back_button_text = font.render("Back", True, (255, 255, 255))
        back_button_text_rect = back_button_text.get_rect(center=(Surface.get_width() // 2, text_rect.bottom + 450))
        back_button_rect = back_button_text_rect.inflate(10, 10)  
        Surface.blit(back_button_text, back_button_text_rect)
        
        # Manejar eventos de clic en el botón de retorno
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and back_button_rect.collidepoint(event.pos):
                exec(open("./main.py", "r").read(), globals()) 
                pygame.display.update()
                pygame.quit()
                sys.exit()

def mouse_release():
    pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONUP, button=pygame.BUTTON_LEFT))

# Función para manejar eventos del juego
def game_event_loop(obj,obj2,obj3,obj4,obj5,obj6,obj7,obj8,obj9):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Manejar el evento de clic del mouse en los objetos
            if obj.rect.collidepoint(event.pos) and obj.clickable:
                obj.click = True
            elif obj2.rect.collidepoint(event.pos) and obj2.clickable:
                obj2.click = True
            elif obj3.rect.collidepoint(event.pos) and obj3.clickable:
                obj3.click = True
            elif obj4.rect.collidepoint(event.pos) and obj4.clickable:
                obj4.click = True
            elif obj5.rect.collidepoint(event.pos) and obj5.clickable:
                obj5.click = True
            elif obj6.rect.collidepoint(event.pos) and obj6.clickable:
                obj6.click = True
            elif obj7.rect.collidepoint(event.pos) and obj7.clickable:
                obj7.click = True
            elif obj8.rect.collidepoint(event.pos) and obj8.clickable:
                obj8.click = True
            elif obj9.rect.collidepoint(event.pos)and obj9.clickable:
                obj9.click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            game_over = True
            # Manejar el evento de liberación del mouse para detener el arrastre
            obj.click = False
            obj2.click = False
            obj3.click = False
            obj4.click = False
            obj5.click = False
            obj6.click = False
            obj7.click = False
            obj8.click = False
            obj9.click = False

            # Verificar y corregir la posición de los objetos si están fuera de los límites
            for move_obj in [obj, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9]:
                move_obj.rect.centerx = max(TABLE_X + CELL_SIZE // 2, move_obj.rect.centerx)
                move_obj.rect.centerx = min(TABLE_X + TABLE_WIDTH - CELL_SIZE // 2, move_obj.rect.centerx)
                move_obj.rect.centery = max(TABLE_Y + CELL_SIZE // 2, move_obj.rect.centery)
                move_obj.rect.centery = min(TABLE_Y + TABLE_HEIGHT - CELL_SIZE // 2, move_obj.rect.centery)

                # Update the cell position based on the corrected rectangle position
                move_obj.cell_pos = (move_obj.rect.centerx // CELL_SIZE, move_obj.rect.centery // CELL_SIZE)


            # **Regresar los objetos a su posición original**
            for move_obj in [obj, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9]:
                if not move_obj.click and move_obj.cell_pos == (11, 5) or move_obj.cell_pos == (16, 10):
                    move_obj.rect.centerx = move_obj.original_cell_pos[0] * CELL_SIZE + CELL_SIZE // 2
                    move_obj.rect.centery = move_obj.original_cell_pos[1] * CELL_SIZE + CELL_SIZE // 2

                    # Update the cell position based on the corrected rectangle position
                    move_obj.cell_pos = (move_obj.rect.centerx // CELL_SIZE, move_obj.rect.centery // CELL_SIZE)


        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Función principal del programa
if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    Screen.blit(BG, (0, 0)) # Dibuja la imagen de fondo en la pantalla
    MyClock = pygame.time.Clock()
    obj = Object((TABLE_X + CELL_SIZE * 1, TABLE_Y + CELL_SIZE * 1, CELL_SIZE, CELL_SIZE), (12, 6))
    obj2 = Object((TABLE_X + CELL_SIZE * 2, TABLE_Y + CELL_SIZE * 2, CELL_SIZE, CELL_SIZE), (13, 7))
    obj3 = Object((TABLE_X + CELL_SIZE * 4, TABLE_Y + CELL_SIZE * 4, CELL_SIZE, CELL_SIZE), (15,9))
    obj4 = Object((TABLE_X + CELL_SIZE * 2, TABLE_Y + CELL_SIZE * 3, CELL_SIZE, CELL_SIZE), (13, 8))
    obj5 = Object((TABLE_X + CELL_SIZE * 3, TABLE_Y + CELL_SIZE * 4, CELL_SIZE, CELL_SIZE), (14, 9))
    obj6 = Object((TABLE_X + CELL_SIZE * 1, TABLE_Y + CELL_SIZE * 3, CELL_SIZE, CELL_SIZE), (12, 8))
    obj7 = Object((TABLE_X + CELL_SIZE * 3, TABLE_Y + CELL_SIZE * 5, CELL_SIZE, CELL_SIZE), (14, 10))
    obj8 = Object((TABLE_X + CELL_SIZE * 4, TABLE_Y + CELL_SIZE * 3, CELL_SIZE, CELL_SIZE), (15, 8))
    obj9 = Object((TABLE_X + CELL_SIZE * 2, TABLE_Y + CELL_SIZE * 5, CELL_SIZE, CELL_SIZE), (13, 10))
    obj10 = Object((TABLE_X + CELL_SIZE * 0, TABLE_Y + CELL_SIZE * 0, CELL_SIZE, CELL_SIZE), (11, 5))
    obj11 = Object((TABLE_X + CELL_SIZE * 5, TABLE_Y + CELL_SIZE * 5, CELL_SIZE, CELL_SIZE), (16, 10))
    obj10.image = pygame.image.load("./assets/fuzebox_start1.png")
    obj11.image = pygame.image.load("./assets/fuzebox_end1.png")
    obj5.image = pygame.image.load("./assets/topright_block.png")

    while 1:
        if not game_over:
            tiempo_restante = int(tiempo_final - time.time())
            
        main(Screen,obj,obj2,obj3,obj4,obj5,obj6,obj7,obj8,obj9,obj10,obj11)
        
        if not game_over and tiempo_restante > 0:
            # Actualiza y dibuja el texto del temporizador
            timer_text = font.render("Time: {}".format(tiempo_restante), True, (255, 0, 0))
            text_rect = timer_text.get_rect(topright=(SCREEN_WIDTH - 10, 10))
            Screen.blit(timer_text, text_rect)
    
        # Verificar si el tiempo ha llegado a 0
        if tiempo_restante <= 0 and not game_over:

            # Manejar el evento de liberación del mouse para detener el arrastre
            obj.click = False
            obj2.click = False
            obj3.click = False
            obj4.click = False
            obj5.click = False
            obj6.click = False
            obj7.click = False
            obj8.click = False
            obj9.click = False
            mouse_release()
            
            BG1 = pygame.image.load("assets/image-1.png")
            BG1 = pygame.transform.scale(BG1, (SCREEN_WIDTH, SCREEN_HEIGHT))
            Screen.blit(BG1, (0, 0))

            BG2 = pygame.image.load("assets/background_2.png")
            BG2 = pygame.transform.scale(BG2, (SCREEN_WIDTH, SCREEN_HEIGHT))
            Screen.blit(BG2, (0, 0))

            # Mostrar "Game Over"
            game_over_text = font.render("Game Over!", True, (255, 0, 0))
            game_over_text_rect = game_over_text.get_rect(center=(Screen.get_width() // 2, Screen.get_height() // 5))
            Screen.blit(game_over_text, game_over_text_rect)
                        
            # Dibujar estrella central
            frs_star_b = pygame.image.load("assets/starb.png")
            frs_star_b = pygame.transform.scale(frs_star_b, (200,200))
            frs_star_b_rect = frs_star_b.get_rect(center=(Screen.get_width() // 2, Screen.get_height() // 3))
            Screen.blit(frs_star_b, frs_star_b_rect)
        
            # Posicionar segunda estrella a la izquierda de la primera
            snd_star_b_rect = pygame.Rect(frs_star_b_rect.left - frs_star_b_rect.width, frs_star_b_rect.top + 20, 100, 40)
            snd_star_b = pygame.image.load("assets/starb.png")
            snd_star_b = pygame.transform.scale(snd_star_b, (200,200))
            Screen.blit(snd_star_b, snd_star_b_rect)

            # Posicionar segunda estrella a la izquierda de la primera
            trd_star_b_rect = pygame.Rect(frs_star_b_rect.right - frs_star_b_rect.width + 200, frs_star_b_rect.top + 20, 100, 40)
            trd_star_b = pygame.image.load("assets/starb.png")
            trd_star_b = pygame.transform.scale(trd_star_b, (200,200))
            Screen.blit(trd_star_b, trd_star_b_rect)

            # Dibujar un botón "Reset"
            reset_button_text = font.render("Reset", True, (255, 255, 255))
            reset_button_text_rect = reset_button_text.get_rect(center=(Screen.get_width() // 2, game_over_text_rect.bottom + 450))
            reset_button_rect = reset_button_text_rect.inflate(10, 10)
            Screen.blit(reset_button_text, reset_button_text_rect)

            # Dibujar un botón "Back"
            back_button_text = font.render("Back", True, (255, 255, 255))
            back_button_text_rect = back_button_text.get_rect(center=(Screen.get_width() // 2, game_over_text_rect.bottom + 550))
            back_button_rect = back_button_text_rect.inflate(10, 10)  
            Screen.blit(back_button_text, back_button_text_rect)

            
            # Manejar eventos de clic en el botón de retorno
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and back_button_rect.collidepoint(event.pos):
                    # Código para volver al menú principal
                    exec(open("./main.py", "r").read(), globals()) 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and reset_button_rect.collidepoint(event.pos):
                    exec(open("./pipegame.py", "r").read(), globals()) 
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()
        MyClock.tick(120)
