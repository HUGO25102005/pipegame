#Short Circuit

#Importación de módulos necesarios
import os,sys
import pygame
    
# Definición de constantes
NUM_CELLS = 6
CELL_SIZE = 68

#Detectar si el juego ha terminado
game_over = False

# Definir el tiempo inicial en segundos
INITIAL_TIME = 30

# Crear un objeto de fuente para el temporizador
font = pygame.font.Font(None, 36)

# Obtener la resolución de la pantalla del usuario
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

# Calcula el ancho y alto de la tabla
TABLE_WIDTH = NUM_CELLS * CELL_SIZE
TABLE_HEIGHT = NUM_CELLS * CELL_SIZE

# Calcula la posición inicial para centrar la tabla en la pantalla
TABLE_X = 0
TABLE_Y = 0

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

     # Dibujar líneas de cuadrícula
    for i in range(NUM_CELLS + 1):
        # Dibuja líneas horizontales centradas en la tabla
        pygame.draw.line(Surface, (0, 0, 0), (TABLE_X, TABLE_Y + i * CELL_SIZE), (TABLE_X + TABLE_WIDTH, TABLE_Y + i * CELL_SIZE))
        # Dibuja líneas verticales centradas en la tabla
        pygame.draw.line(Surface, (0, 0, 0), (TABLE_X + i * CELL_SIZE, TABLE_Y), (TABLE_X + i * CELL_SIZE, TABLE_Y + TABLE_HEIGHT))  

    # Actualizar y dibujar objetos en la superficie
    obj.update(Surface)
    obj2.update(Surface)
    obj3.update(Surface)
    obj4.update(Surface)
    obj5.update(Surface)
    obj6.update(Surface)
    obj7.update(Surface)
    obj8.update(Surface)
    obj9.update(Surface)
    obj10.update(Surface)
    obj11.update(Surface)
    update_obj2(Surface)
    update_obj3(Surface)
    update_obj4(Surface)
    update_obj5(Surface)
    update_obj6(Surface)        
    update_obj7(Surface)
    update_obj8(Surface)
    update_obj9(Surface)
    
    # Cargar una nueva imagen y aplicarla a los objetos 6 al 9
    new_image = pygame.image.load("./assets/hori_block.png")
    for obj6_9 in [obj6, obj7, obj8, obj9]:
        obj6_9.image = new_image 
    
    # Verificar si se ha completado el juego
    if (
        obj.cell_pos[0] == 0 and 1 <= obj.cell_pos[1] <= 4 and
        obj2.cell_pos[0] == 0 and 1 <= obj2.cell_pos[1] <= 4 and
        obj3.cell_pos[0] == 0 and 1 <= obj3.cell_pos[1] <= 4 and
        obj4.cell_pos[0] == 0 and 1 <= obj4.cell_pos[1] <= 4 and
        obj5.cell_pos == (0, 5) and
        1 <= obj6.cell_pos[0] <= 4 and obj6.cell_pos[1] == 5 and
        1 <= obj7.cell_pos[0] <= 4 and obj7.cell_pos[1] == 5 and
        1 <= obj8.cell_pos[0] <= 4 and obj8.cell_pos[1] == 5 and
        1 <= obj9.cell_pos[0] <= 4 and obj9.cell_pos[1] == 5 and
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
        # Mostrar un mensaje de victoria
        font = pygame.font.Font(None, 36)
        text = font.render("You Won", True, (255, 0, 0))
        text_rect = text.get_rect(center=(Surface.get_width() // 2, Surface.get_height() // 2))
        Surface.blit(text, text_rect)
        
        # Dibujar un botón de retorno
        back_button_rect = pygame.Rect(Surface.get_width() // 2 - 50, text_rect.bottom + 20, 100, 40)
        pygame.draw.rect(Surface, (0, 255, 0), back_button_rect)
        font = pygame.font.Font(None, 24)
        text = font.render("Back", True, (255, 255, 255))
        text_rect = text.get_rect(center=(back_button_rect.centerx, back_button_rect.centery))
        Surface.blit(text, text_rect)

        
        # Manejar eventos de clic en el botón de retorno
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and back_button_rect.collidepoint(event.pos):
                exec(open("./main.py", "r").read(), globals()) 
                pygame.display.update()
                pygame.quit()
                sys.exit()

    pygame.display.update()

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

            # **Regresar los objetos a su posición original**
            for move_obj in [obj, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9]:
                if not move_obj.click and move_obj.cell_pos == (0, 0) or move_obj.cell_pos == (5, 5):
                    move_obj.rect.centerx = move_obj.original_cell_pos[0] * CELL_SIZE + CELL_SIZE // 2
                    move_obj.rect.centery = move_obj.original_cell_pos[1] * CELL_SIZE + CELL_SIZE // 2

            # Verificar y corregir la posición de los objetos si están fuera de los límites
            for move_obj in [obj, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9]:
                move_obj.rect.centerx = max(CELL_SIZE // 2, move_obj.rect.centerx)
                move_obj.rect.centerx = min(TABLE_WIDTH - CELL_SIZE // 2, move_obj.rect.centerx)
                move_obj.rect.centery = max(CELL_SIZE // 2, move_obj.rect.centery)
                move_obj.rect.centery = min(TABLE_HEIGHT - CELL_SIZE // 2, move_obj.rect.centery)

        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Función principal del programa
if __name__ == "__main__":
    # Crear un reloj para contar el tiempo
    timer = pygame.time.Clock()
    
    start_time = pygame.time.get_ticks()  # Registra el tiempo de inicio del juego en milisegundos

    time_remaining = INITIAL_TIME  # Tiempo inicial en segundos

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    Screen.blit(BG, (0, 0)) # Dibuja la imagen de fondo en la pantalla
    MyClock = pygame.time.Clock()
    obj = Object((CELL_SIZE * 1, CELL_SIZE * 1, CELL_SIZE, CELL_SIZE), (1, 1))  
    obj2 = Object((CELL_SIZE * 2, CELL_SIZE * 2, CELL_SIZE, CELL_SIZE), (2, 2))
    obj3 = Object((CELL_SIZE * 4, CELL_SIZE * 4, CELL_SIZE, CELL_SIZE), (4, 4)) 
    obj4 = Object((CELL_SIZE * 2, CELL_SIZE * 3, CELL_SIZE, CELL_SIZE), (2, 3))
    obj5 = Object((CELL_SIZE * 3, CELL_SIZE * 4, CELL_SIZE, CELL_SIZE), (3, 4))
    obj6 = Object((CELL_SIZE * 1, CELL_SIZE * 3, CELL_SIZE, CELL_SIZE), (1, 3))  
    obj7 = Object((CELL_SIZE * 3, CELL_SIZE * 5, CELL_SIZE, CELL_SIZE), (3, 5))
    obj8 = Object((CELL_SIZE * 4, CELL_SIZE * 3, CELL_SIZE, CELL_SIZE), (4, 3)) 
    obj9 = Object((CELL_SIZE * 2, CELL_SIZE * 5, CELL_SIZE, CELL_SIZE), (2, 5))
    obj10 = Object((CELL_SIZE * 0, CELL_SIZE * 0, CELL_SIZE, CELL_SIZE), (0, 0))
    obj11 = Object((CELL_SIZE * 5, CELL_SIZE * 5, CELL_SIZE, CELL_SIZE), (5, 5))
    obj10.image = pygame.image.load("./assets/fuzebox_start1.png")
    obj11.image = pygame.image.load("./assets/fuzebox_end1.png")
    obj5.image = pygame.image.load("./assets/topright_block.png")

    while 1:
        # Obtén el tiempo transcurrido desde el inicio del juego en milisegundos
        current_time = pygame.time.get_ticks()
        
        # Calcula el tiempo restante en segundos restando el tiempo transcurrido
        time_remaining = max(INITIAL_TIME - (current_time - start_time) / 1000, 0)
        # Renderizar el texto del temporizador
        timer_text = font.render(f"Time: {max(int(time_remaining), 0)}", True, (255, 0, 0))

        main(Screen,obj,obj2,obj3,obj4,obj5,obj6,obj7,obj8,obj9,obj10,obj11)
        
        if not game_over:
            # Actualiza y dibuja el texto del temporizador
            timer_text = font.render(f"Time: {max(int(time_remaining), 0)}", True, (255, 0, 0))
            text_rect = timer_text.get_rect(topright=(SCREEN_WIDTH - 10, 10))
            Screen.blit(timer_text, text_rect)
    
        # Verificar si el tiempo ha llegado a 0
        if time_remaining <= 0 and not game_over:

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

            # Mostrar "Game Over"
            game_over_text = font.render("Game Over", True, (255, 0, 0))
            game_over_text_rect = game_over_text.get_rect(center=(Screen.get_width() // 2, Screen.get_height() // 2))
            Screen.blit(game_over_text, game_over_text_rect)

            # Dibujar un botón "Reset"
            reset_button_rect = pygame.Rect(Screen.get_width() // 2 - 50, game_over_text_rect.bottom + 20, 100, 40)
            pygame.draw.rect(Screen, (0, 255, 0), reset_button_rect)
            reset_button_text = font.render("Reset", True, (255, 255, 255))
            reset_button_text_rect = reset_button_text.get_rect(center=(reset_button_rect.centerx, reset_button_rect.centery))
            Screen.blit(reset_button_text, reset_button_text_rect)

            # Dibujar un botón "Back"
            back_button_rect = pygame.Rect(Screen.get_width() // 2 - 50, reset_button_rect.bottom + 10, 100, 40)
            pygame.draw.rect(Screen, (0, 255, 0), back_button_rect)
            back_button_text = font.render("Back", True, (255, 255, 255))
            back_button_text_rect = back_button_text.get_rect(center=(back_button_rect.centerx, back_button_rect.centery))
            Screen.blit(back_button_text, back_button_text_rect)

            
        # Manejar eventos de clic en el botón de retorno
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and back_button_rect.collidepoint(event.pos):
                    # Código para volver al menú principal
                    exec(open("./main.py", "r").read(), globals()) 
                    pygame.display.update()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and reset_button_rect.collidepoint(event.pos):
                    exec(open("./pipegame.py", "r").read(), globals()) 
                    pygame.display.update()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        MyClock.tick(60)
